#!/usr/bin/env python3
"""
Process arXiv papers: filter by utility, create skills, update indices.
"""
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "collection" / "skills"
INDEX_JSON = REPO_ROOT / "knowledge" / "arxiv" / "index.json"
INDEX_MD = REPO_ROOT / "INDEX.md"

# Load existing processed IDs
existing_ids = set()
if INDEX_JSON.exists():
    with open(INDEX_JSON) as f:
        data = json.load(f)
        existing_ids = {e['id'] for e in data}

# Load new papers
with open('/tmp/arxiv_latest.json') as f:
    content = f.read()
    # Extract JSON array (before the "--- Total" line)
    json_part = content.rsplit('--- Total', 1)[0].strip()
    papers = json.loads(json_part)

# Filter out already processed
new_papers = [p for p in papers if p['id'] not in existing_ids]
print(f"New papers: {len(new_papers)} (out of {len(papers)} fetched, {len(existing_ids)} already processed)")

# Utility scoring function
def score_utility(paper):
    """Score paper utility 0-1 based on keywords and categories."""
    score = 0.5  # base
    
    title = paper['title'].lower()
    summary = paper['summary'].lower()
    cats = paper['categories']
    text = title + ' ' + summary
    
    # High-value topics
    high_value = [
        'multi-agent', 'agentic', 'reinforcement learning', 'rlvr', 'grpo',
        'neuroscience', 'brain', 'neural', 'spiking', 'neuromorphic',
        'quantum', 'qubit', 'qec', 'llm', 'transformer', 'reasoning',
        'self-evolving', 'self-improving', 'autonomous', 'emergent',
        'memory', 'credit assignment', 'planning', 'tool use',
        'safety', 'alignment', 'benchmark', 'evaluation',
        'distillation', 'pruning', 'efficiency', 'scaling',
        'diffusion', 'generative', 'vision', 'multimodal',
        'control', 'robotics', 'embodied', 'manipulation',
        'graph', 'topology', 'causal', 'bayesian',
        'privacy', 'security', 'federated', 'encryption',
        'finance', 'trading', 'portfolio', 'market',
        'healthcare', 'clinical', 'drug', 'biomedical',
    ]
    
    for kw in high_value:
        if kw in text:
            score += 0.05
    
    # Primary categories boost
    primary_cats = {'cs.AI', 'cs.LG', 'cs.NE', 'cs.MA', 'q-bio.NC'}
    if any(c in primary_cats for c in cats):
        score += 0.1
    
    # Novelty indicators
    novelty = ['novel', 'first', 'state-of-the-art', 'sota', 'breakthrough', 'new framework', 'new approach']
    for kw in novelty:
        if kw in text:
            score += 0.03
    
    # Practical applicability
    practical = ['benchmark', 'evaluation', 'empirical', 'experiment', 'dataset', 'real-world', 'application']
    for kw in practical:
        if kw in text:
            score += 0.02
    
    return min(score, 1.0)

# Score and filter
scored_papers = []
for p in new_papers:
    utility = score_utility(p)
    if utility >= 0.85:
        p['utility'] = round(utility, 2)
        scored_papers.append(p)

# Sort by utility descending
scored_papers.sort(key=lambda x: x['utility'], reverse=True)

print(f"Papers with utility >= 0.85: {len(scored_papers)}")
for p in scored_papers[:20]:
    print(f"  [{p['utility']}] {p['title'][:80]}")

# Save scored papers for next step
with open('/tmp/scored_papers.json', 'w') as f:
    json.dump(scored_papers, f, indent=2)
