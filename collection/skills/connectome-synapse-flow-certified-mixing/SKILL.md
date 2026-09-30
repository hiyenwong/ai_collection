---
name: connectome-synapse-flow-certified-mixing
description: Use when analyzing connectome random-walk mixing certificates.
category: ai_collection
trigger_words: [connectome, random walk, Dobrushin coefficient, spectral gap, mixing time, nearly closed set, boundary set, pre-registered analysis, Drosophila, certified bounds, synapse-flow chain, eigenvalue]
arxiv: 2609.33054
---

# Certified Mixing Analysis of the Drosophila CNS Connectome

**Source**: Eran Kopel (Tel Aviv University), arXiv:2609.33054 (27 Sep 2026), q-bio.NC/physics.bio-ph/q-bio.QM.
Full paper: https://arxiv.org/abs/2609.33054

## Core Claim

A **pre-registered, code-frozen** test of five hypotheses about the synapse-flow random walk on the male Drosophila CNS connectome (166,700 neurons, 124M synapses). Two held, three failed. The central methodological lesson: **random-walk summaries of connectomes are dominated by nearly closed boundary sets (nearly-absorbing neuron groups at reconstruction edges), not by the architecture being studied** — unless boundary sets are treated explicitly, spectral gaps and mixing claims are artifacts.

## The Synapse-Flow Chain

Walker at neuron i moves to postsynaptic partner j with probability ∝ synapse count:
```
P_ij = w_ij / Σ_k w_ik        (row-stochastic on giant SCC G)
```
- Male CNS v1.0 (min synapse confidence 0.5): w≥1 giant SCC = 165,314 neurons (99.2%), 25.5M edges; w≥5 giant SCC = 157,821 neurons, 6.1M edges.
- Signs: acetylcholine +1; GABA/glutamate/histamine −1; others 0.
- Question answered: **after how many synaptic steps has the walk forgotten where it started?** — quantified by the Dobrushin ergodicity coefficient τ(P^r) = largest total-variation distance two starting neurons can keep after r steps.

## Why Dobrushin Coefficient (not spectral gap)

τ(P^r) at finite r can be bounded **from both sides by certified numerical bounds**, and the bounds carry through a stated class of reconstruction errors. τ(P^r)=0 exactly when every starting neuron leads to the same distribution. (Classical analogue of quantum-channel entanglement-breaking index.)

```
τ(Q) = ½ max_{a,b} ||Q_a· − Q_b·||₁ = 1 − min_{a,b} Σ_k min(Q_ak, Q_bk)
```

## Pre-Registered Results (each tested ONCE after public registration + code freeze)

| Hypothesis | Verdict | Key numbers |
|---|---|---|
| H1: spectral gap at w≥5 in predicted range | **FAILED** | predicted 0.03–0.10; observed \|λ₂\|=0.9965, gap 0.0035 (order of magnitude smaller) |
| H2: leading photoreceptor modes are normalisation artefact | **HELD** | R7/R8 pairs (2–43 in-synapses vs 63–174 outputs) → 2-neuron loops of gain≈1; input floor at median F=342 removes them; leading floored mode = GABAergic ellipsoid-body ring neurons (ER3d_b/ER3p_a, PR 96.6) |
| H3: certified mixing depth reaches 0.05 by r=128 | **FAILED** | 0.669 ≤ τ(P^128) ≤ 0.816 at w≥5 — certifiably far from mixed after 128 steps |
| H4: depth certificate robust to per-synapse confidence | **FAILED** | no certificate at any confidence level (c=0.51–0.70); 14.4% of output synapses below 0.7 confidence |
| H5: spectrum insensitive to sign convention | **HELD** | Pospisil convention changes spectral radius by 1.5e-5 |

## The Boundary-Set Mechanism (exploratory, post-hoc)

The slow mode at w≥5 is carried by **11 neurons of the ventral cord** (7 mesothoracic efferent neurons incl. EN00B001/008/011/015, mesVUM-MJ; 2 IN03B088, 1 IN19A061, 1 MNad21):
- Hold 12.8% of stationary mass; escape probability 3.5e-3 per step; two-block estimate 1−p−q=0.99598 reproduces |λ₂|=0.99652.
- **Why**: efferent neurons' main output targets are OUTSIDE the CNS (muscles etc.), so within-graph normalisation leaves them few exits; dropping weak (w<5) connections removes most exits and few entrances (299→43 output synapses on strong connections vs 21,846→19,378 inputs).
- Removing the 11 neurons: |λ₂|→0.9806; next metastable set is again small, in the cord (6 neurons, conductance 0.027).
- Same phenomenon in FlyWire female brain: 7 lamina photoreceptor neurons (R1–6, L2) hold 1e-4 of mass, escape 2.8e-5/step, set |λ₂|=0.99999 at w≥1.
- In contrast, the slowest *well-populated* subsystem in both brains = anterior visual pathway + central complex (sky-compass circuit, MeTu/TuBu/ER/EPG), conductance 0.07–0.11.

**Key insight**: |λ₂| is a statement about the most nearly closed set *however small*; the certified depth profile is a statement about where the walk actually goes. Threshold matters as much: same connectome gives |λ₂|=0.945 at w=1 and 0.9965 at w=5.

## Three Remedies for Connectome Random-Walk Analyses (from Discussion)

1. **Explicit exit state**: route synapses that target outside the graph (non-neuron bodies) to an exit state — the male CNS tables record these, making it possible.
2. **Report with boundary classes removed** (efferent/motor/edge neurons) as a robustness check.
3. **Report depth profiles with witness sets and stationary masses**, not a single eigenvalue.

## Additional Methodological Lessons

- **Certificate vs resampling**: H4's failure is NOT evidence the depth profile is fragile — actual confidence-resampled chains move witness distances by ≤0.017 at r=32, but the worst-case certificate loses all power because it cannot exploit cancellation between row perturbations (Lemma 2 accumulation). Robustness can be shown by resampling, not certified — until certificates exploit cancellation.
- **Input-normalisation pitfall**: linear models/traversals that normalise by postsynaptic input inherit extreme sensitivity at low-input neurons (often sensory). Cheap guard: report input weights of leading-mode carriers, or floor the input at the median.
- **Null models**: cell-type-preserving random wirings *reproduce* the slow modes — the slow modes come from graph-theoretic boundary structure, not biology-specific wiring.
- **Missing synapses** (incomplete proofreading) are NOT modelled by the confidence class (false detections only) — a larger class would be needed.

## Reusable Pipeline

```python
# 1. Build chain: P_ij = w_ij / rowsum(w_i) on giant SCC
# 2. Stationary dist: power iteration; eigenvalues: ARPACK (irrestart Arnoldi, tol 1e-8)
# 3. Certified bounds on Dobrushin coefficient:
#    lower: witness pair (max TV distance between two rows of P^r)
#    upper: 1 - min_{a,b} Σ_k min(P^r_ak, P^r_bk) over sampled pairs
# 4. Locate slow mode: eigenvector of λ₂ → sweep cut minimising
#    φ(S) = F(S→S^c) / min{π(S), π(S^c)}   (stationary-flow conductance)
# 5. Check two-block estimate 1-p-q against |λ₂| to confirm set attribution
# 6. Boundary audit: which neurons have most output synapses leaving the graph?
```

## Applicability Triggers

- Any connectome-scale spectral/random-walk analysis (Drosophila, C. elegans, FlyWire, BANC, mammalian subgraphs, Mesoscanner datasets).
- Claiming "mixing time" or "spectral gap" of a connectome-derived Markov chain.
- Building "eigencircuit" claims from input-normalised linear maps.
- Pre-registration methodology for computational neuroscience: hypothesis + numeric pass/fail criteria + code freeze + single confirmatory run, exploratory analyses clearly labelled post-hoc.

## Related Skills

- [[drosophila-olfactory-connectome-functional-logic]] — prior Drosophila connectome work
- [[brain-higher-order-structures]], [[functional-connectome-fingerprint]] — brain-network spectral analyses that should heed the boundary-set caveat
- [[bell-theorem-statistical-causality]] — unrelated domain, same pre-registration spirit

## Limitations (from author)

- Confidence class models false detections only; missing synapses unmodelled.
- Signed-map analysis is input-normalised (floor needed for stability).
- Whether an adversarial reconstruction perturbation actually moves the depth profile far is open.
