# RSS Feed Weekend Skip Issue (2026-07-05)

## Problem

arXiv RSS feeds (`https://rss.arxiv.org/rss/...`) return empty results on weekends (Saturday + Sunday). The feed XML explicitly declares `<skipDays><day>Sunday</day><day>Saturday</day></skipDays>`. So `curl` succeeds with exit code 0 but the `<channel>` has zero `<item>` entries.

## Symptoms

```bash
curl -sL --proxy http://127.0.0.1:7890 "https://rss.arxiv.org/rss/q-bio.NC" -o /tmp/rss.xml
# Exit code: 0 — looks like success
# But channel has NO <item> elements
# Easy to misinterpret as "no new papers today"
```

## Detection

```bash
grep -c '<item>' /tmp/rss.xml   # Should be > 0 if there are papers
```

## Fix

**On weekends:** Skip RSS entirely, use arXiv API search endpoint instead:

```bash
curl -sL --proxy http://127.0.0.1:7890 \
  "https://export.arxiv.org/api/query?search_query=cat:q-bio.NC+OR+cat:cs.NE&sortBy=submittedDate&sortOrder=descending&max_results=30" \
  -o /tmp/arxiv_search.xml
```

## General Rule

Always add a weekend check before relying on RSS — `datetime.now().weekday() >= 5` means use API, not RSS.
