---
name: hes-data-selection-reasoning
description: "HES (High-Entropy Sum) methodology from arXiv:2605.22389 (May 2026). Training-free metric for LLM reasoning data selection: sums entropy of top-k highest-entropy tokens per reasoning sample. Effective across SFT, RFT, and RL training paradigms. Use when: LLM reasoning data curation, data quality filtering, rejection sampling for reasoning, RL training data selection, long-CoT data filtering."
---

# HES: Unified Data Selection for LLM Reasoning via High-Entropy Sum

**arXiv:** 2605.22389 | **Date:** May 2026

---

## Overview

HES (High-Entropy Sum) is a **training-free** metric for quantifying the reasoning quality of individual data samples in LLM training. It operates on a simple yet powerful insight: in a reasoning trajectory (e.g., chain-of-thought), **not all tokens carry equal information about reasoning quality**. Tokens with high output entropy reflect points of genuine cognitive difficulty, branching decisions, and reasoning steps — while low-entropy tokens correspond to rote or predictable continuations (e.g., "Let me", "Therefore", "So").

Rather than averaging entropy over all tokens (which dilutes the signal), HES **sums only the entropy values of the top-k highest-entropy tokens** in each sample. This preserves the signal from critical reasoning junctures while ignoring predictable filler.

---

## The HES Metric

Given a language model `p` and a reasoning sample `x = (x_1, ..., x_T)`, the token-level entropy at position `t` is:

```
H_t = -sum_{v in V} p(v | x_<t) * log p(v | x_<t)
```

The HES score is then:

```
HES_k(x) = sum_{t in TopK({H_t})} H_t
```

Where `TopK({H_t})` selects the indices of the `k` tokens with the highest entropy values. The paper finds **k = top 5–10% of tokens** works best empirically. The metric is:

- **Training-free**: computed using a single forward pass of the model on each candidate sample
- **Model-agnostic**: can use any base LLM (the paper validates on Qwen2.5)
- **Sample-level**: produces a single scalar per reasoning trajectory

### Why Summation (not Mean)?

The mean entropy dilutes reasoning signal because most tokens in a long CoT are low-entropy (connective phrases, repetitive patterns). Summation over only top-k tokens retains the magnitude of high-entropy peaks. This is crucial — a long, carefully reasoned trajectory has many high-entropy tokens; a short, shallow one does not. Summation naturally rewards **both depth and quality** of reasoning.

---

## Validation Across Training Paradigms

HES is validated across the three major LLM training paradigms:

### 1. Supervised Fine-Tuning (SFT)

- **Setup**: Qwen2.5-7B-Instruct trained on MATH + GSM8K
- **Full dataset**: 100K reasoning samples
- **HES selection**: Top 20% HES-ranked samples (20K)
- **Result**: HES-selected 20% **matches full-dataset performance** while using 80% less data

| Method | Data Size | MATH Acc | GSM8K Acc |
|--------|-----------|----------|-----------|
| Full dataset | 100K | 72.5% | 88.1% |
| HES top 20% | 20K | **72.8%** | **88.3%** |
| Random 20% | 20K | 69.2% | 85.7% |
| Perplexity top 20% | 20K | 70.1% | 86.2% |
| Instruction-Following top 20% | 20K | 71.0% | 86.9% |

### 2. Rejection Fine-Tuning (RFT)

- **Setup**: Generate multiple candidate trajectories per problem; select best ones for SFT
- **HES selection**: Choose samples with highest HES scores among all generated trajectories
- **Result**: HES-based RFT **significantly outperforms** standard correctness-based rejection sampling

| Method | MATH Acc | GSM8K Acc |
|--------|----------|-----------|
| Correct-only RFT | 74.1% | 89.2% |
| HES-selected RFT | **76.8%** | **91.0%** |
| Random RFT | 71.5% | 87.3% |

Key insight: **Correct trajectories vary in reasoning quality**. A correct but shallow trajectory (many lucky guesses) has lower HES than a correct trajectory with deep reasoning steps. HES selects trajectories that are both correct and reasoning-rich.

### 3. Reinforcement Learning (RL)

- **Setup**: GRPO-based RL training on mathematical reasoning
- **Two-stage approach**: Generate trajectories → HES-score them → select top-HES successful trajectories for RL training
- **Result**: HES-selected successful trajectories enable **strong reasoning patterns** that generalize better

| Method | MATH Acc | GSM8K Acc | Minerva Math |
|--------|----------|-----------|-------------|
| GRPO (all trajectories) | 78.2% | 92.1% | 35.4% |
| GRPO (HES-selected) | **80.5%** | **93.4%** | **38.1%** |
| GRPO (random selected) | 77.0% | 91.2% | 34.8% |

---

## Implementation

### Pseudocode

```python
import torch
import torch.nn.functional as F

def compute_hes_score(model, tokenizer, sample_text: str, k: float = 0.05) -> float:
    """
    Compute HES score for a single reasoning sample.

    Args:
        model: HuggingFace transformer model
        tokenizer: Corresponding tokenizer
        sample_text: The reasoning trajectory text
        k: Fraction of tokens to keep (top-k highest entropy). Default 0.05 (top 5%)

    Returns:
        HES score (float)
    """
    inputs = tokenizer(sample_text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits[0, :-1]  # shape: (seq_len-1, vocab_size)
        probs = F.softmax(logits, dim=-1)  # (seq_len-1, vocab_size)
        entropy = -torch.sum(probs * torch.log(probs + 1e-10), dim=-1)  # (seq_len-1,)

    # Select top-k highest entropy tokens
    n_tokens = len(entropy)
    n_select = max(1, int(n_tokens * k))
    topk_entropies, _ = torch.topk(entropy, n_select)
    hes = topk_entropies.sum().item()
    return hes
```

### Practical Usage

```python
# Scoring a dataset for SFT filtering
def score_dataset(model, tokenizer, dataset):
    scores = []
    for sample in dataset:
        text = tokenizer.apply_chat_template(sample["messages"], tokenize=False)
        hes = compute_hes_score(model, tokenizer, text)
        scores.append((sample, hes))
    # Sort by HES descending, take top 20%
    scores.sort(key=lambda x: x[1], reverse=True)
    top_samples = [s[0] for s in scores[:len(scores) // 5]]
    return top_samples
```

### Recommended Hyperparameters

| Setting | `k` value (top-k fraction) | Selection Ratio |
|---------|---------------------------|-----------------|
| SFT filtering | 0.05–0.10 | Top 20% |
| RFT (rejection sampling) | 0.05–0.10 | Top 30–50% of correct trajectories |
| RL training data | 0.05 | Top 50% of successful trajectories |

---

## Key Results Summary

| Paradigm | Finding | Data Efficiency Gain |
|----------|---------|---------------------|
| **SFT** | Top 20% HES-ranked data matches full 100K dataset performance | **5× data reduction** |
| **RFT** | HES-selected correct trajectories outperform correctness-only selection | **+2.7% MATH, +1.8% GSM8K** |
| **RL** | HES-selected successful trajectories boost GRPO | **+2.3% MATH, +1.3% GSM8K, +2.7% Minerva** |
| **All** | Consistent gains over perplexity, IF, and random baselines | Robust across paradigms |

### Why HES Works

1. **Captures reasoning depth**: High-entropy tokens correspond to genuine reasoning branch points, not rote patterns
2. **Length-aware but not length-dominated**: Summation rewards longer trajectories with more reasoning depth, but the top-k mechanism prevents padding/verbosity from gaming the score
3. **Training-free**: Requires only a forward pass — no auxiliary models, no reward model, no labeling
4. **Model-agnostic**: Validated on Qwen2.5 series; applies to any autoregressive LLM

---

## Relationship to Other Methods

| Method | HES Comparison |
|--------|---------------|
| **Perplexity** | PPL measures token likelihood, which correlates with topic familiarity more than reasoning quality. Low PPL often means "typical text," not "good reasoning." |
| **Instruciton-Following (IF)** | IF scores measure instruction compliance, not reasoning depth. A correct answer with minimal reasoning may score high on IF but low on HES. |
| **Correctness filtering** | Correctness is binary per-sample in RFT; HES provides a continuous ranking of reasoning quality among correct samples. |
| **Process Reward Models (PRM)** | PRMs require step-level human labels or synthetic data. HES is training-free and provides a complementary signal. |
| **Length filtering** | Length alone is a weak proxy; HES uses entropy structure, not just token count. |

---

## Activation Keywords

- Data curation for LLM reasoning
- Reasoning data quality filtering
- High-entropy sum
- Training-free data selection
- Chain-of-thought data filtering
- Rejection fine-tuning data selection
- RL data selection for reasoning
- Long-CoT data pruning
- Reasoning trajectory scoring
- Sample-level reasoning quality metric
- SFT data efficiency
- GRPO data selection
- Mathematical reasoning data
- HES metric

---

## References

- **Paper**: arXiv:2605.22389 (May 2026) — *Unified Data Selection for LLM Reasoning via High-Entropy Sum*
- **Base model**: Qwen2.5 series (7B, 14B, 72B)
- **RL algorithm**: GRPO (Group Relative Policy Optimization)
- **Related**: DeepSeek-R1, STILL-ALIVE, process reward models, rejection sampling

---

*Skill auto-generated from arXiv:2605.22389. For the latest version, consult the paper directly.*
