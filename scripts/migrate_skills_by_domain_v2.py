#!/usr/bin/env python3
"""
Domain-based skill migration script (v2 - fixed nested directory issue)
Organizes skills into domain subdirectories to avoid GitHub's 1000-item limit.
"""

import json
import subprocess
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = BASE_DIR / "collection" / "skills"
PLAN_FILE = BASE_DIR / "skill_migration_plan.json"

# Domain categories and keywords (same as classify script)
DOMAIN_KEYWORDS = {
    "neuroscience": [
        "brain",
        "neural",
        "neuron",
        "eeg",
        "fmri",
        "cognitive",
        "spiking",
        "snn",
        "neuroplastic",
        "synaptic",
        "hippocampal",
        "cortex",
        "bci",
        "neuroscience",
    ],
    "quantum": [
        "quantum",
        "qubit",
        "qaoa",
        "vqe",
        "qml",
        "qnn",
        "qkd",
        "qec",
        "qrc",
        "entanglement",
        "superconducting",
        "photonic",
        "bosonic",
        "gkp",
    ],
    "ai-ml": [
        "transformer",
        "llm",
        "moe",
        "attention",
        "reinforcement",
        "gradient",
        "training",
        "learning",
        "agent",
        "agentic",
        "model",
        "deep",
        "network",
        "optimization",
        "rnn",
        "cnn",
        "distillation",
        "finetune",
        "prompt",
    ],
    "systems-engineering": [
        "distributed",
        "control",
        "mpc",
        "cyber",
        "physical",
        "cps",
        "embedded",
        "realtime",
        "fault",
        "tolerant",
        "resilience",
        "security",
        "protocol",
    ],
    "math-statistics": [
        "mathematic",
        "statistical",
        "probability",
        "bayesian",
        "inference",
        "tensor",
        "matrix",
        "algebra",
        "geometry",
        "topology",
        "calculus",
        "differential",
        "equation",
        "optimization",
        "convex",
    ],
    "medical": [
        "medical",
        "health",
        "clinical",
        "diagnosis",
        "drug",
        "therapy",
        "imaging",
        "biomarker",
        "patient",
        "hospital",
        "disease",
    ],
    "finance": [
        "finance",
        "portfolio",
        "stock",
        "trading",
        "market",
        "risk",
        "option",
        "pricing",
        "investment",
        "quantitative",
        "economic",
    ],
    "control-systems": [
        "control",
        "mpc",
        "feedback",
        "stability",
        "dynamics",
        "oscillator",
        "synchronization",
        "phase",
        "kuramoto",
        "robust",
        "adaptive",
    ],
    "tools-frameworks": [
        "docker",
        "git",
        "github",
        "chrome",
        "electron",
        "react",
        "frontend",
        "obsidian",
        "skill",
        "plugin",
        "mcp",
        "cli",
        "api",
    ],
}


def classify_skill(skill_name: str) -> str:
    """Classify a skill into a domain based on keywords."""
    skill_lower = skill_name.lower()

    # Check each domain's keywords
    for domain, keywords in DOMAIN_KEYWORDS.items():
        for keyword in keywords:
            if keyword in skill_lower:
                return domain

    return "other"


def build_migration_plan():
    """Build migration plan from current skills."""
    skills = []

    # Get all skill directories
    for skill_dir in SKILLS_DIR.iterdir():
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
            skill_name = skill_dir.name
            domain = classify_skill(skill_name)
            skills.append(
                {
                    "name": skill_name,
                    "domain": domain,
                    "source": f"collection/skills/{skill_name}",
                    "target": f"collection/skills/{domain}/{skill_name}",
                }
            )

    # Sort by domain
    skills.sort(key=lambda x: (x["domain"], x["name"]))

    # Count by domain
    domain_counts = defaultdict(int)
    for skill in skills:
        domain_counts[skill["domain"]] += 1

    print("\n" + "=" * 60)
    print("Migration Plan Statistics")
    print("=" * 60)
    for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
        print(f"{domain:20s}: {count:4d} skills")
    print("=" * 60)
    print(f"Total: {len(skills)} skills")

    # Save plan
    with open(PLAN_FILE, "w") as f:
        json.dump(skills, f, indent=2)

    print(f"\nPlan saved to: {PLAN_FILE}")
    return skills


def execute_migration(plan: list):
    """Execute migration using git mv."""
    print("\n" + "=" * 60)
    print("Skill Migration Execution (v2 - fixed)")
    print("=" * 60)

    # First, create all domain directories
    domains = set(skill["domain"] for skill in plan)
    for domain in domains:
        domain_dir = SKILLS_DIR / domain
        if not domain_dir.exists():
            domain_dir.mkdir(parents=True)
            print(f"Created directory: {domain_dir}")

    print(f"\nMigrating {len(plan)} skills...")
    print("This will preserve git history using 'git mv'")

    errors = []
    success_count = 0

    for i, skill in enumerate(plan, 1):
        source = BASE_DIR / skill["source"]
        target = BASE_DIR / skill["target"]

        # Skip if already migrated
        if target.exists():
            print(f"  [{i}/{len(plan)}] SKIP: {skill['name']} (already exists)")
            continue

        # Ensure parent directory exists
        target.parent.mkdir(parents=True, exist_ok=True)

        print(f"  [{i}/{len(plan)}] Migrating: {skill['name']} → {skill['domain']}/")

        # Try git mv first
        try:
            cmd = ["git", "mv", str(source), str(target)]
            subprocess.run(cmd, cwd=BASE_DIR, check=True, capture_output=True)
            success_count += 1
        except subprocess.CalledProcessError:
            # If git mv fails (not in git or other issue), use regular mv
            try:
                subprocess.run(["mv", str(source), str(target)], check=True)
                success_count += 1
            except subprocess.CalledProcessError as e2:
                errors.append({"skill": skill["name"], "error": str(e2)})
                print(f"    ERROR: {e2}")

    print("\n" + "=" * 60)
    print("Migration Summary")
    print("=" * 60)
    print(f"Successfully migrated: {success_count}/{len(plan)}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\nFailed skills:")
        for err in errors:
            print(f"  - {err['skill']}: {err['error']}")

    return success_count, errors


def main():
    # Build or load plan
    if PLAN_FILE.exists():
        print(f"Loading existing plan from: {PLAN_FILE}")
        with open(PLAN_FILE) as f:
            plan = json.load(f)
    else:
        print("Building new migration plan...")
        plan = build_migration_plan()

    # Execute migration
    success, errors = execute_migration(plan)

    if success > 0:
        print("\n✓ Migration complete!")
        print("Next steps:")
        print("  1. git status - review changes")
        print("  2. git commit -m 'refactor: organize skills by domain'")
        print("  3. git push")


if __name__ == "__main__":
    main()
