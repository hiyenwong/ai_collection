# Research API Fallback Reference — Session Learnings (2026-05-17)

## Semantic Scholar API Fallback Pattern

When arXiv API rate-limits (HTTP 429), Semantic Scholar works reliably:

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=quantum+information+science&fields=title,authors,year,abstract,externalIds&limit=3&year=2025,2026" --max-time 15 > /tmp/sem.json
```

**Parse with Python (write to file first, NOT pipe):**
```python
import json
with open('/tmp/sem.json') as f:
    data = json.load(f)
for paper in data.get('data', []):
    arxiv_id = paper.get('externalIds', {}).get('ArXiv', 'N/A')
    title = paper.get('title', '')
    abstract = paper.get('abstract', '')
    tldr = paper.get('tldr', {}).get('text', '')
```

**Key fields:**
- `externalIds.ArXiv` — arXiv ID for cross-reference
- `tldr.text` — AI-generated summary
- `abstract` — full abstract

**Security:** Never use `curl | python3` — triggers HIGH security scan. Write to file first.

## kg_tool Import Command

```bash
cd /Users/hiyenwong/wiki
/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool import-paper \
  --title "Paper Title" \
  --url "https://arxiv.org/abs/xxxx.xxxxx" \
  --authors "Author1, Author2" \
  --abstract "Full abstract text"
```

## INDEX.md Safe Editing

- **Never overwrite** after partial read (offset/limit pagination)
- Always use patch mode to prepend/append entries
- System warns: "was last read with offset/limit pagination (partial view)"
- If full read needed, use multiple reads with offset parameter

## Proxy for urllib in Python

Environment variables alone don't work in execute_code sandbox:
```python
proxy = urllib.request.ProxyHandler({
    'http': 'http://127.0.0.1:7890', 
    'https': 'http://127.0.0.1:7890'
})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
```
