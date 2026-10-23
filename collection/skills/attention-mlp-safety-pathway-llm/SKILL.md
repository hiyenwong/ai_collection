---
name: attention-mlp-safety-pathway-llm
description: Mechanistic LLM safety pathway: attention reads harmfulness, MLP writes refusal. Use for jailbreak/over-refusal analysis and safety routing.
category: ai_collection
---

# Attention-MLP Safety Pathway in LLMs

Methodology from "Attention Sees, MLP Refuses: Tracing the Attention-to-MLP Safety Pathway in LLMs" (arXiv:2610.13078, Weng, He, Jin, Huang, Bai). Decomposes LLM safety into a two-stage residual-stream pathway and exploits the split for detection + routing.

## Core Mechanistic Finding

In decoder-only Transformers, safety is a PATHWAY, not a single module property. Separate two distinct computations:

- **Harmfulness recognition (perception)**: decodable predominantly from **attention** module updates, strongest in EARLY layers. Present in base models — post-training does NOT systematically improve it.
- **Refusal writing (decision)**: carried by **MLP** updates, concentrated in DEEPER layers, systematically STRENGTHENED by instruction tuning/post-training across all 18 Base-Instruct pairs (Qwen, Llama, Gemma).

Causal direction: attention perceives → MLP converts perception into readable refusal. Resetting downstream MLP updates to clean values substantially reduces the refusal shift caused by upstream attention interventions (pathway confirmed causally, 18 model pairs + 6 reasoning-enabled models).

Reasoning-model corollary: harmfulness stays decodable THROUGHOUT reasoning chains, but strong refusal writing concentrates at ANSWER ONSET — the pattern persists with reasoning disabled, i.e. it is a structural property of alignment, not reasoning dynamics.

## Two-Score Sentinel Framework

- **P (perception score)**: attention-derived harmfulness evidence — how much harmfulness information the model has actually SEEN.
- **D (decision score)**: MLP-derived refusal-writing evidence — whether the model is acting on it.

Joint profile P×D characterizes failure modes:

| P | D | Interpretation |
|---|---|---|
| High | High | Normal safe refusal |
| High | Low | **Jailbreak**: model perceived harm but refuses to write refusal — attack suppressed the MLP decision stage |
| Low | High | **Over-refusal**: benign query, but MLP writes refusal anyway (false-positive safety) |
| Low | Low | Genuinely benign processing |

Conditional routing on both signals achieves lower aggregate error than any single-signal router or fixed system-reminder, evaluated across 8 models.

## Reusable Patterns

1. **Residual-stream readout protocol**: decode harmfulness info from module updates (what a module EXPOSES) separately from the change it produces in refusal evidence (what it WRITES). The exposure/write split generalizes to any behavior-tracing task beyond safety.
2. **P/D instrumentation**: for any "perception→action" behavior pair, derive module-specific scores and route on their joint profile instead of one aggregate probe — misalignment lives in the disagreement between the two.
3. **Intervention ladder for pathway confirmation**: (a) correlate, (b) intervene upstream (attention), (c) reset downstream (MLP) to clean values, (d) measure shift attenuation. Applicable to any hypothesized module-to-module causal chain.
4. **Jailbreak localization**: a jailbroken response with high P means perception survived and only the decision stage was bypassed — target re-alignment at MLP refusal-writing; low-P jailbreaks indicate input-level obfuscation instead.
5. **Over-refusal debugging**: high D on benign inputs identifies over-triggered refusal writing; the attention record proves no harmfulness was ever seen.

## Scope

Verified on 18 Base-Instruct pairs (Qwen/Llama/Gemma families) + 6 reasoning-enabled models; causal interventions support the directionality. Sentinel routing evaluated on 8 models. The pathway split is architecture-level (decoder-only residual stream); encoder or MoE-routing effects untested.
