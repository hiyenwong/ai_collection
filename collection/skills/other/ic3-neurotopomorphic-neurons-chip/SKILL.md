---
name: ic3-neurotopomorphic-neurons-chip
description: "Use when engineering neurons-on-a-chip or bio-spike circuits. IC³ framework screens topology before fabrication."
category: neuroscience
---

# IC³ Neurotopomorphic Computing (Neurons-on-a-Chip)

From arXiv:2610.06065 (Barros, Univ. of Essex, 5 Oct 2026): "From communication to computation in neurons-on-a-chip: an in silico study of neurotopomorphic computing". Zenodo code/data: 10.5281/zenodo.22723783.

## Core Thesis

**Neurotopomorphic computing**: treat the *physical wiring* of a living neuronal circuit as a design variable, co-designed with stimulation, dynamics, and readout. Screen candidate topologies in simulation for the communication state they produce and whether that state supports the intended computation — **before fabricating the culture**.

**Counter-intuitive central result**: widespread network engagement does NOT improve computation. Predominantly feedforward circuits (Sequential Chain, Microchannel Diode) had the LOWEST IC³ yet the HIGHEST scores on both classification tasks. Across 9 architectures, higher IC³ and higher TE both rank-correlated negatively with decoding (ρ between −0.73 and −0.81). Restricting how signals spread appears to preserve the input distinctions that classification requires.

## IC³: Integrated Characterisation of Communication-Driven Computation

A network is S = (G, Θ); under input u and noise ξ it produces trajectory X = Φ(G, Θ, u, ξ). Three coupled domains are extracted:

- **Q — neuronal dynamics** (weight α_Q = 0.60): activity states generated/sustained
- **C — functional communication** (α_C = 0.30): information exchange as activity propagates
- **S — structural support** (α_S = 0.10): architecture constraining both

Profile: z_IC³ = [N_Q(q), N_C(c), N_S(s)]; scalar index IC³_M = Σ_d α_d Σ_m ω_dm N_dm(x_dm).

### Reference implementation (8 observables, 15-neuron circuit)

| Domain | Observable | Weight | Scale s_m |
|---|---|---|---|
| Q | spike entropy | 0.15 | 1 |
| Q | effective dimensionality | 0.15 | 15 |
| Q | ISI CV | 0.10 | 2 |
| Q | burst-like fraction | 0.10 | 1 |
| Q | regular-spiking fraction | 0.10 | 1 |
| C | pairwise mutual information | 0.15 | 1 |
| C | transfer entropy (bits) | 0.15 | 0.1 |
| S | graph metric (degree + core number) | 0.10 | 100 |

Normalization: z_m = clip(x_m / s_m, 0, 1); IC³ = Σ ω_m z_m. TE = first-order I(X_{t-1}; Y_t | Y_{t-1}), 10 ms bins, 200 circular-shift surrogates for bias correction. Rankings were stable under 500 local weight perturbations, equal weighting, and leave-one-component-out — the negative IC³↔performance association is not a weight artifact.

**IC³ characterizes state, NOT performance**: P_τ = Π_τ(z_IC³, u_τ, r_τ) is a task-specific projection. A high-IC³ network can be a poor decoder; two tasks can depend on different properties of the same profile. Never use IC³ to predict task accuracy.

## Nine-Architecture Benchmark (in silico)

Each: N=15 Izhikevich neurons (12 excitatory RS: a,b,c,d=(0.02,0.20,−65,8); 3 inhibitory FS: (0.10,0.20,−65,2)), 20 seeded instances/architecture, 650 µm square embedding, conductance-based synapses (τ_E=5 ms, τ_I=6 ms; E_rev=(0,−80) mV), LogNormal(0,0.35²) weights ≈0.64 mean/unit adjacency, conduction velocity 0.10–1.2 m/s, tortuosity 1.15, synaptic delay 0.8 ms, noise α=2.0, bias 0.5.

| Architecture | Definition | IC³ (mean) | Notes |
|---|---|---|---|
| All-to-All | full connectivity | 0.354 (highest) | worst decoders; high structural contribution 0.100 |
| Small-World | Watts-Strogatz k=4, p=0.10, symmetrized | 0.344 | highest 90th-pct firing (120.3 Hz) |
| Scale-Free | Barabási-Albert m=2, symmetrized | 0.338 | reachability ≈ recruitment (1.00/0.949) |
| Star | hub at node 0 | mid | shortest latency 11.55 ms, high response prob 0.780 |
| Directed Random | directed ER p=0.12 | mid | highest target-normalized TE (0.0975) |
| Clustered Ring | 5 modules, cyclic unidirectional (p_in=0.75, p_fwd=0.15) | mid | reachability 0.982 → recruitment 0.574 |
| Sparse | directed ER p=0.10 | mid | steepest per-hop decline (−0.175/hop) |
| **Microchannel Diode** | chain + Bern(0.8) boost fwd / 0.3·Bern(0.05) weak reverse | 0.164 | **top-2 decoder**, recruitment 0.307 |
| **Sequential Chain** | pure directed chain | 0.154 (lowest) | **top-2 decoder**, recruitment 0.346, longest latency 15.52 ms |

Source selection (non-fixed architectures): lexicographic max of (reachable-count r(i), out-closeness c⁺(i), out-degree, −i) — prevents isolated sources without assuming central = functionally optimal.

## Key Quantitative Findings

1. **IC³/TE vs tasks (architecture-level Spearman, n=9)**: temporal-order ρ(IC³)=−0.767, ρ(TE)=−0.767; frequency ρ(IC³)=−0.728, ρ(TE)=−0.812. Fading memory: no association.
2. **Within-architecture**: temporal-order β_W = −1.567 per IC³ unit (negative holds inside architectures); frequency β_W = −0.260 (weak).
3. **Reachability ≠ recruitment**: functional recruitment (R≥0.5 response in 50 ms window) is on average 0.264 below structural reachability. Chain/Diode recruit only ~1/3 of reachable neurons — yet decode best.
4. **Latency superlinear in path delay**: β_physical = 1.684 ms per ms (95% CI 1.29–2.08) — each relay adds ~0.68 ms integration beyond transmission; residual 8–13 ms reflects synaptic+integration dynamics.
5. **Centrality hurts relaying**: higher out-closeness → lower response probability after adjustment (β=−0.27, CI −0.47..−0.07). Structurally favorable ≠ functionally recruited.
6. **Readout expansion is useless**: adding first-hop or ALL network neurons to the readout never improved decoding in any architecture×task — downstream activity is redundant or less decoder-accessible. Information can remain present while becoming less *usable*.
7. **Untrained fading memory is null in ALL 9 architectures** (η²=0.029, lags 25–200 ms, held-out R²≈baseline). Input fidelity (current-input distinctions) and persistence (past-input recovery) place different demands on recurrence — none of the nine achieved both. Memory in living cultures requires plasticity protocols, not topology alone.
8. **Task dependence of topology**: architecture explains η²=0.433 (frequency), 0.412 (temporal order), 0.029 (fading memory); partial η² architecture×task = 0.251. Frequency & temporal-order rankings correlate (ρ=0.711); fading memory anticorrelates with temporal order (ρ=−0.367).

## Tasks & Readout Protocol

- **Close-frequency decoding**: 4 classes at 8.5/10/11.5/13 Hz, I_stim=6, 1200 ms trajectories, 8-window spike-count features (all 15 neurons concatenated), L2 multinomial logistic regression, leave-one-instance-out with grouped inner CV (C∈{0.1,1,10}).
- **Temporal-order discrimination**: A→B vs B→A, site B = physically most distant neuron, 75–125 ms inter-pulse interval, 2000 ms.
- **Fading memory**: binary telegraph input (10 ms grid, switch p=0.15), Ridge readout (λ∈{0.01..100}), reconstruct input at lags 25/50/100/200 ms, held-out R².
- Score normalization: S = (A − C_chance)/(1 − C_chance), chance by label permutation through the same nested pipeline.

## When to Use

- Designing neurons-on-a-chip / microfluidic neuronal circuits (choose topology before fabrication)
- Reservoir computing with biological or SNN substrates: predicts **directional sparse chains beat dense recurrent topologies for discrimination tasks**
- Interpreting MEA culture recordings: measure IC³ profile to characterize state, then test tasks separately
- Any bio-spike computing claim where "more connectivity/recruitment/activity" is assumed to mean "more computation" — this paper is the canonical counterexample

## Engineering Implications

1. Constrain propagation (unidirectional microchannels, axonal diodes) to preserve input distinctions; dense recurrent cultures dissipate them.
2. Screen in silico first: simulation-informed design (as in synthetic biology) avoids per-design culture fabrication cost and biological-variance confounds.
3. Readout placement near stimulation sites is sufficient — downstream recruitment adds redundancy, not information.
4. Report architecture, communication phenotype, and task performance as three separate levels; never collapse them into one "network quality" scalar.
5. For device constraints (latency, spike expenditure), pick from the phenotype trade-off frontier: no architecture simultaneously maximizes firing, recruitment, precision, and efficiency.

## Limitations (from paper)

15 neurons, fixed weights (learning only at readout); STP only in sensitivity analysis; geometric surrogates from layout rules (not real devices); Microchannel Diode's circular embedding confounds Chain–Diode comparison; source fixed at node 0 for 3 architectures; 9-point architecture correlations; IC³ weights fixed pre-analysis.

## Related (existing skills)

- [[embodied-neurocomputation]] — BNN culture encoding optimization (complementary substrate)
- [[mea-array-spiking-rvq-motif-transformer]] — MEA spike-train generative modeling
- [[mtc-conductance-spiking-networks]] — multi-timescale conductance SNNs
- [[connectome-wiring-specificity-null-models]] — wiring specificity nulls
