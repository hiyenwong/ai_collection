---
name: compact-latent-coordination-for-autonomous-vehicles-at-unsignalized
description: 'Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections'
metadata:
  {
    "arxiv_id": "2607.21488",
    "utility": 1.0,
    "date_added": "2026-07-26"
  }
---

# Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections

arXiv: 2607.21488  
Published: 2026-07-23  
Utility: 1.0

## Summary
Coordinating autonomous vehicles at unsignalized intersections remains a critical challenge for multi-agent reinforcement learning (MARL) systems, which typically struggle with combinatorial action spaces, reliance on privileged information, or rigid agent designs. We propose Master-Agent Proto-plan System (MAPS), a hierarchical deep reinforcement learning (DRL) architecture in which a centralized Master agent generates a compact, continuous embedding, denoted as proto-plan, that encodes a global coordination strategy. Decentralized Worker agents integrate this embedding with local observations to execute vehicle-specific control, decoupling strategic intent from tactical execution and enabling independent optimization of each module.
  As a proof-of-concept evaluation of this coordination mechanism, we test MAPS across 72 intersection configurations in HighwayEnv. MAPS achieves collision-free navigation while significantly reducing average travel time, outperforming state-of-the-art baselines. The learned proto-plans further exhibit robust generalization: a system trained with three agents achieves a 94% success rate when deployed zero-shot to five-agent scenarios, confirming that proto-plan-based hierarchical learning provides a promising framework for multi-vehicle coordination....

## Key Information
- **Title**: Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections
- **Authors**: [Extract from entry]
- **Primary Category**: cs.AI

## Potential Skill Application
This paper presents research relevant to AI agent systems. Consider extracting methodologies, algorithms, or frameworks for skill development.

## Reference
- arXiv: https://arxiv.org/abs/2607.21488
