---
name: when-does-test-time-search-help-world
description: "When Does Test-Time Search Help World Action Model..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.41970v1
utility: 0.99
published: 2026-10-30
---

# When Does Test-Time Search Help World Action Models? An Empirical Audit of Candidate Selection and Simulator Integrity

**Authors:** Jun Liu, Dajie Sun, Zhenglun Kong, Zhenjiang Fan, Peiyan Dong...
**Published:** 2026-10-30
**arXiv:** [2610.41970v1](https://arxiv.org/abs/2610.41970v1)
**Categories:** cs.AI
**Utility Score:** 0.99

## Abstract

World-action models increasingly apply test-time scaling, spending extra inference computation on candidate selection and adaptive allocation to improve control. Such gains are credible only when candidates carry exploitable signal, nominal compute savings become real speedup, and evaluation stays reliable. We audit all three on Cosmos Policy and RoboCasa with a premise-first, pre-registered methodology. On clean data, a learned value selector is 1.66 pp worse than random; a hindsight oracle gains only 1.40 pp, with an episode-level interval spanning zero; and 82% of states show identical candidate outcomes, leaving little selection headroom. Token pruning cuts per-forward FLOPs by up to 47% but yields at most a measured 1.15$\times$ end-to-end speedup on the deployed path (1.25$\times$ on a decode-excluded path), short of a 1.5$\times$ target, and our adaptive-allocation experiment is inconclusive under a power gate. We further identify and fix a silent rendering corruption whose rate rises sharply along compute-heavy planning paths while leaving the official direct-policy result unaffected, and release a detector, fix, and scripts. These findings show why test-time scaling should be audited as a chain of premises (decision signal, realized efficiency, evaluationintegrity) rather than by success rate alone. Conclusions are scoped to the tested configuration.

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-30

## Activation

when, does, testtime, search, help, world, action, models, empirical, audit
