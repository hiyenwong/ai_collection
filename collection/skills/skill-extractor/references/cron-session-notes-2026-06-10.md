# Cron Session Notes - 2026-06-10 05:00 (Medicine + Quantum)

## Key Finding: arxiv API `+` is parsed as OR, not AND
Query `quantum+machine+learning+medical+diagnosis` → `all:quantum OR all:machine OR all:learning OR all:medical OR all:diagnosis` = 982K results (essentially everything).

**Working pattern for targeted AND queries**:
- `quantum+AND+medical+AND+machine+learning` → better but API still groups OR before AND
- **Best**: category-scoped: `cat:quant-ph+AND+all:medical` or `cat:quant-ph+AND+all:diagnosis`

## Medicine+Quantum domain saturation: ~60% (less saturated than CS+Quantum at ~85%)

---

## Cron Session — 2026-06-10 16:00 (Medicine + Quantum, second run)

### kg_tool generate-embeddings failure (CONFIRMED AGAIN)
Same schema mismatch as before: `no such column: e.source`. The binary's SQL references columns not in the entities view. Direct sqlite3 on `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db` required for all kg operations.

### Papers found (3 total, 1 new)
- **2506.12195** (NEW): OSI Stack Redesign for Quantum Networks — created `quantum-network-osi-stack`
- **2505.06471**: Quantum medical image encoding — already covered by `quantum-image-encoding-fourier`
- **2004.02036**: Quantum Medical Imaging Algorithms — already covered by `quantum-medical-imaging`

### INDEX.md insertion via patch — confirmed reliable
Used `patch` tool to insert new section before unique marker `## 2026-06-10 - Anthropic Research (Cron Job)`. This avoids offset/limit pagination warnings and is more reliable than bulk string replacement on large INDEX.md files (2391+ lines). Git commit + push succeeded.

### kg.db dual-database reminder (confirmed again)
- `/Users/hiyenwong/.openclaw/workspace/kg.db` — 2215 entities, different schema
- `/Users/hiyenwong/.openclaw/workspace/scripts/kg.db` — 250 entities, cron workspace schema
- `~/.hermes/kg.db` → symlinks to `~/.openclaw/workspace/scripts/kg.db`
- kg_tool binary uses `/Users/hiyenwong/wiki/kg.db` → symlinks to `scripts/kg.db`