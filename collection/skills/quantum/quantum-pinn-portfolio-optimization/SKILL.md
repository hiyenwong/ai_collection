---
name: quantum-pinn-portfolio-optimization
description: "Quantum Physics-Informed Neural Networks (QPINN) methodology for solving portfolio optimization PDEs. Uses quantum circuits to encode Hamilton-Jacobi-Bellman (HJB) equation solutions for continuous-time portfolio selection. Use when: solving continuous-time portfolio optimization with neural PDE methods, applying quantum-enhanced PINNs to finance, high-dimensional PDE solution for stochastic control problems, or bridging quantum computing with quantitative finance theory. Activation: quantum PINN portfolio, QPINN finance, quantum PDE portfolio optimization, HJB quantum neural network, quantum stochastic control PDE."
---

# Quantum PINN for Portfolio Optimization

Solve high-dimensional portfolio optimization PDEs using Quantum Physics-Informed Neural Networks (QPINN), combining quantum circuits with PINN methodology for continuous-time stochastic control problems.

## Core Problem

Portfolio optimization in continuous time leads to Hamilton-Jacobi-Bellman (HJB) equations — nonlinear PDEs that become intractable in high dimensions. Classical PINNs solve these but face the curse of dimensionality.

## QPINN Architecture

### Quantum Feature Map
- Encode market state variables (asset prices, volatilities, time) into quantum state
- Use parameterized quantum circuits as ansatz for the value function
- Quantum entanglement captures cross-asset correlations naturally

### PDE Constraints in Loss Function
- Encode HJB equation residual as quantum observable expectation
- Include boundary conditions (terminal wealth, constraints)
- Add regularization for physical constraints (no-arbitrage, positivity)

### Training Objective
```
Loss = L_PDE_residual + L_boundary + L_initial + L_regularization
```
- PDE residual computed via quantum circuit differentiation (parameter-shift rule)
- Boundary conditions enforced through penalty terms
- Terminal condition: value function matches utility at maturity

## Application Domains

### Merton's Portfolio Problem
- Classic continuous-time allocation between risky and risk-free assets
- QPINN recovers analytical solution while demonstrating methodology
- Extends to multi-asset settings where analytical solutions don't exist

### Transaction Costs
- Incorporate proportional or fixed transaction costs
- Leads to free-boundary PDEs (no-trade region identification)
- QPINN handles free boundaries through soft constraints

### Jump-Diffusion Markets
- Markets with Poisson jump components
- Integro-differential PDEs (more complex than pure diffusion)
- Quantum circuits naturally encode jump processes through unitary evolution

## Advantages

- **Dimensionality scaling**: Quantum feature maps scale logarithmically with state dimension
- **Expressivity**: Quantum circuits provide rich function approximation
- **Physical priors**: Quantum mechanics naturally encodes probabilistic constraints
- **NISQ-compatible**: Shallow circuits sufficient for PDE residual evaluation

## Implementation Checklist

- [ ] Formulate portfolio problem as HJB PDE
- [ ] Design quantum feature map for state variables
- [ ] Construct parameterized quantum circuit ansatz
- [ ] Implement PDE residual via parameter-shift differentiation
- [ ] Train on collocation points in state-time domain
- [ ] Validate against known analytical solutions (Merton problem)
- [ ] Extend to multi-asset or transaction cost settings

## Resources

- arXiv: 2604.03346 — "Learning PDEs for Portfolio Optimization with Quantum Physics-Informed Neural Networks"
