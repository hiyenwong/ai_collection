#!/usr/bin/env python3
"""
Update INDEX.md and knowledge/arxiv/index.json with new paper skills from the latest fetch.
"""
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "collection" / "skills"
INDEX_FILE = REPO_ROOT / "collection" / "skills" / "INDEX.md"
INDEX_JSON = REPO_ROOT / "knowledge" / "arxiv" / "index.json"
FETCH_OUTPUT = Path('/tmp/fetch_output.txt')

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '-', text)
    text = re.sub(r'\s+', '-', text)
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

def parse_fetch_output(output):
    papers = []
    lines = output.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        match = re.match(r'^[·⭐]\s+(\d+)\.\s+\[(.+?)\]\s+Utility:\s+([0-9.]+)', line)
        if match:
            rank = int(match.group(1))
            paper_id = match.group(2)
            utility = float(match.group(3))
            i += 1
            if i >= len(lines):
                break
            title_line = lines[i]
            title_match = re.match(r'^\s{5}Title:\s+(.+)', title_line)
            if not title_match:
                title_match = re.match(r'^\s*Title:\s+(.+)', title_line)
            if title_match:
                title = title_match.group(1).strip()
            else:
                title = ""
            i += 1
            if i >= len(lines):
                break
            authors_line = lines[i]
            authors_match = re.match(r'^\s{5}Authors:\s+(.+)', authors_line)
            if not authors_match:
                authors_match = re.match(r'^\s*Authors:\s+(.+)', authors_line)
            if authors_match:
                authors = authors_match.group(1).strip()
            else:
                authors = ""
            i += 1
            if i >= len(lines):
                break
            url_line = lines[i]
            url_match = re.match(r'^\s{5}URL:\s+(.+)', url_line)
            if not url_match:
                url_match = re.match(r'^\s*URL:\s+(.+)', url_line)
            if url_match:
                url = url_match.group(1).strip()
            else:
                url = ""
            papers.append({
                'rank': rank,
                'id': paper_id,
                'title': title,
                'authors': authors,
                'url': url,
                'utility': utility
            })
        i += 1
    return papers

def load_index_json():
    if INDEX_JSON.exists():
        with open(INDEX_JSON, 'r') as f:
            return json.load(f)
    return {}

def save_index_json(data):
    with open(INDEX_JSON, 'w') as f:
        json.dump(data, f, indent=2)

def load_index_md():
    if INDEX_FILE.exists():
        with open(INDEX_FILE, 'r') as f:
            return f.read()
    return ""

def save_index_md(content):
    with open(INDEX_FILE, 'w') as f:
        f.write(content)

def main():
    # Read the fetch output from the file we saved earlier
    if not FETCH_OUTPUT.exists():
        print("Fetch output file not found.")
        sys.exit(1)
    output = FETCH_OUTPUT.read_text()
    papers = parse_fetch_output(output)
    print(f"Found {len(papers)} papers with utility >= 0.85 from fetch output.")
    
    # Load existing index.json
    index_data = load_index_json()
    
    # We'll ensure that for each paper, there is a skill directory (flat) and an entry in index.json.
    # First, create missing skill directories flat under SKILLS_DIR.
    created_flat = 0
    for paper in papers:
        arxiv_id = paper['id']
        skill_dir_name = get_skill_dir_name(arxiv_id, paper['title'])
        flat_dir = SKILLS_DIR / skill_dir_name
        if not flat_dir.exists():
            # Create the directory
            flat_dir.mkdir(parents=True)
            # Create SKILL.md
            skill_md = flat_dir / 'SKILL.md'
            content = f"""---
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

# {paper["title"]}

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
            skill_md.write_text(content)
            created_flat += 1
            print(f"Created flat skill directory: {skill_dir_name}")
        else:
            # Directory already exists; we can optionally update the SKILL.md, but we skip for now.
            pass
    
    print(f"Created {created_flat} new flat skill directories.")
    
    # Now run the classification script to move them to the correct category
    print("Running classification script...")
    result = subprocess.run([sys.executable, str(REPO_ROOT / 'scripts' / 'classify_skills.py')], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Classification script failed: {result.stderr}")
    else:
        print("Classification script completed.")
        # Show summary
        lines = result.stdout.strip().split('\n')
        for line in lines[-10:]:
            print(line)
    
    # Now, for each paper, find the actual skill directory (now in the correct category)
    updated_count = 0
    for paper in papers:
        arxiv_id = paper['id']
        skill_dir_name = get_skill_dir_name(arxiv_id, paper['title'])
        # Search for this directory under SKILLS_DIR
        found = None
        for category_dir in SKILLS_DIR.iterdir():
            if not category_dir.is_dir():
                continue
            candidate = category_dir / skill_dir_name
            if candidate.is_dir():
                found = (category_dir.name, skill_dir_name)
                break
        if found is None:
            print(f"Warning: Could not find skill directory for {arxiv_id} after classification.")
            continue
        category, _ = found
        # Update index.json
        if arxiv_id in index_data:
            # Update the entry
            index_data[arxiv_id]['file'] = f"collection/skills/{category}/{skill_dir_name}/SKILL.md"
            index_data[arxiv_id]['category'] = category
            # Ensure skillCreated is set to the directory name (should already be)
            index_data[arxiv_id]['skillCreated'] = skill_dir_name
            updated_count += 1
        else:
            # Add new entry
            index_data[arxiv_id] = {
                "title": paper["title"],
                "file": f"collection/skills/{category}/{skill_dir_name}/SKILL.md",
                "keywords": [],
                "utility": paper["utility"],
                "skillCreated": skill_dir_name,
                "lastAccessed": date.today().isoformat(),
                "category": category
            }
            updated_count += 1
    
    if updated_count > 0:
        save_index_json(index_data)
        print(f"Updated {updated_count} entries in {INDEX_JSON} with correct categories and paths.")
    else:
        print("No entries to update in index.json.")
    
    # Now update INDEX.md with a section for today.
    # We'll use the papers list and the updated index_data to get the correct category and file.
    # Let's rebuild the mapping from arxiv_id to (category, skill_dir_name) by scanning again.
    paper_info = {}
    for paper in papers:
        arxiv_id = paper['id']
        skill_dir_name = get_skill_dir_name(arxiv_id, paper['title'])
        found = None
        for category_dir in SKILLS_DIR.iterdir():
            if not category_dir.is_dir():
                continue
            candidate = category_dir / skill_dir_name
            if candidate.is_dir():
                found = (category_dir.name, skill_dir_name)
                break
        if found:
            paper_info[arxiv_id] = found
        else:
            print(f"Warning: Could not find {arxiv_id} for INDEX.md.")
    
    # Build the new section for INDEX.md
    today = date.today().isoformat()
    section_lines = [f"\n## {today} - arXiv Paper Skills (Cron Job)\n"]
    # Group by category
    from collections import defaultdict
    by_category = defaultdict(list)
    for arxiv_id, (category, skill_dir_name) in paper_info.items():
        paper = next(p for p in papers if p['id'] == arxiv_id)
        by_category[category].append((paper, skill_dir_name))
    
    # Sort categories for consistent output (optional)
    for category in sorted(by_category.keys()):
        # Make the category name more readable for the section header
        # Replace hyphens with spaces and title case
        category_display = category.replace('-', ' ').title()
        section_lines.append(f"### {category_display}\n")
        for paper, skill_dir_name in by_category[category]:
            # Format: - [[skill_dir_name]] - Title (arXiv: ID) (utility=X.XX)
            section_lines.append(f"- [[{skill_dir_name}]] - {paper['title']} (arXiv: {paper['id']}) (utility={paper['utility']:.2f})\n")
        section_lines.append("\n")  # empty line after category
    
    # Prepend the new section to the existing index_md
    index_md = load_index_md()
    new_content = "".join(section_lines) + index_md
    save_index_md(new_content)
    print(f"Updated {INDEX_FILE} with new section for {today}.")
    
    # Finally, run the neural map update script
    print("Updating neural map...")
    subprocess.run([sys.executable, str(REPO_ROOT / 'scripts' / 'update_neural_map.py')], check=True)
    print("Neural map updated.")

if __name__ == '__main__':
    main()