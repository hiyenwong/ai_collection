import os, re, json, subprocess, sys
from pathlib import Path
from datetime import date

REPO_ROOT = Path.cwd()
SKILLS_DIR = REPO_ROOT / 'collection' / 'skills'
FETCH_OUTPUT = Path('/tmp/fetch_output.txt')
INDEX_FILE = REPO_ROOT / 'collection' / 'skills' / 'INDEX.md'
INDEX_JSON = REPO_ROOT / 'knowledge' / 'arxiv' / 'index.json'

# Parse fetch output to get set of paper ids with utility >= 0.85
def get_high_utility_ids():
    if not FETCH_OUTPUT.exists():
        return set()
    ids = set()
    with open(FETCH_OUTPUT, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Match lines like: "⭐  1. [2608.05144] Utility: 1.00"
            m = re.match(r'^[·⭐]\\s+\\d+\\.\\s+\\[(.+?)\\]\\s+Utility:\\s+[0-9.]+', line)
            if m:
                ids.add(m.group(1))
    return ids

high_ids = get_high_utility_ids()
print(f"High utility paper IDs from fetch: {len(high_ids)}")

# Classification function (title-based) - same as in classify_skills.py but simplified
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

# Step 1: Move flat arxiv-2608-* directories to appropriate categories
flat_dirs = [d for d in SKILLS_DIR.iterdir() if d.is_dir() and d.name.startswith('arxiv-2608-')]
print(f"Found {len(flat_dirs)} flat arxiv-2608-* directories")

moved = 0
for d in flat_dirs:
    # Extract paper id from directory name: arxiv-2608-05144-... -> 2608.05144
    # Remove prefix 'arxiv-'
    rest = d.name[6:]  # after 'arxiv-'
    # Split by '-' and take first two parts as the paper id (with a dot)
    parts = rest.split('-')
    if len(parts) >= 2:
        paper_id = f"{parts[0]}.{parts[1]}"
    else:
        # Try to read from SKILL.md
        skill_md = d / 'SKILL.md'
        if skill_md.exists():
            content = skill_md.read_text()
            # extract arxiv ID from metadata or from the line
            m = re.search(r'arXiv ID:\\s*([0-9]+\\.[0-9]+)', content)
            if m:
                paper_id = m.group(1)
            else:
                m = re.search(r'arXiv:([0-9]+\\.[0-9]+)', content)
                if m:
                    paper_id = m.group(1)
                else:
                    print(f"Could not extract paper id from {d.name}")
                    continue
        else:
            print(f"No SKILL.md in {d.name}")
            continue
    if paper_id not in high_ids:
        # Not a high utility paper from today's fetch, skip (maybe old)
        continue
    title = ""  # We don't have title here, we'll get it from the SKILL.md or fetch output? We'll get from SKILL.md.
    skill_md = d / 'SKILL.md'
    if skill_md.exists():
        content = skill_md.read_text()
        # Extract title from the first line after the header? Or from the metadata? Let's get from the first line after the header.
        # The format: 
        # ---\nname: ...\ndescription: 'Title (arXiv: ID)'\n...
        # Then a blank line, then "# Title"
        lines = content.split('\\n')
        for line in lines:
            if line.startswith('# '):
                title = line[2:].strip()
                break
        if not title:
            # Fallback: extract from description line
            for line in lines:
                if line.startswith('description:'):
                    # description: 'Title (arXiv: ID)'
                    match = re.search(r"description: '(.+?) \\(arXiv:", line)
                    if match:
                        title = match.group(1)
                    break
    if not title:
        title = d.name  # fallback
    category = classify_title(title)
    target_dir = SKILLS_DIR / category / d.name
    if target_dir.exists():
        print(f"SKIP exists: {d.name} -> {category}/{d.name}")
        continue
    # Use git mv
    rel_src = f"collection/skills/{d.name}"
    rel_dst = f"collection/skills/{category}/{d.name}"
    res = subprocess.run(['git', 'mv', rel_src, rel_dst], cwd=str(REPO_ROOT), capture_output=True, text=True)
    if res.returncode == 0:
        print(f"MOVED: {d.name} -> {category}/{d.name}")
        moved += 1
    else:
        print(f"ERROR moving {d.name}: {res.stderr.strip()}")
print(f"Total moved: {moved}")

# Step 2: Update index.json and INDEX.md for any new high utility papers that are not already in index.json
# Load existing index.json (it's a list)
if INDEX_JSON.exists():
    with open(INDEX_JSON, 'r') as f:
        index_data = json.load(f)
else:
    index_data = []

# Build a set of existing arxiv ids in index_data for quick lookup
existing_ids = {entry.get('id') for entry in index_data}

new_entries = []
for paper_id in high_ids:
    if paper_id in existing_ids:
        continue
    # We need to get the title, authors, url, utility from the fetch output? We didn't store all that in the set.
    # Let's re-parse the fetch output to get the full info for this paper_id.
    # We'll do a quick parse again but store in a dict.
    pass  # We'll do below

# Let's re-parse the fetch output to get a dict of paper_id -> info
papers_info = {}
if FETCH_OUTPUT.exists():
    with open(FETCH_OUTPUT, 'r') as f:
        lines = f.readlines()
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
                papers_info[paper_id] = {'title': title, 'authors': authors, 'url': url, 'utility': utility}
            i += 1

for paper_id, info in papers_info.items():
    if paper_id in existing_ids:
        continue
    # Determine category
    category = classify_title(info['title'])
    skill_dir_name = get_skill_dir_name(paper_id, info['title'])
    # Check if the skill directory exists now (after moving)
    skill_dir = SKILLS_DIR / category / skill_dir_name
    if not skill_dir.exists():
        # Maybe not moved yet? We'll skip for now, but we should have moved all.
        # Let's try to create it? But we already created the flat ones and moved them.
        # If it's missing, we can skip.
        print(f"Warning: skill directory not found for {paper_id} in {category}")
        continue
    entry = {
        "id": paper_id,
        "title": info['title'],
        "skill_name": skill_dir_name,
        "category": category,
        "utility": info['utility'],
        "date_added": date.today().isoformat()
    }
    new_entries.append(entry)

if new_entries:
    index_data.extend(new_entries)
    with open(INDEX_JSON, 'w') as f:
        json.dump(index_data, f, indent=2)
    print(f"Added {len(new_entries)} entries to {INDEX_JSON}")
else:
    print("No new entries to add to index.json")

# Step 3: Update INDEX.md: add a section at the top for today's date
if INDEX_FILE.exists():
    with open(INDEX_FILE, 'r') as f:
        index_md_content = f.read()
else:
    index_md_content = ""

today = date.today().isoformat()
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

# Step 4: Update neural map
print("Updating neural map...")
subprocess.run([sys.executable, str(REPO_ROOT / 'scripts' / 'update_neural_map.py')], check=True)
print("Neural map updated.")

# Step 5: Commit and push
print("Committing changes...")
subprocess.run(['git', 'add', '-A'], cwd=str(REPO_ROOT), check=True)
subprocess.run(['git', 'commit', '-m', f"feat: add paper skills from arXiv {today}"], cwd=str(REPO_ROOT), check=True)
subprocess.run(['git', 'push', 'origin', 'main'], cwd=str(REPO_ROOT), check=True)
print("Changes pushed to main.")
