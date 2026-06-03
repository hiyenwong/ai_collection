---
name: multi-objective-snn-oscillation
description: "Multi-objective genetic algorithm (NSGA-III) optimization of Izhikevich neuron-based recurrent spiking neural networks for simultaneously fitting neural firing rates and network oscillation frequencies. Applicable to SNN parameter tuning, brain organoid modeling, and spiking neural network design."
tags: [spiking-neural-networks, nsga-iii, multi-objective-optimization, genetic-algorithm, izhikevich-neuron, oscillations, snn-parameter-tuning, brain-organoid, computational-neuroscience]
---

# Multi-Objective Optimisation with Oscillatory Dynamics in Spontaneous and Decision Spiking Neural Networks

**arXiv:2605.25224** | Submitted: 24 May 2026

**Authors:** Divyansh Sethi, Muhammad Faraz, KongFatt Wong-Lin

## Summary

Spiking neural networks (SNNs) can be used for cost-efficient AI computing or mechanistic modeling of neural data. Fitting neural data with recurrent SNNs (RSNNs) remains challenging, particularly for simultaneously matching network oscillation frequencies and neural firing rates. This work extends genetic algorithm (GA) optimization — specifically **NSGA-III** (non-dominated sorting GA) — to optimize Izhikevich neuron-based RSNN connectivity parameters for targeting emergent neuronal population firing rates AND network oscillation frequencies simultaneously.

## Key Contributions

1. **Multi-Objective SNN Optimization**: First systematic application of NSGA-III to simultaneously optimize both firing rates and oscillation frequencies in Izhikevich-based RSNNs.

2. **Three Evaluation Scenarios**:
   - Spontaneously active simulated RSNN model
   - Low-activation brain organoid
   - Simulated RSNN model with transient decision dynamics

3. **Pareto Frontier Analysis**: Uses RMSE on the Pareto frontier to evaluate trade-offs between competing objectives.

4. **Parameter Sensitivity Findings**:
   - Dominant oscillation frequencies are more parameter-sensitive (harder to fit)
   - Firing rates are more robustly met (easier to optimize)
   - Identified low-activity regime for decision-making

## Methodological Framework

- **Neuron Model**: Izhikevich neuron model (spontaneously firing cortical excitatory and inhibitory neurons)
- **Architecture**: Recurrent SNN (RSNN) with structured connectivity
- **Optimization Algorithm**: NSGA-III (non-dominated sorting genetic algorithm, multi-objective)
- **Optimization Targets**:
  - Neuronal (sub)population firing rates
  - Network oscillation frequencies (dominant oscillatory modes)
  - Activity patterns in different time epochs (for decision model)
- **Evaluation Metric**: RMSE on the Pareto frontier

## Key Findings

- NSGA-III successfully optimizes for multiple network firing rates AND dominant network oscillation frequencies
- Oscillation frequencies are more sensitive to parameter changes than firing rates
- Decision-making model shows distinct activity patterns across different time epochs
- Low-activity regime identified for decision-making dynamics
- Applicable to both simulated RSNNs and real brain organoid data

## Potential Applications

- Parameter tuning for SNN-based neural data fitting
- Brain organoid modeling and analysis
- Neuromorphic system design where oscillation properties matter
- Understanding neural dynamics in decision-making circuits
- Multi-objective optimization of neural network parameters

## Related Work

- Extends previous GA optimization of Izhikevich-based RSNNs
- Complements surrogate gradient methods for SNN training
- Relevant to understanding oscillatory dynamics in cortical circuits

## Activation Keywords

- nsga-iii, multi-objective-snn, spiking-oscillations, izhikevich-optimization, snn-parameter-tuning, brain-organoid, multi-objective-genetic-algorithm, pareto-frontier-snn, oscillatory-spiking-networks

## References

- arXiv:2605.25224 [q-bio.NC]
