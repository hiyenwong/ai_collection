# execute_code Blocked in Cron Mode

## Symptom
```
BLOCKED: execute_code runs arbitrary local Python (including subprocess calls that bypass shell-string approval checks). Cron jobs run without a user present to approve it.
```

## Confirmed: 2026-06-03
- Cron job attempted `execute_code` for sqlite3 queries on kg.db
- Blocked at agent level — no way to bypass
- This is different from the `execute_code` sandbox restrictions (limited tool imports) — this is a complete block

## What Works Instead
| Action | Terminal | execute_code |
|--------|----------|--------------|
| sqlite3 queries | ✅ | ❌ BLOCKED |
| curl to RSS | ✅ | ❌ BLOCKED |
| kg_tool commands | ✅ | ❌ BLOCKED |
| git operations | ✅ | ❌ BLOCKED |
| write_file/create skill | via patch | ❌ BLOCKED |
| skill_manage | ✅ (top-level) | ❌ BLOCKED |

## Updated Cron Fallback Hierarchy
1. RSS Feed (`curl -s -A "Mozilla/5.0" --max-time 15 "https://rss.arxiv.org/rss/quant-ph+q-bio.QM"`)
2. KG.db (`sqlite3 kg.db "SELECT ..."`)
3. Workspace JSON caches (`ls workspace/*.json`)
4. kg_tool via terminal (`./scripts/kg_tool/target/release/kg_tool pagerank --limit 10`)
5. Skill creation via `write_file` to `~/.hermes/skills/{name}/SKILL.md` or `skill_manage` (top-level)

## Impact on research-api-fallback-strategy Skill
The skill's Tier 1.5 fallback (execute_code with httpx/urllib) is now **obsolete for cron jobs**. The RSS feed via curl + KG.db via sqlite3 via terminal is the replacement path.
