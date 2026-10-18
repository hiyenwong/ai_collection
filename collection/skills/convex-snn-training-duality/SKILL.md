---
name: convex-snn-training-duality
description: Use for SNN training optimality via convex duality.
trigger: SNN global optimality, convex duality spike patterns, surrogate gradient guarantee, LIF threshold network convex reformulation, sampled dictionary bound
---

# Convex Optimization of SNN Training (arXiv 2605.08022v3)

First convex characterization of the optimal value of spiking neural network training. Weight-decay-regularized training of parallel recurrent threshold networks and LIF SNNs has **zero duality gap** and equals the value of a finite **convex program over realizable spike patterns** at the last hidden layer.

## Core Method

### 1. Why the reduction is non-trivial
- SNN weights are **shared across timesteps** → hidden weights must be rescaled jointly over all timesteps, with spike patterns consistent along trajectories.
- LIF neurons carry a real-valued membrane with **fixed leak and reset** → the reduction must separate removable scales from model-fixed scales.
- Tool: convex duality of parallel threshold networks (Ergen et al. 2023), extended to handle time-tied weights and the leak/reset constraints.

### 2. Scale invariance (Step 1)
Threshold activation σ_s(x) = s·I{x≥0} with trainable amplitude s is **positive-scale invariant**: σ(cx)=σ(x) for c>0. This removes hidden weights from the group-norm penalty, reducing training to a convex readout-norm problem (group-norm Ω_{p,2} regularizer, Neyshabur et al. form).

### 3. Convex program (Step 2)
Training decomposes into two stages:
- **Pattern selection**: enumerate/sample spike patterns realizable at the last hidden layer (the hard stage — a 2-hidden-layer network of width ≥ n realizes all 2^n binary patterns for general-position inputs).
- **Convex solve**: minimize convex loss + group-norm regularizer over pattern coefficients; solved exactly, duality gap certifies optimality over the dictionary.

### 4. Reconstruction (Step 3)
A convex solution yields a minimizer of the reduced problem; scaling inner weights gives an **ε-optimal network for every ε>0** (original problem minimum not attained in general). Empirically the convex optimum is sparse: 2–22 subnetworks, below the **Carathéodory bound n+1**.

### 5. Sampling guarantee (Theorem 3.6)
Since the pattern set is exponential, sample it via random "witnesses". For shallow networks (two-layer threshold, LIF, parallel LIF subnetworks), the sampled optimum approximates the complete one with high probability at width
- poly(n, 1/λ_min(K), log 1/δ)
- Reservoir tuning affects the bound **only through its kernel** (Theorem E.17); branching-ratio criticality drives θ/s→0 where the kernel converges to the arc-cosine kernel of leaky-integrated inputs.

## Algorithm Variants
| Variant | Witness source | When to use |
|---------|---------------|-------------|
| CVX | Gaussian random | Pure baseline, no pretraining |
| SG-CVX | Surrogate-gradient pretrained SNN | Best on base-2 addition (0.954 vs 0.542 SG) |
| R-CVX | Criticality-tuned spiking reservoir | Best on base-5 addition, first-last-XOR T=6 (1.000) |
| -an | Analog (membrane) readout control | Sanity check vs binary readout |

**SG-CVX hybrid**: use a surrogate-gradient-trained SNN purely as a *pattern source*, then solve the convex program over its spike patterns — beats SG training itself and certifies how far the result is from the global optimum.

## Key Experimental Results (honest reporting)
| Task | Best CVX variant | SG baseline | Reservoir R |
|------|----------------|--------------|-------------|
| Addition base-2 (T=6) | **0.954** (SG-CVX) | 0.542 | 0.904 |
| Addition base-3 | 0.366 (CVX) | 0.238 | **0.407** |
| Addition base-5 | 0.232 (R-CVX) | 0.178 | **0.357** |
| first-last-XOR T=6 | **1.000** (R-CVX) | 0.737 | 1.000 |
| first-last-XOR T=14 | 0.544 (SG-CVX) | 0.516 | 0.524 |
| MNIST-Seq T=4 | 0.851 (SG-CVX-an) | 0.852 | 0.508 |

**No witness source dominates** — test accuracy depends on pattern source. On bases 3/5 the convex variants exceed SG but trail the plain reservoir ridge baseline. At T=14 all methods are near chance.

Sampling bound empirics: ratio p*ₘ/p* grows like √n at fixed m/n, lies below C₀=√(r/√q) from m=2n; bound loose by a constant factor but √n-growth consistent over n=200–600. Tuned reservoir ≈ Gaussian witnesses. Parallel LIF subnetworks match single layer from m=4n but with worse-conditioned kernel (C₀=67 vs 42 at n=600).

## When to Use This Pattern
1. **Diagnosing SNN failures**: convex optimum separates "optimizer failure" from "architecture limits" — the two are indistinguishable without the optimal value.
2. **Certifying near-optimality**: solve convex program over sampled dictionary + report duality gap (<10⁻⁶ achievable) as optimality certificate.
3. **Reservoir computing with guarantees**: ridge readout on a fixed reservoir = special case where the readout is optimal over that reservoir's patterns and distance-to-global-optimum is bounded.
4. **Hybrid training**: SG-CVX — never trust surrogate gradients alone; use them as feature generators then polish with the exact convex solve.

## Implementation Sketch
```
1. Generate m spike-pattern witnesses (Gaussian / pretrained-SG / tuned reservoir)
2. Simulate LIF dynamics forward → collect last-hidden-layer binary patterns D ∈ {0,1}^(n×m_distinct)
3. Solve min_w L(Dw, Y) + Ω(w)  (convex, group-norm regularizer)
4. Read support size vs Carathéodory bound n+1 (sparsity diagnostic)
5. Reconstruct network: assign each support pattern a hidden neuron, scale inner weights → ε-optimal SNN
6. Report: train fit, test acc, duality gap, support size, m/n ratio vs C₀
```

## Limitations
- Exponential pattern space ⇒ sampling needed even for shallow nets; deep nets lack the guarantee.
- Parallel (non-recurrent-hidden) architecture class only — the convex result covers threshold RNNs where recurrence enters through inputs, not arbitrary recurrent weight topologies.
- Original non-attained minimum means reconstruction is ε-optimal, not exact.

## References
- Udupi, Ang, Kim, Yang, Zhai. "Convex Optimization of Spiking Neural Networks with Global and Approximation Guarantees." arXiv:2605.08022v3 (Oct 2026).
- Ergen et al. 2023 (convex duality of parallel threshold networks), Pilanci & Ergen 2020 (ReLU convex reformulation), Kim & Pilanci 2024 (sampled convex relaxation), Becchetti et al. 2026 (dimension-free rank lifting).