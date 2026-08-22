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
        match = re.match(r'^[·⭐]\\s+(\\d+)\\.\\s+\\[(.+?)\\]\\s+Utility:\\s+([0-9.]+)', line)
        if match:
            rank = int(match.group(1))
            paper_id = match.group(2)
            utility = float(match.group(3))
            i += 1
            if i >= len(lines):
                break
            title_line = lines[i]
            title_match = re.match(r'^\\s{5}Title:\\s+(.+)', title_line)
            if not title_match:
                title_match = re.match(r'^\\s*Title:\\s+(.+)', title_line)
            if title_match:
                title = title_match.group(1).strip()
            else:
                title = ""
            i += 1
            if i >= len(lines):
                break
            authors_line = lines[i]
            authors_match = re.match(r'^\\s{5}Authors:\\s+(.+)', authors_line)
            if not authors_match:
                authors_match = re.match(r'^\\s*Authors:\\s+(.+)', authors_line)
            if authors_match:
                authors = authors_match.group(1).strip()
            else:
                authors = ""
            i += 1
            if i >= len(lines):
                break
            url_line = lines[i]
            url_match = re.match(r'^\\s{5}URL:\\s+(.+)', url_line)
            if not url_match:
                url_match = re.match(r'^\\s*URL:\\s+(.+)', url_line)
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
    return []

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
    
    # Load existing index.json as a list
    index_list = load_index_json()
    # Convert to dict for easy lookup by id
    index_dict = {item['id']: item for item in index_list}
    
    # We'll ensure that for each paper, there is an entry in index_dict
    updated_count = 0
    for paper in papers:
        arxiv_id = paper['id']
        skill_dir_name = get_skill_dir_name(arxiv_id, paper['title'])
        # Determine category by looking for the skill directory
        category = None
        for category_dir in SKILLS_DIR.iterdir():
            if not category_dir.is_dir():
                continue
            candidate = category_dir / skill_dir_name
            if candidate.is_dir():
                category = category_dir.name
                break
        if category is None:
            # If not found, default to 'other' (should not happen after classification)
            category = 'other'
        # Create or update entry in index_dict
        if arxiv_id in index_dict:
            # Update existing entry
            index_dict[arxiv_id]['title'] = paper['title']
            index_dict[arxiv_id]['skill_name'] = skill_dir_name
            index_dict[arxiv_id]['category'] = category
            index_dict[arxiv_id]['utility'] = paper['utility']
            index_dict[arxiv_id]['date_added'] = date.today().isoformat()
        else:
            # Add new entry
            index_dict[arxiv_id] = {
                'id': arxiv_id,
                'title': paper['title'],
                'skill_name': skill_dir_name,
                'category': category,
                'utility': paper['utility'],
                'date_added': date.today().isoformat()
            }
        updated_count += 1
    
    # Convert back to list
    new_index_list = list(index_dict.values())
    # Sort by date_added descending for consistency? We'll keep as is.
    if updated_count > 0:
        save_index_json(new_index_list)
        print(f"Updated {updated_count} entries in {INDEX_JSON}.")
    else:
        print("No entries to update in index.json.")
    
    # Now update INDEX.md with a section for today.
    # We'll use the papers list and the index_dict to get the correct category and skill_name.
    # Build mapping from arxiv_id to (category, skill_name)
    paper_info = {}
    for paper in papers:
        arxiv_id = paper['id']
        skill_dir_name = get_skill_dir_name(arxiv_id, paper['title'])
        # Find category by scanning again (or we can use the one we found above)
        category = None
        for category_dir in SKILLS_DIR.iterdir():
            if not category_dir.is_dir():
                continue
            candidate = category_dir / skill_dir_name
            if candidate.is_dir():
                category = category_dir.name
                break
        if category is None:
            category = 'other'
        paper_info[arxiv_id] = (category, skill_dir_name)
    
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