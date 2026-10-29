---
name: uncovering-why-llms-fail-from-internal
description: "Research paper: Uncovering Why LLMs Fail: From Internal Mechanisms to Adversarial Reasoning Traj"
tags: [arxiv, paper, cs.AI]
arxiv_id: "2610.37369"
utility: 0.93
---

# Uncovering Why LLMs Fail: From Internal Mechanisms to Adversarial Reasoning Trajectories

**arXiv:** [2610.37369](https://arxiv.org/abs/2610.37369)
**Authors:** Zirui Ding, Xinxin Fan, Hao Yuan, Shaoye Luo, Men Niu...
**Published:** 2026-10-27
**Categories:** cs.AI
**Utility Score:** 0.93

## Abstract

Large language models (LLMs) are usually evaluated by final-output correctness or safety, yet an endpoint label does not reveal how a failure develops throughout the reasoning process. We therefore ask whether ordinary reasoning failures and adversarially induced failures can be characterized using the same internal coordinates. Towards this end, we in this paper study a white-box diagnostic framework CauTrace to disclose the root-cause of why LLM fails from three fundamental inspections: Functional States, Propagation of Representation, Temporal-State Coordination and Reasoning Trajectory. First, seven functional states are creatively defined to represent the support and constraint processing in LLMs. Second, the propagation of representation change measures how the changes among the seven states persist across subsequent Transformer blocks. Third, temporal-state coordination and trajectory topology characterize when the commitment and verification occur relative to the support, and how the dominant state sequence evolves over the full inference process. Finally, we evaluate CauTrace on both clean reasoning failures and paired adversarial perturbations. Across Qwen and LLaMA-family models, the failed traces show weaker Attention-MLP agreement on support-state updates and less verification activity relative to commitment, while the exact representation-level signatures and timing shifts vary by architecture. Held-out repair and steering tests demonstrate consistent operationa

## Key Contributions

- Paper identified as high-utility (≥0.85) from arXiv scan
- Relevant to: cs.AI

## Potential Applications

- Research reference for ai safety eval domain
- Building block for future work in this area
