---
name: personalization-shopping-conversation
description: Multi-agent multimodal RAG framework for personalized conversational shopping, decomposing dialogue state tracking, recommendation, and long-horizon preference consistency.
tags: [conversational-ai, recommendation-systems, multi-agent, rag, personalization, e-commerce]
---

# Personalization Shopping Agent

## Paper Metadata

- **arXiv ID**: 2610.11375
- **Title**: Personalization Shopping Agent
- **Categories**: cs.AI, cs.CL, cs.IR
- **Utility Score**: 0.87
- **Date**: 2026-10-10
- **Link**: https://arxiv.org/abs/2610.11375

## Key Contributions

- Introduces a multi-agent multimodal RAG framework for personalized conversational shopping.
- Decomposes the shopping conversation task into three specialized agents: dialogue state tracking, recommendation generation, and long-horizon preference consistency.
- Demonstrates that explicit decomposition outperforms monolithic approaches on both task completion and user satisfaction.
- Addresses the challenge of maintaining preference consistency across long shopping conversations where user needs evolve.

## Core Methodology

The framework treats conversational shopping as a multi-agent coordination problem. A dialogue state tracking agent maintains a structured representation of the user's needs, constraints, and preferences as the conversation unfolds. This includes explicit requirements (e.g., "red shoes, size 10") and implicit preferences inferred from conversation history.

A recommendation agent uses multimodal RAG to retrieve and rank products based on the dialogue state. It combines text descriptions, product images, and user reviews to generate recommendations that match both explicit requirements and inferred preferences. The RAG component retrieves from a product database using embeddings that capture semantic similarity across modalities.

A preference consistency agent monitors the conversation for drift and contradictions. As users explore options, their stated preferences may shift or conflict with earlier statements. This agent detects inconsistencies, prompts for clarification when needed, and ensures that recommendations remain aligned with the user's evolving but coherent preferences. The decomposition allows each agent to specialize while the overall system maintains both responsiveness and consistency.

## Relevance to multi-agent-rl

Demonstrates how multi-agent architectures can decompose complex conversational tasks into specialized components. Relevant to building AI shopping assistants, customer service bots, and any conversational system that must balance task completion with personalization over extended interactions.

## Reference

- Paper: https://arxiv.org/abs/2610.11375
