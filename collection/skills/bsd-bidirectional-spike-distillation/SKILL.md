---
name: bsd-bidirectional-spike-distillation
description: Use when SNNs must learn on-device while inferring.
category: ai_collection
trigger_words: [on-device learning, spiking neural network, local learning, bidirectional distillation, edge intelligence, learning while inferring, few-shot incremental]
---

# Bidirectional Spike-Based Distillation (BSD) — Learning While Inferring

**Source**: "Learning While Inferring: Local and Parallel Learning for Edge SNNs across Sensing Modalities" — Zhang et al., Fudan (arXiv:2610.03149, Oct 2026)

## Core Insight

Surrogate-gradient backpropagation (BP) **serializes** training: the backward pass blocks inference, dense float backward chains blow the energy/memory budget of edge devices. BSD replaces BP with **two disjoint computation graphs** that align mid-layer:

- **Forward branch**: stimulus-driven, event-based SNN — runs inference continuously.
- **Reverse branch**: target-driven (labels/strong teacher activations), independent graph, runs concurrently.
- **Local alignment objectives**: match intermediate representations stage-by-stage between branches.

Because the graphs only meet at alignment points, forward inference, reverse inference, and stage-wise updates run **in parallel**. At deployment only the forward branch ships.

## Performance Profile (25 SOUL benchmarks, 5 sensing modalities)

| Metric | Value |
|--------|-------|
| Accuracy vs matched BP | within 3.8 pp average |
| Training latency | 0.72× BP |
| Training energy | 0.36× BP |
| Few-shot class-incremental | transfers without replay |

## Implementation Recipe

1. Build forward SNN `F(x)` (LIF neurons, event-driven, integer-friendly dynamics).
2. Build reverse network `R(y)` driven by targets/teacher outputs, architecturally mirrored so stage `k` of `R` aligns with stage `k` of `F`.
3. At each stage pair `(F_k, R_k)` add a **local alignment loss** — cosine/symmetric-distance between intermediate representations; never backprop across stages.
4. Update each stage with the local loss only (e.g., e-prop style local gradients or direct alignment gradients).
5. Schedule forward and reverse passes concurrently on separate execution resources (separate cores/threads; forward keeps real-time inference obligations).
6. Deploy: drop `R`, keep `F`.

## Key Design Rules

- **Disjoint graphs until alignment** is the entire point — any cross-stage backward edge reintroduces the serialization bottleneck.
- Reverse branch may be *stronger* (teacher with privileged inputs) — distillation flows naturally.
- Local losses should be symmetric (align both ways) to avoid collapse toward the target branch.
- For few-shot incremental: freeze old stages' alignment losses or use feature-isolation; BSD representations transfer without replay buffers.

## Relation to Prior Skills
- Complements `mdtf-temporal-fusion-local-snn` (feedforward local training) — BSD adds the concurrent reverse-branch trick.
- Complements `spikecredit-temporal-credit-carrier` — BSD replaces global credit assignment with stage-local alignment.
- Contrast `surrogate-gradient-snn-training` — keeps full backprop; use BSD when the backward chain is the bottleneck (energy <0.5×, latency <1× available).

## Activation

Use this skill when: deploying SNNs on edge hardware that must adapt on-device (robotics, wearables, sensor nodes), when BP backward chains violate real-time inference, for few-shot class-incremental SNN adaptation without replay memory, or when estimated training energy must drop below half of BP.
