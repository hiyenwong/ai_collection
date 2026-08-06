#!/usr/bin/env python3
import os
import re
import json
import subprocess
import sys
from pathlib import Path
from datetime import date

# Paths
REPO_ROOT = Path('/Users/hiyenwong/projects/ai_projects/ai_collection')
SKILLS_DIR = REPO_ROOT / 'collection' / 'skills'
INDEX_FILE = REPO_ROOT / 'collection' / 'skills' / 'INDEX.md'
INDEX_JSON = REPO_ROOT / 'knowledge' / 'arxiv' / 'index.json'
FETCH_OUTPUT = Path('/tmp/fetch_output.txt')

def parse_fetch(output):
    papers = []
    lines = output.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^[·⭐]\\s+(\\d+)\\.\\s+\\[(.+?)\\]\\s+Utility:\\s+([0-9.]+)', line)
        if m:
            rank = int(m.group(1))
            paper_id = m.group(2)
            utility = float(m.group(3))
            i += 1
            if i >= len(lines): break
            title_line = lines[i]
            title_m = re.match(r'^\\s{5}Title:\\s+(.+)', title_line)
            if not title_m:
                title_m = re.match(r'^\\s*Title:\\s+(.+)', title_line)
            if title_m:
                title = title_m.group(1).strip()
            else:
                title = ""
            i += 1
            if i >= len(lines): break
            authors_line = lines[i]
            authors_m = re.match(r'^\\s{5}Authors:\\s+(.+)', authors_line)
            if not authors_m:
                authors_m = re.match(r'^\\s*Authors:\\s+(.+)', authors_line)
            if authors_m:
                authors = authors_m.group(1).strip()
            else:
                authors = ""
            i += 1
            if i >= len(lines): break
            url_line = lines[i]
            url_m = re.match(r'^\\s{5}URL:\\s+(.+)', url_line)
            if not url_m:
                url_m = re.match(r'^\\s*URL:\\s+(.+)', url_line)
            if url_m:
                url = url_m.group(1).strip()
            else:
                url = ""
            papers.append({'id': paper_id, 'title': title, 'authors': authors, 'url': url, 'utility': utility})
        i += 1
    return papers

def classify_title(title):
    t = title.lower()
    # neuroscience
    if any(k in t for k in ['brain', 'neural', 'neuro', 'eeg', 'fmri', 'bci', 'cortex', 'synapt', 'cognitive']):
        return 'neuroscience'
    # quantum
    if any(k in t for k in ['quantum', 'qubit', 'qec', 'qaoa', 'vqe', 'qml', 'qnn', 'entanglement', 'pauli']):
        return 'quantum'
    # spiking-neuromorphic
    if any(k in t for k in ['spiking', 'snn', 'neuromorphic', 'stdp', 'spike', 'lif']):
        return 'spiking-neuromorphic'
    # multi-agent-rl
    if any(k in t for k in ['multi-agent', 'reinforcement', 'agent', 'agentic', 'ppo', 'grpo']):
        return 'multi-agent-rl'
    # nlp-llm
    if any(k in t for k in ['llm', 'transformer', 'gpt', 'bert', 'nlp', 'prompt', 'rag']):
        return 'nlp-llm'
    # signal-control-systems
    if any(k in t for k in ['control', 'mpc', 'kalman', 'feedback', 'cps']):
        return 'signal-control-systems'
    # general-ml
    if any(k in t for k in ['deep-learning', 'gradient', 'moe', 'distillation', 'pruning']):
        return 'general-ml'
    # physics-math
    if any(k in t for k in ['physics', 'pde', 'topology', 'chaos', 'stochastic', 'tensor']):
        return 'physics-math'
    # vision-generative
    if any(k in t for k in ['vision', 'image', 'video', 'gan', 'diffusion']):
        return 'vision-generative'
    # ai-safety-eval
    if any(k in t for k in ['ai-safety', 'alignment', 'benchmark', 'eval']):
        return 'ai-safety-eval'
    # security-privacy
    if any(k in t for k in ['security', 'privacy', 'encryption', 'cryptography']):
        return 'security-privacy'
    # healthcare-bio
    if any(k in t for k in ['healthcare', 'biomedical', 'clinical', 'drug']):
        return 'healthcare-bio'
    # finance
    if any(k in t for k in ['finance', 'portfolio', 'stock', 'trading', 'market']):
        return 'finance'
    # tools-frameworks
    if any(k in t for k in ['claude-code', 'opencode', 'copilot', 'cli']):
        return 'tools-frameworks'
    return 'other'

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\\s]', '-', text)
    text = re.sub(r'\\s+', '-', text)
    text = text.strip('-')
    text = re.sub(r'-+', '-', text)
    if len(text) > 100:
        text = text[:100].rstrip('-')
    return text

def get_skill_dir_name(paper_id, title):
    id_part = paper_id.replace('.', '-')
    slug = slugify(title)
    if len(slug) > 50:
        slug = slug[:50].rstrip('-')
    return f"arxiv-{id_part}-{slug}"

def main():
    if not FETCH_OUTPUT.exists():
        print("Fetch output not found")
        sys.exit(1)
    papers = parse_fetch(FETCH_OUTPUT.read_text())
    print(f"Found {len(papers)} papers with utility >= 0.85")
    
    # Load existing index.json (it's a list)
    if INDEX_JSON.exists():
        with open(INDEX_JSON, 'r') as f:
            index_data = json.load(f)
    else:
        index_data = []
    
    # Create a set of existing arxiv ids in index_data for quick lookup
    existing_ids = {entry.get('id') for entry in index_data}
    
    # We'll collect new entries to add
    new_entries = []
    
    for paper in papers:
        arxiv_id = paper['id']
        if arxiv_id in existing_ids:
            print(f"SKIP already in index: {arxiv_id}")
            continue
        skill_dir_name = get_skill_dir_name(arxiv_id, paper['title'])
        category = classify_title(paper['title'])
        # Ensure category directory exists
        cat_dir = SKILLS_DIR / category
        cat_dir.mkdir(parents=True, exist_ok=True)
        skill_dir = cat_dir / skill_dir_name
        if skill_dir.exists():
            print(f"SKIP directory exists: {skill_dir}")
        else:
            skill_dir.mkdir(parents=True)
            # Create SKILL.md
            skill_md = skill_dir / 'SKILL.md'
            # Build content
            yaml_front = f"""---
name: {skill_dir_name}
description: '{paper["title"]} (arXiv: {arxiv_id})'
metadata:
  {{
    "arxiv_id": "{arxiv_id}",
    "utility": {paper["utility"]},
    "title": "{paper["title"]}",
    "authors": "{paper["authors"]}",
    "url": "{paper["url"]}"
  }}
---
"""
            body = f"""# {paper["title"]}

**arXiv ID:** {arxiv_id}
**Authors:** {paper["authors"]}
**URL:** {paper["url"]}
**Utility Score:** {paper["utility"]:.2f}

## Summary

This skill was automatically generated from the arXiv paper titled "{paper["title"]}" (ID: {arxiv_id}).

## Usage

This skill can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: {paper["url"]}
"""
            content = yaml_front + body
            skill_md.write_text(content)
            print(f"Created skill: {skill_dir}")
        # Prepare entry for index.json
        entry = {
            "id": arxiv_id,
            "title": paper["title"],
            "skill_name": skill_dir_name,
            "category": category,
            "utility": paper["utility"],
            "date_added": date.today().isoformat()
        }
        new_entries.append(entry)
    
    if new_entries:
        # Append new entries to the list
        index_data.extend(new_entries)
        # Write back
        with open(INDEX_JSON, 'w') as f:
            json.dump(index_data, f, indent=2)
        print(f"Added {len(new_entries)} new entries to {INDEX_JSON}")
    else:
        print("No new entries to add to index.json")
    
    # Update INDEX.md: add a section at the top for today
    if INDEX_FILE.exists():
        with open(INDEX_FILE, 'r') as f:
            index_md_content = f.read()
    else:
        index_md_content = ""
    
    today = date.today().isoformat()
    # Build new section
    section_lines = [f"\\n## {today} - arXiv Paper Skills (Cron Job)\\n"]
    # Group new entries by category
    from collections import defaultdict
    by_category = defaultdict(list)
    for entry in new_entries:
        by_category[entry['category']].append(entry)
    
    for category in sorted(by_category.keys()):
        category_display = category.replace('-', ' ').title()
        section_lines.append(f"### {category_display}\\n")
        for entry in by_category[category]:
            skill_dir_name = get_skill_dir_name(entry['id'], entry['title'])
            section_lines.append(f"- [[{skill_dir_name}]] - {entry['title']} (arXiv: {entry['id']}) (utility={entry['utility']:.2f})\\n")
        section_lines.append("\\n")
    
    new_index_md = "".join(section_lines) + index_md_content
    with open(INDEX_FILE, 'w') as f:
        f.write(new_index_md)
    print(f"Updated {INDEX_FILE} with new section for {today}")
    
    # Finally, run the neural map update script
    print("Updating neural map...")
    subprocess.run([sys.executable, str(REPO_ROOT / 'scripts' / 'update_neural_map.py')], check=True)
    print("Neural map updated.")

if __name__ == '__main__':
    main()