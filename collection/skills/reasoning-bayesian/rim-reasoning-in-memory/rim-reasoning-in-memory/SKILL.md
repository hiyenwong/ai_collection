---
name: rim-reasoning-in-memory
description: Latent reasoning method that replaces autoregressive generation with memory blocks - working memory capacity for compute-efficient reasoning
version: 1.0.0
author: Hermes Agent (from arXiv 2605.30343)
tags: [LLM, reasoning, working-memory, latent-reasoning, inference-optimization]
activation_keywords: [latent reasoning, working memory, memory blocks, test-time compute, reasoning steps, autoregressive]
---

# RiM: Reasoning in Memory - Working Memory for Latent Reasoning

## Overview

RiM (Reasoning in Memory) introduces a latent reasoning method that replaces autoregressive generation of reasoning steps with fixed memory blocks. These memory blocks unlock working-memory capacity in LLMs, enabling compute-efficient reasoning in a single forward pass.

## Core Concept

### Key Insight
Human cognition uses working memory to hold and manipulate information internally without externalizing intermediate thoughts. RiM applies this principle to LLMs.

### Memory Blocks
- Fixed sequences of special tokens (not generated)
- Processed in single forward pass
- Unlock working-memory capacity
- Enable latent reasoning without autoregressive step generation

## Two-Stage Curriculum

### Stage 1: Grounding Phase
```python
# Ground memory blocks by predicting explicit reasoning steps
def grounding_training(model, prompt, memory_block):
    output = model(prompt + memory_block)
    # Predict explicit reasoning step after memory block
    reasoning_step = decode_explicit_step(output)
    # Supervise on step-level outputs
    loss = step_prediction_loss(reasoning_step, ground_truth_step)
```

### Stage 2: Refinement Phase
```python
# Discard step-level supervision, iterate on final answer
def refinement_training(model, prompt, memory_blocks):
    # Process multiple memory blocks iteratively
    for memory_block in memory_blocks:
        output = model(prompt + memory_block)
        answer = decode_answer(output)
        # Refine answer prediction
        loss = answer_prediction_loss(answer, ground_truth)
```

## Implementation Pattern

### Memory Block Design
```python
# Define memory block as fixed token sequence
MEMORY_BLOCK_TOKENS = [MEM_START, MEM_TOKEN_1, ..., MEM_TOKEN_N, MEM_END]

def add_memory_block(prompt, position):
    # Insert memory block at specified position
    return prompt[:position] + MEMORY_BLOCK_TOKENS + prompt[position:]
```

### Single Forward Pass Processing
```python
def rim_forward_pass(model, prompt, num_memory_blocks):
    # Create prompt with multiple memory blocks
    enhanced_prompt = prompt
    for i in range(num_memory_blocks):
        enhanced_prompt = add_memory_block(enhanced_prompt, len(enhanced_prompt))
    
    # Single forward pass processes all memory blocks
    output = model(enhanced_prompt)
    return decode_answer(output)
```

## Key Results
- Matches or exceeds existing latent reasoning methods
- Avoids autoregressive generation of thoughts
- Works across different LLM families and sizes
- Compute-efficient reasoning

## When to Use
- Test-time compute scaling without autoregressive chains
- Latent reasoning applications
- Working memory simulation in LLMs
- When inference efficiency is critical

## Pitfalls
- Memory blocks need grounding phase training first
- Cannot skip two-stage curriculum
- Memory block length needs tuning for specific models
- Special tokens must be added to vocabulary

## References
- arXiv: 2605.30343v1
- Authors: Lukas Aichberger, Sepp Hochreiter
- Published: 2026-05-28