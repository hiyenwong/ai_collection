---
name: quantum-ml-research
description: "Quantum Machine Learning research assistant. Searches arxiv for quantum ML papers, analyzes patterns from knowledge graph (kg.db), extracts concepts from quantum circuits, neural networks, and finance/medical applications. Use when researching quantum computing applications, quantum algorithms, quantum portfolio optimization, quantum Monte Carlo, quantum neural networks, hybrid quantum-classical medical classification, or analyzing quantum ML literature. Activation: quantum ML research, quantum machine learning, quantum circuit learning, quantum neural network, 量子机器学习, quantum finance research, quantum medical imaging."
---

# Quantum Machine Learning Research

Research assistant for quantum computing applications in machine learning, finance, and medical diagnosis.

## Activation Keywords

- quantum ML research
- quantum machine learning
- quantum circuit learning
- quantum neural network
- quantum portfolio optimization
- quantum Monte Carlo
- quantum algorithms
- quantum medical imaging
- hybrid quantum medical
- 量子机器学习
- 量子神经网络

## Tools Used

- `exec`: Run Python scripts for arxiv search, sqlite3 for kg.db
- `read`: Load skill files, analyze papers
- `web_search`: Search for quantum ML papers
- `sqlite3`: Query knowledge graph (kg.db) directly

## Critical Pitfalls

- **arxiv API requires HTTPS**: `http://export.arxiv.org/api/query` is blocked by security scanner. Always use `https://export.arxiv.org/api/query`.
- **web_extract blocks arxiv URLs**: The web_extract tool returns "Blocked: URL targets a private or internal network address" for arxiv. Use curl + arxiv API XML parsing instead.
- **kg.db path**: `/Users/hiyenwong/.openclaw/workspace/kg.db` (NOT `/Users/hiyenwong/wiki/kg.db`)
- **No kg_tool subcommands for pagerank/louvain**: The kg_tool binary does not have `pagerank` or `louvain` subcommands. Implement these in Python using sqlite3 directly.

## Workflow

### Step 1: Search Literature

**IMPORTANT**: arxiv API requires HTTPS. HTTP URLs are blocked by security scanner. web_extract also blocks arxiv URLs.

```python
# Correct: HTTPS arxiv API
url = 'https://export.arxiv.org/api/query?search_query=all:quantum+machine+learning&max_results=10&sortBy=submittedDate'

# With proxy (if needed):
# curl -s "https://export.arxiv.org/api/query?id_list=2504.13910,2604.16953" --proxy http://127.0.0.1:7890
```

Parse the Atom XML response with Python's `xml.etree.ElementTree`:
```python
import xml.etree.ElementTree as ET
ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
root = ET.fromstring(xml_response)
for entry in root.findall('atom:entry', ns):
    title = entry.find('atom:title', ns).text.strip()
    summary = entry.find('atom:summary', ns).text.strip()
    # ... extract authors, categories, published date
```

Categories to search:
- `quant-ph` - Quantum Physics
- `cs.LG` - Machine Learning
- `cs.CV` - Computer Vision (medical imaging)
- `cs.AI` - Artificial Intelligence
- `cs.ET` - Emerging Technologies

### Step 2: Import to Knowledge Graph

kg.db schema:
```sql
CREATE TABLE kg_entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT UNIQUE NOT NULL,
    content TEXT,
    authors TEXT,
    published_date TEXT,
    category TEXT,
    source TEXT
);
CREATE TABLE kg_vectors (id, entity_id, vector_data BLOB);
CREATE TABLE kg_relations (source INT, target INT, type TEXT, weight REAL);
CREATE TABLE kg_relationships (source_id, target_id, relationship_type, weight);
```

Import paper:
```sql
INSERT OR IGNORE INTO kg_entities (title, url, content, authors, published_date, category, source)
VALUES ('title', 'url', 'abstract_text', 'authors', 'date', 'categories', 'arxiv');
```

Generate TF-IDF vector:
```python
import json, sqlite3
# Build term frequency from abstract, multiply by IDF from corpus
# Store top-50 features as JSON in vector_data column
```

### Step 3: Analyze Knowledge Graph (Python, not kg_tool)

```python
import sqlite3
conn = sqlite3.connect('/Users/hiyenwong/.openclaw/workspace/kg.db')
cursor = conn.cursor()

# PageRank (implement in Python — no kg_tool subcommand)
cursor.execute("SELECT source, target, weight FROM kg_relations")
edges = cursor.fetchall()
# Build adjacency, iterate damping factor 0.85 for ~20 iterations

# Community detection by category clustering
cursor.execute("SELECT id, category FROM kg_entities WHERE category IS NOT NULL")
# Group papers by shared categories

# Vector similarity
cursor.execute("SELECT entity_id, vector_data FROM kg_vectors")
# Cosine similarity on JSON-encoded feature vectors
```

### Step 4: Extract Patterns

From quantum ML papers, extract:
1. **Quantum Circuit Architecture**: Gate types, circuit depth, qubit count
2. **Learning Paradigm**: VQE, QAOA, quantum annealing, hybrid quantum-classical
3. **Application Domain**: Finance, chemistry, medical diagnosis, optimization
4. **Performance Metrics**: Accuracy, F1, AUC-ROC, quantum advantage claims
5. **Feature Fusion Strategy**: How quantum and classical features are combined

## Key Research Areas

### Quantum Medical Image Classification (see references/quantum-medical.md)

**Key pattern**: Hybrid quantum-classical architecture for diagnosis
```
Classical Backbone (ResNet/CNN) → Feature Extractor → Quantum Circuit (4-qubit VQC)
→ Measurement → Classifier
```

**Feature Fusion Strategies**:
- **SHF** (Static): Offline extraction, simple concatenation
- **DHF** (Dynamic): End-to-end co-adaptation
- **TSHF** (Temperature-Scaled): Learnable scalar balances gradients ⭐ Best

**Key results**: TSHF + ResNet + trainable QC → 87.82% acc, 91.77% F1 on BreastMNIST

**Privacy-aware federated**: Tensor-network (TTN/MPS/MERA) frontend → MPC aggregation → Quantum-Enhanced Processor

### Quantum Circuit Learning

Papers focus on:
- Parameterized quantum circuits as neural networks
- Structure optimization for shallow circuits
- Quantum circuit optimization with RL
- Framework-agnostic quantum ML

### Quantum Finance

Applications:
- Portfolio optimization (QAOA, quantum annealing)
- Risk analytics (quantum Monte Carlo)
- Derivative pricing
- Option pricing

## Knowledge Graph Integration

### Schema Notes (CRITICAL — verified 2026-05-06)

- **kg.db location**: `/Users/hiyenwong/.openclaw/workspace/kg.db`
- **kg_vectors**: `vector_data` is raw `float32` bytes (256-dim = 1024 bytes per vector), NOT JSON strings. Load with: `np.frombuffer(row[0], dtype=np.float32)`
- **kg_relationships**: Column is `relationship_type` (NOT `relationship`). Schema: `(id, source_id, target_id, relationship_type, weight, created_at)`
- **kg_relations**: Column is `type` (NOT `rel_type`). Schema: `(source, target, type, weight)`

### Query Patterns

```bash
# kg.db is at /Users/hiyenwong/.openclaw/workspace/kg.db

# Find quantum finance papers
sqlite3 kg.db "SELECT id, title FROM kg_entities WHERE category LIKE '%quant%' AND title LIKE '%Finance%'"

# Find quantum medical papers
sqlite3 kg.db "SELECT id, title FROM kg_entities WHERE category LIKE '%quant%' AND (title LIKE '%Medical%' OR title LIKE '%Cancer%' OR title LIKE '%Diagnosis%')"

# Count by category
sqlite3 kg.db "SELECT category, COUNT(*) FROM kg_entities GROUP BY category ORDER BY COUNT(*) DESC"
```

## arXiv Search (with fallback)

**IMPORTANT**: arXiv API (`export.arxiv.org`) is often unreachable from this environment —
it either times out through the sandbox or returns "Rate exceeded" through the proxy.
Always use the fallback workflow below.

### Fallback Workflow (preferred)

```bash
# 1. Search via web_search tool for arxiv papers
# Query: "site:arxiv.org quantum medical healthcare" or similar
# Extract arxiv IDs from results (e.g. 2511.02051, 2603.17790)

# 2. Download HTML for each paper
curl -s -x http://127.0.0.1:7890 --max-time 20 \
  -o /tmp/paper.html "https://arxiv.org/abs/2511.02051"

# 3. Extract metadata via Python regex (NOT piping curl to python)
python3 -c "
import re
with open('/tmp/paper.html') as f: html = f.read()
m = re.search(r'<blockquote[^>]*class=\"abstract[^\"]*\">(.*?)</blockquote>', html, re.DOTALL)
abstract = re.sub(r'<[^>]+>', ' ', m.group(1)).strip() if m else ''
m = re.search(r'<title>(.*?)</title>', html)
title = m.group(1).strip() if m else ''
title = re.sub(r'^\[\d+\.\d+\]\s*', '', title)
print(f'{title}\\n{abstract[:500]}')
"
```

### Direct API (when available)

Use `https://` not `http://` — the API returns 301 redirect:
```python
url = 'https://export.arxiv.org/api/query?search_query=all:quantum+AND+all:medical&max_results=5'
```

## References

- [references/quantum-medical.md](references/quantum-medical.md) — Quantum ML for medical diagnosis
- [references/QUANTUM_FINANCE.md](references/QUANTUM_FINANCE.md) — Quantum finance applications
- [references/QUANTUM_CIRCUITS.md](references/QUANTUM_CIRCUITS.md) — Quantum circuit learning patterns

## Related Skills

- `arxiv-search`: General arxiv search
- `hybrid-quantum-classical-architecture`: System-level hybrid architecture design
- `skill-extractor`: Extract patterns from papers
