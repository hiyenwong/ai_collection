# Browser Console JavaScript for arXiv Listing Extraction

Verified patterns for extracting paper metadata from arXiv listing pages via `browser_console(expression=...)`.

## Pattern 1: Extract IDs + Titles from `<dt>/<dd>` listing

Works on `https://arxiv.org/list/{category}/recent` pages.

```javascript
Array.from(document.querySelectorAll('div#content dl dt')).map(dt => {
  const links = dt.querySelectorAll('a');
  const arxivLink = Array.from(links).find(a => a.href.includes('arxiv.org/abs'));
  const id = arxivLink ? arxivLink.textContent.replace('arXiv:', '').trim() : '';
  const dd = dt.nextElementSibling;
  const title = dd ? dd.childNodes[0].textContent.trim() : '';
  return { id, title };
}).filter(p => p.id).slice(0, 20)
```

**Verified 2026-05-22** — returns clean `{id, title}` pairs from quant-ph listing.

## Pattern 2: IDs + Titles + Authors

```javascript
Array.from(document.querySelectorAll('div#content dl dt')).map(dt => {
  const idEl = dt.querySelector('a[href*="arXiv:"]');
  const id = idEl ? idEl.textContent.trim() : '';
  const dd = dt.nextElementSibling;
  const title = dd ? dd.childNodes[0].textContent.trim() : '';
  const authors = dd ? Array.from(dd.querySelectorAll('a')).map(a => a.textContent).join(', ') : '';
  return { id, title, authors };
}).slice(0, 20)
```

## Pattern 3: Quick ID regex scan

```javascript
Array.from(document.querySelectorAll('a[href*="arxiv.org/abs/"]'))
  .map(a => a.href.match(/abs\/([0-9.]+)/))
  .filter(Boolean)
  .map(m => m[1])
```

## Usage
```
browser_navigate("https://arxiv.org/list/quant-ph/recent")
browser_console(expression="<javascript>")
```

## Notes
- Use `var` not `let`/`const` across multiple console expressions in same session
- `<dt>/<dd>` structure consistent across most arxiv listing pages; `<li.arxiv-result>` used on search pages
- First text node in `<dd>` is always the title; `<a>` elements are authors
- **Pitfall (2026-06-03 confirmed)**: Standard `<dt>/<dd>` selectors (Patterns 1-3) return **empty results** on `arxiv.org/list/quant-ph/recent` — the dt/dd DOM is present in HTML but not accessible via `querySelectorAll('dl dt')`. **Fallback**: parse `document.body.innerText` with regex for `arXiv:XXXX.XXXXX` pattern:
```javascript
var text = document.body.innerText;
var lines = text.split('\n');
var papers = [];
var currentId = '';
for (var i = 0; i < lines.length; i++) {
  var line = lines[i].trim();
  var idMatch = line.match(/arXiv:(\d{4}\.\d{5})/);
  if (idMatch) {
    currentId = idMatch[1];
  } else if (currentId && line.length > 15 && line.length < 300 && !line.includes('Comments:') && !line.includes('Subjects:') && !line.includes('Authors:')) {
    papers.push({id: currentId, title: line});
    currentId = '';
  }
}
JSON.stringify(papers.slice(0, 50));
```
This works universally on any arXiv page since it parses rendered text rather than relying on DOM structure.

## Pattern 4: Extract from arXiv Search UI page (`/search/` — 2026-05-24 verified)

The search results page uses `<li class="arxiv-result">`. The `.list-title` contains multiple links: the arXiv ID link comes first, then `[pdf, ps, other]` format links. Titles are in a subsequent `<p>` (not in `<dd>`). Authors are in a `<p>` starting with "Authors:".

```javascript
(() => {
  var out = [];
  var items = document.querySelectorAll('li.arxiv-result');
  items.forEach(function(li) {
    var id = '';
    var links = li.querySelectorAll('a');
    for (var i = 0; i < links.length; i++) {
      var t = links[i].textContent.trim();
      if (t.startsWith('arXiv:') && id === '') { id = t.replace('arXiv:', ''); break; }
    }
    var paras = li.querySelectorAll('p');
    var title = '';
    for (var j = 0; j < paras.length; j++) {
      var txt = paras[j].textContent.trim();
      if (txt && !txt.startsWith('Authors:') && !txt.startsWith('Submitted') && !txt.startsWith('Comments:')) { title = txt.substring(0, 250); break; }
    }
    var cats = '';
    var tags = li.querySelectorAll('.tags a');
    var tagList = [];
    for (var k = 0; k < tags.length; k++) tagList.push(tags[k].textContent.trim());
    cats = tagList.join(', ');
    if (id && title) out.push({ id: id, title: title, category: cats });
  });
  return JSON.stringify(out);
})()
```

**Pitfall**: `.list-title a:first-of-type` grabs `[pdf, ps, other]` instead of the arXiv ID on the search page. Fix: iterate all links and filter by `text.startsWith('arXiv:')`.
