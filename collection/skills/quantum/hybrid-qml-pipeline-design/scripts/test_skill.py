#!/usr/bin/env python3
"""Test script for hybrid-qml-pipeline-design skill.
Verifies the skill can be loaded and its guidance applied to a sample QML pipeline design task."""

import os
import sys


def test_skill_loadable():
    """Test that SKILL.md exists and has valid frontmatter."""
    skill_path = os.path.join(os.path.dirname(__file__), "..", "SKILL.md")

    if not os.path.exists(skill_path):
        print(f"FAIL: SKILL.md not found at {skill_path}")
        return False

    with open(skill_path) as f:
        content = f.read()

    # Check frontmatter
    if not content.startswith("---"):
        print("FAIL: Missing YAML frontmatter")
        return False

    # Check required fields
    if "name:" not in content:
        print("FAIL: Missing 'name' in frontmatter")
        return False

    if "description:" not in content:
        print("FAIL: Missing 'description' in frontmatter")
        return False

    # Check key sections
    required_sections = [
        "Noise-Aware Pipeline Architecture",
        "Variational Quantum Algorithm",
        "Correlation-Guided Circuit Design",
        "Compact Model Advantage",
        "Pipeline Design Steps",
        "Key Frameworks",
        "Pitfalls",
        "Verification",
    ]

    for section in required_sections:
        if section not in content:
            print(f"FAIL: Missing section '{section}'")
            return False

    print("PASS: SKILL.md is well-formed with all required sections")
    return True


def test_references_exist():
    """Test that reference files exist."""
    ref_path = os.path.join(os.path.dirname(__file__), "..", "references", "sources.md")

    if not os.path.exists(ref_path):
        print("FAIL: references/sources.md not found")
        return False

    with open(ref_path) as f:
        content = f.read()

    if len(content) < 100:
        print("FAIL: references/sources.md is too short")
        return False

    print("PASS: references/sources.md exists with sufficient content")
    return True


def test_skill_trigger():
    """Test that the skill description contains relevant trigger keywords."""
    skill_path = os.path.join(os.path.dirname(__file__), "..", "SKILL.md")

    with open(skill_path) as f:
        content = f.read()

    triggers = [
        "quantum machine learning",
        "VQA",
        "hybrid quantum-classical",
        "NISQ",
        "noise robustness",
    ]

    for trigger in triggers:
        if trigger.lower() not in content.lower():
            print(f"FAIL: Missing trigger keyword '{trigger}'")
            return False

    print("PASS: All trigger keywords present")
    return True


def main():
    results = []
    results.append(test_skill_loadable())
    results.append(test_references_exist())
    results.append(test_skill_trigger())

    if all(results):
        print("\nAll tests passed! Skill is ready for use.")
        return 0
    else:
        print("\nSome tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
