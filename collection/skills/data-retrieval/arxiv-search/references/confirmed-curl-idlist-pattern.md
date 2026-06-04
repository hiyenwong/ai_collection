# Confirmed: curl -x Proxy for arXiv Single-Paper Fetch (2026-05-29)

## Verified Pattern

When Python urllib, direct HTTPS, RSS feeds, and browser all fail with SSL_ERROR_SYSCALL through the HTTP proxy (`http://127.0.0.1:7890`), **curl with HTTP proxy** can still work for targeted single-paper fetches:

```bash
curl -s --proxy http://127.0.0.1:7890 --max-time 15 "https://export.arxiv.org/api/query?id_list=2605.XXXXX" -H "User-Agent: Mozilla/5.0"
```

### What Works
- `curl -x http://127.0.0.1:7890` to `https://export.arxiv.org/api/query?id_list=XXXXX` ✅
- HTTP CONNECT tunnel established, TLS handshake succeeds for arXiv API
- Returns full abstract, title, categories, published date in Atom XML

### What Fails (Same Session, Same Proxy)
- Python `urllib.request` + SSL bypass + direct HTTPS → `SSL_ERROR_SYSCALL` ❌
- `curl` to `https://rss.arxiv.org/rss/quant-ph` → `SSL_ERROR_SYSCALL` ❌
- `curl` to `https://httpbin.org/ip` → connection refused ❌
- `browser_navigate` to any arxiv.org URL → `ERR_CONNECTION_CLOSED` ❌
- `urllib.request` with proxy handler → `SSL: UNEXPECTED_EOF_WHILE_READING` ❌

### Why It Works
curl uses a different TLS library (LibreSSL on macOS) and handles the CONNECT tunnel differently than Python's ssl module. The proxy's HTTP-to-HTTPS tunneling works for curl's TLS stack but fails for Python's.

### Usage
Best for fetching **1-3 specific papers** when broader discovery (RSS, category listing) is blocked. Parse with grep or xmllint:

```bash
curl -s --proxy http://127.0.0.1:7890 --max-time 15 "https://export.arxiv.org/api/query?id_list=2605.28690" \
  -H "User-Agent: Mozilla/5.0" | grep -E "<summary>|<title>|<published>" | head -5
```

### Confirmed 2026-05-29
Successfully fetched full abstract for arXiv:2605.28690 using this pattern when all other methods failed.
