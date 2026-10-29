---
name: gym-anything-rt-scaling-real-time
description: "Research paper: Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents"
tags: [arxiv, paper, cs.LG, cs.AI]
arxiv_id: "2610.37567"
utility: 0.92
---

# Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents

**arXiv:** [2610.37567](https://arxiv.org/abs/2610.37567)
**Authors:** Pranjal Aggarwal, Sean Welleck
**Published:** 2026-10-27
**Categories:** cs.LG, cs.AI
**Utility Score:** 0.92

## Abstract

AI agents have made substantial progress in domains where they have a non-trivial amount of time to deliberate between actions, such as mathematics, software engineering, and performing tasks on desktop applications. It is less clear how such models fare in settings that demand real-time interaction, such as playing a video game or operating a physical device. In these settings, the environment state may evolve as the agent is reasoning, or even as the underlying model is performing a forward pass. To gain insight into the real-time interaction capabilities of vision-language agents, we introduce Gym-Anything-RT. Our key idea is to construct visual minigames that demand a portfolio of capabilities required for interactive real-time settings. Gym-Anything-RT uses an agentic pipeline to automatically generate such environments based on a taxonomy of six capabilities required for real-time interaction, including the ability to perceive the environment and act under an evolving environment state. A key feature of Gym-Anything-RT is that it allows for controlled comparison of real-time interaction capabilities: we can run the same minigame in real time, or pause or slow down the environment to relax the requirement for real-time actions. We use Gym-Anything-RT to construct 100 real-time minigames and evaluate AI agents on them. We find large capability gaps in real-time interaction. For example, GPT-6 Astra (xHigh) achieves a pass rate of only 9.0% on the real-time minigames, whic

## Key Contributions

- Paper identified as high-utility (≥0.85) from arXiv scan
- Relevant to: cs.LG, cs.AI

## Potential Applications

- Research reference for nlp llm domain
- Building block for future work in this area
