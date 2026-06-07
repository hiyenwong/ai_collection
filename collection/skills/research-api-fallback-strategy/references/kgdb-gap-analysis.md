# kg.db Gap Analysis Pattern

When all external APIs fail (arXiv 429 + web_search NoneType), use kg.db as the primary data source for skill creation.

## Quick Gap Analysis Script

```python
import sqlite3, os

conn = sqlite3.connect('/path/to/kg.db')
cursor = conn.cursor()

# 1. Get recent papers in domain
cursor.execute("""
    SELECT id, title, url, published_date, category, content
    FROM kg_entities 
    WHERE published_date >= '2026-05'
      AND (title LIKE '%quantum%' OR title LIKE '%neuro%' 
           OR title LIKE '%spiking%' OR title LIKE '%brain%')
    ORDER BY published_date DESC
""")
papers = cursor.fetchall()

# 2. Check which have skills
skills_dir = '/path/to/ai_collection/collection/skills/'
missing = []
for p in papers:
    # Derive skill name: lowercase, hyphenate key words from title
    title_words = p[1].lower().replace(':', '').replace(',', '').split()
    # Pick 2-3 most distinctive words
    key_words = [w for w in title_words if len(w) > 3]
    skill_name = '-'.join(key_words[:3])
    
    if not os.path.exists(f'{skills_dir}/{skill_name}/SKILL.md'):
        missing.append({
            'id': p[0], 'title': p[1], 'url': p[2],
            'date': p[3], 'category': p[4], 'content': p[5],
            'suggested_name': skill_name
        })

print(f"Found {len(missing)} papers without skills")
```

## PageRank Analysis

```bash
./scripts/kg_tool/target/release/kg_tool pagerank --top 10
```

Output format: `[id] Title PR=value`

## Relationship-Based Community Detection

```python
# Find relationships between top entities
cursor.execute("""
    SELECT r.source, r.target, r.type, r.weight,
           e1.title as source_title, e2.title as target_title
    FROM kg_relations r
    JOIN kg_entities e1 ON r.source = e1.id
    JOIN kg_entities e2 ON r.target = e2.id
    WHERE r.source IN ({0})
    ORDER BY r.source
""".format(','.join(top_entity_ids)))
```

## Schema Reference

| Table | Columns |
|-------|---------|
| kg_entities | id, title, url, content, authors, published_date, category, source, created_at, updated_at |
| kg_relations | source, target, type, weight |
| kg_vectors | id, entity_id, vector_data (binary), created_at |

## Results from Session 2026-05-18

- 1153 entities, 3378 relations, 1147 vectors
- PageRank top: Quantum computing+AI (0.002948), Quantum healthcare (0.002493), Quantum Circuit Learning (0.001777)
- Community types: related (99 entities), category_overlap (11), related_to (17)
- Produced 6 new skills with zero external API calls
