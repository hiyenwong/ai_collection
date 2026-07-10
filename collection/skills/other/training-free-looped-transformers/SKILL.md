---
name: training-free-looped-transformers
description: "Training-free looped transformers — inference-time technique that loops a contiguous mid-stack block of layers in a frozen pretrained LLM to improve reasoning without fine-tuning. Use when: (1) improving a frozen LLM's reasoning at inference time, (2) retrofitting recurrence onto pretrained models without any training, (3) getting free accuracy gains on reasoning benchmarks with no additional training cost.
arxiv_id: "2605.23872"
published: "2026-05-22"
authors: "Lizhang Chen, Jonathan Li, Chen Liang, Ni Lao, Qiang Liu"
tags: [inference-time-compute, llm-reasoning, transformer, looped-models, test-time-scaling, frozen-models]
---

# Training-Free Looped Transformers

Core methodology from arXiv:2605.23872 (2026).

## Core Concept

Training-free looped transformers retrofit recurrence onto **frozen pretrained LLMs at test time** by looping a contiguous mid-stack block of layers. Unlike prior looped transformer methods that require training with the looped structure end-to-end, this approach requires **no fine-tuning, no continued training, and no architectural changes**.

**Key insight**: A pre-norm transformer block can be viewed as a forward Euler step on an ODE. Looping replaces one large update with smaller damped sub-steps.

## Algorithm

1. **Select a mid-stack block** of contiguous layers from a frozen checkpoint
2. **Apply damped sub-step looping** — instead of one forward pass through the block, apply it multiple times with damping:
   - Let `x` be the input to the block
   - Let `F(x)` be the block output
   - Loop: `x ← x + α * (F(x) - x)` where `α < 1` is a damping factor
   - Repeat for `k` iterations
3. **Continue forward pass** through remaining layers

### Why Damping Matters
Naive block reapplication (without damping) usually degrades performance. The damped formulation stabilizes the loop by treating it as a refined ODE integration step.

## Implementation Pattern

```python
def looped_forward(model, input_ids, block_start, block_end,
                   num_loops=3, damping=0.5):
    """
    Inference-time looping of a transformer block.

    Args:
        model: Pretrained transformer (frozen)
        block_start: First layer index of loop block
        block_end: Last layer index of loop block
        num_loops: Number of loop iterations
        damping: Step size dampening factor (try 0.3-0.7)
    """
    # Forward through initial layers
    hidden = model.embed(input_ids)
    for i in range(block_start):
        hidden = model.layers[i](hidden)

    # Looped block
    for _ in range(num_loops):
        block_output = hidden
        for i in range(block_start, block_end):
            block_output = model.layers[i](block_output)
        # Damped update
        hidden = hidden + damping * (block_output - hidden)

    # Forward through remaining layers
    for i in range(block_end, len(model.layers)):
        hidden = model.layers[i](hidden)

    return model.unembed(hidden)
```

## Key Results

- Qwen3-4B-Instruct: +2.64 pp on MMLU-Pro
- Qwen3-30B-A3B-Instruct: +1.14 pp on CommonsenseQA
- Moonlight-16B-A3B-Instruct: +1.20 pp on OpenBookQA
- Works across 7 model families: dense, sparse MoE, and MLA+MoE

## Practical Guidance

- **Loop block selection**: Mid-stack layers (e.g., middle 30-50% of model depth) work best
- **Loop count**: Start with 2-5 iterations; diminishing returns beyond ~10
- **Damping factor**: 0.3-0.7; lower = more conservative (stable), higher = more aggressive (may degrade)
- **No training cost** — only additional forward pass compute at inference
- Compatible with any pretrained transformer (dense, MoE, MLA)

## Activation Keywords

Training-free looped transformers, inference-time looping, test-time compute scaling, frozen LLM improvement, transformer ODE interpretation, damped looping, block reapplication, retrofitting recurrence, pretrained model refinement, no-training reasoning improvement, inference-time compute optimization, looped transformer inference
