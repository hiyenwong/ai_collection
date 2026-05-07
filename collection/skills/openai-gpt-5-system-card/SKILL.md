---
name: openai-gpt-5-system-card
description: GPT-5 system architecture and safety methodology - unified model with reasoning router, safe-completions, and deliberative alignment
tags: [alignment, safety, system-card, routing, llm]
trigger: gpt-5, system card, unified model, router, safe-completions, deliberative alignment
version: 1.0
created: 2026-05-07
---

# OpenAI GPT-5 System Card Methodology

## Overview

GPT-5 represents OpenAI's unified system architecture that combines multiple model variants with intelligent routing. This document extracts the key methodological patterns from the GPT-5 System Card (arXiv:2601.03267).

## Core Architecture

### 1. Unified Model System

GPT-5 uses a **three-component architecture**:

1. **Fast Model (gpt-5-main)**: Answers most questions quickly and efficiently
2. **Deep Reasoning Model (gpt-5-thinking)**: Handles harder problems with extended reasoning
3. **Real-Time Router**: Decides which model to use based on:
   - Conversation type
   - Query complexity
   - Tool requirements
   - Explicit user intent (e.g., "think hard about this")

### 2. Continuous Router Training

The router is trained on real-world signals:
- User model switching behavior
- Response preference rates
- Measured correctness
- Implicit feedback loops

### 3. Fallback Mechanism

When usage limits are reached, a **mini version** of each model handles remaining queries, ensuring graceful degradation rather than complete service denial.

## Safety Methodology

### Safe-Completions

GPT-5 introduces **safe-completions**, OpenAI's latest approach to safety training that prevents disallowed content generation.

### Preparedness Framework

- **Classification**: gpt-5-thinking classified as **High capability** in Biological and Chemical domains
- **Precautionary Approach**: Activates associated safeguards even without definitive evidence of harm potential
- **Threshold Definition**: "High capability" = could meaningfully help a novice create severe biological harm

## Key Improvements Over Previous Models

1. **Reduced Hallucinations**: Significant advances in factual accuracy
2. **Improved Instruction Following**: Better adherence to user instructions
3. **Minimized Sycophancy**: Less tendency to agree with incorrect user premises
4. **Domain Specialization**: Leveled up performance in ChatGPT's most common uses:
   - Writing
   - Coding
   - Health

## Practical Applications

### When to Use Deep Reasoning
- Complex problem solving
- Multi-step reasoning tasks
- Technical analysis
- Code debugging and architecture

### When Fast Model Suffices
- General Q&A
- Simple writing tasks
- Quick information lookup
- Conversational interactions

## Related Patterns

- [[openai-o1-system-card]] - o1's chain-of-thought reasoning training
- [[instruction-following]] - InstructGPT's instruction following methodology
- [[learning-to-summarize-with-human-feedback]] - RLHF foundations
