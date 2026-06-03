---
name: automated-research-pipeline
description: "Lightweight automated research pipeline for searching, filtering, and extracting skills from academic papers without knowledge graph infrastructure. Use for: quick research synthesis, paper-to-skill conversion, domain literature surveys. Activation: automated research, paper to skill, research pipeline, quick literature review, skill extraction from papers."
---

# Automated Research Pipeline

## Description
Lightweight automated research pipeline for searching, filtering, and extracting reusable skills from academic papers. Provides a middle ground between basic search and full knowledge graph workflows - no KG infrastructure required.

## Activation Keywords
- automated research
- paper to skill
- research pipeline
- quick literature review
- skill extraction from papers
- research synthesis
- domain survey
- arxiv to skill
- paper analysis pipeline
- automated skill creation

## Tools Used
- **exec**: Python scripts for arXiv API queries
- **write**: Create skill files from paper analysis
- **read**: Load paper data and templates

## Workflow Overview

```
Search → Filter → Score → Select → Extract → Create Skill → Sync
```

## Step-by-Step Process

### Step 1: Multi-Keyword Search

Search arXiv with multiple related keywords to maximize coverage:

```python
keywords = [
    "systems engineering",
    "system design", 
    "distributed systems",
    "control systems",
    "complex systems"
]

all_papers = []
for kw in keywords:
    papers = await search_arxiv(kw, max_results=15, days=30)
    all_papers.extend(papers)
```

### Step 2: Deduplication

Remove duplicates by arXiv ID:

```python
seen_ids = set()
unique_papers = []
for p in all_papers:
    if p["id"] not in seen_ids:
        seen_ids.add(p["id"])
        unique_papers.append(p)
```

### Step 3: Relevance Scoring

Score papers based on domain-specific criteria:

```python
def score_paper(paper, domain_keywords, category_bonuses):
    """
    Score paper relevance.
    
    Args:
        paper: Paper dict with title, abstract, categories
        domain_keywords: Dict of {keyword: weight}
        category_bonuses: Dict of {category: bonus}
    
    Returns:
        relevance_score: Integer score
    """
    score = 0
    title_lower = paper['title'].lower()
    abstract_lower = paper['abstract'].lower()
    categories = [c.lower() for c in paper.get('categories', [])]
    
    # Keyword scoring
    for kw, weight in domain_keywords.items():
        if kw in title_lower:
            score += weight * 2  # Title match = higher weight
        elif kw in abstract_lower:
            score += weight
    
    # Category bonuses
    for cat, bonus in category_bonuses.items():
        if any(cat in c for c in categories):
            score += bonus
    
    return score
```

### Step 4: Selection

Sort by score and select top N:

```python
# Add scores
for p in papers:
    p['relevance_score'] = score_paper(p, domain_keywords, category_bonuses)

# Sort and select
papers.sort(key=lambda x: x['relevance_score'], reverse=True)
top_papers = papers[:3]  # Select top 3
```

### Step 5: Skill Extraction

Extract skill patterns from selected papers:

```python
def extract_skill_pattern(paper):
    """
    Extract skill components from paper.
    
    Returns dict with:
    - name: Skill name (derived from title)
    - description: Core contribution
    - activation_keywords: Domain terms
    - core_concepts: Key ideas
    - implementation_patterns: Code patterns
    """
    return {
        "name": derive_skill_name(paper['title']),
        "description": extract_contribution(paper['abstract']),
        "activation_keywords": extract_keywords(paper),
        "core_concepts": extract_concepts(paper),
        "arxiv_id": paper['id'],
        "authors": paper['authors'],
        "category": paper['category']
    }
```

### Step 6: Skill Creation

Generate SKILL.md from template:

```markdown
---
name: {skill_name}
description: "{description}. Activation: {keywords}."
---

# {Skill Title}

## Description
{Paper abstract summary}

## Activation Keywords
- {keyword1}
- {keyword2}
...

## Core Concepts
{Key theoretical contributions}

## Implementation Patterns
```python
# Pattern 1: Basic usage
...
```

## References
- **Paper**: {paper_title}
- **Authors**: {authors}
- **arXiv**: {arxiv_id}
```

### Step 7: Sync to Repository

```bash
# Add to ai_collection
git add collection/skills/{skill_name}/
git commit -m "feat(skills): add {skill_name} from arXiv {arxiv_id}"
git push origin main
```

## Configuration Templates

### Template 1: Control Systems Research

```python
config = {
    "keywords": [
        "control systems",
        "MPC", 
        "optimal control",
        "robust control",
        "nonlinear control"
    ],
    "domain_keywords": {
        "control": 2,
        "mpc": 3,
        "stability": 2,
        "optimal": 1
    },
    "category_bonuses": {
        "math.oc": 2,
        "eess.sy": 2,
        "cs.ma": 1
    },
    "max_results_per_keyword": 15,
    "days_back": 30,
    "top_n_selection": 3
}
```

### Template 2: Machine Learning Research

```python
config = {
    "keywords": [
        "machine learning",
        "deep learning",
        "neural networks",
        "reinforcement learning"
    ],
    "domain_keywords": {
        "neural": 2,
        "learning": 1,
        "network": 1
    },
    "category_bonuses": {
        "cs.lg": 2,
        "cs.ai": 2,
        "stat.ml": 2
    }
}
```

## Examples

### Example 1: Systems Engineering Survey

```python
# Define domain
config = {
    "keywords": ["systems engineering", "distributed systems", "control systems"],
    "domain_keywords": {
        "control": 2, "mpc": 3, "multi-agent": 2,
        "distributed": 2, "consensus": 2
    },
    "category_bonuses": {"math.oc": 2, "eess.sy": 2}
}

# Execute pipeline
papers = await search_all_keywords(config['keywords'])
papers = deduplicate(papers)
papers = score_and_filter(papers, config)
top_papers = select_top(papers, n=3)

# Create skills
for paper in top_papers:
    skill = extract_skill_pattern(paper)
    create_skill_file(skill)
```

### Example 2: Quick Domain Scan

```python
# Quick scan for recent developments
keywords = ["quantum computing", "quantum ML"]
papers = await search_arxiv(keywords, days=7)
papers = score_by_relevance(papers, quantum_keywords)
summary = generate_summary(papers[:5])
```

## Output Formats

### Paper Summary Format

```markdown
## Paper {n}: {title}
- **Score**: {relevance_score}
- **Authors**: {authors}
- **arXiv**: {id}
- **Abstract**: {abstract[:300]}...
```

### Research Report Format

```markdown
# Research Summary: {Domain}

## Search Parameters
- Keywords: {list}
- Time range: {days} days
- Papers found: {count}

## Top Papers
{paper summaries}

## Skills Created
{skill list}

## Trends Observed
{trend analysis}
```

## Best Practices

1. **Keyword Diversity**: Use 4-6 related keywords for comprehensive coverage
2. **Scoring Calibration**: Adjust weights based on domain specificity
3. **Quality Threshold**: Set minimum relevance score (e.g., >= 3)
4. **Deduplication**: Always dedupe by arXiv ID before scoring
5. **Skill Naming**: Use lowercase-hyphen format
6. **Citation**: Always include arXiv ID and authors in skills

## Limitations

- Requires arXiv API access (rate limited)
- Scoring is heuristic-based, not semantic
- No full-text analysis (abstracts only)
- Manual review recommended for skill quality

## Related Skills
- `arxiv-search`: Basic arXiv search
- `kg-research-workflow`: Full knowledge graph pipeline
- `research-paper-pattern-extractor`: Pattern extraction from KG
- `skill-creator`: Skill creation guidelines

## References

Based on successful execution for systems engineering research:
- 47 papers searched, 3 skills created
- Papers from math.OC, eess.SY categories
- Skills: discounted-mpc-robust-control, density-driven-multi-agent-control, nonlinear-mas-optimal-control


## Instructions for Agents

When this skill is activated:

1. Identify the user's specific need
2. Apply the specialized knowledge
3. Provide clear guidance