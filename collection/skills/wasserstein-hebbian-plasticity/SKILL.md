---
name: wasserstein-hebbian-plasticity
description: Wasserstein Geometric Framework for Hebbian Plasticity (Tan-HWG). Models memory states as probability measures evolving through Wasserstein minimizing movements. Unifies diverse plasticity rules as gradient flows on Wasserstein space with JKO scheme, Hebbian energy functionals, and sequential stability.
tags:
  - wasserstein
  - hebbian
  - plasticity
  - optimal-transport
  - JKO
  - memory-dynamics
  - gradient-flow
  - computational-neuroscience
triggers:
  - wasserstein hebbian
  - plasticity geometry
  - JKO updates
  - optimal transport learning
  - memory dynamics
  - Tan-HWG
---

# Wasserstein Geometric Framework for Hebbian Plasticity (Tan-HWG)

## 1. Overview

The **Tan-HWG** (Hebbian-Wasserstein-Geometry) framework provides a geometric theory of Hebbian plasticity where memory states are modeled as **probability measures** evolving through **Wasserstein minimizing movements**. This variational structure unifies diverse plasticity rules as gradient flows on Wasserstein space, revealing a fundamental geometric structure underlying Hebbian learning.

### Key Innovations
- Memory states as probability measures, not point vectors
- Hebbian learning rules formalized as Hebbian energy functionals
- Sequential stability condition ensuring well-posed updates
- Fundamental separation between internal (continuous) and observable (discrete) dynamics
- Energy descent inequality guaranteeing convergence

### When to Use
- Designing biologically plausible learning rules with geometric guarantees
- Analyzing stability of Hebbian plasticity through optimal transport
- Modeling memory consolidation as measure-valued dynamics
- Unifying multiple plasticity rules under a single geometric framework
- Implementing gradient flows on probability measure spaces

## 2. Mathematical Foundations

### 2.1 Wasserstein Space

The **Wasserstein space** $\mathcal{P}_2(\mathbb{R}^d)$ is the space of probability measures with finite second moment, equipped with the **Wasserstein-2 distance**:

$$W_2(\mu, \nu) = \left(\inf_{\gamma \in \Gamma(\mu, \nu)} \int_{\mathbb{R}^d \times \mathbb{R}^d} |x - y|^2 \, d\gamma(x, y)\right)^{1/2}$$

where $\Gamma(\mu, \nu)$ is the set of all couplings (transport plans) between $\mu$ and $\nu$.

**Key properties:**
- $\mathcal{P}_2(\mathbb{R}^d)$ is a geodesic space with non-negative curvature in the Otto calculus sense
- Tangent space at $\mu$: closure of gradients of smooth functions in $L^2(\mu)$
- Geodesics are displacement interpolations via optimal transport maps

### 2.2 JKO Scheme (Jordan-Kinderlehrer-Otto)

The **JKO scheme** defines a time-discrete gradient flow on Wasserstein space via minimizing movements:

Given time step $\tau > 0$ and current measure $\mu_n$, compute:

$$\mu_{n+1} \in \arg\min_{\mu \in \mathcal{P}_2} \left\{ \mathcal{E}(\mu) + \frac{1}{2\tau} W_2^2(\mu, \mu_n) \right\}$$

**Properties:**
- As $\tau \to 0$, the scheme converges to the Wasserstein gradient flow $\partial_t \mu = -\text{grad}_{W_2} \mathcal{E}(\mu)$
- Provides implicit time-stepping with inherent stability
- Each step solves an optimal transport regularized energy minimization

### 2.3 Hebbian Energy Functionals

A **Hebbian energy** $\mathcal{E}: \mathcal{P}_2(\mathbb{R}^d) \to \mathbb{R} \cup \{+\infty\}$ formalizes the plasticity objective:

$$\mathcal{E}(\mu) = \mathbb{E}_{w \sim \mu}[\Phi(w; \mathcal{D})] + \lambda \mathcal{R}(\mu)$$

where:
- $\Phi(w; \mathcal{D})$ is the Hebbian correlation term (e.g., $-\frac{1}{2}w^\top C w$ for Oja's rule)
- $\mathcal{R}(\mu)$ is a regularization (entropy, Fisher information, etc.)
- $\lambda$ controls the regularization strength

**Common Hebbian energies:**
| Rule | Energy Form |
|------|-------------|
| Oja's rule | $\mathcal{E}(\mu) = -\frac{1}{2}\mathbb{E}[w^\top C w] + \frac{\beta}{4}(\mathbb{E}[\|w\|^2] - 1)^2$ |
| BCM | $\mathcal{E}(\mu) = -\frac{1}{3}\mathbb{E}[(w^\top x)^3] + \frac{\theta}{2}\mathbb{E}[(w^\top x)^2]$ |
| Covariance rule | $\mathcal{E}(\mu) = -\mathbb{E}[w^\top \Sigma w]$ |

## 3. Sequential Stability Conditions

The **sequential stability condition** ensures well-posedness of the fiberwise JKO updates:

### Definition
A Hebbian energy $\mathcal{E}$ satisfies sequential stability if for all $\mu \in \mathcal{P}_2$ and sufficiently small $\tau$:

$$\exists \, \alpha > 0, \, K \in \mathbb{R} \text{ such that:}$$
$$\mathcal{E}(\nu) \geq \mathcal{E}(\mu) + \langle \xi, \exp_\mu^{-1}(\nu) \rangle - \frac{K}{2} W_2^2(\mu, \nu)$$

for all $\nu$ in a neighborhood of $\mu$, where $\xi \in \partial \mathcal{E}(\mu)$ and $\exp_\mu$ is the exponential map on Wasserstein space.

### Verification Steps

1. **Check lower semicontinuity**: Verify $\mathcal{E}$ is lower semicontinuous w.r.t. narrow convergence
2. **Compute subdifferential**: Find $\partial \mathcal{E}(\mu)$ in the Wasserstein sense
3. **Verify semi-convexity**: Show $\mathcal{E} + \frac{K}{2}W_2^2$ is geodesically convex for some $K$
4. **Establish compactness**: Prove sublevel sets $\{\mu : \mathcal{E}(\mu) \leq c\}$ are compact in $\mathcal{P}_2$

### Energy Descent Inequality

For a sequentially stable Hebbian energy, the JKO iterates satisfy:

$$\mathcal{E}(\mu_{n+1}) + \frac{1}{2\tau} W_2^2(\mu_{n+1}, \mu_n) \leq \mathcal{E}(\mu_n)$$

This guarantees monotone energy decrease along the learning trajectory.

## 4. Internal vs Observable Dynamics Separation

The Tan-HWG framework reveals a **fundamental separation**:

### Internal Dynamics (Continuous)
- Memory state $\mu_t \in \mathcal{P}_2(\mathbb{R}^d)$ evolves continuously via Wasserstein gradient flow
- Governed by: $\partial_t \mu_t = \nabla \cdot (\mu_t \nabla \frac{\delta \mathcal{E}}{\delta \mu_t})$
- Represents the underlying synaptic weight distribution
- Always smooth (under regularity assumptions)

### Observable Dynamics (Discrete)
- Observable output $y_t$ is updated through **threshold crossings**
- Defined by: $y_t = \arg\max_k \mathbb{E}_{w \sim \mu_t}[f_k(w)]$ when crossing threshold $\theta$
- Represents the actual neural response or decision
- Piecewise constant, jumps at discrete times

### Implications

| Aspect | Internal | Observable |
|--------|----------|------------|
| Time domain | Continuous | Discrete |
| Space | $\mathcal{P}_2(\mathbb{R}^d)$ | Finite set / $\mathbb{R}^k$ |
| Update rule | Gradient flow | Threshold crossing |
| Smoothness | Smooth (typically) | Discontinuous |
| Interpretation | Memory state | Behavioral output |

This separation explains why learning appears discontinuous at the behavioral level despite smooth underlying synaptic changes.

## 5. Implementation Methodology

### Step 1: Discretize the Probability Measure

Choose a representation for $\mu$:

**Option A — Particle approximation:**
$$\mu \approx \frac{1}{N}\sum_{i=1}^N \delta_{w_i}$$
- Each $w_i$ is a "particle" (synaptic weight configuration)
- Wasserstein distance between particle sets via assignment problem

**Option B — Parametric family:**
$$\mu_\theta = \mathcal{N}(m(\theta), \Sigma(\theta))$$
- Track mean and covariance parameters
- Closed-form $W_2$ for Gaussians:
$$W_2^2(\mathcal{N}_1, \mathcal{N}_2) = \|m_1 - m_2\|^2 + \text{Tr}(\Sigma_1 + \Sigma_2 - 2(\Sigma_1^{1/2}\Sigma_2\Sigma_1^{1/2})^{1/2})$$

**Option C — Grid discretization:**
- Discretize space into cells, track mass per cell
- Use Sinkhorn algorithm for approximate optimal transport

### Step 2: Implement the JKO Update

For each time step $n$:

```
Given: μ_n, step size τ, energy functional ℰ

1. Define the objective: J(μ) = ℰ(μ) + (1/(2τ)) * W₂²(μ, μ_n)

2. Solve the minimization:
   a. If particle: optimize positions {w_i} via gradient descent
   b. If parametric: optimize θ via natural gradient
   c. If grid: use Sinkhorn-regularized OT + energy gradient

3. Set μ_{n+1} = argmin J(μ)
```

### Step 3: Compute Wasserstein Gradient

The Wasserstein gradient of $\mathcal{E}$ at $\mu$ is:

$$\text{grad}_{W_2} \mathcal{E}(\mu) = -\nabla \cdot \left(\mu \nabla \frac{\delta \mathcal{E}}{\delta \mu}\right)$$

**Practical computation:**

```python
def wasserstein_gradient(energy_fn, mu, points):
    """Compute Wasserstein gradient at discrete points."""
    # Compute functional derivative
    dE_dmu = energy_fn.functional_derivative(mu, points)
    
    # Compute spatial gradient of functional derivative
    grad_dE = jacobian(dE_dmu, points)  # shape: (N, d)
    
    # Wasserstein gradient flow direction
    v = -grad_dE  # velocity field
    
    return v
```

### Step 4: Time Integration

Use implicit or semi-implicit time stepping:

```
Explicit Euler (unstable for stiff problems):
    w_i^{n+1} = w_i^n + τ * v(w_i^n)

Implicit (JKO-style, stable):
    w_i^{n+1} = w_i^n + τ * v(w_i^{n+1})
    → Solve fixed-point iteration or use proximal methods

Semi-implicit (recommended):
    w_i^{n+1} = w_i^n + τ * v(w_i^n)
    Project onto constraint set if needed
```

### Step 5: Observable Extraction

After updating internal state $\mu_t$:

```
1. Compute observable: y = g(μ_t) where g is the readout function
2. Check threshold: if |y - y_prev| > θ, record observable update
3. Return (μ_t, y, update_flag)
```

## 6. Applications to Biologically Plausible Learning

### 6.1 Synaptic Consolidation

Model memory consolidation as measure evolution:
- **Encoding**: Rapid JKO steps with high learning rate (short $\tau$)
- **Consolidation**: Slow JKO steps with regularization (entropy penalty)
- **Recall**: Observable extraction from consolidated measure

### 6.2 Multi-Timescale Plasticity

Different synaptic populations evolve on different Wasserstein geometries:
- **Fast weights**: Low regularization, large $\tau$, frequent updates
- **Slow weights**: High regularization, small $\tau$, sparse updates
- Coupling through shared energy functional

### 6.3 Meta-Learning as Higher-Order Flow

Meta-learning corresponds to gradient flow **on the space of energy functionals**:
- Outer loop: optimize energy parameters $\lambda$
- Inner loop: JKO updates with current $\mathcal{E}_\lambda$
- Geometry: Wasserstein-Fisher-Rao or compound metrics

### 6.4 Homeostatic Plasticity

Add homeostatic constraints to the JKO scheme:
- Constraint: $\mathbb{E}_{w \sim \mu}[\|w\|^2] = C$ (fixed activity level)
- Implementation: Project onto constraint manifold after each JKO step
- Equivalent to Lagrange multiplier in the energy functional

## 7. Practical Pitfalls and Verification

### Pitfall 1: Non-Convex Energy Landscapes
**Problem**: Hebbian energies are typically non-convex → JKO may converge to local minima
**Solution**: 
- Use multiple initial particles/measures
- Add entropy regularization: $\mathcal{E}_{reg}(\mu) = \mathcal{E}(\mu) + \beta \text{Ent}(\mu)$
- Verify with different random seeds

### Pitfall 2: Curse of Dimensionality in $W_2$
**Problem**: Exact $W_2$ computation is $O(N^3 \log N)$ for $N$ particles
**Solution**:
- Use Sinkhorn approximation with entropic regularization
- For Gaussians, use closed-form $W_2$
- Consider sliced Wasserstein distance for high dimensions

### Pitfall 3: Time Step Selection
**Problem**: Too large $\tau$ → instability; too small $\tau$ → slow convergence
**Solution**:
- Start with $\tau = 0.01$, verify energy descent
- Use adaptive step size: decrease $\tau$ when energy increases
- Check CFL-like condition: $\tau < 1/L$ where $L$ is Lipschitz constant of $\nabla \mathcal{E}$

### Pitfall 4: Measure Degeneracy
**Problem**: Particles may collapse to a single point (delta measure)
**Solution**:
- Add entropy regularization to prevent collapse
- Use repulsive interaction terms in energy
- Monitor particle diversity via entropy or effective sample size

### Pitfall 5: Boundary Handling
**Problem**: Weights may leave valid domain (e.g., negative weights)
**Solution**:
- Use reflected Brownian motion at boundaries
- Add barrier terms to energy functional
- Project onto constraint set after each update

### Verification Checklist

1. **Energy descent**: Verify $\mathcal{E}(\mu_{n+1}) \leq \mathcal{E}(\mu_n)$ at each step
2. **Sequential stability**: Check semi-convexity condition numerically
3. **Convergence**: Verify $\mu_n$ stabilizes (measure distance $W_2(\mu_{n+1}, \mu_n) \to 0$)
4. **Consistency**: Compare with known analytical solutions (e.g., Gaussian case)
5. **Robustness**: Test with different initializations and noise levels
6. **Biological plausibility**: Verify weight distributions match experimental data

### Debugging Commands

```python
# Check energy descent
assert energy(mu_next) <= energy(mu_current) + 1e-6, "Energy increased!"

# Check sequential stability (numerical)
def check_semi_convexity(energy_fn, mu, nu, K=1.0):
    lhs = energy_fn(nu)
    rhs = energy_fn(mu) + Wasserstein_grad(energy_fn, mu) * W2(mu, nu) - 0.5 * K * W2(mu, nu)**2
    return lhs >= rhs - 1e-6

# Monitor convergence
convergence_metric = W2(mu_next, mu_current)
if convergence_metric < tolerance:
    print(f"Converged at step {n}: W2 = {convergence_metric}")
```

## 8. References and Further Reading

- **Primary**: Tan, "A Wasserstein Geometric Framework for Hebbian Plasticity" (arxiv:2604.16052)
- **JKO Scheme**: Jordan, Kinderlehrer, Otto (1998) — "The Variational Formulation of the Fokker-Planck Equation"
- **Wasserstein Geometry**: Ambrosio, Gigli, Savaré (2008) — "Gradient Flows in Metric Spaces"
- **Optimal Transport**: Villani (2009) — "Optimal Transport: Old and New"
- **Hebbian Learning**: Oja (1982) — "Simplified Neuron Model as a Principal Component Analyzer"
