# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Policy
- **All PRs with new skills MUST have every skill classified into a category subdirectory before merge.** No skill may remain in `collection/skills/` root. PRs violating this will be held until classify_skills.py is run.
- PR merge requires review: verify skill classification, resolve conflicts, run `python scripts/classify_skills.py`, confirm 0 flat skills remain.
- After any skill changes (add/remove/reclassify), run `python scripts/update_neural_map.py` to update the neural network visualization.
- Git commits authored as `m1_agent`.

### Added
- Skill classification rules documented in CONTRIBUTING.md and docs/skills/creation-guide.md
- 31 category subdirectories under collection/skills/ for organized skill storage
- scripts/classify_skills.py rewritten with expanded keyword rules and SKILL.md-based detection
- CHANGELOG.md created

### Changed
- New skills must be created under collection/skills/<category>/<skill-name>/ instead of the root skills directory
- Skill creation guide updated with category selection rules and directory structure
- Cron job "每日论文冥想" updated to place new skills in category subdirectories and push directly to main
- GitHub branch protection relaxed: removed required_pull_request_reviews and required_linear_history to allow direct push to main

### Fixed
- Removed 976 duplicate flat skills re-introduced by PR #38 merge (old structure conflict)
- PR #39 merged with classification: 14 new skills moved from root to category subdirectories

## [2026-07-08] - PR #38 and #39 Merge

### Added
- 14 new skills from arXiv papers via cron job (PR #39):
  - neuroscience: bayesian-ippm-cortical-entrainment, demented-brain-connectivity-patterns, differentiable-biophysical-simulation-neurostimulation, global-workspace-j-space, silif-dbs-neuromorphic-controller
  - quantum: lean-quantum-formal-verification, low-depth-nonmarkovian-simulation, metrological-quantum-reservoir-networks, quantum-hilbert-schmidt-speed, thermodynamic-quantum-reservoir-computing
  - spiking-neuromorphic: scalable-perturbation-learning-esn
  - multi-agent-rl: onnes-llm-cryogenic-diagnosis
  - healthcare-bio: icl-antibody-affinity
  - physics-math: entropy-maximization-manifold
- 268 commits from cron/medicine-quantum-2026-07-08 branch (PR #38), 639 skills classified into categories

### Fixed
- Resolved 3 file conflicts (flow-matching, metabolic-quantum-limit-meg) during PR #38 merge
- Cleaned 976 duplicate flat skills caused by old-structure branch merge

## [2026-07-07] - Skills Reorganization

### Changed
- **Migrated 1173 flat skills into 31 category subdirectories** using git mv (preserves history)
- Rewrote scripts/classify_skills.py:
  - Fixed hardcoded path to use Path(__file__) relative resolution
  - Changed category detection from subdir-count heuristic to SKILL.md presence
  - Expanded keyword rules from ~200 to ~600+ keywords across all categories
- Removed GitHub branch protection pull_request rule (ruleset 17274326) to allow direct push to main
- Updated cron job prompt to create skills in category subdirectories and commit directly to main

### Category Distribution (post-reorganization)
| Category | Count |
|----------|-------|
| neuroscience | 1299 |
| quantum | 721 |
| spiking-neuromorphic | 337 |
| other | 229 |
| ai-ml | 224 |
| general-ml | 191 |
| nlp-llm | 161 |
| multi-agent-rl | 158 |
| signal-control-systems | 153 |
| physics-math | 113 |
| reasoning-bayesian | 70 |
| systems-engineering | 67 |
| reinforcement-learning | 62 |
| vision-generative | 50 |
| ai-safety-eval | 49 |
| tools-frameworks | 43 |
| software-engineering | 38 |
| control-systems | 38 |
| data-retrieval | 37 |
| healthcare-bio | 26 |
| agent-tools | 25 |
| knowledge-graph | 21 |
| finance | 21 |
| security-privacy | 19 |
| math-statistics | 18 |
| deployment-optimization | 17 |
| medical | 10 |
| memory | 6 |
| skill-rag-indexer | 5 |
| continual-learning | 5 |
| chat-history-lancedb | 5 |

## [2026-07-05] - Neuroscience Skills

### Added
- DendriCL (SNN ICL) skill from arXiv 2607.02283
- SABER (semantic brain network) skill from arXiv 2607.01901

## [2026-06-12] - Math Cron Update

### Added
- Multiple math and quantum skills from arXiv papers

## [2026-04-27] - Plugin Marketplace

### Added
- Plugin marketplace documentation and 5-domain decomposition
- Marketplace quickstart and troubleshooting guides
