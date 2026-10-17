---
name: quantum-trajectory-magic-unraveling
description: "Magic (stabilizer Rényi entropy) of quantum-trajectory unravelings of noisy circuits: trajectory-averaged magic is unraveling-dependent; optimal Kraus choice is a weak two-outcome measurement, not projective; high-magic tail (not the average) controls stabilizer simulation cost. Use when analyzing magic/non-stabilizerness in open-system noisy circuits, optimizing unravelings for classical simulation, or reasoning about Kraus-representation dependence of resource quantities."
---

# Magic in Quantum Trajectory Unravelings of Noisy Random Circuits

**Source**: Magic in quantum trajectory unravelings of noisy random quantum circuits (arXiv: 2610.22318, quant-ph, 2026-10-15)

## Problem

A noisy quantum circuit's trajectory description is **not unique**: every Kraus
representation {K_μ} of the noise channel defines a different unraveling — a
different ensemble of pure states averaging to the same density matrix. All
unravelings give identical observable expectation values, but they **differ in
the quantum resources** (here: magic / non-stabilizerness) carried by individual
trajectories. Since stabilizer-simulation cost scales exponentially with magic,
the choice of unraveling directly changes what you can classically simulate.

## Setup

- Circuits: Haar-random and T-doped random Clifford brickwork
- Noise: local dephasing of strength p
- Magic quantifier: stabilizer Rényi entropy (SRE), extensive in system size

## Key Findings

1. **Canonical Pauli-jump unraveling is magic-neutral**: if the base circuit is
   Clifford, the Pauli-jump unraveling is itself Clifford — trajectories retain
   the Haar-random value of non-stabilizerness. Noise "absorption" into jump
   branches does not dilute magic.

2. **Trajectory-averaged magic is reducible**: exploring the full two-parameter
   family of minimal unravelings, a state-independent choice of Kraus operators
   can substantially reduce average magic. The optimal choice is NOT the
   projective-measurement unraveling but a **two-outcome generalized (weak)
   measurement** — Kraus operators acting as a weak measurement of the noisy qubit.

3. **Average is the wrong statistic**: the optimal unraveling produces a very
   broad magic distribution across trajectories. A sizable fraction retain
   Haar-random magic even at the optimum. Stabilizer simulation cost is governed
   by the **high-magic tail, not the mean** — so unraveling optimization has
   fundamental limits as a route to classical simulation of noisy dynamics.

4. Linear (extensive) scaling of magic density with system size survives every
   unraveling; only the prefactor is p-dependent and reducible.

## Reusable Pattern: "Resource-Distribution Tail-Control"

When a resource quantity (magic, entanglement, circuit complexity) can be
redistributed across an ensemble of equivalent descriptions:

- Optimizing the **mean** is insufficient if cost is set by a **tail/max**
  (simulation cost ∝ exp(resource), DTQW sampling cost, tensor-network bond dim).
- Check whether the cost functional is convex in the resource: exp() means
  Jensen puts the tail in charge.
- Report distributions over ensembles, not just averages — a "reduced average"
  claim must be audited against the surviving tail fraction.

## Reusable Pattern: "Kraus-Gauge Dependence Audit"

Trajectory-level quantities are functions of the (K_μ) gauge choice. Before
attributing a physical interpretation to a per-trajectory resource:

1. Fix the canonical gauge (Pauli jumps for Pauli channels) as baseline.
2. Sweep the minimal-parameter family of equivalent gauges.
3. Verify whether the quantity is gauge-invariant (density-matrix-level:
   always) or gauge-covariant (trajectory-level: usually).
4. Optimization over gauges is legitimate for cost engineering, but claims
   about "the magic of the evolution" must state the gauge.

## Limitations

- Restricted to dephasing-type local noise; amplitude-damping and general
  channels with non-orthogonal Kraus geometry may behave differently.
- Stabilizer Rényi entropy as the magic measure; stabilizer extent/Robustness
  of Magic could reorder unravelings.
- Two-parameter minimal family — full Kraus gauge space is larger.

## Related Skills

- `sre-phase-averaged-magic-invariant` — magic invariant under phase frames
- `magic-rectangle-rigidity` — nonlocal game magic quantification
- `monitored-clifford-purification` — trajectory purification dynamics
- `magna-magic-factory-tensor-network` — (today, sibling) factory-level magic cost simulation
