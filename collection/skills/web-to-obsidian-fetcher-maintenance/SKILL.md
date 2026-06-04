---
name: web-to-obsidian-fetcher-maintenance
description: "Maintaining automated scripts that fetch web content and save to Obsidian notes. Covers deduplication strategies, Cloudflare-protected sites, index management, and common cron job pitfalls. Use when: (1) building or debugging automated content fetchers, (2) Obsidian note accumulation has duplicates, (3) web scraping fails due to Cloudflare/bot protection, (4) maintaining cron jobs that save content to Obsidian."
---

# Web-to-Obsidian Fetcher Maintenance

Maintaining automated scripts that scrape web content and save as Obsidian notes. Covers the recurring bugs and patterns seen in daily cron fetchers.

## When to Use This Skill

**Trigger situations**:
- Building a script that fetches articles/blog posts and saves to Obsidian
- Daily cron job creating duplicate files every run
- Web scraping blocked by Cloudflare or other bot protection
- Obsidian index/INDEX.md not accumulating history
- Need to clean up accumulated duplicate notes

## Critical Bugs to Prevent

### Bug 1: Date-Prefix Filename Duplication

**Symptom**: Same content saved daily with new filenames like `2026-05-02-GPT-4.md`, `2026-05-03-GPT-4.md`, etc.

**Root cause**: Using `date + title` as filename instead of a stable identifier.

**Fix**: Use the content's stable slug/ID as filename:
```python
# WRONG: creates duplicates every day
filename = f"{today}-{title}.md"

# RIGHT: slug-based, naturally deduplicated
filename = f"{article_slug}.md"
if os.path.exists(filepath):
    print(f"⏭️  Skipped (exists): {filename}")
    continue
```

**Cleanup command** for existing duplicates:
```bash
cd "path/to/Obsidian/dir"
# List duplicates (date-prefixed files)
ls -1 *.md | grep -E "^[0-9]{4}-[0-9]{2}-[0-9]{2}-"
# Remove after verification
ls -1 *.md | grep -E "^[0-9]{4}-[0-9]{2}-[0-9]{2}-" | while read f; do rm "$f"; done
```

### Bug 2: Index Overwriting History

**Symptom**: INDEX.md only shows today's batch, loses all previous entries.

**Root cause**: Rewriting the entire index from the current batch instead of scanning actual files.

**Fix**: Scan the directory for all existing notes and rebuild from filesystem:
```python
def build_index_from_files(obsidian_dir):
    notes = []
    for f in os.listdir(obsidian_dir):
        if f.endswith('.md') and f != 'INDEX.md':
            # Read frontmatter for title, category, url
            filepath = os.path.join(obsidian_dir, f)
            with open(filepath, 'r') as fh:
                content = fh.read(500)
                title = extract_frontmatter_field(content, 'title')
                category = extract_frontmatter_field(content, 'category')
                url = extract_frontmatter_field(content, 'url')
                notes.append({'filename': f, 'title': title, ...})
    # Group by category, sort, write
```

### Bug 3: Content Extraction Failure on Protected Sites

**Symptom**: All saved notes contain "内容获取失败" or empty placeholders.

**Root cause**: Target site uses Cloudflare protection, client-side rendering (Next.js/React), or requires JavaScript execution.

**Detection**: Check response for:
```python
if 'cloudflare' in response.text.lower() or response.status_code == 403:
    # Cloudflare blocked - content unavailable via simple requests
    return None
```

## Solutions (in order of effort):
1. **Firecrawl API**: If configured, use `firecrawl.dev` for JS-rendered pages
2. **Browser automation**: Use `browser_navigate` + `browser_snapshot` for small batches
3. **Archive services**: Try `web.archive.org/web/{url}` as fallback
4. **Metadata only**: Accept title + description + link as placeholder, fill content later manually

### Cloudflare-Only Fallback: Search Engine + Third-Party Aggregation

When the target site is fully Cloudflare-protected (even browser automation fails with "Just a moment..." / empty pages), and Firecrawl is unavailable:

1. **Use `web_search` to discover new content** — search engines often index pages behind Cloudflare. Use `site:target.com` queries to find new URLs.
2. **Extract content via `web_extract` on third-party sources** — news aggregators, AI news sites, and tech blogs often republish/summarize the same content and may be accessible.
3. **Create notes from search engine descriptions + third-party summaries** — even without full original content, you can capture: title, publication date, URL, description, and key points from aggregator summaries.
4. **Mark notes clearly as partial** — include a note that full content was unavailable due to Cloudflare blocking.

Example search patterns:
```
site:openai.com/index 2026 research
site:openai.com/research new publications
"openai.com/index" "paper title keywords"
```

**This approach is particularly valuable for cron jobs**: even when the script's known article list is stale and the target site is blocked, web search can still surface new articles that the script missed.

### Ultimate Fallback: arXiv Browser Search (when web_search is also broken)

When `web_search` itself fails (e.g., `'NoneType' object has no attribute 'status_code'`), fall back to arXiv browser search:

1. **Navigate**: `browser_navigate("https://arxiv.org/search/?query=OpenAI+GPT-5&searchtype=all&order=-submitted_date")`
2. **Extract via `browser_console` JavaScript**:
   ```javascript
   // Extract paper titles, authors, dates from arXiv results
   const items = document.querySelectorAll('.arxiv-result');
   // Extract title, authors, date from each
   ```
3. **Navigate to individual papers**: `browser_navigate("https://arxiv.org/abs/2601.03267")`
4. **Extract abstract**: `document.querySelector('blockquote.abstract').textContent.trim()`

This has been proven to work when EVERYTHING else fails simultaneously: target site blocked by Cloudflare, web_search broken, web_extract blocking URLs.

**Headers that help** (may bypass soft protection):
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}
response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
```

## Recommended Note Structure

```markdown
---
title: "Article Title"
source: "Source Name"
url: "https://..."
date: "2026-05-02"          # When fetched
first_fetched: "2026-05-02" # Original fetch date (for updates)
category: "category-name"
tags: [tag1, tag2]
---

# Article Title

> **原文链接**: [url](url)
> **获取日期**: 2026-05-02
> **分类**: category-name
> **来源**: Source Name

---

## 内容摘要

[Description or abstract]

---

## 原文内容

[Full content if available, or link to original]

---

## 中文翻译与解读

[待补充]

### 核心创新点
- 

### 技术细节
- 

### 应用场景
- 

### 个人思考


---

## 相关链接

- [Source homepage](https://...)
```

## Recommended Index Structure

```markdown
# {Source} Research 索引

> 自动更新于: {date}

## 统计
- 总文章数: {total}
- 今日新增: {new}
- 跳过（已存在）: {skipped}

## 全部文章

### {category} ({count})
- [[slug|Title]] — [url](url)
- ...

---

## 分类标签
- #tag1
- #tag2
```

## Maintenance Checklist

When taking over or debugging an existing fetcher:

- [ ] **Filename strategy**: Uses stable slug, not date prefix
- [ ] **Dedup check**: `os.path.exists()` before writing
- [ ] **Index rebuild**: Scans filesystem, not just current batch
- [ ] **Cloudflare handling**: Detects and reports blockage
- [ ] **Stats reporting**: Reports new vs skipped counts
- [ ] **Frontmatter**: Includes `first_fetched` for tracking
- [ ] **Cleanup**: No accumulated duplicates from previous bugs
- [ ] **Content discovery**: Script discovers content dynamically (RSS, sitemap, web scraping) rather than relying on a static known-article list. Static lists become stale quickly and miss new publications. If using a static list, ensure it is auto-updated or supplemented with web search fallback. **Important**: the pre-run script's known list should be compared against actual filesystem contents — discrepancies (files on disk not in the list) cause false "skipped" counts and missed new articles.

## Activation Keywords

- web to obsidian fetcher
- automated content scraping
- cron job duplicates
- Cloudflare scraping blocked
- Obsidian index management
- article fetcher maintenance
- 自动获取文章到Obsidian
- 爬虫去重

## Reference Files

- `references/arxiv-browser-extraction.md` — JavaScript snippets for extracting paper data from arXiv via browser automation (tested working when web_search and web_extract both fail)
