---
name: ctm-fixed-point-curve-non-normal-thought
description: "Use when analyzing recurrent 'thinking' models mechanistically. Moving attracting fixed points + balanced amplification explain CTM thought trajectories."
tags: [neuroscience, recurrent-networks, continuous-thought-machine, non-normal-dynamics, fixed-points]
category: ai_collection
---

# Riding the Fixed-Point Curve: Image Classification in the Continuous Thought Machine

**Source**: Thomas Hannagan (Stellantis), arXiv:2610.19220, submitted 13 Oct 2026, cs.LG + cs.CV + cs.NE. Accepted at NeurIPS 2026 NeurReps Workshop. Official ImageNet CTM checkpoint (D=4096, T=50 ticks, ResNet backbone, L=196 tokens).

## Core Claim

The CTM's emergent "thought processes" are a **curve of moving attracting fixed points**: each tick map (memory held fixed) is contractive in spectrum (ρ(J)<1) but strongly non-normal (σmax(J)>1), so by Banach's theorem the state has a locally unique attracting fixed point that moves every tick as the synchronization memory updates. The thought trajectory = this fixed-point curve, followed exactly one tick behind. Most of the curve's motion is shared across images, visible as the previously-reported traveling wave; the attention schedule is largely generic (a shared program), and class identity rides the same curve displaced sideways.

## Mechanism Map

**1. Attracting but non-normal tick map (§3)**
- Reconstruct the exact tick map f(z; A_t) (single step reproduces next state <10⁻⁶); iterate to fixed point: converges at 3055/3072 image-tick pairs.
- At every fixed point: spectral radius ρ(J) = 0.15 median (max 0.95) — stable, locally unique attractor (Banach, adapted norm).
- BUT largest singular value σmax(J) = 3.2 median (up to 74) — transiently stretches a few directions. Non-normality = balanced amplification (Murphy & Miller 2009): Henrici departure from normality 0.99, eigenvalues carry only 2.0% of ‖J‖²_F (random core: 14%).
- Attraction is architectural (untrained CTM already ρ<1, median 0.05); **training promotes non-normality** (σmax/ρ: ~7 random-core → ~23 trained; untrained map is plain Euclidean contraction).

**2. One-tick lag structure (§3)**
- ‖z_t − z*_{t−1}‖ minimized at k=1 (5.9 vs 41.4 at k=0, 40.7 at k=2): the state sits on the *previous* fixed point, trailing the moving attractor by one contraction step (cos with fixed-point motion 0.995, step ratio 1.01).
- Shrink factor per step (0.11) ≈ ρ(J) prediction (0.14) — the lag is structural.

**3. Attention is a shared schedule (§4)**
- Freezing the query at first-tick value: −34% accuracy. Cross-image query shuffling at matching tick: **only −7%**. Flattening attention: −80%. No-attention: −100% (all images same class).
- Population-average query reproduces the image's attention map at cosine 0.936; query + shared average increment predicts next attention map at cosine 0.996 (vs 0.948 for "attention stays put") — the next glance is predictable before the model takes it.
- Freezing the query leaves 97% of the fixed point's motion — the curve's motion comes from the recurrence/memory, not the schedule.

**4. Traveling wave = the moving fixed point (§5)**
- Ordering neurons by fixed-point-curve phase reproduces the CTM authors' traveling wave (peak-tick Spearman 0.82, circular phase corr 0.88); neurons spread across nearly the whole window (std 15.0/50 ticks ≈ uniform 14.4) — staggered phase makes the front travel.
- The feed-forward cascade account FAILS: rank corr between Schur cascade position and peak tick is −0.08 — J and its Schur ordering are redefined every tick, so no single instantaneous cascade organizes the trajectory. The wave is a signature of the moving fixed-point curve, not the cascade.
- Wave vs attention: canonical correlation 0.52 does NOT exceed permutation null (p=0.17) — decoupled.

**5. Class identity rides the curve from tick 1 (§6)**
- Linear probes (128 PCs + multinomial LR, 5-fold): fixed point leads state by one tick (0.82 vs 0.79 at tick 1); all peak ~0.86 by tick 4–6.
- Decomposition z*_i,t = c_t + d_{k(i),t} + r_{i,t}: shared curve carries 0.66 variance, class offsets 0.105 (shuffled: 0.007), image residual 0.24. Class offsets lie almost entirely OUTSIDE the curve's leading 2D plane (0.5% inside) — classes ride the same curve, displaced sideways, with time-varying offset direction.

**6. What the synchronization memory does (§7)**
- Entropy fall (0.52→0.05 normalized) is fully accounted by the memory term (share 111–159%); state motion alone would slightly RAISE entropy (+0.11; |cos(Δz, −∇H)| < 0.06 — nearly orthogonal to entropy descent).
- Causal tests: frozen state (memory accumulates a repeated state) → confident but wrong (top-1 0.73→0.28); shuffled tick order → same final readout (order-free running mean of co-activations); fixed logit norm → entropy descent vanishes. **Entropy fall = growth of accumulated readout's magnitude (a growing gain), not evidence accumulation.**

**7. Scale dissociation (§8, MNIST/CIFAR D=128 models)**
- The attracting curve (ρ(J)<1) is universal; transient amplification (σmax>1) and the attention program emerge ONLY at ImageNet scale (MNIST σmax=0.49, CIFAR median 0.36, ImageNet 3.2). Freezing/swapping queries on small models: ±0.3% or less.
- Training increases non-normality at every scale (normal share 0.29→0.16 MNIST, 0.095 CIFAR, 0.020 ImageNet) but only ImageNet reaches transient amplification + query-dependent attention.

## Reusable Analysis Patterns

1. **Moving-fixed-point protocol for memory-modulated recurrences**: hold the memory/context fixed → the tick becomes an ordinary map → find fixed points → read Jacobian via autograd power iteration (ρ(J), σmax(J)) → verify convergence + no second basin (random restarts). This generalizes Sussillo-Barak fixed-point analysis to systems where the map is redefined every step.
2. **One-step-lag test**: for each k, compute mean ‖z_t − z*_{t−k}‖; the minimizing k identifies how many steps the state trails the moving attractor.
3. **Shared-vs-specific decomposition**: population-average the query/curve; measure cosine to image-specific attention (generic schedule detection); decompose trajectory into shared curve + class offset + image residual; test whether class offsets lie in the curve's leading plane.
4. **Non-normality quantification**: Schur-triangularize J = U T U*; feed-forward fraction (= Henrici departure) + eigenvalue energy share ‖λ‖²/‖J‖²_F + antisymmetric part at random-matrix level ⇒ balanced amplification signature.
5. **Cascade falsification**: order neurons by their mean Schur-chain position; correlate with peak activation time. Near-zero correlation kills the "instantaneous feed-forward cascade organizes the wave" story.

## Caveats & Limitations

- One checkpoint, validation subsamples, image classification only (author's own statement).
- Balanced-amplification structure of J is established as a property of the operator; its **functional role is left open** — the wave is NOT explained by the cascade.
- Results are for the released ImageNet CTM with random-pairing memory (8196 output + 2048 action pairs); the learned decay rates are negligible over the 50-tick budget (S_out ≈ uniform running mean of co-activations).

## Related Skills

- [[reciprocity-three-way-tradeoff-recurrent-circuits]] — non-normality in recurrent circuit trade-offs
- [[temporal-representation-degree-neural-networks]] — temporal representation design space
- [[finite-time-lyapunov-mde-rnn]] — tangent propagator spectra of random RNNs
- [[moving-fixed-point-thermodynamic-brain]] — moving attractor viewpoint in thermodynamic brain models

## Key References

- Darlow et al., "Continuous Thought Machines", NeurIPS 2025, arXiv:2505.05522
- Murphy & Miller 2009, "Balanced amplification", Neuron
- Sussillo & Barak 2013 (fixed-point linearization); Maheswaranathan et al. 2019 (reverse-engineering RNNs)
- Muller et al. 2018, "Cortical travelling waves", Nat Rev Neurosci

## Activation

continuous thought machine, CTM, fixed-point curve, non-normal dynamics, balanced amplification, moving attractor, traveling wave, synchronization memory, attention schedule, one-tick lag, Henrici departure, Schur decomposition, transient amplification
