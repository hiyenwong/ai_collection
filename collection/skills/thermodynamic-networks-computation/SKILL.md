---
name: thermodynamic-networks-computation
description: "Thermodynamic Networks methodology for autonomous physics-based computation using non-equilibrium steady states. Identifies Negative Differential Conductance (NDC) as the critical property for computational expressivity. Applies to quantum dot networks, enzymatic reaction networks, and physical reservoir computing. Activation: thermodynamic networks, non-equilibrium computation, steady-state computing, NDC computation, physics-based computation, autonomous computation."
---

# Thermodynamic Networks for Autonomous Computation

> Framework for autonomous, physics-based computation using non-equilibrium steady states, where computation emerges from the natural tendency of coupled finite-size reservoirs to exchange conserved quantities and relax to steady states.

## Metadata
- **Source**: arXiv:2605.15985
- **Authors**: Patryk Lipka-Bartosik, Gianmichele Blasi, Javier Lalueza Puértolas, Géraldine Haack, Martí Perarnau-Llobet, Nicolas Brunner
- **Published**: 2026-05-15
- **Categories**: quant-ph; cond-mat.stat-mech; cs.NE; physics.bio-ph

## Core Methodology

### Key Innovation

**Thermodynamic Networks** — a unified framework where computation is performed by physical systems relaxing to non-equilibrium steady states, rather than by sequential algorithmic steps. The framework establishes a rigorous link between non-equilibrium thermodynamics and computational expressivity.

### The Central Result: NDC as Expressivity Switch

**Negative Differential Conductance (NDC)** is identified as the critical physical property governing computational expressivity:

- **Without NDC**: Networks restricted to computing only monotonic functions (severely limited expressivity)
- **With NDC**: Networks achieve universal function approximation (full computational expressivity)

This establishes a clear physical criterion for when a thermodynamic system can perform general computation.

### Framework Architecture

```
[Input Configuration] → [Network of Coupled Reservoirs] → [Non-Equilibrium Steady State] → [Output/Result]
                          │
                          ├── Finite-size reservoirs exchange conserved quantities
                          │   (electric charge, molecular number, etc.)
                          ├── System relaxes to steady state encoding solution
                          └── Training exploits natural equilibration tendency
```

### Training Protocol

Training leverages the system's natural tendency to equilibrate:
1. Configure reservoir parameters and couplings
2. Apply input as initial/boundary conditions
3. Let system naturally evolve to steady state
4. Read output from steady-state configuration
5. Adjust parameters to minimize error (gradient-free or physics-informed)

## Implementation Guide

### Prerequisites
- Understanding of non-equilibrium thermodynamics
- Knowledge of open quantum systems or chemical kinetics
- Python with numpy/scipy for simulation

### Platform 1: Quantum Dot Networks

```python
import numpy as np
from scipy.integrate import solve_ivp

class QuantumDotNetwork:
    """Thermodynamic network using quantum dots as finite reservoirs."""
    
    def __init__(self, n_dots, tunnel_couplings, energy_levels, temperature):
        self.n_dots = n_dots
        self.tunnel_couplings = tunnel_couplings  # Gamma_{ij}
        self.energy_levels = energy_levels        # E_i
        self.temperature = temperature            # k_B * T
        self.beta = 1.0 / temperature
        
    def fermi_function(self, E, mu):
        """Fermi-Dirac distribution."""
        return 1.0 / (1.0 + np.exp(self.beta * (E - mu)))
    
    def current(self, n, mu_source, mu_drain):
        """
        Compute particle current between quantum dots.
        Can exhibit Negative Differential Conductance (NDC).
        """
        currents = np.zeros(self.n_dots)
        for i in range(self.n_dots):
            for j in range(self.n_dots):
                if i != j:
                    gamma = self.tunnel_couplings[i, j]
                    f_i = self.fermi_function(self.energy_levels[i], mu_source)
                    f_j = self.fermi_function(self.energy_levels[j], mu_drain)
                    currents[i] += gamma * (n[j] * (1 - n[i]) * f_j - 
                                            n[i] * (1 - n[j]) * f_i)
        return currents
    
    def steady_state_dynamics(self, t, n, chemical_potentials):
        """ODE for particle number evolution."""
        dn_dt = self.current(n, chemical_potentials[0], chemical_potentials[1])
        return dn_dt
    
    def compute_steady_state(self, chemical_potentials, n0=None, t_max=100):
        """Find non-equilibrium steady state."""
        if n0 is None:
            n0 = np.full(self.n_dots, 0.5)
        
        sol = solve_ivp(
            lambda t, n: self.steady_state_dynamics(t, n, chemical_potentials),
            [0, t_max], n0, method='RK45', rtol=1e-8
        )
        return sol.y[:, -1]  # Final state = steady state
    
    def has_ndc(self, chemical_potentials, n0=None):
        """
        Check if the network exhibits Negative Differential Conductance.
        NDC: dI/dV < 0 for some voltage range.
        """
        voltages = np.linspace(0.01, 2.0, 50)
        currents = []
        for V in voltages:
            mu = np.array([V/2, -V/2])
            n_ss = self.compute_steady_state(mu, n0)
            I = np.sum(self.current(n_ss, mu[0], mu[1]))
            currents.append(I)
        
        currents = np.array(currents)
        dI_dV = np.diff(currents) / np.diff(voltages)
        return np.any(dI_dV < 0)  # True if NDC present
```

### Platform 2: Enzymatic Reaction Networks

```python
class EnzymaticReactionNetwork:
    """Thermodynamic network using enzymatic reactions."""
    
    def __init__(self, n_species, rate_constants, stoichiometry):
        self.n_species = n_species
        self.k = rate_constants      # Reaction rate constants
        self.S = stoichiometry       # Stoichiometric matrix
        
    def reaction_rates(self, concentrations):
        """Compute reaction rates (can exhibit NDC-like behavior)."""
        rates = []
        for i, k in enumerate(self.k):
            # Michaelis-Menten-like kinetics
            # NDC can emerge from substrate inhibition
            substrate = concentrations[i % self.n_species]
            rate = k * substrate / (1 + substrate + substrate**2)  # Inhibition term
            rates.append(rate)
        return np.array(rates)
    
    def dynamics(self, t, concentrations):
        """Mass-action dynamics."""
        rates = self.reaction_rates(concentrations)
        return self.S @ rates
    
    def steady_state(self, initial_concentrations):
        """Find steady-state concentrations."""
        sol = solve_ivp(self.dynamics, [0, 1000], initial_concentrations,
                       method='RK45', rtol=1e-8)
        return sol.y[:, -1]
```

### Universal Function Approximation with NDC

```python
def approximate_function(thermo_network, target_fn, x_range, n_training_points=100):
    """
    Use thermodynamic network to approximate arbitrary function.
    Requires network with NDC capability.
    """
    # Training: adjust network parameters to match target function
    # Readout: steady state encodes function value
    
    x_train = np.linspace(*x_range, n_training_points)
    y_target = target_fn(x_train)
    
    # Optimization loop (gradient-free or physics-informed)
    for iteration in range(1000):
        # Forward pass: compute steady state for each input
        y_pred = []
        for x in x_train:
            steady = thermo_network.compute_steady_state([x, 0])
            y_pred.append(steady[0])  # Read from first reservoir
        
        y_pred = np.array(y_pred)
        loss = np.mean((y_pred - y_target) ** 2)
        
        # Update parameters (simplified)
        # ... parameter adjustment logic ...
        
    return y_pred
```

## Applications

1. **Physical reservoir computing**: Use thermodynamic relaxation as computational substrate
2. **Molecular computing**: Enzymatic networks as autonomous molecular computers
3. **Quantum information processing**: Quantum dot networks for quantum-classical hybrid computation
4. **Neuromorphic devices**: Bio-inspired computing using physical steady states
5. **Biological computation**: Understanding computation in cellular networks

## Theoretical Framework

### Expressivity Theorem

- **Theorem**: A thermodynamic network can approximate any continuous function on a compact domain **if and only if** it exhibits Negative Differential Conductance.
- **Proof sketch**: NDC provides the non-monotonicity needed for universal approximation; without it, the network is restricted to monotonic functions.

### Connection to Existing Fields

| Field | Connection |
|-------|-----------|
| Reservoir Computing | Steady state replaces echo state property |
| Physics-Informed NN | Physical constraints are intrinsic, not penalized |
| Chemical Computing | Enzymatic networks as formalized thermodynamic computers |
| Quantum Computing | Quantum dot networks provide quantum-enhanced reservoirs |

## Pitfalls

1. **NDC is necessary**: Without NDC, the network can only compute monotonic functions — verify NDC presence before attempting universal approximation
2. **Training exploits equilibration**: Training must work WITH the natural physics, not against it — gradient-based optimization may not be appropriate
3. **Finite-size effects matter**: The framework relies on finite-size reservoirs; infinite reservoirs behave differently
4. **Steady-state convergence**: Ensure the system actually reaches a steady state; some parameter regimes may produce oscillations or chaos
5. **Physical realizability**: Both quantum dot and enzymatic platforms have been demonstrated, but engineering NDC requires careful design

## Related Skills

- thermocoherent-cognitive-dynamics
- nonequilibrium-brain-dynamics-physics
- quantum-reservoir-computing
- energy-based-neurocomputation
- physics-guided-neural-networks
- parametric-oscillator-reservoir-computing
