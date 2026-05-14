"""Generate Markdown docs from LeetHub-pushed solutions.

Walks <SOLUTIONS_DIR>/<NNNN>-<slug>/ folders (the layout LeetHub creates) and
produces docs/leetcode/<NNNN>-<slug>.md. Each problem folder is expected to
contain README.md (problem statement) and a solution file matching the folder
name (e.g. 0001-two-sum.py).

Approach text is sourced from, in order of preference:
  1. The Python module docstring at the top of the .py file (preferred)
  2. NOTES.md, if LeetHub managed to push one
  3. Inferred by the model from the code itself (flagged in the output)

Set LEETCODE_SOLUTIONS_PATH to point at a checked-out LeetHub repo; defaults to
./solutions for local runs.
"""

import ast
import os
import sys
import time
from pathlib import Path

from google import genai
from google.genai import errors as genai_errors

SOLUTIONS_DIR = Path(os.environ.get("LEETCODE_SOLUTIONS_PATH", "solutions"))
DOCS_DIR = Path("docs/leetcode")
MODEL = "gemini-2.5-flash-lite"
MAX_RETRIES = 4

LANG_BY_EXT = {
    ".py": "python",
    ".cpp": "cpp",
    ".c": "c",
    ".go": "go"
}

PROMPT = """You are documenting a LeetCode solution for a personal Docusaurus portfolio.

Inputs:
- The LeetCode problem statement (from LeetHub's README.md, may include HTML)
- The author's approach notes (from a Python module docstring or NOTES.md — may be empty)
- The solution code

Produce a Markdown file with this EXACT structure (note the literal `---` delimiters for the frontmatter — do NOT wrap them in a yaml code fence):

---
title: Problem Name In Title Case
tags: [Arrays, Hashing]
---

# Problem Name

## Problem

2-3 sentence paraphrase of the problem. Do NOT copy LeetCode's full text verbatim and do NOT include HTML.

## Approach

Polish the author's notes into clear prose, keeping their intent and voice. Don't add details the author didn't say. If the notes are empty or trivial, write a short approach summary inferred from the code and prepend the line `_(approach inferred from code — author notes were empty)_`.

## Solution

```{lang}
<the code, exactly as-is — keep the docstring at the top if present>
```

## Complexity

- **Time:** O(...) — short explanation
- **Space:** O(...) — short explanation

Return ONLY the markdown content starting with `---`. No preamble, no wrapping ```markdown fences.

---
Problem slug: {slug}
Language: {lang}

Problem statement (from LeetCode):
{readme}

Author notes:
{notes}

Code:
{code}
"""


def extract_python_docstring(code: str) -> str:
    """Return the module-level docstring from Python source, or empty string."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return ""
    return ast.get_docstring(tree) or ""


def collect(folder: Path) -> tuple[str, str, str, str, str] | None:
    """Return (slug, lang, readme, notes, code) or None if no solution file."""
    slug = folder.name
    readme = (folder / "README.md").read_text() if (folder / "README.md").exists() else ""

    code_file = next(
        (folder / f"{slug}{ext}" for ext in LANG_BY_EXT if (folder / f"{slug}{ext}").exists()),
        None,
    )
    if code_file is None:
        for f in folder.iterdir():
            if f.suffix in LANG_BY_EXT:
                code_file = f
                break
    if code_file is None:
        return None

    code = code_file.read_text()
    lang = LANG_BY_EXT[code_file.suffix]

    notes = ""
    if lang == "python":
        notes = extract_python_docstring(code)
    if not notes and (folder / "NOTES.md").exists():
        notes = (folder / "NOTES.md").read_text()

    return slug, lang, readme, notes, code


def generate(client: genai.Client, slug: str, lang: str, readme: str, notes: str, code: str) -> str:
    prompt = PROMPT.format(
        slug=slug,
        lang=lang,
        readme=readme or "(no README)",
        notes=notes or "(empty)",
        code=code,
    )
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(model=MODEL, contents=prompt)
            return response.text.strip()
        except genai_errors.APIError as e:
            status = getattr(e, "status_code", None)
            if status not in (429, 500, 502, 503, 504):
                raise
            wait = 2 ** attempt * 15
            print(f"transient {status} (attempt {attempt}); sleeping {wait}s")
            time.sleep(wait)
    raise RuntimeError(f"giving up on {slug} after {MAX_RETRIES} retries")


def is_problem_folder(p: Path) -> bool:
    if not p.is_dir():
        return False
    head, _, _ = p.name.partition("-")
    return head.isdigit() and len(head) >= 1


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("GEMINI_API_KEY not set")
    if not SOLUTIONS_DIR.exists():
        sys.exit(f"solutions path not found: {SOLUTIONS_DIR}")

    client = genai.Client(api_key=api_key)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    written = 0

    for folder in sorted(SOLUTIONS_DIR.iterdir()):
        if not is_problem_folder(folder):
            continue

        out = DOCS_DIR / f"{folder.name}.md"
        if out.exists():
            print(f"skip  {folder.name}  (already documented)")
            continue

        result = collect(folder)
        if result is None:
            print(f"skip  {folder.name}  (no solution file)")
            continue

        slug, lang, readme, notes, code = result
        source = "docstring" if lang == "python" and notes else ("NOTES.md" if notes else "(none — will infer)")
        print(f"gen   {folder.name}  (approach source: {source})")
        markdown = generate(client, slug, lang, readme, notes, code)
        out.write_text(markdown + "\n")
        written += 1
        print(f"wrote {out}")

    print(f"\n{written} new file(s) generated")


if __name__ == "__main__":
    main()
