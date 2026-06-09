#!/usr/bin/env python3
"""
进一步细分 "other" 类别的技能
"""

import json
import subprocess
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path("/Users/hiyenwong/ai_github/ai_collection")
SKILLS_DIR = BASE_DIR / "collection" / "skills"
OTHER_DIR = SKILLS_DIR / "other"

# 细分类别关键词
SUB_DOMAIN_KEYWORDS = {
    "vision-generative": [
        "image", "visual", "vision", "generative", "diffusion", "gan", "vae",
        "pixel", "rendering", "reconstruction", "perceptual", "imaging"
    ],
    "nlp-llm": [
        "language", "text", "nlp", "sentiment", "translation", "generation",
        "conversation", "dialogue", "semantic", "lexical", "linguistic"
    ],
    "spiking-neuromorphic": [
        "spike", "spiking", "neuromorphic", "snn", "memristor", "event",
        "brain-inspired", "neuro-inspired", "biological", "plasticity"
    ],
    "signal-control-systems": [
        "signal", "filter", "audio", "speech", "sensor", "wavelet",
        "frequency", "spectrum", "oscillator", "rhythm", "phase"
    ],
    "reinforcement-learning": [
        "rl", "reward", "policy", "agent", "actor", "critic", "ppo",
        "dpo", "grpo", "reinforcement", "learning"
    ],
    "reasoning-bayesian": [
        "reasoning", "inference", "bayesian", "probabilistic", "uncertainty",
        "belief", "evidence", "causal", "logic"
    ],
    "multi-agent-rl": [
        "multi-agent", "marl", "distributed", "coordination", "collaborative",
        "collective", "swarm", "federated"
    ],
    "knowledge-graph": [
        "knowledge", "graph", "kg", "rdf", "ontology", "semantic",
        "relationship", "entity", "embedding"
    ],
    "healthcare-bio": [
        "health", "clinical", "medical", "biological", "genomic", "drug",
        "therapy", "disease", "patient", "diagnosis"
    ],
    "software-engineering": [
        "software", "engineering", "architecture", "pattern", "refactor",
        "test", "debug", "deploy", "container", "pipeline"
    ],
    "security-privacy": [
        "security", "privacy", "attack", "defense", "adversarial", "robust",
        "vulnerability", "threat", "encryption", "auth"
    ],
    "data-retrieval": [
        "data", "retrieval", "search", "index", "database", "storage",
        "query", "rag", "embedding"
    ],
    "agent-tools": [
        "agent", "tool", "workflow", "automation", "orchestration",
        "planning", "task", "execution"
    ],
    "general-ml": [
        "machine", "learning", "ml", "model", "training", "optimization",
        "gradient", "loss", "feature", "representation"
    ],
    "physics-math": [
        "physics", "mathematical", "equation", "dynamics", "mechanics",
        "quantum", "field", "tensor", "geometry", "algebra"
    ],
    "deployment-optimization": [
        "deployment", "optimization", "performance", "efficiency", "scaling",
        "inference", "compression", "quantization"
    ],
    "memory": [
        "memory", "forgetting", "recall", "storage", "consolidation",
        "retention"
    ]
}


def classify_other_skill(skill_name: str) -> str:
    """将 other 技能细分到更具体的类别"""
    skill_lower = skill_name.lower()
    
    for sub_domain, keywords in SUB_DOMAIN_KEYWORDS.items():
        for keyword in keywords:
            if keyword in skill_lower:
                return sub_domain
    
    return "other"


def build_sub_migration_plan():
    """构建 other 类别的细分迁移计划"""
    if not OTHER_DIR.exists():
        print("Error: 'other' directory does not exist")
        return []
    
    skills = []
    
    for skill_dir in OTHER_DIR.iterdir():
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
            skill_name = skill_dir.name
            sub_domain = classify_other_skill(skill_name)
            skills.append({
                "name": skill_name,
                "domain": sub_domain,
                "source": f"collection/skills/other/{skill_name}",
                "target": f"collection/skills/{sub_domain}/{skill_name}"
            })
    
    # 统计
    domain_counts = defaultdict(int)
    for skill in skills:
        domain_counts[skill["domain"]] += 1
    
    print("\n" + "="*60)
    print("'other' Sub-domain Classification Statistics")
    print("="*60)
    for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
        print(f"{domain:30s}: {count:4d} skills")
    print("="*60)
    print(f"Total: {len(skills)} skills in 'other'")
    
    return skills


def execute_sub_migration(plan: list):
    """执行细分迁移"""
    print("\n" + "="*60)
    print("Executing 'other' Sub-domain Migration")
    print("="*60)
    
    # 创建目标目录
    domains = set(skill["domain"] for skill in plan)
    for domain in domains:
        if domain != "other":
            domain_dir = SKILLS_DIR / domain
            if not domain_dir.exists():
                domain_dir.mkdir(parents=True)
                print(f"Created directory: {domain_dir}")
    
    success_count = 0
    errors = []
    
    for i, skill in enumerate(plan, 1):
        if skill["domain"] == "other":
            continue  # 保持真正的 other
        
        source = BASE_DIR / skill["source"]
        target = BASE_DIR / skill["target"]
        
        print(f"  [{i}/{len(plan)}] {skill['name']} → {skill['domain']}/")
        
        try:
            cmd = ["git", "mv", str(source), str(target)]
            subprocess.run(cmd, cwd=BASE_DIR, check=True, capture_output=True)
            success_count += 1
        except subprocess.CalledProcessError:
            try:
                subprocess.run(["mv", str(source), str(target)], check=True)
                success_count += 1
            except subprocess.CalledProcessError as e:
                errors.append({"skill": skill["name"], "error": str(e)})
    
    print("\n" + "="*60)
    print(f"Successfully migrated: {success_count}")
    print(f"Remaining in 'other': {len([s for s in plan if s['domain'] == 'other'])}")
    print(f"Errors: {len(errors)}")
    print("="*60)
    
    return success_count, errors


def main():
    print("Building sub-domain classification for 'other' skills...")
    plan = build_sub_migration_plan()
    
    if plan:
        execute_sub_migration(plan)
        print("\n✓ Sub-domain migration complete!")
        print("Next: git commit -m 'refactor: further organize other skills by sub-domain'")


if __name__ == "__main__":
    main()