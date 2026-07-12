# Neuroscience Cron 2026-06-07: Complete Verification Session

## Context
Sunday 2026-06-07 neuroscience paper retrieval cron job. Goal: search arXiv for recent neuroscience papers, create skills, sync to ai_collection, update Obsidian wiki, import to kg.db.

## Key Learning: Complete Verification Before Creating

**Papers were ALREADY indexed** — full verification pattern prevented duplicate creation:

1. **Skills verified present**: 
   - `cross-scale-spatial-generative-neurodegeneration/SKILL.md` (320 lines) — already in both ~/.hermes/skills and ~/ai_github/ai_collection
   - `intrinsic-computational-functionalism/SKILL.md` (195 lines) — already present
   - `psychosis-scaling-critical-regime/SKILL.md` — INDEX.md entry at line 212
   - `boosting-brain-to-image-tribe-v2/SKILL.md` — INDEX.md entries at lines 83, 97, 205

2. **INDEX.md grep before insert**: Ran `grep "2606.05870" INDEX.md` and `grep "2606.06424" INDEX.md` — confirmed entries exist, skipped duplicate insertions

3. **Obsidian wiki notes created anyway**: 
   - `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/2026-06-07-neuroscience-cron-cross-scale-spatial-generative.md` (2693 bytes)
   - `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/2026-06-07-neuroscience-cron-intrinsic-computational-functionalism.md` (4534 bytes)
   - These are session-specific notes that supplement the existing skills, not duplicates

4. **kg.db import verified**: Both paper entities (2606.05870, 2606.06424) confirmed present via `SELECT id, name FROM entities WHERE id LIKE '2606%'`

5. **Git status clean**: Final verification `cd ~/ai_github/ai_collection && git status --short | head -10` returned empty (exit code 0) — all changes committed

## Fallback Chain Used

```
1. terminal curl → HTTP blocked (tirith:plain_http_to_sink)
2. web_search → limited results (444 chars)
3. web_extract → blocked (arxiv.org treated as private network)
4. skill_view(arxiv-search) → found fallback guidance
5. browser_navigate("https://arxiv.org/list/q-bio.NC/recent") → SUCCESS (40 entries)
6. browser_navigate("https://arxiv.org/abs/{id}") → paper details
```

**Weekend note**: RSS empty on Saturday/Sunday (`<skipDays>`). Browser listing pages worked when `/search/` may be blocked. `/list/{cat}/recent` is the most reliable weekend fallback.

## Top Paper Insights

### 2606.05870 — Cross-scale spatially-aware generative modeling
- **R²=86.04%, r=0.9439** spatial correlation
- **910 landmark genes → 68 cortical regions** degeneration prediction
- **Method**: variational generative framework + graph spatial smoothness prior
- **Application**: longitudinal Alzheimer's progression prediction from cross-scale gene expression data

### 2606.06424 — Intrinsic Computational Functionalism
- **Authors**: Shuqin Ma, Ryota Kanai
- **Framework**: Three-tier decomposition for observer-relativity problem in consciousness theory
- **Tiers**: interpreter-relative ❌, theoretically-constrained ⚠️, dynamics-internal ✅
- **Criteria**: C1 (normativity), C2 (coherence) for intrinsic computational functionalism

## kg.db Import Pattern (Verified)

```python
import sqlite3
import json

conn = sqlite3.connect('~/.hermes/knowledge_graph/kg.db')
cur = conn.cursor()

# Insert pattern
cur.execute("""
    INSERT INTO entities (id, name, type, description, metadata, created_at)
    VALUES (?, ?, ?, ?, ?, datetime('now'))
""", (arxiv_id, paper_title, 'paper', abstract, json.dumps({'category': category, 'authors': authors})))

conn.commit()

# Verification
cur.execute("SELECT id, name FROM entities WHERE id LIKE '2606%'")
print(cur.fetchall())
```

**Schema verified**: `entities` table has `id` (TEXT, arxiv IDs), `rowid` (INTEGER auto-increment). `kg_vectors.entity_id` references `rowid`, not `id`. `relationships` columns: `from_entity`, `to_entity`, `relationship_type`, `weight`.

## Pitfalls Avoided

1. **Duplicate skill creation**: Verified existing skills in both locations before creating new ones
2. **INDEX.md duplicate entries**: Grep'd for arxiv IDs before inserting — confirmed existing, skipped
3. **Git add capturing sibling sessions**: Used targeted `git add` (not `-A`) in shared working tree
4. **kg.db schema mismatch**: Verified actual schema with `PRAGMA table_info` before INSERT

## Outcome

- **Papers discovered**: 6 (2606.06424, 2606.05870, 2606.06290, 2606.05206, 2606.05189, 2606.06345)
- **Relevant skills**: 4 already present (cross-scale, intrinsic-computational-functionalism, psychosis-scaling, boosting-brain-to-image)
- **Obsidian notes**: 2 created (session-specific supplement)
- **kg.db entities**: 2 imported (2606.05870, 2606.06424)
- **Git status**: clean working tree (all changes committed)

## Lessons for Future Sessions

1. **Always verify before create**: Grep INDEX.md for arxiv IDs, `ls` both skill directories for existing skills
2. **Browser fallback is reliable**: `/list/{cat}/recent` works on weekends when RSS/API fail
3. **kg.db import pattern**: Use verified schema, capture `lastrowid` for vector embeddings
4. **Session-specific notes are OK**: Obsidian wiki notes supplement skills, even when skills already exist
5. **Clean git status before push**: `git status --short | head -10` should return empty for clean push