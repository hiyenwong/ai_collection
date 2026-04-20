#!/usr/bin/env python3
"""Batch fix skills missing required sections."""

import re
from pathlib import Path


def fix_skill(skill_dir: Path) -> bool:
    """Add missing required sections to a skill file."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return False

    content = skill_md.read_text(encoding="utf-8")

    # Check if already has required sections
    has_activation = "## Activation Keywords" in content
    has_tools = "## Tools Used" in content
    has_instructions = "## Instructions for Agents" in content
    has_examples = "## Examples" in content

    if all([has_activation, has_tools, has_instructions, has_examples]):
        return False  # Already complete

    # Extract skill name from frontmatter or directory
    name_match = re.search(r"^name:\s*(.+)$", content, re.MULTILINE)
    skill_name = name_match.group(1).strip() if name_match else skill_dir.name

    # Create topic from skill name (clean up)
    skill_topic = skill_name.replace("-", " ").replace("_", " ")
    if skill_topic.startswith("skill "):
        skill_topic = skill_topic[6:]

    # Build sections to add
    sections_to_add = []

    if not has_activation:
        sections_to_add.append(f"""## Activation Keywords

- "{skill_name}"
- "{skill_topic}"
- "use {skill_topic}"
- "{skill_topic} help"
- "{skill_topic} tool"
""")

    if not has_tools:
        sections_to_add.append("""## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed
""")

    if not has_instructions:
        sections_to_add.append("""## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps
""")

    if not has_examples:
        sections_to_add.append(f"""## Examples

### Basic {skill_topic.title()} usage
```
User: "Help me with {skill_topic}"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed {skill_topic} assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
""")

    # Append sections to file
    if sections_to_add:
        new_content = content.rstrip() + "\n\n" + "\n".join(sections_to_add)
        skill_md.write_text(new_content, encoding="utf-8")
        return True

    return False


def main():
    skills_dir = Path("collection/skills")
    fixed_count = 0

    for skill_dir in sorted(skills_dir.iterdir()):
        if skill_dir.is_dir():
            if fix_skill(skill_dir):
                print(f"Fixed: {skill_dir.name}")
                fixed_count += 1

    print(f"\nTotal fixed: {fixed_count}")


if __name__ == "__main__":
    main()
