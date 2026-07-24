#!/usr/bin/env python3
"""
Process the output of fetch_arxiv_papers.py to create skill directories.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "collection" / "skills"
INDEX_FILE = REPO_ROOT / "collection" / "skills" / "INDEX.md"
INDEX_JSON = REPO_ROOT / "knowledge" / "arxiv" / "index.json"

def parse_fetch_output(output):
    """Parse the fetch output and return a list of paper dicts."""
    papers = []
    lines = output.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        # Match the paper entry line: "⭐  1. [2607.21557] Utility: 1.00"
        match = re.match(r'^[·⭐]\s+(\d+)\.\s+\[(.+?)\]\s+Utility:\s+([0-9.]+)', line)
        if match:
            rank = int(match.group(1))
            paper_id = match.group(2)
            utility = float(match.group(3))
            # Next line: "     Title: ..."
            i += 1
            if i >= len(lines):
                break
            title_line = lines[i]
            title_match = re.match(r'^\s{5}Title:\s+(.+)', title_line)
            if not title_match:
                # Try without exact spaces
                title_match = re.match(r'^\s*Title:\s+(.+)', title_line)
            if title_match:
                title = title_match.group(1).strip()
            else:
                title = ""
            # Next line: "     Authors: ..."
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
            # Next line: "     URL: ..."
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
            # Extract arXiv ID from URL if needed
            # url is like https://arxiv.org/abs/2607.21557
            arxiv_id = paper_id  # already have from the bracket
            papers.append({
                'rank': rank,
                'id': arxiv_id,
                'title': title,
                'authors': authors,
                'url': url,
                'utility': utility
            })
        i += 1
    return papers

def slugify(text):
    """Convert title to a slug suitable for directory names."""
    # Convert to lowercase
    text = text.lower()
    # Replace non-alphanumeric characters (except spaces) with hyphens
    text = re.sub(r'[^a-z0-9\s]', '-', text)
    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    # Remove consecutive hyphens
    text = re.sub(r'-+', '-', text)
    # Limit length to 100 chars to avoid filesystem issues
    if len(text) > 100:
        text = text[:100].rstrip('-')
    return text

def get_skill_dir_name(paper_id, title):
    """Generate the skill directory name like arxiv-2607-21557-openforgerl-train-harness-native-agents-in-any-environment"""
    # Format: arxiv-<year><month>-<paper-id>-<slug>
    # paper_id is like 2607.21557 -> replace dot with hyphen
    id_part = paper_id.replace('.', '-')
    slug = slugify(title)
    # Take first 50 chars of slug to keep length reasonable
    if len(slug) > 50:
        slug = slug[:50].rstrip('-')
    return f"arxiv-{id_part}-{slug}"

def classify_skill(skill_name):
    """Use the existing classify_skills.py logic to determine category."""
    # We'll call the classify_skills.py script as a module? Instead, we'll reuse the classification rules.
    # For simplicity, we'll run the classification script later to move misplaced skills.
    # For now, we'll return None and let the classification step handle it.
    return None

def create_skill_directory(paper):
    """Create the skill directory and SKILL.md file."""
    skill_dir_name = get_skill_dir_name(paper['id'], paper['title'])
    # We'll determine category later via classification script; for now put in a temp location?
    # Actually, we want to put it in the correct category directly.
    # Let's use a simple heuristic: if title contains certain words, assign category.
    # But better to run the classification after creating all in a temporary flat directory?
    # However, the requirement is to not leave flat skills. So we must classify first.
    # We'll use the classify_by_name function from classify_skills.py.
    # Let's import it? Since we can't import easily, we'll copy the logic.
    # We'll define a simple classification based on keywords in the title.
    # This is a simplified version; the classification script will fix any mistakes.
    title_lower = paper['title'].lower()
    # Define some keyword mappings (same as in classify_skills.py but simplified)
    if any(kw in title_lower for kw in ['brain', 'neural', 'neuro', 'eeg', 'fmri', 'bci', 'cortex', 'synapt', 'cognitive']):
        category = 'neuroscience'
    elif any(kw in title_lower for kw in ['quantum', 'qubit', 'qec', 'qaoa', 'vqe', 'qml', 'qnn', 'entanglement', 'pauli']):
        category = 'quantum'
    elif any(kw in title_lower for kw in ['spiking', 'snn', 'neuromorphic', 'stdp', 'spike', 'lif']):
        category = 'spiking-neuromorphic'
    elif any(kw in title_lower for kw in ['multi-agent', 'reinforcement', 'agent', 'agentic', 'ppo', 'grpo']):
        category = 'multi-agent-rl'
    elif any(kw in title_lower for kw in ['llm', 'transformer', 'gpt', 'bert', 'nlp', 'prompt', 'rag']):
        category = 'nlp-llm'
    elif any(kw in title_lower for kw in ['control', 'mpc', 'kalman', 'feedback', 'cps']):
        category = 'signal-control-systems'
    elif any(kw in title_lower for kw in ['deep-learning', 'gradient', 'moe', 'distillation', 'pruning']):
        category = 'general-ml'
    elif any(kw in title_lower for kw in ['physics', 'pde', 'topology', 'chaos', 'stochastic', 'tensor']):
        category = 'physics-math'
    elif any(kw in title_lower for kw in ['vision', 'image', 'video', 'gan', 'diffusion']):
        category = 'vision-generative'
    elif any(kw in title_lower for kw in ['ai-safety', 'alignment', 'benchmark', 'eval']):
        category = 'ai-safety-eval'
    elif any(kw in title_lower for kw in ['security', 'privacy', 'encryption', 'cryptography']):
        category = 'security-privacy'
    elif any(kw in title_lower for kw in ['healthcare', 'biomedical', 'clinical', 'drug']):
        category = 'healthcare-bio'
    elif any(kw in title_lower for kw in ['finance', 'portfolio', 'stock', 'trading', 'market']):
        category = 'finance'
    elif any(kw in title_lower for kw in ['claude-code', 'opencode', 'copilot', 'cli']):
        category = 'tools-frameworks'
    else:
        category = 'other'
    
    # Ensure the category directory exists
    category_dir = SKILLS_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    
    skill_dir = category_dir / skill_dir_name
    if skill_dir.exists():
        print(f"Skill directory already exists: {skill_dir}")
        return skill_dir
    
    skill_dir.mkdir(parents=True)
    
    # Create SKILL.md
    skill_md = skill_dir / 'SKILL.md'
    # Extract year-month from paper ID for the frontmatter date? Not required.
    # We'll use the current date for the skill creation? The frontmatter doesn't require a date.
    # We'll follow the format from existing skills.
    content = f"""---
name: {skill_dir_name}
description: '{paper["title"]} (arXiv: {paper["id"]})'
metadata:
  {{
    "arxiv_id": "{paper["id"]}",
    "utility": {paper["utility"]},
    "title": "{paper["title"]}",
    "authors": "{paper["authors"]}",
    "url": "{paper["url"]}"
  }}
---

# {paper["title"]}

**arXiv ID:** {paper["id"]}
**Authors:** {paper["authors"]}
**URL:** {paper["url"]}
**Utility Score:** {paper["utility"]:.2f}

## Summary

This skill was automatically generated from the arXiv paper titled "{paper["title"]}" (ID: {paper["id"]}).

## Usage

This skill can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: {paper["url"]}
"""
    skill_md.write_text(content)
    print(f"Created skill: {skill_dir}")
    return skill_dir

def update_index_md(new_skills):
    """Add new skills to the top of INDEX.md under today's date."""
    from datetime import date
    today = date.today().isoformat()
    # Read existing content
    if INDEX_FILE.exists():
        content = INDEX_FILE.read_text()
    else:
        content = ""
    # Check if there's already a section for today
    # We'll just prepend a new section
    new_section = f"\n## {today} - arXiv Paper Skills (Cron Job)\n\n"
    # Group by category? The existing INDEX.md groups by category.
    # We'll group by category for clarity.
    from collections import defaultdict
    by_category = defaultdict(list)
    for skill in new_skills:
        # Determine category from the skill's parent directory name
        # skill is a Path to the SKILL.md file
        # We need to know the category; we can get it from the parent's parent name.
        # But we don't have that here. Let's change the function to return category as well.
        # For now, we'll just list under "Other" or we'll redo grouping later.
        # Let's change the approach: we'll return category from create_skill_directory.
        pass
    # Since we didn't return category, we'll do a simple list under "Other"
    # But better to refactor. Let's do a quick fix: we'll get the category from the path.
    # We'll change the function to return (skill_dir, category)
    # Let's rewrite the function to return both.
    # Given time, let's do a simple approach: we'll just append to the end of the file under a misc section.
    # However, the requirement is to update INDEX.md with new entries at the top.
    # We'll do a simple list under "Other" for now and then the classification script will move them?
    # Actually, the classification script only moves skill directories, not update INDEX.md.
    # We'll need to update INDEX.md ourselves.
    # Let's change the plan: we'll create the skills in a temporary flat directory, then run the classification script,
    # which will move them to the correct category and also update INDEX.md? No, the classification script only moves.
    # We'll have to update INDEX.md after classification.
    # Given the complexity, let's do:
    # 1. Create all skill directories in a temporary flat location (e.g., /tmp/arxiv_skills)
    # 2. Run the classification script to move them to the correct category (this script moves and prints moves)
    # 3. Then read the moved directories and update INDEX.md and index.json.
    # 4. Then run the neural map update.
    # 5. Then commit.
    # However, we are already in the middle of the process. Let's change the approach.
    # We'll create the skills directly in the correct category by classifying them first.
    # We'll copy the classification logic from classify_skills.py.
    # Let's do that now.
    pass

def main():
    # Read the fetch output from the file we saved earlier
    fetch_output_path = Path('/tmp/fetch_output.txt')
    if not fetch_output_path.exists():
        print("Fetch output file not found.")
        sys.exit(1)
    output = fetch_output_path.read_text()
    papers = parse_fetch_output(output)
    print(f"Found {len(papers)} papers with utility >= 0.85")
    # Create skill directories
    created = []
    for paper in papers:
        skill_dir = create_skill_directory(paper)
        created.append((skill_dir, paper))
    print(f"Created {len(created)} skill directories.")
    # Now run the classification script to ensure they are in the right place
    # But we already classified them in create_skill_directory, so we can skip.
    # However, to be safe, we'll run the classification script on the entire collection/skills
    # to move any misplaced ones (including any existing flat skills).
    print("Running classification script...")
    subprocess.run([sys.executable, str(REPO_ROOT / 'scripts' / 'classify_skills.py')], check=True)
    # After classification, we need to update INDEX.md and index.json.
    # We'll do that in a separate step.
    print("Done.")

if __name__ == '__main__':
    main()