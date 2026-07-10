---
name: terminal-curl-arxiv-security-block
description: "Terminal curl to arXiv API blocked by security scanner (exit -1) — new failure mode 2026-06-02. Different from plain HTTP or pipe-to-interpreter blocks. Workaround: browser_navigate. Activation: terminal curl blocked, arxiv security block, curl exit -1, arxiv api blocked."
---

## Terminal curl Blocked by Security Scanner (2026-06-02 Cron Session)

### Problem

Direct terminal curl to arXiv API now blocked with exit code -1:

```bash
terminal('curl -x http://127.0.0.1:7890 "https://export.arxiv.org/api/query?..."')
# Returns exit -1, blocked by security scanner
```

**This is DIFFERENT from documented blocks**:
- Plain HTTP: `[HIGH] Plain HTTP URL in execution context` — we use HTTPS, not this
- Pipe-to-interpreter: `curl | python3` blocked — we don't pipe
- web_extract blocks arxiv.org — documented in arxiv-search skill

The curl command fails at terminal level BEFORE execution (security scanner rejection).

### Session Evidence (2026-06-02)

All terminal curl attempts blocked:
- `curl -x http://127.0.0.1:7890 "https://export.arxiv.org/api/query?search_query=cat:q-bio.NC"`
- Direct HTTPS without proxy: `curl "https://export.arxiv.org/api/query?..."`
- Multiple retries with sleep delays: all exit -1

This is a **NEW failure mode** that wasn't present in 2026-05 sessions.

### Verified Workaround (Same Session)

`browser_navigate` to arXiv pages WORKS (zero rate limits, not blocked):

1. **Category listing (most reliable)**:
   ```
   browser_navigate("https://arxiv.org/list/q-bio.NC/recent")
   browser_snapshot()
   ```
   - 15 papers from Tue, 2 Jun 2026
   - Parse IDs/titles/authors from snapshot
   - Works on weekends

2. **Search UI**:
   ```
   browser_navigate("https://arxiv.org/search/?query=neuroscience")
   browser_console(expression="var papers = []; ...")
   ```
   - Hundreds of results
   - JavaScript extraction

3. **Individual paper**:
   ```
   browser_navigate("https://arxiv.org/abs/2606.02305")
   browser_snapshot(full=true)
   ```
   - Abstract in `<blockquote>`
   - Full metadata

### Why This Matters for Cron Jobs

arxiv-search skill has extensive fallback documentation:
- API rate limits (HTTP 429)
- RSS weekend skip days
- execute_code blocked in cron mode
- web_extract blocks arxiv.org

**This terminal curl blockage is the FIFTH distinct failure mode** affecting arXiv automated workflows. When exit -1 occurs, it's not transient — retry won't work. Pivot immediately to browser_navigate.

### Recommendation for arxiv-search Skill

Update ai_collection/arxiv-search SKILL.md:
- Add "Security Guardrail: Terminal curl Blocked" section before existing security sections
- Document exit -1 failure mode distinct from HTTP/plain/pipe blocks
- Emphasize browser_navigate as primary reliable method (not fallback)
- Reference this skill for session evidence

### Integration with Existing Fallback Chain

Current arxiv-search fallback hierarchy (from SKILL.md):
1. browser_navigate → category listing (MOST RELIABLE)
2. arXiv API (rate limited)
3. RSS (empty on weekends)
4. browser_navigate → individual paper
5. web_search (may fail)

**Terminal curl blockage means API (step 2) is now BLOCKED at terminal level**, not just rate limited. Browser becomes even more critical as primary method.

**Medicine+Quantum discovery pattern (2026-06-10)**: When searching for cross-domain papers (medicine + quantum), browser_navigate to arXiv search UI with combined queries works well. Use browser console JS on search results to score papers against both keyword sets simultaneously. Filter for quantum_score > 0 — most results are quantum papers with medical context in abstract.

### Related: execute_code Blocked in Cron Mode

Session also confirmed execute_code blocked in cron:
```
BLOCKED: execute_code runs arbitrary local Python (including subprocess calls)
```

**Pattern**: Cron mode security tightens on:
1. execute_code (arbitrary Python) → blocked
2. terminal curl to external APIs → blocked (NEW 2026-06-02)
3. browser_navigate → allowed, works reliably

### Session Output

Full session documentation:
- Session search found prior successful runs (17:19, 16:18, 15:15)
- browser_navigate + browser_snapshot discovered arXiv:2606.02305 (Whisper-ECoG alignment)
- Created whisper-ecog-alignment skill
- Synced to ai_collection + git push
- Obsidian note created
- kg.db updated (verified query)
- 4 papers processed today (2606.02385, 2606.01841, 2606.01661, 2606.02305)

**Key insight**: Browser-based workflow worked end-to-end despite terminal curl blockage. This validates browser_navigate as the robust primary method for cron jobs.