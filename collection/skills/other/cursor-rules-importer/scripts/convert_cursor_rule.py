#!/usr/bin/env python3
"""
Convert cursor.directory rules to AgentSkills format.

Usage:
    python convert_cursor_rule.py --url "https://cursor.directory/react-component-catalog" --output ./skills/
    python convert_cursor_rule.py --input rule.md --output ./skills/
    python convert_cursor_rule.py --batch typescript --output ./skills/
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional
from dataclasses import dataclass


@dataclass
class CursorRule:
    """Represents a cursor.directory rule."""

    name: str
    slug: str
    content: str
    category: Optional[str] = None
    tags: list[str] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []


@dataclass
class AgentSkill:
    """Represents an AgentSkill."""

    name: str
    description: str
    content: str
    version: str = "1.0.0"


def sanitize_name(name: str) -> str:
    """Convert name to valid skill name (lowercase, hyphens only)."""
    # Remove common suffixes
    name = re.sub(r"-cursor-rules?$", "", name, flags=re.IGNORECASE)
    name = re.sub(r"-development$", "", name, flags=re.IGNORECASE)

    # Convert to lowercase and replace spaces/underscores with hyphens
    name = name.lower()
    name = re.sub(r"[\s_]+", "-", name)
    name = re.sub(r"[^a-z0-9-]", "", name)
    name = re.sub(r"-+", "-", name)
    name = name.strip("-")

    return name


def extract_expert_domain(content: str) -> str:
    """Extract the expert domain from the first line."""
    lines = content.strip().split("\n")
    if lines:
        first_line = lines[0]
        # Pattern: "You are an expert in X."
        match = re.match(
            r"You are an? (?:expert|senior) (?:in|developer|programmer)?\s*(.+?)(?:\.|,|$)",
            first_line,
            re.IGNORECASE,
        )
        if match:
            return match.group(1).strip()
    return "software development"


def extract_keywords(content: str) -> list[str]:
    """Extract keywords from content for triggering."""
    keywords = []

    # Common technology keywords
    tech_patterns = [
        r"\b(React|TypeScript|JavaScript|Python|Next\.js|Node\.js|Vue|Angular|Svelte)\b",
        r"\b(Electron|Expo|React Native|Flutter|Swift|Kotlin|Rust|Go)\b",
        r"\b(Tailwind|CSS|HTML|Sass|SCSS)\b",
        r"\b(Chrome Extension|Browser Extension|Firefox Add-on)\b",
        r"\b(Accessibility|WCAG|A11y|ARIA)\b",
        r"\b(Component|Hook|State|Props|Effect)\b",
    ]

    for pattern in tech_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        for match in matches:
            keyword = match.lower()
            if keyword not in keywords:
                keywords.append(keyword)

    return keywords[:10]  # Limit to 10 keywords


def extract_tasks(content: str) -> list[str]:
    """Extract common tasks from content."""
    tasks = []

    # Look for section headers that indicate tasks
    task_sections = re.findall(r"##\s+([A-Z][A-Za-z\s]+)", content)

    for section in task_sections:
        section_lower = section.lower()
        if any(
            word in section_lower
            for word in ["test", "debug", "build", "deploy", "security", "performance"]
        ):
            tasks.append(section_lower)

    return tasks[:5]


def generate_description(rule: CursorRule) -> str:
    """Generate a description for the skill."""
    domain = extract_expert_domain(rule.content)
    keywords = extract_keywords(rule.content)
    tasks = extract_tasks(rule.content)

    # Build description
    parts = [f"Expert guidance for {domain}."]

    if tasks:
        tasks_str = ", ".join(tasks[:3])
        parts.append(f"Use when {tasks_str}.")

    if keywords:
        keywords_str = ", ".join(keywords[:5])
        parts.append(f"Triggers on: {keywords_str}.")

    return " ".join(parts)


def convert_content(content: str) -> str:
    """Convert cursor rule content to skill content."""
    lines = content.strip().split("\n")

    # Remove the first "You are an expert..." line
    if lines and lines[0].lower().startswith("you are"):
        lines = lines[1:]

    # Clean up empty lines at the start
    while lines and not lines[0].strip():
        lines.pop(0)

    # Process sections
    processed_lines = []
    in_code_block = False

    for line in lines:
        # Track code blocks
        if line.strip().startswith("```"):
            in_code_block = not in_code_block

        # Convert section headers (ensure proper formatting)
        if line.startswith("##") and not in_code_block:
            # Ensure proper spacing
            if processed_lines and processed_lines[-1].strip():
                processed_lines.append("")
            processed_lines.append(line)
        else:
            processed_lines.append(line)

    return "\n".join(processed_lines)


def convert_rule_to_skill(rule: CursorRule) -> AgentSkill:
    """Convert a CursorRule to an AgentSkill."""
    name = sanitize_name(rule.name)
    description = generate_description(rule)
    content = convert_content(rule.content)

    return AgentSkill(name=name, description=description, content=content)


def generate_skill_file(skill: AgentSkill) -> str:
    """Generate the SKILL.md file content."""
    frontmatter = f"""---
name: {skill.name}
description: {skill.description}
---

"""

    # Add title
    title = skill.name.replace("-", " ").title()
    body = f"# {title}\n\n{skill.content}"

    return frontmatter + body


def fetch_rule_from_url(url: str) -> Optional[CursorRule]:
    """Fetch a rule from cursor.directory URL."""
    # This is a placeholder - actual implementation would use browser tool
    # or API if available
    print("Note: Direct URL fetching requires browser automation.")
    print(f"URL: {url}")
    return None


def load_rule_from_file(filepath: str) -> Optional[CursorRule]:
    """Load a rule from a local file."""
    path = Path(filepath)
    if not path.exists():
        print(f"Error: File not found: {filepath}")
        return None

    content = path.read_text(encoding="utf-8")
    name = path.stem
    slug = sanitize_name(name)

    return CursorRule(name=name, slug=slug, content=content)


def save_skill(skill: AgentSkill, output_dir: str) -> str:
    """Save a skill to the output directory."""
    skill_dir = Path(output_dir) / skill.name
    skill_dir.mkdir(parents=True, exist_ok=True)

    skill_file = skill_dir / "SKILL.md"
    content = generate_skill_file(skill)
    skill_file.write_text(content, encoding="utf-8")

    print(f"✅ Created: {skill_file}")
    return str(skill_file)


def main():
    parser = argparse.ArgumentParser(
        description="Convert cursor.directory rules to AgentSkills format"
    )
    parser.add_argument("--url", help="URL of the cursor rule")
    parser.add_argument("--input", "-i", help="Path to local rule file")
    parser.add_argument("--output", "-o", default="./skills/", help="Output directory")
    parser.add_argument("--name", help="Override skill name")
    parser.add_argument(
        "--batch", help="Batch import a category (e.g., typescript, react)"
    )

    args = parser.parse_args()

    # Ensure output directory exists
    Path(args.output).mkdir(parents=True, exist_ok=True)

    rule = None

    if args.input:
        rule = load_rule_from_file(args.input)
    elif args.url:
        rule = fetch_rule_from_url(args.url)
    else:
        parser.print_help()
        return 1

    if not rule:
        print("Error: Could not load rule")
        return 1

    # Override name if provided
    if args.name:
        rule.name = args.name

    # Convert and save
    skill = convert_rule_to_skill(rule)
    save_skill(skill, args.output)

    print("\n📋 Skill Details:")
    print(f"   Name: {skill.name}")
    print(f"   Description: {skill.description[:100]}...")

    return 0


if __name__ == "__main__":
    sys.exit(main())
