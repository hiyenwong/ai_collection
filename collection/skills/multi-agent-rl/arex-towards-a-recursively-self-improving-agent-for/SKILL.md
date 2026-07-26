---
name: arex-towards-a-recursively-self-improving-agent-for
description: 'AREX: Towards a Recursively Self-Improving Agent for Deep Research'
metadata:
  {
    "arxiv_id": "2607.21461",
    "utility": 1.0,
    "date_added": "2026-07-26"
  }
---

# AREX: Towards a Recursively Self-Improving Agent for Deep Research

arXiv: 2607.21461  
Published: 2026-07-23  
Utility: 1.0

## Summary
Deep research requires agents to find answers that jointly satisfy multiple constraints. Discovering such answers is costly, whereas verifying a candidate can often be decomposed into tractable constraint-wise checks. This discovery--verification asymmetry suggests that a research agent should do more than simply search longer: it should recursively improve its current answer by verifying intermediate results and using the partially verified state to guide subsequent refinement. We introduce AREX, a family of Recursively Self-Improving (RSI) deep research agents. AREX alternates between an inner research loop that gathers evidence and constructs a provisional answer, and an outer self-improvement loop that audits the answer constraint-wise, identifies unresolved claims, and launches targeted follow-up research. To sustain RSI over long horizons, AREX learns an autonomous context-update tool that compresses growing interaction history into a compact improvement state preserving verified evidence and unresolved constraints, without relying on an external model. We train AREX on verified synthetic tasks and high-quality trajectories through agentic mid-training and long-horizon reinforcement learning. To mitigate sparse final rewards during long horizon learning, we emphasize key steps where decisive evidence is acquired or erroneous research directions are corrected. We instantiate a dense 4B model and a 122B-A10B Mixture-of-Experts model. Across BrowseComp, WideSearch, DeepSea...

## Key Information
- **Title**: AREX: Towards a Recursively Self-Improving Agent for Deep Research
- **Authors**: [Extract from entry]
- **Primary Category**: cs.AI

## Potential Skill Application
This paper presents research relevant to AI agent systems. Consider extracting methodologies, algorithms, or frameworks for skill development.

## Reference
- arXiv: https://arxiv.org/abs/2607.21461
