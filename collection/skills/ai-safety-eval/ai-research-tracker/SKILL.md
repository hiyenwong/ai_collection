---
name: ai-research-tracker
description: Track and analyze AI research from companies like OpenAI, Anthropic, Google DeepMind. Create bilingual (English/Chinese) structured notes in Obsidian with automated daily updates.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [research-tracking, ai-research, obsidian, bilingual, automation, openai]
    category: research
    related_skills: [obsidian, web-content-extraction, llm-wiki, arxiv]
---

# AI Research Tracker

Track and analyze AI research publications from major labs (OpenAI, Anthropic, Google DeepMind, etc.) with structured bilingual notes and automated daily updates.

## Overview

This skill provides a complete system for:
- Fetching research content from AI labs (even with Cloudflare protection)
- Creating structured bilingual (English/Chinese) notes
- Organizing content in Obsidian with templates
- Automating daily updates via cron jobs

## When to Use

Use this skill when:
- User wants to track AI research from OpenAI, Anthropic, etc.
- Content is blocked by Cloudflare (use jina.ai proxy)
- Need bilingual documentation (English source + Chinese translation)
- Want structured analysis format (innovation, technical details, applications)
- Need automated daily fetching

## Prerequisites

- Obsidian vault configured
- Proxy available (if needed for network access)
- Python 3.x for automation scripts

## Directory Structure

```
OpenAI Research/                    # Or "AI Research/" for multiple sources
├── README.md                       # System documentation
├── Index.md                        # Navigation hub
├── Papers/                         # Detailed research notes
│   ├── o3-o4-mini.md
│   ├── gpt-5.md
│   └── ...
├── Daily Updates/                  # Daily summaries
│   ├── 2025-04-09.md
│   └── ...
├── Insights/                       # Trend analysis
│   ├── trends.md
│   └── ...
├── _templates/                     # Note templates
│   ├── paper-template.md
│   └── daily-template.md
└── _scripts/                       # Automation
    └── fetch_research.py
```

## Content Fetching Strategy

### Method 1: Direct Browser Navigation (Preferred for Anthropic)

For sites like Anthropic that don't block browser access:

```python
# Navigate to research page
browser_navigate(url="https://www.anthropic.com/research")

# Extract full text content
browser_console(expression="document.body.innerText")

# For long articles, get content in chunks
browser_console(expression="document.body.innerText.substring(0, 15000)")
browser_console(expression="document.body.innerText.substring(15000, 30000)")
```

**Advantages:**
- Full content extraction (not just summary)
- Preserves article structure
- No proxy needed for many sites
- Can scroll and navigate sections

### Method 2: jina.ai Proxy (For Cloudflare-Protected Sites like OpenAI)

When direct access fails:

```bash
# Use jina.ai proxy
curl -sL --proxy "http://127.0.0.1:7890" \
  "https://r.jina.ai/http://openai.com/research" 2>&1

# For specific articles
curl -sL --proxy "http://127.0.0.1:7890" \
  "https://r.jina.ai/http://openai.com/index/article-slug/" 2>&1
```

**When to use:**
- Site blocks direct browser access
- Need quick text extraction
- Don't need interactive navigation

### Response Format

jina.ai returns clean Markdown:
```
Title: Article Title

URL Source: http://original-url.com

Markdown Content:
# Article content...
```

## Note Structure (Bilingual - Enhanced Format)

Each research note follows this comprehensive structure:

```markdown
# [Article Title in Chinese]

**原文标题**: [Original Title]
**发布日期**: [Date]
**分类**: [Category]
**原文链接**: [URL]

## 摘要 (Abstract)
[Chinese translation of abstract/summary]

## 核心内容翻译 (Full Translation)
[Complete Chinese translation of the article content]

## 深度解读 (Deep Analysis)

### 1. 研究背景与动机
[Research context and why this matters]

### 2. 方法论与创新点
[Methods used and what's novel]

### 3. 主要发现与结论
[Key findings and conclusions]

### 4. 技术细节剖析
[Technical deep dive - architecture, algorithms, benchmarks]

### 5. 实际应用与影响
[Practical implications for developers, businesses, policymakers]

### 6. 局限性与未来方向
[Limitations and future work]

## 思考与反思 (Personal Reflection)
[Your critical thinking about the research]
- What are the implications?
- What concerns does it raise?
- How does it connect to other work?

## 相关阅读 (Related Reading)
- [Links to related papers/articles]
- [Previous work from same lab]
- [Follow-up research]

---
*Generated on [date]*
```

### Alternative Structure (for quick notes)

For faster processing of multiple articles:

```markdown
# Article Title

**原文标题**: [Original]
**发布日期**: [Date]
**分类**: [Category]
**原文链接**: [URL]

## 核心发现 (Key Findings)
- Finding 1
- Finding 2
- Finding 3

## 中文翻译 (Translation)
[Key sections translated]

## 分析 (Analysis)
[Brief analysis]

## 影响 (Implications)
[Practical implications]

---
*Generated: [date]*
```

## Setup Instructions

### Step 1: Create Directory Structure

```bash
mkdir -p "{OBSIDIAN_PATH}/OpenAI Research/"{Papers,Daily Updates,Insights,_templates,_scripts}
```

### Step 2: Create Templates

**paper-template.md:**
```markdown
---
title: {{title}}
date: {{date}}
url: {{url}}
tags: [{{tags}}]
status: {{status}}
---

# {{title}}

## 基本信息
- **发布日期**: {{date}}
- **原文链接**: [{{url}}]({{url}})
- **研究类型**: {{type}}
- **重要性**: {{priority}}

---

## 原文摘要
{{original_summary}}

---

## 中文翻译
{{chinese_translation}}

---

## 深度解读
### 核心创新
{{core_innovation}}

### 技术细节
{{technical_details}}

### 性能提升
{{performance_gains}}

---

## 关键要点
1. {{key_point_1}}
2. {{key_point_2}}
3. {{key_point_3}}

---

## 实际应用
{{applications}}

---

## 局限性与风险
{{limitations}}

---

*创建于: {{created_date}}*
```

**daily-template.md:**
```markdown
---
date: {{date}}
type: daily-update
---

# Daily Update - {{date}}

## 今日概览
- **新发布研究**: {{count}} 篇
- **重要更新**: {{important_count}} 篇
- **重点关注**: {{focus_area}}

---

## 新发布内容
{{articles_section}}

---

## 趋势观察
{{trends}}

---

*自动生成于: {{timestamp}}*
```

### Step 3: Create Automation Script

**fetch_research.py:**
```python
#!/usr/bin/env python3
"""Fetch AI research and create Obsidian notes"""

import os
import subprocess
from datetime import datetime

OBSIDIAN_PATH = "{path}/OpenAI Research"
PROXY = "http://127.0.0.1:7890"
JINA_BASE = "https://r.jina.ai/http://"

def fetch(url):
    cmd = f'curl -sL --proxy "{PROXY}" "{JINA_BASE}{url}" 2>&1'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else None

def create_note(article):
    # Create structured note from article
    pass

def main():
    # Fetch research page
    content = fetch("openai.com/research")
    # Parse articles
    # Create notes
    # Generate daily update
    pass

if __name__ == "__main__":
    main()
```

### Step 4: Setup Cron Job

```bash
# Copy script to hermes scripts directory
cp fetch_research.py ~/.hermes/scripts/

# Create cron job (runs daily at 9 AM)
cronjob create --name "AI Research Daily" \
  --schedule "0 9 * * *" \
  --script "fetch_research.py"
```

## Workflow

### Multi-Article Batch Processing (Anthropic Example)

For tracking multiple articles from a research page:

1. **Navigate to research page:**
   ```python
   browser_navigate(url="https://www.anthropic.com/research")
   ```

2. **Extract article list:**
   ```python
   browser_console(expression="document.body.innerText")
   # Parse to find article URLs, titles, dates
   ```

3. **Create todo list for batch processing:**
   ```python
   todo(todos=[
       {"id": "1", "content": "Article 1: Title (Date)", "status": "in_progress"},
       {"id": "2", "content": "Article 2: Title (Date)", "status": "pending"},
       # ... etc
   ])
   ```

4. **Process each article:**
   ```python
   for article in articles:
       browser_navigate(url=article['url'])
       content = browser_console(expression="document.body.innerText")
       # Create comprehensive note
       write_file(path=f"{date} {title}.md", content=note_content)
       todo(todos=[...], merge=True)  # Mark as completed
   ```

### Manual Research Tracking (Single Article)

1. **Fetch content:**
   ```bash
   # Method 1: Direct browser (for Anthropic, etc.)
   browser_navigate(url="https://www.anthropic.com/research/article-slug")
   browser_console(expression="document.body.innerText")
   
   # Method 2: jina.ai proxy (for OpenAI, etc.)
   curl -sL --proxy "http://127.0.0.1:7890" \
     "https://r.jina.ai/http://openai.com/index/article-slug/" 2>&1
   ```

2. **Create note from template:**
   - Copy paper-template.md
   - Fill in all sections
   - Translate key content to Chinese
   - Add deep analysis with 6 sections
   - Include personal reflection

3. **Update index:**
   - Add to Index.md
   - Link related notes

4. **Create daily update:**
   - Summarize new research
   - Note trends

### Automated Daily Updates

The cron job will:
1. Fetch latest research
2. Detect new articles
3. Create draft notes
4. Generate daily summary
5. Deliver notification

## Best Practices

### Content Quality

1. **Always translate key sections** - Don't leave English-only notes
2. **Add personal insights** - Don't just copy official content
3. **Include performance tables** - Benchmarks are crucial for AI research
4. **Note limitations** - Every research has limitations
5. **Cross-reference** - Link to related notes

### Organization

1. **Use consistent tags** - #o-series, #gpt-series, #multimodal, etc.
2. **Rate importance** - ⭐ to ⭐⭐⭐⭐⭐
3. **Update status** - draft → completed → archived
4. **Maintain index** - Keep Index.md current
5. **Archive old content** - Move outdated notes to _archive/

### Automation

1. **Proxy auto-detection** - Script automatically detects common proxy ports (7890, 7891, 7897, 1080, 1087, 9090)
2. **Handle failures gracefully** - Script continues on errors and provides helpful diagnostics
3. **Limit API calls** - Don't hammer jina.ai
4. **Log everything** - Keep track of what was fetched
5. **Review drafts** - Automated notes need human review

**Proxy Configuration Priority:**
1. Environment variable `HTTP_PROXY` or `HTTPS_PROXY`
2. Auto-detected working proxy on common ports
3. Direct connection (fallback)

## Common Patterns

### Pattern 1: Model Release

For new model announcements (GPT-5, o3, etc.):

```markdown
## 核心创新
- **Architecture**: What's new in the architecture
- **Training**: New training methods
- **Capabilities**: New abilities

## 性能提升
| Benchmark | New Model | Previous | Improvement |
|-----------|-----------|----------|-------------|
| MMLU | 87% | 82% | +5% |
```

### Pattern 2: Technical Report

For research papers:

```markdown
## 技术细节
### Method
[Detailed method description]

### Experiments
[Experimental setup]

### Results
[Key results with tables]

### Ablation Studies
[What matters most]
```

### Pattern 3: Product Launch

For product announcements:

```markdown
## 实际应用
### 适用场景
- [Specific use case 1]
- [Specific use case 2]

### 对开发者的影响
[API changes, new features]

### 定价与可用性
[Pricing tiers, rollout plan]
```

## Troubleshooting

### Issue: jina.ai returns empty

**Cause:** URL format issue or rate limiting
**Solution:** 
- Check URL format (must include http://)
- Add delay between requests
- Try alternative: textise dot iitty

### Issue: Proxy connection fails / "Failed to fetch research page"

**Cause:** Proxy service not running or network connectivity issues
**Solution:**
1. **Check if proxy is running:**
   ```bash
   curl --proxy http://127.0.0.1:7890 https://httpbin.org/ip
   ```

2. **Common proxy ports to check:**
   - Clash: 7890 (HTTP), 7891 (SOCKS5)
   - V2Ray: 1080, 1087
   - Surge: 9090

3. **Start your proxy service:**
   - Clash Verge: Open app and click "Enable"
   - V2Ray/Shadowsocks: Start the client
   - Verify: `lsof -i :7890` should show the proxy process

4. **The script now auto-detects proxies** - it will try common ports automatically

5. **If no proxy available:**
   - The script will try direct connection as fallback
   - Some networks may block jina.ai directly
   - Consider using a VPN or different network

### Issue: Cron job fails but manual run works

**Cause:** Environment variables or proxy not available in cron context
**Solution:**
- The script auto-detects proxies at runtime (added in v1.1)
- Ensure proxy service starts before cron job runs
- Check logs: `cronjob list` and `cronjob log <job-id>`

### Issue: Chinese characters garbled

**Cause:** Encoding issue
**Solution:**
- Ensure files are UTF-8
- Use `encoding='utf-8'` in Python
- Check terminal encoding

### Issue: Cron job not running

**Cause:** Path or permission issue
**Solution:**
- Use absolute paths in script
- Check script permissions: `chmod +x script.py`
- Check hermes logs: `cronjob list`

## Integration with Other Skills

### With obsidian skill
- Use `skill_view("obsidian")` for vault operations
- Link research notes to existing notes
- Use Dataview queries for research dashboard

### With arxiv skill
- Combine with arxiv for academic papers
- Link blog posts to arxiv papers
- Track both industry and academic research

### With llm-wiki skill
- Use llm-wiki structure for broader knowledge base
- AI Research Tracker as specialized module
- Cross-link between systems

## Examples

### Example 1: OpenAI o3/o4-mini

See the full example in the conversation history. Key sections:
- Agentic tool use breakthrough
- Multimodal reasoning details
- Performance benchmarks
- Safety considerations

### Example 2: GPT-5

See the full example in the conversation history. Key sections:
- Unified system architecture
- Router mechanism
- Coding/writing/health capabilities
- Comparison with previous models

## Resources

- [OpenAI Research](https://openai.com/research)
- [Anthropic Research](https://www.anthropic.com/research)
- [Google DeepMind](https://deepmind.google/research/)
- [jina.ai reader](https://r.jina.ai/)
- [Obsidian](https://obsidian.md/)

---

*Skill version: 1.1.0*
*Last updated: 2026-04-11*

## Changelog

### v1.2.0 (2026-04-12)
- Added browser-based content extraction method for sites like Anthropic
- Added batch processing workflow for multiple articles
- Enhanced note template with 6-section deep analysis format
- Added personal reflection section to template
- Support for both Anthropic and OpenAI research tracking

### v1.1.0 (2026-04-11)
- Added automatic proxy detection for common ports (7890, 7891, 7897, 1080, 1087, 9090)
- Added fallback to direct connection if no proxy available
- Improved error messages with troubleshooting guidance
- Added multiple jina.ai service endpoints for redundancy
- Updated troubleshooting section with proxy debugging steps

## Activation Keywords

- "ai-research-tracker"
- "ai research tracker"
- "use ai research tracker"
- "ai research tracker help"
- "ai research tracker tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps
