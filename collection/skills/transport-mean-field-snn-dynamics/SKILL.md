---
name: transport-mean-field-snn-dynamics
description: "Transport-based mean field theory for spiking neural networks (SNNs). Derives approximate macroscopic dynamics of SNN populations using transport solutions to the Fokker-Planck/advection equation. Bridges microscopic integrate-and-fire neuron models to macroscopic firing rate fluctuations. Use when: (1) analyzing SNN population-level dynamics, (2) studying firing rate fluctuations and variability in neural networks, (3) deriving mean field approximations for coupled integrate-and-fire neurons with time-varying inputs, (4) modeling neural mass dynamics from transport/advective solutions rather than steady-state assumptions, (5) understanding how initial voltage distributions shape population responses."
---

# Transport Mean Field SNN Dynamics

Methodology from arXiv:2605.14319 (Nicola & Campbell, 2026).

## Core Contribution

Derives an approximation for the evolution of the instantaneous population firing rate (**flux**) as a function of the initial voltage distribution through a Fokker-Planck system, based on the **transport solution to the advection equation**.

Unlike earlier mean field approaches that assumed asynchronous or constant flux steady states, this method assumes:
- Time-varying inputs are **slow**
- Neurons operate in the **excitation-driven regime**

## Key Mathematical Framework

### Population Rate / Flux Definition

The instantaneous population rate \( \nu(t) \) (flux) emerges from the probability current at threshold in the Fokker-Planck equation:

\[
\frac{\partial \rho(v,t)}{\partial t} = -\frac{\partial}{\partial v}[J(v,t)]
\]

where \( \rho(v,t) \) is the voltage density and \( J(v,t) \) is the probability current.

### Transport-Based Approximation

For slow time-varying inputs and excitation-driven regimes, the transport solution to the advection equation provides:

\[
\nu(t) \approx \text{flux from transport solution with initial density } \rho(v,0)
\]

This predicts how firing rate fluctuations emerge from the dynamic interaction between:
1. **Time-varying inputs**
2. **Initial voltage densities**
3. **Network coupling**

### Advantages Over Previous Mean Field Methods

| Feature | Traditional MF | Transport MF (this paper) |
|---------|---------------|--------------------------|
| Assumption | Asynchronous steady state | Transport from arbitrary initial density |
| Handles slow input variations | Poorly | Well |
| Predicts fast fluctuations | Limited | Accurate |
| Depends on initial conditions | No | Yes |

## Application Workflow

### 1. Define the Neuron Model

Start with coupled integrate-and-fire neurons:

\[
\tau \dot{v}_i = -v_i + \mu_i(t) + \sigma_i \xi_i(t) + \sum_j w_{ij} \sum_k \delta(t - t_{jk})
\]

### 2. Derive the Fokker-Planck System

The population density evolves according to:

\[
\frac{\partial \rho}{\partial t} = -\frac{\partial}{\partial v}\left[ \frac{-v + \mu(t) + J_{\text{syn}}}{\tau} \rho - \frac{\sigma^2}{2\tau^2} \frac{\partial \rho}{\partial v} \right]
\]

### 3. Apply Transport Solution

For the excitation-driven regime with slow inputs:
- Solve the advection equation for the deterministic transport
- Use the initial voltage distribution \( \rho(v,0) \)
- Compute flux at threshold \( v_{\text{th}} \)

### 4. Validate Against Network Simulations

Compare the transport mean field predictions with direct simulation of the coupled integrate-and-fire network.

## Key Insights

1. **Initial density matters**: The shape of the initial voltage distribution significantly affects transient population dynamics.
2. **Coupling shapes fluctuations**: Network coupling transforms individual neuron variability into population-level oscillations.
3. **Slow input assumption**: The transport approximation works best when input timescales are slower than the neuron membrane time constant.

## Related Skills

- `spiking-neural-network-analysis` - General SNN paper analysis
- `neural-population-dynamics` - Neural population analysis methods
- `heterogeneous-synaptic-dynamics` - Synaptic heterogeneity modeling
