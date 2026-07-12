# Complete Network Blockade — 2026-06-16

## Symptoms (all sources failed simultaneously)

| Source | Error |
|--------|-------|
| arXiv API (urllib/ProxyHandler) | HTTP 502 Bad Gateway |
| arXiv API (curl + proxy) | Empty response (0 bytes) |
| arXiv API (curl direct) | Empty response (0 bytes) |
| arXiv RSS (curl + proxy) | Empty response (0 bytes) |
| browser_navigate (arxiv.org) | ERR_CONNECTION_CLOSED |
| GitHub (git push/pull) | LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to github.com:443 |

## Root Cause
All HTTPS connections failing — likely proxy outage, DNS resolution failure, or system-wide SSL configuration issue. This is distinct from individual source failures (rate limits, API errors, weekend blocks) where at least one source works.

## Recovery Workflow

1. **Detect**: When 3+ independent sources fail with connection/SSL errors within the same session, declare complete network blockade.
2. **Fallback to kg.db exclusively**:
   ```bash
   # Discover schema first (it drifts)
   sqlite3 kg.db "PRAGMA table_info(papers)"
   
   # Query papers without skills
   sqlite3 kg.db "SELECT arxiv_id, title, categories, abstract FROM papers WHERE skill_name IS NULL OR skill_name = '' ORDER BY published_date DESC LIMIT 20"
   
   # Score papers against topic keywords
   # Create skills from top novel papers
   ```
3. **Local-only operations**:
   - Create skills in `~/.hermes/skills/`
   - Copy to `ai_collection/collection/skills/`
   - Update INDEX.md locally
   - `git commit` locally (push will fail, defer)
4. **Defer push**: Record push as pending. Push manually when network recovers.

## Key Difference from Individual Fallbacks
The existing fallback chain (browser → API → RSS → web_search) assumes at least one source works. Complete blockade means ALL network-dependent sources are unreachable. kg.db is the *only* viable data source. This is rare but produces productive sessions — 120 papers without skills in kg.db yielded 4 new skills.

## Git Push Deferral Pattern
When `git push` fails with SSL_ERROR_SYSCALL:
- Commits succeed locally — do NOT lose them
- Do NOT retry indefinitely (3 attempts max)
- Record pending push in session report
- Push on next session when network is available
- Use `git pull` before push to handle potential remote divergence
