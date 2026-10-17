---
name: magna-magic-factory-tensor-network
description: "Classical simulation of magic-state factories (distillation/cultivation/code-switching) at Clifford-like cost: express acceptance rate and output fidelity as tensor networks, contract globally by exploiting the structural correspondence between factory feedforward structure and transversal gates on codes; supports decoder-dependent feedforward, simulates Bravyi-Haah up to 100 outputs without exponential blowup. Use when evaluating/optimizing magic state factory designs, distillation protocols, or lattice-surgery-based cultivation."
---

# Magna: Magic-State Factory Simulation via Global Network Algebra

**Source**: Magna: simulating magic state factories as cheaply as Clifford circuits (arXiv: 2610.22315, quant-ph, 2026-10-15)

## Problem

Magic-state factories are the dominant cost driver of FTQC resource estimates,
yet classical simulation of full factory protocols (distillation, cultivation,
code switching) is hard because of their substantial non-Clifford content and
**feedforward conditioned on mid-circuit measurements** (including decoder
outputs). Standard stabilizer/clifford simulators cannot represent the magic;
full state-vector simulation is exponentially expensive.

## Core Method

`magna` (magic-state-factory assessment via global network algebra):

1. **Figures of merit as tensor networks**: the protocol's acceptance rate and
   the fidelity of accepted output states are expressed as tensor networks.

2. **Global contraction exploiting code structure**: the networks are reduced
   globally by a structural correspondence with **transversal gates on quantum
   codes** — the factory's repetition structure maps onto transversal-gate
   tensor decompositions, letting the network be contracted without ever
   building the magic resource explicitly.

3. **Arbitrary feedforward support**: feedforward conditioned on arbitrary
   functions of mid-circuit measurement outcomes — including real decoder
   outputs — is natively expressible in the network algebra.

## Results

- **Bravyi–Haah 15-to-1 distillation** with up to **100 output magic states**
  simulated at cost NOT growing exponentially in the number of outputs
  (batched factory layouts become cheaper per-output to simulate).
- **Distance-5 magic state cultivation**: state-of-the-art sampling times on
  both color codes and RP² surface codes.
- **Nonlinear decoder-dependent feedforward**: validated on a logical-level
  distillation protocol with 15 rounds of decoder-dependent feedforward —
  the regime where Monte-Carlo-with-decoders is usually the only option.

## Reusable Pattern: "Merit-Functional Tensorization"

Instead of simulating the state and post-processing to a metric, **compile the
metric itself into a tensor network**:

```
metric = E_outcomes[ f(outcomes) ]  →  Σ_outcomes  f(outcomes) · Π_nodes T_node
```

- Acceptance rate: indicator function tensored with circuit amplitudes.
- Output fidelity: overlap networks ⟨ψ_accepted|·|ψ_target⟩.
- Any post-selection statistic: insert the conditioning as a tensor leg.

This is the same pattern as decoders-as-tensors and classical-shadow
estimators-as-networks: collapse the simulate-then-measure pipeline into a
single contraction where structure (repetition, transversality, symmetries)
can be factored out globally.

## Reusable Pattern: "Structural Correspondence Lifting"

The cost win comes from mapping a protocol-level structure (repeated
distillation rounds, transversal-gate equivariance of the code) onto the
tensor network's contraction order — not from a better generic contraction
heuristic. When simulating any repetitive fault-tolerance protocol:

1. Identify the symmetry/repetition (rounds, code blocks, transversal gates).
2. Check if the measurement pattern is invariant under it (it usually is for
   factory designs).
3. Contract the invariant part once, reuse via einsum broadcasting.

## Tooling Notes

- Designed as infrastructure for large-scale factory evaluation/optimization:
  pair with resource-estimation pipelines (see `ft-resource-estimation-uncertainty-propagation`).
- Complements `logical-catalyst-dyadic-phase` (cultivation protocols) and
  `syndrome-mediated-deterministic-t-gates` (T-gate factories) for end-to-end
  T-cost accounting.

## Limitations

- Distance-5 scale demonstrated; higher-distance cultivation needs the
  contraction order to exploit more code structure or hits memory walls.
- Decoder-dependent feedforward validated at logical level with 15 rounds —
  real-time decoder latency not modeled (it doesn't need to be: magna is
  offline evaluation).

## Related Skills

- `quantum-trajectory-magic-unraveling` — (today, sibling) magic of noisy trajectories
- `fault-counting-logical-sensitivity` — error sensitivity of QEC circuits
- `gkp-qldpc-circuit-benchmarks` — bosonic/qLDPC benchmarking
