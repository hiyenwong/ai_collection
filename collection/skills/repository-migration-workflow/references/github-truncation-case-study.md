# GitHub Truncation Case Study

Session: 2026-06-04
Repository: hiyenwong/ai_collection
Issue: collection/skills/ (1844 directories) exceeds GitHub 1000-entry limit

## Problem Manifestation

GitHub web view showed:
```
Sorry, we had to truncate this directory to 1,000 files.
839 entries were omitted from the list.
Latest commit info may be omitted.
```

**Root cause**: GitHub's web UI hard limit of 1000 entries per directory for performance reasons. Affects:
- Directory listings
- File browsing
- Commit file lists
- API pagination

**Impact**: 839 skills invisible in web view → users cannot discover skills via GitHub interface.

## Solution Applied

### Domain-Based Classification

**Classification script output**:
```
Total entries: 1844

Domain distribution:
  neuroscience: 773
  other: 409
  quantum: 353
  ai-ml: 133
  systems-engineering: 74
  math-statistics: 47
  finance: 16
  medical: 14
  tools-frameworks: 14
  control-systems: 11
```

**Result**: All domains ≤ 773 entries (well within 1000 limit).

### Migration Execution

```bash
python scripts/migrate_by_domain.py collection/skills/
```

Output:
- 10 domain directories created: `ai-ml/`, `control-systems/`, `finance/`, etc.
- All 1844 skills moved using `git mv`
- 0 failures, 100% success rate
- Git working directory: 1844 unstaged 'renamed:' entries

### User Commit Required

Agent cannot push without credentials. User must execute:
```bash
git add -A
git commit -m "Reorganize skills by domain to fix GitHub truncation issue"
git push origin main
```

## Lessons Learned

### Domain Distribution Imbalance

**neuroscience dominates** (773/1844 = 42%). This reflects research focus but risks future truncation if domain grows beyond 1000.

**Mitigation strategies**:
1. Alphabetical sub-split within neuroscience (e.g., `neuroscience/A-M/`, `neuroscience/N-Z/`)
2. Topic-based sub-categories (e.g., `neuroscience/eeg/`, `neuroscience/fmri/`)
3. Monitor domain growth via cron script that alerts when domain approaches threshold

### "Other" Category Size

409 entries classified as "other" (22%). This indicates:
- Keyword coverage gaps
- Emerging domains not yet in classification config
- Niche topics with ambiguous classification

**Action**: Review "other" entries periodically, refine keywords, or create new domains.

### Keyword Matching Simplicity

Classification used **simple substring matching**. More sophisticated approaches:
- Multi-keyword scoring (require 2+ matches)
- Weighted keywords (domain-specific weights)
- LLM-based classification (semantic understanding)
- Manual expert labeling (for ambiguous cases)

For this session, simple matching was sufficient. Consider advanced methods if "other" category grows large.

### Git History Preservation

All moves used `git mv`, confirmed by `git status` showing "renamed:" entries. This ensures:
- File blob history preserved
- Blame/authorship tracked across moves
- Merge/rebase handles renames correctly
- GitHub diff shows as rename (not delete+add)

**Critical**: NEVER use `mv` + `git add` for large migrations — breaks history.

## Verification Checklist

After migration, verify:

1. **Local structure**: `ls collection/skills/` → shows 10 domains only
2. **Entry counts**: `find collection/skills/<domain>/ -type d | wc -l` → ≤ 1000
3. **Git status**: All entries show as "renamed:" (not "new file:")
4. **GitHub web view**: Navigate to domain, verify NO truncation warning

## Follow-Up Actions

1. Update INDEX.md to reflect new domain structure (references skill paths)
2. Update AGENTS.md if agent references use old flat paths
3. Monitor domain growth via script that alerts when approaching threshold
4. Review "other" category monthly, refine classification keywords
5. Document domain taxonomy in repo docs for contributor guidance

## Alternative Approaches Considered

### Alphabetical Split

Rejected because:
- Creates arbitrary groupings (A-F, G-M, N-Z)
- No semantic meaning → users must search across multiple alphabetic dirs
- Future additions require calculating which bucket
- Hard to explain why skill is in "G-M" vs "N-Z"

### Hybrid (Domain + Alphabetical)

Rejected because:
- Over-engineering for current state
- Neuroscience (773) still within 1000 limit
- Only needed if single domain exceeds threshold
- Can add alphabetic sub-split later if needed

### External Storage (Git Submodule)

Rejected because:
- Requires external hosting (new repo, new overhead)
- Breaks single-repo simplicity
- Users need submodule init/update
- Doesn't solve root problem (directory still flat in submodule)

**Decision**: Domain-based reorganization is simplest, semantic, and sufficient.