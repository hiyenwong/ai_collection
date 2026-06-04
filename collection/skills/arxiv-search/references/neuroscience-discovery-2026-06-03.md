# Neuroscience Research Discovery — 2026-06-03 Session

## Session Overview

- **Trigger**: Scheduled cron job for neuroscience paper discovery
- **Method**: RSS feed parsing (highest yield)
- **Outcome**: 697 papers parsed, 2 high-scoring papers selected, 2 skills created

## Key Findings

### RSS Feed Success (Primary Discovery Method)

**Yield**: 697 papers from `https://rss.arxiv.org/rss/q-bio.NC+cs.NE+cs.AI+cs.LG`

**Time**: <30 seconds for full download + parse

**Rate**: ZERO rate limits — RSS has no API-style throttling

**Pattern**:
```bash
curl -x http://127.0.0.1:7890 -s "https://rss.arxiv.org/rss/q-bio.NC+cs.NE+cs.AI+cs.LG" -o /tmp/neuro_rss.xml
python3 parse.py /tmp/neuro_rss.xml  # Regex parse, NO CDATA
```

**Key insight**: RSS is more reliable than browser in cron mode. Browser navigate to arxiv.org timed out (60s). RSS completed in <30s.

### Paper Scoring Strategy

Keywords (weight 2-3):
- Neuroscience: 'brain', 'neural', 'neuron', 'cortex', 'synaptic' (2pt)
- Dynamics: 'dynamics', 'oscillation', 'synchronization', 'phase' (3pt)
- Spiking: 'spiking', 'neuromorphic', 'LIF', 'STDP' (3pt)
- Computational: 'computational neuroscience', 'modeling', 'simulation' (2pt)
- Innovation: 'novel', 'framework', 'transformer', 'foundation model' (1pt)

**Top papers**:
- **2602.18690** (Score: 9.5): "Neural Fields as World Models" — isomorphic world models, motor gating, offline task learning
- **2511.13899** (Score: 8.5): "Factorized Low-Rank RNN" — FacRNN framework, independent latent dynamics, VAE + partial correlation penalty

### KG Database Schema (Verified)

**Active DB**: `/Users/hiyenwong/.hermes/knowledge_graph/kg.db`

**Tables**:
- `papers` (id INTEGER, arxiv_id TEXT, title, authors, published, categories, abstract, keywords, created_at)
- `relations` (id INTEGER, source_id, target_id, relation_type TEXT, created_at)

**NOT** the documented `entities` + `kg_vectors` schema — simpler schema works better for cron workflows.

### Obsidian Flat Structure

**Actual path**: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/{date} Neuroscience Research.md`

**NOT** nested `Neuroscience/arxiv/YYYY-MM/` — flat structure at root.

### Skills Created

1. **neural-fields-world-models** (arXiv:2602.18690)
   - Core: Isomorphic neural field world models with motor gating
   - Activation: neural field, world model, motor gating, offline learning
   - Method: Stationary neural fields with online/offline task distinction
   
2. **factorized-lowrank-rnn-independent-latent** (arXiv:2511.13899)
   - Core: FacRNN for discovering group-specific latent dynamics
   - Activation: factorized RNN, latent dynamics, VAE, partial correlation
   - Method: Low-rank decomposition + partial correlation penalty for group independence

### Workflow Steps Verified

1. **RSS download + Python parse** — 697 papers, <30s (RELIABLE)
2. **Paper scoring** — keyword-weighted scoring, top 50 candidates
3. **Duplicate check** — grep arxiv_id across skills/*/SKILL.md (4 levels)
4. **Skill creation** — init_skill.py + SKILL.md write
5. **ai_collection sync** — cp + INDEX.md patch + git commit/push
6. **Obsidian sync** — write_file to iCloud Documents root
7. **KG update** — Python script with parameterized INSERT (NOT sqlite3 CLI)

### Pitfalls Avoided

- **Browser timeout**: RSS used instead (reliable)
- **execute_code blocked**: write_file + terminal pattern
- **sqlite3 CLI silent failures**: Python parameterized queries
- **INDEX.md escaping**: Simple format, no special chars
- **KG schema mismatch**: Verified actual schema before INSERT
- **Duplicate skills**: Checked 4 levels before creation

## Lessons for Future Sessions

1. **RSS > Browser** in cron mode — higher yield, zero timeout
2. **KG path differs from docs** — verify schema with PRAGMA table_info before INSERT
3. **Obsidian is flat** — not nested subdirectories
4. **Python > sqlite3 CLI** — parameterized queries prevent silent failures
5. **4-level duplicate check** — prevents skill proliferation

## Related Skills

- [[neural-fields-world-models]]
- [[factorized-lowrank-rnn-independent-latent]]
- [[arxiv-search]] (this skill)
- [[kg-research-workflow]]