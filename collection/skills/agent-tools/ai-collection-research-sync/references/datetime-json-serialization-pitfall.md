# datetime JSON Serialization Pitfall (arXiv RSS Parsing)

**Date**: 2026-05-29
**Context**: Session log reference for future cron job runs

## Problem

When parsing arXiv RSS feeds with `xmltodict.parse()`, the `<pubDate>` XML element is parsed as a Python `datetime` object. If you subsequently try to JSON-serialize the parsed results (e.g., caching intermediate paper data before skill creation), you encounter:

```python
TypeError: Object of type datetime is not JSON serializable
```

## Root Cause

`xmltodict` parses XML date/time elements into native Python datetime objects:

```python
import xmltodict

with open('/tmp/arxiv.xml', 'r') as f:
    rss_data = xmltodict.parse(f.read())

# rss_data['rss']['channel']['item'][0]['pubDate'] is datetime object
# type(rss_data['rss']['channel']['item'][0]['pubDate']) → datetime.datetime
```

When you attempt `json.dumps()` on this structure, datetime objects cannot be serialized.

## Solution 1: Explicit String Conversion

Convert datetime fields to strings during extraction:

```python
import xmltodict, json

with open('/tmp/arxiv.xml', 'r') as f:
    rss_data = xmltodict.parse(f.read())

papers = []
for item in rss_data['rss']['channel']['item']:
    pub_date = item.get('pubDate', '')
    
    # Convert datetime to ISO format string
    if hasattr(pub_date, 'strftime'):
        pub_date_str = pub_date.strftime('%Y-%m-%d')
    elif hasattr(pub_date, 'isoformat'):
        pub_date_str = pub_date.isoformat()
    else:
        pub_date_str = str(pub_date)
    
    papers.append({
        'title': item['title'],
        'link': item['link'],
        'description': item.get('description', ''),
        'published': pub_date_str,  # Now JSON-serializable
        'category': item.get('dc:subject', '')
    })

# Safe to serialize
with open('/tmp/papers_cache.json', 'w') as f:
    json.dump(papers, f, indent=2)
```

## Solution 2: JSON Encoder Default Handler

Use `json.dumps(..., default=str)` to auto-convert non-serializable types:

```python
import json

# Automatically converts datetime to ISO string
json_str = json.dumps(papers, default=str)

# Or with custom encoder:
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        elif hasattr(obj, 'strftime'):
            return obj.strftime('%Y-%m-%d')
        return super().default(obj)

json.dumps(papers, cls=DateTimeEncoder)
```

## Solution 3: Force String During XML Parse

Configure `xmltodict` to return strings instead of datetime objects:

```python
import xmltodict

# Force all values to strings
rss_data = xmltodict.parse(
    xml_content,
    force_cdata=True,  # Wraps values in strings
    postprocessor=lambda path, key, value: (key, str(value) if hasattr(value, 'isoformat') else value)
)
```

## When This Occurs

**Pipeline stages where this pitfall is likely**:
- RSS → parse → **cache intermediate papers to JSON** → filter → create skills
- RSS → parse → **log paper metadata to file** → analysis
- RSS → parse → **pass data to subprocess** (JSON serialization required)

**Confirmed occurrence**: 2026-05-29 neuroscience cron job run — RSS parsing succeeded, but intermediate cache file creation failed with TypeError.

## Related Pitfalls in arXiv RSS Pipeline

1. **No CDATA wrapping**: arXiv RSS uses plain text in `<description>`, not `<![CDATA[...]]>` (see `arxiv-search` skill)
2. **Abstract extraction**: `<description>` starts with `arXiv:{id}v{ver} Announce Type: {type} \nAbstract: {text}` — regex required
3. **datetime JSON serialization**: This pitfall — solved by string conversion before `json.dumps()`
4. **Pipe-to-interpreter blocked**: Security guardrail prevents `curl | python3` — save to file first
5. **RSS feed rate limits**: No limits on RSS, but API has 429 rate limiting (use RSS for cron jobs)

## Reference Files

- This file: `ai-collection-research-sync/references/datetime-json-serialization-pitfall.md`
- Session log: `ai-collection-research-sync/references/session-2026-05-29.md`
- arXiv RSS pattern: `ai_collection/arxiv-search/references/rss-fallback.md`
- Verified RSS feeds: `ai_collection/arxiv-search/references/neuroscience-rss-feeds.md`

## Integration with arxiv-search Skill

This pitfall is documented here for the research-sync pipeline context. The `arxiv-search` skill (if patched) should include this pitfall in its main SKILL.md "RSS 2.0 Parsing" section or as a separate reference file.

**Recommendation**: Patch `ai_collection/arxiv-search/SKILL.md` to add this datetime pitfall note in the RSS parsing section (but duplicate skills cause ambiguity — use reference files instead).