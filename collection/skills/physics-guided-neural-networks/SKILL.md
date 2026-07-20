---
name: physics-guided-neural-networks
description: "Physics-guided neural network design and training methods. Embed physical laws, constraints, and symmetries into neural network architecture for improved modeling of physical systems (quantum mechanics, statistical physics, fluid dynamics, materials science). Activation: physics guided neural network, 物理学指导神经网络, physics-informed neural network, PINN, physics-constrained learning, quantum neural network, physics-aware training."
---

# Physics-Guided Neural Networks

Combine physics knowledge with deep learning for more accurate, efficient, and physically consistent models.

## Core Principles

### 1. Physics as Architecture Constraints

Embed physical laws directly into network design:
- **Symmetry preservation**: Network outputs respect physical symmetries
- **Conservation laws**: Energy, momentum, mass automatically conserved
- **Boundary conditions**: Hard constraints enforced by architecture

Example: Equivariant networks that preserve rotational symmetry in molecular dynamics.

### 2. Physics as Loss Functions

Add physical constraints to training objectives:
- **Physics-informed loss**: Penalize violations of physical laws
- **Energy conservation**: Minimize deviation from energy conservation
- **Equation residuals**: Minimize PDE/ODE residuals in predictions

```python
loss = data_loss + physics_loss_weight * physics_residual
```

### 3. Physics-Encoded Outputs

Force outputs to satisfy physical properties:
- **Unit constraints**: Output units match physical units
- **Positive-definite**: Quantities like density are always positive
- **Probability distributions**: Quantum states normalized and positive

## Workflow

### Step 1: Identify Physical Laws

What physics governs your system?
- Conservation laws (energy, momentum)
- Symmetries (rotation, translation, gauge)
- Constitutive relations (stress-strain, etc.)
- Boundary and initial conditions

### Step 2: Choose Embedding Strategy

| Strategy | When to Use | Example |
|----------|-------------|---------|
| Architecture constraint | Hard physical laws | Equivariant layers |
| Loss function penalty | Soft constraints, approximate physics | PDE residuals |
| Output encoding | Physical properties must be satisfied | Positive density |

### Step 3: Implement Physics Constraints

**Architecture-based** (most reliable):
```python
# Example: Rotation-equivariant layer
class E3Layer(nn.Module):
    # Automatically respects 3D rotation symmetry
    ...
```

**Loss-based** (flexible):
```python
# Example: PDE residual loss
def physics_loss(prediction, x, t):
    # Compute PDE residual: ∂u/∂t - α∇²u
    residual = compute_pde_residual(prediction, x, t)
    return torch.mean(residual**2)

total_loss = mse_loss + physics_weight * physics_loss
```

**Output-encoded** (guaranteed):
```python
# Example: Positive density via exponential
density = torch.exp(raw_output)  # Always positive
```

## Application Domains

### Quantum Mechanics

- **Neural-network quantum states**: Represent quantum wavefunctions
- **Quantum entanglement**: Learn entanglement patterns
- **Hamiltonian learning**: Infer quantum Hamiltonians from data

**Key paper**: arXiv:2604.03482 - "Learning high-dimensional quantum entanglement through physics-guided neural networks"

Example:
```python
# Physics constraint: wavefunction normalization
psi_normalized = psi_raw / torch.norm(psi_raw)
# Physics constraint: Born rule (probability from amplitude)
probability = torch.abs(psi_normalized)**2
```

### Fluid Dynamics

- **Navier-Stokes solver**: Learn flow fields
- **Turbulence modeling**: Physics-constrained turbulence
- **Boundary layer**: Enforce no-slip boundary conditions

### Materials Science

- **Crystal energy landscapes**: Predict crystal properties
- **Phase transitions**: Learn thermodynamic transitions
- **Mechanical properties**: Stress-strain relationships

**Key paper**: arXiv:2604.04636 - "Interpretation of Crystal Energy Landscapes with Kolmogorov-Arnold Networks"

## Best Practices

1. **Start simple**: Begin with one physics constraint, add more incrementally
2. **Balance weights**: Tune physics_loss_weight to balance data vs physics
3. **Verify physics**: Check that trained model actually satisfies physics
4. **Use symbolic**: Symbolic differentiation for exact PDE residuals
5. **Test extremes**: Physics should hold even for unusual inputs

## Common Pitfalls

- **Over-constraining**: Too many physics terms → model can't learn from data
- **Wrong physics**: Using incorrect physical laws
- **Numerical issues**: Computing derivatives numerically can be unstable
- **Training instability**: Physics loss gradients may conflict with data gradients

## Resources

### References (load as needed)

- `references/quantum_states.md`: Neural network quantum states methods
- `references/pde_solver.md`: Physics-informed neural networks for PDEs
- `references/symmetry.md`: Equivariant neural networks

### Key Papers

- arXiv:2604.03482 - Physics-guided quantum entanglement
- arXiv:2604.04435 - Neural-network quantum states for few-body problems
- arXiv:2604.04636 - Kolmogorov-Arnold Networks for crystal energy
- Raissi et al. (2019) - Physics-informed neural networks (PINN)

### External

- DeepXDE library: https://github.com/lululxvi/deepxde
- JAX-CFD: Physics-constrained fluid dynamics
- PennyLane: Quantum machine learning

## Activation Triggers

Use this skill when:
- Modeling physical systems (quantum, fluid, materials, etc.)
- User mentions "physics-informed", "PINN", "physics-guided"
- Data has physical constraints that should be preserved
- Need interpretable, physically consistent predictions
- Working with quantum states, entanglement, or Hamiltonians

## Example Usage

**User**: "How do I build a neural network that respects energy conservation?"

**Agent**:
1. Identify energy conservation as key physics
2. Recommend architecture-based or loss-based approach
3. Show code for energy-preserving layer or loss function
4. Explain trade-offs between hard vs soft constraints
5. Reference quantum states or fluid dynamics examples

## Related Skills

- **neural-network-quantum-states**: Specialized for quantum systems
- **pde-neural-solver**: For differential equations
- **equivariant-neural-networks**: For symmetry-preserving networks