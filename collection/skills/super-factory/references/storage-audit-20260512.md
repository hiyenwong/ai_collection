# Super Factory Storage Architecture — Current State

Generated: 2026-05-12

## Knowledge Base (knowledge/)

**Backend:** SQLite (`.super_factory/data/knowledge.db`)
**Data Models:** Entity / Relation / Source (in `models.py`)
**Service Layer:** KnowledgeService facade with add/get/search/link/promote_tier
**Validation:** EntityValidator with spec-based rules (K003-K011)
**Repository Pattern:** Abstract interface in `repository/base.py`, implemented by SQLiteRepository
**Hook Bridge:** adapter.py connects KnowledgeService to Hook system

**Three-tier system:** research → finding → knowledge (promote-only, no downgrade)
**Search:** Keyword-only (title + content text match), no vector/semantic search yet
**Source tracking:** Citation provenance via Source model

**Missing capabilities (planned):**
- Vector/semantic search (embedding generation + cosine similarity)
- External kg.db integration (hermes-agent's `~/wiki/kg.db`)
- Automatic knowledge ingestion from `.research/findings/`
- Knowledge expiration/obsolescence management

## Memory System (memory/)

**Backend:** File-first JSON storage
**Data Model:** MemoryEntry frozen dataclass (immutable once created)
**Storage:** Individual JSON files per entry in `memory/store/{id}.json`
**Index:** `_index.json` for fast metadata querying
**Thread safety:** threading.Lock

**Categories:** decision | finding | error | lesson
**Query methods:**
- `query()` — filter by pipeline_id/agent_role/category/tags
- `relevant()` — keyword relevance with confidence-weighted scoring
- `prune(max_age_days=30)` — remove expired/old entries

**Directories:**
- `memory/store/` — long-term JSON storage
- `memory/blocked/` — blocked pipeline records
- `memory/skills/` — agent skill cache

**Missing capabilities (planned):**
- Vector/semantic search
- Layered memory architecture (working/longterm/procedural)
- Smart forgetting strategy (category-based retention, not just time cutoff)
- Memory consolidation/summarization

## OpenSpec Specs

Written in `openspec/core/`:
- `knowledge.spec.md` — 6 requirements (models, query, vector search, validation, auto-ingestion, kg.db integration)
- `memory.spec.md` — 7 requirements (models, file storage, query, cleanup, vector search, layered architecture, smart forgetting)
- `storage.spec.md` — 5 requirements (abstraction, embedding infra, DB migration, health check, backup)
- `storage.yaml` — centralized config template
