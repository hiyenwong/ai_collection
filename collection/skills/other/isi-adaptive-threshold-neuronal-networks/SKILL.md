---
name: isi-adaptive-threshold-neuronal-networks
description: "First-passage-time analysis of inter-spike interval (ISI) statistics for excitatory-inhibitory (EI) integrate-and-fire neurons with depolarizing and hyperpolarizing adaptive thresholds. Use when studying stochastic neuronal firing, ISI variability, adaptive threshold mechanisms, or EI balance effects on spike-time statistics."
metadata:
  arxiv_id: "2607.18428"
  published: "2026-07-22"
  authors: ["Oliver Gambrell", "Abhyudai Singh"]
  tags: [neuroscience, spiking-neurons, inter-spike-interval, adaptive-threshold, EI-balance, first-passage-time, stochastic-neuronal-dynamics]
license: Complete terms in LICENSE.txt
---

# ISI Statistics in Adaptive-Threshold Neuronal Networks

A first-passage-time methodology for analyzing how depolarizing and hyperpolarizing adaptive thresholds shape the mean and variability of inter-spike intervals in excitatory-inhibitory (EI) integrate-and-fire neurons.

## Core Idea

Extend the classical integrate-and-fire model by letting the threshold potential depend on recent presynaptic activity. This captures two biophysical effects:

- **Depolarizing adaptive threshold**: threshold rises after excitation (spike-frequency adaptation via sodium/calcium-activated potassium channels).
- **Hyperpolarizing adaptive threshold**: threshold falls after inhibition (post-inhibitory rebound via sodium channel recovery from inactivation).

The framework derives the ISI distribution via first-passage-time (FPT) analysis and quantifies ISI noise with the coefficient of variation (CV).

## When to Use

- Modeling spike-time variability in EI circuits.
- Comparing fixed vs. adaptive threshold effects on firing regularity.
- Predicting post-inhibitory rebound spiking.
- Studying how excitatory/inhibitory input balance affects ISI statistics.

## Key Findings

1. **Depolarizing adaptive thresholds increase ISI noise** relative to fixed thresholds at the same mean ISI.
2. **ISI noise can be hypo- or hyper-exponential** (CV < 1 or CV > 1) depending on excitatory and inhibitory input rates.
3. **Hyperpolarizing adaptive thresholds can generate spikes driven purely by inhibition**, producing post-inhibitory rebound firing.
4. **Quantal content (QC) is modeled as binomial random variables**, linking synaptic release stochasticity to postsynaptic firing statistics.

## Methodology

1. **Model the postsynaptic neuron** as a leaky integrate-and-fire neuron receiving Poisson excitatory and inhibitory inputs.
2. **Model quantal content** of each presynaptic AP as independent binomial random variables with known mean and variance.
3. **Fix a threshold potential** for the baseline case; then extend to adaptive thresholds:
   - Depolarizing: threshold increases with membrane depolarization.
   - Hyperpolarizing: threshold decreases with membrane hyperpolarization.
4. **Apply first-passage-time analysis** to derive the mean ISI and the coefficient of variation.
5. **Validate analytical predictions** with stochastic simulations across input-rate parameter space.

## Implementation Sketch

```python
import numpy as np

# Simulate membrane potential with EI Poisson inputs and adaptive threshold
# V(t): membrane potential, tau: leak time constant
# dV/dt = -V/tau + sum_i qe_i * delta(t-te_i) - sum_j qi_j * delta(t-ti_j)
# threshold theta(t) adapts based on recent excitation or inhibition

# First-passage-time estimate: sample trajectories, record crossing times
# ISI = time between successive threshold crossings
# mean_ISI = np.mean(ISIs); CV = np.std(ISIs)/mean_ISI
```

## Parameter Sensitivities

- **High, balanced EI rates** maximize ISI noise (CV²) in the fixed-threshold model.
- **Depolarizing threshold** systematically raises CV for matched mean ISI.
- **Hyperpolarizing threshold** introduces rebound spikes even when net synaptic drive is inhibitory.

## Pitfalls

- Adaptive threshold dynamics must be slow enough relative to the membrane time constant; otherwise the model effectively reverts to a fixed threshold.
- Binomial QC approximation assumes independent vesicle releases; correlated release or short-term plasticity require extension.
- The analytical FPT solution assumes diffusion-like statistics; Poisson input with large quanta may need exact simulation.

## Related Concepts

- Integrate-and-fire neurons
- Coefficient of variation
- Spike-frequency adaptation
- Post-inhibitory rebound
- First-passage-time analysis
- Excitatory-inhibitory balance
- Quantal content / synaptic vesicle release

## Activation

inter-spike interval, ISI statistics, adaptive threshold, EI circuit, first-passage time, spike variability, integrate-and-fire, post-inhibitory rebound, quantal content, neuronal noise
