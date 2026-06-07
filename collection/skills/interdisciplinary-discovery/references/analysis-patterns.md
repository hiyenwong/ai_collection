# Analysis Patterns

Common patterns for interdisciplinary discovery using knowledge graphs.

## Pattern 1: Domain Bridge Discovery

**Use case:** Find entities connecting two different research domains.

**Workflow:**
1. Search entities in domain A: `kg_tool search kg.db "domain_a_keyword"`
2. Search entities in domain B: `kg_tool search kg.db "domain_b_keyword"`
3. Check similarity between representative entities
4. Look for >0.8 similarity as bridge indicators

**Example: Quantum-Finance Bridge**
```bash
# Step 1: Find quantum entities
kg_tool search kg.db "quantum" | grep finance

# Step 2: Get entity IDs
sqlite3 kg.db "SELECT id FROM kg_entities WHERE name LIKE '%quantum%finance%'"

# Step 3: Find similarities
kg_tool similar kg.db 128 5  # quantum finance entity
# Results: quantum economics (0.87), Quantum Computing for Finance (0.84)

# Interpretation: Strong bridge between quantum and finance domains
```

**Key indicators:**
- Similarity >0.8: Strong bridge
- Entity appears in both search results: Direct bridge
- High PageRank + cross-domain similarity: Influential bridge

## Pattern 2: Community Cross-Reference

**Use case:** Find research areas spanning multiple communities.

**Workflow:**
1. Run Louvain to detect communities
2. Identify entities in different communities
3. Check similarity between entities from different communities
4. High similarity + different community = interdisciplinary entity

**Example: Quantum Neuroscience**
```bash
# Step 1: Detect communities
kg_tool louvain kg.db | grep "Entity 9"
# Entity 9 -> Community 0

# Step 2: Check another entity
kg_tool louvain kg.db | grep "Entity 128"
# Entity 128 -> Community 1

# Step 3: Check similarity
kg_tool similar kg.db 9 5
# Brain connectivity tools (0.15), Spiking neural networks (0.14)

# Interpretation: Quantum cryptography (Comm 0) linked to neuroscience (via 0.15 similarity)
```

**Note:** Lower similarity (<0.5) may still indicate valuable bridges.

## Pattern 3: PageRank Influence Analysis

**Use case:** Find most influential cross-domain entities.

**Workflow:**
1. Run PageRank to find top entities
2. Check entity types (topic vs paper)
3. Topics with high PageRank = influential research areas
4. Search for papers related to high PageRank topics

**Example: Quantum Algorithms Influence**
```bash
# Step 1: PageRank
kg_tool pagerank kg.db
# Entity 343: Quantum Algorithms (0.045)  # Highest!

# Step 2: Check entity type
sqlite3 kg.db "SELECT entity_type, name FROM kg_entities WHERE id = 343"
# topic | Quantum Algorithms

# Step 3: Find related papers
kg_tool search kg.db "quantum algorithm"
# Returns papers citing this topic

# Interpretation: Quantum algorithms is core influential area
```

**Key insight:** High PageRank topics often reveal interdisciplinary hubs.

## Pattern 4: Unexpected Connection Mining

**Use case:** Discover surprising interdisciplinary connections.

**Workflow:**
1. Pick random entity from domain A
2. Run similarity search with k=10
3. Look for entities from unexpected domain B
4. Analyze the connection type

**Example: Music-Quantum Bridge**
```bash
# Step 1: Random entity
kg_tool similar kg.db <music_entity> 10

# Step 2: Look for quantum in results
# [unexpected] quantum harmonics (0.12)
# [unexpected] quantum oscillation (0.11)

# Step 3: Investigate
sqlite3 kg.db "SELECT properties FROM kg_entities WHERE name LIKE '%quantum harmonics%'"

# Interpretation: Music theory has quantum physics connections through harmonic analysis
```

**Threshold for discovery:**
- Similarity 0.1-0.3: Weak but interesting connection
- Similarity <0.1: May be noise, requires investigation

## Pattern 5: Temporal Trend Analysis

**Use case:** Track interdisciplinary evolution over time.

**Workflow:**
1. Compare snapshots at different times
2. Track PageRank changes for bridge entities
3. Monitor community merging/splitting
4. Identify emerging cross-domain areas

**Implementation:**
```bash
# Save daily snapshots
sqlite3 kg.db "SELECT id, name FROM kg_entities ORDER BY created_at DESC LIMIT 10" > snapshots/daily_entities.txt

# Track PageRank evolution
kg_tool pagerank kg.db > snapshots/daily_pagerank.txt

# Compare over time
diff snapshots/week1_pagerank.txt snapshots/week2_pagerank.txt
```

**Indicators:**
- Rising PageRank of bridge entity: Growing interdisciplinary interest
- Community merging: Domains converging
- New bridge entities: Emerging interdisciplinary areas

## Pattern 6: Keyword Co-occurrence Network

**Use case:** Build keyword network from entity properties.

**Workflow:**
1. Extract keywords from entity properties JSON
2. Build co-occurrence network
3. Find keywords appearing in multiple domains
4. Identify interdisciplinary keywords

**Implementation:**
```python
import sqlite3
import json

conn = sqlite3.connect('kg.db')
cursor = conn.cursor()

# Extract keywords
keywords = {}
for row in cursor.execute("SELECT id, properties FROM kg_entities WHERE properties IS NOT NULL"):
    props = json.loads(row[1])
    if 'keywords' in props:
        for kw in props['keywords']:
            if kw not in keywords:
                keywords[kw] = []
            keywords[kw].append(row[0])

# Find cross-domain keywords
cross_domain = {k: v for k, v in keywords.items() if len(v) > 3}
```

**Example output:**
```json
{
  "machine learning": [1, 23, 45, 67, 89],
  "quantum": [2, 12, 34, 56, 78, 90],
  "neural network": [3, 24, 46, 68]  # Appears in quantum papers!
}
```

## Analysis Checklist

Before concluding interdisciplinary discovery:

1. ✅ Run PageRank to find influential nodes
2. ✅ Run Louvain to detect communities
3. ✅ Check similarity for multiple entities
4. ✅ Cross-reference different communities
5. ✅ Investigate unexpected connections
6. ✅ Document findings in memory/
7. ✅ Validate with domain knowledge

## Common Pitfalls

1. **Over-interpreting low similarity** - <0.1 may be noise
2. **Ignoring entity types** - Papers vs topics have different roles
3. **Single entity analysis** - Always check multiple entities
4. **Missing database locks** - Add delays between operations
5. **Forgetting to document** - Always save to memory/

## Reporting Format

When documenting discoveries:

```markdown
## Interdisciplinary Discovery: [Domain A] - [Domain B]

**Date:** YYYY-MM-DD

### Method
- PageRank: Entity X (score Y)
- Similarity: Entity A → Entity B (0.ZZ)
- Community: Entity A (Comm 1), Entity B (Comm 2)

### Connection
[Brief description of how domains connect]

### Evidence
[Specific similarity scores, common keywords, shared papers]

### Implications
[Research opportunities, skill extraction potential, follow-up]

### References
[Entity IDs, papers, keywords]
```

## Integration with Skill Extraction

After discovering patterns, consider creating skills:

1. Identify recurring pattern
2. Extract workflow steps
3. Document in SKILL.md
4. Add to skill library

**Example skills from discoveries:**
- `quantum-finance-analysis`: Bridge between quantum computing and finance
- `interdisciplinary-literature-synthesis`: Cross-domain paper synthesis
- `kg-research-workflow`: General KG analysis workflow