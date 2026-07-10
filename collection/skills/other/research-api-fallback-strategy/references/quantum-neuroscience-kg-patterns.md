# Quantum-Neuroscience Research Patterns (from kg.db Analysis)

## Successful KG-Only Research Workflow (2026-05-26)

When arXiv API, web_search, web_extract, AND browser navigation ALL failed, the following workflow successfully produced 3 new skills:

### Step 1: Query kg_entities for Domain Papers

```python
# kg_entities uses 'content' NOT 'summary' — this is a common mistake
cursor.execute('''
    SELECT id, title, url, authors, published_date, content 
    FROM kg_entities 
    WHERE title LIKE '%quantum%' OR title LIKE '%Quantum%' OR title LIKE '%Neural%'
    ORDER BY id DESC LIMIT 15
''')
```

### Step 2: PageRank for Importance Ranking

```python
# pagerank table column is 'score' NOT 'pagerank'
cursor.execute('''
    SELECT pe.entity_id, pe.score, ke.title, ke.url, ke.authors, ke.content
    FROM pagerank pe
    JOIN kg_entities ke ON pe.entity_id = ke.id
    WHERE ke.title LIKE '%quantum%' OR ke.title LIKE '%Quantum%'
    ORDER BY pe.score DESC
    LIMIT 20
''')
```

### Step 3: Relationship Analysis for Research Clusters

```python
# kg_relationships columns: (id, source_id, target_id, relationship_type, weight, created_at)
# relationship_types: similarity, related_to, cites, shares_category
cursor.execute('''
    SELECT kr.source_id, ke1.title as src, kr.target_id, ke2.title as tgt, 
           kr.relationship_type, kr.weight
    FROM kg_relationships kr
    JOIN kg_entities ke1 ON kr.source_id = ke1.id
    JOIN kg_entities ke2 ON kr.target_id = ke2.id
    WHERE (ke1.title LIKE '%quantum%' OR ke2.title LIKE '%quantum%')
    AND kr.weight > 0.7
    LIMIT 30
''')
```

### Step 4: Create Skills from Paper Content

Extract reusable methodology from paper `content` field (abstracts stored in kg_entities):
- Identify core innovations
- Map methodological steps
- Note applications and pitfalls
- Record arXiv IDs for citation

### Key Schema Reminders

| Table | Key Columns | Notes |
|-------|------------|-------|
| kg_entities | id, title, url, **content**, authors, published_date, category, source | Uses `content` NOT `summary` |
| arxiv_papers | id, title, authors, published, categories, **summary**, pdf_url, abs_url | Separate table, has `summary` |
| pagerank | entity_id, **score** | Column is `score` NOT `pagerank` |
| kg_relationships | id, source_id, target_id, **relationship_type**, weight | Types: similarity, related_to, cites, shares_category |
| kg_vectors | id, entity_id, vector_data, created_at | BLOB embedding data |

## Quantum-Neuroscience Research Clusters Identified

### Cluster 1: Quantum-Like Cognitive Modeling
- **Core papers**: arXiv:2509.16253 (mental entanglement), GKSL dynamics paper
- **Key insight**: QLM uses quantum formalism WITHOUT requiring quantum brain
- **Methodology**: Operator algebras → tensor product structure → entanglement detection

### Cluster 2: Spiking-Quantum Hybrid Networks
- **Core papers**: arXiv:2512.03895 (SQDR-CNN), QLIF-CAST
- **Key insight**: Joint training of SNNs + quantum circuits in single backpropagation
- **Result**: 86% SOTA accuracy with 0.5% parameters

### Cluster 3: Quantum Brain Imaging
- **Core papers**: arXiv:2511.06401 (MEG quantum limit), quantum-limited-brain-imaging
- **Key insight**: Fundamental physical limits on brain measurement information capacity

### Cluster 4: Optical Neural Morphic Computing
- **Core paper**: arXiv:2605.17752 (Waveguide QED optical neural networks)
- **Key insight**: Eliminates optoelectronic activation bottleneck using transient quantum dynamics
