#!/usr/bin/env python3
"""
Domain classification script for repository entries.

Pattern: Keyword-based classification with configurable domains and thresholds.

Usage:
    python classify_entries_by_domain.py <base_dir> [--domains config.json] [--output plan.json]
"""

import os
import json
import argparse
from pathlib import Path
from collections import defaultdict

# Domain classification keywords (customize for your repo)
DOMAIN_KEYWORDS = {
    "neuroscience": [
        "brain", "neural", "spike", "spiking", "EEG", "fMRI", "MEG", "ECoG",
        "cortex", "cortical", "hippocampal", "synaptic", "neuron", "neuromorphic",
        "BCI", "neuroplasticity", "LFP", "cognitive", "dendritic"
    ],
    "quantum": [
        "quantum", "QNN", "QAOA", "VQE", "qubit", "entanglement", "superposition",
        "Pauli", "Hamiltonian", "gate", "circuit", "QKD", "qubit", "QEC",
        "variational", "ansatz", "stabilizer", "decoder", "error-correction"
    ],
    "ai-ml": [
        "machine-learning", "deep-learning", "transformer", "neural-network",
        "attention", "embedding", "representation", "gradient", "optimization",
        "training", "model", "learning", "RL", "reinforcement", "distillation"
    ],
    "systems-engineering": [
        "control", "CPS", "cyber-physical", "MPC", "model-predictive",
        "distributed", "consensus", "fault-tolerant", "resilience", "robust",
        "digital-twin", "verification", "architecture", "design-pattern"
    ],
    "math-statistics": [
        "theorem", "proof", "algebra", "statistical", "bayesian", "estimation",
        "inference", "geometry", "topology", "algebraic", "probability",
        "distribution", "optimization", "convergence"
    ],
    "finance": [
        "portfolio", "trading", "stock", "market", "option", "pricing",
        "risk", "volatility", "hedging", "investment", "quantitative",
        "backtesting", "financial"
    ],
    "medical": [
        "diagnosis", "imaging", "clinical", "healthcare", "disease",
        "treatment", "patient", "medical", "hospital", "therapy",
        "biomedical", "health"
    ],
    "tools-frameworks": [
        "docker", "python", "framework", "tool", "library", "API",
        "cli", "workflow", "pipeline", "automation", "script"
    ],
    "control-systems": [
        "feedback", "stability", "robust", "adaptive", "controller",
        "PID", "loop", "dynamic", "system", "regulation", "actuator"
    ],
    "other": []  # Fallback for unclassifiable entries
}


def classify_entry(name: str, keywords: dict) -> str:
    """
    Classify entry by keyword matching.
    
    Strategy:
    1. Check each domain's keywords against entry name
    2. Count matches per domain
    3. Return domain with highest match count (threshold: >= 1)
    4. If no matches, return 'other'
    """
    scores = defaultdict(int)
    
    for domain, domain_keywords in keywords.items():
        if domain == "other":
            continue
            
        for keyword in domain_keywords:
            if keyword.lower() in name.lower():
                scores[domain] += 1
    
    if scores:
        # Return domain with max score
        max_domain = max(scores.items(), key=lambda x: x[1])
        if max_domain[1] >= 1:  # Threshold: at least 1 keyword match
            return max_domain[0]
    
    return "other"


def main(base_dir: str, domains_config: str = None, output: str = "migration_plan.json"):
    """Generate migration plan with domain classification."""
    
    # Load custom domain config if provided
    if domains_config:
        with open(domains_config) as f:
            domain_keywords = json.load(f)
    else:
        domain_keywords = DOMAIN_KEYWORDS
    
    # Scan entries to classify
    base_path = Path(base_dir)
    entries = []
    
    # For directory entries (skills/agents/etc):
    for entry in base_path.iterdir():
        if entry.is_dir() and not entry.name.startswith('.'):
            entries.append(entry.name)
    
    # Classify each entry
    migration_plan = []
    domain_counts = defaultdict(int)
    
    for entry_name in entries:
        domain = classify_entry(entry_name, domain_keywords)
        migration_plan.append({
            "name": entry_name,
            "domain": domain
        })
        domain_counts[domain] += 1
    
    # Save migration plan
    with open(output, 'w') as f:
        json.dump(migration_plan, f, indent=2)
    
    # Report statistics
    print(f"Total entries: {len(entries)}")
    print("\nDomain distribution:")
    for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
        print(f"  {domain}: {count}")
    
    print(f"\nMigration plan saved to: {output}")
    
    # Safety check: any domain exceeding 1000?
    max_domain, max_count = max(domain_counts.items(), key=lambda x: x[1])
    if max_count > 1000:
        print(f"\n⚠ WARNING: {max_domain} domain has {max_count} entries (exceeds GitHub 1000 limit)")
        print("   Consider further splitting this domain alphabetically or by subtopic")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classify repository entries by domain")
    parser.add_argument("base_dir", help="Directory to scan for entries")
    parser.add_argument("--domains", help="Custom domain keywords config (JSON)")
    parser.add_argument("--output", default="migration_plan.json", help="Output migration plan file")
    
    args = parser.parse_args()
    main(args.base_dir, args.domains, args.output)