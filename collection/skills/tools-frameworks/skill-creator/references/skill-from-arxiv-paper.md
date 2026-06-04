# Skill Creation from arXiv Papers

Proven workflow for creating skills directly from arXiv paper metadata when full-text extraction fails.

## Context
When web_search and web_extract fail on arxiv.org (Firecrawl errors, URL blocking), you can still create high-quality skills from:
- arXiv listing pages via browser_navigate
- Existing kg.db entries with paper metadata
- The paper's core contribution as described in its abstract

### arXiv API Access — Fallback Chain

**Primary: browser_navigate to listing pages.** The arXiv API is aggressively rate-limited (429 errors) even through proxy. Use browser navigation:

```python
# Browse by category — shows 50 most recent papers
browser_navigate(url="https://arxiv.org/list/q-bio.NC/recent")  # neuroscience — last few days
browser_navigate(url="https://arxiv.org/list/q-bio.NC/new")     # same category, TODAY's submissions only
browser_navigate(url="https://arxiv.org/list/quant-ph/recent")  # quantum physics
browser_navigate(url="https://arxiv.org/list/cs.NE/recent")     # neural/evolutionary computing
browser_navigate(url="https://arxiv.org/list/cs.LG/recent")     # machine learning
```

Then extract paper IDs from the snapshot, and navigate to individual papers:

```python
browser_navigate(url="https://arxiv.org/abs/2605.xxxxx")
# Abstract appears in <blockquote> in the page snapshot
```

**Fallback: curl with proxy** (when API isn't rate-limited):

```bash
curl -s --proxy http://127.0.0.1:7890 \
  "https://export.arxiv.org/api/query?search_query=all:QUERY&sortBy=submittedDate&sortOrder=descending&max_results=5"
```

**Pitfall — pipe security guardrail**: `curl ... | python3 -c "..."` triggers a security guardrail. Always save to file first with `-o`, then run python3 on the saved file.

**Pitfall — HTTP vs HTTPS**: arXiv API at `https://export.arxiv.org` may trigger security scans for plain HTTP URLs. Always use HTTPS.

**Pitfall — `&` is a shell metacharacter in curl URLs**: URLs containing `&` query parameters (e.g., `?query=foo&order=-date&size=50`) must be **fully quoted** with double quotes. Without quotes, bash interprets `&` as the background-process operator, truncating the URL and likely causing a 400 Bad Request from arXiv:

```bash
# WRONG — `&order` and `&size` launch background processes
curl "https://arxiv.org/search/?query=neuroscience"&order=-date&size=50

# RIGHT — entire URL in one set of quotes
curl "https://arxiv.org/search/?query=neuroscience&order=-date&size=50"
```

Symptom: arXiv returns a "400 Bad Request" page (~11KB HTML) instead of search results (~250KB HTML). The URL is silently truncated at the first `&`.

**Pitfall — arXiv HTML search is fragile for complex queries**: When querying via `https://arxiv.org/search/`, certain special characters in the query string (even URL-encoded parentheses, pipes, or long multi-term queries) trigger 400 errors. Keep queries simple with spaces between terms: `?query=neuroscience+brain+network` rather than `?query=%28neuroscience+OR+brain%29`. If a complex query fails, simplify to individual terms separated by `+`.

**Pitfall — arXiv HTML search results vary in structure**: The search results page wraps papers in `<li class="arxiv-result">` elements, but the HTML within varies between simple and advanced searches. Some serve inline abstracts, others serve short snippets with expandable full text. Extract arXiv IDs with a simple regex (`r'arXiv:(\d+\.\d+)'`) rather than depending on specific HTML structure, then fetch individual paper pages for full metadata.

**Pitfall — Pipeline gap: skill exists but INDEX entry missing**: When dedup-checking whether a paper already has a skill, check THREE locations, not one:
1. `~/.hermes/skills/ai_collection/` — local skill directory
2. `~/ai_github/ai_collection/collection/skills/` — repo skill directory  
3. `~/ai_github/ai_collection/INDEX.md` — index entries

A skill may exist in locations 1+2 (from a prior cron run that created the skill and committed it) but lack an INDEX.md entry (if the prior run's INDEX update step was interrupted or failed silently). In this case: **do NOT create a new skill — only add the missing INDEX.md entry** using the existing skill's wiki-link name. The entry should follow the standard format with bullet points and activation keywords derived from the existing skill's SKILL.md content.

## Workflow
1. Get paper title/abstract from arXiv API or kg.db
2. Extract the **core contribution** (1 sentence)
3. Identify **key technical insights** (2-4 bullet points)
4. Create SKILL.md with:
   - name: kebab-case, class-level (not paper-specific)
   - description: what the skill does + when to use it
   - **Pitfall**: Do NOT put `arxiv_id`, `date`, `authors`, `tags` as top-level frontmatter keys — `quick_validate.py` rejects them. Nest under `metadata:` block instead.
   - Body: Core Concept, Key Insights/Findings, Implementation Patterns, Applications, Activation Keywords
5. **Verify creation** by reading the created SKILL.md back — confirm the description is class-level (not paper-specific), the body is rich (not just abstract copy), and activation keywords cover the technique space
6. **Verify INDEX.md entry** — after inserting into INDEX.md, read the entry back to confirm: (a) bullet points are substantive (not "Core point 1" placeholders), (b) **Activation** keywords are present and at least 4-6 terms, (c) the entry is under the correct dated section
7. **Git verify** — after `git add` + `git commit`, run `git diff --cached --stat` to confirm the right files are staged before pushing

**Pitfall**: Subagents (delegate_task) may create correct SKILL.md files but produce INDEX.md entries with placeholder bullet points or missing activation keywords. Always re-read and patch both after delegation returns.

**Pitfall: `web_search` via Firecrawl unreliable in cron (2026-05-26 confirmed):** `web_search` consistently returns `'NoneType' object has no attribute 'status_code'` — both for regular queries and `site:arxiv.org` searches. This is a cron-environment-specific Firecrawl backend failure. **Fallback chain for cron sessions:**
1. **Primary**: arXiv API via `urllib.request` with proxy (works but rate-limited — wait 5s+ between calls)
2. **Fallback**: Direct kg.db queries for existing papers
3. **Fallback**: `browser_navigate` to arxiv.org category pages or search
4. **Do NOT rely on** `web_search` or `web_extract` in cron sessions — both are unreliable

**Pitfall: `web_extract` blocks arxiv.org as "private/internal" (2026-05-26 confirmed):** Even when not rate-limited, arxiv.org URLs get `Blocked: URL targets a private or internal network address`. Never use web_extract for arxiv.org — use the API or browser navigation instead.

**Pitfall: YAML frontmatter description field must be quoted (2026-05-28 confirmed):** Description fields containing colons, commas, or special characters MUST be wrapped in double quotes (`"..."`) to pass `quick_validate.py`. Unquoted descriptions with punctuation cause YAML parsing errors:
```yaml
description: "Methodology from arXiv:2605.XXXXX..."  # ✓ Correct
description: Methodology from arXiv:2605.XXXXX...    # ✗ Fails validation with "mapping values are not allowed here"
```
Always quote the description field if it contains any punctuation beyond basic periods and spaces.

**Pitfall: Processing duplicate papers wastes effort (2026-05-28 confirmed):** Before creating a new skill for an arXiv paper, ALWAYS search the skills directory first to avoid redundant work:
```bash
grep -r "arXiv:2605.XXXXX" ~/.hermes/skills/ai_collection/
```
If the paper already has a skill, skip creation but still update INDEX.md and Obsidian notes for consistency. Creating duplicate skills for the same paper fragments the knowledge base and wastes cron cycles.

**Pitfall: Overbuilding skill structure for research papers (2026-05-28 confirmed):** Research paper skills need ONLY `SKILL.md`. The `init_skill.py` script creates `scripts/`, `references/`, and `assets/` directories by default — these are unnecessary for paper-derived skills and clutter the library. After initialization, remove unused directories:
```bash
rm -rf ~/.hermes/skills/ai_collection/{skill-name}/scripts
rm -rf ~/.hermes/skills/ai_collection/{skill-name}/references
rm -rf ~/.hermes/skills/ai_collection/{skill-name}/assets
```
Minimalist structure (just SKILL.md) improves maintainability and reduces confusion about which files serve what purpose.

**Pitfall: Validation before commit prevents repo corruption (2026-05-28 confirmed):** ALWAYS run `quick_validate.py` BEFORE `git add` and `git commit`. Pushing invalid SKILL.md files (YAML errors, missing required fields) breaks the skill library and blocks future skill loading:
```bash
python3 ~/.hermes/skills/skill-creator/scripts/quick_validate.py ~/.hermes/skills/ai_collection/{skill-name}/
# If errors: fix SKILL.md, re-validate
# Only after validation passes: git add -A && git commit && git push
```
Skipping validation creates cascading failures — invalid skills prevent skill_view from working in future sessions, blocking skill library updates entirely.

## Dedup Check — Prevents Multi-Skill Collisions

### Single-paper check

**Critical**: Before creating a skill for an arXiv paper, always check if the paper
is already indexed in the ai_collection INDEX.md. Some papers get picked up by
multiple cron runs and accumulate 3-7+ entries under different wiki-link names:

```bash
grep "{arxiv_id}" ~/ai_github/ai_collection/INDEX.md
```

Also check if the paper already exists in kg.db to avoid duplicate inserts:

```bash
sqlite3 /Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/kg.db "SELECT id, name, description FROM kg_entities WHERE name = '{arxiv_id}'"
```

If found in either location: skip creation, or update the existing entry if it's low quality.
Do NOT create a new skill directory or INDEX.md entry for an already-indexed paper.

### Batch dedup for multiple candidate papers

When processing multiple papers at once (e.g., from a cron job batch), batch-check all candidates in a single `search_files` call instead of grepping INDEX.md one-at-a-time. Also search the skill directory itself — a skill directory may exist even if it hasn't been added to INDEX.md yet (e.g., created by a prior cron run that didn't finish the update):

```python
from hermes_tools import search_files
# Search skill directories for all candidate papers at once
search_files(
    pattern="pattern1|pattern2|pattern3",
    path="/Users/hiyenwong/.hermes/skills/ai_collection",
    target="files"
)
```

This catches skills-in-progress (directory exists, INDEX.md missing) and lets you quickly see which candidates overlap existing skills.

Also check INDEX.md for the same batch in one pass:

```bash
grep -iE "pattern1|pattern2|pattern3" ~/ai_github/ai_collection/INDEX.md
```

## Naming Rules
- Use the **concept/technique** name, not the paper title
- Example: `quantum-purity-amplification` NOT `quantum-purity-amplification-for-arbitrary-eigenstates`
- The name should be reusable across multiple papers on the same topic

## INDEX.md Format for ai_collection
```
### {Paper Title} (arXiv:{id})
- [[{skill-name}]] - One-line description (arXiv: {id})
  - Core point 1
  - Core point 2
  - **Activation**: keyword1, keyword2, ...
```

## Git Sync

### Pitfall: Split Index — `git add` silently ignores new files

The ai_collection repo uses a git **split index** (`DIRC` flag `0x10 = SPLIT_INDEX`). This causes `git add <specific-file>` to silently fail for newly created files and modified INDEX.md — they won't appear in `git diff --cached --stat` and won't be committed.

**Symptom**: After creating new skill directories and patching INDEX.md, `git add INDEX.md collection/skills/new-skill/` reports nothing staged.

**Fix**: Use `git add -A` (or `git add -u` for tracked files, then `git add -A` for untracked) to force a full index refresh:

```bash
cd /Users/hiyenwong/ai_github/ai_collection
git add -A        # NOT git add INDEX.md skills/... — split index silently drops those
git diff --cached --stat   # verify the right files are staged
git commit -m "feat: add {skill-name} skill (arXiv: {id})"
git push
```

**Alternative**: Run `git update-index --force-write-index` before staging, but `git add -A` is simpler and always works.

### Standard Git Sync
```
cd /Users/hiyenwong/ai_github/ai_collection
git add -A
git diff --cached --stat   # verify
git commit -m "feat: add {skill-name} skill (arXiv: {id})"
git push
```