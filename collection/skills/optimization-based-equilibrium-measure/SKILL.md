---
name: optimization-based-equilibrium-measure
description: 'Analyze non-equilibrium steady state dynamics using optimization-based equilibrium measure. Apply to edge-of-chaos theory in neural networks with replica method for order parameters.'
---

# Optimization-Based Equilibrium Measure for Non-Equilibrium Steady States

## Description

A theoretical framework treating steady state search as an optimization problem. Constructs approximate potential related to dynamics speed, enabling analytical study of non-equilibrium steady states in neural networks. Applies replica method to derive order parameters characterizing the edge-of-chaos transition.

**Source:** arXiv:2401.10009v2
**Journal:** Commun. Theor. Phys. 77 035601 (2025)
**Utility:** 0.91

## Activation Keywords

- edge of chaos
- non-equilibrium steady state
- equilibrium measure
- replica method neural networks
- order parameters dynamics
- Langevin dynamics
- Fokker-Planck steady state
- chaotic transition
- neural dynamics analysis

## Core Concepts

### 1. Non-Equilibrium Steady States

**Challenge:**
- Neural dynamics is non-linear, stochastic, non-gradient
- Driving force cannot be written as gradient of potential
- Fokker-Planck steady state solution generally unknown
- Path integral approach computationally expensive

**Solution:**
- Treat steady state search as optimization problem
- Construct approximate potential related to dynamics speed
- Search for ground state = run approximate stochastic gradient dynamics
- Only in zero temperature limit achieve original steady state distribution

### 2. Optimization-Based Equilibrium Measure

**Key Insight:**
```
Original dynamics: dx/dt = f(x) + noise
Optimization: Find min V(x) where V ~ dynamics speed
Ground state → Canonical Boltzmann measure
```

**Framework:**
| Aspect | Traditional | Optimization-Based |
|--------|-------------|-------------------|
| Steady state | Solve Fokker-Planck | Minimize potential |
| Distribution | Unknown | Boltzmann measure |
| Computational cost | High (integro-differential) | Lower (optimization) |
| Closed form | Generally no | Yes for ground state |

### 3. Replica Method for Quenched Disorder

**Application:**
- Neural networks have quenched disorder (random weights, connectivity)
- Replica method averages out disorder
- Naturally leads to order parameters for non-equilibrium steady states

**Order Parameters:**
- Fluctuations of steady states
- Responses of steady states
- Characterize continuous transition

### 4. Edge-of-Chaos Theory

**Reproduced Results:**
- Theory reproduces well-known edge-of-chaos result
- Order parameters characterize the continuous transition
- Fluctuations and responses explained

**Edge of Chaos:**
```
Ordered regime  ← → Edge of chaos ← → Chaotic regime
   (stable)        (optimal)          (unstable)
```

## Step-by-Step Instructions

### 1. Potential Construction

```python
import numpy as np

class EquilibriumMeasurePotential:
    """
    Construct approximate potential for dynamics.
    
    Args:
        dynamics_func: Function f(x) for dx/dt = f(x) + noise
        noise_strength: Noise amplitude
        temperature: Temperature parameter (→ 0 for true steady state)
    """
    def __init__(self, dynamics_func, noise_strength, temperature):
        self.f = dynamics_func
        self.noise = noise_strength
        self.T = temperature
        
    def potential(self, x):
        """
        Construct potential V(x) ~ dynamics speed.
        
        Args:
            x: State vector
        
        Returns:
            V: Potential value
        """
        # Dynamics speed squared
        speed_squared = np.sum(self.f(x)**2)
        
        # Add noise contribution
        noise_term = self.noise**2 * np.sum(x**2) / 2
        
        # Potential
        V = speed_squared / 2 + noise_term
        
        return V
    
    def gradient(self, x):
        """
        Gradient of potential.
        
        Args:
            x: State vector
        
        Returns:
            grad_V: Gradient
        """
        # Gradient of speed squared
        df_dx = self.jacobian(self.f, x)
        grad_speed = np.dot(df_dx.T, self.f(x))
        
        # Gradient of noise term
        grad_noise = self.noise**2 * x
        
        # Combined gradient
        grad_V = grad_speed + grad_noise
        
        return grad_V
    
    def jacobian(self, func, x, eps=1e-5):
        """
        Compute Jacobian numerically.
        
        Args:
            func: Function to differentiate
            x: Point
            eps: Small perturbation
        
        Returns:
            J: Jacobian matrix
        """
        n = len(x)
        J = np.zeros((n, n))
        
        for i in range(n):
            x_plus = x.copy()
            x_minus = x.copy()
            x_plus[i] += eps
            x_minus[i] -= eps
            
            J[:, i] = (func(x_plus) - func(x_minus)) / (2 * eps)
        
        return J
```

### 2. Stochastic Gradient Dynamics

```python
class StochasticGradientDynamics:
    """
    Run approximate stochastic gradient dynamics.
    
    Args:
        potential: EquilibriumMeasurePotential
        learning_rate: Step size
        noise_level: Stochastic noise
    """
    def __init__(self, potential, learning_rate, noise_level):
        self.V = potential
        self.lr = learning_rate
        self.noise = noise_level
        
    def step(self, x):
        """
        Single step of stochastic gradient dynamics.
        
        Args:
            x: Current state
        
        Returns:
            x_new: New state
        """
        # Gradient descent
        grad = self.V.gradient(x)
        
        # Stochastic noise
        stochastic_noise = np.random.randn(len(x)) * self.noise
        
        # Update
        x_new = x - self.lr * grad + stochastic_noise
        
        return x_new
    
    def simulate(self, x0, n_steps, record_interval=100):
        """
        Simulate dynamics for multiple steps.
        
        Args:
            x0: Initial state
            n_steps: Number of steps
            record_interval: Recording interval
        
        Returns:
            trajectory: Recorded states
        """
        trajectory = []
        x = x0.copy()
        
        for step in range(n_steps):
            x = self.step(x)
            
            if step % record_interval == 0:
                trajectory.append(x.copy())
        
        return np.array(trajectory)
```

### 3. Replica Method Implementation

```python
class ReplicaMethod:
    """
    Replica method for averaging quenched disorder.
    
    Args:
        n_replicas: Number of replicas
        disorder_func: Function generating quenched disorder
    """
    def __init__(self, n_replicas, disorder_func):
        self.n_replicas = n_replicas
        self.disorder_func = disorder_func
        
    def average_over_disorder(self, state_func, n_samples=100):
        """
        Average state function over quenched disorder.
        
        Args:
            state_func: Function computing state quantity
            n_samples: Number of disorder samples
        
        Returns:
            averaged: Averaged quantity
            fluctuations: Fluctuations (order parameter)
        """
        results = []
        
        for sample in range(n_samples):
            # Generate quenched disorder
            disorder = self.disorder_func()
            
            # Compute state quantity
            result = state_func(disorder)
            results.append(result)
        
        # Average
        averaged = np.mean(results)
        
        # Fluctuations (order parameter)
        fluctuations = np.std(results)
        
        return averaged, fluctuations
    
    def replica_symmetric_solution(self, potential, x0):
        """
        Replica symmetric (RS) solution.
        
        Args:
            potential: Potential function
            x0: Initial state
        
        Returns:
            order_params: Order parameters (fluctuations, responses)
        """
        # Run dynamics for each replica
        replicas = []
        
        for r in range(self.n_replicas):
            dynamics = StochasticGradientDynamics(
                potential, learning_rate=0.01, noise_level=0.1
            )
            trajectory = dynamics.simulate(x0, n_steps=1000)
            replicas.append(trajectory[-1])  # Final state
        
        replicas = np.array(replicas)
        
        # Order parameters
        # Fluctuation: variance across replicas
        fluctuations = np.var(replicas)
        
        # Response: correlation with perturbation
        perturbed = replicas + np.random.randn(len(replicas), len(x0)) * 0.01
        responses = np.mean(replicas * perturbed) - np.mean(replicas)**2
        
        order_params = {
            'fluctuations': fluctuations,
            'responses': responses
        }
        
        return order_params
```

### 4. Edge-of-Chaos Detection

```python
class EdgeOfChaosDetector:
    """
    Detect edge-of-chaos transition using order parameters.
    
    Args:
        dynamics_func: Neural dynamics function
        noise_range: Range of noise strengths to test
    """
    def __init__(self, dynamics_func, noise_range):
        self.f = dynamics_func
        self.noise_range = noise_range
        
    def compute_order_parameters(self, noise_strength):
        """
        Compute order parameters for given noise.
        
        Args:
            noise_strength: Noise amplitude
        
        Returns:
            order_params: Order parameters
        """
        potential = EquilibriumMeasurePotential(
            self.f, noise_strength, temperature=noise_strength
        )
        
        replica_method = ReplicaMethod(
            n_replicas=10,
            disorder_func=lambda: np.random.randn(100, 100)  # Random weights
        )
        
        x0 = np.random.randn(100)
        
        order_params = replica_method.replica_symmetric_solution(
            potential, x0
        )
        
        return order_params
    
    def scan_transition(self):
        """
        Scan noise range to detect transition.
        
        Returns:
            transition_point: Noise strength at transition
            order_params_history: History of order parameters
        """
        history = []
        
        for noise in self.noise_range:
            order_params = self.compute_order_parameters(noise)
            history.append({
                'noise': noise,
                'fluctuations': order_params['fluctuations'],
                'responses': order_params['responses']
            })
        
        # Find transition point (maximum fluctuations)
        fluctuations = [h['fluctuations'] for h in history]
        transition_idx = np.argmax(fluctuations)
        transition_point = self.noise_range[transition_idx]
        
        return transition_point, history
    
    def classify_regime(self, noise_strength, transition_point):
        """
        Classify regime based on noise strength.
        
        Args:
            noise_strength: Current noise
            transition_point: Edge-of-chaos point
        
        Returns:
            regime: 'ordered', 'edge-of-chaos', or 'chaotic'
        """
        margin = 0.1 * transition_point
        
        if noise_strength < transition_point - margin:
            return 'ordered'
        elif noise_strength > transition_point + margin:
            return 'chaotic'
        else:
            return 'edge-of-chaos'
```

### 5. Analysis and Visualization

```python
import matplotlib.pyplot as plt

def analyze_edge_of_chaos(history):
    """
    Analyze edge-of-chaos transition.
    
    Args:
        history: Order parameters history
    
    Returns:
        analysis: Analysis summary
    """
    noises = [h['noise'] for h in history]
    fluctuations = [h['fluctuations'] for h in history]
    responses = [h['responses'] for h in history]
    
    # Find peak
    peak_idx = np.argmax(fluctuations)
    peak_noise = noises[peak_idx]
    peak_fluctuation = fluctuations[peak_idx]
    
    analysis = {
        'transition_point': peak_noise,
        'peak_fluctuation': peak_fluctuation,
        'ordered_regime': noises[0:peak_idx],
        'chaotic_regime': noises[peak_idx:]
    }
    
    # Plot
    plt.figure(figsize=(12, 5))
    
    # Fluctuations
    plt.subplot(1, 2, 1)
    plt.plot(noises, fluctuations, 'b-', linewidth=2)
    plt.axvline(peak_noise, color='r', linestyle='--', label='Edge of chaos')
    plt.xlabel('Noise Strength')
    plt.ylabel('Fluctuations')
    plt.title('Fluctuations vs Noise')
    plt.legend()
    plt.grid(True)
    
    # Responses
    plt.subplot(1, 2, 2)
    plt.plot(noises, responses, 'g-', linewidth=2)
    plt.axvline(peak_noise, color='r', linestyle='--', label='Edge of chaos')
    plt.xlabel('Noise Strength')
    plt.ylabel('Responses')
    plt.title('Responses vs Noise')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('edge_of_chaos_transition.png')
    
    return analysis
```

## Tools Used

- `numpy` - Numerical computations
- `scipy` - Optimization and integration
- `matplotlib` - Visualization
- `exec` - Run simulations
- `read` - Load model parameters

## Example Use Cases

### 1. Basic Edge-of-Chaos Detection

```python
# Define neural dynamics
def neural_dynamics(x, weights):
    """
    Simple neural dynamics: dx/dt = -x + weights @ x
    """
    return -x + np.dot(weights, x)

# Create detector
detector = EdgeOfChaosDetector(
    dynamics_func=lambda x: neural_dynamics(x, np.random.randn(100, 100)),
    noise_range=np.linspace(0.01, 2.0, 20)
)

# Scan transition
transition_point, history = detector.scan_transition()

print(f"Edge-of-chaos at noise = {transition_point:.3f}")
```

### 2. Order Parameter Analysis

```python
# Analyze
analysis = analyze_edge_of_chaos(history)

print(f"Transition point: {analysis['transition_point']}")
print(f"Peak fluctuation: {analysis['peak_fluctuation']}")

# Classify current regime
regime = detector.classify_regime(1.0, transition_point)
print(f"Current regime: {regime}")
```

### 3. Replica Symmetric Solution

```python
# Compute order parameters for specific noise
order_params = detector.compute_order_parameters(1.0)

print(f"Fluctuations: {order_params['fluctuations']:.4f}")
print(f"Responses: {order_params['responses']:.4f}")
```

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Potential Construction

## Examples

### Example 1: Basic Application

**User:** I need to apply Optimization-Based Equilibrium Measure for Non-Equilibrium Steady States to my analysis.

**Agent:** I'll help you apply optimization-based-equilibrium-measure. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for optimization-based-equilibrium-measure?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `griffiths-phase-brain-criticality` - Criticality in brain networks
- `chaos-freezing-without-plasticity` - Chaos dynamics
- `neutral-theory-neural-dynamics` - Neutral theory dynamics

## References

- Huang, H. (2025). "An optimization-based equilibrium measure describes non-equilibrium steady state dynamics: application to edge of chaos" Commun. Theor. Phys. 77 035601
- arXiv:2401.10009v2 [q-bio.NC]

---

**Created:** 2026-03-29 21:05
**Author:** Aerial (from arXiv:2401.10009v2)