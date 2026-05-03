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
from typing import Dict, List, Optional

# Required sections for SKILL.md
# Required sections for SKILL.md
REQUIRED_SECTIONS = [
    "# Skill Name",
    "## Description",
    "## Activation Keywords",
    "## Tools Used",
    "## Instructions for Agents",
    "## Examples",
]

# Paper-based skills have different structure
PAPER_SKILL_INDICATORS = [
    "arXiv ID:",
    "**arXiv ID:**",
    "## Abstract",
    "## Key Contributions",
    "## Core Contributions",
    # Extended indicators for research paper skills from various sources
    "arXiv:",  # matches "arXiv:2604.xxxxx" and "Source: arXiv:..."
    "arxiv.org",  # matches arxiv.org URLs
    "source_paper:",  # matches YAML frontmatter source_paper key
    "触发词:",  # Chinese "activation keywords" hint in description
    "references:",  # YAML frontmatter references key (for paper-based skills)
    "核心论点",  # Chinese "core arguments"
    "核心贡献",  # Chinese "key contributions"
]


def is_paper_skill(content: str) -> bool:
    """Check if this is a paper-based skill (arXiv research paper)."""
    return any(indicator in content for indicator in PAPER_SKILL_INDICATORS)


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


def _parse_frontmatter(content: str) -> tuple[Optional[dict], str]:
    """Parse YAML frontmatter from markdown content.

    Returns:
        Tuple of (frontmatter_dict or None, content_without_frontmatter).
    """
    if not content.startswith("---"):
        return None, content
    end = content.find("\n---", 3)
    if end == -1:
        return None, content
    fm_text = content[3:end].strip()
    rest = content[end + 4 :]
    fm: dict = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm, rest


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
        self._frontmatter, self._body = _parse_frontmatter(content)

        # Check if this is a paper-based skill (different validation rules)
        if is_paper_skill(content):
            self.info.append(
                "Paper-based skill (arXiv research) - using relaxed validation"
            )
            return self._validate_paper_skill(content)

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

    def _validate_paper_skill(self, content: str) -> bool:
        """Validate a paper-based skill (arXiv research paper)."""
        # Paper skills need:
        # - YAML frontmatter with name and description
        # - arXiv ID
        # - Abstract or Key Contributions

        if not self._frontmatter:
            self.errors.append("Missing YAML frontmatter")
            return False

        if "name" not in self._frontmatter:
            self.errors.append("Missing 'name' in frontmatter")

        if "description" not in self._frontmatter:
            self.errors.append("Missing 'description' in frontmatter")

        # Check for arXiv ID
        if "arXiv ID:" not in content and "**arXiv ID:**" not in content:
            self.warnings.append("Missing arXiv ID")

        # Check for abstract or key contributions
        has_abstract = "## Abstract" in content
        has_contributions = "## Key Contributions" in content

        if not (has_abstract or has_contributions):
            self.warnings.append("Missing Abstract or Key Contributions section")

        # Check format (line length)
        self._check_format(content)

        return len(self.errors) == 0

    def _check_sections(self, content: str) -> None:
        """Check for required sections."""
        # Extract all markdown headers (text after the # markers)
        headers = re.findall(r"^#{1,6}\s+(.+)$", content, re.MULTILINE)
        found_sections = set(headers)

        # Build a set of lowercase header texts for lookup
        headers_lower = {h.lower() for h in found_sections}

        # Frontmatter keys available as fallback sources
        fm = self._frontmatter or {}
        fm_keys_lower = {k.lower() for k in fm}

        def _section_present(required: str) -> bool:
            """Check if a required section is satisfied by markdown or frontmatter."""
            # Strip leading '#' and whitespace to get the bare section name
            pattern = re.sub(r"^#+\s*", "", required).lower()

            # Special case: '# Skill Name' → any H1 header is acceptable
            if required == "# Skill Name":
                has_h1 = any(re.match(r"^#\s", line) for line in content.splitlines())
                if has_h1:
                    return True
                # fallback: frontmatter 'name' field
                return "name" in fm_keys_lower

            # Check markdown headers
            if any(pattern in h for h in headers_lower):
                return True

            # Fallback: check YAML frontmatter keys
            # e.g. 'description' satisfies '## Description'
            if pattern.replace(" ", "_") in fm_keys_lower or pattern in fm_keys_lower:
                return True

            return False

        # Check required sections
        for required in REQUIRED_SECTIONS:
            if not _section_present(required):
                self.errors.append(f"Missing required section: {required}")

        # Report optional sections found
        for optional in OPTIONAL_SECTIONS:
            optional_pattern = re.sub(r"^#+\s*", "", optional).lower()
            if any(optional_pattern in h for h in headers_lower):
                self.info.append(f"Has optional section: {optional}")

    def _check_format(self, content: str) -> None:
        """Check format compliance."""
        lines = content.split("\n")

        # Check for very long lines
        for i, line in enumerate(lines, 1):
            if len(line) > 120:
                self.warnings.append(
                    f"Line {i} exceeds 120 characters ({len(line)} chars)"
                )

        # Check for proper code blocks
        code_blocks = re.findall(r"```(\w*)", content)
        if not code_blocks:
            self.warnings.append("No code blocks found - examples may need code blocks")

    def _check_activation_keywords(self, content: str) -> None:
        """Check activation keywords section."""
        # Find Activation Keywords section
        match = re.search(
            r"## Activation Keywords\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL
        )
        if not match:
            return

        keywords_text = match.group(1)
        keywords = re.findall(r"^-\s*(.+)$", keywords_text, re.MULTILINE)

        if len(keywords) < 3:
            self.warnings.append(
                f"Only {len(keywords)} activation keywords - recommend 5-10"
            )

        # Check for common pitfalls
        generic_keywords = ["help", "do", "make", "create", "get"]
        for kw in keywords:
            kw_lower = kw.strip().lower()
            if kw_lower in generic_keywords:
                self.errors.append(
                    f"Too generic keyword: '{kw}' - use specific phrases"
                )

        # Check for variety
        if len(keywords) > 0:
            has_chinese = any(re.search(r"[\u4e00-\u9fff]", kw) for kw in keywords)
            has_english = any(re.search(r"[a-zA-Z]", kw) for kw in keywords)

            if not has_chinese and not has_english:
                self.warnings.append(
                    "Consider adding both Chinese and English keywords"
                )

    def _check_tools(self, content: str) -> None:
        """Check Tools Used section."""
        match = re.search(r"## Tools Used\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
        if not match:
            return

        tools_text = match.group(1)
        # Support multiple formats:
        # - `exec`
        # - exec
        # - **exec**: description
        tools = re.findall(
            r"^-\s*(?:`(\w+)`|(\*\*\w+\*\*)|(\w+))", tools_text, re.MULTILINE
        )
        tools = [t[0] or t[1].strip("*") if t[1] else t[2] for t in tools if any(t)]

        if len(tools) == 0:
            self.errors.append("No tools listed in Tools Used section")

        valid_tools = [
            "exec",
            "read",
            "write",
            "edit",
            "glob",
            "grep",
            "memory",
            "memory_search",
            "memory_get",
            "web_search",
            "web_fetch",
            "bash",
            "browser",
            "sessions_spawn",
            "sessions_list",
            "sessions_send",
            "agents_list",
            "chat",
            "read_file",
            "write_file",
        ]

        for tool in tools:
            if tool.lower() not in [v.lower() for v in valid_tools]:
                self.warnings.append(f"Uncommon tool: '{tool}' - verify it's valid")

    def _check_examples(self, content: str) -> None:
        """Check Examples section."""
        match = re.search(r"## Examples\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
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

        # Skip parent directories that only contain sub-skills
        # (e.g., systems-engineering with cps-resilience-roadmap, soft-control-multi-agent)
        skill_md = skill_path / "SKILL.md"
        if not skill_md.exists():
            # Check if this is a parent directory with sub-skills
            subdirs = [d for d in skill_path.iterdir() if d.is_dir()]
            if subdirs and all((d / "SKILL.md").exists() for d in subdirs):
                print(
                    f"⏭️  Skipping parent directory with sub-skills: {skill_path.name}"
                )
                continue

        validator = SkillValidator(skill_path)
        validator.validate()
        validators[skill_path.name] = validator

    return validators


def main():
    parser = argparse.ArgumentParser(description="Validate OpenClaw skills")
    parser.add_argument(
        "--skill", type=str, help="Specific skill to validate (default: all skills)"
    )
    parser.add_argument(
        "--fix", action="store_true", help="Auto-fix issues if possible (experimental)"
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
