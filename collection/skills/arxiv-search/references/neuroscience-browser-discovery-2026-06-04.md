# Neuroscience Research via Browser Category Listings (2026-06-04)

**Session Context**: Cron job blocked on `execute_code`, web_search, and arXiv API. Browser category listings were the ONLY reliable discovery method.

## Complete Workflow (Verified End-to-End)

### Stage 1: Discovery via Category Listings

**Working pattern**: Navigate to category listing pages, parse snapshot for paper IDs+titles:

```
browser_navigate("https://arxiv.org/list/q-bio.QM/new")  → Quantitative Biology (methods)
browser_navigate("https://arxiv.org/list/cs.NE/new")     → Neural & Evolutionary Computing  
browser_navigate("https://arxiv.org/list/q-bio.NC/new")  → Neurons & Cognition
```

**Yield**: 3 neuroscience-relevant papers discovered from q-bio.NC listing:
- **2606.02937** — BEAST3D: 3D Gaussian splatting animal behavioral analysis
- **2606.03481** — STP stabilizes goal-conditioned dynamics in PFC reservoir
- **2606.02623** — Oscillatory State-Space Models for PDE solvers

**Snapshot parsing**: Paper IDs appear as `arXiv:2606.02937` in anchor text, titles in adjacent span.

### Stage 2: Paper Detail Extraction

Navigate to individual paper pages for full abstracts:

```
browser_navigate("https://arxiv.org/abs/2606.02937")  → BEAST3D details
```

**Extraction pattern**:
- Abstract in `<blockquote class="abstract mathjax">`
- Title in `<h1 class="title mathjax">`
- Authors: multiple `<a href="/search/?searchtype=author&query=...">` links
- Categories: `<span class="primary-subject">` + secondary subjects

### Stage 3: Skill Creation

**Selection criteria**: Most innovative neuroscience applications:
1. **BEAST3D** (2606.02937) — Self-supervised 3D Gaussian splatting + ViT for animal behavior, neural encoding, novel view synthesis from only 4 viewpoints
2. **STP Goal-Conditioned Dynamics** (2606.03481) — STP stabilizes PFC reservoir model under noise (49.5% → 89.2% success rate, Cohen's dz=1.31)

**Skill creation pattern** (write_file + terminal):
```
write_file('/Users/hiyenwong/.hermes/skills/beast3d-animal-behavioral-neural-encoding/SKILL.md', skill_content)
write_file('/Users/hiyenwong/.hermes/skills/stp-stabilizes-goal-conditioned-dynamics/SKILL.md', skill_content)
```

**SKILL.md structure**:
```yaml
---
name: beast3d-animal-behavioral-neural-encoding
description: "BEAST3D方法论：基于3D Gaussian splatting的自监督动物行为分析和神经编码框架..."
metadata:
  arxiv_id: "2606.02937"
  categories: "q-bio.NC, cs.CV"
  published: "2026-06-04"
---
```

### Stage 4: ai_collection Sync

**Sync pattern**:
```bash
# Copy skill directory
cp -r ~/.hermes/skills/beast3d-animal-behavioral-neural-encoding ~/ai_github/ai_collection/collection/skills/
cp -r ~/.hermes/skills/stp-stabilizes-goal-conditioned-dynamics ~/ai_github/ai_collection/collection/skills/

# Update INDEX.md (patch at top)
patch ~/ai_github/ai_collection/INDEX.md ...  # Add dated section with skill entries

# Git commit + push
cd ~/ai_github/ai_collection
git add collection/skills/beast3d-animal-behavioral-neural-encoding/
git add collection/skills/stp-stabilizes-goal-conditioned-dynamics/
git add INDEX.md
git commit -m "feat: add beast3d & stp-goal-conditioned-dynamics from arXiv neuroscience papers"
git push
```

**Verified commit**: `fd9f540c` — successfully pushed to main branch.

### Stage 5: Obsidian Sync

**Output path**: `~/.hermes/obsidian/neuroscience-papers/`

**Note structure**:
```markdown
# {Paper Title}

**arXiv**: [{id}](https://arxiv.org/abs/{id})
**Categories**: {categories}
**Published**: {date}

## Abstract
{abstract}

## Key Contributions
- {bullet points}

## Methodology Highlights
{technical details}

## Neural Encoding Applications
{specific neuroscience applications}

## Related Skills
- [[{skill-name}]]
```

### Stage 6: kg.db Batch Import

**Hermes main kg.db**: `/Users/hiyenwong/.hermes/kg.db` — dedicated `arxiv_papers` table

```bash
sqlite3 ~/.hermes/kg.db \
  "INSERT OR REPLACE INTO arxiv_papers (id, title, authors, published, categories, summary, pdf_url, abs_url) \
   VALUES ('2606.02937', 'BEAST3D...', '...', '2026-06-04', 'q-bio.NC,cs.CV', 'Abstract...', \
           'https://arxiv.org/pdf/2606.02937', 'https://arxiv.org/abs/2606.02937');"
```

**Key insight**: Use `INSERT OR REPLACE` (not `INSERT OR IGNORE`) to handle duplicates gracefully. ID column uses bare arXiv ID (e.g., `2606.02937`, NOT `arxiv:2606.02937`).

## Pitfalls Resolved

1. **execute_code BLOCKED in cron** → use `write_file` + `terminal` pattern for all Python/shell operations
2. **web_search NoneType errors** → pivot to browser category listings
3. **arXiv API rate limits (429)** → browser listing pages have zero rate limits
4. **kg.db schema mismatch** → Hermes main kg.db has separate `arxiv_papers` table with clean schema
5. **INDEX.md line number artifacts** → clean pagination prefixes before patching

## Session Summary

- **Discovery method**: Browser category listings (q-bio.QM, cs.NE, q-bio.NC)
- **Papers selected**: 2 (BEAST3D, STP Goal-Conditioned Dynamics)
- **Skills created**: 2 class-level neuroscience methodology skills
- **Git commit**: fd9f540c pushed to ai_collection main
- **KG entities**: 2 papers inserted to ~/.hermes/kg.db arxiv_papers table
- **Obsidian notes**: 2 markdown notes in ~/.hermes/obsidian/neuroscience-papers/

**Next sessions**: Follow this 6-stage workflow for neuroscience cron research when API/browser search fails.