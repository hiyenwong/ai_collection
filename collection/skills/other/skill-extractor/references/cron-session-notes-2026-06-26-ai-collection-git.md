# ai_collection Git Workflow — Cron Session Notes (2026-06-26)

## PR Protection Rules Discovered
The ai_collection repo enforces branch protection rules on `main`:
- **No merge commits** on main (GH013 error)
- **Changes must be made through a pull request**
- Direct `git push origin main` is rejected with `push declined due to repository rule violations`

## Working Pattern for Cron Push
When direct push to main is blocked:
```
cd /Users/hiyenwong/ai_github/ai_collection
# Create a feature branch for the cron changes
git checkout -b cron-{topic}-{date}
# ... make changes, commit ...
git push origin cron-{topic}-{date}
# PR URL will be shown by GitHub
# Then manually create PR from that URL
```

## Merge Conflict Resolution on Diverged Branch
When cron branch is hundreds of commits behind main and has merge conflicts:
- `git pull --rebase` produces massive conflict chain (400+ commits to replay)
- `git checkout --ours <conflicted_file>` resolves by keeping local version
- After resolving all conflicts, commit and push to a new feature branch
- Alternative: `git reset --hard origin/main` to start fresh, then re-apply changes

## Domain Saturation Update (2026-06-26)
- Number Theory + Quantum: ~40-50% (still productive — 2 new skills from 5 new papers)
- Statistics + Quantum: ~65%
- Tensor network methods remain under-represented — high-value territory

## New Overlap Alert
- `iqp-connectivity-trainability` (2606.24264) — related to existing `qiqp-trainability-analysis` (IQP Born Machines) and `qml-expressivity-trainability`. All in the VQA/IQP trainability space. Candidate for future cross-referencing or consolidation under `quantum-circuit-trainability` umbrella.
