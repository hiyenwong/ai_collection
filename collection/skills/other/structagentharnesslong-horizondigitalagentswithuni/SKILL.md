---
name: structagentharnesslong-horizondigitalagentswithuni
description: 'Research paper: StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure. Brief summary of key findings and contributions.'
metadata:
  openclaw:
    emoji: "⚡"
    tags: ["research", "arxiv", "agent"]
---

# StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure

**arXiv ID:** 2607.11388  
**Published:** 2026-07-11  
**Utility Score:** 0.85

## Abstract

Recent advances in large language models (LLMs) and vision-language models (VLMs) have enabled increasingly capable digital agents for computer use. However, real-world tasks are often long-horizon and involve evolving contexts containing accumulated observations, intermediate edits, failed attempts, and partially completed executions. Existing agents typically operate over raw interaction history, making task progress difficult to interpret, verify, and recover, which ultimately limits reliable long-horizon execution. In this paper, we argue that addressing this challenge requires explicitly structuring both the agent's state and workflow around a unified causal representation of task progress. We present **StructAgent**, a state-centered framework that introduces a unified state for maintaining compact, verifiable task progress and a structured workflow that regulates progress through verifier-backed state transitions. Building on this design, StructAgent further enables explicit progress checkpointing, evidence-driven task completion, targeted failure recovery, and tool-supported execution, while ensuring that all progress updates remain grounded in verification. Extensive experiments show that StructAgent consistently improves a wide range of LLM and VLM backbones on long-horizon computer-use tasks. On OSWorld-Verified, it improves Qwen3.5-9B from 27.0% to 46.9% success rate and Qwen3.5-27B from 31.6% to 62.2%, while achieving a new open-source state of the art of 78.9% with MiniMax-M3. Moreover, the same framework generalizes beyond desktop environments to Minecraft, demonstrating the generality of our design.

## URL

https://arxiv.org/abs/2607.11388