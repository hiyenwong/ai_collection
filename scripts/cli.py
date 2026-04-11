#!/usr/bin/env python3
"""OpenClaw Collection CLI - Scaffolding tool for creating agents and skills.

Usage:
    python scripts/cli.py create agent <name> [--purpose <desc>] [--model <model>]
    python scripts/cli.py create skill <name> [--description <desc>] [--keywords kw1,kw2]
    python scripts/cli.py list agents [--category <cat>]
    python scripts/cli.py list skills [--category <cat>]
    python scripts/cli.py scan [--json] [-o <file>]
    python scripts/cli.py validate [--skill <name>]

Examples:
    python scripts/cli.py create agent devops-engineer --purpose "DevOps and infrastructure"
    python scripts/cli.py create skill k8s-deploy --keywords "kubernetes,deploy,k8s"
    python scripts/cli.py list skills --category finance
    python scripts/cli.py scan
    python scripts/cli.py validate --skill stock-analysis
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Resolve project root (two levels up from scripts/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
COLLECTION_DIR = PROJECT_ROOT / "collection"
AGENTS_DIR = COLLECTION_DIR / "agents"
SKILLS_DIR = COLLECTION_DIR / "skills"
TEMPLATES_DIR = PROJECT_ROOT / "templates"

AGENT_TEMPLATE = TEMPLATES_DIR / "agent-template.md"
SKILL_TEMPLATE = TEMPLATES_DIR / "skill-template.md"

VALID_TOOLS = [
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
]


def _title_case(name: str) -> str:
    """Convert kebab-case to Title Case."""
    return " ".join(word.capitalize() for word in name.split("-"))


def _slug_exists(base_dir: Path, name: str) -> bool:
    """Check if an agent/skill with this name already exists."""
    return (base_dir / name).is_dir()


def _create_subdirs(base_dir: Path, subdirs: list[str]) -> None:
    """Create optional subdirectories."""
    created: list[str] = []
    for subdir in subdirs:
        path = base_dir / subdir
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(subdir)
    if created:
        print(f"  Created directories: {', '.join(created)}")


def create_agent(
    name: str, purpose: str | None = None, model: str | None = None
) -> None:
    """Scaffold a new agent from template."""
    slug = name.lower().replace(" ", "-").strip("-")
    if _slug_exists(AGENTS_DIR, slug):
        print(f"Agent '{slug}' already exists at {AGENTS_DIR / slug}")
        sys.exit(1)

    agent_dir = AGENTS_DIR / slug
    agent_dir.mkdir(parents=True, exist_ok=True)

    # Read template
    template_content = AGENT_TEMPLATE.read_text(encoding="utf-8")
    title = _title_case(slug)

    # Fill in template
    purpose_text = purpose or f"{title} agent"
    model_primary = model or "claude-sonnet-4.5"
    model_alt = (
        "claude-opus-4.5"
        if model_primary.startswith("claude-sonnet")
        else "claude-sonnet-4.5"
    )

    content = template_content.replace("[Agent Name]", title)
    content = content.replace(
        "[Clear, concise description of what this agent does and why it exists]",
        purpose_text,
    )
    content = content.replace("[Default model, e.g., claude-sonnet-4.5]", model_primary)
    content = content.replace("[Alternative model, optional]", model_alt)
    content = content.replace("[agent-id]", slug)

    # Replace remaining placeholders with guidance comments
    content = re.sub(
        r"\[tool\d\]: \[Description of usage\]", "# TODO: add tools", content
    )
    content = re.sub(r"\[skill\d\]: \[Description\]", "# TODO: add skills", content)

    # Write AGENT.md
    agent_md = agent_dir / "AGENT.md"
    agent_md.write_text(content, encoding="utf-8")

    # Create optional subdirectories
    _create_subdirs(agent_dir, ["examples", "references", "assets"])

    # Create README.md placeholder
    readme = agent_dir / "README.md"
    readme.write_text(
        f"# {title}\n\n{purpose_text}.\n\nSee [AGENT.md](./AGENT.md) for full agent definition.\n",
        encoding="utf-8",
    )

    print(f"Created agent: {slug}")
    print(f"  Directory: {agent_dir}")
    print("  Files: AGENT.md, README.md")
    print("  Subdirs: examples/, references/, assets/")
    print("\nNext steps:")
    print(f"  1. Edit {agent_md} to fill in system prompt, tools, and skills")
    print(f"  2. Add usage examples in {agent_dir / 'examples' / ''}")
    print(f"  3. Run: python scripts/cli.py validate --agent {slug}")


def create_skill(
    name: str,
    description: str | None = None,
    keywords: list[str] | None = None,
) -> None:
    """Scaffold a new skill from template."""
    slug = name.lower().replace(" ", "-").strip("-")
    if _slug_exists(SKILLS_DIR, slug):
        print(f"Skill '{slug}' already exists at {SKILLS_DIR / slug}")
        sys.exit(1)

    skill_dir = SKILLS_DIR / slug
    skill_dir.mkdir(parents=True, exist_ok=True)

    # Read template
    template_content = SKILL_TEMPLATE.read_text(encoding="utf-8")
    title = _title_case(slug)

    desc_text = description or f"{title} skill for OpenClaw agents"
    kw_list = keywords or [slug, title.lower()]
    kw_section = "\n".join(f"- {kw}" for kw in kw_list)

    content = template_content.replace("[Skill Name]", title)
    content = content.replace(
        "[Brief description (1-2 sentences) of what this skill does]",
        desc_text,
    )
    content = content.replace(
        "- [keyword1]\n- [keyword2]\n- [keyword3]",
        kw_section,
    )
    content = re.sub(
        r"\[tool\d\]: \[Description of usage\]", "# TODO: add tools", content
    )

    # Add YAML frontmatter with metadata
    frontmatter = f"""---
name: {slug}
description: "{desc_text}"
---

"""
    # Only prepend if not already present
    if not content.startswith("---"):
        content = frontmatter + content

    # Write SKILL.md
    skill_md = skill_dir / "SKILL.md"
    skill_md.write_text(content, encoding="utf-8")

    # Create optional subdirectories
    _create_subdirs(skill_dir, ["examples", "references", "scripts", "assets"])

    print(f"Created skill: {slug}")
    print(f"  Directory: {skill_dir}")
    print("  Files: SKILL.md")
    print("  Subdirs: examples/, references/, scripts/, assets/")
    print(f"  Keywords: {', '.join(kw_list)}")
    print("\nNext steps:")
    print(f"  1. Edit {skill_md} to add detailed instructions and examples")
    print(f"  2. Add reference docs in {skill_dir / 'references' / ''}")
    print(f"  3. Run: python scripts/cli.py validate --skill {slug}")


def list_agents(category: str | None = None) -> None:
    """List all agents, optionally filtered by category."""
    if not AGENTS_DIR.exists():
        print("No agents directory found.")
        return

    agents = sorted(AGENTS_DIR.iterdir())
    if not agents:
        print("No agents found.")
        return

    print(f"{'Agent':<40} {'Purpose':<50}")
    print("-" * 90)

    for agent_dir in agents:
        if not agent_dir.is_dir():
            continue
        agent_md = agent_dir / "AGENT.md"
        purpose = ""
        if agent_md.exists():
            match = re.search(
                r"## Purpose\s*\n+(.*?)(?:\n##|\Z)",
                agent_md.read_text(encoding="utf-8"),
                re.DOTALL,
            )
            if match:
                purpose = match.group(1).strip().replace("\n", " ")[:50]
        print(f"{agent_dir.name:<40} {purpose:<50}")


def list_skills(category: str | None = None) -> None:
    """List all skills, optionally filtered by category."""
    if not SKILLS_DIR.exists():
        print("No skills directory found.")
        return

    skills = sorted(SKILLS_DIR.iterdir())
    if not skills:
        print("No skills found.")
        return

    # Import scanner for categorization
    sys.path.insert(0, str(Path(__file__).parent))
    from scan_skills import classify_skill

    if category:
        filtered_count = 0
        print(f"{'Skill':<55} {'Category':<25}")
        print("-" * 80)
        for skill_dir in skills:
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            content = skill_md.read_text(encoding="utf-8")
            cat = classify_skill(skill_dir.name, content)
            if cat == category:
                print(f"{skill_dir.name:<55} {cat:<25}")
                filtered_count += 1
        print(f"\nTotal: {filtered_count} skills in '{category}'")
    else:
        # Summary by category
        from collections import Counter

        cats: Counter[str] = Counter()
        for skill_dir in skills:
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            content = skill_md.read_text(encoding="utf-8")
            cat = classify_skill(skill_dir.name, content)
            cats[cat] += 1

        print(f"{'Category':<30} {'Count':>6}")
        print("-" * 36)
        for cat, count in cats.most_common():
            print(f"{cat:<30} {count:>6}")
        print("-" * 36)
        print(f"{'Total':<30} {sum(cats.values()):>6}")


def scan_skills(json_output: bool = False, output_file: str | None = None) -> None:
    """Run skill scanner."""
    sys.path.insert(0, str(Path(__file__).parent))
    from scan_skills import scan_skills as _scan

    results = _scan(SKILLS_DIR)

    if json_output or output_file:
        output = json.dumps(results, ensure_ascii=False, indent=2)
        if output_file:
            Path(output_file).write_text(output, encoding="utf-8")
            print(f"Written {len(results)} skills to {output_file}")
        else:
            print(output)
    else:
        from collections import Counter

        cats = Counter(r["category"] for r in results)
        print(f"Total skills: {len(results)}")
        print("\nCategories:")
        for cat, count in cats.most_common():
            print(f"  {cat}: {count}")


def validate(skill_name: str | None = None) -> None:
    """Run skill validation."""
    sys.path.insert(0, str(Path(__file__).parent))
    from validate_skill import SkillValidator

    if skill_name:
        skill_path = SKILLS_DIR / skill_name
        if not skill_path.exists():
            print(f"Skill not found: {skill_path}")
            sys.exit(1)
        validator = SkillValidator(skill_path)
        validator.validate()
        print(validator.report())
        sys.exit(0 if not validator.errors else 1)
    else:
        # Validate all
        errors_list: list[str] = []
        total = 0
        for skill_dir in sorted(SKILLS_DIR.iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            total += 1
            validator = SkillValidator(skill_dir)
            validator.validate()
            if validator.errors:
                errors_list.append(
                    f"{skill_dir.name}: {', '.join(str(e) for e in validator.errors)}"
                )

        valid = total - len(errors_list)
        print(f"Validated {total} skills: {valid} valid, {len(errors_list)} failed")
        if errors_list:
            print("\nFailed skills:")
            for err in errors_list:
                print(f"  - {err}")
            sys.exit(1)
        else:
            print("All skills valid!")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="cli",
        description="OpenClaw Collection CLI - Scaffolding and management tool",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # create
    create_parser = subparsers.add_parser("create", help="Create a new agent or skill")
    create_sub = create_parser.add_subparsers(dest="create_type", help="Type to create")

    # create agent
    agent_parser = create_sub.add_parser("agent", help="Create a new agent")
    agent_parser.add_argument("name", help="Agent name (kebab-case, e.g., my-agent)")
    agent_parser.add_argument("--purpose", "-p", help="Agent purpose description")
    agent_parser.add_argument(
        "--model", "-m", help="Primary model (default: claude-sonnet-4.5)"
    )

    # create skill
    skill_parser = create_sub.add_parser("skill", help="Create a new skill")
    skill_parser.add_argument("name", help="Skill name (kebab-case, e.g., my-skill)")
    skill_parser.add_argument("--description", "-d", help="Skill description")
    skill_parser.add_argument(
        "--keywords", "-k", help="Comma-separated activation keywords"
    )

    # list
    list_parser = subparsers.add_parser("list", help="List agents or skills")
    list_sub = list_parser.add_subparsers(dest="list_type", help="Type to list")

    list_agent_p = list_sub.add_parser("agents", help="List all agents")
    list_agent_p.add_argument("--category", "-c", help="Filter by category")

    list_skill_p = list_sub.add_parser("skills", help="List all skills")
    list_skill_p.add_argument("--category", "-c", help="Filter by category")

    # scan
    scan_parser = subparsers.add_parser("scan", help="Scan and classify all skills")
    scan_parser.add_argument("--json", action="store_true", help="Output as JSON")
    scan_parser.add_argument("-o", "--output", help="Output file path")

    # validate
    validate_parser = subparsers.add_parser("validate", help="Validate skills")
    validate_parser.add_argument("--skill", "-s", help="Validate a specific skill")

    args = parser.parse_args()

    if args.command == "create":
        if args.create_type == "agent":
            create_agent(args.name, args.purpose, args.model)
        elif args.create_type == "skill":
            kw = args.keywords.split(",") if args.keywords else None
            create_skill(args.name, args.description, kw)
        else:
            agent_parser.print_help()
            skill_parser.print_help()
    elif args.command == "list":
        if args.list_type == "agents":
            list_agents(args.category)
        elif args.list_type == "skills":
            list_skills(args.category)
        else:
            list_agent_p.print_help()
            list_skill_p.print_help()
    elif args.command == "scan":
        scan_skills(args.json, args.output)
    elif args.command == "validate":
        validate(args.skill)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
