---
name: auditable-deployable-multi-agent-motion-planning
description: "Auditable and Deployable Multi-Agent Motion Planning via Posetal Games from Lega"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22277"
utility: 0.96
date: "2026-10-17"
---

# Auditable and Deployable Multi-Agent Motion Planning via Posetal Games from Legal Guidelines

**arXiv:** [2610.22277](https://arxiv.org/abs/2610.22277)
**Authors:** Florian Lercher, Karan Mahesh, Yujun Huang, Meshal Alharbi, Runyu Zhang...
**Published:** 2026-10-15
**Categories:** cs.MA, cs.GT, cs.RO, eess.SY
**Utility Score:** 0.96

## Abstract

When robots are deployed in the real-world, they must interact with other agents and accomplish their own goals while adhering to legal constraints. These potentially conflicting objectives are often only partially prioritized, making scalarized objectives or fully specified hierarchies unsuitable. We present a framework for multi-agent motion planning under legal requirements based on games with partially ordered preferences (posetal games). Scenario-independent legal guidelines order abstract legal concerns, from which we automatically derive agent preferences and a legal game for any concrete scenario. Agents may refine their legal preferences with private objectives, and regulators may refine the guideline as laws evolve. We prove that such customizations can only remove equilibria and thus preserve legality. To coordinate agents without explicitly communicating private preferences, we introduce belief play, which provably recovers the true equilibria from conservative local games, and a distributed iterative best-response protocol requiring less information. We apply the framework to maritime navigation, systematically lifting pairwise traffic rules to multi-vessel encounters. On seven encounters with up to four vessels, every rule violation of the committed equilibria is certified as forced by the legal hierarchy or unsatisfiable, and defectors are identified from public information in all tested cases. These results indicate that guideline-based posetal games offer an auditable route from partially specified laws to multi-agent motion planning.

## Key Contributions

- Novel research in cs.MA, cs.GT
- High utility score (0.96) indicating significant research value

## Activation

auditable, deployable, multiagent, motion, planning, posetal, games, legal, guidelines

## Notes

Added by arXiv cron job on 2026-10-17.
