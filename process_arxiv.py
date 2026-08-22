import os
import re
import json
import sqlite3
from datetime import datetime, timedelta
from urllib import request
import xml.etree.ElementTree as ET

# Step 1: Fetch recent papers from arXiv API
def fetch_recent_arxiv_papers(days=2, max_results=100):
    # Categories: cs.AI, cs.NE, cs.LG, q-bio.NC
    categories = ['cs.AI', 'cs.NE', 'cs.LG', 'q-bio.NC']
    cat_query = '+OR+'.join([f'cat:{cat}' for cat in categories])
    # We'll use the arXiv API without date range, then filter by date
    url = f'http://export.arxiv.org/api/query?search_query={cat_query}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending'
    try:
        req = request.Request(url)
        with request.urlopen(req) as response:
            xml_data = response.read()
    except Exception as e:
        print(f"Error fetching from arXiv API: {e}")
        return []
    
    # Parse XML
    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []
    
    # Namespace
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    papers = []
    cutoff_date = datetime.now() - timedelta(days=days)
    for entry in root.findall('atom:entry', ns):
        id_elem = entry.find('atom:id', ns)
        if id_elem is None:
            continue
        arxiv_id = id_elem.text.split('/abs/')[-1].split('v')[0]  # Remove version
        title_elem = entry.find('atom:title', ns)
        title = title_elem.text.strip() if title_elem is not None else ''
        # Get abstract for classification
        summary_elem = entry.find('atom:summary', ns)
        abstract = summary_elem.text.strip() if summary_elem is not None else ''
        # Get published date
        published_elem = entry.find('atom:published', ns)
        if published_elem is None:
            continue
        published_str = published_elem.text
        try:
            # Published format: 2021-01-01T00:00:00Z
            published = datetime.strptime(published_str, '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            # Try without Z
            try:
                published = datetime.strptime(published_str, '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                print(f"Could not parse date: {published_str}")
                continue
        # Filter by date
        if published < cutoff_date:
            # Since results are sorted by submittedDate descending, we can break early
            break
        papers.append({
            'id': arxiv_id,
            'title': title,
            'abstract': abstract,
            'published': published_str  # Keep original string for consistency
        })
    return papers

# Step 2: Query knowledge graph for utility
def get_utility_from_kg(arxiv_ids):
    # Path to knowledge graph
    kg_path = '/Users/hiyenwong/projects/ai_projects/ai_collection/knowledge/kg.db'
    if not os.path.exists(kg_path):
        print(f"Knowledge graph not found at {kg_path}")
        return {}
    
    try:
        conn = sqlite3.connect(kg_path)
        cursor = conn.cursor()
        # Placeholders for IN query
        placeholders = ','.join(['?'] * len(arxiv_ids))
        query = f"SELECT arxiv_id, utility FROM papers WHERE arxiv_id IN ({placeholders})"
        cursor.execute(query, arxiv_ids)
        rows = cursor.fetchall()
        conn.close()
        utility_dict = {row[0]: row[1] for row in rows}
        return utility_dict
    except Exception as e:
        print(f"Error querying knowledge graph: {e}")
        return {}

# Step 3: Classify paper using rules from classify_skills.py
def classify_paper(title, abstract):
    # We'll load the classification rules from classify_skills.py
    # Since we cannot import the script directly in this context, we'll define the rules here
    # based on the user's description
    rules = {
        'neuroscience': ['brain', 'neural', 'neuro', 'eeg', 'fmri', 'bci', 'cortex', 'synapt', 'cognitive'],
        'quantum': ['quantum', 'qubit', 'qec', 'qaoa', 'vqe', 'qml', 'qnn', 'entanglement', 'pauli'],
        'spiking-neuromorphic': ['spiking', 'snn', 'neuromorphic', 'stdp', 'spike', 'lif'],
        'multi-agent-rl': ['multi-agent', 'reinforcement', 'agent', 'agentic', 'ppo', 'grpo'],
        'nlp-llm': ['llm', 'transformer', 'gpt', 'bert', 'nlp', 'prompt', 'rag'],
        'signal-control-systems': ['control', 'mpc', 'kalman', 'feedback', 'cps'],
        'general-ml': ['deep-learning', 'gradient', 'moe', 'distillation', 'pruning'],
        'physics-math': ['physics', 'pde', 'topology', 'chaos', 'stochastic', 'tensor'],
        'vision-generative': ['vision', 'image', 'video', 'gan', 'diffusion'],
        'ai-safety-eval': ['ai-safety', 'alignment', 'benchmark', 'eval'],
        'security-privacy': ['security', 'privacy', 'encryption', 'cryptography'],
        'healthcare-bio': ['healthcare', 'biomedical', 'clinical', 'drug'],
        'finance': ['finance', 'portfolio', 'stock', 'trading', 'market'],
        'tools-frameworks': ['claude-code', 'opencode', 'copilot', 'cli']
    }
    text = (title + ' ' + abstract).lower()
    for category, keywords in rules.items():
        for keyword in keywords:
            if keyword in text:
                return category
    return 'other'

# Step 4: Create skill directory and SKILL.md
def create_skill_file(paper, category, base_path='/Users/hiyenwong/projects/ai_projects/ai_collection'):
    # Sanitize skill name: use arXiv ID or a cleaned title
    skill_name = paper['id'].replace('.', '_')  # e.g., 2101_00001
    # Alternatively, we can use a slug from the title, but ID is safer
    skill_dir = os.path.join(base_path, 'collection', 'skills', category, skill_name)
    os.makedirs(skill_dir, exist_ok=True)
    skill_path = os.path.join(skill_dir, 'SKILL.md')
    
    # Frontmatter
    frontmatter = {
        'name': skill_name,
        'description': f"Skill generated from arXiv paper {paper['id']}: {paper['title']}",
        'category': category,
        'created_at': datetime.now().isoformat(),
        'source': 'arXiv',
        'arxiv_id': paper['id']
    }
    # Convert frontmatter to YAML-like format (simplified)
    frontmatter_str = '---\n'
    for key, value in frontmatter.items():
        frontmatter_str += f'{key}: {value}\n'
    frontmatter_str += '---\n\n'
    
    # Content: we'll include the paper info and a note to process further
    content = f"""# {skill_name}

**Source:** arXiv paper {paper['id']}
**Title:** {paper['title']}
**Abstract:** {paper['abstract']}
**Published:** {paper['published']}

## Notes
This skill was automatically generated from an arXiv paper with utility >= 0.85.
Please review and update the skill content based on the paper's details.

## References
- arXiv: https://arxiv.org/abs/{paper['id']}
"""
    # Write the file
    with open(skill_path, 'w') as f:
        f.write(frontmatter_str + content)
    return skill_path

# Step 5: Update INDEX.md and knowledge/arxiv/index.json
def update_index_files(new_skills, base_path='/Users/hiyenwong/projects/ai_projects/ai_collection'):
    # Update INDEX.md: add new entries at the top
    index_md_path = os.path.join(base_path, 'collection', 'skills', 'INDEX.md')
    new_entries = []
    for skill_path in new_skills:
        # Extract skill name and category from path
        rel_path = os.path.relpath(skill_path, os.path.join(base_path, 'collection', 'skills'))
        # rel_path is like: <category>/<skill_name>/SKILL.md
        parts = rel_path.split(os.sep)
        if len(parts) >= 2:
            category = parts[0]
            skill_name = parts[1]
            new_entries.append(f"- [{skill_name}]({category}/{skill_name}/SKILL.md) - arXiv paper")
    
    if new_entries:
        try:
            with open(index_md_path, 'r') as f:
                existing_content = f.read()
        except FileNotFoundError:
            existing_content = '# Skills Index\n\n'
        # Insert new entries after the header
        lines = existing_content.split('\n')
        # Find the first non-empty line after the header
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.strip() and not line.startswith('#'):
                insert_idx = i
                break
        else:
            insert_idx = len(lines)
        # Insert new entries
        for entry in reversed(new_entries):
            lines.insert(insert_idx, entry)
        new_content = '\n'.join(lines)
        with open(index_md_path, 'w') as f:
            f.write(new_content)
    
    # Update knowledge/arxiv/index.json
    index_json_path = os.path.join(base_path, 'knowledge', 'arxiv', 'index.json')
    try:
        with open(index_json_path, 'r') as f:
            index_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        index_data = {"papers": [], "last_updated": ""}
    
    # Add new papers
    for skill_path in new_skills:
        rel_path = os.path.relpath(skill_path, base_path)
        # Extract arXiv ID from the skill path (we used the ID in the skill name)
        skill_name = os.path.basename(os.path.dirname(skill_path))
        arxiv_id = skill_name.replace('_', '.')  # Reverse of sanitization
        # Avoid duplicates
        if any(p.get('arxiv_id') == arxiv_id for p in index_data.get('papers', [])):
            continue
        index_data['papers'].append({
            'arxiv_id': arxiv_id,
            'skill_path': rel_path,
            'added_at': datetime.now().isoformat()
        })
    
    index_data['last_updated'] = datetime.now().isoformat()
    with open(index_json_path, 'w') as f:
        json.dump(index_data, f, indent=2)

# Step 6: Run classification check and neural map update
def run_maintenance_scripts(base_path='/Users/hiyenwong/projects/ai_projects/ai_collection'):
    # Run classify_skills.py
    script1 = os.path.join(base_path, 'scripts', 'classify_skills.py')
    if os.path.exists(script1):
        os.system(f"cd {base_path} && python {script1}")
    # Run update_neural_map.py
    script2 = os.path.join(base_path, 'scripts', 'update_neural_map.py')
    if os.path.exists(script2):
        os.system(f"cd {base_path} && python {script2}")

# Step 7: Git commit and push
def git_commit_push(base_path='/Users/hiyenwong/projects/ai_projects/ai_collection'):
    commit_message = f"feat: add paper skills from arXiv {datetime.now().strftime('%Y-%m-%d')}"
    cmd = f"cd {base_path} && git add -A && git commit -m \"{commit_message}\" && git push origin main"
    os.system(cmd)

# Main execution
if __name__ == '__main':
    base_path = '/Users/hiyenwong/projects/ai_projects/ai_collection'
    print("Fetching recent arXiv papers...")
    papers = fetch_recent_arxiv_papers(days=2, max_results=50)
    if not papers:
        print("No papers found.")
        exit(0)
    
    arxiv_ids = [p['id'] for p in papers]
    print(f"Found {len(papers)} papers. Checking knowledge graph for utility...")
    utility_dict = get_utility_from_kg(arxiv_ids)
    
    high_utility_papers = []
    for paper in papers:
        uid = paper['id']
        utility = utility_dict.get(uid, 0)
        if utility >= 0.85:
            high_utility_papers.append(paper)
    
    print(f"Found {len(high_utility_papers)} papers with utility >= 0.85.")
    
    if not high_utility_papers:
        print("No high utility papers to process.")
        exit(0)
    
    # Create skill files
    created_skills = []
    for paper in high_utility_papers:
        category = classify_paper(paper['title'], paper['abstract'])
        print(f"Processing paper {paper['id']} -> category: {category}")
        skill_path = create_skill_file(paper, category, base_path)
        created_skills.append(skill_path)
    
    # Update index files
    print("Updating index files...")
    update_index_files(created_skills, base_path)
    
    # Run maintenance scripts
    print("Running maintenance scripts...")
    run_maintenance_scripts(base_path)
    
    # Git commit and push
    print("Committing and pushing changes...")
    git_commit_push(base_path)
    
    print(f"Successfully processed {len(high_utility_papers)} papers.")