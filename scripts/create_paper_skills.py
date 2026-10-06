#!/usr/bin/env python3
"""
Create skill files for high-utility arXiv papers.
"""
import json
import os
import re
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "collection" / "skills"
INDEX_JSON = REPO_ROOT / "knowledge" / "arxiv" / "index.json"
INDEX_MD = REPO_ROOT / "INDEX.md"

# Classification rules (simplified from classify_skills.py)
CATEGORY_RULES = [
    # Neuroscience
    (['brain', 'neural', 'neuro', 'eeg', 'fmri', 'bci', 'cortex', 'synapt', 'cognitive',
      'electrophysiology', 'neuron', 'spike', 'connectome', 'neuromodulation'], 'neuroscience'),
    # Quantum
    (['quantum', 'qubit', 'qec', 'qaoa', 'vqe', 'qml', 'qnn', 'entanglement', 'pauli',
      'hamiltonian'], 'quantum'),
    # Spiking/Neuromorphic
    (['spiking', 'snn', 'neuromorphic', 'stdp', 'spike'], 'spiking-neuromorphic'),
    # Multi-agent/RL
    (['multi-agent', 'reinforcement', 'agent', 'agentic', 'ppo', 'grpo', 'rlvr',
      'delegation', 'collaboration', 'orchestrat'], 'multi-agent-rl'),
    # NLP/LLM
    (['llm', 'transformer', 'gpt', 'bert', 'nlp', 'prompt', 'rag', 'language model',
      'diffusion transformer', 'dit'], 'nlp-llm'),
    # Signal/Control/Systems
    (['control', 'mpc', 'kalman', 'feedback', 'cps', 'robot', 'manipulation'], 'signal-control-systems'),
    # General ML
    (['deep learning', 'gradient', 'moe', 'distillation', 'pruning', 'memory',
      'attention', 'flow matching', 'generative', 'world model'], 'general-ml'),
    # Physics/Math
    (['physics', 'pde', 'topology', 'chaos', 'stochastic', 'tensor', 'wasserstein'], 'physics-math'),
    # Vision/Generative
    (['vision', 'image', 'video', 'gan', 'diffusion', 'segmentation', 'visual'], 'vision-generative'),
    # AI Safety/Eval
    (['safety', 'alignment', 'benchmark', 'eval'], 'ai-safety-eval'),
    # Security/Privacy
    (['security', 'privacy', 'encryption', 'cryptography', 'iot'], 'security-privacy'),
    # Healthcare/Bio
    (['healthcare', 'biomedical', 'clinical', 'drug', 'patient', 'medical', 'brain trace'], 'healthcare-bio'),
    # Finance
    (['finance', 'portfolio', 'stock', 'trading', 'market'], 'finance'),
    # Tools/Frameworks
    (['claude-code', 'opencode', 'copilot', 'cli', 'harness', 'protocol'], 'tools-frameworks'),
]

def classify_paper(paper):
    """Classify paper into category based on title and summary."""
    text = (paper['title'] + ' ' + paper['summary']).lower()
    
    for keywords, category in CATEGORY_RULES:
        for kw in keywords:
            if kw in text:
                return category
    
    return 'other'

def create_skill_name(title):
    """Create a skill name from paper title."""
    # Remove special chars, take first few words
    name = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower())
    words = name.split()[:6]
    return '-'.join(words)

def create_skill_md(paper, category):
    """Create SKILL.md content for a paper."""
    skill_name = create_skill_name(paper['title'])
    
    # Extract key concepts from summary
    summary = paper['summary']
    
    # Create activation keywords
    activation_words = []
    for word in paper['title'].split():
        clean = re.sub(r'[^a-zA-Z]', '', word)
        if len(clean) > 3 and clean.lower() not in ['the', 'and', 'for', 'with', 'from', 'using']:
            activation_words.append(clean.lower())
    activation = ', '.join(activation_words[:10])
    
    content = f"""---
name: {skill_name}
description: "{paper['title'][:50]}..."
tags: [{', '.join(paper['categories'][:3])}]
source: arxiv
arxiv_id: {paper['id']}
utility: {paper['utility']}
published: {paper['published']}
---

# {paper['title']}

**Authors:** {paper['authors']}
**Published:** {paper['published']}
**arXiv:** [{paper['id']}]({paper['url']})
**Categories:** {', '.join(paper['categories'])}
**Utility Score:** {paper['utility']}

## Abstract

{paper['summary'][:1500]}

## Key Contributions

- Novel research in {', '.join(paper['categories'][:2])}
- Published {paper['published']}

## Activation

{activation}
"""
    return content, skill_name

# Load scored papers
with open('/tmp/scored_papers.json') as f:
    scored_papers = json.load(f)

print(f"Creating skills for {len(scored_papers)} papers...")

# Load existing index
if INDEX_JSON.exists():
    with open(INDEX_JSON) as f:
        existing_index = json.load(f)
else:
    existing_index = []

existing_ids = {e['id'] for e in existing_index}

# Track new entries
new_entries = []
new_index_entries = []
today = datetime.now().strftime('%Y-%m-%d')

for paper in scored_papers:
    if paper['id'] in existing_ids:
        print(f"  Skipping {paper['id']} (already exists)")
        continue
    
    category = classify_paper(paper)
    skill_content, skill_name = create_skill_md(paper, category)
    
    # Create directory
    skill_dir = SKILLS_DIR / category / skill_name
    skill_dir.mkdir(parents=True, exist_ok=True)
    
    # Write SKILL.md
    skill_file = skill_dir / "SKILL.md"
    with open(skill_file, 'w') as f:
        f.write(skill_content)
    
    print(f"  Created: {category}/{skill_name}")
    
    # Track for index
    new_index_entries.append({
        'id': paper['id'],
        'title': paper['title'],
        'authors': paper['authors'],
        'url': paper['url'],
        'utility': paper['utility'],
        'categories': paper['categories'],
        'published': paper['published'],
        'skill_dir': str(skill_dir),
        'skill_category': category
    })
    
    # Track for INDEX.md
    new_entries.append({
        'title': paper['title'],
        'skill_name': skill_name,
        'category': category,
        'arxiv_id': paper['id'],
        'summary': paper['summary'][:300]
    })

# Update knowledge/arxiv/index.json
existing_index.extend(new_index_entries)
with open(INDEX_JSON, 'w') as f:
    json.dump(existing_index, f, indent=2)
print(f"Updated index.json: {len(existing_index)} total entries")

# Update INDEX.md
if INDEX_MD.exists():
    with open(INDEX_MD, 'r') as f:
        existing_content = f.read()
else:
    existing_content = "# AI Collection Index\n\n"

# Build new INDEX.md entries
new_md_content = f"## {today} - High-Utility arXiv Papers (Cron Job)\n\n"
for entry in new_entries:
    new_md_content += f"### {entry['title']}\n"
    new_md_content += f"- [[{entry['skill_name']}]] - {entry['summary'][:200]}... (arXiv: {entry['arxiv_id']})\n"
    new_md_content += f"  - Category: {entry['category']}\n\n"

# Prepend new content after the first heading
lines = existing_content.split('\n')
insert_idx = 0
for i, line in enumerate(lines):
    if line.startswith('# '):
        insert_idx = i + 1
        break

new_content = '\n'.join(lines[:insert_idx]) + '\n\n' + new_md_content + '\n'.join(lines[insert_idx:])

with open(INDEX_MD, 'w') as f:
    f.write(new_content)
print(f"Updated INDEX.md with {len(new_entries)} new entries")

print(f"\nSummary:")
print(f"  - Created {len(new_entries)} new skills")
print(f"  - Updated index.json ({len(existing_index)} total)")
print(f"  - Updated INDEX.md")
