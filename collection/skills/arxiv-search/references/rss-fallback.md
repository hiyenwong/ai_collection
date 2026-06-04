# arXiv RSS Fallback

When the arXiv REST API (`export.arxiv.org/api/query`) returns HTTP 429 (Too Many Requests), use RSS feeds as a reliable fallback. RSS feeds are much more generous with rate limits and return large batches instantly.

## RSS Feed URLs

```
https://rss.arxiv.org/rss/<category>
https://rss.arxiv.org/rss/<cat1>+<cat2>+<cat3>
```

### Common Categories

| Feed | Categories |
|------|-----------|
| quant-ph | `https://rss.arxiv.org/rss/quant-ph` |
| cs.AI | `https://rss.arxiv.org/rss/cs.AI` |
| cs.LG | `https://rss.arxiv.org/rss/cs.LG` |
| cs.CL | `https://rss.arxiv.org/rss/cs.CL` |
| cs.SE | `https://rss.arxiv.org/rss/cs.SE` |
| Combined | `https://rss.arxiv.org/rss/cs.AI+cs.LG+cs.CL` |

## Python Implementation

```python
import feedparser
import urllib.request
import ssl

ctx = ssl.create_default_context()
url = 'https://rss.arxiv.org/rss/quant-ph+cs.LG'
req = urllib.request.Request(url, headers={'User-Agent': 'ResearchBot/1.0'})
with urllib.request.urlopen(req, timeout=30, context=ctx) as response:
    data = response.read().decode('utf-8')

feed = feedparser.parse(data)
print(f'{len(feed.entries)} entries')

for entry in feed.entries:
    title = entry.get('title', '').strip()
    abstract = entry.get('summary', '').strip()
    link = entry.get('link', '')
    published = entry.get('published', '')
    # Extract arXiv ID: https://arxiv.org/abs/2605.16467v1 → 2605.16467
    arxiv_id = link.split('/')[-1].split('v')[0] if link else 'unknown'
```

## Key Notes

- RSS feeds return ~100-300 entries per category per day
- `entry.summary` contains the full abstract prefixed with "arXiv:XXXX.XXXXXv1 Announce Type: new/replacement/cross Abstract: ..."
- `entry.published` format: `"Tue, 19 May 2026 00:00:00 -0400"`
- The `feedparser` package is typically pre-installed; if not: `pip install feedparser`
- Multiple categories can be combined with `+` in the URL
- RSS is ideal for bulk fetching; REST API is better for targeted keyword search
