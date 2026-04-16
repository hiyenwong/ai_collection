# kg-integration - Knowledge Graph Integration for Hermes

## Description

Integrate sqlite-knowledge-graph (kg.db) with Hermes. Provides tools to search papers, query agents/skills, and find the best agent for tasks using the knowledge graph with 2,497 papers, 452 skills, and 25 agents migrated from OpenClaw.

## Activation Keywords

- knowledge graph
- kg search
- find agent
- recommend skill
- search paper
- arxiv paper
- agent selection
- skill recommendation
- knowledge base query

## Core Concepts

### Knowledge Graph Structure

The kg.db contains:
- **2,497 papers** - arXiv papers with utility scores
- **452 skills** - Extracted from papers with activation keywords
- **25 agents** - Specialized agents migrated from OpenClaw
- **743,466 relations** - Connections between entities

### Entity Types

| Type | Count | Description |
|------|-------|-------------|
| paper | 2,497 | arXiv papers with metadata |
| skill | 452 | Reusable skills from papers |
| agent | 25 | Specialized task agents |

### Relation Types

| Type | Count | Description |
|------|-------|-------------|
| derived_from | 115 | Paper → Skill relationships |
| has_skill | 7 | Agent → Skill relationships |
| related_by_keywords | 740,418 | Keyword-based paper similarity |
| similar_to | 2,926 | Skill similarity |

## Tools

### kg_search_papers

Search papers in the knowledge graph by keywords.

**Parameters:**
- `query` (required): Search query keywords
- `limit` (optional): Maximum number of results (default: 10)

**Example:**
```python
kg_search_papers("multi-agent reinforcement learning", limit=5)
```

### kg_get_agent

Get detailed information about an agent.

**Parameters:**
- `agent_name` (required): Agent name (e.g., algorithm-engineer, ml-engineer)

**Available Agents:**
- algorithm-engineer - Algorithm design and optimization
- ml-engineer - Machine learning model development
- fullstack-engineer - Full-stack development
- data-engineer - Data pipeline and infrastructure
- security-engineer - Security analysis and implementation
- neuroscientist - Neuroscience research
- biologist - Biological research
- geneticist - Genetics research
- economist - Economic analysis
- stock-analyst - Stock market analysis
- mathematician - Mathematical modeling
- physicist - Physics research
- philosopher - Philosophical analysis
- linguist - Linguistic analysis
- psychologist - Psychological analysis
- tech-cofounder - Startup technical leadership
- research-agent - Research assistance
- quantitative-analyst - Quantitative analysis
- computational-scientist - Computational research
- population-dynamics-scientist - Population dynamics
- computer-network-scientist - Network research
- applied-scientist - Applied research
- statistician - Statistical analysis
- logician - Logical analysis
- prompt-engineer - Prompt engineering

**Example:**
```python
kg_get_agent("algorithm-engineer")
```

### kg_get_skill

Get detailed information about a skill.

**Parameters:**
- `skill_name` (required): Skill name

**Example:**
```python
kg_get_skill("turboquant-vector-quantization")
```

### kg_find_agent_for_task

Find the best agent for a given task.

**Parameters:**
- `task_description` (required): Description of the task

**Example:**
```python
kg_find_agent_for_task("Implement a graph neural network for brain connectivity analysis")
```

### kg_recommend_skills

Recommend skills related to a topic.

**Parameters:**
- `topic` (required): Topic or keywords
- `min_utility` (optional): Minimum utility score 0-1 (default: 0.8)

**Example:**
```python
kg_recommend_skills("neural network", min_utility=0.9)
```

### kg_high_utility_papers

Get high utility papers (utility >= 0.85).

**Parameters:**
- `threshold` (optional): Utility threshold (default: 0.85)
- `limit` (optional): Maximum number of results (default: 20)

**Example:**
```python
kg_high_utility_papers(threshold=0.9, limit=10)
```

### kg_stats

Get knowledge graph statistics.

**Example:**
```python
kg_stats()
```

## Usage Patterns

### Pattern 1: Find Agent for Task

When user asks for help with a specific task:
1. Use `kg_find_agent_for_task` to find the best agent
2. Present the top 3 agents with their purposes
3. Recommend the best match

### Pattern 2: Skill Discovery

When user wants to learn about a topic:
1. Use `kg_recommend_skills` to find relevant skills
2. Use `kg_search_papers` to find related papers
3. Present skills with high utility scores

### Pattern 3: Agent Delegation

When a task matches a specialized agent:
1. Use `kg_get_agent` to get agent details
2. Check if the agent has relevant skills
3. Suggest delegating to that agent

### Pattern 4: Research Assistance

When user is researching a topic:
1. Use `kg_search_papers` to find relevant papers
2. Use `kg_recommend_skills` to find implementation skills
3. Present papers with high utility scores first

## Examples

### Example 1: Find Agent for ML Task

User: "I need help training a neural network"

```python
agents = kg_find_agent_for_task("training a neural network")
# Returns: ml-engineer (score: 6)
```

Response: "For training neural networks, I recommend the **ml-engineer** agent. Would you like me to delegate this task?"

### Example 2: Find Skills for Brain Analysis

User: "What skills are available for brain network analysis?"

```python
skills = kg_recommend_skills("brain network", min_utility=0.9)
# Returns: hypergraph-unet-brain (utility: 0.95), dcorp-connectivity-refinement (utility: 0.95), ...
```

### Example 3: Search Papers

User: "Find papers about multi-agent systems"

```python
papers = kg_search_papers("multi-agent", limit=5)
# Returns: EvoScientist, The Devil Behind Moltbook, From Spark to Fire, ...
```

## Technical Details

### Database Location

```
~/.openclaw/openclaw/workspace-fullstack-engineer/sqlite-knowledge-graph/kg.db
```

### Data Sources

- **Papers**: arXiv cs.AI papers with utility scores
- **Skills**: Extracted from papers using skill-extractor
- **Agents**: Migrated from OpenClaw workspace

### Migration History

- **Date**: 2025-04-14
- **Papers**: 2,497 (from kg.db)
- **Skills**: 452 (from ~/.openclaw/openclaw/workspace/skills)
- **Agents**: 25 (from ~/.openclaw/openclaw/agents)

## Integration with Hermes

The kg_tool.py script provides Python functions that can be called from Hermes. The tools are registered in the Hermes tool system for easy access.

## Performance

- Search: < 100ms for typical queries
- Agent matching: < 50ms
- Skill recommendation: < 100ms

## Future Enhancements

- Vector-based semantic search
- Graph traversal for related entities
- Automatic agent delegation suggestions
- Skill learning from conversations
