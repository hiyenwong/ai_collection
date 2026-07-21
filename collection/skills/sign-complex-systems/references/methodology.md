# SIGN Methodology

Detailed methodology for Sparse Identification Graph Neural Network.

## Mathematical Foundation

### Network Dynamical Systems

Consider a networked dynamical system:

$$\frac{dx_i}{dt} = f_i(x_i, \{x_j\}_{j \in \mathcal{N}_i})$$

where:
- $x_i$ is the state of node $i$
- $\mathcal{N}_i$ is the neighborhood of node $i$
- $f_i$ is the governing dynamics

### Goal

Discover the function $f_i$ from observed time series data $\{x_i(t)\}$.

## SIGN Architecture

### 1. Graph Neural Network Encoder

**Message Passing:**

$$m_{ij} = \phi_e(h_i, h_j, e_{ij})$$

where:
- $h_i$ = node embedding of node $i$
- $e_{ij}$ = edge features between $i$ and $j$
- $\phi_e$ = edge message function

**Node Update:**

$$h_i' = \phi_n(h_i, \sum_{j \in \mathcal{N}_i} m_{ij})$$

### 2. Symbolic Library Construction

Build a library $\Theta$ of candidate functions:

$$\Theta = [1, x, y, x^2, y^2, xy, \sin(x), \cos(x), \ldots]$$

**Edge-level library:**

$$\Theta_{ij} = [\Delta x_{ij}, x_i \cdot x_j, \sin(\Delta x_{ij}), \ldots]$$

where $\Delta x_{ij} = x_j - x_i$ represents relative state differences.

### 3. Sparse Regression (STRidge)

**Sequential Threshold Ridge Regression:**

1. Initialize: $\xi = \Theta^\dagger \dot{x}$ (pseudoinverse solution)
2. Threshold: Remove terms with $|\xi_k| < \lambda$
3. Ridge: $\xi = (\Theta_{\text{active}}^T \Theta_{\text{active}} + \alpha I)^{-1} \Theta_{\text{active}}^T \dot{x}$
4. Iterate until convergence

**Result:** Sparse coefficient vector $\xi$ selecting active terms.

### 4. Equation Assembly

For each edge type, assemble the discovered equation:

$$\dot{x}_i = \sum_{k} \xi_k \cdot \theta_k(x_i, \{x_j\})$$

## Key Innovations

### Edge-level Discovery

Traditional SINDy operates on full system state, becoming computationally expensive for large networks.

SIGN performs discovery at edge level:
- Each edge discovers its interaction pattern
- Patterns are shared across similar edges
- Complexity decoupled from network size

### Scalability Analysis

| Network Size | Traditional SINDy | SIGN |
|--------------|-------------------|------|
| 100 nodes | O(100²) | O(100) |
| 1,000 nodes | O(10⁶) | O(1,000) |
| 100,000 nodes | O(10¹⁰) | O(100,000) |

SIGN achieves **linear complexity** in network size.

### Noise Robustness

- Statistical aggregation across edges
- Thresholding removes noise-induced spurious terms
- GNN smooths local noise through message passing

## Implementation Details

### Numerical Derivatives

$$\dot{x} \approx \frac{x(t+\Delta t) - x(t-\Delta t)}{2\Delta t}$$

For noisy data, use smoothing:

```python
def smooth_derivative(x, dt, window=5):
    """Compute smoothed numerical derivative."""
    # Savitzky-Golay filter
    from scipy.signal import savgol_filter
    smoothed = savgol_filter(x, window, 3)
    derivative = np.gradient(smoothed, dt)
    return derivative
```

### Library Functions

**Polynomial terms:**
$$[x, x^2, x^3, xy, x^2y, xy^2, \ldots]$$

**Trigonometric terms:**
$$[\sin(x), \cos(x), \sin(xy), \cos(xy), \ldots]$$

**Interaction terms:**
$$[x_j - x_i, (x_j - x_i)^2, x_i \cdot x_j, \ldots]$$

### Hyperparameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `sparsity_threshold` | 0.01 | Coefficient threshold |
| `ridge_alpha` | 1e-5 | Ridge regularization |
| `max_iterations` | 10 | STRidge iterations |
| `library_degree` | 3 | Polynomial degree |

## Validation

### Cross-validation

Split time series into training/validation:
- Train on first 70% of time points
- Validate on remaining 30%
- Check equation prediction accuracy

### Bootstrapping

For robustness assessment:
1. Bootstrap sample edges
2. Run SIGN on each sample
3. Aggregate discovered equations
4. Report consensus terms

## Limitations

1. **Assumes smooth dynamics**: Not suitable for discontinuous systems
2. **Requires sufficient sampling**: Need enough time points for derivative estimation
3. **Library design**: Must include relevant candidate functions
4. **Homogeneous assumption**: Assumes similar dynamics across network