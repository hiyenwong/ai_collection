---
name: robust-regret-control
description: Framework for distributionally robust regret optimization (DRRO) in stochastic control systems, combining robust control with regret minimization under uncertainty. Use when designing control systems with ambiguous disturbances, robust LQR, or optimizing control under unknown probability distributions.
---

# Robust Regret Control

## Overview

This skill provides a framework for distributionally robust regret optimization (DRRO) in stochastic control systems, combining robust control theory with regret minimization to handle uncertainty and ambiguity in system dynamics.

**Core Innovation**: First tractable multistage ex-ante distributionally robust regret optimization for stochastic control.

## Core Capabilities

### 1. Distributionally Robust Framework

**Concept**: Handle unknown probability distributions of disturbances.

**Key Elements**:
- Ambiguity sets for unknown distributions
- Gelbrich ball around nominal parameters
- Robust optimization across distribution uncertainty

**Framework**:
```python
class DRROController:
    def __init__(self, nominal_mean, nominal_cov, ambiguity_radius):
        self.nominal_mean = nominal_mean
        self.nominal_cov = nominal_cov
        self.ambiguity_radius = ambiguity_radius  # Gelbrich ball radius
    
    def worst_case_distribution(self):
        """Find worst-case distribution in ambiguity set."""
        # Distribution in Gelbrich ball around nominal
        return optimize_over_ambiguity_set(
            self.nominal_mean,
            self.nominal_cov,
            self.ambiguity_radius
        )
```

### 2. Regret Optimization

**Concept**: Minimize regret (performance difference) rather than absolute cost.

| Optimization | Objective | Advantage |
|--------------|-----------|-----------|
| **Cost Minimization** | Minimize absolute cost | Sensitive to distribution choice |
| **Regret Minimization** | Minimize vs. optimal policy | Robust to distribution ambiguity |

**Formula**:
```
Regret = Cost(policy) - Cost(optimal_policy_for_true_distribution)
```

**Why Regret?**:
- Comparing to optimal policy under true distribution
- Robust to distribution uncertainty
- More stable optimization landscape

### 3. Multistage Control

**Concept**: Finite-horizon control with stage-wise ambiguity.

**Structure**:
- Independent disturbances across time
- Common stage-law ambiguity (unknown but shared distribution)
- Multistage optimization framework

**Implementation**:
```python
def multistage_drro(system, horizon, ambiguity_set):
    """Solve multistage distributionally robust regret optimization."""
    
    # Initialize policy
    policy = []
    
    for stage in range(horizon):
        # Optimize for worst-case regret at this stage
        stage_policy = optimize_stage_regret(
            system,
            stage,
            ambiguity_set,
            previous_policy=policy
        )
        policy.append(stage_policy)
    
    return policy
```

## Workflow

### Step 1: Define Ambiguity Set

When designing robust control:

```python
# 1. Specify nominal distribution parameters
nominal_mean = estimate_mean(disturbances)
nominal_cov = estimate_covariance(disturbances)

# 2. Define ambiguity radius (Gelbrich ball)
ambiguity_radius = specify_uncertainty_level()

# 3. Construct ambiguity set
ambiguity_set = GelbrichBall(nominal_mean, nominal_cov, ambiguity_radius)
```

### Step 2: Formulate Regret Objective

Set up regret optimization:

```python
def formulate_drro(system, ambiguity_set):
    # 1. Define cost function
    cost_fn = define_stage_cost(system)
    
    # 2. Define optimal policy oracle
    optimal_policy = oracle_policy_for_distribution
    
    # 3. Formulate regret
    regret = cost(policy) - cost(optimal_policy(true_distribution))
    
    # 4. Robustify over ambiguity set
    robust_regret = max_{distribution in ambiguity_set} regret
    
    return minimize(robust_regret)
```

### Step 3: Solve Multistage Problem

Optimize across stages:

```python
# 1. Ex-ante optimization (before seeing disturbances)
ex_ante_policy = solve_ex_ante_drro(system, horizon, ambiguity_set)

# 2. Alternative: Ex-post optimization (after seeing disturbances)
ex_post_policy = solve_ex_post_drro(system, disturbances)

# 3. Choose based on application
policy = select_policy_type(application, ex_ante_policy, ex_post_policy)
```

## Applications

### Application 1: LQR Control with Ambiguity

**Use Case**: Linear Quadratic Regulator with unknown disturbance distribution.

**Setup**:
- Finite-horizon LQR
- Common stage-law ambiguity
- Gelbrich ball around nominal mean/covariance

**Solution**:
```python
class DRROLQR:
    def solve(self, A, B, Q, R, horizon, ambiguity):
        # State dynamics: x_{t+1} = A*x_t + B*u_t + w_t
        # w_t: disturbance with unknown distribution
        
        # Optimize policy minimizing worst-case regret
        return solve_multistage_drro(
            dynamics=(A, B),
            cost=(Q, R),
            horizon=horizon,
            ambiguity=ambiguity
        )
```

### Application 2: Stochastic Control Systems

**Use Case**: Control systems with probabilistic uncertainty.

**Benefits**:
- Handles distribution ambiguity
- Robust to estimation errors
- Regret-based performance guarantee

### Application 3: Robust Decision Making

**Use Case**: Decision making under uncertainty with unknown probabilities.

**Benefits**:
- No requirement for precise distribution knowledge
- Robust to worst-case scenarios
- Regret minimization vs. optimal

## Key Concepts

### Certainty-Equivalent vs. Regret-Optimal

| Policy Type | Approach | Robustness |
|-------------|----------|------------|
| **CE Controller** | Use nominal distribution | Not regret-optimal |
| **Regret-Optimal** | Minimize regret over ambiguity | Robust to distribution uncertainty |

**Key Insight**: CE controller is generally not regret-optimal in multistage setting.

### Gelbrich Ball Ambiguity

| Parameter | Role | Specification |
|-----------|------|----------------|
| **Nominal Mean** | Expected disturbance | Estimated from data |
| **Nominal Covariance** | Disturbance variance | Estimated from data |
| **Ambiguity Radius** | Uncertainty level | User-specified tolerance |

**Gelbrich Distance**: Measures deviation from nominal distribution.

### Ex-Ante vs. Ex-Post

| Optimization | Timing | Information |
|--------------|--------|-------------|
| **Ex-Ante** | Before disturbances | Distribution ambiguity only |
| **Ex-Post** | After disturbances | Observed disturbance values |

## Related Skills

- **robust-control**: General robust control theory
- **stochastic-control**: Stochastic optimal control
- **lqr-design**: Linear Quadratic Regulator design

## Resources

### references/

- `drro_theory.md`: Distributionally robust regret optimization theory
- `gelbrich_ball.md`: Gelbrich ball ambiguity sets

## Key Papers

1. **Distributionally Robust Regret Optimal LQR with Common Stage-Law Ambiguity** (arxiv:2604.06158v1)
   - Authors: Lukas-Benedikt Fiechtner, Jose Blanchet
   - Date: 2026-04-07
   - Key innovation: First tractable multistage DRRO formulation

2. **Related Works**: Robust control, regret minimization, distributionally robust optimization

## Usage Examples

### Example 1: Design Robust LQR

**Request**: "Design a robust LQR controller for unknown disturbances"

**Response**:
1. Estimate nominal disturbance distribution
2. Define Gelbrich ball ambiguity set
3. Formulate regret optimization problem
4. Solve multistage DRRO for optimal policy

### Example 2: Handle Distribution Ambiguity

**Request**: "Control system with ambiguous probability distribution"

**Response**:
1. Specify ambiguity radius for distribution uncertainty
2. Set up regret objective (vs. optimal policy)
3. Optimize over worst-case distribution in ambiguity set
4. Implement robust policy