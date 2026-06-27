---
name: free-energy-rl-investment
description: "Free Energy-Entropy Duality methodology for risk-sensitive reinforcement learning in continuous-time investment management. Reformulates benchmarked asset allocation as a linear-quadratic-Gaussian stochastic differential game under an equivalent probability measure."
---

# Free Energy-RL Investment

## Description
Free Energy-Entropy Duality approach to risk-sensitive reinforcement learning for continuous-time investment management. Reformulates benchmarked asset allocation — where the state is uncontrolled but terminal reward contains a controlled Itô integral — as a linear-quadratic-Gaussian (LQG) stochastic differential game under an equivalent probability measure, enabling RL-based policy optimization.

Based on arXiv:2606.20903 "Reinforcement Learning for Risk-Sensitive Investment Management: a Free Energy--Entropy Duality Approach" (Lleo & Runggaldier, 2026).

## Activation Keywords
- free energy entropy duality investment
- risk-sensitive RL portfolio
- 自由能熵对偶投资
- benchmarked asset allocation RL
- LQG stochastic differential game investment
- continuous-time risk-sensitive RL
- 风险敏感强化学习投资

## Core Concepts

### Free Energy-Entropy Duality
The key insight: risk-sensitive optimization with exponential utility can be reformulated using the variational representation:
- log E[exp(θ·reward)] = sup_Q [θ·E_Q[reward] - D_KL(Q||P)]
- This converts a risk-sensitive problem into a zero-sum game between the investor (maximizing expected return) and an adversarial "nature" (minimizing via KL divergence)
- The KL divergence term acts as a risk penalty proportional to the investor's risk aversion

### Benched Asset Allocation Problem
The benchmarked problem does NOT fit standard Markovian stochastic control because:
- State process is uncontrolled (benchmark evolves exogenously)
- Terminal reward contains a controlled Itô integral (not just terminal state)
- Standard HJB approach fails due to non-Markovian structure

### LQG Reformulation
Under the equivalent probability measure via Girsanov transformation:
- The problem becomes a linear-quadratic-Gaussian stochastic differential game
- Linear state dynamics, quadratic cost, Gaussian noise
- This enables closed-form solutions or tractable RL approximations

## Usage Patterns

### Pattern 1: Risk-Sensitive Portfolio Optimization
Apply when:
- Portfolio must outperform a benchmark (relative performance)
- Investor has specific risk aversion (not just mean-variance)
- Continuous-time setting with partial model knowledge
- Need RL because model parameters are partially unknown

### Pattern 2: Free Energy Regularization in RL
Use free energy-entropy duality as a regularization mechanism:
- Replace standard expected return objective with free energy objective
- The entropy term (KL divergence) naturally regularizes the policy
- Trade-off parameter θ controls risk sensitivity
- θ → 0 recovers risk-neutral (standard) RL
- θ > 0 for risk-seeking, θ < 0 for risk-averse

### Pattern 3: Stochastic Differential Game Formulation
For benchmarked problems that don't fit standard control templates:
1. Identify the non-Markovian elements (uncontrolled state, controlled Itô integral)
2. Apply Girsanov transformation to change probability measure
3. Reformulate as zero-sum game: investor vs. adversarial nature
4. Solve via LQG theory or approximate with RL

## Mathematical Framework

### Free Energy Variational Formula
```
sup_π (1/θ) log E^π[exp(θ·J(π))] = sup_π sup_Q E^Q[J(π)] - (1/θ) D_KL(Q||P^π)
```

Where:
- J(π) is the benchmarked performance criterion
- θ is the risk-sensitivity parameter
- Q is an alternative probability measure
- D_KL is the KL divergence (acts as risk penalty)

### LQG Stochastic Differential Game
Under the equivalent measure:
- State dynamics: dX_t = (A·X_t + B·u_t)dt + Σ·dW_t^Q
- Cost functional: J = E^Q[∫(X'QX + u'Ru)dt + X_T'FX_T]
- Solution via Riccati equation or RL approximation

## Instructions for Agents

### Step 1: Problem Classification
Determine if the investment problem fits the benchmarked setting:
- Is there an exogenous benchmark process?
- Does the reward involve a controlled stochastic integral?
- Is the risk sensitivity non-trivial (not just mean-variance)?

### Step 2: Free Energy Reformulation
- Apply the variational representation of the exponential utility
- Identify the dual variables (alternative measure Q)
- Express the KL divergence penalty in terms of the control

### Step 3: LQG Game Solution
- If model is fully known: solve Riccati equation analytically
- If model is partially unknown: use RL to approximate the saddle point
- Policy gradient methods work well for the game formulation

### Step 4: RL Implementation
- Use actor-critic methods (the game has both max and min players)
- The "nature" player can be parameterized as a disturbance policy
- Train both policies simultaneously (minimax optimization)

## Error Handling
### Non-Markovian State
If the benchmarked problem doesn't admit Markovian reduction:
- Use the free energy duality to eliminate the non-Markovian element
- The Girsanov transformation absorbs the benchmark into the drift

### Risk Parameter Selection
- θ = 0: recovers standard (risk-neutral) RL — use as baseline
- θ < 0: risk-averse — appropriate for conservative portfolios
- θ > 0: risk-seeking — only for specific mandates

## Related Skills
- `qrl-dynamic-portfolio` - Quantum RL for portfolio optimization
- `quantum-portfolio-optimizer` - QAOA-based portfolio optimization
- `heuristic-portfolio-optimization` - Heuristic portfolio optimization (economics/)
- `quantum-rl-scuc-qsample` - Quantum-sampled features in RL
