---
name: falcon-snn-latency-pipeline-delay
version: v1.0.0
last_updated: 2026-09-30
description: "Falcon methodology — optimizing SNN latency via per-layer Pipeline Delay Search with a counterintuitive proof that more input-waiting can make SNNs both slower AND less accurate, plus spike-based QAT and threshold tuning. Use when: (1) SNN multi-timestep latency exceeds budget, (2) overlapping layers across timesteps for speed, (3) analyzing latency-accuracy tradeoffs on analog CIM hardware. Keywords: SNN latency, pipeline delay search, timestep overlap, spike QAT, compute-in-memory."
arxiv_id: "2609.35260"
authors: "Zhanglu Yan, Zixuan Zhu, Kaiwen Tang et al. (6 authors)"
tags: [snn, latency, pipeline, quantization-aware-training, compute-in-memory, edge]
---

# Falcon: Fine-Grained SNN Latency Analysis and Pipeline Delay Optimization

From arXiv:2609.35260 (2026-09-28).

## The Counterintuitive Core

Standard belief: SNN multi-timestep execution ⇒ slower than quantized NNs (QNNs). **False** — with **cross-layer timestep overlap** (layer l+1 starts computing on partial inputs from layer l), SNNs can finish *faster* than bit-serial QNNs.

But overlap requires firing on **incomplete inputs**, and **a spike cannot be withdrawn** — an early wrong spike persists downstream. The naive fix — wait longer for more input before firing — is assumed to trade speed for accuracy. **The paper proves this intuition fails**: at some layers, even a small added delay changes spike timing and downstream computation, making the network **both slower AND less accurate**.

## Falcon Framework

1. **Pipeline Delay Search**: select each layer's waiting delay by balancing **task-level accuracy** against **added network latency** — a per-layer search over the delay knob, evaluated at the end-to-end level (not per-layer proxies).
2. **Spike-based QAT**: quantization-aware training adapted to spike dynamics.
3. **Bounded tuning** of firing thresholds and initial membrane potentials.

Target mapping: spatial analog compute-in-memory (CIM) with shared digital engines.

## Implementation Pattern

```
for each layer l:  candidate delays D_l ∈ {0, 1, ..., T_max}
search: per-layer delay assignment d = (d_1..d_L)
objective: minimize (modeled_network_latency(d))
           s.t. task_accuracy(model with d) ≥ target
evaluate: full-network latency model + real task accuracy
         (per-layer accuracy proxies are unreliable —
          the spike-irreversibility coupling defeats them)
then: spike-QAT + bounded threshold/V0 tuning on selected config
```

## Key Results (GSCV2 / SSC speech command)

| Benchmark | Accuracy | Modeled network-core latency |
|---|---|---|
| GSCV2 | 96.31 | 119.64 µs |
| SSC | 83.02 | 124.00 µs |

Competitive accuracy at **microsecond-scale** modeled latency.

## When to Use

- Low-latency edge audio/command recognition with SNNs on analog CIM hardware.
- Any SNN deployment where latency (not just energy) is the binding constraint.
- Deciding per-layer firing delays — never assume "wait more = more accurate"; measure task-level.

## Design Notes

- **Spike irreversibility** is the structural cause of the non-monotonicity: an early spike is a committed bit of computation. Delays shift *which* spikes fire early, coupling layers in ways per-layer analysis misses.
- Latency model must be end-to-end (pipeline overlap makes per-layer sums wrong).
- The delay-accuracy non-monotonicity result generalizes: any irreversible-event streaming system (event cameras, neuromorphic sensors) has the same failure mode when tuning event buffering.
