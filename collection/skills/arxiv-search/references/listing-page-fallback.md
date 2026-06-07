# arXiv Listing Page Scraping (API Fallback)

When the arXiv API returns `Rate exceeded.` (which it does on most requests), use category listing HTML pages instead.

## Fetch Listing Page

```bash
# Save to file — NEVER pipe curl directly to python (security guardrail blocks it)
curl -s -L --max-time 30 -o /tmp/arxiv_listing.html "https://arxiv.org/list/{category}/recent"
# Examples: q-bio.NC, cs.NE, cs.LG, cs.AI
```

## Extract Paper IDs and Titles

```python
import re

with open('/tmp/arxiv_listing.html', 'r') as f:
    html = f.read()

sections = html.split('</dt>')
papers = []
for section in sections[1:]:
    id_m = re.search(r'arXiv:(\d+\.\d+)', section)
    if not id_m:
        continue
    arxiv_id = id_m.group(1)
    
    title_m = re.search(r"<div class='list-title[^']*'>.*?</span>\s*(.*?)\s*</div>", section, re.DOTALL)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else 'Unknown'
    
    authors_m = re.search(r"<div class='list-authors'[^>]*>(.*?)</div>", section, re.DOTALL)
    authors = ', '.join(re.findall(r'>([^<]+)<', authors_m.group(1))) if authors_m else ''
    
    papers.append({'id': arxiv_id, 'title': title, 'authors': authors})
```

## Fetch Abstracts via Individual Abs Pages

Each paper's abstract page contains a `citation_abstract` meta tag:

```bash
curl -s -L --max-time 15 "https://arxiv.org/abs/{arxiv_id}" \
  | grep 'citation_abstract' \
  | sed 's/.*content="//;s/"//'
```

For full metadata (title, authors, abstract together):

```bash
curl -s -L --max-time 15 "https://arxiv.org/abs/{arxiv_id}" \
  | grep -E 'citation_title|citation_abstract|citation_author|citation_date'
```

## Parse HTML Paper Pages for Full Content

For papers with HTML versions (`https://arxiv.org/html/{id}v1`):

```python
import re

with open('/tmp/paper_html.html', 'r') as f:
    html = f.read()

# Extract paragraphs
paras = re.findall(r'<p class="ltx_p">(.*?)</p>', html, re.DOTALL)

# Extract headings
headings = re.findall(r'<h[2-6] class="ltx_[^"]*">(.*?)</h[2-6]>', html, re.DOTALL)

def clean(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = s.replace('&amp;', '&').replace('&#39;', "'")
    return re.sub(r'\s+', ' ', s).strip()
```

## ⚠️ Pitfall: Listing Page Tabs Are Client-Side Only (2026-05-23)

The "New submissions" / "Cross-lists" / "Replacements" page tabs (↕ links at the top of the listing) are **CSS/JS visibility toggles**, not server-side navigation. `browser_click` on these tabs does NOT load new content — `browser_snapshot` returns the same DOM regardless of which tab is "active."

All three sections are pre-loaded in the initial HTML response. To see all entries:

- **Scroll down**: `browser_scroll(direction="down")` reveals all sections
- **Use `browser_vision`**: Captures the full rendered page including all three sections in one pass
- **Check via console**: `document.querySelectorAll('dl > dt').length` returns the total count across all sections

**Symptoms**: Clicking a tab returns `"clicked": "@e31"` but snapshot content never changes. The tool warns `idempotent_no_progress_warning`. Just scroll instead.

## Key Points

- **Always save curl output to a file first** — the security guardrail blocks `curl | python3`
- Listing pages have no rate limit (unlike the API)
- The `citation_*` meta tags on abs pages are the most reliable way to get structured metadata
- HTML paper pages (`/html/{id}v1`) contain full paper text if available
