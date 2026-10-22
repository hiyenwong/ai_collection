---
name: memorytax-agent-memory
description: "MemoryTax: The Bitter Lesson of Agent Memory. Tests whether designed memory systems still help when LLMs are strong enough to search raw history themselves."
paper_id: 2610.29823
utility_score: 0.80
categories: [cs.CL, cs.AI]
date: 2026-10-21
tags: [agent-memory, mem0, zep, coding-agents, bitter-lesson, retrieval]
---

# MemoryTax: The Bitter Lesson of Agent Memory

## Key Contribution
Empirical study asking whether designed memory systems (Mem0, Zep) still help once LLMs are strong enough to search raw conversation history themselves. Tests on LoCoMo benchmark (419 turns, 152 questions) with 4 memory methods × 3 coding agents.

## Core Findings
- **Designed memory** (Mem0, Zep) pre-selects what to keep before any question arrives
- **Raw history** (coding agents keeping full context + search tools) lets the model search itself
- **Result**: As model capability increases, the gap between designed memory and raw history narrows or reverses — a "bitter lesson" for memory system designers
- **BM25 baseline** often competitive with sophisticated memory systems
- **Implication**: Investing in better models may yield more than investing in complex memory architectures

## Why It Matters
- Challenges the assumption that structured memory systems are always beneficial
- Suggests a phase transition: weak models need memory curation, strong models can search raw history
- Practical guidance: for frontier models (Claude, GPT-4+), simple retrieval over full history may outperform Mem0/Zep
- Cost implications: designed memory systems add infrastructure complexity that may not pay off

## Application Scenarios
- Choosing memory architecture for LLM agent systems
- Deciding between Mem0/Zep vs. raw context + retrieval
- Understanding when to invest in memory curation vs. model upgrades
- Debugging memory system failures in production agents

## Implementation Notes
- Tested on LoCoMo: long conversation (419 turns) with 152 questions
- Memory methods: full context, BM25, Mem0, Zep
- Coding agents: Claude, GPT-4, etc.
- Key metric: question-answering accuracy over long conversation history
- Recommendation: for frontier models, start with BM25 over raw history before adding Mem0/Zep complexity
