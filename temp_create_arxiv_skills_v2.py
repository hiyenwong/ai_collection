#!/usr/bin/env python3
import os
import re
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

PROJECT_ROOT = '/Users/hiyenwong/projects/ai_projects/ai_collection'
COLLECTION_SKILLS_DIR = os.path.join(PROJECT_ROOT, 'collection', 'skills')
CLASSIFY_SCRIPT = os.path.join(PROJECT_ROOT, 'scripts', 'classify_skills.py')
INDEX_MD_PATH = os.path.join(PROJECT_ROOT, 'INDEX.md')
KNOWLEDGE_ARXIV_INDEX_PATH = os.path.join(PROJECT_ROOT, 'knowledge', 'arxiv', 'index.json')
CATEGORIES = ['cs.AI', 'cs.NE', 'cs.LG', 'q-bio.NC']
DAYS_BACK = 2

def log(msg):
    print(f"[LOG] {msg}")

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def load_classification_rules():
    """Load classification rules from classify_skills.py"""
    try:
        with open(CLASSIFY_SCRIPT, 'r') as f:
            content = f.read()
        # Find the CLASSIFICATION_RULES dictionary
        start = content.find('CLASSIFICATION_RULES = {')
        if start == -1:
            log("Could not find CLASSIFICATION_RULES in classify_skills.py")
            return {}
        # Find the matching end brace
        brace_count = 0
        end = start
        for i, ch in enumerate(content[start:], start=start):
            if ch == '{':
                brace_count += 1
            elif ch == '}':
                brace_count -= 1
                if brace_count == 0:
                    end = i + 1
                    break
        rules_str = content[start:end]
        # Evaluate the dictionary string (we trust the source)
        rules = eval(rules_str)
        return rules
    except Exception as e:
        log(f"Error loading classification rules: {e}")
        return {}

def classify_paper(title, abstract, rules):
    """Classify a paper into a category based on title and abstract"""
    text = (title + " " + abstract).lower()
    for category, keywords in rules.items():
        for keyword in keywords:
            if keyword.lower() in text:
                return category
    return 'other'  # Default category

def get_recent_arxiv_papers():
    """Fetch recent arXiv papers from specified categories"""
    # Build arXiv query
    query = ' OR '.join([f'cat:{cat}' for cat in CATEGORIES])
    # Date range: last DAYS_BACK days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=DAYS_BACK)
    # Format: YYYYMMDDHHMM
    start_str = start_date.strftime('%Y%m%d') + '0000'
    end_str = end_date.strftime('%Y%m%d') + '2359'
    date_range = f' submittedDate:[{start_str} TO {end_str}]'
    full_query = f'{query} AND {date_range}'
    # URL encode the query
    encoded_query = urllib.parse.quote(full_query)
    url = f"http://export.arxiv.org/api/query?search_query={encoded_query}&start=0&max_results=100"
    log(f"Fetching from arXiv: {url}")
    
    try:
        response = urllib.request.urlopen(url)
        xml_data = response.read()
        root = ET.fromstring(xml_data)
        
        # Define namespace
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        entries = []
        for entry in root.findall('atom:entry', ns):
            title_elem = entry.find('atom:title', ns)
            summary_elem = entry.find('atom:summary', ns)
            id_elem = entry.find('atom:id', ns)
            if title_elem is None or summary_elem is None or id_elem is None:
                continue
            title = title_elem.text.strip()
            abstract = summary_elem.text.strip()
            arxiv_id = id_elem.text.split('/')[-1]  # Get the ID part
            entries.append({
                'title': title,
                'abstract': abstract,
                'arxiv_id': arxiv_id,
                'url': f"http://arxiv.org/abs/{arxiv_id}"
            })
        return entries
    except Exception as e:
        log(f"Error fetching arXiv papers: {e}")
        return []

def create_skill_for_paper(paper, category):
    """Create a skill directory and SKILL.md for a paper"""
    # Generate skill name from arXiv ID
    skill_name = f"arxiv-{paper['arxiv_id'].replace('.', '-')}"
    skill_dir = os.path.join(COLLECTION_SKILLS_DIR, category, skill_name)
    ensure_dir(skill_dir)
    
    skill_md_path = os.path.join(skill_dir, 'SKILL.md')
    
    # Create SKILL.md content
    template = f"""---
description: "Skill generated from arXiv paper {paper['arxiv_id']}: {paper['title'][:50]}..."
category: "{category}"
---

# {skill_name}

## Purpose
{paper['title']}

## When to Use
Use when you need to apply the techniques from "{paper['title']}" (arXiv:{paper['arxiv_id']}).

## Steps
1. Read the arXiv paper: {paper['url']}
2. Implement the approach described in the paper.

## References
- [arXiv:{paper['arxiv_id']}] {paper['title']} ({paper['url']})
"""
    with open(skill_md_path, 'w') as f:
        f.write(template)
    log(f"Created skill: {skill_md_path}")
    return skill_md_path

def update_index_md(new_papers):
    """Update INDEX.md with new paper entries at the top"""
    # First, try to find INDEX.md
    index_paths = [
        INDEX_MD_PATH,
        os.path.join(PROJECT_ROOT, 'collection', 'skills', 'INDEX.md'),
        os.path.join(PROJECT_ROOT, 'skills', 'INDEX.md')
    ]
    index_path = None
    for path in index_paths:
        if os.path.exists(path):
            index_path = path
            break
    if not index_path:
        log("INDEX.md not found, creating new one at project root")
        index_path = INDEX_MD_PATH
        ensure_dir(os.path.dirname(index_path))
    
    # Read existing content
    try:
        with open(index_path, 'r') as f:
            existing = f.read()
    except:
        existing = ""
    
    # Generate new entries
    new_entries = []
    for paper in new_papers:
        entry = f"- [{paper['arxiv_id']}] {paper['title']} ({paper['url']}) - {datetime.now().strftime('%Y-%m-%d')}"
        new_entries.append(entry)
    
    new_content = "\n".join(new_entries) + "\n\n" + existing if existing else "\n".join(new_entries)
    with open(index_path, 'w') as f:
        f.write(new_content)
    log(f"Updated {index_path} with {len(new_papers)} new entries")

def update_knowledge_arxiv_index(new_papers):
    """Update knowledge/arxiv/index.json with new papers"""
    ensure_dir(os.path.dirname(KNOWLEDGE_ARXIV_INDEX_PATH))
    
    # Read existing index
    try:
        with open(KNOWLEDGE_ARXIV_INDEX_PATH, 'r') as f:
            existing_data = json.load(f)
        if not isinstance(existing_data, list):
            existing_data = []
    except:
        existing_data = []
    
    # Add new papers (avoid duplicates by arxiv_id)
    existing_ids = {p.get('arxiv_id') for p in existing_data if isinstance(p, dict)}
    for paper in new_papers:
        if paper['arxiv_id'] not in existing_ids:
            existing_data.append({
                'arxiv_id': paper['arxiv_id'],
                'title': paper['title'],
                'url': paper['url'],
                'date_added': datetime.now().strftime('%Y-%m-%d')
            })
    
    with open(KNOWLEDGE_ARXIV_INDEX_PATH, 'w') as f:
        json.dump(existing_data, f, indent=2)
    log(f"Updated {KNOWLEDGE_ARXIV_INDEX_PATH} with {len(new_papers)} new papers")

def main():
    log("Starting arXiv paper skill creation")
    
    # Step 1: Get papers
    papers = get_recent_arxiv_papers()
    
    if not papers:
        log("No papers found")
        return
    
    log(f"Found {len(papers)} papers")
    
    # Step 2: Load classification rules
    rules = load_classification_rules()
    if not rules:
        log("Warning: No classification rules found, using default 'other'")
    
    # Step 3: Classify papers and create skills
    created_skills = []
    for paper in papers:
        category = classify_paper(paper['title'], paper['abstract'], rules)
        log(f"Classifying paper {paper['arxiv_id']} as '{category}'")
        skill_path = create_skill_for_paper(paper, category)
        created_skills.append({
            'paper': paper,
            'category': category,
            'skill_path': skill_path
        })
    
    log(f"Created {len(created_skills)} skills")
    
    # Step 4: Update INDEX.md
    update_index_md([cs['paper'] for cs in created_skills])
    
    # Step 5: Update knowledge/arxiv/index.json
    update_knowledge_arxiv_index([cs['paper'] for cs in created_skills])
    
    log("Skill creation completed")

if __name__ == '__main__':
    main()