---
name: repository-migration-workflow
description: "Systematic workflow for repository reorganization when structure limits are hit (GitHub 1000-entry truncation, directory bloat). Covers problem identification, domain-based classification, git history preservation, and migration execution. Use when: (1) GitHub shows truncation warning in directory listings, (2) Flat directory exceeds organizational limits, (3) Need to restructure repository while preserving git history, (4) Moving large numbers of files/directories in a repo. Activation: repository migration, git mv large scale, directory reorganization, GitHub truncation, domain-based split"
license: Complete terms in LICENSE.txt
---

# Repository Migration Workflow

Systematic approach for repository reorganization when structural limits are encountered.

## Problem Pattern

GitHub displays **max 1000 entries per directory** in web view. When a directory exceeds this limit (e.g., `collection/skills/` with 1844 directories), 839+ entries are omitted from listings, breaking discoverability.

**Signal**: GitHub web view shows "Sorry, we had to truncate this directory to 1,000 files. X entries were omitted."

## Workflow

### Step 1: Problem Assessment

Check actual entry count vs limit:

```bash
find <directory> -type d | wc -l  # directory count
find <directory> -type f | wc -l  # file count
```

If count > 1000, reorganization needed.

### Step 2: Classification Strategy Selection

**Preferred approach**: Domain-based classification

- Creates semantic groupings that aid discoverability
- Users can navigate by topic rather than arbitrary alphabetical chunks
- Future additions follow natural categorization

**Alternative approaches** (use only when domain classification fails):
- Alphabetical split (A-F, G-M, N-Z)
- Hybrid (domain first, then alphabetical for large domains)

**Avoid**: Flat migration to another location without classification — same problem recurs.

### Step 3: Domain Classification

Create classification script that:

1. Scans all entries to classify
2. Uses keyword matching against entry names
3. Assigns to predefined domain categories
4. Tracks "other" category for unclassifiable entries
5. Generates migration plan JSON

**Example domains** (adjust to your repo):
- neuroscience (keywords: brain, neural, spike, EEG, fMRI)
- quantum (keywords: quantum, QNN, QAOA, VQE)
- ai-ml (keywords: machine-learning, deep-learning, transformer, neural-network)
- systems-engineering (keywords: control, CPS, MPC, distributed)
- math-statistics (keywords: theorem, proof, algebra, statistical)
- finance (keywords: portfolio, trading, stock, market)
- medical (keywords: diagnosis, imaging, clinical, healthcare)
- tools-frameworks (keywords: docker, python, framework, tool)
- control-systems (keywords: feedback, stability, robust)
- other (fallback)

**Output**: `migration_plan.json` with structure:
```json
[
  {"name": "skill1", "domain": "neuroscience"},
  {"name": "skill2", "domain": "quantum"},
  ...
]
```

### Step 4: Migration Execution

Create migration script that:

1. Reads migration plan JSON
2. Creates domain subdirectories: `mkdir -p <base>/<domain>/`
3. Uses `git mv` for each entry (preserves history)
4. Tracks per-domain counts
5. Logs all moves for audit

**Critical**: Must use `git mv`, NOT `mv` + `git add`. Git history preservation requires the move operation to be tracked as a rename.

**Pattern**:
```python
for entry in migration_plan:
    domain = entry['domain']
    source = f"{base_dir}/{entry['name']}"
    dest = f"{base_dir}/{domain}/{entry['name']}"
    subprocess.run(["git", "mv", source, dest], check=True)
```

### Step 5: Verification

After migration completes:

```bash
ls -la <base>/           # Should show domain directories only
ls <base>/<domain>/      # Verify entries moved correctly
find <base>/<domain>/ -type d | wc -l  # Count per domain (must be ≤1000)
git status               # Check unstaged changes (all 'renamed:' entries)
```

### Step 6: Commit and Push

User executes commit manually (agent cannot push without credentials):

```bash
git add -A
git commit -m "Reorganize <directory> by domain to fix GitHub truncation"
git push origin main
```

**Verification on GitHub**: Navigate to `<base>/<domain>/` in web view — should show ALL entries without truncation warning.

## Pitfalls

- **`mv` instead of `git mv`**: Breaks history — file appears as deleted + added, losing rename tracking
- **Direct push to main blocked**: The ai_collection repository (and many others) have branch protection rules requiring pull requests. `git push origin main` will fail with "Changes must be made through a pull request". Always push to a feature branch and create a PR: `git checkout -b feat/add-skill-name && git push origin feat/add-skill-name`
- **Domain imbalance**: One domain may still exceed 1000 (e.g., neuroscience: 773 is safe, but 1500+ would need further split)
- **Orphaned entries**: Check for entries not in migration plan (should go to 'other' domain)
- **Path collisions**: Ensure dest directory doesn't already exist before `git mv`

## Scripts

This skill includes reusable templates:

- **`scripts/classify_entries_by_domain.py`** — Domain classification script with keyword matching. Customize DOMAIN_KEYWORDS dict for your repo. Generates `migration_plan.json`.

- **`scripts/migrate_by_domain.py`** — Migration execution script using `git mv`. Reads plan JSON, creates domain directories, executes moves with progress tracking.

Usage pattern:
```bash
# Step 1: Classify
python scripts/classify_entries_by_domain.py collection/skills/

# Step 2: Review plan
cat migration_plan.json

# Step 3: Execute (after user confirms)
python scripts/migrate_by_domain.py collection/skills/ --plan migration_plan.json
```

## References

- `references/github-truncation-case-study.md` — Full case study from ai_collection migration (1844 skills, domain classification, lessons learned)
- GitHub 1000-entry limit: Official GitHub limitation for web directory listings
- Git rename tracking: `git mv` preserves blob history, shows as rename in diff