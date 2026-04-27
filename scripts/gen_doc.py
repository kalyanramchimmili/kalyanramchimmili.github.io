"""Generate Markdown docs from LeetCode solutions in solutions/."""

import ast
import os
import sys
from pathlib import Path

import google.generativeai as genai

SOLUTIONS_DIR = Path("solutions")
DOCS_DIR = Path("docs/leetcode")

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


def generate(name: str, docstring: str, code: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(
        PROMPT.format(filename=name, docstring=docstring, code=code)
    )
    return response.text.strip()


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("GEMINI_API_KEY not set")
    genai.configure(api_key=api_key)

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    written = 0

    for py in sorted(SOLUTIONS_DIR.glob("*.py")):
        md = DOCS_DIR / f"{py.stem}.md"
        if md.exists():
            print(f"skip  {py.name}  (already documented)")
            continue
        docstring, code = extract(py)
        markdown = generate(py.stem, docstring, code)
        md.write_text(markdown + "\n")
        written += 1
        print(f"wrote {md}")

    print(f"\n{written} new file(s) generated")


if __name__ == "__main__":
    main()
