"""
INDEX.md Rebuild Utility for ai_collection

Rebuilds the skill count in INDEX.md by scanning the filesystem directly.
Use when INDEX.md count drifts from actual skill count (common after multiple
sessions that create/sync skills without updating INDEX.md).

Usage: Run via execute_code in Hermes cron jobs.
"""

import os
import re


def count_skills(skill_dir):
    """Count actual skills by scanning filesystem."""
    return sum(
        1
        for item in os.listdir(skill_dir)
        if os.path.isdir(os.path.join(skill_dir, item))
        and os.path.exists(os.path.join(skill_dir, item, "SKILL.md"))
    )


def fix_index_count(index_path, skill_dir):
    """Find and fix the skill count in INDEX.md."""
    actual = count_skills(skill_dir)

    with open(index_path) as f:
        content = f.read()

    # Pattern: **Total Skills**: NNN or Total: NNN skills
    patterns = [
        (r"(\*\*Total Skills\*\*: )(\d+)", rf"\g<1>{actual}"),
        (r"(Total: )(\d+)( skills)", rf"\g<1>{actual}\g<3>"),
        (r"(\()(\d{3,})(\) skills)", rf"\g<1>{actual}\g<3>"),
    ]

    updated = False
    for pattern, replacement in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            updated = True

    if updated:
        with open(index_path, "w") as f:
            f.write(content)
        print(f"INDEX.md count updated to {actual}")
    else:
        print(
            f"INDEX.md count verification: actual={actual}, no pattern matched to update"
        )

    return actual


if __name__ == "__main__":
    skill_dir = os.path.expanduser("~/.hermes/skills/ai_collection")
    index_path = os.path.join(
        os.environ.get(
            "OBSIDIAN_VAULT_PATH", "/Users/hiyenwong/Documents/Obsidian Vault"
        ),
        "ai_collection",
        "INDEX.md",
    )

    if os.path.exists(index_path):
        fix_index_count(index_path, skill_dir)
    else:
        print(f"INDEX.md not found at {index_path}")
