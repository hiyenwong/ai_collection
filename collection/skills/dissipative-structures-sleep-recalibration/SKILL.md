---
name: dissipative-structures-sleep-recalibration
description: "Use when modeling sleep need from neural parameter drift."
---

# Neural Computation on Dissipative Structures Under Cyclic Calibration: A Systems Perspective on Sleep

Theory paper from arXiv:2610.21486 (Javier Antonio Díaz Cisternas, IIIS University of Tsukuba, Oct 2026). Reframes sleep as an emergent property of neural computation running on far-from-equilibrium dissipative structures. Trigger words: sleep homeostasis, synaptic fatigue, thermodynamics of computation, dissipative structures, parameter drift, Process S, SHY hypothesis, release probability.

## Core Thesis

Neural computation runs on metastable, low-entropy molecular structures (synaptic vesicle pools, receptor assemblies, ion gradients) that DEGRADE THROUGH USE. Wakefulness = computation that progressively consumes its own substrate, causing drift in key signaling parameters (gain, threshold, integration time). Sleep = a system-wide anabolic recalibration phase that restores function-structure coupling by counterbalancing entropic drift. Sleep need is therefore NOT homeostatic regulation of an unknown physiological variable (Process S mystery) but an unavoidable thermodynamic constraint of dissipative computation.

## The Causal Chain

1. **Dissipative structures**: Living systems self-organize far from equilibrium (Prigogine), sustaining local low-entropy states by exporting entropy. Unlike crystals (passive potential minima), dissipative structures are dynamic configurations requiring continuous energy/matter flux (typhoons, Rayleigh–Bénard cells, biological molecular turnover).
2. **Thermodynamic asymmetry of function turnover**: building low-entropy structures is SLOW (vesicle biogenesis, transport, neurotransmitter packing); discharging them is FAST (sub-millisecond exocytosis collapses the investment). Function execution always outruns local regeneration.
3. **Synaptic fatigue as the canonical drift readout**: sustained stimulation depletes functional vesicles (short-term synaptic depression). The vesicular release probability P_r is a continuous state variable tracing a trajectory from optimal release efficiency to presynaptic fatigue. P_r decline during prolonged wake has been proposed as a universal cross-species metric of sleep need.
4. **Postsynaptic parallel**: receptors undergo non-equilibrium assembly → activation → internalization → degradation; sustained activation drives desensitization and endocytic degradation.
5. **Structural debt**: local endocytic recycling is a stopgap on an aging molecular substrate accumulating oxidative damage; only de novo anabolic turnover fundamentally resets it.
6. **Logistics**: synapses are sub-femtoliter compartments with low protein copy numbers, hundreds of µm from the soma. Rodents show circadian mRNA waves: dusk wave = transmission components (prepare wake); dawn wave = translation/metabolic machinery (rebuild during sleep).
7. **Why sleep must be SYSTEMIC**: neural circuits are tightly coupled analog computers — fidelity of any node depends on coordinated calibration of the whole network manifold. Once degraded nodes inject local signal distortion, collective integrity fails. Sleep cannot be piecemeal local maintenance; it requires a global state transition.
8. **Executive trigger vs. primary driver**: subcortical flip-flop circuits (VLPO ↔ monoaminergic/orexinergic arousal centers) are NOT the cause of sleep need — they are the executive switch integrating physiological surrogates of wake load (extracellular adenosine, SIK3-mediated cumulative phosphorylation) and enforcing the nonlinear transition to recalibration mode.

## Key Claims vs. Dominant Theories

- vs. SHY (Synaptic Homeostasis Hypothesis): SHY operates in the same physical space but restricts restoration to postsynaptic weight scaling tied to learning/plasticity. This framework generalizes to ALL signaling parameters (gain, threshold, integration time, release probability), independent of learning.
- vs. metabolic-waste / energy hypotheses: those address boundary conditions (glutamate excitotoxicity, interstitial waste, ATP budgets) but not the core function-structure coupling drift.
- vs. Two-Process Model (Borbély): Process S is operationalized phenomenology — the underlying homeostatically-regulated variable is identified as cumulative entropic drift in computational parameters.
- Wakefulness cannot maintain a continuous non-equilibrium steady state because self-organizing physiological systems are governed by critical phase transitions — uninterrupted computation is physically unachievable. Neural computation is fundamentally SELF-LIMITING.

## Testable Signatures (paper's empirical avenues)
- Track P_r (release probability) and other signaling parameters across sleep-wake cycles as direct drift/calibration readouts.
- Reinterpret existing paradigms by shifting the analytical lens from functionalist synaptic scaling to non-equilibrium thermodynamics — the entropic trace is delocalized from subcellular architecture to circuit level.
- Circadian mRNA wave composition (dusk vs dawn enrichment) as scheduled maintenance logistics.
- Sleep rebound (homeostatic criterion) = repayment of accumulated structural debt; deep-sleep amount should track prior computation-load heterogeneity across nodes.

## Why This Matters for Computational Systems

- Provides a physics-grounded first-principles account unifying synaptic homeostasis, waste clearance, energy, and memory-consolidation theories as partial views of one thermodynamic cycle: synthesis → function execution (entropy export) → degradation → recalibration.
- Analogy for engineered systems: any analog computer built on degradable substrates with tight inter-node coupling requires periodic global recalibration; local repair cannot preserve collective fidelity.
- Relevant to neuromorphic hardware, reservoir computing on memristive/analog devices (drift is a known failure mode), and theories of why biological intelligence needs offline states.

## Related Skills
- [[sleep-like-consolidation-llm]] — memory consolidation in LLMs during sleep-like phases
- [[thermodynamic-networks-computation]] — autonomous thermodynamic computation
- [[stochastic-synaptic-plasticity]] — synaptic stochastic modeling
- [[tsodyks-markram-chaotic-dynamics]] — short-term synaptic depression dynamics

## Reference
- arXiv:2610.21486 — Neural Computation Runs on Dissipative Structures Under Cyclic Calibration: A Systems Perspective on Sleep
