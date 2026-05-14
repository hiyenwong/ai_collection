---
name: quantum-gaussian-processes
description: "Quantum Gaussian Processes (QGP) methodology — Bayesian framework for learning from quantum systems through priors over unknown quantum transformations. Enables regression, classification, and Bayesian optimization directly on quantum data using quantum kernels derived from process structure and symmetries. Provable and scalable for matchgate/free-fermionic evolutions. Activation: quantum gaussian process, QGP, quantum kernel, bayesian quantum learning, free-fermion learning, quantum Bayesian optimization."
---

# Quantum Gaussian Processes (QGP)

Research methodology for Bayesian quantum machine learning using quantum Gaussian processes, based on Jäger et al. (arXiv: 2605.00099).

## Overview

Quantum Gaussian Processes provide a **Bayesian framework for learning from quantum systems** through priors over unknown quantum transformations. Under suitable conditions, unitary quantum stochastic processes define Gaussian processes, enabling regression, classification, and Bayesian optimization directly on quantum data. The key is injecting physics-informed inductive bias through quantum kernels derived from process structure and symmetries.

## Key Concepts

### 1. Quantum Gaussian Process Framework

- **Prior**: Place a Gaussian process prior over unknown quantum transformations
- **Quantum Kernel**: Define kernels from quantum process structure and symmetries
- **Inductive Bias**: Inject strong physics-informed priors via quantum kernels
- **Posterior**: Update beliefs about quantum transformations from measurement data

### 2. Provable Scalability for Matchgate Evolutions

- Matchgate (free-fermionic) evolutions give rise to **provable and scalable** QGPs
- First family where the unknown unitary acts **non-trivially on all qubits**
- Kernel computation scales efficiently with system size
- Provides theoretical guarantees for learning performance

### 3. Applications

- **Quantum Regression**: Predict quantum state properties from limited data
- **Quantum Classification**: Classify quantum states using kernel methods
- **Bayesian Optimization**: Sample-efficient optimization of quantum sensing tasks
- **Phase Diagram Learning**: Learn phase boundaries in many-body systems
- **Long-range Extrapolation**: Accurate prediction beyond training data range

## Methodology

### Quantum Kernel Construction

```python
import numpy as np

def quantum_kernel(x, x_prime, unitary_structure):
    """
    Construct quantum kernel from process structure.
    
    The kernel encodes the similarity between two inputs
    through the lens of the quantum process's symmetries.
    
    Args:
        x, x_prime: Input parameter configurations
        unitary_structure: Known structural information about the process
    
    Returns:
        Kernel value k(x, x')
    """
    # For matchgate/free-fermion processes:
    # k(x, x') = <ψ(x)|ρ(x')|ψ(x)>
    # where ρ is the quantum state at x' and |ψ(x)> is a probe state
    
    # Exploit free-fermion structure for efficient computation
    # via covariance matrix formalism
    gamma_x = build_covariance_matrix(x, unitary_structure)
    gamma_xp = build_covariance_matrix(x_prime, unitary_structure)
    
    # Gaussian kernel from covariance matrices
    diff = gamma_x - gamma_xp
    return np.exp(-0.5 * np.trace(diff @ diff.T))
```

### Bayesian Optimization on Quantum Data

```python
def quantum_bayesian_optimization(
    quantum_process,
    acquisition_function='EI',
    n_iterations=50,
    prior_structure='matchgate'
):
    """
    Bayesian optimization of quantum sensing/learning tasks.
    
    Uses QGP posterior to guide sampling of quantum experiments,
    achieving sample-efficient optimization.
    
    1. Initialize with small set of quantum measurements
    2. Fit QGP posterior over quantum transformation
    3. Select next measurement via acquisition function
    4. Update posterior and repeat
    """
    # Initialize with diverse quantum states
    X_init = design_quantum_experiment(n=5)
    y_init = quantum_process.measure(X_init)
    
    # Fit QGP posterior
    gp = QuantumGP(kernel=matchgate_kernel(prior_structure))
    gp.fit(X_init, y_init)
    
    for i in range(n_iterations):
        # Select next point via Expected Improvement
        x_next = gp.optimize_acquisition(acquisition_function)
        y_next = quantum_process.measure(x_next)
        gp.update(x_next, y_next)
    
    return gp.best_solution()
```

### Phase Diagram Learning

```python
def learn_quantum_phase_diagram(hamiltonian, parameter_range):
    """
    Learn phase boundaries in many-body quantum systems
    using QGP with physics-informed kernel.
    
    The kernel encodes locality and symmetry constraints
    of the Hamiltonian, enabling efficient learning
    from limited measurement data.
    """
    # Sample sparse points across parameter space
    X_sample = latin_hypercube_sampling(parameter_range, n=20)
    
    # Measure order parameters at each point
    order_params = measure_order_parameters(hamiltonian, X_sample)
    
    # Fit QGP with symmetry-aware kernel
    gp = QuantumGP(
        kernel=symmetry_kernel(hamiltonian.symmetries),
        noise_variance=measurement_noise
    )
    gp.fit(X_sample, order_params)
    
    # Predict full phase diagram
    X_dense = grid_sampling(parameter_range, resolution=100)
    phase_predictions = gp.predict(X_dense)
    uncertainty = gp.predict_uncertainty(X_dense)
    
    return phase_predictions, uncertainty
```

## Why QGP Over Standard QML?

| Aspect | Standard QML | Quantum GPs |
|--------|-------------|-------------|
| **Interpretability** | Black-box | Bayesian posterior provides uncertainty |
| **Sample Efficiency** | Requires large datasets | Works with few measurements |
| **Theoretical Guarantees** | Limited | Provable for matchgate evolutions |
| **Scalability** | Often limited | Efficient kernel computation |
| **Inductive Bias** | Architecture-dependent | Physics-informed via kernel design |

## Inductive Bias Design

### Structure-Based Priors

1. **Locality**: Encode that nearby parameters produce similar quantum states
2. **Symmetry**: Build group symmetries directly into the kernel
3. **Conservation Laws**: Enforce conserved quantities in the prior
4. **Scaling**: Incorporate known finite-size scaling behavior

### Kernel Design Patterns

```python
# Locality + Symmetry kernel
def physics_informed_quantum_kernel(x, x_prime, symmetries):
    # Base kernel from quantum overlap
    base = quantum_overlap_kernel(x, x_prime)
    
    # Symmetry averaging
    sym_avg = np.mean([
        base(symmetry(x), symmetry(x_prime))
        for symmetry in symmetries
    ])
    
    # Locality weighting
    locality = locality_weight(x, x_prime)
    
    return sym_avg * locality
```

## Performance Results

### Demonstrated Applications

1. **Long-range extrapolation**: Accurate prediction far beyond training data
2. **Phase diagram learning**: Efficient mapping of many-body phase boundaries
3. **Quantum sensing**: Sample-efficient Bayesian optimization

### Scalability

- Matchgate evolutions: **Poly(n)** kernel computation
- Free-fermion structure enables efficient covariance matrix updates
- First framework with provable scaling for full-system unitaries

## Implementation Notes

### When to Use QGP

- Limited quantum measurement budget
- Need uncertainty quantification
- Physics-informed priors available
- Regression/classification on quantum data

### When Not to Use QGP

- Very high-dimensional parameter spaces (>100 parameters)
- Non-stationary quantum processes without known structure
- Real-time quantum control (GP inference overhead)

### Computational Considerations

- Standard GP: O(n³) for n training points
- Use sparse GPs or inducing points for scalability
- Matchgate kernel: O(n²) or better via covariance structure

## Error Handling

### Finite Measurement Noise

- Quantum measurements are inherently noisy (shot noise)
- Include noise variance in GP likelihood
- Use heteroscedastic noise model if noise varies with parameters

### Kernel Misspecification

- If kernel doesn't match process structure, predictions degrade
- Validate kernel choice on held-out quantum data
- Use automatic relevance determination (ARD) for feature selection

## References

- Jäger, J., Braccia, P., Bermejo, P., Algaba, M.G., García-Martín, D., & Cerezo, M. (2026). Provable and scalable quantum Gaussian processes for quantum learning. arXiv: 2605.00099.
- Related: `quantum-ml-patterns`, `quantum-statistical-estimation`, `bayesian-agent-orchestration`
