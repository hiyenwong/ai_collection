---
name: shortcut-sensitivity-in-agent-safety-evaluations
description: "Shortcut Sensitivity in Agent-Safety Evaluations..."
tags: [cs.AI, cs.CR, cs.LG]
source: arxiv
arxiv_id: 2610.22243v1
utility: 0.86
published: 2026-10-15
---

# Shortcut Sensitivity in Agent-Safety Evaluations

**Authors:** Hasan Demirkiran, Jens Ernstberger
**Published:** 2026-10-15
**arXiv:** [2610.22243v1](https://arxiv.org/abs/2610.22243v1)
**Categories:** cs.AI, cs.CR, cs.LG
**Utility Score:** 0.86

## Abstract

AI agents take actions through tools. Some actions are sensitive, so guards that supervise them must themselves be evaluated reliably. Yet the data used to evaluate a guard can include cues that make labels predictable without measuring the intended safety construct, and those cues can also influence guard decisions. We introduce a three-level shortcut-auditing framework and audit completed LinuxArena trajectories and two TS-Bench-derived step datasets. We distinguish label predictability, observational guard association, and paired decision sensitivity. In LinuxArena, shorter average shell commands strongly predict trajectory labels. In AgentDojo-Traj, exact-tool lookup falls from F_1=.901 with mixed-domain folds to .495 under domain holdout. In AgentHarm-Traj, released TS-Guard F_1 falls from .902 under row weighting to .719 with equal interaction weighting, while balanced accuracy rises. We then test the strongest safe-row marker association in a seven-configuration screen on a frozen 64-step AgentDojo-Traj cohort using repeated, interleaved Haiku calls. Rewriting the <INFORMATION> marker lowers blocking by 8.33 percentage points, while opaque tool aliases raise it by 11.46 points. All unsafe calls remain blocked; the changes concern false positives against inherited labels. Both effects remain nonzero after subtracting the formatting-placebo effect, with exploratory 95% ranges excluding zero. The same edits also change measured accuracy against inherited labels. This prov

## Key Contributions

- Novel research in cs.AI, cs.CR
- Published 2026-10-15

## Activation

shortcut, sensitivity, agentsafety, evaluations
