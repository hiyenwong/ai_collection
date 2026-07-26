---
name: search-e1-self-distillation
description: "Search-E1 methodology from arXiv:2605.22511 (May 2026). Self-evolution for search-augmented reasoning agents via vanilla GRPO + Offline Self-Distillation (OFSD) with token-level forward KL objective. No external supervision needed. Use when: training search-augmented LLM agents, self-evolution pipelines, GRPO-based reasoning, offline distillation from privileged context."
---

# Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning

**arXiv:** 2605.22511 | **Date:** May 2026  
**Authors:** Zijun Liu, Yitao Zhai, Xiaotian Ye, Siyuan Huang, Shuyuan Zheng, Qing Yang, Yixuan Chen, Zixuan Zhang, Jian Hu, Peng Li, Yang Liu

## Overview

Search-E1 is a **self-evolution method** for search-augmented reasoning agents that requires **no external supervision, no auxiliary modules, and no process reward models**. It alternates between vanilla GRPO (Group Relative Policy Optimization) training rounds and **Offline Self-Distillation (OFSD)** — a token-level forward KL objective that bootstraps the policy's own inference-time distribution using privileged information available during training.

The core insight: during search-augmented inference, the model's own distributions under different contexts (with vs. without future knowledge) can serve as training signal. No ground-truth, no PRM, no human annotation needed.

## Method

### Training Pipeline (Two Interleaved Stages)

```
┌─────────────────────────────────────────────────┐
│              GRPO Training Round                │
│  • Policy samples multiple search trajectories  │
│  • Rewards from answer correctness (EM/F1)      │
│  • Advantage = (reward - baseline) / std        │
│  • Group-level normalization of preferences      │
└─────────────────────┬───────────────────────────┘
                      │
                      ▼  (next round)
┌─────────────────────────────────────────────────┐
│       Offline Self-Distillation (OFSD)          │
│  • Policy rolls out on its OWN training Qs      │
│  • Collects two distributions per token:        │
│    1. πθ(·|q, history) — standard inference     │
│    2. πθ(·|q, history, privileged context)      │
│  • Forward KL: KL(π_privileged || π_inference)  │
│  • No external labels or reward models           │
└─────────────────────────────────────────────────┘
```

### GRPO (Vanilla, No KL Penalty)

Standard GRPO is used for the RL stage. The policy generates a group of candidate search trajectories/answers for each question. Normalized advantages computed within each group drive preference learning at the trajectory level. Notably, the authors use **no KL penalty against a reference model** — the KL regularization comes entirely from OFSD.

### Offline Self-Distillation (OFSD)

OFSD is the key contribution. After each GRPO round, the **current policy** is used to generate offline rollouts on its **own training questions**. For each token position, two distributions are collected:

| Distribution | Context | Description |
|---|---|---|
| **Inference distribution** `πθ(· \| q, h_t)` | Only question + generated prefix history | What the model predicts normally at this token |
| **Privileged distribution** `πθ(· \| q, h_t, c_privileged)` | Question + history + privileged info | What the model predicts with knowledge from the full trajectory (e.g., which search results will be retrieved, what the final answer will be) |

### Token-Level Forward KL Objective

The OFSD loss aligns the inference-time distribution to the privileged distribution using **forward KL divergence**:

```
ℒ_OFSD = Σ_t KL(πθ(·|q, h_t, c_privileged) || πθ(·|q, h_t))
```

**Why forward KL (not reverse KL)?** Forward KL is mode-covering — it forces the inference distribution to assign probability everywhere the privileged distribution assigns probability. This is critical for search-augmented reasoning because it prevents the model from collapsing to a single mode and preserves diverse search behaviors.

**Key properties:**
- Token-level (not trajectory-level): preserves fine-grained per-step signal
- Forward direction: **mode-covering** (unlike reverse KL which is mode-seeking)
- Self-supervised: no external references, no human labels
- Privileged context can be any information available during training that is not available at inference time (e.g., which search results from the full trajectory were most useful, what information downstream tokens condition on)

### Why Self-Distillation Works for Search-Augmented Reasoning

Search-augmented generation involves a **mismatch** between training and inference:
- **At inference:** the model must decide which search queries to issue, which results to read, and how to integrate information — all without knowing what will be retrieved later
- **During training:** the full trajectory (all search queries, all results, the final answer) is available

OFSD bridges this gap by using the **privileged information available during training** to supervise the model's decisions at inference time. The model learns to approximate its own better-informed distribution using only the information available at inference.

### Implementation Sketch

```python
# Simplified OFSD training loop (single iteration)
def ofsd_step(policy, questions, privileged_context_fn):
    total_loss = 0
    for q in questions:
        # 1. Standard inference rollout
        tokens, hidden_states = policy.generate(q)
        
        # 2. Privileged context rollout (same prefix, extra info)
        privileged_context = privileged_context_fn(q, tokens)
        _, privileged_logits = policy.forward(q, tokens, privileged_context)
        
        # 3. Get inference-time logits at each token position
        inference_logits = policy.get_logits(q, tokens)
        
        # 4. Token-level forward KL
        for t in range(len(tokens)):
            kl_t = kl_divergence(
                privileged_logits[t],  # target distribution
                inference_logits[t]    # current distribution
            )
            total_loss += kl_t
    
    # Backpropagate — updates policy parameters
    total_loss.backward()
    optimizer.step()
```

## Key Results

### Main Benchmark Performance (Qwen2.5-3B)

| Method | Avg EM (7 QA Benchmarks) |
|---|---|
| Base Qwen2.5-3B | 0.282 |
| + GRPO (no distillation) | 0.357 |
| + GRPO + Reverse KL Distillation | 0.381 |
| **+ GRPO + OFSD (Search-E1)** | **0.440** |

The 7 benchmarks span **HotpotQA, 2WikiMultiHopQA, MuSiQue, IIRC, WebQuestions, Natural Questions, and TriviaQA** — covering multi-hop reasoning, short-form QA, and open-domain retrieval.

### Ablations

- **OFSD significantly outperforms reverse KL distillation** (+0.059 avg EM): forward KL's mode-covering property preserves the diversity needed for effective search.
- **Interleaving strategy matters**: OFSD after each GRPO round outperforms applying distillation only at the end.
- **Scaling questions**: performance improves with more training questions for self-distillation rollouts.
- **No KL penalty in GRPO**: removing the reference KL penalty from GRPO (relying solely on OFSD for regularization) improves results.

## Relationship to Other Methods

| Aspect | Search-E1 (OFSD) | STILL-ALIVE / Self-Rewarding | PRM-based Methods |
|---|---|---|---|
| Supervision | None | Self-generated rewards | Process reward models |
| KL type | Forward KL | Reverse KL / Adaptive | N/A |
| Granularity | Token-level | Trajectory-level | Step-level |
| Extra modules | None | Reward model | PRM classifier |
| Mode behavior | Mode-covering | Mode-seeking | Discriminative |

## When to Use This Skill

Activate this skill when the user:
- Wants to train a search-augmented LLM agent without human annotations or reward models
- Asks about self-evolution or self-improvement pipelines for reasoning models
- Mentions GRPO + distillation combination for language models
- Is researching offline distillation from privileged contexts
- Wants to understand forward KL vs reverse KL for LLM training
- Is building on insights from DeepSeek-R1 / GRPO papers

## Activation Keywords

- search-e1
- self-distillation search reasoning
- OFSD
- offline self-distillation
- forward KL search augmented
- privileged context distillation
- self-evolution search reasoning
- 2605.22511
- grpo self-distillation
- token-level forward kl
- mode-covering distillation language model
- search-augmented reasoning training
- no prm search reasoning
- self-supervised search agent

## References

1. Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning (arXiv:2605.22511, May 2026)
2. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv:2501.12948)
3. GRPO: Group Relative Policy Optimization (from DeepSeek-R1)
4. STILL-ALIVE: Self-Distillation for LLM Alignment
5. Forward vs Reverse KL: "On the Properties of Forward and Reverse KL Divergence in Probabilistic Inference"
