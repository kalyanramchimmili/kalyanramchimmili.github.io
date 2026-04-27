"""Generate Markdown docs from LeetCode solutions in solutions/."""

import ast
import os
import sys
import time
from pathlib import Path

from google import genai
from google.genai import errors as genai_errors

SOLUTIONS_DIR = Path("solutions")
DOCS_DIR = Path("docs/leetcode")
MODEL = "gemini-2.5-flash"
MAX_RETRIES = 4

PROMPT = """You are documenting a LeetCode solution for a personal Docusaurus portfolio.

The author wrote their approach in the module docstring and the Python code below it.

Produce a clean Markdown file with:

- YAML frontmatter: `title` (Title Case from filename), `tags` (array of relevant DSA categories)
- `# Problem Name`
- `## Approach` — rewrite the docstring more polished, keep the author's intent
- `## Solution` — the code in a ```python fenced block
- `## Complexity` — Time and Space, derived from the approach

Return ONLY the markdown. No preamble, no wrapping code fences.

---
Filename: {filename}

Docstring:
{docstring}

Code:
{code}
"""


def extract(path: Path) -> tuple[str, str]:
    source = path.read_text()
    tree = ast.parse(source)
    return ast.get_docstring(tree) or "", source


def generate(client: genai.Client, name: str, docstring: str, code: str) -> str:
    prompt = PROMPT.format(filename=name, docstring=docstring, code=code)
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
    raise RuntimeError(f"giving up on {name} after {MAX_RETRIES} retries")


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("GEMINI_API_KEY not set")
    client = genai.Client(api_key=api_key)

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    written = 0

    for py in sorted(SOLUTIONS_DIR.glob("*.py")):
        md = DOCS_DIR / f"{py.stem}.md"
        if md.exists():
            print(f"skip  {py.name}  (already documented)")
            continue
        docstring, code = extract(py)
        markdown = generate(client, py.stem, docstring, code)
        md.write_text(markdown + "\n")
        written += 1
        print(f"wrote {md}")

    print(f"\n{written} new file(s) generated")


if __name__ == "__main__":
    main()
