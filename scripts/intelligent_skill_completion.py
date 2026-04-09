#!/usr/bin/env python3
"""
Intelligently complete skill documentation by generating meaningful content
from existing skill content.

This script:
1. Generates specific Description from existing skill content
2. Creates relevant Instructions for Agents from methodology/steps
3. Produces meaningful Examples from use cases/applications

Usage:
    python scripts/intelligent_skill_completion.py
"""

import re
from pathlib import Path

# Placeholder patterns to detect
PLACEHOLDER_DESCRIPTION = (
    "Framework from arXiv papers. See paper reference for details."
)
PLACEHOLDER_INSTRUCTIONS_START = (
    "**Understand the Request**: Analyze what the user needs"
)
PLACEHOLDER_EXAMPLES_SKILL_NAME = "How can I apply {skill_name}?"


def extract_title(content: str) -> str:
    """Extract skill title from the first H1 header."""
    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""


def extract_key_concepts(content: str) -> list[str]:
    """Extract key concepts from the skill content."""
    concepts = []

    # Look for Key Concepts section
    match = re.search(r"## Key Concepts\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if match:
        concepts_text = match.group(1)
        # Extract bullet points
        concepts.extend(re.findall(r"-\s*(.+)$", concepts_text, re.MULTILINE))

    # Look for Core Methodology section
    match = re.search(r"## Core Methodology\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if match:
        methodology = match.group(1)
        # Extract numbered steps
        steps = re.findall(r"###\s*\d+\.\s*(.+)$", methodology, re.MULTILINE)
        concepts.extend(steps)

    # Look for Problem Statement
    match = re.search(r"## Problem Statement\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if match:
        problem = match.group(1)[:200]
        concepts.append(problem.strip())

    # Look for Applications section
    match = re.search(r"## Applications\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if match:
        apps_text = match.group(1)
        apps = re.findall(r"###\s*\d+\.\s*(.+)$", apps_text, re.MULTILINE)
        concepts.extend(apps)

    return concepts[:10]  # Limit to top 10


def extract_when_to_use(content: str) -> list[str]:
    """Extract when-to-use conditions."""
    match = re.search(r"## When to [Uu]se\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if match:
        text = match.group(1)
        return re.findall(r"-\s*(.+)$", text, re.MULTILINE)
    return []


def extract_methodology_steps(content: str) -> list[str]:
    """Extract step-by-step methodology."""
    steps = []

    # Look for Step-by-Step Instructions
    match = re.search(
        r"## Step-by-Step Instructions\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL
    )
    if match:
        methodology = match.group(1)
        # Extract numbered steps
        steps = re.findall(r"###\s*\d+\.\s*(.+)$", methodology, re.MULTILINE)

    # Also look for numbered steps in other sections
    if not steps:
        matches = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*", content, re.MULTILINE)
        steps.extend(matches)

    return steps


def generate_description(skill_name: str, content: str) -> str:
    """Generate a meaningful description from existing content."""

    # Check if description already exists and is not placeholder
    desc_match = re.search(r"## Description\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if desc_match:
        existing_desc = desc_match.group(1).strip()
        if PLACEHOLDER_DESCRIPTION not in existing_desc and len(existing_desc) > 20:
            return existing_desc

    # Extract title
    title = extract_title(content)

    # Extract key concepts
    concepts = extract_key_concepts(content)

    # Extract frontmatter description
    fm_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        fm_desc_match = re.search(
            r"description:\s*['\"]?(.+?)['\"]?\n", fm_match.group(1)
        )
        if fm_desc_match:
            fm_desc = fm_desc_match.group(1).strip()
            if len(fm_desc) > 30 and PLACEHOLDER_DESCRIPTION not in fm_desc:
                return fm_desc

    # Build description from extracted content
    if title:
        desc = title
        if concepts:
            desc += "\n\n**Key Concepts:**\n"
            for concept in concepts[:3]:
                desc += f"- {concept[:100]}\n"
        return desc

    # Fallback: use skill name
    return f"Skill for {skill_name.replace('-', ' ')} - see detailed methodology below."


def generate_instructions(skill_name: str, content: str) -> str:
    """Generate meaningful instructions for agents."""

    # Check if existing instructions are placeholder
    instr_match = re.search(
        r"## Instructions for Agents\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL
    )
    if instr_match:
        existing_instr = instr_match.group(1).strip()
        if PLACEHOLDER_INSTRUCTIONS_START not in existing_instr:
            return existing_instr

    # Extract methodology steps
    methodology_steps = extract_methodology_steps(content)

    # Extract when-to-use
    when_to_use = extract_when_to_use(content)

    # Build instructions
    instructions = []

    if methodology_steps:
        instructions.append("## Instructions for Agents\n")
        instructions.append("Follow these steps when applying this skill:\n\n")

        for i, step in enumerate(methodology_steps[:5], 1):
            step_clean = step.strip()
            if step_clean:
                instructions.append(f"### Step {i}: {step_clean}\n\n")

        # Add when to use section
        if when_to_use:
            instructions.append("### When to Apply\n")
            for condition in when_to_use[:3]:
                instructions.append(f"- {condition}\n")

    else:
        # Generic but contextualized instructions
        title = extract_title(content)
        instructions.append("## Instructions for Agents\n\n")
        instructions.append(f"**Context:** {title if title else skill_name}\n\n")
        instructions.append("### Steps\n\n")
        instructions.append(
            "1. **Understand User Need**: Identify the specific application context.\n"
        )
        instructions.append(
            "2. **Review Methodology**: Check the skill's core concepts and methodology sections.\n"
        )
        instructions.append(
            "3. **Apply Framework**: Use the techniques described in this skill.\n"
        )
        instructions.append(
            "4. **Validate Results**: Cross-check with established benchmarks.\n"
        )
        instructions.append(
            "5. **Report Findings**: Summarize key insights and actionable recommendations.\n"
        )

    return "".join(instructions)


def generate_examples(skill_name: str, content: str) -> str:
    """Generate meaningful examples."""

    # Check if existing examples are placeholder
    examples_match = re.search(r"## Examples\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if examples_match:
        existing_examples = examples_match.group(1).strip()
        placeholder_pattern = PLACEHOLDER_EXAMPLES_SKILL_NAME.replace(
            "{skill_name}", skill_name
        )
        if (
            placeholder_pattern not in existing_examples
            and "How can I apply" not in existing_examples
        ):
            return existing_examples

    # Extract title and concepts
    title = extract_title(content)
    concepts = extract_key_concepts(content)

    # Build examples
    examples = []
    examples.append("## Examples\n\n")

    # Example 1: Basic application
    concept1 = concepts[0] if concepts else "Apply the methodology"
    examples.append("### Example 1: Basic Application\n\n")
    examples.append(
        f"**User:** I need to apply {title if title else skill_name} to my analysis.\n\n"
    )
    examples.append(
        f"**Agent:** I'll help you apply {skill_name}. First, let me understand your specific use case...\n\n"
    )
    examples.append(f"**Context:** {concept1[:80]}\n\n")

    # Example 2: Advanced use case
    when_to_use = extract_when_to_use(content)
    use_case = when_to_use[0] if when_to_use else "Complex analysis scenario"
    examples.append("### Example 2: Advanced Scenario\n\n")
    examples.append(f"**User:** {use_case[:60]}\n\n")
    examples.append(
        "**Agent:** Based on the methodology, I'll guide you through the advanced application...\n\n"
    )

    return "".join(examples)


def complete_skill(skill_path: Path) -> bool:
    """Complete a skill's documentation. Returns True if changes made."""
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        return False

    content = skill_md.read_text(encoding="utf-8")
    skill_name = skill_path.name
    original_content = content

    # Check if skill needs completion
    needs_desc = PLACEHOLDER_DESCRIPTION in content
    needs_instr = PLACEHOLDER_INSTRUCTIONS_START in content
    needs_examples = "How can I apply" in content and skill_name in content

    if not (needs_desc or needs_instr or needs_examples):
        return False

    # Generate and replace sections
    new_content = content

    # Replace Description if needed
    if needs_desc:
        new_desc = generate_description(skill_name, content)
        # Find and replace the placeholder Description section
        desc_match = re.search(
            r"## Description\s*\n(.*?)(?=\n##|\Z)", new_content, re.DOTALL
        )
        if desc_match:
            old_desc_section = desc_match.group(0)
            new_desc_section = f"## Description\n\n{new_desc}\n"
            new_content = new_content.replace(old_desc_section, new_desc_section)

    # Replace Instructions if needed
    if needs_instr:
        new_instr = generate_instructions(skill_name, content)
        instr_match = re.search(
            r"## Instructions for Agents\s*\n(.*?)(?=\n##|\Z)", new_content, re.DOTALL
        )
        if instr_match:
            old_instr_section = instr_match.group(0)
            # Ensure proper section boundary
            new_instr_clean = new_instr.rstrip() + "\n"
            new_content = new_content.replace(old_instr_section, new_instr_clean)

    # Replace Examples if needed
    if needs_examples:
        new_examples = generate_examples(skill_name, content)
        examples_match = re.search(
            r"## Examples\s*\n(.*?)(?=\n##|\Z)", new_content, re.DOTALL
        )
        if examples_match:
            old_examples_section = examples_match.group(0)
            new_examples_clean = new_examples.rstrip() + "\n"
            new_content = new_content.replace(old_examples_section, new_examples_clean)

    # Clean up excessive whitespace
    new_content = re.sub(r"\n{3,}", "\n\n", new_content)

    if new_content != original_content:
        skill_md.write_text(new_content, encoding="utf-8")
        changes = []
        if needs_desc:
            changes.append("Description")
        if needs_instr:
            changes.append("Instructions")
        if needs_examples:
            changes.append("Examples")
        print(f"✅ Completed: {skill_name} ({', '.join(changes)})")
        return True

    return False


def main():
    """Complete all skills with placeholder content."""
    script_dir = Path(__file__).parent
    skills_dir = script_dir.parent / "collection" / "skills"

    if not skills_dir.exists():
        print(f"❌ Skills directory not found: {skills_dir}")
        return

    print("🔧 Completing skills with placeholder content...\n")

    # Find skills with placeholders
    skills_with_placeholders = []

    for skill_path in skills_dir.iterdir():
        if not skill_path.is_dir():
            continue

        skill_md = skill_path / "SKILL.md"
        if not skill_md.exists():
            continue

        content = skill_md.read_text(encoding="utf-8")

        if (
            PLACEHOLDER_DESCRIPTION in content
            or PLACEHOLDER_INSTRUCTIONS_START in content
            or ("How can I apply" in content and skill_path.name in content)
        ):
            skills_with_placeholders.append(skill_path)

    print(f"Found {len(skills_with_placeholders)} skills needing completion\n")

    # Complete each skill
    completed_count = 0
    for skill_path in skills_with_placeholders:
        if complete_skill(skill_path):
            completed_count += 1

    print(f"\n{'=' * 50}")
    print(f"Summary: Completed {completed_count} skills")

    # Run validation
    import subprocess

    print("\n🔍 Running validation...")
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


if __name__ == "__main__":
    main()
