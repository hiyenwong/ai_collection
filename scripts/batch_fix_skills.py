#!/usr/bin/env python3
"""
Batch fix missing required sections in SKILL.md files.

This script automatically adds placeholder sections for:
- ## Activation Keywords
- ## Tools Used
- ## Instructions for Agents
- ## Examples
- ## Description (if missing in both frontmatter and body)

Usage:
    python scripts/batch_fix_skills.py
"""

import re
import sys
from pathlib import Path
from typing import List, Optional

# Required sections
REQUIRED_SECTIONS = [
    ("## Description", "description"),
    ("## Activation Keywords", "activation_keywords"),
    ("## Tools Used", "tools_used"),
    ("## Instructions for Agents", "instructions"),
    ("## Examples", "examples"),
]

# Default content for each section
DEFAULT_CONTENT = {
    "description": """Framework from arXiv papers. See paper reference for details.""",
    "activation_keywords": """
- {skill_name}
- {skill_name} 技能
- {skill_name} skill
""",
    "tools_used": """
- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation
""",
    "instructions": """
1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.
""",
    "examples": """
### Example 1: Basic Usage

**User:** How can I apply {skill_name}?

**Agent:** I'll help you understand and apply {skill_name}...

### Example 2: Advanced Application

**User:** What are the key considerations for {skill_name}?

**Agent:** Let me search for the latest research and best practices...
""",
}


def _parse_frontmatter(content: str) -> tuple[Optional[dict], str, int]:
    """Parse YAML frontmatter from markdown content.

    Returns:
        Tuple of (frontmatter_dict or None, content_without_frontmatter, frontmatter_end_line).
    """
    if not content.startswith("---"):
        return None, content, 0

    end = content.find("\n---", 3)
    if end == -1:
        return None, content, 0

    fm_text = content[3:end].strip()
    rest = content[end + 4 :]

    # Calculate frontmatter end line
    fm_lines = content[: end + 4].split("\n")
    fm_end_line = len(fm_lines)

    fm: dict = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            # Handle quoted values and inline JSON
            val = val.strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            fm[key.strip()] = val

    return fm, rest, fm_end_line


def _find_section_position(content: str, section_name: str) -> Optional[int]:
    """Find the line position where a section starts."""
    pattern = re.compile(rf"^{re.escape(section_name)}\s*$", re.MULTILINE)
    match = pattern.search(content)
    if match:
        return content[:match.start()].count("\n") + 1
    return None


def _find_last_section_position(content: str) -> int:
    """Find the position after the last ## section."""
    # Find all ## headers
    headers = re.findall(r"^##\s+.+$", content, re.MULTILINE)
    if not headers:
        return 0

    # Find the last header position
    last_header = headers[-1]
    pattern = re.compile(rf"^{re.escape(last_header)}\s*$", re.MULTILINE)
    match = pattern.search(content)

    if match:
        # Find the content after the last section
        rest = content[match.end() :]
        # Find where this section's content ends (next ## or end of file)
        next_section = re.search(r"\n##", rest)
        if next_section:
            return match.end() + next_section.start()
        else:
            return len(content)

    return len(content)


def fix_skill(skill_path: Path) -> bool:
    """Fix missing sections in a skill. Returns True if changes were made."""
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        return False

    content = skill_md.read_text(encoding="utf-8")
    original_content = content

    frontmatter, body, fm_end_line = _parse_frontmatter(content)
    skill_name = skill_path.name

    # Check which sections are missing
    missing_sections: List[str] = []

    # Check Description
    has_description_in_body = _find_section_position(body, "## Description") is not None
    has_description_in_fm = frontmatter and "description" in frontmatter

    if not has_description_in_body and not has_description_in_fm:
        missing_sections.append("## Description")

    # Check other sections (must be in body)
    for section, key in REQUIRED_SECTIONS[1:]:  # Skip Description
        if _find_section_position(body, section) is None:
            missing_sections.append(section)

    if not missing_sections:
        return False

    # Add missing sections
    # Find a good position to insert (after the main content, before Resources/Notes/etc.)
    insert_positions = []

    # Determine insertion order and positions
    # We want to insert sections in the correct order

    # First, rebuild the body with sections in correct order
    sections_to_add = []

    for section, key in REQUIRED_SECTIONS:
        if section in missing_sections:
            content_template = DEFAULT_CONTENT[key]
            # Replace placeholders
            section_content = content_template.format(skill_name=skill_name)
            sections_to_add.append(f"\n{section}\n{section_content}")

    # Find insertion point: after existing sections but before Resources/Notes
    optional_sections_pattern = r"\n(## Resources|## Notes|## References|## Related Skills|## Limitations)"
    optional_match = re.search(optional_sections_pattern, body)

    if optional_match:
        insert_pos = optional_match.start()
        # Insert before optional sections
        new_body = body[:insert_pos] + "".join(sections_to_add) + body[insert_pos:]
    else:
        # Insert at the end
        new_body = body + "".join(sections_to_add)

    # Reconstruct the full content
    if frontmatter:
        # Rebuild frontmatter
        fm_lines = []
        for key, val in frontmatter.items():
            if isinstance(val, str) and len(val) > 50:
                fm_lines.append(f"{key}: '{val}'")
            else:
                fm_lines.append(f"{key}: {val}")

        new_content = "---\n" + "\n".join(fm_lines) + "\n---\n" + new_body
    else:
        new_content = new_body

    # Clean up extra whitespace
    new_content = re.sub(r"\n{3,}", "\n\n", new_content)

    if new_content != original_content:
        skill_md.write_text(new_content, encoding="utf-8")
        print(f"✅ Fixed: {skill_name} (added: {', '.join(missing_sections)})")
        return True

    return False


def main():
    """Fix all skills with missing sections."""
    script_dir = Path(__file__).parent
    skills_dir = script_dir.parent / "collection" / "skills"

    if not skills_dir.exists():
        print(f"❌ Skills directory not found: {skills_dir}")
        sys.exit(1)

    print("🔧 Batch fixing skills with missing sections...\n")

    fixed_count = 0
    skipped_count = 0

    # Get list of skills to fix from validation output
    import subprocess

    # Run validation to get failed skills
    result = subprocess.run(
        ["python3", str(script_dir / "validate_skill.py")],
        capture_output=True,
        text=True,
    )

    # Extract failed skill names
    failed_skills = []
    lines = result.stdout.split("\n")
    current_skill = None

    for line in lines:
        if "Validating:" in line:
            current_skill = line.split("Validating:")[1].strip()
        elif "❌ Errors:" in line and current_skill:
            failed_skills.append(current_skill)
            current_skill = None

    # Fix each failed skill
    for skill_name in sorted(failed_skills):
        skill_path = skills_dir / skill_name
        if skill_path.exists():
            if fix_skill(skill_path):
                fixed_count += 1
            else:
                skipped_count += 1
        else:
            print(f"⚠️  Skill directory not found: {skill_name}")

    print(f"\n{'='*50}")
    print(f"Summary: Fixed {fixed_count} skills, skipped {skipped_count}")

    # Re-run validation
    print("\n🔍 Re-running validation...")
    result = subprocess.run(
        ["python3", str(script_dir / "validate_skill.py")],
        capture_output=True,
        text=True,
    )

    # Print summary
    summary_match = re.search(r"Summary: (\d+)/(\d+) skills valid", result.stdout)
    if summary_match:
        valid, total = summary_match.groups()
        print(f"Final: {valid}/{total} skills valid")

    if "✅ All skills are valid!" in result.stdout:
        print("✅ All skills are now valid!")
        sys.exit(0)
    else:
        print("⚠️  Some skills still have issues. Check validation output.")
        sys.exit(1)


if __name__ == "__main__":
    main()