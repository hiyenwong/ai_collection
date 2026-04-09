#!/usr/bin/env python3
"""Scan all skills in the collection and produce a categorized inventory.

Usage:
    python scan_skills.py                     # Print summary to stdout
    python scan_skills.py --json              # Output full JSON
    python scan_skills.py --json -o skill-scan-results.json
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

# Category classification rules: (keyword_list, category_name)
CATEGORY_RULES: list[tuple[list[str], str]] = [
    # Coding / development
    (["opencode", "claude-code", "copilot", "openspec", "cursor", "react", "electron",
      "chrome-extension", "frontend", "docker", "spring-boot", "codex", "gemini-cli",
      "harness-engineering", "swe-bench", "swe-ci"], "coding"),
    # Finance
    (["stock", "akshare", "finance", "portfolio", "quantum-finance", "quantum-portfolio",
      "thsdk", "trading", "quantitative"], "finance"),
    # Quantum computing (exclude quantum-finance which goes to finance)
    (["quantum-knowledge", "quantum-game", "quantum-neural", "quantum-protocol",
      "quantum-algorithm", "quantum-information", "quantum-ml", "quantum-eeg",
      "distributed-quantum", "quantum-nonreciprocal"], "quantum"),
    # Neuroscience / brain
    (["brain", "neural", "snn", "synaptic", "spike", "neuro", "eeg", "fmri", "meg",
      "connectome", "dendritic", "kuramoto", "seizure", "stdp", "hebbian", "hopfield",
      "nca", "potassium", "attractor", "plasticity", "cognitive", "bcmi", "bold",
      "tms", "dementia", "autism", "schizophrenia", "alzheimer"], "neuroscience"),
    # AI agents / systems
    (["agent", "agentic", "multi-agent", "delegation", "coordination", "autopoiesis",
      "evolving", "self-evolution", "godel-self", "espl", "competitive-self",
      "emergent-tool", "hierarchical-agent"], "ai-agents"),
    # AI reasoning / training
    (["reasoning", "rl", "reinforcement", "mcmc", "attention", "scaling", "scaling-law",
      "generative", "diffusion", "gan", "vae", "normalization", "dropout", "pruning",
      "蒸馏", "training", "inference", "llm", "language-model", "transformer",
      "gpt", "token", "consistency-model", "clip", "efficient", "bcvareta",
      "claude", "sonnet", "opus", "haiku"], "ai-reasoning"),
    # AI safety / evaluation
    (["safety", "red-team", "adversarial", "bias", "fairness", "privacy",
      "robust", "alignment", "guardrails", "injection", "honest", "verifiable",
      "prover-verifier", "political-bias", "truthful", "membership-inference",
      "evaluating", "mle-bench", "simpleqa", "indqa", "evmbench",
      "cognitive-dark"], "ai-safety"),
    # Meta-skills
    (["skill-extractor", "skill-rag", "skill-creator", "skill-updater", "find-skills",
      "ice-review", "memory-retrieval", "self-challenge", "indexed-memory",
      "meta-cognitive", "declarative-self"], "meta-skills"),
    # Security tools
    (["security-engineer", "security-guardrails", "prompt-injection-defense"], "security"),
    # OpenAI research papers
    (["openai-", "openai_", "gpt-2", "gpt-4", "gpt-5", "dota-2", "dalle",
      "jukebox", "point-e", "musenet", "sora", "retro-contest", "procgen",
      "roboschool", "gym", "universe", "webgpt", "image-gpt", "scaling-kubernetes",
      "whisper", "spinning-up", "o1-mini", "o3-mini"], "openai-research"),
    # Data analysis tools
    (["data-engineer", "sqlite-knowledge-graph", "sqlite-kg", "rag", "graph-rag",
      "knowledge-graph", "research-literature", "hypergraph", "lancedb",
      "chat-history"], "data-analysis"),
    # Domain tools / integration
    (["feishu", "apple-", "iamb", "matrix", "sonos", "weather", "news",
      "consulting-report", "arxiv-search", "arxiv-paper", "openai-research-monitor",
      "hourly-research", "autoresearch", "news-search", "taiyi", "meditation"], "domain-tools"),
    # General AI topics (catch broader research topics)
    (["robot", "sim-to-real", "imitation-learning", "montezuma", "minecraft",
      "exploration", "curiosity", "meta-learning", "evolution", "gamepad",
      "domain-randomization", "dexterity", "rubik", "theorem", "math",
      "world-model", "simulator", "physics"], "general-ai"),
    # IoT / systems
    (["iot"], "systems-engineering"),
    # Additional coverage for uncategorized items
    (["tripartite-synapse", "hysteresis", "gyralnet", "subnetwork",
      "trajectory-controlled"], "neuroscience"),
    (["policy-gradient", "hindsight-experience", "reinforcement",
      "variance-reduction", "option-discovery", "curriculum-learning",
      "opponent-learning"], "ai-reasoning"),
    (["accessibility-wcag", "a11y"], "coding"),
    (["infinite-horizon", "stochastic-analysis", "stochastic-momentum",
      "admm"], "ai-reasoning"),
    (["pixelcnn", "variational-lossy", "texture-interpolation",
      "nonlinear-computation", "deep-linear", "visual-perception",
      "understanding-the-source"], "ai-reasoning"),
    (["research-agenda", "evals-drive", "interpretable-and-pedagogical",
      "requests-for-research", "teaching-models", "self-verification",
      "interdisciplinary-discovery", "reflection-driven",
      "prediction-and-control-with-temporal"], "ai-safety"),
    (["infrastructure", "ml-complexity", "distributed-tasks",
      "teach-cofounder", "international-2018-results"], "general-ai"),
]


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
    fm_text = content[3:end].strip()
    rest = content[end + 4:]
    fm: dict[str, str] = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm, rest


def extract_activation_keywords(content: str) -> list[str]:
    """Extract activation keywords from SKILL.md content."""
    # From frontmatter description field
    fm, body = parse_frontmatter(content)
    keywords: list[str] = []

    # Check frontmatter description for trigger keywords
    desc = fm.get("description", "")
    kw_match = re.search(r"Trigger keywords?:\s*(.+?)(?:\.|$)", desc)
    if kw_match:
        keywords.extend(k.strip() for k in kw_match.group(1).split(",") if k.strip())

    # Check markdown body for Activation Keywords section
    match = re.search(
        r"## Activation Keywords\s*\n(.*?)(?=\n##|\Z)", body, re.DOTALL
    )
    if match:
        kws = re.findall(r"^-\s*(.+)$", match.group(1), re.MULTILINE)
        keywords.extend(k.strip() for k in kws if k.strip())

    # Deduplicate while preserving order, filter out empty/junk
    seen: set[str] = set()
    unique: list[str] = []
    for kw in keywords:
        kw = kw.strip()
        if kw and kw not in ("---", "-", "--") and kw not in seen:
            seen.add(kw)
            unique.append(kw)
    return unique


def extract_title(content: str) -> str:
    """Extract skill title from SKILL.md."""
    fm, body = parse_frontmatter(content)
    # Try frontmatter name first
    if "name" in fm:
        return fm["name"]
    # Try H1 header - use only the first part before " - " if present
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        # If title is very long, try to extract just the skill name
        if " - " in title:
            title = title.split(" - ")[0].strip()
        if len(title) > 60:
            title = title[:57] + "..."
        return title
    return "Unknown"


def extract_description(content: str, max_len: int = 120) -> str:
    """Extract a short description from SKILL.md."""
    fm, body = parse_frontmatter(content)
    if "description" in fm:
        desc = fm["description"].strip()
        # Skip frontmatter separators or empty descriptions
        if desc in ("---", "", "---\n"):
            pass
        elif len(desc) <= max_len:
            return desc
        else:
            # Try to cut at sentence boundary
            for sep in [". ", "。", ";"]:
                idx = desc.find(sep, max_len // 2)
                if 0 < idx <= max_len:
                    return desc[: idx + len(sep)]
            return desc[:max_len] + "..."
    # Try Description section
    match = re.search(
        r"## Description\s*\n+(.*?)(?:\n\n|\n##|\Z)", body, re.DOTALL
    )
    if match:
        desc = match.group(1).strip().replace("\n", " ")
        # Remove markdown bold markers
        desc = re.sub(r"\*\*(.+?)\*\*", r"\1", desc)
        if len(desc) <= max_len:
            return desc
        return desc[:max_len] + "..."
    # Try first paragraph after H1
    match = re.search(r"^#\s+.+\n+(.+?)(?:\n\n|\n##|\Z)", body, re.DOTALL)
    if match:
        desc = match.group(1).strip().replace("\n", " ")
        desc = re.sub(r"\*\*(.+?)\*\*", r"\1", desc)
        if len(desc) <= max_len:
            return desc
        return desc[:max_len] + "..."
    return "No description available"


def classify_skill(dirname: str, content: str) -> str:
    """Classify a skill into a category based on directory name and content."""
    name_lower = dirname.lower()

    # Count category scores
    scores: dict[str, int] = {}
    for keywords, category in CATEGORY_RULES:
        score = sum(1 for kw in keywords if kw in name_lower)
        # Also scan content for strong signals
        content_lower = content[:500].lower()
        for kw in keywords:
            if kw in content_lower and kw not in name_lower:
                score += 0.5
        if score > 0:
            scores[category] = score

    if scores:
        return max(scores, key=scores.get)

    return "uncategorized"


def has_subdirs(skill_path: Path) -> dict[str, bool]:
    """Check which subdirectories a skill has."""
    return {
        subdir: (skill_path / subdir).is_dir()
        for subdir in ["examples", "references", "scripts", "assets"]
    }


def scan_skills(skills_dir: Path) -> list[dict[str, Any]]:
    """Scan all skills and return structured data."""
    results: list[dict[str, Any]] = []

    for skill_path in sorted(skills_dir.iterdir()):
        if not skill_path.is_dir():
            continue

        skill_md = skill_path / "SKILL.md"
        if not skill_md.exists():
            continue

        content = skill_md.read_text(encoding="utf-8")

        title = extract_title(content)
        description = extract_description(content)
        keywords = extract_activation_keywords(content)
        category = classify_skill(skill_path.name, content)
        subdirs = has_subdirs(skill_path)

        results.append({
            "name": skill_path.name,
            "title": title,
            "description": description,
            "category": category,
            "keywords": keywords[:10],  # Limit to first 10
            "has_examples": subdirs["examples"],
            "has_references": subdirs["references"],
            "has_scripts": subdirs["scripts"],
            "has_assets": subdirs["assets"],
        })

    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan all skills in the collection")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("-o", "--output", type=str, help="Output file path")
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    skills_dir = script_dir.parent / "collection" / "skills"

    if not skills_dir.exists():
        print(f"Skills directory not found: {skills_dir}", file=sys.stderr)
        sys.exit(1)

    results = scan_skills(skills_dir)

    if args.json or args.output:
        output = json.dumps(results, ensure_ascii=False, indent=2)
        if args.output:
            Path(args.output).write_text(output, encoding="utf-8")
            print(f"Written {len(results)} skills to {args.output}")
        else:
            print(output)
    else:
        # Print summary
        categories = Counter(r["category"] for r in results)
        with_subs = sum(1 for r in results if any(
            [r["has_examples"], r["has_references"], r["has_scripts"], r["has_assets"]]
        ))
        with_keywords = sum(1 for r in results if r["keywords"])

        print(f"Total skills: {len(results)}")
        print(f"Skills with activation keywords: {with_keywords}")
        print(f"Skills with subdirectories (examples/refs/scripts): {with_subs}")
        print(f"\nCategories:")
        for cat, count in categories.most_common():
            print(f"  {cat}: {count}")

        print(f"\nUncategorized: {categories.get('uncategorized', 0)}")
        uncategorized = [r["name"] for r in results if r["category"] == "uncategorized"]
        if uncategorized:
            print("  " + ", ".join(uncategorized[:20]))
            if len(uncategorized) > 20:
                print(f"  ... and {len(uncategorized) - 20} more")


if __name__ == "__main__":
    main()
