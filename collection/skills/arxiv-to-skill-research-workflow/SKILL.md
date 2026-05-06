---
name: arxiv-to-skill-research-workflow
description: "Lightweight research workflow: search arXiv papers, select valuable ones, generate skills, sync to ai_collection, and update Obsidian wiki. No knowledge graph required. Use for: automated paper research, skill generation from academic papers, research note management, lightweight literature review. Keywords: arxiv research, paper to skill, research automation, skill generation, obsidian research notes, ai_collection sync."
---

# arXiv to Skill Research Workflow

Lightweight end-to-end workflow for researching arXiv papers, extracting valuable insights, generating skills, and documenting findings in Obsidian.

## Overview

This workflow provides a streamlined alternative to knowledge graph-based research:
- No KG database setup required
- Direct arXiv API access
- Manual paper selection based on value criteria
- Direct skill creation from paper analysis
- Multi-format documentation (skills + Obsidian wiki)

## Trigger Conditions

- Scheduled cron job for neuroscience paper monitoring
- User requests arXiv paper research and skill creation
- Keywords: arxiv, paper search, skill generation, research automation, obsidian wiki update

## Workflow Steps

### Step 1: Search arXiv

**PRIMARY METHOD: Browser-based extraction (Recommended for API rate limits)**

When arXiv API returns HTTP 429 (rate limit) or fails, use browser navigation to access category listing pages directly:

```python
from hermes_tools import browser_navigate, browser_click, browser_snapshot

# Navigate to category recent submissions page
browser_navigate(url="https://arxiv.org/list/q-bio.NC/recent")

# Get structured paper list from snapshot
snapshot = browser_snapshot(full=True)
# Parse entries from DescriptionList elements
# Each entry contains: arXiv ID, title, authors, subjects

# Click specific paper for details
browser_navigate(url="https://arxiv.org/abs/XXXX.XXXXX")
detailed_snapshot = browser_snapshot(full=True)
# Extract abstract, metadata from full page
```

**CRITICAL (2026-05-05)**: `browser_navigate` to arxiv.org URLs now fails with `net::ERR_CONNECTION_CLOSED`. arXiv.org direct navigation is unreliable. **Discovery strategy**: (1) `web_search` for Google-indexed arXiv links, (2) GitHub SNN-Daily-Arxiv (`https://github.com/SpikingChen/SNN-Daily-Arxiv/`) for SNN papers via table JS extraction, (3) Individual `browser_navigate` to `https://arxiv.org/abs/XXXX.XXXXX` for abstracts (single-paper pages work when category listings fail).

**Category pages to use:**
- `https://arxiv.org/list/q-bio.NC/new` - Neurons and Cognition (shows FULL abstracts in snapshot — preferred over `/recent`)
**Category pages to use:**
- `https://arxiv.org/list/q-bio.NC/recent` - Neurons and Cognition
- `https://arxiv.org/list/cs.NE/recent` - Neural and Evolutionary Computing
- `https://arxiv.org/list/cs.LG/recent` - Machine Learning (broad)
- `https://arxiv.org/list/quant-ph/recent` - Quantum Physics
- `https://arxiv.org/list/stat.ML/recent` - Statistics ML (emerging methods)

**WARNING**: Cross-category keyword search via `/search/?query=...` is broken (HTTP 400) as of 2026-05-05. Only use category listing pages.

**IMPORTANT: `/new` vs `/recent`**: The `/new` pages show complete abstracts directly in the `browser_snapshot` text (as `<paragraph>` elements under each entry), while `/recent` pages only show titles/authors/subjects. Use `/new` for paper assessment without needing to navigate to individual `/abs/` pages.

**Multiple sessions per day**: arXiv only updates once daily (new papers appear at ~14:00 ET / ~02:00 UTC). Running multiple cron sessions on the same calendar day yields diminishing returns — afternoon/evening sessions will find the same papers as morning sessions. Consider skipping evening sessions unless monitoring for rapid cross-lists or replacements.
**WARNING (2026-05-04)**: arXiv `/search/?query=...` URLs with multi-term queries (using `+` separators) now return HTTP 400 "Bad Request". The cross-category keyword search URL pattern is **broken**. Use category listing pages exclusively — they remain fully functional.

**Advantage**: Pre-structured, chronological listings with direct links to PDF and HTML versions — more reliable than API when rate-limited.

**CRITICAL (2026-05-03)**: arXiv `/search/?query=...` browser pages now return **400 Bad Request** even for simple queries. Combined with HTTP 429 rate limits on the API, browser-based search is ALSO unreliable. The ONLY reliable discovery method is direct category page browsing (`/list/{category}/recent`). Do NOT waste time on `/search/?query=...` pages or API queries — go straight to category listing pages.

**CRITICAL (2026-05-05)**: arXiv search forms are BROKEN — `/search/?query=...` returns HTTP 400 Bad Request and `/search/advanced` returns "Whoops! Something went wrong" even with valid parameters. Do NOT waste time on arXiv search pages. **Only category listing pages work reliably**: `/list/{category}/recent` (e.g., `/list/q-bio.NC/recent`, `/list/cs.NE/recent`).

**CRITICAL (2026-05-02)**: JS extraction on category listing pages (`/list/{category}/recent`) is **UNRELIABLE** — the dt/dd DOM structure produces garbled output due to page structure differences. For category pages, use `browser_snapshot(full=True)` and parse the text output directly — it contains all paper titles, IDs, authors, and subjects in structured text format.

**CRITICAL (2026-05-02)**: JS extraction on category listing pages (`/list/{category}/recent`) is **UNRELIABLE** — the dt/dd DOM structure produces garbled output due to page structure differences. For category pages, use `browser_snapshot(full=True)` and parse the text output directly — it contains all paper titles, IDs, authors, and subjects in structured text format.

**CRITICAL (2026-05-06)**: JS extraction on search result pages (`/search/?query=...`) is **INTERMITTENTLY UNRELIABLE**. The `li.arxiv-result` DOM sometimes produces incorrect titles or empty fields. When it works, the improved recipe below extracts IDs, titles, authors, AND abstracts — but fallback to `browser_snapshot(full=True)` if results look garbled. Category pages (`/list/{category}/recent`) remain the most reliable method.

**Improved JS extraction recipe** (verified working 2026-05-06 on search result pages — use if snapshot parsing is insufficient):
```javascript
(() => {
  const results = document.querySelectorAll('li.arxiv-result');
  const papers = [];
  results.forEach(li => {
    const idEl = li.querySelector('a[href*="abs/"]');
    const id = idEl ? idEl.textContent.trim().replace('arXiv:','').trim() : '';
    const allP = li.querySelectorAll('p');
    let title = '', authors = '', abstract = '';
    allP.forEach(p => {
      const t = p.textContent.trim().replace(/\s+/g, ' ');
      if (!t.startsWith('Authors:') && !t.startsWith('Submitted') && !t.startsWith('Abstract:') && !title) { title = t; }
      if (t.startsWith('Authors:')) { authors = t.replace('Authors:', '').trim().substring(0, 150); }
      if (t.startsWith('Abstract:')) { abstract = t.substring(9).trim().substring(0, 300); }
    });
    papers.push({ id, title, authors, abstract });
  });
  return JSON.stringify(papers);
})()
```
**NOTE**: This improved recipe extracts abstracts in addition to IDs/titles/authors, which is critical for coverage analysis. The older recipe only extracted titles/authors.

**Search URL format**: Use `?query=term1+term2&start=0&order=-announced_date_first`. Avoid `searchtype=all` and `size=20` params — these cause 400 Bad Request errors.

**FALLBACK METHOD: Python urllib** — Only if browser navigation fails (rare):

**CRITICAL: Use `execute_code` with Python `urllib.request` — `web_extract` returns EMPTY content for arXiv `/abs/` URLs and "Blocked" for `/pdf/` URLs. `terminal` (curl) also unreliable.**

```python
from hermes_tools import terminal
import urllib.request, urllib.parse, ssl, xml.etree.ElementTree as ET, json, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def search_arxiv(query, max_results=30):
    params = urllib.parse.urlencode({
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results
    })
    url = f"https://export.arxiv.org/api/query?{params}"
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req, context=ctx, timeout=30)
    return resp.read().decode("utf-8")
```

**IMPORTANT**: Use `urllib.parse.urlencode()` — manual URL construction with spaces causes "Malformed or illegal URL" errors. XML namespaces: `{"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}`.

**Multiple keyword searches recommended** — run 2-3 queries with different term combinations:
- `all:"neuroscience" AND all:"brain network"`
- `all:"spiking neural network" AND all:"computational"`
- `all:"neural dynamics" AND all:"brain"`

**Important**: Add `time.sleep(3)` between requests to respect arXiv API rate limits.

### Step 1b: Pre-Flight Same-Day Dedup (CRITICAL 2026-05)

**Before running the full workflow, check if today's papers were already scanned in an earlier cron session.** At 738+ skills with multiple daily cron runs, same-day paper batches are frequently rescanned, producing zero-new-skills sessions that waste resources.

```python
import os, re
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
vault = os.environ.get("OBSIDIAN_VAULT_PATH", "/Users/hiyenwong/Documents/Obsidian Vault")
ai_notes = os.path.join(vault, "ai_collection")

# Find all today's research notes
today_notes = [f for f in os.listdir(ai_notes) if f.endswith('.md') and today in f.lower() and 'research' in f.lower()]
if today_notes:
    # Collect all arXiv IDs already documented today
    documented_ids = set()
    for note in today_notes:
        with open(os.path.join(ai_notes, note)) as fh:
            content = fh.read()
        ids = re.findall(r'26\d{2}\.\d{5}', content)
        documented_ids.update(ids)
    
    print(f"Existing same-day sessions: {len(today_notes)}")
    print(f"arXiv IDs already documented today: {len(documented_ids)}")
    
    # After scraping, compare:
    # new_ids = scraped_ids - documented_ids
    # if not new_ids:
    #     print("[SILENT] — all papers already covered in earlier session")
    #     # Skip the rest of the workflow
```

**Decision rule**: If `len(new_ids) == 0` after comparing scraped papers against same-day notes, respond with `[SILENT]` and skip skill creation, Obsidian updates, and report generation entirely.

### Step 2: Filter and Select Papers

From the search results:
1. Deduplicate by arXiv ID (papers appear across multiple queries)
2. **Deduplicate against same-day session notes** (Step 1b above) — if all papers already documented today, output `[SILENT]` and stop
3. Cross-reference paper titles against existing skill directory names in `~/.hermes/skills/ai_collection/` — list directories, normalize names (lowercase, strip hyphens), check for substring matches. This catches papers already covered under different naming conventions.
3. Filter to target date range (e.g., papers from the last 24-48 hours)
### Coverage Analysis** — Calculate coverage metrics:

**CRITICAL (2026-05-05)**: The word-overlap matching alone misses exact-match skills. Use a two-tier approach:

```python
def normalize_for_matching(text):
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'using', 'based'}
    words = [w for w in text.lower().replace('-', ' ').replace('_', ' ').split() if w not in stop_words]
    return set(words)

# TIER 1: Direct substring / acronym matching (highest priority)
# Check if paper title contains skill name tokens or vice versa
def direct_match(title, skill_name):
    title_lower = title.lower()
    skill_lower = skill_name.lower().replace('-', ' ').replace('_', ' ')
    # Check for key acronyms or exact phrases
    for token in skill_lower.split():
        if len(token) > 3 and token in title_lower:
            # Also check reverse: title key terms in skill name
            return True
    # Check for known acronyms (e.g., "UniBCI" in skill name "unibci-invasive-foundation-model")
    import re
    title_acronyms = re.findall(r'\b[A-Z]{2,}\b', title)
    for acronym in title_acronyms:
        if acronym.lower() in skill_lower:
            return True
    return False

# TIER 2: Word overlap (for when direct match fails)
for paper in papers:
    title_words = normalize_for_matching(paper['title'])
    matched_skill = None
    
    # Try direct match first
    for skill in existing_skills:
        if direct_match(paper['title'], skill):
            matched_skill = skill
            break
    
    # Fall back to word overlap
    if not matched_skill:
        for skill in existing_skills:
            skill_words = normalize_for_matching(skill)
            # Weight key neuroscience terms higher
            key_terms = {'spiking','brain','neural','network','hopfield','attractor',
                        'reservoir','free','energy','criticality','quantum','modality','bci'}
            common = title_words & skill_words
            key_matches = common & key_terms
            if len(key_matches) >= 2 or len(common) >= 3:
                matched_skill = skill
                break

coverage_rate = already_covered / len(papers) * 100
# >90% = high maturity, >98% = extreme maturity
```

**Observed misses from word-overlap-only matching** (2026-05-05):
- "UniBCI: Towards a Unified Pretrained Model for Invasive BCI" → missed `unibci-invasive-foundation-model` (acronym mismatch)
- "Geometric analysis of attractor boundaries in kernel Hopfield networks" → missed `kernel-hopfield-associative-memory` (word order differs)
- "Attractor FCM" → missed `attractor-fcm-gradient-descent` (too short for 2-word overlap)
       elif best_overlap >= 2:
           # Verify with manual substring check
           covered = any(kw in paper['title'].lower() for kw in matched_skill.replace('-', ' ').split() if len(kw) > 3)
   
   coverage_rate = already_covered / len(papers) * 100
   # >90% = high maturity, >95% = extreme maturity, >98% = near-saturation
   ```
5. **Value-Based Prioritization** — For uncovered papers, implement scoring:
   ```python
   value_factors = []
   if 'brain' in paper['title'].lower(): value_factors.append("Brain focus")
   if 'spiking' in paper['abstract'].lower(): value_factors.append("Neural dynamics")
   if 'digital twin' in paper['title'].lower(): value_factors.append("Digital twins")
   
   score = len(value_factors) * 10
   # Bonus for interdisciplinary/high-impact topics
   if 'digital twin' in paper['title'].lower(): score += 30
   if 'active inference' in paper['abstract'].lower(): score += 25
   
   # Priority: HIGH (>=50), MEDIUM (30-49), LOW (<30)
   ```
6. Select top 8-12 papers based on priority score and coverage analysis

### Step 3: Extract Paper Content

For each selected paper:
1. Use `web_extract` with the arXiv abstract page (`https://arxiv.org/abs/XXXX.XXXXX`)
2. Also try the PDF if abstract is insufficient: `https://arxiv.org/pdf/XXXX.XXXXX`
3. Extract: title, authors, key methodology, core contribution, practical applications

### Step 4: Check for Existing Skills

Before creating, check if a skill already exists:
- Search `~/.hermes/skills/ai_collection/` for similar topics
- Use `skills_list` to check registered skills
- Skip papers that map to existing skills (note them in the report)

### Step 5: Create Hermes Skills

**Decide skill placement** before creating:
- **ai_collection domain**: Neuroscience, SNN, brain networks, computational neuroscience → `~/.hermes/skills/ai_collection/<skill-name>/`
- **Standalone domain**: Quantum computing, control systems, systems engineering, or other distinct fields → `~/.hermes/skills/<skill-name>/` (top-level)
### Step 5: Create Hermes Skills

**PREFERRED: `skill_manage(action="create")`** — auto-creates directories, validates structure.
**ALTERNATIVE: `write_file`** directly at `~/.hermes/skills/<skill-name>/SKILL.md` — reliable, direct.
**ALTERNATIVE: `delegate_task`** — works for parallel skill creation when multiple skills needed simultaneously (confirmed working 2026-05-05). Provide the target skill path and full SKILL.md content in the task context.

For each new skill, create a SKILL.md with this structure:

1. **YAML frontmatter MUST include `description`**:
   ```yaml
   ---
   name: skill-name
   description: "Short description of what the skill does."
   version: 1.0.0
   ---
   ```

2. **Paper-based skills MUST include `**arXiv ID:**` format** (not `**arXiv:**`):
   ```markdown
   **arXiv ID:** 2604.20209 | **Code:** https://github.com/...
   ```

3. **Paper-based skills MUST have `## Abstract` and `## Key Contributions` sections**

4. **No line exceeding 120 characters** — break long lines

5. **Location**: `ai_collection/collection/skills/<skill-name>/SKILL.md` (note: `collection/skills/` not just `skills/`)
   - The root `skills/` directory exists but the validator checks `collection/skills/`
   - After creating in `skills/`, copy to `collection/skills/` for validation

For each new skill, create a SKILL.md with this structure:

```markdown
---
name: skill-name
description: "Short description of the methodology. Activation triggers: keyword1, keyword2, keyword3."
---

# Skill Title

> One-line summary of the paper's contribution and methodology.

## Metadata
- **Source**: arXiv:XXXX.XXXXX
- **Authors**: Author names
- **Published**: YYYY-MM-DD

## Core Methodology

### Key Innovation
Description of what's novel.

### Technical Framework
Step-by-step technical description.

## Implementation Guide

### Prerequisites
- Required tools/libraries

### Step-by-Step
1. Concrete implementation steps

### Code Example
\`\`\`python
# Minimal working example
\`\`\`

## Applications
- Use case 1
- Use case 2

## Pitfalls
- Known limitations

## Related Skills
- related-skill-1
- related-skill-2
```

**Naming convention**: Use lowercase, hyphenated names: `topic-method-detail`
**Location**: `~/.hermes/skills/ai_collection/<skill-name>/SKILL.md`

### Step 6: Update Obsidian Wiki

**Multi-domain organization** (2026-05-04): When researching non-neuroscience domains (e.g., quantum computing), create separate folder structures rather than mixing into ai_collection:
- `Quantum Computing Research/Quantum Computing Index.md` — domain index
- `Skills/Quantum/<skill-name>.md` — domain-specific skill notes
- `Research Logs/Quantum Computing Research - YYYY-MM-DD.md` — daily logs

This keeps the vault organized by research domain. The ai_collection folder remains neuroscience-focused.

**Vault path**: Check `OBSIDIAN_VAULT_PATH` env var. Also check these common locations in order: `/Users/hiyenwong/obsidian_notes/` (actual vault, 2026-05 confirmed), `/Users/hiyenwong/obsidian-vault/`, `/Users/hiyenwong/Workspace/obsidian/`, `/Users/hiyenwong/ai_github/obsidian_wiki/`, then default `/Users/hiyenwong/Documents/Obsidian Vault`. Verify by checking for `.obsidian/` directory inside.

**Use `execute_code` with Python** for vault file operations — cleaner string handling than terminal commands.

#### 6a: Create Daily Research Note
- Path: `ai_collection/neuroscience-research-YYYY-MM-DD[-session].md`
- Content: Date, scan summary, paper list with links, key findings, trends
- Use `-late` or `-morning` suffix if multiple sessions per day
- **Include coverage analysis**: Papers scanned, recent papers count, coverage rate, new skills created, covered papers list, research trends

#### 6b: Create Individual Skill Notes
- Path: `ai_collection/<skill-name>.md`
- Content: Skill metadata, methodology summary, links to arXiv and SKILL.md
- **Structure**: Include YAML frontmatter with tags, source arXiv link, core methodology summary, applications list, implementation link, and related skills wikilinks
- **Purpose**: Quick reference notes that link to full skill implementation and daily research notes

**Example Skill Note Structure**:
```markdown
---
tags: [brain-digital-twins, execution-semantics, arxiv-XXXX.XXXXX]
---

# Skill Title

> One-line summary

## Source
- **arXiv**: [XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX)
- **Published**: YYYY-MM-DD

## Core Methodology
Brief description...

## Applications
- App 1
- App 2

## Implementation
See full guide in: `~/.hermes/skills/ai_collection/<skill-name>/SKILL.md`

## Related
- [[related-skill-1]]
- [[Neuroscience Research - YYYY-MM-DD - Cron Job Update]]
```

#### 6c: Update INDEX.md
- Increment total skill count
- Update timestamp
- Add new entries to the skills list

#### 6d: Update Neuroscience Research MOC
- Add session row to the session history table
- Add new papers to relevant thematic sections
- Create new thematic sections if needed (e.g., "Neuromorphic Hardware & Devices")
- Update trend analysis

**MOC Update Pattern (3 separate patches required):**
1. Daily table row: Insert `| [[daily-note-name|YYYY-MM-DD]] | N | N | themes |` into the **Research Sessions** table (NOT the Research Statistics table). The MOC has TWO tables — the Statistics table (lines ~10-17) has a different column structure. The Sessions table has columns `| Date | Papers | New Skills | Key Themes |`. Find the `|------|--------|------------|------------|` separator and insert the new row immediately after it.
2. Thematic section: Add bullet entry under the matching `### Theme Name` section with wikilink to daily note
3. Latest Skills section: Add `#### skill-name` header + summary entry at the end of the file

**MOC structure** (800+ line file as of 2026-05, ~56KB):
- Lines 1-5: Frontmatter
- Lines 7-17: Title + Research Statistics table (2-column: Metric | Count)
- Lines 19-43: Research Sessions table (4-column: Date | Papers | New Skills | Key Themes)
- Lines 45-800+: Research Themes sections by topic
- Final section: Latest Skills

**CRITICAL**: Do NOT insert daily rows into the Statistics table (2-column) — it will corrupt the MOC layout. Always target the Sessions table (4-column with `| Date | Papers | New Skills | Key Themes |` header).

## Key Learnings (from production runs)

### ai_collection CI Validation (2026-05-04)
The CI pipeline (`validate.yml`) enforces strict validation on new skills. See `references/ai-collection-ci-validation.md` for full details. Key requirements:
- `description` in YAML frontmatter (required, causes failure if missing)
- `**arXiv ID:**` format in body (not `**arXiv:**`)
- `## Abstract` and `## Key Contributions` sections for paper skills
- Line length < 120 characters
- File must be in `collection/skills/` (not root `skills/`)

**Note**: CI has pre-existing lint failures in older Python scripts — new markdown-only skills don't cause these. If CI fails on `Lint Python Scripts`, it's likely a pre-existing issue, not your change.

### Tool Selection
### Tool Selection
- **write_file** for skill creation at `~/.hermes/skills/<skill-name>/SKILL.md` — reliable, direct
- **execute_code** for Obsidian vault manipulation — Python's string operations handle markdown cleanly
- **terminal** for file discovery, reading existing content, and git operations
- **web_search** for initial paper discovery — NOTE: Increasingly returns empty results for academic queries (e.g., "arxiv neuroscience brain network" returned 0 results on 2026-05-04). Still worth trying as first-pass, but do NOT rely on it. Browser category page scraping (`/list/{category}/recent`) remains the most reliable discovery method
- **web_extract** for arXiv content — NOTE: Returns "Blocked: URL targets a private or internal network" for many arXiv URLs (new failure mode observed 2026-05). Also returns empty content for `/abs/` URLs. When web_extract fails, fall back to browser navigation
- **browser_navigate + browser_snapshot** for arXiv scraping — `browser_snapshot(full=True)` is the ONLY reliable method for arXiv content. Returns structured text with arXiv IDs, titles, authors, and subjects. JS extraction via `browser_console` is UNRELIABLE on both category pages AND search result pages (confirmed 2026-05-06) — do NOT use it. **Parallel browser_navigate**: Launch for multiple category pages (q-bio.NC + cs.NE) simultaneously before snapshotting — both load concurrently, cutting discovery time in half.
- **Parallel browser_navigate**: Launch `browser_navigate` for multiple category pages (e.g., q-bio.NC + cs.NE) simultaneously before snapshotting — both pages load concurrently, cutting discovery time in half
- **cp -r with mkdir -p** for syncing skills to ai_collection — cp -r silently fails on some directories; always `mkdir -p` target first
- See `references/arxiv-access-failure-modes.md` for comprehensive list of all documented arXiv access failure modes (429, Blocked, 400 Bad Request, empty httpx responses)

### Common Pitfalls
1. **delegate_task for skill creation**: Does NOT work reliably — use `skill_manage(action="create")` (preferred, auto-creates directories) or `write_file` directly
2. **arXiv rate limits**: Worsened significantly (2026-04 observed). Use 5s delays between queries, reduce `max_results` to 15, add `User-Agent` header, 60s timeout, SSL verification disabled. Some query patterns permanently fail (429) — implement 3 retries with 10s exponential backoff. If first query fails, remaining queries may still succeed. **2026-05 update**: All 5 queries in a single batch can hit 429 simultaneously. Use `wait = 4 * (attempt + 1)` (4s, 8s, 12s) between retries. When ALL queries are rate-limited, wait 60+ seconds before retrying the entire batch.
3. **web_extract "Blocked" error**: `web_extract` consistently returns "Blocked: URL targets a private or internal network" for arXiv URLs since 2026-05. This is a new failure mode beyond rate limits. When this happens, use `browser_navigate` + `browser_snapshot` + `browser_console` (JS extraction) instead — this is the most reliable method for arXiv content
4. **`httpx` in `execute_code` returns empty responses INTERMITTENTLY**: `httpx.get()` against arXiv API from within `execute_code` sandbox sometimes returns 0-byte responses (no error, just empty) — but it ALSO works reliably on many sessions (2026-05-05: full data for 11 papers). Always try `httpx` first (fastest when it works), but have `web_search` → `terminal` + `curl` + HTTPS fallback ready. If `httpx` response length < 100, immediately switch to fallback.
4. **curl requires HTTPS for arXiv API**: Terminal `curl` to `http://export.arxiv.org/api/query` triggers security scan approval prompt. Always use `https://export.arxiv.org/api/query` to avoid interactive approval blocking cron jobs.
3. **Deduplication**: Papers appear in multiple keyword searches; dedupe by arXiv ID
4. **execute_code state persistence**: State does NOT persist between `execute_code` calls. Save intermediate data to `/tmp/` files (e.g., `papers_data.json`, `paper_details.json`) and reload in subsequent calls. Without this, accumulated search results will be lost between steps.
4. **Vault path**: Always check env var first; don't hardcode
5. **Session naming**: Use time-of-day suffix when running multiple sessions per day
6. **Existing skills**: Always check before creating — some papers were already covered. Use `ls ~/.hermes/skills/ai_collection/` and normalize names for coverage detection
7. **INDEX.md corruption**: INDEX.md can silently corrupt during writes — skill count can drift by 200+ from actual (observed: INDEX.md said 477, actual was 697). Always verify count with Python before reporting. See `references/index-rebuild-utility.py` for automated rebuild script.
8. **`read_file` unreliability**: Hermes `read_file` returns double-numbered lines (`     1|     1|content`) — unreliable for parsing. Use Python `open()` directly for file content manipulation
9. **Cron execution pattern**: When running as scheduled job, use `execute_code` with Python (not terminal+curl) for better reliability. Save state to `/tmp/` between steps. Handle partial failures gracefully — if some queries fail, continue with successful ones.
10. **MOC patching requires 3 separate operations**: (1) Daily table row insertion, (2) Thematic section bullet addition, (3) Latest Skills section header+summary append. Each requires reading current content and precise positioning.
11. **Mature collection adaptation**: When >90% papers have existing skills (typical after 90+ skills), expand keyword scope or add new domains rather than expecting many new skills per session.
12. **Date filtering**: Papers returned may have dates in the future relative to system time. Use flexible date ranges (30 days) and sort by published date to get truly recent papers.
13. **Empty search results**: If queries return 0 papers in target date range, expand search to all recent papers regardless of date and filter post-hoc.
- **Standalone neuroscience skills fully synced** (2026-05-05): All neuroscience standalone skills have been synced to ai_collection (0 remaining). Earlier notes about "~130 pending neuroscience skills" are obsolete. The 142 remaining standalone skills are non-neuroscience (devops, quantum, control systems, web dev, etc.).
- **Leverage cached search results**: Previous cron runs may have saved papers to `/tmp/` files (e.g., `/tmp/arxiv_papers.json`, `/tmp/neuro_papers_v3.json`). If arXiv API is rate-limited or failing, scan `/tmp/*.json` for existing paper data before attempting new queries — this can save significant time and avoid API blocks.
15. **Coverage detection via title normalization**: When checking if papers are already covered, normalize both paper titles AND skill names by removing punctuation, lowercasing, and splitting into word sets. Check for intersection of 2+ common words between title and skill name for robust matching across naming conventions. **CAUTION at 700+ skills**: Word-overlap matching produces false positives (e.g., ShiftLIF paper matched to `neuron-photonic-spiking-laser` because both share 'spiking' + 'neural' keywords). Always do a second pass with exact keyword matching (e.g., `shiftlif` in skill name → `shiftlif-power-of-two-quantization`). Priority order: (1) exact arXiv ID match in existing skill, (2) exact keyword match (unique term from title present in skill name), (3) word-overlap matching.
16. **Paper scoring for selection**: Implement relevance scoring based on keyword frequency weighted by importance. Example scoring for neuroscience:
    ```python
    keywords = {'spiking neural network': 5, 'brain network': 4, 'neural dynamics': 4}
    score = sum(text.count(kw) * weight for kw, weight in keywords.items())
    ```
    This helps prioritize high-value papers when collection is mature.
17. **Standalone-to-ai_collection sync**: Skills may exist as standalone directories in `~/.hermes/skills/` but not yet in `ai_collection/`. Check both locations. Use `shutil.copytree()` to sync. The INDEX.md entry may reference a standalone skill that hasn't been copied to ai_collection yet.
18. **Standalone duplicate detection pattern**: When standalone skills have names very similar to existing ai_collection skills (e.g., `fc-guided-band-selection-bci` vs `fc-guided-band-selection-mi-bci`, or `saliency-aware-eeg-decoding` vs `simon-saliency-neural-decoding`), they are almost always near-identical duplicates covering the same paper. Check the first 3 lines of both SKILL.md files to confirm. If confirmed, skip the sync — no value in duplicating. At 714+ skills in ai_collection, most remaining standalone neuroscience skills are either duplicates or very tangential topics.

**Dual-directory sync (ai-collection vs ai_collection)**: There are TWO parallel directories:
- `~/.hermes/skills/ai-collection/` (hyphen) — curated subset (~27 skills)
- `~/.hermes/skills/ai_collection/` (underscore) — full collection (700+ skills)
Skills created in one don't appear in the other. `skill_manage(action='create')` targets the MAIN skills dir only. Use `shutil.copytree()` for cross-directory sync. Check both directories when determining if a skill already exists.

18. **`skill_manage` path limitations**: `skill_manage(action='create')` creates skills in `~/.hermes/skills/` (main dir), NOT in `ai_collection/`. When creating skills for the ai_collection, use `write_file` to write directly to `~/.hermes/skills/ai_collection/<name>/SKILL.md`.
18. **Skip evaluation criteria**: At high coverage rates (85%+), not every uncovered paper warrants a skill. Skip papers that are: (a) too narrow/specific (e.g., single-dataset validation, specific neuroanatomy like hippocampal place cells or cerebellar motor learning), (b) conceptually overlapping with existing skills (e.g., new Hamiltonian method when energy-based/physics-guided skills exist), (c) review/perspective papers with no extractable methodology, **(d) empirical/observational studies reporting neural correlates without computational methodology** (e.g., "ACC-Insula connectivity correlates with anxiety severity" — reports findings but introduces no reusable algorithm, framework, or analytical method), **(e) HCI/eye-tracking focused papers when the collection targets computational neuroscience methodology** (e.g., confidence-based line assignment in reading gaze data), **(f) non-neuroscience optimization/multi-agent papers** (e.g., distributed black-box consensus optimization), **(h) incremental robustness fixes** to existing frameworks (e.g., HGF Lambert W function fix to avoid negative posterior precision - a bug fix, not a new methodology), **(i) theoretical/conceptual papers** without concrete methodology (e.g., AGI papers on measuring understanding that propose philosophical frameworks without extractable algorithms), **(j) toy/demo environment papers** — papers demonstrating methodologies in game-like or toy environments (e.g., Minecraft navigation, simple simulations) where the underlying methodology is already covered by existing skills. Document skip reasons in the daily research note.

**Skip taxonomy** (from 2026-05-05 session at 729 skills):
- `too_narrow`: Application-specific with no generalizable method (Minecraft navigation)
- `incremental_fix`: Bug fix or robustness patch to existing framework (HGF volatility fix)
- `review_paper`: Literature review without new methodology (EEG/EMG neural regeneration review)
- `theoretical`: Philosophical/conceptual without extractable algorithms (AGI understanding measurement)
- `too_generic`: Insufficient abstract + generic title, likely covered (generic EEG/ML+neuro papers)
19. **Extreme maturity skip patterns** (700+ skills): At this scale, the skip-to-create ratio approaches 1:1 or higher. In a 57-paper session, expect ~4-8 skippable papers among uncovered ones. Common skip categories: theoretical neurobiology without computational methodology (murburn-thermodynamic), HCI applications (gaze tracking), non-neuroscience optimization (distributed consensus), narrow neuroanatomy without generalizable methodology, and **integration/benchmark papers where ablation shows simpler is better** (MPCS: 11 mechanisms → removing 2 yields best Perf at 4.7x lower compute). When the collection reaches 700+ skills, the workflow should prioritize skip evaluation quality over creation volume. **New skills at 700+ skills primarily come from mathematical formalism papers** (e.g., RG theory, universal approximation theorems) applied to neuroscience rather than domain-specific methodology papers — these cross-domain formalism transfers are the remaining gap.
19. **Same-day category scan coverage**: Scanning q-bio.NC or cs.NE category pages on the day of submission (or within 1-2 days) produces much lower coverage rates (~40-50%) compared to delayed scans (~80-100%). This is expected — same-day scans catch papers before any previous session has filtered them. A low coverage rate on a same-day scan does NOT indicate collection regression; it indicates the scan is catching genuinely fresh papers.
20. **Large file timeouts** (2026-05-05): `execute_code` times out at 300s on large Obsidian files (>50KB, 800+ lines). `read_file` with `limit`/`offset` pagination is slow on large files. **Solution**: Use `patch` for targeted updates — read only the relevant section via `read_file` with small `limit` (10-30 lines), then patch. For statistics updates, read just the frontmatter and first 20 lines. Never load the entire MOC or INDEX.md in a single `execute_code` call.
21. **Browser timeout on arXiv search URL** (2026-05-05): `browser_navigate` to `https://arxiv.org/search/?query=...` can timeout at 60s. **Solution**: Prefer category listing pages (`/list/{category}/recent`) which are faster and more reliable. If search page is needed, reduce `size=25` and retry once on timeout.
22. **Two-tier coverage matching required** (2026-05-05): Word-overlap matching alone misses 15-25% of existing skills due to acronym mismatches (e.g., "UniBCI" vs "unibci-") and short titles (e.g., "Attractor FCM" vs "attractor-fcm-gradient-descent"). Use direct substring/acronym matching as Tier 1, word overlap as Tier 2. See updated Coverage Analysis section.

### Cron Execution Output Format

When running as a scheduled cron job, format the final report for automatic delivery:

```markdown
## Session Summary
- **Session Date**: YYYY-MM-DD [Time of Day]
- **Papers Scanned**: N (via X API queries)
- **Recent Papers (N days)**: M
- **Coverage Rate**: X% (N/N papers covered by existing skills)
- **New Skills Created**: N

### New Skills Added
#### 1. skill-name-1
**Paper**: Title (arXiv:XXXX.XXXXX)  
**Authors**: Author names  
**Published**: YYYY-MM-DD  
**Key Innovation**: One-line summary of the methodology  
**Applications**: Use case 1, use case 2

#### 2. skill-name-2
...

### Covered Papers (Already in Collection)
- Paper A → covered by `existing-skill-1`
- Paper B → covered by `existing-skill-2`
...

### Research Trends Identified
1. Trend 1 with brief explanation
2. Trend 2 with brief explanation
...

### Collection Statistics
- **Total Skills**: N
- **Research Sessions**: N sessions tracked
- **Coverage Maturity**: [High/Medium/Low]
```

**Key principle for cron execution**: The report must be self-contained and actionable without interactive follow-up. Structure it as a complete research digest that can be automatically delivered to Slack/email/Discord.

### Typical Output
- **Early phase** (<30 skills): 7-10 new skills per session from ~35 candidate papers
- **Mature phase** (90-160 skills): Expect 0-3 new skills per session; high coverage rate (90%+) is normal — selective approach justified
- **Highly mature phase** (160+ skills): 98%+ coverage expected; focus on interdisciplinary boundaries and emerging niches
- **Extreme maturity phase** (700+ skills): 80-90% coverage typical when scanning multiple categories, because q-bio.NC and cs.NE include non-neuroscience papers (HCI, optimization, multi-agent) that correctly get skipped. All neuroscience-relevant papers ARE covered. Sessions confirm comprehensive coverage and document trends rather than finding new skills. Consider reducing scan frequency to weekly.
- **Extreme maturity phase** (400+ skills): 100% coverage on core topics likely. Primary value extraction shifts from new skill creation to (a) syncing standalone skills to ai_collection (~269 neuroscience-related pending at 477 skills), and (b) monitoring interdisciplinary boundaries for cross-domain opportunities. arXiv search pages may return 400 errors or timeout — use category page scraping only.
- **Extreme maturity phase** (400+ skills): 90-100% coverage normal; skip evaluation with documented justification is the primary value activity. Expect 0-1 new skills per session. Focus on: (a) identifying interdisciplinary boundaries not yet covered, (b) monitoring research trends for emerging methodologies, (c) tracking hardware/neuromorphic device developments. All skipped papers require explicit reasoning (too narrow, conceptually overlapping, review-only).
- **Mature collection example** (2026-04-27): 45 papers scanned, 2 from last 7 days, 1 existing skill found, 1 new skill created — successful session with 50% coverage
- **Zero-new-skills session** (2026-04-29): 58 papers scanned, 4 recent papers analyzed, 100% existing coverage — successful session demonstrating collection maturity at scale
- **High-coverage niche discovery** (2026-04-29 evening): 77 papers scanned (5 keywords), 67 recent papers, 83% coverage (5/6 papers already covered), 1 high-value skill created (brain-foundation-model-inversion). Demonstrates that even with high coverage, novel research directions (brain foundation model inversion) still emerge from interdisciplinary boundaries.
- **Partial failure + high coverage** (2026-04-29 late evening): 4 queries attempted, 2 hit 429 rate limits (50% failure), 40 papers from successful queries, 21 neuroscience papers identified, 3 new skills created (vlm-visual-cortex-alignment-robustness, computational-lesions-multilingual-language-models, meta-learning-ict-brain-decoding). Coverage: 93% (146 existing skills). Demonstrates graceful degradation under API pressure while still extracting value from partial results.
- **Extreme maturity example** (2026-04-30): 74 papers scanned across 5 queries, 98.7% coverage (73/74 papers already covered by 163 existing skills), 1 new skill created (brain-llm-key-neurons-grammar). Demonstrates that even with near-complete coverage of core neuroscience topics, valuable skills can still be found in interdisciplinary areas (Brain-LLM alignment for grammar processing). Key insight: expand keyword scope to include cross-domain topics when core domain is saturated.
- **Partial query success + high coverage** (2026-04-30 morning): 5 queries attempted, all 5 succeeded, 72 papers scanned, 39 recent papers, 75% coverage (6/8 analyzed papers already covered), 2 new skills created (energy-first neural architecture, burst spiking ViT). Demonstrates successful execution with valuable new skill extraction from interdisciplinary boundaries even with high baseline coverage.
- **Mature collection with memory architectures** (2026-04-30 cron morning): 61 papers scanned (3 queries), 23 recent papers, 96% coverage, 2 new skills created (zenbrain-7layer-memory-architecture, smartvector-neuroscience-embeddings-rag). Demonstrates focus on neuroscience-inspired memory systems for autonomous AI and self-aware embeddings for temporal-aware RAG.
- **Extreme maturity with interdisciplinary focus** (2026-04-30 evening): 132 papers scanned across 8 expanded queries, 99.2% coverage (131/132 papers covered by 188 existing skills), 1 new skill created (direct-neural-assemblies-causal-learning). Demonstrates that at extreme maturity (>99%), valuable skills emerge exclusively from interdisciplinary boundaries—"causal learning" keyword expansion yielded DIRECT mechanism combining neural assemblies with causal inference.
- Daily research note with full analysis
- Updated INDEX and MOC files
- **Collection maturity signal**: When >90% of papers have existing skills, the collection is near saturation — consider expanding keyword scope or adding new domains
- **2026-05-06 cron evening**: 57 papers scanned across 2 categories (25 q-bio.NC + 32 cs.NE), 75.4% overall coverage (43/57), 100% neuroscience-relevant coverage. 0 new skills created, 3 synced from standalone to ai_collection (bosonic-grid-states-qec, ice-review, quantum-ml-certification). 14 uncovered papers all rejected — optimization benchmarks, toy projects, reviews, non-neuroscience. At 738 skills, collection at extreme maturity; dual-metric reporting essential for accurate assessment.
- **Extreme maturity signal**: When >98% coverage achieved, focus exclusively on interdisciplinary boundaries and emerging research directions at the intersection of covered domains
- **Ultra-mature phase** (500+ skills): At this scale, nearly ALL papers in core neuroscience categories (q-bio.NC, cs.NE) are already covered. The primary value extraction activities are:
  1. **Standalone-to-ai_collection sync** (batch of 25-30 per session) — check for standalone neuroscience skills not yet copied to ai_collection
  2. **Skip evaluation** — filter out non-methodology papers (optimization algorithms, hardware tools, review-only papers)
  3. **Cross-domain monitoring** — watch cs.LG, stat.ML, and other adjacent categories for interdisciplinary breakthroughs
  4. **Browser-only discovery** — `web_search` and `httpx`/`curl` API calls are increasingly unreliable; browser category page scraping is the only consistent method
  4. **arXiv search API is completely unreliable** (429 + 400 errors) — use ONLY `/list/{category}/recent` category pages

### Zero New Skills Session Handling

When all papers are already covered (100% coverage), this is a **successful completion**, not a failure:

**Report Structure:**
```markdown
## Session Summary
- **Papers Scanned**: N
- **Recent Papers**: M
- **New Skills Created**: 0
- **Coverage Rate**: 100% (mature collection)

## Papers Analyzed
| # | Paper Title | arXiv ID | Status |
|---|-------------|----------|--------|
| 1 | Paper A | XXXX.XXXXX | ✅ Covered |
| 2 | Paper B | XXXX.XXXXX | ✅ Covered |

## Collection Maturity Assessment
The ai_collection has reached mature phase with N+ skills covering major research areas...
```

**Key Points to Document:**
1. **Coverage rate** — percentage of papers already in collection
2. **Skill mappings** — which existing skill covers each paper
3. **Research trends** — themes detected even without new skills
4. **Recommendations** — next steps for expanding coverage (new keywords, domains)

**Obsidian Updates (Still Required):**
- Create daily research note with "zero new skills" status
- Update MOC with session entry (papers scanned = N, new skills = 0)
- Document coverage rate in statistics
- Do NOT increment skill count in INDEX.md when no new skills created

**Verification Checklist:**
- [ ] Daily research note created with coverage analysis
- [ ] MOC updated with zero-new-skills session entry
- [ ] Skill mappings documented for each analyzed paper
- [ ] Research trends identified and recorded
- [ ] Recommendations for coverage expansion provided
### Collection Statistics Verification

**Always verify INDEX.md count matches filesystem** — INDEX.md has been observed to drift by 220+ skills (477 vs 697 actual). The count in INDEX.md is NOT authoritative; always compute from filesystem.

**Authoritative counting**: Use Python for definitive skill count:
```python
count = sum(1 for item in os.listdir(skill_dir)
            if os.path.isdir(os.path.join(skill_dir, item))
            and os.path.exists(os.path.join(skill_dir, item, "SKILL.md")))
```

**Automated rebuild**: Use `references/index-rebuild-utility.py` to fix INDEX.md count drift automatically. Run it as part of every session's verification step.

### Coverage Rate Variability

Coverage rate is NOT monotonically increasing and does NOT approach 100% as skill count grows:
- **At 233 skills**: Coverage dropped to 60% because collection expanded into adjacent domains (emotion energy, receptive field geometry, neuro-symbolic AI)
- **At 379 skills**: Coverage was 100% for a single-category scan (q-bio.NC only, narrow scope)
- **At 756 skills**: Coverage was 69.0% across 44 papers from 3 sources (q-bio.NC + cs.NE + search). 29/42 analyzable papers matched. The "uncovered" papers were mostly generic q-bio.NC titles without abstracts (e.g., "Neural coding in the visual cortex") that couldn't be reliably matched. This demonstrates that at extreme maturity, multi-source scanning inflates paper count with generic titles that have no extractable methodology — coverage rate should be calculated on analyzable papers only
- **Key insight**: Coverage depends on scan breadth, not just skill count. Narrow single-category scans can hit 100% even at moderate skill counts; broad multi-domain scans stay at 70-90% even at 700+ skills because adjacent domains are continuously being added
- **Don't assume high coverage** — always compute fresh per session
- When coverage drops below 70%, collection is actively expanding into new domains — healthy growth, not regression

### Standalone Sync False Positive Pitfall (2026-05-06)

**Problem**: Keyword-based standalone-to-ai_collection sync matched non-neuroscience skills using broad keywords like "neural" and "dynamics" which appear in quantum, finance, and systems engineering skills. 18 unrelated skills synced (stock-analysis, skill-extractor, quantum-computing-patterns, etc.).

**Root Cause**: Single-keyword matching is too broad — "neural" and "dynamics" appear across many domains.

**Fix**:
- **Require co-occurrence**: Match ≥2 neuroscience-specific keywords (e.g., `brain` + `network`, `spiking` + `neuron`, `eeg` + `decoding`)
- **Exclude non-neuro domains**: Skip skills with `quantum`, `finance`, `stock`, `security`, `systems-engineering` as primary domains
- **At 750+ skills**: Disable automated standalone sync — false positive cost exceeds discovery benefit
- When coverage is 80-85% at 700+ skills and all unmatched papers are non-neuroscience (HCI, optimization, multi-agent), the collection IS mature — the dip is category noise, not skill gaps
- **">98% extreme maturity" signal is misleading at scale** — at 800+ skills spanning many domains, expect 80-90% coverage on broad scans; treat anything >85% as mature

### Domain-Scoped Coverage Reporting (2026-05-06)

When scanning broad categories like cs.NE (which includes optimization, evolutionary computing, general neural networks alongside neuroscience), a single overall coverage rate is misleading. Use **dual-metric reporting**:

1. **Overall coverage**: all scanned papers vs existing skills
2. **Domain-scoped coverage**: only neuroscience-relevant papers (brain networks, SNNs, EEG/fMRI, BCI, predictive coding, cognitive modeling, neural dynamics)

**Example from 2026-05-06 scan**: 57 papers → 75.4% overall coverage but 100% neuroscience-relevant coverage. The 14 uncovered papers were all outside scope: optimization benchmarks (RCMAES, MAEO), evolutionary computing (BEAGLE GP), toy projects (Minecraft navigation), aerospace verification (ACAS-Xu), etc.

**Interpretation guide:**
- Overall < 70% → collection expanding into new domains
- Overall 70-90% but domain 100% → broad category has noise; collection is mature for target domain
- Both > 95% → extreme maturity; focus on interdisciplinary boundaries

**Action**: Report both rates. If overall is low but domain rate is high, the collection is healthy — evaluate uncovered papers for rejection rather than skill creation.

### New Session Examples

*2026-05-06 early morning cron*: 26 papers scanned (q-bio.NC + cs.NE + 2 keyword searches via browser_console JS extraction), 0 new skills, 96.2% coverage (25/26), 1 paper skipped (Minecraft neuromorphic navigation — toy environment, methodology already covered). Key workflow: **parallel `browser_navigate` calls** for q-bio.NC and cs.NE simultaneously (both pages load concurrently), then `browser_snapshot` for text parsing on category pages + `browser_console` JS extraction on search result pages. Coverage check included **both ai_collection (738) and standalone skills (889 total)** for comprehensive matching. At 738+ skills, 96% coverage is the new normal for extreme maturity — zero new skills per session is expected and healthy.

*2026-05-02 cron v2*: 21 papers scanned across 4 domains

*2026-05-02 cron v2*: 21 papers scanned across 4 domains (brain network, neural dynamics, SNN, computational neuroscience), 86% coverage (18/21), 0 new skills created, 1 synced (`geometric-brain-dynamics-mapping-v7` from standalone to ai_collection). Key workflow: `execute_code` with `httpx` returned empty responses for arXiv API → fallback to `web_search` for discovery → `terminal` with `curl` + HTTPS for full XML parsing → Python dedup/skill coverage check → `shutil.copytree` for standalone-to-ai_collection sync → patch Obsidian wiki. 3 papers skipped: too narrow (JASTAP), conceptually overlapping (Hamiltonian brain dynamics), review-only (linguistics). Demonstrates that at 255 skills, sync and skip decisions become as important as creation. Key learning: `httpx` in `execute_code` sandbox can return 0-byte responses for arXiv API even with HTTPS — use `web_search` as first pass, then `terminal` + `curl` for reliable XML retrieval.

*2026-05-04 cron (hourly research)*: 10 papers scanned (neuroscience + quantum topics), 14 Anthropic research articles fetched. Pipeline: `weekly_topics.py` → arXiv HTTPS curl (proxy) → `fetch_anthropic_research.py` → Python import to kg.db → vector similarity + PageRank + Louvain → report to `memory/YYYY-MM-DD.md`. **Key findings**: `arxiv_fetch.py` script uses `http://` (not `https://`) causing 429 rate limits — must patch to HTTPS. KG grew from 32→56 entities. Hash-based vector similarity scores remain low (0.05-0.26), confirming known limitation. Louvain community detection produces mostly singleton communities with hash vectors. 5 reusable skill patterns extracted. Anthropic research trending toward AI safety (Constitutional Classifiers, Trustworthy Agents) and AI economics (81,000 person survey).

*2026-05-05 cron*: 50 papers scanned (5 arXiv API queries via `execute_code`+`httpx` — all succeeded), 11 high-value papers identified, 4 new skills created (kernel-hopfield-attractor-geometry, saliency-aware-eeg-decoding, fc-guided-band-selection-bci, fcn-llm-graph-tuning), 2 existing skills verified (scalable-snn-without-backprop, free-energy-moe-routing). Key workflow: `execute_code`+`httpx` worked reliably → `delegate_task` in batches of 3 for skill creation → Obsidian weekly report at `/Users/hiyenwong/obsidian_notes/neuroscience/` (vault path, NOT `ai_collection/`). Weekly report format: `神经科学研究周报-YYYY-MM-DD.md`. Demonstrates efficient pipeline: API→selection→delegate_task×4→Obsidian update. Skills created at top-level `~/.hermes/skills/<name>/` (not under `ai_collection/` subdirectory). Vault structure: `neuroscience/` subdirectory with weekly reports.

*2026-05-05 early morning cron*: 33 papers scanned (q-bio.NC: 15, cs.NE: 18), 84.8% coverage (28/33), 0 new skills created. 5 papers skipped: all non-neuroscience (HCI gaze tracking, gait dynamics, optimization algorithms CMA-ES/MAEO, multi-agent consensus). Key insight: at 705 skills, all neuroscience-relevant papers are covered. The 84.8% coverage rate is lower than the 90-100% seen in recent sessions because broader multi-category scanning captures more adjacent-domain papers that correctly get skipped. Browser category scraping (q-bio.NC + cs.NE) remains the most reliable discovery method. Demonstrates that at extreme maturity, session value comes from confirming comprehensive coverage and documenting trends, not from finding new skills.

*2026-05-02 cron v2*: 21 papers scanned across 4 domains (brain network, neural dynamics, SNN, computational neuroscience), 86% coverage (18/21), 0 new skills created, 1 synced (`geometric-brain-dynamics-mapping-v7` from standalone to ai_collection). Key workflow: `execute_code` with `httpx` + HTTPS + `follow_redirects=True` works reliably for arXiv API — previously-reported "empty response" was caused by HTTP (not HTTPS). Fallback chain if needed: `web_search` for discovery → `terminal` with `curl` + HTTPS for full XML parsing → Python dedup/skill coverage check → `shutil.copytree` for standalone-to-ai_collection sync → patch Obsidian wiki.

*2026-05-02 early cron*: 24 papers scanned (q-bio.NC + cs.NE categories + API), 92% coverage (22/24), 2 new skills created (dimensionality-modularity-continual-learning, attractor-fcm-gradient-descent). Demonstrates that even at 240 skills, valuable skills emerge from interdisciplinary boundaries (continual learning architecture analysis, attractor-based FCMs). Coverage remained high despite expanding into adjacent domains.

*2026-05-02 cron*: 9 skills created from ~200 arXiv results (neuroscience, brain network, neural dynamics, SNN, computational neuroscience). Key workflow: web_search for initial discovery → browser_navigate + browser_console JS extraction for arXiv scraping → write_file for skill creation at `~/.hermes/skills/<name>/` → mkdir -p + cp for sync to `~/ai_collection/collection/skills/` → Obsidian wiki update. Notable papers: brain foundation model inversion (SBI), AFR-Net flow routing, HoloBrain/HoloGraph oscillatory GNNs, SWpC directed FC, GeoDynamics SPD manifold, NH-GCAT depression diagnosis, sparse connectivity recovery, LuminaNet BNN, JEDI dynamics inference. Key learning: `web_extract` consistently returns "Blocked" for arXiv URLs; browser-based scraping via browser_console is most reliable.

*2026-05-02 evening cron v2*: 32 papers scanned (q-bio.NC + cs.NE categories), 90.6% coverage (29/32), 0 new skills created, 1 synced (`geometry-aware-spiking-gnn` from standalone to ai_collection). 3 papers skipped: hardware tool (earable platform), optimization algorithms (CMA-ES, MAEO). Key learning: JS extraction on category listing pages produces garbled output — use `browser_snapshot(full=True)` text parsing instead. At 324 ai_collection skills, standalone-to-ai_collection sync and skip evaluation are as important as new skill creation.

*2026-05-04 evening cron v2*: 16 papers scanned (q-bio.NC + cs.NE browser, same-day May 4 submissions), 42.9% coverage (6/14 covered), 2 new skills created (self-organized-criticality-brain-body-resonance, modal-neural-modality-discovery). Key findings: same-day scan coverage was ~43% — significantly lower than typical, confirming same-day scans catch genuinely fresh papers. Correctly skipped empirical fMRI study (no extractable methodology). Demonstrates effective skip evaluation and same-day scan dynamics.

*2026-05-03 morning cron*: 12 papers scanned (q-bio.NC + cs.NE browser + 9 API queries), 83.3% coverage (10/12), 0 new skills, 10 synced to ai_collection (standalone neuroscience batch). 2 papers skipped: optimization algorithms (RCMAES, MAEO). Key finding: 4 of 9 `curl` API queries returned 0-byte responses (empty XML, no HTTP error) — `execute_code` + `curl` against arXiv is increasingly unreliable. Browser category page scraping (`/list/{category}/recent`) remains the most reliable discovery method. At 337 skills, standalone-to-ai_collection sync (~130 pending neuroscience skills) is now the primary value extraction activity alongside new paper monitoring.

*2026-05-05 afternoon v3 cron*: 43 papers scanned (arXiv search + q-bio.NC), 95.3% coverage (41/43), 0 new skills created, 0 standalone neuroscience skills remaining to sync. 2 papers skipped: AGI/hierarchical automata (out of scope) + incremental HGF update (no new methodology). Collection has reached extreme maturity at 723 skills — all core neuroscience domains saturated. Browser-based scraping (browser_navigate + browser_console JS extraction) confirmed as most reliable arXiv access method. At this maturity level, successful sessions are defined by accurate coverage analysis and justified skip decisions, not new skill creation.

*2026-05-03 evening cron (final)*: 15 papers scanned (q-bio.NC + cs.NE browser category pages only — search API returned 400 Bad Request), 100% coverage (15/15), 0 new skills created, 29 standalone neuroscience skills synced to ai_collection (total: 506). 2 papers skipped: RCMAES (optimization algorithm), MAEO (engineering optimization). Key insight: arXiv search pages now return 400 Bad Request, not just 429 — category page browsing is the ONLY reliable discovery method. At 506 skills, sync (29 per batch) + skip evaluation are the primary value extraction activities. Search API completely broken; category browsing works perfectly.

*2026-05-03 evening cron*: 30 papers scanned (q-bio.NC + cs.NE browser + keyword searches), 90.0% coverage (27/30), 0 new skills created. 3 uncovered papers evaluated and all skipped: (a) RCMAES — pure optimization algorithm, no neuroscience, (b) NEAT-NC — robotics-focused, NEAT is well-known, (c) Bayesian neuroimaging association — statistical methodology overlapping with `multimodal-brain-connectivity-gnn`. Notable recent papers: geometry-aware brain dynamics mapping (2604.25592), Attractor FCM (2604.27947), Physical Foundation Models (2604.27911). Key insight: at 470 skills, skip evaluation with documented justification is the primary value activity. All skipped papers require explicit reasoning in the daily note. Trends identified: geometry-aware brain mapping, SNN hardware scaling, higher-order brain interactions, neuromorphic devices beyond traditional SNN.

*2026-05-03 late evening cron*: 34 papers scanned (q-bio.NC + cs.NE browser only, search pages failed), 100% coverage (34/34). 0 new skills created, 7 standalone skills synced to ai_collection (pa-tcnet-brain-tumor-seg, pa-tcnet-cross-subject-eeg, odebrain-continuous-eeg-graph, meta-learning-in-context-brain-decoding-v3/v4, meta-learning-in-context-decoding-v3, mind2drive-eeg-driver-intention). Key finding: arXiv search pages (`/search/?query=...`) now return 400 Bad Request or 60s timeout — category page scraping is the ONLY reliable discovery method. At 477 skills, 100% coverage on both q-bio.NC and cs.NE confirms extreme maturity. ~269 neuroscience-related standalone skills remain pending sync.

### arXiv Search Page Degradation (2026-05-03)

arXiv search pages (`/search/?query=...`) have degraded significantly:
- **400 Bad Request**: Direct search URLs with `+` separators return HTTP 400
- **60s Timeout**: `browser_navigate` to search pages hangs and times out
- **Only reliable method**: Category listing pages (`/list/{category}/recent`) — these work consistently
- **At extreme maturity (450+ skills)**: Skip search pages entirely, only use category pages — all core papers are covered anyway, and search pages waste 60+ seconds

*2026-05-03 late evening cron*: 34 papers scanned (q-bio.NC + cs.NE browser only, search pages failed), 100% coverage (34/34). 0 new skills created, 7 standalone skills synced to ai_collection (pa-tcnet-brain-tumor-seg, pa-tcnet-cross-subject-eeg, odebrain-continuous-eeg-graph, meta-learning-in-context-brain-decoding-v3/v4, meta-learning-in-context-decoding-v3, mind2drive-eeg-driver-intention). Key finding: arXiv search pages (`/search/?query=...`) now return 400 Bad Request or 60s timeout — category page scraping is the ONLY reliable discovery method. At 477 skills, 100% coverage on both q-bio.NC and cs.NE confirms extreme maturity. ~269 neuroscience-related standalone skills remain pending sync.

*2026-05-04 morning cron*: 37 papers scanned (q-bio.NC + cs.NE browser categories), 83.8% coverage (31/37), 0 new skills, 8 standalone synced (quantum-computing, reservoir computing, synaptic dynamics). 6 papers skipped (robotics, AI safety, fringe theory, biomechanics, survey methodology, hardware tool). Key insight: coverage rate dropped from 90%+ to 83.8% because collection expanded into quantum-neuroscience, reservoir computing, and federated learning — healthy domain expansion. Browser category scraping remains the most reliable discovery method. At 558 skills, standalone sync continues to add value across adjacent domains.

*2026-05-05 early cron*: 14 papers scanned (q-bio.NC: 9, cs.NE: 5 neuroscience-relevant), 100% coverage, 0 new skills, 1 synced (`kernel-hopfield-attractor-geometry` from standalone to ai_collection). Key workflow: browser category scraping → Python coverage check with 3+ word intersection → standalone-to-ai_collection sync → Obsidian wiki update. 1 paper skipped: distributed consensus optimization (non-neuroscience, cs.MA cross-list). At 715 skills, collection has reached extreme maturity — sync operations and skip evaluation are the primary value extraction activities. Coverage matching with 3+ word intersection achieved perfect accuracy across all 14 papers. Key learning: cs.NE cross-lists from cs.MA, cs.LG often contain non-neuroscience papers (distributed systems, optimization) — explicitly skip papers without brain/neural/SNN/cognitive content.

*2026-05-06 morning cron*: 44 papers scanned (q-bio.NC: 17, cs.NE: 7, keyword search: 20), 69.0% coverage (29/42 analyzable), 0 new skills, 2 skipped (review paper, gaming/navigation). Key finding: at 756 skills, simple normalization yields ~50% but adding a `specific_mappings` dict (key phrase → skill name) brings coverage to 69% with high accuracy. The remaining "uncovered" papers were mostly generic q-bio.NC titles without abstracts that couldn't be reliably matched. Multi-source scanning increases total papers but decreases per-paper match rate due to generic titles. Key learning: when coverage drops below 70% at extreme maturity, it's usually due to generic category titles, not actual collection gaps — focus on analyzable papers with abstracts.

### Partial Rate Limit Resilience

When some queries fail with 429 errors but others succeed:
1. **Don't abort** — proceed with papers from successful queries
2. **Log the failure** — note which queries failed in the daily research note
3. **Reduce scope** — set expectations accordingly (e.g., "2 papers from last 7 days found" vs "45 total papers")
4. **Still valuable** — even 1-2 recent papers can yield new skills in mature collections

**Updated Recommendations** (from 2026-04-30 production run):
- **Retry strategy**: On 429 error, wait 10s, retry once; if still failing, skip and continue
- **Success rate tolerance**: Even 20% query success (1/5) can yield valuable results
- **Never abort entirely**: Partial results are still valuable, especially in mature collections
- **API degradation periods**: Some query patterns may permanently fail (429) during high-traffic periods — implement fallback to broader queries
- **Empty published dates**: When arXiv API returns empty published dates, extract date from arXiv ID format (YYMM.XXXXX → 20YY-MM). See date extraction utility in "Handling Date Parsing" section below

**Example sessions demonstrating resilience**:

*2026-04-27 cron*:
- 5 queries attempted, 3 succeeded, 2 rate-limited
- 45 total papers, 2 recent, 1 new skill created
- **Result**: Successful completion despite partial failures

*2026-04-29 late evening*:
- 4 queries attempted, 2 hit 429 rate limits (50% failure)
- 40 papers from successful queries, 3 new skills created
- **Result**: Graceful degradation under API pressure

*2026-04-30 late-night*:
- 5 queries attempted, 1 succeeded, 4 failed (429/503)
- 11 papers from successful query, 1 new skill created
- **Result**: 91% coverage, extracted value from 20% success rate
- **Key insight**: Even with severe rate limiting, continuing with available data yields valuable skills

## Verification
## Verification

After completing the workflow:
1. Count new skill directories in `~/.hermes/skills/ai_collection/`
2. Verify INDEX.md skill count matches actual files
3. Check MOC has the new session entry
4. Confirm daily research note exists and is complete
5. Present summary to user with: scan stats, new skills table, skipped papers, key trends

## CI Validation Notes

See `references/ci-validation-status.md` for pre-existing CI failure tracking. New skills pass validation — failures are in legacy content (~37 skills with warnings, 28 ruff errors in old quantum scripts).
