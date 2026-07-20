---
name: avsd-adaptive-view-self-distillation
description: "AVSD (Adaptive-View Self-Distillation) methodology from arXiv:2605.20643 (May 2026). Multi-view self-distillation separating consensus from view-specific residual signals for token-level supervision in LLM self-training. Use when: multi-view distillation, self-distillation with privileged information, token-level supervision, consensus-residual decomposition, LLM reasoning improvement."
---

# AVSD: Adaptive-View Self-Distillation

**Paper:** *AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals* (arXiv:2605.20643, May 2026)

## Overview

AVSD is a **multi-view self-distillation** framework for token-level supervision in large language model (LLM) self-training. Standard self-distillation uses a single frozen teacher to generate supervisory signals for a student model. AVSD instead employs **multiple teacher views** (different checkpoints, decoding strategies, or augmentation conditions) and decomposes their supervisory signals into two components:

1. **Consensus signal** — the component shared across all teacher views (stable, reliable update direction)
2. **View-specific residual signal** — the component unique to each teacher view (potentially noisy but contains privileged information)

The key insight: cross-view consensus represents trustworthy knowledge worth propagating, while view-specific residuals provide additional signal that must be selectively gated to avoid injecting noise.

## The Multi-View Privileged Information Problem

Standard single-teacher self-distillation suffers from:

- **Bias amplification** — teacher errors are propagated to the student
- **Limited supervision diversity** — a single view cannot capture the full distribution of plausible next-token probabilities
- **Overconfidence in weak teachers** — fixed teachers may have high confidence on incorrect tokens

Multi-view setups introduce a new challenge: **how to aggregate multiple, possibly conflicting, teacher signals** without averaging away useful information or amplifying noise.

Naive approaches fail:
- **Averaging** all teacher logits washes out sharp, informative signals
- **Max-confidence** selection amplifies the most overconfident (often wrong) teacher
- **GRPO-based** group-relative policy optimization treats all views equally without structural decomposition

## Consensus-Residual Decomposition

Given a set of $K$ teacher views, each producing a logit distribution $p_k(y_t | x, y_{<t})$ at token position $t$, AVSD decomposes:

**Consensus signal** $c_t$:
$$
c_t = \mathbb{E}_{k \in \mathcal{V}}[p_k(y_t)]
$$

This is the average logit distribution across all views — capturing what all teachers agree on. This component provides a **stable, low-variance** update direction that penalizes the student for deviating from commonly-held beliefs.

**View-specific residual** $r_t^{(k)}$:
$$
r_t^{(k)} = p_k(y_t) - c_t
$$

Each teacher's unique deviation from consensus. This captures **privileged information** — insights that only a particular teacher view possesses (e.g., a specific decoding strategy's preference for certain reasoning patterns).

**Reconstruction**:
$$
p_k(y_t) = c_t + r_t^{(k)}
$$

Every teacher signal is the sum of shared consensus and a private residual.

## Selective Residual Gating

The core contribution of AVSD is an **adaptive gating mechanism** that selectively admits view-specific residuals into the student's training loss. The gate has two conditions:

### Condition 1: Directional Alignment (Consistency)
The residual must **point in the same direction** as the consensus. Measured by the cosine similarity between the residual vector and the consensus vector:

$$
g_{\text{align}}^{(k,t)} = \mathbb{1}\left[ \cos(r_t^{(k)}, c_t) > \tau_{\text{align}} \right]
$$

This prevents the student from being pulled in a direction that contradicts the majority consensus.

### Condition 2: Proportionality (Magnitude)
The residual's magnitude must be **proportionate** — not so large that it dominates the consensus signal:

$$
g_{\text{prop}}^{(k,t)} = \mathbb{1}\left[ \|r_t^{(k)}\|_2 < \lambda \cdot \|c_t\|_2 \right]
$$

where $\lambda$ is a proportionality hyperparameter (typically 1.0–2.0).

### Gated Residual
The final residual used for training:

$$
\hat{r}_t^{(k)} = r_t^{(k)} \cdot g_{\text{align}}^{(k,t)} \cdot g_{\text{prop}}^{(k,t)}
$$

### Training Objective (per token)
$$
\mathcal{L}_t = \underbrace{\text{KL}(c_t \parallel p_{\text{student}}(y_t))}_{\text{consensus distillation}} + \alpha \cdot \frac{1}{K} \sum_{k=1}^K \underbrace{\text{KL}(c_t + \hat{r}_t^{(k)} \parallel p_{\text{student}}(y_t))}_{\text{gated privileged distillation}}
$$

where $\alpha$ balances the consensus and residual terms.

## Key Design Choices

| Component | Purpose |
|---|---|
| **Multi-view teachers** | Different checkpoints, temperatures, decoding strategies, or data augmentations |
| **Consensus signal** | Reliable, low-variance supervision — always used |
| **Directional alignment gate** | Prevents contradictory updates from view-specific signals |
| **Proportionality gate** | Prevents any single view from dominating the training |
| **Gated residual term** | Selectively enriches the student with useful privileged information |
| **$\alpha$ hyperparameter** | Balances consensus vs. residual influence (default: 0.5–1.0) |

## Results

### Math Reasoning (Avg@8)

| Model | Baseline | GRPO | Single-View SD | AVSD (Ours) | Gain |
|---|---|---|---|---|---|
| **Qwen3-8B** | 67.8% | 69.0% | 69.5% | **72.6%** | **+3.1%** |
| **Qwen3-4B** | 59.3% | 60.8% | 61.3% | **63.5%** | **+2.2%** |

AVSD outperforms:
- Single-view self-distillation (strongest baseline)
- GRPO (group-relative policy optimization)
- Direct multi-view averaging (ablated at 70.1%)
- Max-confidence multi-view selection (ablated at 68.4%)

### Code Reasoning

| Benchmark | Single-View SD | AVSD | Improvement |
|---|---|---|---|
| **Codeforces** | 31.2% | **33.8%** | +2.6% |
| **LiveCodeBench** | 28.9% | **31.1%** | +2.2% |
| **Combined** | — | — | **+2.4%** |

### Ablations

- **Removing directional alignment gate:** -1.8% on Avg@8 (noisy updates hurt)
- **Removing proportionality gate:** -1.2% on Avg@8 (occasional residual domination)
- **Removing both gates (full residual always on):** -2.7% on Avg@8 (equivalent to naive multi-view averaging)
- **Reducing $\alpha$ to 0 (consensus-only):** -1.5% on Avg@8 (privileged signal matters)
- **Using only 2 views vs. 8 views:** -1.9% on Avg@8 (more views = better consensus)

## Implementation Sketch

```python
def avsd_loss(student_logits, teacher_logits_list, alpha=0.7, tau_align=0.3, lam=1.5):
    """
    Args:
        student_logits: [B, T, V] student output logits
        teacher_logits_list: list of [B, T, V] from K teacher views
        alpha: residual loss weight
        tau_align: directional alignment threshold
        lam: proportionality ratio threshold
    """
    K = len(teacher_logits_list)
    
    # 1. Compute consensus signal
    consensus = torch.stack(teacher_logits_list, dim=0).mean(dim=0)  # [B, T, V]
    consensus_probs = F.softmax(consensus, dim=-1)
    
    # 2. Compute residuals and gating for each teacher view
    gated_residuals = []
    for k in range(K):
        residual = teacher_logits_list[k] - consensus  # r_t^(k)
        r_probs = F.softmax(residual, dim=-1)
        c_probs = consensus_probs
        
        # Directional alignment: cosine similarity
        cos_sim = F.cosine_similarity(r_probs.flatten(1), c_probs.flatten(1), dim=-1)
        align_mask = (cos_sim > tau_align).float()  # [B]
        
        # Proportionality: residual magnitude vs consensus magnitude
        r_norm = torch.norm(r_probs.flatten(1), dim=-1)
        c_norm = torch.norm(c_probs.flatten(1), dim=-1)
        prop_mask = (r_norm < lam * c_norm).float()  # [B]
        
        # Combined gate
        gate = align_mask * prop_mask  # [B]
        gated_res = residual * gate.unsqueeze(-1).unsqueeze(-1)  # [B, T, V]
        gated_residuals.append(gated_res)
    
    # 3. Consensus distillation loss
    loss_consensus = kl_divergence(consensus_probs, student_probs)
    
    # 4. Gated privileged distillation loss
    loss_privileged = 0.0
    for k in range(K):
        privileged_target = consensus + gated_residuals[k]
        privileged_probs = F.softmax(privileged_target, dim=-1)
        loss_privileged += kl_divergence(privileged_probs, student_probs)
    loss_privileged /= K
    
    return loss_consensus + alpha * loss_privileged
```

## Relation to Other Methods

| Method | Relation to AVSD |
|---|---|
| **Standard self-distillation** | Single-teacher subset; AVSD generalizes to multi-view |
| **GRPO** | Group-relative advantage, no structural decomposition; AVSD's consensus-residual separation is principled |
| **SPIN / Reverse KL distillation** | Iterative self-play; AVSD uses concurrent multi-view |
| **Ensemble distillation** | Averages teachers; AVSD selectively keeps residual information |
| **Multi-agent debate / self-consistency** | Uses multiple samples, but at inference; AVSD is a training-time method |

## Activation Keywords

- `multi-view self-distillation`
- `adaptive-view self-distillation`
- `AVSD`
- `consensus-residual decomposition`
- `token-level supervision`
- `privileged signal gating`
- `cross-view consensus`
- `view-specific residual`
- `directional alignment gate`
- `proportionality gate`
- `LLM self-training`
- `multi-teacher distillation`
- `self-distillation with privileged information`
- `consensus distillation`
- `group-relative policy optimization alternative`
- `selective residual gating`
- `balanced multi-view training`
