---
name: belief-self-distillation-user-models
description: Belief Self-Distillation (BSD) - extract, read, and causally write a frozen LLM's implicit user model from natural conversations, no external annotations. Use for user-model interpretability, hidden-state steering that actually works, refusal-behavior intervention, and testing whether probed states have causal roles.
category: ai_collection
trigger_words: user model extraction, belief self-distillation, causal probing, linear probing, hidden-state steering, refusal intervention, user attribute inference, frozen teacher, activation steering, safety conditioning, cross-model representational geometry
---

# User Model Extraction via Belief Self-Distillation (BSD)

**Source**: arXiv:2609.31603v1 (2026-09-25) — Holmov, Huang, Bykov, Akata (University of Tübingen), cs.LG/cs.CL.

## Problem

LLMs implicitly infer who they are talking to (expertise, intent, demographics) and adapt behavior accordingly — but these **user beliefs** are invisible: linear probes show correlations, yet you cannot inspect or causally manipulate the belief itself. Conventional probing conflates "information is present in activations" with "the model uses this state as a belief."

## Core Mechanism

The **frozen LLM is its own teacher**. A compact user representation is learned by distilling the model's own beliefs about the user from **natural conversations**, without any external annotation:

1. Feed multi-turn conversations to the frozen LLM.
2. Train a low-dimensional **user-code head** (read path) that decodes the model's inferred user attributes.
3. Train the **write path**: a function that maps a user-code back into the hidden state (steering vector), so the representation is both **decodable and writable** — bridging linear probing (read-only, correlational) and causal probing (intervention-only).

This isolates not just information present in activations, but a **state whose causal role can be directly tested**: write a different user-code → behavior changes accordingly → the state is a belief, not a spurious correlate.

## Key Findings

- **Causal writability**: BSD representations enable substantially stronger interventions than matched hidden-state steering (raw activation steering underperforms because it entangles belief with other features).
- **Refusal depends on inferred user intent, not just the request**: holding the request fixed, changing the model's belief about the user **alters refusal decisions** — direct safety implication: models condition safety on whom they believe they are interacting with.
- **Cross-model regularity**: independently trained LLMs converge on a **shared geometry** for representing users — user-model structure is not model-idiosyncratic.

## Recipe

1. Freeze the target LLM. Collect (or synthesize) natural conversations with varied user personas.
2. Extract hidden states at chosen layers; train a bottleneck user-code (e.g., few-dim latent) to predict the model's own user-related behavior — self-supervised, no human labels.
3. Train the inverse map (code → hidden-state delta) so codes can be injected.
4. Validate causality: swap user-codes mid-conversation; measure downstream behavior shifts (refusal rates, tone, task adaptation).
5. Compare against: linear probes (read-only) and raw hidden-state steering (entangled) — BSD should dominate both on intervention fidelity.

## Reusable Patterns

- **Self-distillation from a frozen model** as a label-free way to externalize implicit internal models (user models, world models, self-models).
- **Read-write unified probing**: a representation is only "real" if it supports both decode and intervention. Use this criterion to separate genuine internal states from correlational artifacts.
- **Request-fixed, belief-varied intervention design**: to prove a model conditions on inferred user attributes, never vary the input — only the written belief.

**Activation**: user model extraction, belief self-distillation, causal probing, refusal intervention, activation steering, safety conditioning, cross-model geometry.
