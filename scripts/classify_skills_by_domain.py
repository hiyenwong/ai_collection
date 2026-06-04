#!/usr/bin/env python3
"""
Skill Domain Classification Script
分析现有技能并按领域分类
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json

SKILLS_DIR = Path("/Users/hiyenwong/ai_github/ai_collection/collection/skills")

# 领域分类规则（基于关键词）
DOMAIN_KEYWORDS = {
    "neuroscience": [
        "brain", "neural", "neuron", "cortex", "eeg", "fmri", "meg", "ecog",
        "bci", "spiking", "synaptic", "hippocampal", "cortical", "neuroplastic",
        "cognitive", "memory", "attention", "learning", "perception",
        "snn", "spiking-neural", "neuromorphic", "reservoir", "lif", "qif"
    ],
    "quantum": [
        "quantum", "qubit", "qaoa", "vqe", "qnn", "qec", "qml", "qkd",
        "entanglement", "bell", "superconducting", "photonic", "rydberg",
        "quantum-computing", "quantum-control", "quantum-error", "quantum-finance",
        "quantum-medical", "quantum-neural", "quantum-portfolio", "quantum-sensor"
    ],
    "ai-ml": [
        "agent", "llm", "transformer", "attention", "moe", "distillation",
        "reinforcement-learning", "rlhf", "dpo", "grpo", "ppo",
        "foundation-model", "embedding", "token", "inference", "serving",
        "prompt", "alignment", "safety", "interpretability", "sae"
    ],
    "systems-engineering": [
        "control", "mpc", "digital-twin", "cyber-physical", "cps",
        "distributed", "fault-tolerant", "reliability", "resilience",
        "mbse", "sysml", "verification", "testing", "security"
    ],
    "control-systems": [
        "mpc", "optimal-control", "feedback", "stability", "robust",
        "adaptive-control", "model-predictive", "nonlinear-control",
        "distributed-control", "quantum-control"
    ],
    "finance": [
        "portfolio", "stock", "trading", "option", "pricing", "risk",
        "market", "financial", "quant", "backtesting", "akshare"
    ],
    "medical": [
        "medical", "clinical", "diagnosis", "healthcare", "biomarker",
        "imaging", "patient", "disease", "treatment", "drug"
    ],
    "tools-frameworks": [
        "docker", "git", "github", "terminal", "browser", "file",
        "skill", "hermes", "claude", "opencode", "codex"
    ],
    "math-statistics": [
        "tensor", "matrix", "linear-algebra", "probability", "bayesian",
        "statistics", "optimization", "numerical", "pde", "ode"
    ]
}

def classify_skill(skill_name: str) -> str:
    """根据技能名称关键词分类到领域"""
    skill_lower = skill_name.lower()
    
    # 统计各领域匹配数
    domain_matches = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        matches = sum(1 for kw in keywords if kw in skill_lower)
        if matches > 0:
            domain_matches[domain] = matches
    
    # 返回匹配最多的领域
    if domain_matches:
        return max(domain_matches.items(), key=lambda x: x[1])[0]
    
    return "other"

def analyze_skills_distribution():
    """分析现有技能分布"""
    skills = [d for d in SKILLS_DIR.iterdir() if d.is_dir()]
    
    print(f"Total skills: {len(skills)}")
    print(f"\nDomain Distribution:")
    
    domain_stats = defaultdict(list)
    
    for skill_dir in skills:
        skill_name = skill_dir.name
        domain = classify_skill(skill_name)
        domain_stats[domain].append(skill_name)
    
    for domain in sorted(domain_stats.keys(), key=lambda x: len(domain_stats[x]), reverse=True):
        count = len(domain_stats[domain])
        print(f"  {domain}: {count} skills")
        # 显示前5个示例
        examples = domain_stats[domain][:5]
        print(f"    Examples: {', '.join(examples)}")
    
    return domain_stats

def generate_migration_plan(domain_stats: dict):
    """生成迁移计划"""
    plan = {
        "source": "collection/skills/",
        "target_structure": {},
        "migrations": []
    }
    
    for domain, skills in domain_stats.items():
        target_dir = f"collection/skills/{domain}/"
        plan["target_structure"][domain] = {
            "count": len(skills),
            "path": target_dir
        }
        
        for skill in skills:
            plan["migrations"].append({
                "from": f"collection/skills/{skill}",
                "to": f"{target_dir}{skill}",
                "domain": domain
            })
    
    # 保存计划
    with open("skill_migration_plan.json", "w") as f:
        json.dump(plan, f, indent=2)
    
    print(f"\nMigration plan saved to skill_migration_plan.json")
    print(f"Total migrations: {len(plan['migrations'])}")
    
    return plan

if __name__ == "__main__":
    print("=" * 60)
    print("Skill Domain Classification Analysis")
    print("=" * 60)
    
    domain_stats = analyze_skills_distribution()
    
    print("\n" + "=" * 60)
    print("Generating Migration Plan...")
    print("=" * 60)
    
    plan = generate_migration_plan(domain_stats)
    
    print("\nNext steps:")
    print("1. Review skill_migration_plan.json")
    print("2. Create domain directories")
    print("3. Execute migration with git mv (preserve history)")
    print("4. Update INDEX.md and documentation")
    print("5. git commit and push")