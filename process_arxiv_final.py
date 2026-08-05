#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from collections import defaultdict, Counter

REPO_ROOT = Path(__file__).resolve().parent
SKILLS_DIR = REPO_ROOT / "collection" / "skills"
INDEX_FILE = REPO_ROOT / "collection" / "skills" / "INDEX.md"
INDEX_JSON = REPO_ROOT / "knowledge" / "arxiv" / "index.json"
FETCH_OUTPUT = Path('/tmp/fetch_output.txt')

# Add scripts directory to path to import classify_skills
sys.path.insert(0, str(REPO_ROOT / 'scripts'))
from classify_skills import CLASSIFICATION_RULES

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

def parse_fetch_output(output):
    papers = []
    lines = output.split('\\n')
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

def classify_skill(skill_name):
    name_lower = skill_name.lower()
    for keywords, category in CLASSIFICATION_RULES:
        if any(kw in name_lower for kw in keywords):
            return category
    return None

def main():
    # Step 1: Ensure we are on the latest main
    print("Syncing with remote main...")
    try:
        subprocess.run(["git", "fetch", "origin"], check=True)
        subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)
        print("Synced.")
    except subprocess.CalledProcessError as e:
        print(f"Warning: git sync failed: {e}")
        # Continue anyway

    # Step 2: Fetch fresh arXiv data
    print("Fetching latest arXiv papers...")
    import urllib.request
    import urllib.parse
    import xml.etree.ElementTree as ET
    from datetime import datetime, timedelta

    categories = ['cs.AI', 'cs.NE', 'cs.LG', 'q-bio.NC']
    base_url = 'http://export.arxiv.org/api/query?'

    def fetch_arxiv_query(query, max_results=50):
        params = {
            'search_query': query,
            'start': 0,
            'max_results': max_results,
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }
        query_string = urllib.parse.urlencode(params)
        url = base_url + query_string
        try:
            with urllib.request.urlopen(url) as response:
                return response.read()
        except Exception as e:
            print(f"Error fetching {url}: {e}", file=sys.stderr)
            return None

    def parse_feed(xml_data):
        if not xml_data:
            return []
        root = ET.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        entries = []
        for entry in root.findall('atom:entry', ns):
            id_elem = entry.find('atom:id', ns)
            title_elem = entry.find('atom:title', ns)
            summary_elem = entry.find('atom:summary', ns)
            authors = [author.find('atom:name', ns).text for author in entry.findall('atom:author', ns) if author.find('atom:name', ns) is not None]
            published = entry.find('atom:published', ns)
            link = entry.find('atom:id', ns)
            if id_elem is not None and title_elem is not None:
                arxiv_id = id_elem.text.split('/')[-1]
                title = title_elem.text.strip()
                summary = summary_elem.text.strip() if summary_elem is not None else ''
                authors_str = ', '.join(authors)
                url = link.text if link is not None else ''
                entries.append({
                    'id': arxiv_id,
                    'title': title,
                    'summary': summary,
                    'authors': authors_str,
                    'url': url,
                    'published': published.text if published is not None else ''
                })
        return entries

    def compute_utility(entry):
        utility = 0.5
        try:
            pub_date = datetime.strptime(entry['published'], '%Y-%m-%dT%H:%M:%SZ')
            if datetime.now() - pub_date < timedelta(days=3):
                utility += 0.3
        except:
            pass
        if entry['summary']:
            utility += 0.2
        return min(utility, 1.0)

    all_entries = []
    for cat in categories:
        query = f'cat:{cat}'
        print(f"Fetching category {cat}...", file=sys.stderr)
        xml = fetch_arxiv_query(query, max_results=100)
        if xml is None:
            continue
        entries = parse_feed(xml)
        for e in entries:
            e['category'] = cat
            all_entries.append(e)
    # Deduplicate by arxiv id
    seen = set()
    unique = []
    for e in all_entries:
        if e['id'] not in seen:
            seen.add(e['id'])
            unique.append(e)
    # Sort by published date descending
    try:
        unique.sort(key=lambda x: x['published'], reverse=True)
    except:
        pass
    # Compute utility and filter
    papers = []
    for idx, entry in enumerate(unique, start=1):
        utility = compute_utility(entry)
        if utility >= 0.85:
            papers.append((idx, entry, utility))
    # Output in the expected format (to /tmp/fetch_output.txt for consistency)
    out_lines = []
    for rank, entry, utility in papers:
        out_lines.append(f'⭐  {rank}. [{entry["id"]}] Utility: {utility:.2f}')
        out_lines.append(f'     Title: {entry["title"]}')
        out_lines.append(f'     Authors: {entry["authors"]}')
        out_lines.append(f'     URL: {entry["url"]}')
        out_lines.append('')  # empty line between entries
    with open(FETCH_OUTPUT, 'w') as f:
        f.write('\\n'.join(out_lines))
    print(f"Fetched {len(papers)} papers with utility >= 0.85", file=sys.stderr)

    # Now read the fetch output we just wrote
    output = FETCH_OUTPUT.read_text()
    papers = parse_fetch_output(output)
    print(f"Found {len(papers)} papers with utility >= 0.85 from fetch output.")
    
    # Load existing index.json
    index_data = load_index_json()
    
    # We'll ensure that for each paper, there is a skill directory (in correct category) and an entry in index.json.
    created_count = 0
    for paper in papers:
        arxiv_id = paper['id']
        skill_dir_name = get_skill_dir_name(arxiv_id, paper['title'])
        # Determine category
        category = classify_skill(skill_dir_name)
        if category is None:
            category = 'other'
        # Ensure the category directory exists
        category_dir = SKILLS_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)
        skill_dir = category_dir / skill_dir_name
        if not skill_dir.exists():
            # Create the directory
            skill_dir.mkdir(parents=True)
            # Create SKILL.md
            skill_md = skill_dir / 'SKILL.md'
            content = f"""--
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
--

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
            created_count += 1
            print(f"Created skill directory: {skill_dir}")
        else:
            # Directory already exists; we can optionally update the SKILL.md, but we skip for now.
            pass
    
    print(f"Created {created_count} new skill directories.")
    
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
            # Ensure skillCreated is set to the directory name
            index_data[arxiv_id]['skillCreated'] = skill_dir_name
            updated_count += 1
        else:
            # Add new entry
            index_data[arxiv_id] = {
                "title": paper['title'],
                "file": f"collection/skills/{category}/{skill_dir_name}/SKILL.md",
                "keywords": [],
                "utility": paper['utility'],
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
    
    # Now update INDEX.md with a section for today
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
    section_lines = [f"\\n## {today} - arXiv Paper Skills (Cron Job)\\n"]
    # Group by category
    by_category = defaultdict(list)
    for arxiv_id, (category, skill_dir_name) in paper_info.items():
        paper = next(p for p in papers if p['id'] == arxiv_id)
        by_category[category].append((paper, skill_dir_name))
    
    # Sort categories for consistent output (optional)
    for category in sorted(by_category.keys()):
        # Make the category name more readable for the section header
        category_display = category.replace('-', ' ').title()
        section_lines.append(f"### {category_display}\\n")
        for paper, skill_dir_name in by_category[category]:
            # Format: - [[skill_dir_name]] - Title (arXiv: ID) (utility=X.XX)
            section_lines.append(f"- [[{skill_dir_name}]] - {paper['title']} (arXiv: {paper['id']}) (utility={paper['utility']:.2f})\\n")
        section_lines.append("\\n")  # empty line after category
    
    # Prepend the new section to the existing index_md
    index_md = load_index_md()
    new_content = "".join(section_lines) + index_md
    save_index_md(new_content)
    print(f"Updated {INDEX_FILE} with new section for {today}.")
    
    # Run the classification script to ensure no flat skills remain
    print("Running classification script...")
    result = subprocess.run([sys.executable, str(REPO_ROOT / 'scripts' / 'classify_skills.py')], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Classification script failed: {result.stderr}")
    else:
        print("Classification script completed.")
        # Show summary of moved/skipped
        lines = result.stdout.strip().split('\\n')
        for line in lines[-10:]:
            print(line)
    
    # Finally, run the neural map update script
    print("Updating neural map...")
    subprocess.run([sys.executable, str(REPO_ROOT / 'scripts' / 'update_neural_map.py')], check=True)
    print("Neural map updated.")
    
    # Print summary
    print("\\nSummary:")
    print(f"  Total papers processed: {len(papers)}")
    print(f"  New skill directories created: {created_count}")
    # Count by category
    cat_counts = Counter([category for _, (category, _) in paper_info.items()])
    for cat, cnt in cat_counts.most_common():
        print(f"  {cat}: {cnt}")
    
    # Git commit and push
    print("\\nCommitting and pushing changes...")
    try:
        # Change to the repo root
        os.chdir(REPO_ROOT)
        # Add all changes
        subprocess.run(["git", "add", "-A"], check=True)
        # Commit
        commit_msg = f"feat: add paper skills from arXiv {date.today().isoformat()}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        # Push
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Successfully committed and pushed.")
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")
        # Don't exit with error because the main task is done, but we note the failure.

if __name__ == '__main__':
    main()
