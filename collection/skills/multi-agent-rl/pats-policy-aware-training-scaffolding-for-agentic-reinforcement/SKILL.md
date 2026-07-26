---
name: pats-policy-aware-training-scaffolding-for-agentic-reinforcement
description: 'PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning'
metadata:
  {
    "arxiv_id": "2607.21419",
    "utility": 1.0,
    "date_added": "2026-07-26"
  }
---

# PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning

arXiv: 2607.21419  
Published: 2026-07-23  
Utility: 1.0

## Summary
In long-horizon LLM agent reinforcement learning, weak policies often repeat similar failures, producing uninformative rollout trajectories and limiting effective policy optimization. Existing skill-centric methods improve exploration by optimizing, filtering, or internalizing reusable skills. However, they remain centered on the skills themselves rather than being designed as adaptive training-time support for the evolving policy. To address this, we propose a policy-centric training paradigm that reframes skills as a dynamic training scaffold. Our framework, Pats, converts rollout groups from the latest policy into evidence cards and uses task-specific evaluation to adjust the context used in subsequent rollouts. Concrete guidance helps weak policies to complete challenging tasks. As policy improves, redundant context is revised or removed to reduce reliance on explicit guidance while preserving useful rollout variation. The policy is optimized with environmental rewards using standard RLVR, and the training scaffold is discarded at deployment. On ALFWorld and WebShop, Pats improves over strong baselines by up to 18.6%. Across seven search-augmented QA benchmarks, it remains competitive while using 32.1% fewer prompt tokens than the baseline....

## Key Information
- **Title**: PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning
- **Authors**: [Extract from entry]
- **Primary Category**: cs.AI

## Potential Skill Application
This paper presents research relevant to AI agent systems. Consider extracting methodologies, algorithms, or frameworks for skill development.

## Reference
- arXiv: https://arxiv.org/abs/2607.21419
