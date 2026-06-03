---
name: two-timescale-learning-dynamics
description: "Two-time-scale population dynamics framework for neural network training. Models fast parameter updates (SGD) and slow hyperparameter evolution (selection-mutation) as interacting agent system. Use for population-based training, evolutionary strategies, model merging, and bilevel optimization. Keywords: two-time-scale, population dynamics, selection-mutation, hyperparameter evolution, interacting agent system."
---

# Two-Time-Scale Learning Dynamics

Theoretical framework for neural network training based on two-time-scale population dynamics, modeling population-based learning paradigms including evolutionary strategies, PBT, and model merging.

## Overview

Population-based learning combines:
- **Fast dynamics:** Within-model optimization (SGD/Langevin)
- **Slow dynamics:** Population-level adaptation (selection-mutation)

**Key Innovation:** Mathematical framework proving large-population limit and deriving reduced equations under time-scale separation.

## Mathematical Framework

### Interacting Agent System

**State Variables:**
- $\theta$: Network parameters (fast)
- $\alpha$: Hyperparameters (slow)

**Dynamics:**

$$
\begin{aligned}
d\theta_t &= -\nabla_\theta L(\theta_t; \alpha_t) dt + \sigma dW_t & \text{(fast)} \\
d\alpha_t &= \epsilon \cdot \text{(selection-mutation)}( \alpha_t) dt & \text{(slow)}
\end{aligned}
$$

Where $\epsilon \ll 1$ is the time-scale separation parameter.

### Large Population Limit

As population size $N \to \infty$:

**Joint Distribution:** $f(t, \theta, \alpha)$ evolves according to:

$$
\partial_t f = \nabla_\theta \cdot (f \nabla_\theta L) + \frac{\sigma^2}{2} \Delta_\theta f - \epsilon \mathcal{L}_{\alpha}^* f
$$

Where $\mathcal{L}_{\alpha}^*$ is the adjoint of the selection-mutation operator.

### Strong Time-Scale Separation Limit

When $\epsilon \to 0$:

**Reduced Equation for Hyperparameters:**

$$
\partial_t \rho(t, \alpha) = -\nabla_\alpha \cdot (\rho \cdot v(\alpha)) + \text{mutation terms}
$$

Where:
- $\rho(t, \alpha)$: Marginal distribution of hyperparameters
- $v(\alpha)$: Effective fitness (drift velocity)

### Effective Fitness

For fixed hyperparameter $\alpha$, fast dynamics relax to **Boltzmann-Gibbs measure**:

$$
f^*(\theta | \alpha) \propto \exp\left(-\frac{2}{\sigma^2} L(\theta; \alpha)\right)
$$

**Effective Fitness:**

$$
v(\alpha) = -\mathbb{E}_{\theta \sim f^*(\cdot | \alpha)}[\nabla_\alpha L(\theta; \alpha)]
$$

**Interpretation:** Average gradient of loss with respect to hyperparameters, averaged over equilibrium parameter distribution.

## Implementation

### 1. Population Dynamics Simulator

```python
import numpy as np
import torch
from dataclasses import dataclass

@dataclass
class PopulationConfig:
    """Configuration for two-time-scale population dynamics."""
    population_size: int = 100
    n_parameters: int = 1000
    n_hyperparameters: int = 10
    
    # Fast dynamics (SGD)
    learning_rate: float = 0.01
    noise_std: float = 0.001
    
    # Slow dynamics (selection-mutation)
    selection_strength: float = 0.1
    mutation_rate: float = 0.01
    time_scale_ratio: float = 0.01  # epsilon

class TwoTimeScalePopulation:
    """
    Two-time-scale population dynamics simulator.
    
    Fast: Parameter updates via noisy SGD
    Slow: Hyperparameter evolution via selection-mutation
    """
    
    def __init__(self, config: PopulationConfig, loss_fn):
        self.config = config
        self.loss_fn = loss_fn
        
        # Initialize population
        self.population = []
        for _ in range(config.population_size):
            agent = {
                'params': torch.randn(config.n_parameters),
                'hyperparams': torch.randn(config.n_hyperparameters),
                'fitness': 0.0
            }
            self.population.append(agent)
    
    def fast_step(self, agent, batch):
        """
        Fast dynamics: Noisy gradient step on parameters.
        
        Simulates: d theta = -grad L dt + sigma dW
        """
        params = agent['params']
        hyperparams = agent['hyperparams']
        
        # Compute gradient
        params.requires_grad = True
        loss = self.loss_fn(params, hyperparams, batch)
        loss.backward()
        
        # Noisy gradient update (Langevin dynamics)
        with torch.no_grad():
            noise = torch.randn_like(params) * self.config.noise_std
            params -= self.config.learning_rate * params.grad + noise
            params.grad.zero_()
        
        agent['fitness'] = -loss.item()  # Negative loss = fitness
        
        return agent
    
    def slow_step(self):
        """
        Slow dynamics: Selection-mutation on hyperparameters.
        
        Simulates: d alpha = epsilon * selection-mutation(alpha)
        """
        # Selection: Weighted by fitness
        fitnesses = torch.tensor([a['fitness'] for a in self.population])
        weights = torch.softmax(
            fitnesses / self.config.selection_strength, 
            dim=0
        )
        
        # Select parents
        selected_indices = torch.multinomial(
            weights, 
            self.config.population_size, 
            replacement=True
        )
        
        # Create new population
        new_population = []
        for idx in selected_indices:
            parent = self.population[idx]
            
            # Mutation
            mutation = torch.randn_like(parent['hyperparams']) * self.config.mutation_rate
            new_hyperparams = parent['hyperparams'] + mutation
            
            # New agent (inherited params + mutated hyperparams)
            new_agent = {
                'params': parent['params'].clone(),
                'hyperparams': new_hyperparams,
                'fitness': 0.0
            }
            new_population.append(new_agent)
        
        self.population = new_population
    
    def step(self, batch):
        """One combined step (fast + slow)."""
        # Fast: Update all agents' parameters
        for agent in self.population:
            self.fast_step(agent, batch)
        
        # Slow: Evolutionary step (only every 1/epsilon steps)
        if np.random.random() < self.config.time_scale_ratio:
            self.slow_step()
    
    def get_mean_hyperparameters(self):
        """Get population mean of hyperparameters."""
        hypers = torch.stack([a['hyperparams'] for a in self.population])
        return hypers.mean(dim=0)
    
    def get_best_agent(self):
        """Get agent with highest fitness."""
        best_idx = max(range(len(self.population)), 
                       key=lambda i: self.population[i]['fitness'])
        return self.population[best_idx]
```

### 2. Effective Fitness Estimation

```python
class EffectiveFitnessEstimator:
    """
    Estimate effective fitness v(alpha) for hyperparameters.
    
    v(alpha) = -E_theta~f*(.|alpha)[grad_alpha L(theta, alpha)]
    """
    
    def __init__(self, loss_fn, n_samples=100):
        self.loss_fn = loss_fn
        self.n_samples = n_samples
    
    def estimate(self, hyperparams, parameter_dim):
        """
        Estimate effective fitness at given hyperparameters.
        
        Simulates fast dynamics to equilibrium, then averages
        hyperparameter gradients.
        """
        # Sample from equilibrium distribution (approximate)
        # Run Langevin dynamics to burn-in
        params = torch.randn(parameter_dim, requires_grad=True)
        
        # Burn-in phase
        for _ in range(self.n_samples):
            loss = self.loss_fn(params, hyperparams)
            loss.backward()
            
            with torch.no_grad():
                params -= 0.01 * params.grad + 0.001 * torch.randn_like(params)
                params.grad.zero_()
        
        # Collect samples and estimate gradient
        grad_sum = torch.zeros_like(hyperparams)
        
        for _ in range(self.n_samples):
            # Sample with Langevin
            loss = self.loss_fn(params, hyperparams)
            loss.backward()
            
            with torch.no_grad():
                params -= 0.01 * params.grad + 0.001 * torch.randn_like(params)
                params.grad.zero_()
            
            # Compute hyperparameter gradient
            hyperparams_grad = torch.autograd.grad(
                loss, hyperparams, retain_graph=True
            )[0]
            grad_sum += hyperparams_grad
        
        # Effective fitness (negative expected gradient)
        effective_fitness = -grad_sum / self.n_samples
        
        return effective_fitness
```

### 3. Connection to Bilevel Optimization

```python
class BilevelOptimizer:
    """
    Bilevel optimization using two-time-scale framework.
    
    Upper level: min_alpha L_val(theta*(alpha), alpha)
    Lower level: theta*(alpha) = argmin_theta L_train(theta, alpha)
    """
    
    def __init__(self, train_loss, val_loss):
        self.train_loss = train_loss
        self.val_loss = val_loss
    
    def optimize(self, init_params, init_hyperparams, n_iterations):
        """
        Two-time-scale bilevel optimization.
        
        Fast (lower level): Converge to theta*(alpha)
        Slow (upper level): Update alpha using validation loss
        """
        params = init_params.clone().requires_grad_(True)
        hyperparams = init_hyperparams.clone().requires_grad_(True)
        
        for t in range(n_iterations):
            # === FAST: Lower level optimization ===
            # Converge to optimal params for current hyperparams
            for _ in range(100):  # Inner loop (fast)
                loss_train = self.train_loss(params, hyperparams)
                
                params_grad = torch.autograd.grad(loss_train, params)[0]
                with torch.no_grad():
                    params -= 0.01 * params_grad
            
            # === SLOW: Upper level optimization ===
            if t % 10 == 0:  # Outer loop (slow)
                loss_val = self.val_loss(params.detach(), hyperparams)
                
                hyperparams_grad = torch.autograd.grad(loss_val, hyperparams)[0]
                with torch.no_grad():
                    hyperparams -= 0.001 * hyperparams_grad
                
                print(f"Step {t}: Val Loss = {loss_val.item():.4f}")
        
        return params, hyperparams
```

## Applications

### 1. Population-Based Training (PBT)

```python
def pbt_with_two_timescale(models, hyperparam_space, train_fn, eval_fn):
    """
    Population-Based Training using two-time-scale dynamics.
    
    Fast: Individual model training
    Slow: Hyperparameter evolution via exploit-and-explore
    """
    population = [
        {'model': m, 'hyperparams': h, 'performance': 0}
        for m, h in zip(models, hyperparam_space)
    ]
    
    for epoch in range(100):
        # Fast: Train each model
        for agent in population:
            agent['model'] = train_fn(
                agent['model'], 
                agent['hyperparams'], 
                n_steps=100
            )
            agent['performance'] = eval_fn(agent['model'])
        
        # Slow: Exploit-and-explore
        if epoch % 10 == 0:
            # Sort by performance
            population.sort(key=lambda x: x['performance'], reverse=True)
            
            # Exploit: Copy weights from better models
            for i in range(len(population) // 2, len(population)):
                source = population[i - len(population) // 2]
                population[i]['model'].load_state_dict(
                    source['model'].state_dict()
                )
            
            # Explore: Perturb hyperparameters
            for agent in population[len(population)//2:]:
                agent['hyperparams'] = perturb_hyperparams(
                    agent['hyperparams']
                )
    
    return population[0]
```

### 2. Model Merging

```python
def model_merging_two_timescale(models, merging_coefficients):
    """
    Model merging as slow dynamics over merging coefficients.
    
    Fast: Evaluate merged model performance
    Slow: Evolve merging coefficients
    """
    # Start with equal weighting
    coeffs = torch.ones(len(models)) / len(models)
    
    for iteration in range(1000):
        # Fast: Create merged model
        merged = merge_models(models, coeffs)
        
        # Evaluate
        performance = evaluate(merged)
        
        # Slow: Update coefficients based on gradient
        if iteration % 100 == 0:
            # Estimate gradient w.r.t. coefficients
            grad = estimate_coefficient_gradient(models, coeffs)
            
            with torch.no_grad():
                coeffs -= 0.01 * grad
                coeffs = torch.softmax(coeffs, dim=0)  # Normalize
    
    return merge_models(models, coeffs)
```

## Key Theoretical Results

1. **Large Population Limit:** As $N \to \infty$, population converges to deterministic mean-field

2. **Time-Scale Separation:** When $\epsilon \to 0$, hyperparameters follow selection-mutation with effective fitness

3. **Noise-Diversity Trade-off:** 
   - Higher noise ($\sigma$) → more exploration → better population diversity
   - Lower noise → faster convergence → better individual optimization

4. **Connection to Replicator Dynamics:** Reduced equation connects to classical evolutionary game theory

## Numerical Insights

From paper experiments:
- **Effective fitness estimation** improves population-level updates
- **Two-time-scale regime** shows different behavior than synchronous updates
- **Optimal noise level** balances exploration and exploitation

## Activation Keywords

- two-time-scale
- population dynamics
- selection-mutation
- hyperparameter evolution
- interacting agent system
- effective fitness
- replicator dynamics
- bilevel optimization

## Tools Used

- PyTorch for differentiable simulation
- NumPy for numerical analysis
- Matplotlib for visualization

## References

Borghi, G., Im, H., & Pareschi, L. (2026). Two-Time-Scale Learning Dynamics: A Population View of Neural Network Training. arXiv:2603.19808.

## Related Skills

- population-based-training
- evolutionary-strategies
- model-merging
- bilevel-optimization
- hyperparameter-optimization