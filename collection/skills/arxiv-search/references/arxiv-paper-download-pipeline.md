# arXiv Paper Download & Extraction Pipeline

Working pipeline for downloading and extracting arXiv paper content, verified 2026-05-16.

## Download PDF

```python
import httpx

url = "https://arxiv.org/pdf/2605.14916v1.pdf"
r = httpx.get(url, timeout=60, proxy="http://127.0.0.1:7890", follow_redirects=True)
r.raise_for_status()
with open("/tmp/paper.pdf", "wb") as f:
    f.write(r.content)
```

**Pitfall**: Use `proxy="http://..."` (string), NOT `proxies={...}` (dict). The latter raises `TypeError`.

## Extract Text (fallback chain)

### Option 1: pdftotext (most reliable on macOS)
```bash
pdftotext /tmp/paper.pdf /tmp/paper.txt
```

### Option 2: pymupdf (if pdftotext unavailable)
```python
import fitz
doc = fitz.open("/tmp/paper.pdf")
text = "".join(page.get_text() for page in doc)
doc.close()
```

### Option 3: marker-pdf (best quality, but heavy dependency)
```bash
marker_single /tmp/paper.pdf /tmp/ --batch_multiplier 1
```

**Reality**: `marker_single` is often not installed. `pdftotext` is pre-installed on macOS and works reliably. `pymupdf` requires `pip install pymupdf`.

## What DOESN'T work

- `web_extract` blocks arxiv.org URLs ("private/internal network")
- `marker_single` — binary not available in standard environments

## Key lesson

The skill's example code in SKILL.md uses the old `proxies` kwarg. Always use `proxy` (singular string) with httpx. The skill needs updating — see Pitfalls section in SKILL.md.
