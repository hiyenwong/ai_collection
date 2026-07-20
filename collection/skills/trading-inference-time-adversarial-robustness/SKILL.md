---
name: trading-inference-time-adversarial-robustness
category: ai-safety
description: Methodology for trading inference-time compute to improve adversarial robustness in LLMs through repeated sampling and output filtering.
---

# Trading Inference Time Compute for Adversarial Robustness

## Overview

Methodology from OpenAI research showing that inference-time compute (repeated sampling) can be traded for improved adversarial robustness. By generating multiple outputs and applying filtering/aggregation, models can defend against adversarial prompts.

## Core Methodology

1. **Repeated Sampling**: Generate multiple completions from the same prompt
2. **Safety Filter**: Apply a safety classifier/judge to each output
3. **Aggregation**: Return the majority-voted or highest-scoring safe output
4. **Compute-Robustness Trade-off**: More samples → higher robustness guarantee

## Key Findings

- Adversarial robustness improves logarithmically with number of samples
- A safety filter with even moderate accuracy can provide strong guarantees when combined with sufficient sampling
- This approach is complementary to prompt-level defenses and training-time alignment

## Implementation Pattern

```
n_samples = 10-100  # More samples = more robust
outputs = [model.generate(prompt) for _ in range(n_samples)]
scores = [safety_filter(o) for o in outputs]
safe_outputs = [o for o, s in zip(outputs, scores) if s > threshold]
if safe_outputs:
    return majority_vote(safe_outputs)
else:
    return "I cannot answer this"
```

## When to Use

- Building adversarial-robust LLM applications
- Need provable robustness guarantees
- Can afford higher inference-time compute costs
- Post-hoc defense layer on top of existing alignment

**Activation**: adversarial robustness, inference-time compute, repeated sampling, safety filter, jailbreak defense, compute-robustness tradeoff
