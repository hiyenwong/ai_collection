#!/usr/bin/env python3
"""
Generate skill network data for docs/html/skill-neural-map.html.

Scans collection/skills/ for category subdirectories, counts skills per
category, and injects the data into the HTML file's SKILL_DATA constant.

Usage:
    python scripts/update_neural_map.py
"""

import json
import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "collection" / "skills"
HTML_FILE = REPO_ROOT / "docs" / "html" / "skill-neural-map.html"

# Category colors (matching the HTML design)
CATEGORY_COLORS = {
    "neuroscience": "#e74c3c",
    "quantum": "#9b59b6",
    "other": "#5a6a80",
    "spiking-neuromorphic": "#e67e22",
    "general-ml": "#2ecc71",
    "ai-ml": "#1abc9c",
    "nlp-llm": "#3498db",
    "multi-agent-rl": "#f1c40f",
    "signal-control-systems": "#e91e63",
    "physics-math": "#00bcd4",
    "vision-generative": "#ff9800",
    "reinforcement-learning": "#ffc107",
    "reasoning-bayesian": "#673ab7",
    "systems-engineering": "#3f51b5",
    "tools-frameworks": "#795548",
    "software-engineering": "#607d8b",
    "data-retrieval": "#4caf50",
    "control-systems": "#cddc39",
    "ai-safety-eval": "#f44336",
    "healthcare-bio": "#8bc34a",
    "knowledge-graph": "#cddc39",
    "security-privacy": "#ff5722",
    "finance": "#4caf50",
    "math-statistics": "#009688",
    "deployment-optimization": "#8bc34a",
    "medical": "#f44336",
    "memory": "#9c27b0",
    "continual-learning": "#3f51b5",
    "agent-tools": "#607d8b",
    "chat-history-lancedb": "#455a64",
    "skill-rag-indexer": "#455a64",
}

# Fallback color for unknown categories
FALLBACK_COLOR = "#607d8b"


def count_skills_per_category():
    """Scan collection/skills/ and count SKILL.md files per category."""
    categories = []
    total = 0

    if not SKILLS_DIR.exists():
        return categories, total

    for cat_name in sorted(os.listdir(SKILLS_DIR)):
        cat_path = SKILLS_DIR / cat_name
        if not cat_path.is_dir():
            continue
        # Check if it's a category dir (contains subdirs with SKILL.md)
        count = 0
        for item in os.listdir(cat_path):
            item_path = cat_path / item
            if item_path.is_dir() and (item_path / "SKILL.md").is_file():
                count += 1
        if count > 0 or cat_name in CATEGORY_COLORS:
            color = CATEGORY_COLORS.get(cat_name, FALLBACK_COLOR)
            categories.append({
                "name": cat_name,
                "count": count,
                "color": color,
            })
            total += count

    # Sort by count descending for consistent ordering
    categories.sort(key=lambda x: -x["count"])
    return categories, total


def update_html(categories, total):
    """Inject skill data into the HTML file.

    Replaces the SKILL_DATA constant by finding the start marker
    and matching braces to the closing };</const>.
    """
    if not HTML_FILE.exists():
        print(f"ERROR: HTML file not found: {HTML_FILE}")
        return False

    html = HTML_FILE.read_text()

    # Build the new SKILL_DATA JS object — single-line compact format
    data_js = json.dumps(
        {"categories": categories, "total": total},
        ensure_ascii=False,
    )
    new_data_block = f"const SKILL_DATA = {data_js};"

    start_marker = "const SKILL_DATA = {"
    start_idx = html.find(start_marker)
    if start_idx == -1:
        print("ERROR: Could not find SKILL_DATA in HTML")
        return False

    # Find matching closing brace by counting depth
    brace_depth = 0
    i = start_idx + len(start_marker) - 1  # at the opening '{'
    end_idx = None
    while i < len(html):
        if html[i] == '{':
            brace_depth += 1
        elif html[i] == '}':
            brace_depth -= 1
            if brace_depth == 0:
                end_idx = i + 1  # include }
                # Find the semicolon
                while end_idx < len(html) and html[end_idx] != ';':
                    end_idx += 1
                end_idx += 1  # include ;
                break
        i += 1

    if end_idx is None:
        print("ERROR: Could not find end of SKILL_DATA")
        return False

    html = html[:start_idx] + new_data_block + html[end_idx:]
    HTML_FILE.write_text(html)
    print(f"Updated {HTML_FILE}")
    return True


def main():
    categories, total = count_skills_per_category()
    print(f"Found {len(categories)} categories, {total} total skills")
    for cat in categories:
        print(f"  {cat['name']:30s} {cat['count']:5d}  {cat['color']}")

    if update_html(categories, total):
        print(f"\nNeural map HTML updated with {total} skills across {len(categories)} categories.")
    else:
        print("\nERROR: Failed to update HTML.")


if __name__ == "__main__":
    main()
