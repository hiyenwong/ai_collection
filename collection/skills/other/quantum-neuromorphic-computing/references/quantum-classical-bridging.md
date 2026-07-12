# Quantum-Classical Bridging Patterns

## Deep Boltzmann Quantum States (DBM-NQS)

**Problem**: Classical and quantum spin glasses have exponentially many local energy minima due to disorder and frustration. Standard variational neural network models fail to represent the complex entanglement structure.

**Solution**: Use Deep Boltzmann Machine architectures as variational ansatz for quantum wavefunctions. Key innovations:
- Complex-valued amplitudes encode both magnitude and phase of the wavefunction
- Hidden layers capture multi-spin correlations beyond simple RBM
- Handles sign problem through complex-valued network parameters
- Variational Monte Carlo with stochastic reconfiguration for natural gradient descent

**When to use**: Ground-state problems of quantum spin glasses, classical spin glass energy minimization, systems with quenched disorder and frustration, when conventional mean-field approaches fail.

**Reference**: arXiv: 2605.15899 — "Solving Classical and Quantum Spin Glasses with Deep Boltzmann Quantum States" (Leone, Dutta, Heyl)

## Thermodynamic Networks for Autonomous Computation

**Problem**: Traditional computation requires external clocking and control, consuming significant energy. Need autonomous, energy-efficient computation paradigms.

**Solution**: Model computation as non-equilibrium steady states in networks of finite-size reservoirs exchanging conserved quantities (charge, molecular number) while relaxing toward equilibrium. Key properties:
- Computation through thermodynamic relaxation processes
- Autonomous: no external clocking or control needed
- Energy efficiency: powered by free energy dissipation
- Robust: thermodynamic stability provides noise resilience
- Scalable: modular composition of network elements

**When to use**: Designing physical computing systems, thermodynamic engines, autonomous molecular computation, neuromorphic computing with physical substrates.

**Reference**: arXiv: 2605.15985 — "Thermodynamic Networks: Harnessing Non-Equilibrium Steady States for Computation" (Lipka-Bartosik, Blasi, Puértolas)

## Born-Rule Dynamical Quantum Phase Transitions

**Problem**: Understanding how quantum measurement statistics relate to dynamical critical phenomena in time-evolving quantum systems.

**Solution**: Analyze DQPTs through Born-rule statistical measurement dynamics. DQPTs occur when quantum states exhibit nonanalytic changes in return probability (Loschmidt echo) during time evolution:
- Rate function: g(t) = -(1/N) ln|G(t)|² where G(t) = ⟨ψ(0)|ψ(t)⟩
- DQPTs occur at critical times where g(t) is nonanalytic
- Statistical ensemble of measurements reveals DQPT signatures
- Connection between measurement statistics and dynamical free energy

**Detection methods**:
- Interferometric measurement of Loschmidt echo
- Statistical analysis of return probability distributions
- Fisher zero analysis in complex time plane

**Key signatures**: Nonanalytic cusps in rate function, topological changes in dynamical order parameter, dynamical vortices in parameter space.

**When to use**: Analyzing quantum measurement-induced phase transitions, dynamical critical phenomena, quantum state fidelity dynamics, characterizing quantum quenches.

**Reference**: arXiv: 2605.16029 — "Born-rule statistical dynamical quantum phase transitions under measurement" (Chen, Zhu)

## Leggett-Garg Tests in Neural Dynamics

**Problem**: Distinguishing between diffusive (Wiener/cable-equation) models and non-diffusive persistent stochastic models in single-neuron dynamics.

**Solution**: Test Leggett-Garg-type temporal correlations in single-neuron dynamics:
- LGI as temporal analogue of Bell constraints for neural dynamics
- Persistent stochastic (Kac-type) models can violate LGI; diffusive models always satisfy it
- Violation indicates non-Markovian memory, not necessarily quantum coherence
- Incorporates memory and finite signal propagation speeds

**When to use**: Understanding ion channel dynamics, neural signaling at quantum-classical boundary, testing for non-diffusive processes in neural systems.

**Reference**: arXiv: 2605.12126 — "Leggett--Garg Tests in Neural Dynamics: Probing Non-Diffusive Stochastic Structure in Single Neurons" (Ghose)
