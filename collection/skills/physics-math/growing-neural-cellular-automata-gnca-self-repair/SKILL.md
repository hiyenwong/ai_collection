---
name: growing-neural-cellular-automata-gnca-self-repair
description: "Methodology for analyzing internal fluctuations in Growing Neural Cellular Automata (GNCA) to understand self-maintenance and self-repair mechanisms. Based on arXiv:2607.12403v1."
category: ai_collection/neuroscience
---

## Context
Growing Neural Cellular Automata (GNCA) exhibit robust self-maintenance and self-repair, but the underlying dynamical mechanisms are poorly understood. This skill provides a structured approach to investigate the role of internal fluctuations—temporal micro-variability of hidden channel states—as a functional component supporting information flow, coordination, and recovery from damage.

## Core Methodology
1. **Train a GNCA model** on a task that requires self-maintenance (e.g., regenerative pattern formation).
2. **Measure internal fluctuations**: Compute temporal micro-variability of hidden channel states across time steps.
3. **Spatial correlation analysis**: Compute spatial correlation maps of fluctuations to identify structured patterns.
4. **Dimensionality reduction**: Apply techniques (e.g., PCA) to collective state trajectories to identify attracting states.
5. **Update-rate sweeps**: Vary the update rate to test robustness of fluctuation dynamics across timescales.
6. **Localized damage experiments**: Introduce localized perturbations (e.g., clamping cells to fixed states) and observe system response.
7. **Transfer entropy vector field estimation**: Compute transfer entropy between cells to quantify directed information flow; visualize as a vector field.
8. **Partial information decomposition (PID)**: Decompose information dynamics into synergistic, redundant, and unique components to detect shifts in computation during recovery.
9. **Identify permissive radius**: Determine a radius around damage within which suppressing small-magnitude fluctuations significantly impairs recovery.
10. **Characterize repair dynamics**: Observe inward corrective flow near damage and outward perturbation propagation at distance via transfer entropy.
11. **Detect regime shift**: Use PID to observe transition from synergy-dominant resting computation to redundancy-increased coordination during recovery.

## Implementation Steps
1. **Implement or obtain a GNCA simulator** capable of recording hidden cell states over time.
2. **Run baseline simulations** without damage to collect time series of cell states.
3. **Compute fluctuation metrics**: For each cell, calculate variance or standard deviation of its state over time; map spatial distribution.
4. **Apply spatial correlation**: Compute pairwise correlations of fluctuation amplitudes across cells; visualize correlation matrix or spatial maps.
5. **Perform dimensionality reduction** (e.g., PCA) on the spatiotemporal state matrix to extract dominant modes; track projection over time.
6. **Run update-rate experiments**: Repeat simulations with different update intervals (e.g., synchronous vs asynchronous) and compare fluctuation statistics.
7. **Inflict localized damage**: Select a region of cells and fix their states (or inject noise) for a defined period.
8. **Compute transfer entropy**: Use a suitable estimator (e.g., Kraskov-based) to compute transfer entropy from source to target cells across delays; aggregate to infer net information flow.
9. **Generate vector field**: Represent transfer entropy values as arrows on the cellular grid indicating direction and magnitude of information flow.
10. **Apply PID**: Use an IDA toolbox or custom implementation to compute synergistic, redundant, and unique information contributions from sets of sources to a target.
11. **Vary suppression radius**: In damage recovery simulations, suppress fluctuations outside increasing radii; measure recovery speed or fidelity to identify critical radius.
12. **Analyze results**: Correlate spatial structure of fluctuations with attractor dynamics; verify that suppressing fluctuations outside permissive radius impairs recovery; confirm inward/outward flow patterns and PID shifts.

## Pitfalls
- **Confounding noise with signal**: Ensure fluctuations are intrinsic to the deterministic dynamics, not due to stochastic updates; use deterministic updates or sufficient averaging.
- **Parameter sensitivity**: Results may depend on GNCA rule parameters, lattice size, and neighborhood range; perform sensitivity analysis.
- **Transfer entropy estimation bias**: Choose appropriate estimator and embedding parameters; validate on surrogate data.
- **PID interpretation**: PID measures can be subtle; ensure sufficient data statistics and consider complementary measures (e.g., mutual information, synergy).
- **Defining "permissive radius"**: May require iterative search; consider using mutual information or transfer entropy decay with distance.

## Verification
- **Baseline fluctuation structure**: Confirm that fluctuations exhibit spatial correlations (e.g., decay with distance) and are not uniform white noise.
- **Attractor coupling**: Show that fluctuation dynamics correlate with proximity to attracting states in reduced dimensional space.
- **Damage response**: Demonstrate that damage causes a transient global deviation in state space followed by gradual return; quantify recovery time.
- **Causality test**: Suppress fluctuations within permissive radius and observe impaired recovery; suppress outside radius and observe little effect.
- **Information flow**: Verify transfer entropy vectors point inward near damage and outward farther away during recovery.
- **PID shift**: Observe significant reduction in synergy and increase in redundancy during recovery compared to resting state.

## Activation Keywords
Growing Neural Cellular Automata, GNCA, self-repair, self-maintenance, internal fluctuations, transfer entropy, partial information decomposition, cellular automata, neural networks, dynamical systems, information dynamics