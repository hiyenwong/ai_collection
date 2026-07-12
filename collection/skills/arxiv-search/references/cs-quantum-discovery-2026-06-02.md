# CS + Quantum Discovery - 2026-06-02

## Browser Console Extraction Pattern (Works on Search Results Pages)

The standard browser_console JS pattern for arXiv search pages that actually works:

```javascript
var items = document.querySelectorAll('li.arxiv-result');
var out = [];
for (var i = 0; i < items.length; i++) {
  var item = items[i];
  var allP = item.querySelectorAll('p');
  var id = '';
  var title = '';
  var cats = '';
  var abs = '';
  var authors = '';
  // ID: first paragraph, links with /abs/ in href
  if (allP.length > 0) {
    var links = allP[0].querySelectorAll('a');
    for (var k = 0; k < links.length; k++) {
      var h = links[k].getAttribute('href');
      if (h && h.indexOf('/abs/') >= 0) {
        id = links[k].textContent.trim();
      }
    }
  }
  if (allP.length > 1) title = allP[1].textContent.trim();
  if (allP.length > 2) {
    var t2 = allP[2].textContent.trim();
    if (t2.indexOf('Authors:') >= 0) authors = t2.replace('Authors:', '').trim();
    else cats = t2;
  }
  if (allP.length > 3) {
    var t3 = allP[3].textContent.trim();
    if (t3.indexOf('Abstract:') >= 0) abs = t3.replace('Abstract:', '').trim().substring(0, 200);
  }
  out.push({id: id, title: title, authors: authors, abs: abs.substring(0, 150)});
}
JSON.stringify(out.slice(0, 15));
```

**Why this works**: On arXiv search result pages, the HTML structure puts the arXiv ID link in `<p>` index 0, the title in `<p>` index 1, authors in index 2, and abstract in index 3. The old pattern that queries `.list-title` doesn't work because search pages have a different structure than category listing pages.

## Duplicate Check Speed Optimization

Instead of grepping across all `~/.hermes/skills/` directories (which times out with 500+ skills), target the ai_collection directory first since most cron-created skills live there:

```bash
# Fast check (usually sufficient)
grep -rl "2605.XXXXX" ~/.hermes/skills/ai_collection/ 2>/dev/null | grep SKILL

# Full check (fallback)
grep -rl "2605.XXXXX" ~/.hermes/skills/ 2>/dev/null | grep SKILL
```

## INDEX.md Patch Pattern (Safe)

Never overwrite INDEX.md entirely — use patch with unique context:

```bash
# Find a unique anchor near the top of the file
# Then patch that anchor with prepended new entry
```

The safest anchor is the `> Auto-generated index` line which only appears once.

## Paper Coverage Rate (2026-06-02)

Today's search: 15 papers found
- Already had skills: 14 (93% coverage)
- New skills created: 1 (mole-lambda-coupled-cluster-response)

This demonstrates the library has accumulated substantial coverage. Future cron runs should prioritize **synthesis** of existing papers over **discovery** of new ones when coverage exceeds ~80%.
