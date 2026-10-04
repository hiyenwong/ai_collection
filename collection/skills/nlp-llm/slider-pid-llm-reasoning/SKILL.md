---
name: slider-pid-llm-reasoning
description: Use when auditing LLM reasoning trajectories for redundancy.
category: ai_collection
---

# SLIDER: PID-Based LLM Reasoning Audit

**Paper**: Interpreting Reasoning of Large Language Models via Partial Information Decomposition (arXiv:2610.00571, Halder, Zhang, Dutta — UMD/Elorian AI, Sep 2026)

## Core Insight

Apply Partial Information Decomposition (PID) to *consecutive reasoning steps* of a Large Reasoning Model (LRM): disentangle the answer-relevant information in step S_i into non-negative components — unique (in S_i, in past steps S_<i), redundant, and synergistic — then detect repetitive reasoning as redundancy-dominant steps.

## Formal Definitions

**PID unique information** (Bertschinger et al. 2014):
```
Δ_P = {Q_AXY : Q_AX = P_AX, Q_AY = P_AY}  # same marginals
Uni(A:X|Y) := min_{Q ∈ Δ_P} I_Q(A;X|Y)
```
Any one PID term suffices to derive the rest (redundancy/synergy closure).

**Step-RRI (Definition 2)** — step-level repetitiveness:
```
RRI_i = Red(A: S_i, S_<i) − η · max{Uni(A:S_i|S_<i), Syn(A:S_i,S_<i)},  η ≥ 1
```
RRI_i > 0 ⟺ current step is redundancy-dominant (repetitive). When S_i repeats logic already in S_<i (relevant part S_A ⊆ S_<i): Uni and Syn are provably 0 and RRI_i = Red > 0 (Theorem 2).

**Trajectory-RRI (Definition 3)** — per-question aggregate:
```
RRI(Q) = Σ_{i=2..T} 𝟙[RRI_i > 0]   # count of repetitive steps
```

**Theorem 1 (Uniqueness under noise)**: injecting independent noise N ⊥ (A, S_i, S_{i-1}) into a step strictly decreases its unique information: Uni(A:S_i|S_{i-1}) ≥ Uni(A:S_i'|S_{i-1}). Error detection = unique-info drop.

## Implementation Pipeline

1. **Segment** trajectory into steps S_1..S_T and final answer A.
2. **Structure-preserving sample generation**: use an LLM (GPT-4o-mini in paper) to generate *numerical variants* of the same question — only numbers change, step structure/order/correspondence preserved. A variant is accepted only if trajectory steps align 1:1. These aligned samples give the joint distribution needed for PID estimation.
3. **PID estimation**: CVX estimator (Liang et al. 2023) over (A, S_i, S_<i) triples from the variant ensemble.
4. **Compute RRI_i, aggregate Trajectory-RRI.**

## Empirical Results

- PRMBench redundancy class: step-level redundancy detection **+10 pts accuracy** over embedding-similarity and InfoGain baselines.
- Average Trajectory-RRI **strongly correlates with reasoning length** across QwQ-32B, DeepSeek-R1-Distill-Qwen-32B, GPT-4.1 (GSM8K + AIME2025).
- **Trajectory-RRI-guided SFT data selection**: fine-tuning Qwen2.5-7B-Instruct (LoRA) on low-RRI trajectories → reasoning efficiency (LLM-judged) negatively correlated ρ = −0.97 with training-data average Trajectory-RRI, task performance largely preserved.

## Reusable Patterns

1. **Redundancy-vs-uniqueness contrast index**: for any step-level quality signal, use `dominant_term − η·max(other_terms)` rather than raw similarity — it is threshold-free and monotone under adversarial side information.
2. **Variant-ensemble distribution estimation**: when direct joint distributions over text are intractable, generate structure-preserving numerical variants and treat step correspondence as i.i.d. samples. Applicable to any step-level information measure (info-gain, entropy drop, PID).
3. **Noise-injection as ground truth**: Theorem 1 justifies synthetic noise injection as a *causal* probe for step contribution — perturb one step, measure unique-info decrease.
4. **Data-selection signal**: aggregate per-example redundancy counts (Trajectory-RRI) as a cheap proxy for fine-tuning data quality filtering.

## Limitations

- Depends on LLM quality for structure-preserving variant generation.
- Experiments focus on mathematical reasoning; broader domains untested.
- PID estimation in high-dimensional continuous settings is non-trivial (CVX estimator used).

## Activation

partial information decomposition, PID, reasoning redundancy, repetitive reasoning, Step-RRI, Trajectory-RRI, reasoning interpretability, LRM audit, reasoning efficiency, fine-tuning data selection, PRMBench