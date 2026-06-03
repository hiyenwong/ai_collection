# ai_collection CI Validation Rules

Source: `scripts/validate_skill.py` in the ai_collection repo.

## Validation Categories

### 1. Skill Validation (`validate-skills` job)
Runs `python scripts/validate_skill.py` which checks all SKILL.md files.

#### Standard Skills Required Sections:
```
# Skill Name
## Description
## Activation Keywords
## Tools Used
## Instructions for Agents
## Examples
```

#### Paper-Based Skills (relaxed validation):
Detected by any of these indicators in content:
- `arXiv ID:` or `**arXiv ID:**`
- `## Abstract` or `## Key Contributions` or `## Core Contributions`
- `arxiv.org` URL
- `source_paper:` frontmatter key
- `触发词:` (Chinese activation keywords)
- `references:` frontmatter key
- `核心论点` or `核心贡献`

Paper skills still require:
- **`description` in YAML frontmatter** (this is NOT optional)
- **`**arXiv ID:**` or `arXiv ID:` text** in body
- **`## Abstract` or `## Key Contributions`** section

#### Common Warnings (non-fatal):
- Line length > 120 characters
- Uncommon tool names (empty strings `''`)
- Missing code blocks in examples
- Examples not showing `User:` / `Agent:` interactions

### 2. Markdown Links (`lychee` job)
Checks all markdown links with lychee.

#### Excluded patterns (from workflow):
- `github\.com`
- `docs\.openclaw\.ai`
- `discord\.gg`
- `api\.star-history\.com`
- `openai\.com`
- `collection/` and `knowledge/` paths

#### NOT excluded (will fail):
- `arxiv.org` URLs — lychee may flag these if arxiv returns non-200
- Other external academic URLs

### 3. Python Linting (`lint-python` job)
Runs `ruff check` and `ruff format --check` on `collection/` and `scripts/`.

#### Known pre-existing failures (as of 2026-05-04):
- `kg-research-workflow/scripts/kg_workflow.py` — unused variable
- `quantum-medical-imaging/scripts/extract_paper_insights.py` — bare except, f-string
- `quantum-ml-data-loading/scripts/encoding_utils.py` — unused imports
- `quantum-neural-architecture-search/scripts/build_supercircuit.py` — unused imports
- Many other scripts with similar issues

**These are NOT caused by new skill additions** — they exist in the repo before any new commits. The lint failure is a pre-existing condition.

### 4. Project Structure (`check-structure` job)
Checks directory structure consistency. Generally passes for valid skill additions.

### 5. Spell Check (`spell-check` job)
Spell checks documentation. Generally passes for technical content.

## Known CI Issues

### Node.js 20 Deprecation Warning
The workflow uses `actions/checkout@v4` which runs on Node.js 20. GitHub will force Node.js 24 starting June 2, 2026. This generates warnings but does NOT cause failures.

### Pre-existing Lint Errors
The `lint-python` job has been failing consistently due to pre-existing ruff errors in older scripts. This is NOT caused by new skill additions. New skills that are markdown-only will not trigger additional lint errors.

## Validation Checklist for New Skills

- [ ] `description` field in YAML frontmatter
- [ ] `**arXiv ID:**` format in body (for paper skills)
- [ ] `## Abstract` section
- [ ] `## Key Contributions` section
- [ ] No line > 120 characters
- [ ] File in `collection/skills/<name>/SKILL.md`
- [ ] Valid YAML frontmatter (use `---` delimiters)
- [ ] No bare except, unused imports, or other ruff violations (for Python scripts)

## Local Validation Command
```bash
cd /Users/hiyenwong/ai_github/ai_collection
python scripts/validate_skill.py --skill <skill-name>
```
