# arXiv API Query Format — Working vs Broken Patterns

## Broken (HTTP 400)

```
search_query=all:"quantum error correction"     # quoted phrase → 400
search_query=cat:quant-ph+AND+all:"cryptography" # boolean + quoted → 400
search_query=all:"quantum+entanglement+entropy"  # quoted phrase → 400
```

## Working

```
search_query=all:quantum error correction        # simple keywords, space-separated → OK
search_query=all:quantum entanglement entropy    # same → OK
search_query=all:quantum number theory           # same → OK
search_query=all:quantum statistics              # same → OK
search_query=all:number theory quantum           # same → OK
```

## Rule

The arXiv API `all:` field accepts **simple space-separated keyword strings only**.
It does NOT support:
- Quoted phrases (`"..."`)
- Boolean operators (`AND`, `OR`, `NOT`, `+AND+`, `+OR+`)
- Category filters combined with quoted phrases (`cat:quant-ph AND all:"..."`)

## Workaround for Advanced Queries

1. **Multiple simple queries**: Run separate queries for each keyword group, merge client-side
2. **Category listing pages**: `browser_navigate` to `https://arxiv.org/list/quant-ph/recent`
3. **Search page via browser**: `browser_navigate` to `https://arxiv.org/search/?searchtype=all&query=KEYWORDS`

## Verified Working Query List (2026-06-19)

| Query | Result |
|-------|--------|
| `all:quantum error correction` | HTTP 400 ❌ |
| `all:quantum entanglement entropy` | HTTP 400 ❌ |
| `all:quantum random matrix` | HTTP 400 ❌ |
| `all:quantum fourier` | No results (empty) |
| `all:quantum hamiltonian` | No results (empty) |
| `all:quantum cryptography` | HTTP 400 ❌ |
| `all:quantum information theory` | HTTP 400 ❌ |
| `all:number theory quantum` | No results (empty) |
| `all:quantum statistics` | Returned papers ✓ |
| `all:quantum probability` | Returned papers ✓ |

Note: Queries that returned papers vs. empty results may depend on arXiv's current index.
The 400 errors are consistent and query-format related.

## Correct Python Pattern

```python
import urllib.parse

keywords = "quantum algorithm benchmarking noise"
query = f"all:{keywords}"  # No quotes, no boolean ops
url = f"http://export.arxiv.org/api/query?search_query={urllib.parse.quote(query)}&max_results=3"
```
