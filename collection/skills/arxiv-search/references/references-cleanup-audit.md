# arXiv-search References Cleanup Audit (2026-05-26)

**Problem:** 40+ reference files accumulated across cron sessions. Heavy overlap — many files cover identical rate-limiting/fallback patterns already captured in SKILL.md's "Consolidated Fallback Chain" section.

## Consolidation Groups (keep ONE per group, delete the rest)

### Rate-limiting → keep `arxiv-rate-limiting.md`
Delete: `arxiv-rate-limits.md`, `arxiv-rate-limit-fallback.md`, `rate-limiting.md`, `rate-limit-recovery.md`, `rate-limiting-fallback.md`, `arxiv-rate-limit-recovery.md`, `arxiv-api-rate-limits.md`

### Fallback strategies → keep `arxiv-fallback-strategies.md`
Delete: `arxiv-fallback.md`, `arxiv-fallback-patterns.md`, `arxiv-fallback-strategies.md`, `arxiv-api-fallback.md`, `arxiv-api-fallbacks.md`, `rate-limit-fallback.md`

### API reliability → keep `verified-search-patterns.md`
Delete: `arxiv-api-reliability.md`, `arxiv-api-working-pattern.md`, `arxiv-code-pattern.md`, `working-arxiv-search-pattern.md`, `reliable-arxiv-search-pattern.md`

### Browser fallback → keep `browser-console-listing-extraction.md`
Delete: `browser-fallback.md`, `html-fallback.md`, `listing-page-fallback.md`, `arxiv-html-listing-fallback.md`

### RSS feeds → keep `rss-fallback-and-patterns.md`
Delete: `rss-fallback.md`, `rss-verified-pattern.md`

## Principle
The SKILL.md body's "Consolidated Fallback Chain" is the authoritative source. Reference files should ONLY contain details NOT in the body (verified paper lists, session-specific notes, RSS feed configs, multi-topic scanning configs).
