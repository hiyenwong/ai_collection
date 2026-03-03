#!/usr/bin/env python3
"""Install agents and skills from collection/ into OpenClaw (~/.copilot/agents/ and ~/.claude/skills/).

Usage:
    python scripts/install.py           # Install all
    python scripts/install.py --agents  # Agents only
    python scripts/install.py --skills  # Skills only
    python scripts/install.py --dry-run # Preview without installing
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
AGENTS_SRC = REPO_ROOT / "collection" / "agents"
SKILLS_SRC = REPO_ROOT / "collection" / "skills"
AGENTS_DST = Path.home() / ".copilot" / "agents"
SKILLS_DST = Path.home() / ".claude" / "skills"


# ---------------------------------------------------------------------------
# Agent installation
# ---------------------------------------------------------------------------

def _extract_system_prompt(content: str) -> str:
    """Extract content inside the first fenced code block after '## System Prompt'.
    Falls back to full document content (after the title) if no such section exists.
    """
    match = re.search(r"## System Prompt\s*```[^\n]*\n(.*?)```", content, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Fallback 1: everything after '## System Prompt' heading
    match = re.search(r"## System Prompt\n+(.*?)(?:\n## |\Z)", content, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Fallback 2: whole document is the system prompt (no System Prompt section)
    # Strip the first H1 title line and use the rest
    lines = content.splitlines()
    body_lines = [l for l in lines if not l.startswith("# ")]
    body = "\n".join(body_lines).strip()
    return body if body else ""


def _extract_purpose(content: str) -> str:
    """Extract first non-empty paragraph under '## Purpose', '## Mission', or '## Identity'."""
    for section in ("Purpose", "Mission", "Identity"):
        match = re.search(rf"## {section}\n+(.*?)(?:\n## |\Z)", content, re.DOTALL)
        if match:
            text = match.group(1).strip()
            # Strip markdown bold/bullet formatting and take first meaningful line
            lines = [re.sub(r"\*\*|^[-*]\s*", "", l).strip() for l in text.splitlines() if l.strip() and not l.startswith("#")]
            if lines:
                return " ".join(lines[:2])  # max 2 lines
    return ""


def _extract_tools(content: str) -> list[str]:
    """Extract tool names from '## Tools' section (lines like '- **tool:**')."""
    match = re.search(r"## Tools\n+(.*?)(?:\n## |\Z)", content, re.DOTALL)
    if not match:
        return []
    tools = re.findall(r"\*\*(\w[\w-]*)\*\*", match.group(1))
    return list(dict.fromkeys(tools))  # deduplicate, preserve order


def install_agent(agent_dir: Path, dst: Path, dry_run: bool = False) -> tuple[bool, str]:
    """Convert AGENT.md → flat .md file and write to dst.

    Args:
        agent_dir: Source agent directory containing AGENT.md.
        dst: Destination directory (~/.copilot/agents/).
        dry_run: If True, only simulate.

    Returns:
        (success, message)
    """
    agent_md = agent_dir / "AGENT.md"
    if not agent_md.exists():
        return False, f"AGENT.md not found in {agent_dir}"

    name = agent_dir.name
    content = agent_md.read_text(encoding="utf-8")

    description = _extract_purpose(content)
    tools = _extract_tools(content)
    system_prompt = _extract_system_prompt(content)

    if not description:
        return False, f"{name}: could not extract description from Purpose section"
    if not system_prompt:
        return False, f"{name}: could not extract system prompt"

    tools_yaml = "\n".join(f"  - {t}" for t in tools) if tools else "  - read\n  - write"

    flat_md = f"""---
name: "{name}"
description: "{description.replace('"', "'")}"
tools:
{tools_yaml}
---

{system_prompt}
"""

    out_file = dst / f"{name}.md"
    if dry_run:
        action = "UPDATE" if out_file.exists() else "CREATE"
        return True, f"[dry-run] {action} {out_file}"

    dst.mkdir(parents=True, exist_ok=True)
    out_file.write_text(flat_md, encoding="utf-8")
    action = "Updated" if out_file.exists() else "Installed"
    return True, f"{action} agent → {out_file}"


# ---------------------------------------------------------------------------
# Skill installation
# ---------------------------------------------------------------------------

SKILL_DESCRIPTIONS: dict[str, tuple[str, str]] = {
    "skill-extractor": (
        "skill-extractor",
        "Meta-skill that automatically identifies and extracts reusable skill patterns from "
        "conversations, saving them as standard SKILL.md files. Use when user says 提炼技能, "
        "提取 skill, extract skill, or wants to turn a workflow into a reusable skill.",
    ),
    "skill-rag-indexer": (
        "skill-rag-indexer",
        "RAG indexer for local skill documents with semantic search and intelligent skill "
        "recommendation. Use when user says skill rag search, search skills, or needs to "
        "find skills by semantic query.",
    ),
    "iamb-matrix-cli": (
        "iamb-matrix-cli",
        "Matrix CLI operations for iamb: account registration, token acquisition, Space ID "
        "retrieval and space management beyond iamb native commands. Use when user mentions "
        "iamb or matrix cli.",
    ),
    "copilot-cli": (
        "copilot-cli",
        "GitHub Copilot CLI terminal agent for planning, editing, running and reviewing code "
        "with repository context. Use when user mentions copilot cli or github copilot cli.",
    ),
    "chat-history-lancedb": (
        "chat-history-lancedb",
        "LanceDB-based chat history system with vector semantic search and RAG context "
        "retrieval. Use when user needs to persist chat history, search past conversations, "
        "or mentions lancedb chat history.",
    ),
    "teach-cofounder": (
        "teach-cofounder",
        "Senior technical mentor skill that teaches through Socratic guidance, deep principle "
        "explanation, and progressive learning. Use when user says teach me, mentor me, "
        "or wants to learn a technical concept.",
    ),
    "taiyi-jinhua-meditation": (
        "taiyi-jinhua-meditation",
        "Taoist meditation guidance based on Taiyi Jinhua Zongzhi (太乙金华宗旨). Guides "
        "回光守中 practice and inner alchemy concepts. Use when user mentions 冥想, meditation, "
        "太乙金华宗旨, 回光守中, or Taoist inner cultivation.",
    ),
}


def _has_valid_frontmatter(skill_md: Path) -> bool:
    """Return True if SKILL.md has valid YAML frontmatter with name and description."""
    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False
    end = content.find("---", 3)
    if end < 0:
        return False
    try:
        parsed = yaml.safe_load(content[3:end]) or {}
        return bool(parsed.get("name") and parsed.get("description"))
    except yaml.YAMLError:
        return False


def _add_frontmatter(skill_md: Path, name: str, description: str) -> None:
    """Prepend YAML frontmatter to SKILL.md in place."""
    content = skill_md.read_text(encoding="utf-8")
    frontmatter = f'---\nname: {name}\ndescription: "{description}"\n---\n\n'
    skill_md.write_text(frontmatter + content, encoding="utf-8")


def install_skill(skill_dir: Path, dst: Path, dry_run: bool = False) -> tuple[bool, str]:
    """Copy skill directory to dst, adding frontmatter if missing.

    Args:
        skill_dir: Source skill directory.
        dst: Destination directory (~/.claude/skills/).
        dry_run: If True, only simulate.

    Returns:
        (success, message)
    """
    name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return False, f"{name}: SKILL.md not found"

    out_dir = dst / name
    if dry_run:
        action = "UPDATE" if out_dir.exists() else "INSTALL"
        return True, f"[dry-run] {action} skill → {out_dir}"

    dst.mkdir(parents=True, exist_ok=True)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    shutil.copytree(skill_dir, out_dir)

    # Fix frontmatter if needed
    installed_md = out_dir / "SKILL.md"
    if not _has_valid_frontmatter(installed_md):
        if name in SKILL_DESCRIPTIONS:
            fm_name, fm_desc = SKILL_DESCRIPTIONS[name]
            _add_frontmatter(installed_md, fm_name, fm_desc)
        else:
            return True, f"Installed skill → {out_dir} (⚠️  frontmatter missing, add manually)"

    return True, f"Installed skill → {out_dir}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    """Entry point."""
    parser = argparse.ArgumentParser(description="Install OpenClaw agents and skills")
    parser.add_argument("--agents", action="store_true", help="Install agents only")
    parser.add_argument("--skills", action="store_true", help="Install skills only")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    do_agents = args.agents or not args.skills
    do_skills = args.skills or not args.agents

    ok = err = 0

    if do_agents:
        print(f"\n{'='*50}")
        print("Installing Agents → ~/.copilot/agents/")
        print("=" * 50)
        for agent_dir in sorted(AGENTS_SRC.iterdir()):
            if not agent_dir.is_dir() or agent_dir.name.startswith("."):
                continue
            success, msg = install_agent(agent_dir, AGENTS_DST, dry_run=args.dry_run)
            icon = "✅" if success else "❌"
            print(f"  {icon} {msg}")
            if success:
                ok += 1
            else:
                err += 1

    if do_skills:
        print(f"\n{'='*50}")
        print("Installing Skills → ~/.claude/skills/")
        print("=" * 50)
        for skill_dir in sorted(SKILLS_SRC.iterdir()):
            if not skill_dir.is_dir():
                continue
            success, msg = install_skill(skill_dir, SKILLS_DST, dry_run=args.dry_run)
            icon = "✅" if success else "❌"
            print(f"  {icon} {msg}")
            if success:
                ok += 1
            else:
                err += 1

    print(f"\n{'='*50}")
    prefix = "[dry-run] " if args.dry_run else ""
    print(f"{prefix}Done: {ok} succeeded, {err} failed")
    if args.dry_run:
        print("Run without --dry-run to apply changes.")
    else:
        print("Restart Copilot CLI to pick up changes.")
    print("=" * 50)

    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
