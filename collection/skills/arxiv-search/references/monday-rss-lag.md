# Monday Morning RSS Lag (2026-06-01)

## Discovery

On Monday June 1, 2026 at ~09:00 (morning cron run), RSS feed `https://rss.arxiv.org/rss/q-bio.NC+cs.NE+cs.AI+cs.LG` showed **Sunday May 31 data** despite being Monday.

**Evidence**:
- RSS `<pubDate>` showed Sunday's timestamp
- RSS feed returned neuroscience papers with May 31 dates
- Browser fallback to `arxiv.org/list/q-bio.NC/recent` revealed **38 new entries** (May 29 and May 27 papers)
- INDEX.md grep confirmed 5 papers from May 29 already processed on May 31
- 2 papers from May 27 (2605.26551, 2605.26973) were NEW — not in INDEX.md

## Pattern

**RSS feeds lag by ~24 hours on Monday mornings**, showing previous day's data. This is NOT the weekend skip (`<skipDays>` for Sat+Sun), but a **Monday morning stale feed** phenomenon.

**Detection**: When RSS date shows yesterday's date on Monday morning, RSS is stale → pivot immediately.

## Solution

**Browser fallback chain for Monday mornings**:

1. **Navigate to category listing**:
   ```
   browser_navigate("https://arxiv.org/list/q-bio.NC/recent")
   ```
   Returns actual Monday submissions + recent backlog.

2. **Parse paper IDs from snapshot**:
   Snapshot format: `arXiv:2605.XXXXX [pdf, other]` — extract ID from first line.

3. **Check INDEX.md for duplicates**:
   ```bash
   grep "2605.XXXXX" ~/ai_github/ai_collection/INDEX.md
   ```
   If found → already processed, skip.

4. **Navigate to unprocessed papers**:
   ```
   browser_navigate("https://arxiv.org/abs/2605.XXXXX")
   ```
   Abstract in `<blockquote class="abstract mathjax">`.

5. **Process new papers**: skill creation, ai_collection sync, Obsidian, kg.db.

## Why This Happens

RSS feed generation likely runs at a fixed time (e.g., midnight UTC), producing the next day's feed. On Monday morning before the feed update, RSS still shows Sunday's snapshot. The arXiv **web server** serves listing pages 24/7 with real-time submissions.

## Do NOT Retry RSS

**Monday morning stale RSS is NOT rate limiting** — it's stale data. Retrying RSS won't help. Pivot to browser.

## Related

- weekend-arxiv-discovery — weekend skip pattern
- neuroscience-cron-workflow — complete workflow