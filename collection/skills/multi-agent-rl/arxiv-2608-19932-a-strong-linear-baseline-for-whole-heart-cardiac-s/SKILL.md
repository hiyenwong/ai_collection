---
name: arxiv-2608-19932-a-strong-linear-baseline-for-whole-heart-cardiac-s
description: 'A Strong Linear Baseline for Whole-Heart Cardiac Shape Completion on CT, with an Open Eleven-Structure Statistical Shape Model (arXiv: 2608.19932)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# A Strong Linear Baseline for Whole-Heart Cardiac Shape Completion on CT, with an Open Eleven-Structure Statistical Shape Model

**Authors:** Matej Gazda, Jakub Gazda, Juraj Gazda, Peter Drotar
**arXiv:** 2608.19932
**Utility:** 1.00
**Published:** 2026-08-20T11:45:20Z
**Link:** http://arxiv.org/abs/2608.19932

## Abstract

Public cardiac cohorts annotate different subsets of the heart, so shapes from separate sources cannot be pooled without shared correspondence. Among released cardiac shape resources, none we identified carries the atrial appendage, pulmonary veins, and caval stumps as separate blocks in one mesh. Completion benchmarks also compare deep models against a least-squares projection onto shape modes, not the conditional estimator the same fitted model implies. We release an eleven- structure cardiac computed-tomography (CT) statistical shape model, built from 383 automatically labelled cases in 11 571-vertex correspondence, and compare completion estimators under one frozen internal split and endpoint. On a 76-case internal list held out from fitting, a closed-form conditional-Gaussian estimator reconstructed the missing non-chamber structures at 3.717 mm mean per-vertex error, averaged equally over one, three, five, and nine observed structures. A five-refit mask-conditioned graph variational autoencoder reached 5.248 mm and nearest-neighbour retrieval 8.931 mm. The paired difference was 1.531 mm (95% confidence interval 1.384 to 1.711), and the ordering held in a raw-coordinate sensitivity arm. Expert manual labels exist for 58 external CT cases, but our registered reference is close enough to score only five structures. There the closed-form estimator again had lower average surface distance, 95th-percentile Hausdorff distance, and Chamfer error for both completed atria. On a second public benchmark of 20 cases the reference was close enough for three of four completed structures, and the same ordering held there. Four structures have no expert reference. The released model and its completion operator support cohort-unification research on aligned CT, not clinical use.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "A Strong Linear Baseline for Whole-Heart Cardiac Shape Completion on CT, with an Open Eleven-Structure Statistical Shape Model". 
The paper presents novel ideas in multi-agent-rl that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.19932
