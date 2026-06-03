---
name: quantum-tensor-train-surrogates
description: "Local tensor-train surrogates methodology for quantum machine learning models. Constructs fast, cheap, provably accurate classical surrogates of fully trained QML models within local patches of input data space. Combines Taylor polynomial approximation with tensor-train representation via empirical risk minimization. Use when implementing efficient quantum ML inference acceleration, tensor-train approximation of quantum circuits, or local surrogate modeling for QML."
---

# Local Tensor-Train Surrogates for Quantum Learning Models

Research methodology from arXiv:2604.25631 (April 2026) - Nair & Ferrie.

## Core Idea

Addresses the key bottleneck in quantum machine learning: **computational cost of repeated quantum circuit evaluations during inference**. The solution constructs classical tensor-train surrogates that approximate QML models locally.

## Methodology

### Framework Components

1. **Taylor Polynomial Approximation**
   - Local approximation within patches of input data space
   - Controlled by patch radius `r` and polynomial degree `p`
   - Deterministic error certificate for approximation quality

2. **Tensor-Train (TT) Representation**
   - Efficient representation avoiding exponential scaling
   - Parameter count: `d_eff = N(p+1)χ²` instead of `(p+1)^N`
   - Bond dimension `χ` controls TT approximation error

3. **Empirical Risk Minimization**
   - Statistical learning paradigm for surrogate construction
   - Provably recovers surrogate with controlled generalization error
   - Sample complexity depends explicitly on local patch radius `r`

### Three Controllable Error Sources

| Error Type | Control Parameter | Description |
|------------|-------------------|-------------|
| Taylor Truncation | Patch radius `r`, degree `p` | Local polynomial approximation error |
| TT Approximation | Bond dimension `χ` | Tensor representation error |
| Statistical | Sample size `n` | Estimation error from finite data |

### Parameter Scaling

```
Naive scaling: (p+1)^N  (exponential in data dimensions)
TT scaling: N(p+1)χ²    (polynomial in data dimensions)
```

**Note**: Worst-case constants inherit exponential factor through tensor-product feature norm during Taylor embedding.

## Implementation Workflow

### Step 1: Data Space Partitioning

```python
def partition_input_space(data, patch_radius_r):
    """
    Divide input space into local patches of radius r
    """
    patches = []
    centers = select_patch_centers(data)
    for center in centers:
        patch = data[|data - center| < r]
        patches.append((center, patch))
    return patches
```

### Step 2: Local Taylor Expansion

```python
def taylor_expand(f, center, degree_p):
    """
    Compute Taylor polynomial of degree p around center
    """
    taylor_coeffs = []
    for order in range(degree_p + 1):
        deriv = compute_nth_derivative(f, center, order)
        taylor_coeffs.append(deriv)
    return taylor_coeffs
```

### Step 3: Tensor-Train Construction

```python
def build_tt_surrogate(taylor_coeffs, bond_dim_chi):
    """
    Construct tensor-train representation of Taylor polynomial
    """
    tt_cores = []
    for dim in range(N):
        core = initialize_tt_core(dim, bond_dim_chi)
        tt_cores.append(core)
    return optimize_tt_cores(tt_cores, taylor_coeffs)
```

### Step 4: Empirical Risk Minimization

```python
def train_surrogate(tt_model, local_data, local_labels, loss_fn):
    """
    Optimize TT parameters via empirical risk minimization
    """
    def risk(tt_params):
        predictions = tt_forward(tt_model, tt_params, local_data)
        return loss_fn(predictions, local_labels)
    
    optimal_params = minimize(risk, initial_params)
    return optimal_params
```

## Usage Patterns

### Pattern 1: Single-Patch Surrogate

For small input regions or low-dimensional data:
- Use single patch covering entire input space
- Higher polynomial degree `p`
- Larger bond dimension `χ`

### Pattern 2: Multi-Patch Ensemble

For high-dimensional or complex input spaces:
- Multiple overlapping patches
- Local experts (one per patch)
- Smooth interpolation between patches

### Pattern 3: Adaptive Refinement

For dynamic accuracy requirements:
- Start with coarse approximation
- Refine patches where error > threshold
- Iteratively increase `p` or decrease `r`

## Error Bounds

### Theoretical Guarantees

The framework provides explicit bounds on:

1. **Approximation Error**: ||f - f_TT|| ≤ ε_Taylor + ε_TT
2. **Generalization Error**: With probability 1-δ, R(f̂) ≤ R(f*) + O(√(d_eff/n))
3. **Overall Error**: Decomposition into three independent controllable sources

### Practical Considerations

- **Feature Norm**: Exponential constant from Taylor embedding
- **Sample Complexity**: Scales with local patch radius `r`
- **Computational Cost**: Polynomial in dimensions, linear in samples

## Comparison with Alternatives

| Method | Cost | Accuracy | Scalability |
|--------|------|----------|-------------|
| Direct QML | High (quantum) | Exact | Limited |
| Neural Network | Medium | Good | Good |
| **TT Surrogates** | **Low** | **Controllable** | **Polynomial** |
| Gaussian Process | Medium | Good | Poor (cubic) |

## Applications

- **Variational Quantum Classifiers**: Fast inference after training
- **Quantum Kernel Methods**: Classical evaluation of quantum kernels
- **Quantum Generative Models**: Efficient sampling via classical surrogate
- **Error Mitigation**: Classical pre-computation for quantum circuits

## Tools Used

- `exec`: Python for numerical implementation (NumPy, Quimb, Scipy)
- `read`: Load trained QML models and training data
- `write`: Save tensor-train surrogates and evaluation results

## References

- **Primary Paper**: arXiv:2604.25631 - "Local tensor-train surrogates for quantum learning models"
- **Tensor-Train**: Oseledets, I. (2011). Tensor-train decomposition
- **Quantum ML**: Schuld & Petruccione (2021). Machine Learning with Quantum Computers

## Related Skills

- quantum-neural-network-designer
- quantum-ml-research
- quantum-annealing-feature-selection
