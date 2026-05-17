---
name: physics-guided-generative-optimization
description: Generate-and-evaluate loop for quantum circuit optimization combining conditional diffusion models, physics-informed neural networks, and graph neural networks. Use when optimizing Trotter-Suzuki decompositions, designing quantum circuits with generative models, or applying physics-guided neural optimization to NISQ compilation. Triggered by: generative quantum optimization, Trotter Suzuki decomposition, PINN feedback quantum, diffusion model circuit, NISQ compilation.
---

# Physics-Guided Generative Optimization

## Description
Generate-and-evaluate framework for quantum circuit optimization using:
1. Conditional diffusion model for strategy proposal
2. Physics-informed neural network (PINN) for fidelity feedback
3. Graph neural network for commutator structure encoding

## Activation Keywords
- generative quantum optimization
- Trotter Suzuki decomposition
- PINN feedback quantum
- diffusion model circuit
- NISQ compilation
- physics-guided optimization

## Architecture

### Components
1. **Generator**: Conditional diffusion model proposes term grouping, product formula order, timestep allocation
2. **Evaluator**: PINN supplies differentiable fidelity feedback
3. **Encoder**: GNN encodes Hamiltonian commutator structure
4. **Trainer**: REINFORCE + Pareto tracker for hybrid discrete-continuous space

### Training Loop
```
for step in training:
    # 1. Generate strategy
    strategy = diffusion_model.sample(condition=hamiltonian)
    
    # 2. Evaluate fidelity
    fidelity = pinn.evaluate(strategy)
    
    # 3. Compute reward
    reward = fidelity - lambda * circuit_depth
    
    # 4. Update via REINFORCE
    diffusion_model.update(reward)
    
    # 5. Track Pareto frontier
    pareto_tracker.update(fidelity, depth)
```

## Key Results
- TFIM benchmark: 85.6% fidelity at 21.8% circuit depth vs 4th order Qiskit
- Equal depth: 0.9994 fidelity after fine-tuning
- 19.2% CNOT count vs baseline

## Configuration Guidance
- CFG (Classifier-Free Guidance) must be tuned jointly with compute budget
- Module contributions depend on training recipe and guidance hyperparameters
- Discrete grouping and order require REINFORCE (not gradient descent)

## Error Handling
- Monitor training stability across hybrid spaces
- Validate commutator structure encoding accuracy
- Track Pareto frontier for fidelity-cost tradeoff

## References
- Paper: arXiv:2605.13268 (WenBin Yan, 2026-05-13)
- Applicable to: TFIM, Heisenberg, Hubbard models
