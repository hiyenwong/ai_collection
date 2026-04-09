#!/usr/bin/env python3
"""
Fix Tools Used section format - convert tables to lists.
"""

import re
from pathlib import Path


def fix_tools_section(skill_path: Path) -> bool:
    """Fix Tools Used section by converting tables to lists."""
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        return False

    content = skill_md.read_text(encoding="utf-8")
    original = content

    # Find Tools Used section with table
    pattern = r'(## Tools Used\s*\n)\s*\n(\|[^\n]+\|\n\|[^\n]+\|\n(?:\|[^\n]+\|\n)+)'

    def replace_table_with_list(match):
        header = match.group(1)
        table = match.group(2)

        # Parse table rows
        lines = table.strip().split('\n')
        if len(lines) < 2:
            return header + table

        # Skip header and separator lines
        data_lines = []
        for line in lines:
            if '|' in line and not re.match(r'^\|[-\s:]+\|', line):
                data_lines.append(line)

        # Extract tool names from first column
        tools = []
        for line in data_lines:
            cells = [c.strip() for c in line.split('|')]
            if len(cells) >= 2 and cells[1]:
                tool_name = cells[1]
                # Clean up tool name
                tool_name = re.sub(r'\s*\([^)]*\)\s*', '', tool_name)  # Remove parentheses
                tool_name = tool_name.strip()
                if tool_name:
                    tools.append(f"- `{tool_name}` - Analysis component\n")

        if tools:
            return header + "\n" + "".join(tools) + "\n"
        else:
            return header + "\n- `read` - Read documentation\n- `exec` - Run analysis\n\n"

    new_content = re.sub(pattern, replace_table_with_list, content)

    if new_content != original:
        skill_md.write_text(new_content, encoding="utf-8")
        print(f"✅ Fixed: {skill_path.name}")
        return True

    return False


def main():
    skills_dir = Path(__file__).parent.parent / "collection" / "skills"

    # Skills with table format Tools Used
    skills_to_fix = [
        "brain-network-lesions-robustness",
        "brain-spatiotemporal-patterns-blueprint",
        "bursty-persistent-brain-networks-pbm",
        "cbtr-causality-topological-ranking",
        "conex-connect-eeg-extremal",
        "evolving-plasticity-rules-cgp",
        "graph-gaussian-embedding-alzheimer-meg",
        "grid-fields-place-cells-self-organization",
        "naplib-neural-acoustic-processing",
        "neural-simulator-openai-gym-bridge",
        "sbm-zebrafish-foundation-model",
        "sex-by-age-brain-connectivity",
        "snn-simulation-tools-review",
        "ssgr-gt-influential-brain-nodes",
        "stochastic-lowrank-rnn-inference",
    ]

    print("🔧 Fixing Tools Used section format...\n")

    fixed = 0
    for skill_name in skills_to_fix:
        skill_path = skills_dir / skill_name
        if fix_tools_section(skill_path):
            fixed += 1

    print(f"\nFixed {fixed} skills")


if __name__ == "__main__":
    main()