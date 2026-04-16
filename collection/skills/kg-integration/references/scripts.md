# Knowledge Graph Migration Scripts

This directory contains scripts for migrating and querying the sqlite-knowledge-graph database.

## Scripts

### migrate_openclaw_to_kg.py
Migrates OpenClaw skills and agents to kg.db.

```bash
python3 ~/.hermes/scripts/migrate_openclaw_to_kg.py
```

**What it does:**
- Parses 452 skills from `~/.openclaw/openclaw/workspace/skills/`
- Parses 25 agents from `~/.openclaw/openclaw/agents/`
- Inserts them into kg.db as entities
- Creates placeholder vectors for each entity
- Creates agent-skill relationships

### kg_tool.py
Python API for querying kg.db.

```python
from kg_tool import (
    kg_search_papers,
    kg_get_agent,
    kg_get_skill,
    kg_find_agent_for_task,
    kg_recommend_skills,
    kg_high_utility_papers,
    kg_stats
)

# Search papers
papers = kg_search_papers("neural network", 10)

# Find agent for task
agents = kg_find_agent_for_task("machine learning model training")

# Recommend skills
skills = kg_recommend_skills("graph neural network", 0.9)

# Get agent details
agent = kg_get_agent("ml-engineer")

# Get skill details
skill = kg_get_skill("turboquant-vector-quantization")

# Get high utility papers
papers = kg_high_utility_papers(threshold=0.9, limit=10)

# Get stats
stats = kg_stats()
```

### kg_query.py
CLI tool for kg.db queries.

```bash
# Get stats
python3 ~/.hermes/scripts/kg_query.py stats

# Search papers
python3 ~/.hermes/scripts/kg_query.py search "multi-agent" 5

# Get high utility papers
python3 ~/.hermes/scripts/kg_query.py high-utility 0.9

# Get paper neighbors
python3 ~/.hermes/scripts/kg_query.py neighbors 123 2

# Get skills from paper
python3 ~/.hermes/scripts/kg_query.py skills 123
```

### kg_tool_handler.py
Tool handler for Hermes integration.

## Database Location

```
~/.openclaw/openclaw/workspace-fullstack-engineer/sqlite-knowledge-graph/kg.db
```

## Data Statistics

After migration:
- **2,497 papers** - arXiv papers with utility scores
- **452 skills** - Migrated from OpenClaw
- **25 agents** - Migrated from OpenClaw
- **743,466 relations** - Including new has_skill relationships
- **2,974 vectors** - Placeholder vectors for all entities

## Entity Types

| Type | Count | Source |
|------|-------|--------|
| paper | 2,497 | Original kg.db |
| skill | 452 | OpenClaw workspace/skills |
| agent | 25 | OpenClaw agents |

## Relation Types

| Type | Count | Description |
|------|-------|-------------|
| derived_from | 115 | Paper → Skill |
| has_skill | 7 | Agent → Skill |
| related_by_keywords | 740,418 | Keyword similarity |
| similar_to | 2,926 | Skill similarity |
