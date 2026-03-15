#!/usr/bin/env python3
"""
Fix missing required sections in SKILL.md files.

Adds placeholder sections for:
- Activation Keywords
- Tools Used
- Instructions for Agents
- Examples
"""

import re
from pathlib import Path

REQUIRED_SECTIONS = {
    "Activation Keywords": """## Activation Keywords

- `<skill-name>`
- `<keyword-1>`
- `<keyword-2>`
""",
    "Tools Used": """## Tools Used

- `exec`
- `read`
- `write`
- `edit`
""",
    "Instructions for Agents": """## Instructions for Agents

1. Read the task description carefully
2. Follow the step-by-step process
3. Use the appropriate tools
4. Verify the results
""",
    "Examples": """## Examples

### Example 1: Basic Usage

**User:** <example user request>

**Agent:** <example agent response>

### Example 2: Advanced Usage

**User:** <example user request>

**Agent:** <example agent response>
""",
}


def fix_skill_md(skill_path: Path) -> bool:
    """Fix missing sections in a SKILL.md file."""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False

    content = skill_md.read_text(encoding="utf-8")
    original = content
    skill_name = skill_path.name

    # Check and add each required section
    for section_name, section_content in REQUIRED_SECTIONS.items():
        pattern = rf"^## {section_name}"
        if not re.search(pattern, content, re.MULTILINE):
            # Customize the section for this skill
            customized = section_content.replace("<skill-name>", skill_name)
            customized = customized.replace("<keyword-1>", f"{skill_name}")
            customized = customized.replace("<keyword-2>", f"{skill_name.replace('-', ' ')}")

            # Find the best place to insert (after last ## section or at end)
            sections = list(re.finditer(r"^## .+", content, re.MULTILINE))
            if sections:
                last_section = sections[-1]
                # Find the end of the last section's content
                next_section = re.search(
                    r"^## ",
                    content[last_section.end() :],
                    re.MULTILINE,
                )
                if next_section:
                    insert_pos = last_section.end() + next_section.start()
                else:
                    insert_pos = len(content)
                content = content[:insert_pos] + "\n" + customized + content[insert_pos:]
            else:
                content = content + "\n" + customized

    if content != original:
        skill_md.write_text(content, encoding="utf-8")
        print(f"Fixed: {skill_name}")
        return True
    return False


def main():
    skills_dir = Path(__file__).parent.parent / "collection" / "skills"

    fixed = 0
    for skill_path in sorted(skills_dir.iterdir()):
        if skill_path.is_dir() and (skill_path / "SKILL.md").exists():
            if fix_skill_md(skill_path):
                fixed += 1

    print(f"\nFixed {fixed} skills")


if __name__ == "__main__":
    main()