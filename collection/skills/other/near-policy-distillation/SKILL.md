---
name: near-policy-distillation
description: Methodology for accelerating on-policy distillation via asynchronous generation and evaluation. Decouples generation from evaluation using a near-policy buffer, achieving 2-4x throughput gains without quality degradation.
category: deep-learning
tags: [LLM, distillation, RL, training-efficiency, async-compute]
trigger: distillation, on-policy distillation, async generation, NPD, teacher-student, throughput optimization
---

# Near-Policy Distillation (NPD) Methodology

## Overview
Near-Policy Distillation accelerates on-policy distillation by decoupling the expensive generation phase from the evaluation/update phase using an asynchronous buffer of near-policy samples.

## Core Technique
1. **Asynchronous Generation Buffer**: A separate worker continuously generates samples from a slightly stale (near-policy) version of the model
2. **Decoupled Evaluation**: The main training loop consumes buffered samples for distillation updates without waiting for generation
3. **Near-Policy Guarantee**: The buffer is managed to ensure samples are close enough to the current policy (bounded KL divergence) to maintain on-policy quality

## Key Benefits
- **2-4x throughput improvement** over synchronous on-policy distillation
- **No quality degradation** — maintains distillation fidelity via KL-bounded staleness
- **GPU utilization** — generation and evaluation can run on separate devices or time-sliced

## Implementation Steps
1. Spawn async generation worker with delayed policy snapshot
2. Maintain circular buffer of (prompt, response, logprob) tuples
3. Main loop consumes buffer entries, applies KL penalty if policy drift exceeds threshold
4. Refresh generation worker's policy snapshot periodically
5. Tune buffer size and refresh frequency based on GPU memory and staleness tolerance

## Pitfalls
- Buffer staleness must be monitored — excessive KL divergence degrades distillation quality
- Memory management: large buffers can exceed GPU/CPU memory on long-context models
- Requires careful synchronization to avoid race conditions between buffer write/read

## Activation Keywords
distillation, on-policy distillation, async generation, NPD, teacher-student, throughput optimization, generation buffer
