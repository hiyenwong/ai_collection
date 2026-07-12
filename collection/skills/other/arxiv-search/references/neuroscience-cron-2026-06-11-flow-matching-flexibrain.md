# Neuroscience Cron Session: 2026-06-11 Afternoon

## Papers Processed

1. **arXiv:2606.11833** - "Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics"
   - Authors: Sam Gijsen, Michał Łukomski, Marc-André Schulz, Kerstin Ritter
   - Keywords: flow matching, diffusion transformer, fMRI, zero-shot generation, compositional priors
   - Score: theoretical framework with mathematical formulation
   - Skill: `flow-matching-in-context-priors-brain-dynamics`

2. **arXiv:2606.11500** - "FlexiBrain: Resolution-Agnostic Voxel-Level Encoding for Native fMRI"
   - Authors: Mo Wang, Wenhao Ye, Junfeng Xia, Minghao Xu, Hongkai Wen, Quanying Liu
   - Keywords: Mamba-JEPA, native fMRI, preprocessing-free, voxel-level encoding
   - Score: engineering framework with practical architecture
   - Skill: `flexibrain-resolution-agnostic-fmri-encoding`

## Key Session Discoveries

### kg.db Schema Drift Pattern

**CRITICAL**: This session revealed kg.db schema variance between sessions.

**Afternoon session found**:
```sql
-- papers table
CREATE TABLE papers (
    arxiv_id TEXT PRIMARY KEY,
    title TEXT,
    authors TEXT,
    skill TEXT,
    date_added TEXT
);
-- NO id column, arxiv_id is PRIMARY KEY directly

-- skills table
CREATE TABLE skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    category TEXT,
    created_at TEXT,
    path TEXT
);
```

**Insert patterns used**:
```bash
# Papers insert (verified working)
sqlite3 kg.db "INSERT OR REPLACE INTO papers (arxiv_id, title, authors, skill, date_added) VALUES ('2606.11833', 'Flow Matching...', 'Authors', 'flow-matching-in-context-priors-brain-dynamics', datetime('now'))"

# Skills insert (verified working)
sqlite3 kg.db "INSERT INTO skills (name, description, category, created_at, path) VALUES ('flexibrain-resolution-agnostic-fmri-encoding', 'Description...', 'neuroscience', datetime('now'), 'collection/skills/flexibrain-resolution-agnostic-fmri-encoding')"
```

**Morning session (same day) documented different schema**:
- Claimed `id INTEGER PK AUTOINCREMENT + arxiv_id TEXT UNIQUE`
- This contradicts afternoon findings

**Resolution**: ALWAYS run `PRAGMA table_info(papers)` before insert. Schema drifts across sessions — do not assume fixed schema.

### Complete Workflow Pattern

1. **Search**: browser_navigate → `https://arxiv.org/list/q-bio.NC/recent` (listing page fallback, NOT `/abs/` which causes ID resolution mismatch)
2. **Score**: Dual-keyword neuroscience scoring (brain network, neural dynamics, spiking, computational neuroscience keywords)
3. **Select**: 2 papers with theoretical frameworks (Flow Matching + FlexiBrain)
4. **Create skills**: write_file → `~/.hermes/skills/ai_collection/{skill-name}/SKILL.md`
5. **Sync to ai_collection**: `cp -r ~/.hermes/skills/ai_collection/{skill-name}/ ~/ai_github/ai_collection/collection/skills/{skill-name}/`
6. **Update INDEX.md**: patch → prepend entries under date heading
7. **Git workflow**: 
   - `git checkout neuro-cron-2026-06-11` (branch already existed)
   - `git add collection/skills/{skill-name}/ INDEX.md`
   - `git commit -m "feat: add {skill-name} from arXiv {id}"`
   - `git push origin neuro-cron-2026-06-11`
8. **Obsidian sync**: write_file → `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/2026-06-11 神经科学研究 - Flow Matching + FlexiBrain.md`
9. **kg.db insert**: 
   - Papers: `INSERT OR REPLACE` with correct schema
   - Skills: explicit INSERT for missing skill (flexibrain)
   - Verify: `sqlite3 kg.db "SELECT * FROM papers WHERE arxiv_id='2606.11833'"`

### Git Branch Sharing Pattern

- Branch `neuro-cron-2026-06-11` already existed from morning session
- Afternoon session appended commit to same branch
- No collision: papers differ → skills differ
- Targeted `git add collection/skills/{specific-skill}/` (not `-A`) avoids capturing sibling session files

### Paper Already in kg.db Pattern

Both papers (2606.11833, 2606.11500) already existed in kg.db from prior session:
```bash
sqlite3 kg.db "SELECT arxiv_id, title FROM papers WHERE arxiv_id IN ('2606.11833', '2606.11500')"
# Both found → UNIQUE constraint prevents duplicate insert
```

Skill `flow-matching-in-context-priors-brain-dynamics` also already registered.
Skill `flexibrain-resolution-agnostic-fmri-encoding` required explicit INSERT.

### Skill Architecture Observation

**Future consideration**: Paper-specific skills should be `references/` files under umbrella skills rather than flat list. Current architecture has ~296 papers but creates independent skills per paper — leads to proliferation. Better pattern: umbrella skill (e.g., `fMRI-foundation-models`) with `references/flow-matching-2026-06-11.md` and `references/flexibrain-2026-06-11.md` containing session-specific detail.

## Lessons Learned

1. **kg.db schema is UNSTABLE** — varies by session. Always PRAGMA before insert.
2. **Papers may already exist** — UNIQUE constraint handles duplicates safely.
3. **Skills table may need explicit INSERT** — not all skills auto-register.
4. **Git branch sharing safe** — targeted add prevents sibling collision.
5. **`/abs/` navigation unreliable** — listing page extraction is correct pattern.
6. **INDEX.md prepend before git add** — patch workflow is reliable.

## kg.db State After Session

- Papers: 296 total
- Skills table contains both flow-matching and flexibrain skills (category=neuroscience)
- Verified with: `sqlite3 kg.db "SELECT name, category FROM skills WHERE name LIKE '%flow%' OR name LIKE '%flexi%'"`