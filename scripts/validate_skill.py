#!/usr/bin/env python3
"""
Skill Validation Script

Validates SKILL.md files against the project specification.
Checks for required sections, format compliance, and completeness.

Usage:
    python validate_skill.py                    # Validate all skills
    python validate_skill.py --skill stock-analysis  # Validate specific skill
    python validate_skill.py --fix               # Auto-fix issues if possible
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Required sections for SKILL.md
REQUIRED_SECTIONS = [
    "# Skill Name",
    "## Description",
    "## Activation Keywords",
    "## Tools Used",
    "## Instructions for Agents",
    "## Examples",
]

# Optional sections
OPTIONAL_SECTIONS = [
    "## Installation",
    "## Usage Patterns",
    "## Context Files",
    "## Error Handling",
    "## Configuration",
    "## Advanced Features",
    "## Best Practices",
    "## Limitations",
    "## Resources",
    "## Related Skills",
    "## Notes",
    "## Troubleshooting",
]


class SkillValidator:
    """Validator for SKILL.md files."""

    def __init__(self, skill_path: Path):
        self.skill_path = skill_path
        self.skill_md = skill_path / "SKILL.md"
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []

    def validate(self) -> bool:
        """Validate the skill. Returns True if valid."""
        if not self.skill_md.exists():
            self.errors.append(f"SKILL.md not found at {self.skill_md}")
            return False

        content = self.skill_md.read_text(encoding="utf-8")

        # Check required sections
        self._check_sections(content)

        # Check format
        self._check_format(content)

        # Check activation keywords
        self._check_activation_keywords(content)

        # Check tools used
        self._check_tools(content)

        # Check examples
        self._check_examples(content)

        return len(self.errors) == 0

    def _check_sections(self, content: str) -> None:
        """Check for required sections."""
        found_sections = set()

        # Extract all headers
        headers = re.findall(r'^#{1,3}\s+(.+)$', content, re.MULTILINE)
        found_sections = set(headers)

        # Check required sections
        for required in REQUIRED_SECTIONS:
            # Match loosely - just check if the section exists
            required_pattern = required.replace("# ", "").replace("## ", "")
            if not any(required_pattern.lower() in h.lower() for h in found_sections):
                self.errors.append(f"Missing required section: {required}")

        # Report optional sections found
        for optional in OPTIONAL_SECTIONS:
            optional_pattern = optional.replace("## ", "")
            if any(optional_pattern.lower() in h.lower() for h in found_sections):
                self.info.append(f"Has optional section: {optional}")

    def _check_format(self, content: str) -> None:
        """Check format compliance."""
        lines = content.split('\n')

        # Check for very long lines
        for i, line in enumerate(lines, 1):
            if len(line) > 120:
                self.warnings.append(f"Line {i} exceeds 120 characters ({len(line)} chars)")

        # Check for proper code blocks
        code_blocks = re.findall(r'```(\w*)', content)
        if not code_blocks:
            self.warnings.append("No code blocks found - examples may need code blocks")

    def _check_activation_keywords(self, content: str) -> None:
        """Check activation keywords section."""
        # Find Activation Keywords section
        match = re.search(r'## Activation Keywords\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
        if not match:
            return

        keywords_text = match.group(1)
        keywords = re.findall(r'^-\s*(.+)$', keywords_text, re.MULTILINE)

        if len(keywords) < 3:
            self.warnings.append(f"Only {len(keywords)} activation keywords - recommend 5-10")

        # Check for common pitfalls
        generic_keywords = ["help", "do", "make", "create", "get"]
        for kw in keywords:
            kw_lower = kw.strip().lower()
            if kw_lower in generic_keywords:
                self.errors.append(f"Too generic keyword: '{kw}' - use specific phrases")

        # Check for variety
        if len(keywords) > 0:
            has_chinese = any(re.search(r'[\u4e00-\u9fff]', kw) for kw in keywords)
            has_english = any(re.search(r'[a-zA-Z]', kw) for kw in keywords)

            if not has_chinese and not has_english:
                self.warnings.append("Consider adding both Chinese and English keywords")

    def _check_tools(self, content: str) -> None:
        """Check Tools Used section."""
        match = re.search(r'## Tools Used\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
        if not match:
            return

        tools_text = match.group(1)
        tools = re.findall(r'^-\s*(\w+)', tools_text, re.MULTILINE)

        if len(tools) == 0:
            self.errors.append("No tools listed in Tools Used section")

        valid_tools = [
            "exec", "read", "write", "edit", "glob", "grep",
            "memory", "web_search", "web_fetch", "bash"
        ]

        for tool in tools:
            if tool.lower() not in [v.lower() for v in valid_tools]:
                self.warnings.append(f"Uncommon tool: '{tool}' - verify it's valid")

    def _check_examples(self, content: str) -> None:
        """Check Examples section."""
        match = re.search(r'## Examples\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
        if not match:
            return

        examples_text = match.group(1)

        # Check for example blocks
        has_user = "User:" in examples_text or "用户" in examples_text
        has_agent = "Agent:" in examples_text or "代理" in examples_text

        if not (has_user and has_agent):
            self.warnings.append("Examples should show User: and Agent: interactions")

    def report(self) -> str:
        """Generate validation report."""
        lines = []
        lines.append(f"Validating: {self.skill_path.name}")
        lines.append("=" * 50)

        if self.info:
            lines.append("\n✅ Info:")
            for info in self.info:
                lines.append(f"  • {info}")

        if self.warnings:
            lines.append("\n⚠️  Warnings:")
            for warning in self.warnings:
                lines.append(f"  • {warning}")

        if self.errors:
            lines.append("\n❌ Errors:")
            for error in self.errors:
                lines.append(f"  • {error}")

        if not self.errors and not self.warnings:
            lines.append("\n✅ Skill is valid!")

        return "\n".join(lines)


def validate_all_skills(skills_dir: Path) -> Dict[str, SkillValidator]:
    """Validate all skills in the collection."""
    validators = {}

    if not skills_dir.exists():
        print(f"❌ Skills directory not found: {skills_dir}")
        return validators

    for skill_path in skills_dir.iterdir():
        if not skill_path.is_dir():
            continue

        validator = SkillValidator(skill_path)
        validator.validate()
        validators[skill_path.name] = validator

    return validators


def main():
    parser = argparse.ArgumentParser(description="Validate OpenClaw skills")
    parser.add_argument(
        "--skill",
        type=str,
        help="Specific skill to validate (default: all skills)"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Auto-fix issues if possible (experimental)"
    )

    args = parser.parse_args()

    # Find skills directory
    script_dir = Path(__file__).parent
    skills_dir = script_dir.parent / "collection" / "skills"

    if args.skill:
        # Validate specific skill
        skill_path = skills_dir / args.skill
        if not skill_path.exists():
            print(f"❌ Skill not found: {skill_path}")
            sys.exit(1)

        validator = SkillValidator(skill_path)
        validator.validate()
        print(validator.report())
        sys.exit(0 if len(validator.errors) == 0 else 1)
    else:
        # Validate all skills
        print("🔍 Validating all skills...\n")
        validators = validate_all_skills(skills_dir)

        # Print reports
        for name, validator in sorted(validators.items()):
            print(validator.report())
            print()

        # Summary
        valid = sum(1 for v in validators.values() if not v.errors)
        total = len(validators)

        print("=" * 50)
        print(f"Summary: {valid}/{total} skills valid")

        if valid < total:
            print("\n⚠️  Some skills have issues. Please review above.")
            sys.exit(1)
        else:
            print("\n✅ All skills are valid!")
            sys.exit(0)


if __name__ == "__main__":
    main()
