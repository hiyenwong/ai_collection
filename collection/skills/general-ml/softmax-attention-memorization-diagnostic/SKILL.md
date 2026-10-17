---
name: softmax-attention-memorization-diagnostic
version: v1.0.0
last_updated: 2026-10-17
description: "Detect attention memorization via weight-spread metric."
arxiv_id: "2610.22191"
authors: "Francesco Alemanno"
tags: [hopfield-networks, attention, statistical-mechanics, memorization, generalization]
---

# Attention over Noisy Examples: Generalization vs Memorization in Exponential Hopfield Networks

From arXiv:2610.22191 (2026-10-15).

## Problem

Hebbian learning from blurred examples: a Hopfield network of N neurons sees M noisy examples of each of K archetypes. Can it infer the archetypes? Depends on load α=K/N (interference) and dataset entropy ρ=(1−r²)/(Mr²) (how little the examples say). Transferred to the exponential Hopfield model, whose zero-temperature update is one step of **softmax attention with unlabelled examples as keys**.

## Method

Closed-form signal-to-noise analysis:

1. Overlap with unseen archetype: m⁽¹⁾ = erf(1/√(2ρ_eff)) — the pairwise majority-rule law with ρ replaced by an **attention entropy ρ_eff** built from the softmax weight on the correct class and how many examples it spreads over.
2. In a √N-wide window of inverse temperatures β, interference between archetypes is exponentially small in Nβ: **load drops out**, learnable archetypes grow as exp(c√N).
3. Failure mode differs: pairwise model fails via spin-glass phase; exponential model fails via **memorization** — softmax concentrates weight on the training example closest to the input and returns it instead of the archetype. Seen from the input, softmax weights match the **random energy model**; memorization is its freezing transition at β√(N(1−r²)) ≃ √(2 ln M).
4. Measurable diagnostic: count how many examples carry weight on a head whose keys are examples. On MNIST follows random-energy prediction; on fashion-MNIST detects class sub-clusters, with best accuracy lying **beyond** the memorization threshold (softmax reads out a local sub-prototype).

## Reusable Pattern

**Weight-spread as a memorization/freezing diagnostic for attention heads.** For any attention head whose keys are training examples (retrieval-augmented, example-based in-context learning, nearest-neighbor attention), the effective number of examples carrying attention weight is a cheap, training-free indicator of whether the head generalizes (weight spread over a class) or memorizes (weight collapsed onto single examples). The transition threshold scales as √(N·noise) vs ln M, so more examples or more noise push toward collapse. Useful for auditing RAG heads, kNN-LM lookups, and few-shot attention layers.

## Resources

- Paper: https://arxiv.org/abs/2610.22191
