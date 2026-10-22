---
name: tom2vec-multi-agent-coordination
description: "ToM2Vec: Continuous Theory-of-Mind tokens for multi-agent LLM coordination. Use when building multi-agent systems needing partner state reasoning under uncertainty."
paper_id: 2610.29934
utility_score: 1.0
categories: [cs.AI, cs.CL, cs.MA]
date: 2026-10-21
tags: [multi-agent, theory-of-mind, llm-agents, coordination, continuous-representations]
---

# ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination

## Key Contribution
Introduces ToM2Vec, which learns continuous Theory-of-Mind (ToM) embeddings for multi-agent LLM coordination. Instead of describing partner states in text (which captures only one state), ToM2Vec forms abstract continuous tokens representing multiple possible partner states under uncertainty.

## Core Method
- **Problem**: Text-based ToM in LLM agents can only describe a single partner state; real multi-agent collaboration requires reasoning over multiple possible partner states simultaneously
- **Solution**: Learn continuous ToM tokens that encode distributions over partner mental states
- **Architecture**: ToM encoder produces vector embeddings → injected as special tokens into LLM context → enables probabilistic reasoning about partner beliefs/intents
- **Training**: Agents learn ToM representations through cooperative gameplay with gradient-based optimization

## Why It Matters
- First approach to represent ToM as continuous vectors rather than text descriptions for LLM agents
- Enables reasoning about uncertainty in partner states — critical for real-world coordination
- Bridges cognitive science (Theory of Mind) with practical multi-agent LLM systems
- Outperforms text-based ToM prompting on coordination benchmarks

## Application Scenarios
- Multi-agent LLM systems requiring partner modeling
- Cooperative AI agents in partially observable environments
- Human-AI teaming where the AI must model human intent under uncertainty
- Negotiation and dialogue systems

## Implementation Notes
- ToM tokens are learned embeddings, not hand-crafted
- Compatible with existing LLM agent architectures (added as special tokens)
- Requires cooperative training signal — agents must interact to learn useful ToM representations
