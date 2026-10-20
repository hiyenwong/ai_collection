---
name: adult-structural-plasticity-multiscale
description: Use when modeling synaptic turnover or adult rewiring.
category: ai_collection
trigger: structural plasticity, synaptic turnover, spine dynamics, rewiring, homeostatic structural plasticity, Hebbian rewiring, connectome self-organization, synapse formation elimination
---

# Adult Structural Plasticity Across Multiple Scales

Source: Fauth, Lu, Luboeinski, Senk et al., "Rewiring of adult neural networks – learning from structural plasticity across multiple scales" (arXiv:2610.18024, q-bio.NC, Oct 2026). Multi-institution position paper (Göttingen/Jülich/Sussex, Volkswagen Foundation workshop) defining the research agenda for adult synaptic rewiring.

## Core Distinction

**Structural plasticity** = formation/elimination of entire synapses (network topology changes, hours–days timescale). **Synaptic plasticity** = weight changes at existing synapses (LTP/LTD/STDP, ms–min timescale).

**Zero-weight equivalence fallacy**: removing a synapse ≠ setting its weight to zero. The equivalence holds at one instant but not over time — different timescales, different resource budgets (synapses are metabolically costly and limited in biology AND neuromorphic hardware), different functions.

## Regulation Rules (what determines formation/elimination probabilities)

Synapse formation/elimination must be treated as stochastic; these factors modulate rates:

1. **Homeostatic structural plasticity (negative feedback)**: chronic activity blockade → spine growth; activity increase → spine loss. Calcium is the candidate messenger (NMDA blockade stabilizes spines). Denervation/monocular deprivation/whisker trimming → compensatory spine increase. Non-linear: chronic inhibition can also trigger non-homeostatic spine loss.
2. **Hebbian structural plasticity (positive feedback)**: LTP-inducing stimuli → new spines/boutons within minutes ("fire-together-wire-together"); LTD-inducing stimuli → spine loss. Needs homeostatic/resource boundaries to avoid runaway.
3. **Weight-size coupling**: larger spine head ↔ larger PSD ↔ stronger synapse ↔ more stable. LTP expands/stabilizes, LTD shrinks/destabilizes — weight and turnover are tightly coupled.
4. **Actin cytoskeleton dynamics**: spontaneous (activity-independent) morphology fluctuations from actin polymerization introduce intrinsic randomness into turnover.
5. **Spine age**: older spines/boutons more stable → stable "backbone" subpopulation supporting long-term function.
6. **Clustered plasticity**: learning-related new spines cluster within µm along the same dendritic branch; driven by correlated presynaptic input, local dendritic plateaus, diffusing actin regulators/calcium signals, local protein synthesis.
7. **Local supply structures**: SER/spine apparatus (synaptopodin+) and nearby mitochondria increase local spine density and stability → spatially heterogeneous plasticity that networks can self-organize (organelles are activity-responsive).
8. **Morphology constraints**: synapses only form at "potential synapse" sites (axon-dendritic appositions); major perturbations remodel arbors = structural metaplasticity (changes capacity for future rewiring).
9. **Cell adhesion molecules (CAMs)**: neurexin-neuroligin pairs initiate synaptogenesis; cadherins etc. modulate stability; molecular synapse profiles are heterogeneous (Unterauer et al. multiplexed imaging).
10. **Glia/ECM/microglia**: astrocytes secrete synaptogenic factors; ECM/perineuronal nets restrict where synapses form (long-term memory hypothesis, Tsien 2013); microglia eliminate synapses via complement/phosphatidylserine signaling.

## Computational Function: Stable Memory Despite Continuous Turnover

Three theoretical resolutions of the "stable memory from unstable synapses" dilemma:

- **Stable core**: an age-stabilized subset of spines carries permanent memories — insufficient alone.
- **Equifunctional pairwise connections**: Hebbian structural plasticity creates a dynamic equilibrium — synapses between neuron pairs turn over, but the CONNECTION strength stays stable; positive feedback lets multiple synapses stabilize each other. Achieves fast learning + slow forgetting (Deger et al. 2012; Fauth et al. 2015).
- **Equifunctional networks/cell assemblies**: identity of individual connections irrelevant; stability from strong connectivity within the assembly. Hebbian rewiring forms and stabilizes assemblies (Fauth & van Rossum 2019). Purely homeostatic (firing-rate set-point) rewiring ALSO forms assemblies — random pre/post pairing implicitly evaluates correlations (Gallinaro & Rotter 2018; Gallinaro et al. 2022), again with fast learning / slow forgetting.

Other functional results:
- **Connectivity statistics**: Hebbian/weight-dependent rewiring reproduces measured multisynapse-count distributions, bidirectional-connection overrepresentation, and clustered motifs (Miner & Triesch 2016; Diaz-Pier et al. 2016 for homeostatic).
- **Memory capacity**: structural reorganization of synapses increases associative memory capacity beyond weight-only plasticity, reproduces graded amnesia, spacing effect, resistance to catastrophic forgetting (Knoblauch et al. 2014).
- **Dendritic clustering**: nonlinear branch subunits (Poirazi & Mel) + weight-dependent clustering of same-input synapses increases pattern-recognition capacity (Limbacher & Legenstein 2020; calcium-correlation detector of Helias et al. 2008).
- **Representational drift**: rewiring both contributes to drift (sampling degenerate equifunctional configurations, Kappel et al. 2018) and mitigates its functional impact (readout plasticity, Acker et al. 2019).
- **Replay**: sleep replay stabilizes memory-related synapses while pruning irrelevant ones; weight-dependent structural plasticity self-organizes replay (Fauth & van Rossum 2019).

## Clinical Translation

- **MSP (model of structural plasticity)**: homeostatic rewiring after lesions predicts sequential reorganization, neighbor-region ingrowth, and that stimulation mitigates poor adult compensation of stroke deafferentation (Butz et al.).
- **Brain stimulation modeling**: weak sub-threshold tDCS achieves stronger network remodeling than supra-threshold TMS pulses; partitioning stimulation duration with rest intervals beats one long epoch; effects depend on brain state (resting vs. learning vs. consolidation). CRS (coordinated reset) explained by homeostatic+STDP interaction.
- **Open clinical questions**: are homeostatic set-points altered in disease (ASD, epilepsy, schizophrenia, Alzheimer's)? Firing-rate homeostasis persists under pathology but structural set-point invariance is unverified. Does the set-point live per-neuron or at population level?

## Simulation & Neuromorphic Toolchain

| Platform | Structural plasticity support |
|---|---|
| NEST (CPU) | Fully integrated homeostatic rule (Butz & van Ooyen), synapse add/remove without kernel interrupt; scalable approximation (Rinke/Czappa) |
| GeNN (GPU) | Flexible user-defined rewiring rules; sparse-from-scratch training (Knight et al. 2026) |
| Brian 2 | Only synapse status flip, no true add/remove |
| ANNarchy / Arbor | Conditional rewiring / backend-agnostic loose integration |
| BrainScaleS-2 (analog) | On-chip digital co-processor for rewiring |
| SpiNNaker 1/2 | On-chip rewiring support |

**Sparse-network training algorithms**: DEEP R (Bellec et al. 2018) replaces weak synapses with random new ones during training — sparse nets match dense accuracy; combine with biologically plausible weight learning (Bellec et al. 2020). Constructive networks grow topology during training. Lottery-ticket search = a structural plasticity algorithm (dense nets contain sparse winning subnets).

## Key Open Problems (research agenda)
1. Complete the predictor set — apparent randomness = incomplete predictors + true biological noise (turnover persists when activity is blocked).
2. Inhibitory/gap-junction rewiring (coordinated with excitatory, subtype-dependent).
3. Multiscale bridging: generative models linking molecular (actin, CAMs, protein lifetimes) → spine dynamics → network statistics → whole-brain activity.
4. Interaction with late-phase LTP/LTD and synaptic scaling (partially redundant under moderate perturbation, complementary under strong deprivation).
5. No standard benchmarks/frameworks exist for structural plasticity simulators.

## Application Checklist
- When building spiking network models with rewiring: choose homeostatic (set-point, MSP) vs Hebbian (correlation-driven) vs weight-dependent rules; combine both for stability.
- When memory must survive parameter turnover: use equifunctional assemblies (redundant connectivity), not stable-core-only.
- For edge/neuromorphic ML: initialize sparse, use DEEP R-style replace-weak-with-random; structural rules allocate limited synapse budget during training.
- For stimulation therapy modeling: sub-threshold + temporally partitioned protocols; check brain state dependence.

## Key References
- Butz & van Ooyen 2013 (homeostatic MSP rule); Deger et al. 2012; Fauth et al. 2015 (equifunctional connections); Gallinaro et al. 2022 (homeostatic assemblies); Knoblauch et al. 2014 (capacity/cognitive phenomena); Limbacher & Legenstein 2020 (dendritic clustering); Kappel et al. 2018 (drift as sampling); Bellec et al. 2018 (DEEP R); Achterberg et al. 2023 (spatially embedded RNNs).