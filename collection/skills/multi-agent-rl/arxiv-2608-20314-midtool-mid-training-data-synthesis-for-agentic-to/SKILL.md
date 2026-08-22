---
name: arxiv-2608-20314-midtool-mid-training-data-synthesis-for-agentic-to
description: 'MidTool: Mid-training Data Synthesis for Agentic Tool Use (arXiv: 2608.20314)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# MidTool: Mid-training Data Synthesis for Agentic Tool Use

**Authors:** Fengqing Jiang, Yite Wang, Boyi Liu, Zhaoyang Wang, Canwen Xu, Zhewei Yao, Radha Poovendran, Yuxiong He
**arXiv:** 2608.20314
**Utility:** 1.00
**Published:** 2026-08-20T17:53:59Z
**Link:** http://arxiv.org/abs/2608.20314

## Abstract

Mid-training is increasingly recognized as a critical stage for shaping the capabilities of large language models. Recent work has shown that targeted mid-training can strengthen reasoning-intensive abilities such as math and science, and can also improve agentic capabilities in software-engineering settings. In this work, we study the parallel but less explored agentic capability: general tool use. We present MidTool, an open corpus construction pipeline for agentic tool-use mid-training that combines large-scale web, PDF, and code data with synthesized supervision from real-world tool APIs, MCP skills, and document-grounded workflows. MidTool is designed to teach models how to recognize tool affordances, ground arguments from context, compose tool call workflow, and recover from incomplete information. We mid-train Qwen3-4B-Base and Qwen3-8B-Base on MidTool-Mix, and then apply follow-up post-training with both supervised fine-tuning and reinforcement learning. Compared with baselines, MidTool-Mix consistently improves downstream performance under both SFT and RL on BFCL, tau2-Bench, and MCP Universe. These results suggest that general tool use, like other important LLM capabilities, benefits from dedicated mid-training rather than being left entirely to post-training.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "MidTool: Mid-training Data Synthesis for Agentic Tool Use". 
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

- arXiv:2608.20314
