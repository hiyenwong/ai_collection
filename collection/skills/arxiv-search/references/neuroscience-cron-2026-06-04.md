# Neuroscience Literature Search Workflow (2026-06-04)

Session: Automated cron job for neuroscience paper discovery, skill creation, and knowledge graph sync.

## RSS Dual-Keyword Scoring for Neuroscience (Verified 2026-06-04)

Score papers by counting keyword matches in title + abstract:
- **Neuroscience keywords**: neuroscience, brain network, neural dynamics, spiking neural network, computational neuroscience, cortical, neural circuit, synaptic, plasticity (9 keywords total)
- **Filter**: Count matches across all keywords
- **Sort**: by total_score descending
- **Top papers**:
  - **2512.05252** (Score: 9) - "Competition, stability, and functionality in E-I neural circuits: a game-theoretic energetic framework"
  - **2606.04426** (Score: 6) - "Discrete signaling mediates chaotic regularization in RNNs"

## Fallback Chain Executed

1. **RSS** → 64 papers with keyword score ≥ 3
2. **browser_navigate** → `https://arxiv.org/abs/{id}` for individual paper details
3. No API or web_search needed (RSS sufficient)

## Skills Created

### 1. discrete-signaling-chaotic-regularization
- **arXiv ID**: 2606.04426 (submitted 3 Jun 2026)
- **Core methodology**: Introduces Onsager reaction term to stabilize neural network dynamics without Hebbian learning
- **Category**: ai_collection (neuromorphic/computational neuroscience)
- **Key insight**: Discrete signaling mechanism can freeze chaotic dynamics in RNNs

### 2. competition-stability-ei-circuits
- **arXiv ID**: 2512.05252
- **Core methodology**: Game-theoretic energetic framework for E-I balance analysis
- **Category**: ai_collection (neural circuits/theoretical neuroscience)
- **Key insight**: Competition-stability-functionality trade-off formalized via game theory

## Skill Sync Workflow

```bash
# Create skills in Hermes
mkdir -p ~/.hermes/skills/ai_collection/{skill-name}
write_file to SKILL.md

# Copy to ai_collection GitHub
cp -r ~/.hermes/skills/ai_collection/{skill-name} ~/ai_github/ai_collection/collection/skills/

# Update INDEX.md
read_file ~/ai_github/ai_collection/INDEX.md (FULL FILE)
write_file with new entries appended

# Git workflow
cd ~/ai_github/ai_collection
git add collection/skills/{skill-name}/ INDEX.md
git commit -m "feat: add 2 neuroscience skills (arXiv: 2606.04426, 2512.05252)"
git push
```

## INDEX.md Update Pattern

Add neuroscience entries before git commit:
```markdown
## 2026-06-04 - Neuroscience Research (Cron Job)

### Competition, stability, and functionality in E-I neural circuits
- [[competition-stability-ei-circuits]] - Game-theoretic energetic framework for E-I balance (arXiv: 2512.05252)
  - Game-theoretic analysis of excitatory-inhibitory competition
  - Energetic constraints on neural circuit functionality
  - Stability-functionality trade-off characterization
  - **Activation**: E-I balance, neural circuit, game theory, energetic framework

### Discrete signaling mediates chaotic regularization in RNNs
- [[discrete-signaling-chaotic-regularization]] - Chaos stabilization via discrete signaling (arXiv: 2606.04426)
  - Onsager reaction term for chaos suppression
  - Discrete signaling mechanism without Hebbian learning
  - RNN dynamics regularization pathway
  - **Activation**: chaotic regularization, RNN dynamics, discrete signaling, Onsager term
```

## Obsidian Note Workflow

Save to vault at `/Users/hiyenwong/obsidian/`:
- Title: `神经科学前沿-2026-06-04.md`
- Structure: YAML frontmatter + paper summaries + skill links + methodology highlights
- Content: 6774 bytes covering both papers

## Knowledge Graph Import to 5 Instances

Expanded from 3 to 5 kg.db instances (verified 2026-06-04):
1. **Hermes main**: `/Users/hiyenwong/.hermes/kg.db` → `arxiv_papers` table (bare IDs: `2606.04426`, `2512.05252`)
2. **Wiki**: `/Users/hiyenwong/wiki/kg.db` → `entities` + `kg_vectors` (prefix: `arxiv:2606.04426`)
3. **Workspace scripts**: `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db` → `entities` + `kg_vectors`
4. **Workspace root**: `/Users/hiyenwong/.openclaw/kg.db` → `kg_entities` + `kg_vectors` (entity_id format)
5. **ai_collection**: `/Users/hiyenwong/ai_github/ai_collection/kg.db` → `entities`

### Import Script Pattern

```python
# Hermes kg.db - use bare arXiv IDs
conn1.execute("INSERT INTO arxiv_papers (id, title, abstract, authors, submitted_date, category) VALUES (?, ?, ?, ?, ?, ?)",
              ('2606.04426', '...', '...', '...', '2026-06-03', 'q-bio.NC'))

# Other kg.db - use arxiv: prefix for entities
conn2.execute("INSERT INTO entities (id, name, entity_type, metadata, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
              ('arxiv:2606.04426', 'Discrete signaling...', 'arxiv_paper', json.dumps({...}), '2026-06-04', '2026-06-04'))

# kg_vectors table - deterministic 256-dim embedding
embedding = generate_embedding_from_sha256(f"arxiv:2606.04426:{title}")
conn2.execute("INSERT INTO kg_vectors (entity_id, vector) VALUES (?, ?)",
              ('arxiv:2606.04426', json.dumps(embedding)))
```

### Pitfall: ID Format Varies by Database

- **Hermes kg.db `arxiv_papers`**: Use bare IDs (`2606.04426`) — NOT `arxiv:2606.04426`
- **Other kg.db `entities` tables**: Use prefix (`arxiv:2606.04426`)
- Verified via SQL queries after import

## INDEX.md Integrity Pitfall (Resolved 2026-06-04)

**Problem**: `write_file` truncated INDEX.md content when partial view was used.

**Solution**: Always re-read FULL file before overwriting:
```python
# WRONG - causes truncation
existing = read_file(path, offset=1, limit=100)  # partial view
write_file(path, new_content)  # overwrites with incomplete base

# CORRECT - preserves all content
existing = read_file(path)  # full file
write_file(path, existing_content + new_entries)  # append without truncation
```

## Git Commit Generated

```
commit ae3cb070
Author: hiyenwong
Date: Thu Jun 4 2026

feat: add 2 neuroscience skills - discrete-signaling-chaotic-regularization and competition-stability-ei-circuits (arXiv: 2606.04426, 2512.05252)
```

Pushed to `origin/main` successfully.

## Verified Output

- Skills created: 2 (both in `~/.hermes/skills/ai_collection/` and `~/ai_github/ai_collection/collection/skills/`)
- INDEX.md updated: Neuroscience section added
- Obsidian note: `/Users/hiyenwong/obsidian/神经科学前沿-2026-06-04.md` (6774 bytes)
- kg.db imports: 2 papers → 5 database instances (verified via SELECT queries)
- Git push: Success

## Key Insights for Future Sessions

1. **RSS neuroscience scoring**: 9 keywords → effective paper ranking (score ≥ 3 threshold works)
2. **kg.db expansion**: Now 5 instances (from 3) — script must handle varying schemas
3. **INDEX.md integrity**: Full file read before overwrite prevents truncation
4. **ID format pitfall**: Hermes `arxiv_papers` uses bare IDs, others use `arxiv:` prefix
5. **Skill sync pattern**: Same as Systems+Quantum workflow — dual directory copy + INDEX.md + git

## Overlap with Existing References

- `neuroscience-cron-2026-06-02.md` — earlier session with 3 papers (Score Broadcast, MindVoice, Metastable Mind)
- `neuroscience-cron-2026-06-04.md` — this session with 2 papers (Discrete Signaling, E-I Circuits)
- Both use same RSS → browser → skill → git → Obsidian → kg.db pattern
- Key difference: 2026-06-04 expanded kg.db to 5 instances and resolved INDEX.md truncation pitfall