---
name: embodied-multiagent-isac
description: Embodied multiagent framework based on token communications for cooperative ISAC with UAV agents linking perception, decision-making, and physical actions.
tags: [embodied-ai, multi-agent-systems, isac, uav, token-communication, cooperative-perception]
---

# Embodied Multiagent ISAC

## Paper Metadata

- **arXiv ID**: 2610.11434
- **Title**: Embodied Multiagent ISAC
- **Categories**: cs.MA, cs.AI, cs.RO
- **Utility Score**: 0.86
- **Date**: 2026-10-10
- **Link**: https://arxiv.org/abs/2610.11434

## Key Contributions

- Introduces an embodied multiagent framework for cooperative Integrated Sensing and Communication (ISAC) using UAV agents.
- Proposes token-based communication protocols that link perception, decision-making, and physical actions in a closed loop.
- Demonstrates that token communication is more bandwidth-efficient than raw sensor sharing while maintaining task performance.
- Shows that embodied agents with physical constraints require different coordination strategies than abstract multi-agent systems.

## Core Methodology

The framework deploys multiple UAV agents equipped with ISAC capabilities, where each agent must simultaneously sense the environment and communicate with teammates. The challenge is that sensing and communication compete for the same radio resources, requiring careful coordination.

The key innovation is a token-based communication protocol where agents exchange discrete semantic tokens rather than raw sensor data. Each agent processes its local observations into tokens that capture task-relevant information (e.g., detected objects, estimated positions, uncertainty bounds). These tokens are transmitted to teammates, who integrate them into their own perception and planning.

The closed-loop architecture links perception (sensing the environment), decision-making (planning actions based on local and received tokens), and physical actions (moving the UAV, adjusting sensing parameters). This embodiment creates feedback loops absent in abstract multi-agent systems: physical movement affects sensing quality, which affects token generation, which affects teammate decisions. The framework demonstrates that token communication achieves near-optimal cooperative performance while using a fraction of the bandwidth required by raw data sharing.

## Relevance to multi-agent-rl

Addresses the challenge of coordinating embodied agents under communication constraints. Relevant to drone swarms, autonomous vehicles, robotic teams, and any multi-agent system where agents must cooperate while operating under bandwidth, energy, or latency limitations.

## Reference

- Paper: https://arxiv.org/abs/2610.11434
