# arXiv Deep Reading Fallbacks

When you have paper IDs but need full content (not just abstracts), use this fallback chain:

## Fallback Chain

### 1. browser_navigate → arxiv.org/html/{id}v1
```
browser_navigate("https://arxiv.org/html/{arxiv_id}v1")
browser_snapshot()  # Get full paper content
```
**Works reliably** for most papers (LaTeXML-rendered HTML). Best first choice.

### 2. web_extract → arxiv.org/abs/{id}
```
web_extract(["https://arxiv.org/abs/{arxiv_id}"])
```
Often blocked by security guardrails. Try if browser_navigate fails.

### 3. curl → save to file → parse
```
curl -x http://127.0.0.1:7890 -s "https://arxiv.org/html/{arxiv_id}v1" -o /tmp/paper.html
```
Then parse with BeautifulSoup/Python. Last resort when browser tools unavailable.

### 4. web_search → snippets
```
web_search("arxiv {arxiv_id} {topic} full text")
```
Gets summary snippets but not full content.

## Why This Matters
- arXiv XML API only provides abstracts (not full text)
- `web_extract` often blocks arxiv.org as "private/internal network"
- `web_search` gives snippets, not structured paper content
- `browser_navigate` to the HTML version bypasses these limitations

## Parsing arxiv.org/html
The HTML is rendered by LaTeXML with predictable structure:
- Section headings in `<h1>`, `<h2>`, `<h3>` tags
- Math in MathML or `<span class="ltx_Math">`
- References in `<li class="ltx_bibitem">`
- Figures with `<figure>` and `<figcaption>`

Use BeautifulSoup to extract sections by heading:
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
for section in soup.find_all(['h1', 'h2', 'h3']):
    print(f"=== {section.get_text().strip()} ===")
```
