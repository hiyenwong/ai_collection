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

**Category pages to use:**
- `https://arxiv.org/list/q-bio.NC/recent` - Neurons and Cognition
- `https://arxiv.org/list/cs.NE/recent` - Neural and Evolutionary Computing
- `https://arxiv.org/list/cs.LG/recent` - Machine Learning (broad)
- `https://arxiv.org/list/quant-ph/recent` - Quantum Physics
- `https://arxiv.org/list/stat.ML/recent` - Statistics ML (emerging methods)
- `https://arxiv.org/search/?query=spiking+neural+network&searchtype=all&abstracts=show&order=-announced_date_first&start=0&max=20` - Cross-category keyword search with abstracts (browser-based). **CRITICAL**: Use `max=N` and `start=N`, NOT `size=N`. The `size` parameter returns HTTP 400. Also use `abstracts=show` to include abstracts in results.

**Advantage**: Pre-structured, chronological listings with direct links to PDF and HTML versions — more reliable than API when rate-limited.

**CRITICAL (2026-05-03)**: arXiv `/search/?query=...` browser pages now return **400 Bad Request** even for simple queries. Combined with HTTP 429 rate limits on the API, browser-based search is ALSO unreliable. The ONLY reliable discovery method is direct category page browsing (`/list/{category}/recent`). Do NOT waste time on `/search/?query=...` pages or API queries — go straight to category listing pages.

**CRITICAL (2026-05-02)**: JS extraction on category listing pages (`/list/{category}/recent`) is **UNRELIABLE** — the dt/dd DOM structure produces garbled output due to page structure differences. For category pages, use `browser_snapshot(full=True)` and parse the text output directly — it contains all paper titles, IDs, authors, and subjects in structured text format. Only use JS extraction on `/search/?query=...` pages (the search result page with `li.arxiv-result` elements is stable).

**JS extraction recipe** (for search result pages only, paste into browser_console expression parameter):

For **search result pages** (`/search/?query=...`):
```javascript
(() => {
  const results = document.querySelectorAll('li.arxiv-result');
  const papers = [];
  results.forEach(li => {
    const idEl = li.querySelector('a[href*="abs/"]');
    const id = idEl ? idEl.textContent.trim() : '';
    const allP = li.querySelectorAll('p');
    let title = '', authors = '';
    allP.forEach((p, i) => {
      const t = p.textContent.trim();
      if (i === 0 && !t.startsWith('Authors:') && !t.startsWith('Submitted')) title = t;
      if (t.startsWith('Authors:')) authors = t.replace('Authors:', '').trim().substring(0, 120);
    });
    papers.push({ id, title, authors });
  });
  return JSON.stringify(papers);
})()
```

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

### Step 2: Filter and Select Papers

From the search results:
1. Deduplicate by arXiv ID (papers appear across multiple queries)
2. Cross-reference paper titles against existing skill directory names in `~/.hermes/skills/ai_collection/` — list directories, normalize names (lowercase, strip hyphens), check for substring matches. This catches papers already covered under different naming conventions.
3. Filter to target date range (e.g., papers from the last 24-48 hours)
4. **Coverage Analysis** — Calculate coverage metrics:
   ```python
   # Normalize for matching
   def normalize_for_matching(text):
       stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'using', 'based'}
       words = [w for w in text.lower().replace('-', ' ').replace('_', ' ').split() if w not in stop_words]
       return set(words)
   
   # Check coverage
   for paper in papers:
       title_words = normalize_for_matching(paper['title'])
       matched_skill = None
       for skill in existing_skills:
           skill_words = normalize_for_matching(skill)
           common = title_words & skill_words
           if len(common) >= 2:
               matched_skill = skill
               break
   
   coverage_rate = already_covered / len(papers) * 100
   # >90% = high maturity, >98% = extreme maturity
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
- **Rule of thumb**: If the ai_collection already has 50+ skills in a related domain (e.g., 53+ quantum skills exist), new skills in that domain can go standalone OR to ai_collection. Keep consistency with existing placement patterns.

**CRITICAL: Use `write_file` directly, NOT `delegate_task`** — delegate_task does not reliably create skill files. Direct write_file is the proven approach.

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

**Vault path**: Check `OBSIDIAN_VAULT_PATH` env var, default `/Users/hiyenwong/Documents/Obsidian Vault`

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
1. Daily table row: Insert `| [[daily-note-name|YYYY-MM-DD]] | N | N | themes |` before the closing `|---|` separator or after last data row
2. Thematic section: Add bullet entry under the matching `### Theme Name` section with wikilink to daily note
3. Latest Skills section: Add `#### skill-name` header + summary entry at the end of the file

**MOC structure** (typical 213-line file, ~15.6KB):
- Lines 1-5: Frontmatter
- Lines 7-9: Title
- Lines 11-25: Daily Research Notes table
- Lines 27-199: Research Themes sections
- Lines 201+: Latest Skills section

## Key Learnings (from production runs)

### Tool Selection
- **web_search** as FIRST-PASS discovery (updated 2026-05-04): When both arXiv API and browser navigation return 429 rate limits, `web_search` with targeted queries (e.g., "arxiv quantum computing 2025 2026 breakthrough") can surface paper titles, IDs, and abstracts from Google indexing. This is a viable fallback when all direct arXiv access methods are blocked.
- **write_file** for skill creation at `~/.hermes/skills/<skill-name>/SKILL.md` — reliable, direct
- **execute_code** for Obsidian vault manipulation — Python's string operations handle markdown cleanly
- **terminal** for file discovery, reading existing content, and git operations
- **web_search** for initial paper discovery — broad results from Google/arXiv/other sources, useful first-pass filter before deeper arXiv scraping
- **web_extract** for arXiv content — NOTE: Returns "Blocked: URL targets a private or internal network" for many arXiv URLs (new failure mode observed 2026-05). Also returns empty content for `/abs/` URLs. When web_extract fails, fall back to browser navigation
- **browser_navigate + browser_snapshot + browser_console** for arXiv scraping — browser_console with JavaScript extraction (`document.querySelectorAll('li.arxiv-result')`) is effective for parsing structured paper data (titles, authors, abstracts, dates) from arXiv search result pages
- **cp -r with mkdir -p** for syncing skills to ai_collection — cp -r silently fails on some directories; always `mkdir -p` target first

### Common Pitfalls
1. **delegate_task for skill creation**: Does NOT work reliably — use `skill_manage(action="create")` (preferred, auto-creates directories) or `write_file` directly
2. **arXiv rate limits**: Worsened significantly (2026-04 observed). Use 5s delays between queries, reduce `max_results` to 15, add `User-Agent` header, 60s timeout, SSL verification disabled. Some query patterns permanently fail (429) — implement 3 retries with 10s exponential backoff. If first query fails, remaining queries may still succeed
3. **web_extract "Blocked" error**: `web_extract` consistently returns "Blocked: URL targets a private or internal network" for arXiv URLs since 2026-05. This is a new failure mode beyond rate limits. When this happens, use `browser_navigate` + `browser_snapshot` + `browser_console` (JS extraction) instead — this is the most reliable method for arXiv content
3. **`httpx` in `execute_code` returns empty responses**: `httpx.get()` against arXiv API from within `execute_code` sandbox can return 0-byte responses (no error, just empty). Observed 2026-05-02. Fallback chain: `web_search` for discovery → `terminal` + `curl` with HTTPS for full XML parsing. Never trust `httpx` response length < 100 for arXiv API.
4. **curl requires HTTPS for arXiv API**: Terminal `curl` to `http://export.arxiv.org/api/query` triggers security scan approval prompt. Always use `https://export.arxiv.org/api/query` to avoid interactive approval blocking cron jobs.
3. **Deduplication**: Papers appear in multiple keyword searches; dedupe by arXiv ID
4. **execute_code state persistence**: State does NOT persist between `execute_code` calls. Save intermediate data to `/tmp/` files (e.g., `papers_data.json`, `paper_details.json`) and reload in subsequent calls. Without this, accumulated search results will be lost between steps.
4. **Vault path**: Always check env var first; don't hardcode
5. **Session naming**: Use time-of-day suffix when running multiple sessions per day
6. **Existing skills**: Always check before creating — some papers were already covered. Use `ls ~/.hermes/skills/ai_collection/` and normalize names for coverage detection
7. **INDEX.md corruption**: INDEX.md can silently corrupt during writes — if line count looks wrong, rebuild from filesystem using `find ~/.hermes/skills/ai_collection -maxdepth 1 -type d | sort` and filter to dirs with SKILL.md
8. **`read_file` unreliability**: Hermes `read_file` returns double-numbered lines (`     1|     1|content`) — unreliable for parsing. Use Python `open()` directly for file content manipulation
9. **Cron execution pattern**: When running as scheduled job, use `execute_code` with Python (not terminal+curl) for better reliability. Save state to `/tmp/` between steps. Handle partial failures gracefully — if some queries fail, continue with successful ones.
10. **MOC patching requires 3 separate operations**: (1) Daily table row insertion, (2) Thematic section bullet addition, (3) Latest Skills section header+summary append. Each requires reading current content and precise positioning.
11. **Mature collection adaptation**: When >90% papers have existing skills (typical after 90+ skills), expand keyword scope or add new domains rather than expecting many new skills per session.
12. **Date filtering**: Papers returned may have dates in the future relative to system time. Use flexible date ranges (30 days) and sort by published date to get truly recent papers.
13. **Empty search results**: If queries return 0 papers in target date range, expand search to all recent papers regardless of date and filter post-hoc.
14. **Leverage cached search results**: Previous cron runs may have saved papers to `/tmp/` files (e.g., `/tmp/arxiv_papers.json`, `/tmp/neuro_papers_v3.json`). If arXiv API is rate-limited or failing, scan `/tmp/*.json` for existing paper data before attempting new queries — this can save significant time and avoid API blocks.
15. **Coverage detection via title normalization**: When checking if papers are already covered, normalize both paper titles AND skill names by removing punctuation, lowercasing, and splitting into word sets. Check for intersection of 2+ common words between title and skill name for robust matching across naming conventions.
16. **Paper scoring for selection**: Implement relevance scoring based on keyword frequency weighted by importance. Example scoring for neuroscience:
    ```python
    keywords = {'spiking neural network': 5, 'brain network': 4, 'neural dynamics': 4}
    score = sum(text.count(kw) * weight for kw, weight in keywords.items())
    ```
    This helps prioritize high-value papers when collection is mature.
17. **Standalone-to-ai_collection sync**: Skills may exist as standalone directories in `~/.hermes/skills/` but not yet in `ai_collection/`. Check both locations. Use `shutil.copytree()` to sync. The INDEX.md entry may reference a standalone skill that hasn't been copied to ai_collection yet.
18. **Skip evaluation criteria**: At high coverage rates (85%+), not every uncovered paper warrants a skill. Skip papers that are: (a) too narrow/specific (e.g., single-dataset validation), (b) conceptually overlapping with existing skills (e.g., new Hamiltonian method when energy-based/physics-guided skills exist), (c) review/perspective papers with no extractable methodology, (d) **optimization algorithms without neuroscience methodology** (e.g., CMA-ES variants like RCMAES, ensemble optimization like MAEO, genetic algorithm benchmarks). Document skip reasons in the daily research note.

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
- **Extreme maturity signal**: When >98% coverage achieved, focus exclusively on interdisciplinary boundaries and emerging research directions at the intersection of covered domains
- **Ultra-mature phase** (500+ skills): At this scale, nearly ALL papers in core neuroscience categories (q-bio.NC, cs.NE) are already covered. The primary value extraction activities are:
  1. **Standalone-to-ai_collection sync** (batch of 25-30 per session) — check for standalone neuroscience skills not yet copied to ai_collection
  2. **Skip evaluation** — filter out non-methodology papers (optimization algorithms, hardware tools, review-only papers)
  3. **Cross-domain monitoring** — watch cs.LG, stat.ML, and other adjacent categories for interdisciplinary breakthroughs
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

**Authoritative counting**: Use Python for definitive skill count:
```python
count = sum(1 for item in os.listdir(skill_dir)
            if os.path.isdir(os.path.join(skill_dir, item))
            and os.path.exists(os.path.join(skill_dir, item, "SKILL.md")))
```

### Coverage Rate Variability

Coverage rate is NOT monotonically increasing. At 233+ skills, coverage dropped to 60% because:
- Collection expanded into adjacent domains (emotion energy, receptive field geometry, neuro-symbolic AI)
- New keyword combinations surface papers from domains not yet well-covered
- **Don't assume high coverage** — always compute fresh per session
- When coverage drops below 70%, collection is actively expanding into new domains — healthy growth, not regression

### New Session Examples

*2026-05-02 cron v2*: 21 papers scanned across 4 domains (brain network, neural dynamics, SNN, computational neuroscience), 86% coverage (18/21), 0 new skills created, 1 synced (`geometric-brain-dynamics-mapping-v7` from standalone to ai_collection). Key workflow: `execute_code` with `httpx` returned empty responses for arXiv API → fallback to `web_search` for discovery → `terminal` with `curl` + HTTPS for full XML parsing → Python dedup/skill coverage check → `shutil.copytree` for standalone-to-ai_collection sync → patch Obsidian wiki. 3 papers skipped: too narrow (JASTAP), conceptually overlapping (Hamiltonian brain dynamics), review-only (linguistics). Demonstrates that at 255 skills, sync and skip decisions become as important as creation. Key learning: `httpx` in `execute_code` sandbox can return 0-byte responses for arXiv API even with HTTPS — use `web_search` as first pass, then `terminal` + `curl` for reliable XML retrieval.

*2026-05-02 early cron*: 24 papers scanned (q-bio.NC + cs.NE categories + API), 92% coverage (22/24), 2 new skills created (dimensionality-modularity-continual-learning, attractor-fcm-gradient-descent). Demonstrates that even at 240 skills, valuable skills emerge from interdisciplinary boundaries (continual learning architecture analysis, attractor-based FCMs). Coverage remained high despite expanding into adjacent domains.

*2026-05-02 cron*: 9 skills created from ~200 arXiv results (neuroscience, brain network, neural dynamics, SNN, computational neuroscience). Key workflow: web_search for initial discovery → browser_navigate + browser_console JS extraction for arXiv scraping → write_file for skill creation at `~/.hermes/skills/<name>/` → mkdir -p + cp for sync to `~/ai_collection/collection/skills/` → Obsidian wiki update. Notable papers: brain foundation model inversion (SBI), AFR-Net flow routing, HoloBrain/HoloGraph oscillatory GNNs, SWpC directed FC, GeoDynamics SPD manifold, NH-GCAT depression diagnosis, sparse connectivity recovery, LuminaNet BNN, JEDI dynamics inference. Key learning: `web_extract` consistently returns "Blocked" for arXiv URLs; browser-based scraping via browser_console is most reliable.

*2026-05-02 evening cron v2*: 32 papers scanned (q-bio.NC + cs.NE categories), 90.6% coverage (29/32), 0 new skills created, 1 synced (`geometry-aware-spiking-gnn` from standalone to ai_collection). 3 papers skipped: hardware tool (earable platform), optimization algorithms (CMA-ES, MAEO). Key learning: JS extraction on category listing pages produces garbled output — use `browser_snapshot(full=True)` text parsing instead. At 324 ai_collection skills, standalone-to-ai_collection sync and skip evaluation are as important as new skill creation.

*2026-05-03 morning cron*: 12 papers scanned (q-bio.NC + cs.NE browser + 9 API queries), 83.3% coverage (10/12), 0 new skills, 10 synced to ai_collection (standalone neuroscience batch). 2 papers skipped: optimization algorithms (RCMAES, MAEO). Key finding: 4 of 9 `curl` API queries returned 0-byte responses (empty XML, no HTTP error) — `execute_code` + `curl` against arXiv is increasingly unreliable. Browser category page scraping (`/list/{category}/recent`) remains the most reliable discovery method. At 337 skills, standalone-to-ai_collection sync (~130 pending neuroscience skills) is now the primary value extraction activity alongside new paper monitoring.

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

After completing the workflow:
1. Count new skill directories in `~/.hermes/skills/ai_collection/`
2. Verify INDEX.md skill count matches actual files
3. Check MOC has the new session entry
4. Confirm daily research note exists and is complete
5. Present summary to user with: scan stats, new skills table, skipped papers, key trends
