# Pending Cleanup

## Duplicate Skill: zero-shot-kinematic-bci-decoding

Accidentally created during 2026-05-20 neuroscience cron job. The existing skill `kinematic-zero-shot-bci-decoding` already covers the exact same paper (arXiv: 2605.19048).

**What was done:**
- Deleted from `~/.hermes/skills/ai_collection/zero-shot-kinematic-bci-decoding/` ✅
- Still exists in git repo at `~/ai_github/ai_collection/collection/skills/zero-shot-kinematic-bci-decoding/` (commit 7cb887d)

**Cleanup needed:**
```bash
# 1. Remove duplicate directory
rm -rf ~/ai_github/ai_collection/collection/skills/zero-shot-kinematic-bci-decoding/

# 2. Remove duplicate entry from INDEX.md
# Delete lines referencing "zero-shot-kinematic-bci-decoding" under "## 2026-05-20 - Neuroscience Research"

# 3. Commit and push
cd ~/ai_github/ai_collection
git add -A
git commit -m "fix: remove duplicate zero-shot-kinematic-bci-decoding (consolidated into kinematic-zero-shot-bci-decoding)"
git push
```
