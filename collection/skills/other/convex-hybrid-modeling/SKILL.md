---
name: convex-hybrid-modeling
description: "Convex Hybrid Modeling methodology using operator theory for process control and systems engineering. Formulates convex learning problems that combine model interpretability with system identification efficiency. Covers three settings: (1) regularization around a reference model, (2) restriction on interpretable subspaces, (3) kernel-based mixture models on interpretable manifolds. Use when: building interpretable control models, combining physics-based and data-driven modeling, designing hybrid model learning frameworks, or applying operator-theoretic approaches to system identification. Activation: convex hybrid modeling, operator-based control, interpretable modeling, kernel mixture models, process control, system identification, reference model regularization, canonical features, lifted parameters."
---

# Convex Hybrid Modeling: An Operator-Based Approach

Based on: Tang, W. (2026). "Convex Hybrid Modeling: An Operator-Based Approach." arXiv:2605.23151. Submitted to FOCAPO/CPC 2027.

## Problem

Machine learning can accurately model process systems, but models for decision-making (especially in process control) must also be:
- **Structurally simple**: (Nearly) linear models preferred over nonlinear ones
- **Physically interpretable**: Must satisfy first-principles constraints
- **Efficiently computable**: Surrogate models for optimization

Standard ML approaches excel at accuracy but struggle with interpretability and constraint satisfaction.

## Core Innovation

The paper bridges operator theory with convex optimization to create hybrid models that are simultaneously:
- **Expressive** (can represent nonlinear dynamics)
- **Interpretable** (constrained by known physics)
- **Efficient** (convex learning problems, not non-convex)

### Key Insight: Lifted Parameters

By introducing an operator-theoretic technique to re-parameterize models in "lifted" parameters (canonical features, potentially infinite-dimensional), the system becomes a **kernel-based mixture of interpretable models**.

## Three Hybrid Modeling Settings

### Setting 1: Regularization Around a Reference Model

**Goal**: Learn a model that stays close to a known reference model while fitting data.

```python
minimize    loss(model, data) + λ · ||model - reference_model||²
subject to  model ∈ InterpretableModelFamily
```

- Linear in the parameters when model is linear
- λ controls trade-off between data fit and prior knowledge
- Equivalent to Bayesian MAP estimation with Gaussian prior on model parameters

**Use case**: When you have a first-principles model that is approximately correct and want to refine it with data.

### Setting 2: Restriction on an Interpretable Subspace

**Goal**: Force the model to live in a known "interpretable subspace" — a set of physically meaningful basis functions.

```python
minimize    loss(model, data)
subject to  model ∈ span{φ₁, φ₂, ..., φₖ}
```

- φᵢ are physically interpretable basis functions (e.g., polynomial terms, eigenmodes)
- The subspace encodes known physics exactly
- Learning reduces to convex optimization in the subspace coefficients

**Use case**: When you know the functional form of the dynamics but need to identify coefficients.

### Setting 3: Restriction on an Interpretable Manifold (Most General)

**Goal**: Learn models on a nonlinearly parameterized manifold of interpretable models.

**Solution**: Introduce "lifted" canonical features via operator theory:

- Map original parameters to a potentially infinite-dimensional feature space
- Kernel trick makes computation tractable
- Model is a kernel-based mixture of interpretable models
- Reproducing kernel Hilbert space (RKHS) formulation ensures convexity

```python
# Kernel-based mixture of interpretable models
model(x) = Σᵢ wᵢ · k(x, xᵢ) · g_local(x; θᵢ)

# where:
# k(x, xᵢ) = kernel weighting (data-driven attention)
# g_local(x; θᵢ) = local interpretable model at data point xᵢ
# wᵢ = mixture weights (learned convexly)
```

**Use case**: When dynamics are nonlinear and not well-captured by a fixed subspace, but local interpretable models can approximate the behavior.

## Methodology Implementation

### Static Model Learning

```python
class ConvexHybridModel:
    def __init__(self, reference_model=None, kernel='rbf', regularization=0.1):
        self.reference = reference_model
        self.kernel = Kernel(kernel)
        self.reg = regularization
        self.weights = None
    
    def fit_setting1(self, X, y):
        """Regularization around reference model"""
        # Convex optimization: ||y - Φθ||² + λ||θ - θ_ref||²
        # Closed form: θ = (ΦᵀΦ + λI)⁻¹(Φᵀy + λ·θ_ref)
        Phi = self._compute_basis(X)
        self.weights = np.linalg.solve(
            Phi.T @ Phi + self.reg * np.eye(Phi.shape[1]),
            Phi.T @ y + self.reg * self.reference.params
        )
    
    def fit_setting2(self, X, y):
        """Restriction on interpretable subspace"""
        # Subspace basis defined by φ functions
        # Solve: min ||y - Φθ||² s.t. θ ∈ subspace
        Phi = self._compute_basis(X)
        subspace_projection = self._projection_matrix()
        self.weights = subspace_projection @ np.linalg.lstsq(
            Phi @ subspace_projection, y
        )[0]
    
    def fit_setting3(self, X, y):
        """Kernel-based mixture on interpretable manifold"""
        # Use Nyström approximation for large datasets
        # Kernel matrix K with K_ij = k(x_i, x_j)
        K = self.kernel.matrix(X)
        # Convex: α = (K + λI)⁻¹y
        alpha = np.linalg.solve(
            K + self.reg * np.eye(len(X)), y
        )
        self.dual_weights = alpha
        self.support_vectors = X
    
    def predict(self, X):
        if self.dual_weights is not None:
            K = self.kernel.matrix(X, self.support_vectors)
            return K @ self.dual_weights
        return self._basis_predict(X)
```

### Dynamic Model Learning

```python
class ConvexHybridDynamics:
    """NARX-style dynamics model with convex learning"""
    
    def __init__(self, input_dim, output_dim, lag_order=2, **kwargs):
        self.p = lag_order  # number of past inputs/outputs
        self.feature_map = NonlinearLiftedFeatures(input_dim, output_dim)
        self.model = ConvexHybridModel(**kwargs)
    
    def fit(self, u, y):
        # Build regressor matrix from lagged I/O data
        Z = self._build_regressor(u, y)
        # Target: one-step-ahead prediction
        y_target = y[self.p:]
        self.model.fit(Z, y_target)
    
    def _build_regressor(self, u, y):
        """Create feature vector: [y_{k-1}, ..., y_{k-p}, u_{k-1}, ..., u_{k-p}]"""
        N = len(u) - self.p
        Z = np.zeros((N, self.p * (u.shape[1] + y.shape[1])))
        for k in range(self.p):
            Z[:, k*y.shape[1]:(k+1)*y.shape[1]] = y[k:k+N]
            Z[:, self.p*y.shape[1] + k*u.shape[1]:self.p*y.shape[1] + (k+1)*u.shape[1]] = u[k:k+N]
        return Z
    
    def predict(self, u, y_initial):
        y_pred = [y_initial[-self.p:]]
        for k in range(len(u)):
            z = self._build_single_step(y_pred[-1], u[k])
            y_next = self.model.predict(z.reshape(1, -1))
            y_pred.append(y_next.flatten())
        return np.array(y_pred)
```

## Numerical Examples

The paper demonstrates the approach on:

1. **Static modeling**: Nonlinear static function approximation with interpretable basis functions
2. **Dynamic modeling**: Identification of nonlinear process dynamics (e.g., chemical reactor)
3. **Comparison**: Against pure ML (overfits without regularization) and pure physics-based (insufficient flexibility)

## Benefits

- **Convex optimization**: Guaranteed global optimum, no local minima
- **Interpretability**: Model structure constrained by known physics
- **Data efficiency**: Less data needed than pure black-box ML
- **Scalability**: Kernel methods with Nyström approximation handle large datasets
- **Unified framework**: Same methodology covers static and dynamic models

## Pitfalls

- Kernel choice significantly affects performance (use cross-validation)
- Setting 3's "lifted parameters" require careful feature engineering
- Interpretable manifold may not capture all nonlinear dynamics
- For very large datasets, random Fourier features may be needed instead of exact kernel
- The method assumes the reference model and subspace are known a priori

## Related Work

- **Koopman operator theory**: Koopman mode decomposition and DMD for linear representations of nonlinear systems
- **Gaussian processes**: Non-parametric Bayesian approach, related via kernel formulation
- **Sparse identification (SINDy)**: Symbolic regression for interpretable dynamics
- **Physics-informed neural networks (PINNs)**: Neural network approach with physics constraints

## Activation Keywords

- Convex hybrid modeling
- Operator-based control
- Interpretable system identification
- Kernel mixture models for control
- Reference model regularization
- Lifted parameterization
- Canonical features
- Process control hybrid models
- Convex learning for dynamics
- Operator theory systems engineering
