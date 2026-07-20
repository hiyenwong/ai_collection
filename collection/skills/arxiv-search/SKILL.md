---
name: arxiv-search
description: "arXiv paper search skill - search academic papers by keywords, authors, categories. Supports time filtering, category filtering, and paper detail retrieval. Activation: arxiv search, paper search, 论文搜索, search papers, arxiv 论文."
---

# arXiv Search Skill

Academic paper search skill using arXiv API. Search papers by keywords, authors, categories with time filtering and detail retrieval.

## Features

- **Search Capabilities**
  - Keyword search (title, abstract, all fields)
  - Author search
  - Title-specific search
  - Category-based filtering

- **Filtering Options**
  - Time range (last day/week/month/year)
  - Subject categories (cs.AI, cs.CL, cs.LG, etc.)
  - Result count limit
  - Sort by relevance or date

- **Paper Information**
  - Title, authors, abstract
  - arXiv ID and version
  - PDF download link
  - Publication date
  - Primary category

## Activation Keywords

- arxiv search
- arxiv 搜索
- paper search
- 论文搜索
- search papers
- arxiv 论文
- 学术论文
- 搜论文

## Recommended Model

- **sonnet4.5** (Balanced for search and analysis)
- **opus4.5** (For complex research tasks)

## Tools Used

- **exec**: Run arxiv API queries via curl/httpx
- **read**: Load cached results, read paper PDFs
- **write**: Save search results, create paper summaries

## Usage Examples

### Basic Search

```
搜索 arxiv: "large language model"
```

### Author Search

```
搜索作者 "Yann LeCun" 的论文
```

### Category Search

```
搜索 cs.AI 类别最新论文
```

### Time-filtered Search

```
搜索最近一周的 "vision transformer" 论文
```

## API Details

### arXiv API Endpoint

```
http://export.arxiv.org/api/query
```

### Query Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `search_query` | Search query | `ti:machine learning` |
| `start` | Start index | 0 |
| `max_results` | Max results | 10 |
| `sortBy` | Sort method | `relevance`, `submittedDate` |
| `sortOrder` | Sort order | `ascending`, `descending` |

### Query Prefixes

| Prefix | Field |
|--------|-------|
| `ti:` | Title |
| `au:` | Author |
| `ab:` | Abstract |
| `cat:` | Category |
| `all:` | All fields |

### Common Categories

| Category | Description |
|----------|-------------|
| cs.AI | Artificial Intelligence |
| cs.CL | Computation and Language |
| cs.LG | Machine Learning |
| cs.CV | Computer Vision |
| cs.NE | Neural and Evolutionary Computing |
| cs.RO | Robotics |
| stat.ML | Machine Learning (Statistics) |
| math.OC | Optimization and Control |
| physics.** | Physics subcategories |

## Implementation

### Search Function

```python
import httpx
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

ARXIV_API = "https://export.arxiv.org/api/query"

async def search_arxiv(
    query: str,
    field: str = "all",
    category: str = None,
    max_results: int = 10,
    sort_by: str = "relevance",
    days: int = None
) -> list[dict]:
    """Search arXiv papers."""
    
    # Build query
    search_query = f"{field}:{query}"
    if category:
        search_query += f" AND cat:{category}"
    
    params = {
        "search_query": search_query,
        "max_results": max_results,
        "sortBy": sort_by,
        "sortOrder": "descending"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(ARXIV_API, params=params)
        response.raise_for_status()
    
    return parse_arxiv_response(response.text, days)


def parse_arxiv_response(xml_text: str, days: int = None) -> list[dict]:
    """Parse arXiv API XML response."""
    
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom"
    }
    
    root = ET.fromstring(xml_text)
    papers = []
    cutoff = datetime.now() - timedelta(days=days) if days else None
    
    for entry in root.findall("atom:entry", ns):
        published = entry.find("atom:published", ns).text
        pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))
        
        if cutoff and pub_date < cutoff.replace(tzinfo=pub_date.tzinfo):
            continue
        
        paper = {
            "id": entry.find("atom:id", ns).text.split("/")[-1],
            "title": entry.find("atom:title", ns).text.strip().replace("\n", " "),
            "authors": [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)],
            "abstract": entry.find("atom:summary", ns).text.strip().replace("\n", " "),
            "published": pub_date.strftime("%Y-%m-%d"),
            "updated": entry.find("atom:updated", ns).text[:10],
            "pdf_url": f"https://arxiv.org/pdf/{entry.find('atom:id', ns).text.split('/')[-1]}",
            "abs_url": entry.find("atom:id", ns).text,
            "category": entry.find("atom:category", ns).get("term") if entry.find("atom:category", ns) else None
        }
        papers.append(paper)
    
    return papers
```

### Quick Search Command

```bash
# Search via curl
curl -s "http://export.arxiv.org/api/query?search_query=all:transformer&max_results=5" | xmllint --format -
```

## Workflow for Agents

### Step 1: Understand Search Intent

```markdown
- What is the user looking for?
  - Keywords → keyword search
  - Author name → author search
  - Specific topic → category + keyword
  - Recent papers → time-filtered search
```

### Step 2: Build Query

```python
def build_query(intent):
    """Build arXiv query from user intent."""
    
    if intent["type"] == "keyword":
        return f"all:{intent['query']}"
    elif intent["type"] == "author":
        return f"au:{intent['query']}"
    elif intent["type"] == "title":
        return f"ti:{intent['query']}"
    elif intent["type"] == "category":
        return f"cat:{intent['category']}"
    elif intent["type"] == "combined":
        # e.g., "machine learning in computer vision"
        return f"all:{intent['keywords']} AND cat:{intent['category']}"
```

### Step 3: Execute Search

```python
# Execute search with appropriate parameters
results = await search_arxiv(
    query=built_query,
    field=intent.get("field", "all"),
    category=intent.get("category"),
    max_results=intent.get("max_results", 10),
    sort_by=intent.get("sort_by", "relevance"),
    days=intent.get("days")
)
```

### Step 4: Present Results

```markdown
## arXiv Search Results

Found {count} papers for "{query}":

### 1. {title}
- **Authors:** {authors}
- **Published:** {date}
- **Category:** {category}
- **arXiv:** [{id}]({abs_url})
- **PDF:** [Download]({pdf_url})

**Abstract:** {abstract}

---
```

## Category Reference

### Computer Science

| Category | Name |
|----------|------|
| cs.AI | Artificial Intelligence |
| cs.CL | Computation and Language (NLP) |
| cs.CV | Computer Vision and Pattern Recognition |
| cs.LG | Machine Learning |
| cs.NE | Neural and Evolutionary Computing |
| cs.RO | Robotics |
| cs.CR | Cryptography and Security |
| cs.DB | Databases |
| cs.DC | Distributed Computing |
| cs.HC | Human-Computer Interaction |
| cs.IR | Information Retrieval |
| cs.MM | Multimedia |
| cs.SE | Software Engineering |

### Mathematics

| Category | Name |
|----------|------|
| math.OC | Optimization and Control |
| math.ST | Statistics Theory |
| math.NA | Numerical Analysis |
| stat.ML | Machine Learning (Statistics) |

### Physics

| Category | Name |
|----------|------|
| physics.comp-ph | Computational Physics |
| physics.data-an | Data Analysis |
| quant-ph | Quantum Physics |

## Best Practices

1. **Be Specific**: Use specific keywords for better results
2. **Use Categories**: Filter by category to narrow results
3. **Sort Appropriately**: Use `relevance` for overview, `submittedDate` for latest
4. **Limit Results**: Start with 10-20 results, increase if needed
5. **Check Date**: Use time filter for recent developments

## Common Use Cases

### 1. Literature Review

```
搜索 arxiv: "prompt engineering" --category cs.CL --days 30 --max 20
```

### 2. Author Tracking

```
搜索作者 "Andrew Ng" 的最新论文
```

### 3. Topic Monitoring

```
搜索 cs.AI 类别最近一周的论文
```

### 4. Specific Paper

```
搜索标题 "Attention is All You Need"
```

## Output Format

### Summary Format

```markdown
# arXiv Search Results

**Query:** {query}
**Results:** {count} papers
**Time Range:** {time_range}

---

## Papers

### 1. {Title}
**Authors:** {Author 1}, {Author 2}, et al.
**Published:** {YYYY-MM-DD}
**Category:** {category}

**Abstract:** 
{abstract}

**Links:**
- arXiv: [{id}](https://arxiv.org/abs/{id})
- PDF: [Download](https://arxiv.org/pdf/{id})

---
```

## Limitations

- arXiv API has rate limits (be respectful, ~3 second delays for large requests)
- No abstract search in advanced mode (use `all:` prefix)
- Some papers may not have PDF available immediately
- Preprints are not peer-reviewed

## Related Skills

- **news-search**: For general news
- **tech-researcher agent**: For technical research
- **skill-extractor**: Extract patterns from papers

## Dependencies

```bash
pip install httpx xmltodict
```

## Notes

- arXiv is free and open access
- Papers are preprints (not peer-reviewed)
- Good for cutting-edge research
- Check citation count on Google Scholar for impact
- Use Semantic Scholar API for additional metadata
## Instructions for Agents

1. Read the task description carefully
2. Follow the step-by-step process
3. Use the appropriate tools
4. Verify the results

## Examples

### Example 1: Basic Usage

**User:** <example user request>

**Agent:** <example agent response>

### Example 2: Advanced Usage

**User:** <example user request>

**Agent:** <example agent response>
