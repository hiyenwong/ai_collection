---
name: learning-meta-skills-agent-harness-design
description: Test-time AI-for-AI where Builder agents learn meta-skills to construct better execution environments for Target agents with fixed weights
version: 1.0.0
tags: [cs.AI, cs.CL, cs.LG, meta-skills, agent-harness, test-time-adaptation, ai4ai]
source: arxiv
arxiv_id: 2609.38143v1
utility: 0.85
---

# Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI

**Authors:** Cheng Qian, Kunlun Zhu, Beibin Li
**Published:** 2026-09-29
**Categories:** cs.AI, cs.CL, cs.LG
**arXiv:** https://arxiv.org/abs/2609.38143v1

## Summary

Agent performance depends on both reasoning ability and the environment in which it acts. We study test-time AI-for-AI, asking how a Builder can learn to construct better execution environments for a Target while both models' weights remain fixed. To make the Builder's experience reusable, we introduce Meta-Skill: principles specifying when support is needed and what resources to provide. The Builder learns these principles from Target's execution feedback on the development set, then uses the feedback to construct improved environments. This approach enables adaptive environment design without modifying the underlying agent weights, making the learned meta-skills transferable across different scenarios and tasks.

## Key Contributions

- Introduces the concept of Meta-Skills for agent harness design in test-time AI-for-AI
- Enables Builder agents to construct better execution environments for Target agents without weight updates
- Provides reusable principles that specify when support is needed and what resources to provide
- Demonstrates that environment design can significantly improve agent performance independently of reasoning ability

## Relevance

This paper is highly relevant for researchers working on agent systems, test-time adaptation, and AI-for-AI approaches. The meta-skill framework provides a novel way to improve agent performance through environment design rather than model updates, which is particularly valuable when model weights are fixed or when rapid adaptation is needed. The approach has implications for creating more effective agent harnesses, improving LLM performance through better prompting and tool provision, and developing adaptive systems that can optimize their own execution environments.
