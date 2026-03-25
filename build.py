#!/usr/bin/env python3
"""Build SKILL.md files from templates by inlining instruction references.

Templates use {{path/to/file.md}} to include instruction file contents.
Paths are relative to the repository root.
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
INCLUDE_PATTERN = re.compile(r"\{\{(.+?)\}\}")


def build_skill(template_path: Path) -> str:
    template = template_path.read_text()

    def replace_include(match):
        rel_path = match.group(1).strip()
        include_path = REPO_ROOT / rel_path
        if not include_path.exists():
            print(f"Error: {include_path} not found (referenced in {template_path})", file=sys.stderr)
            sys.exit(1)
        return include_path.read_text().rstrip()

    return INCLUDE_PATTERN.sub(replace_include, template)


def main():
    templates = list(REPO_ROOT.rglob("SKILL.md.template"))
    if not templates:
        print("No SKILL.md.template files found.", file=sys.stderr)
        return 1

    for template_path in templates:
        output_path = template_path.with_name("SKILL.md")
        result = build_skill(template_path)
        output_path.write_text(result)
        print(f"Built {output_path.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
