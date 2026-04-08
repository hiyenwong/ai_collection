---
name: physics-guided-neural-network
description: "Design neural networks that embed physical constraints (equations, symmetries, conservation laws) directly into the computational graph. Use when modeling physical systems, scientific computing, or when physics-informed AI is needed. Keywords: PGNN, physics-guided NN, physics-informed ML, physics-embedded NN, scientific ML, holographic QCD, AdS Dirac equation."
---

# Physics-Guided Neural Networks (PGNN)

Design patterns for embedding physical constraints into neural network architectures, ensuring outputs satisfy physical laws while maintaining learning flexibility.

## Core Concepts

### 1. Physics Embedding Strategy

**Key Principle:** Physical equations are not just loss functions - they are embedded into the network architecture as computational graph constraints.

**Three Levels of Integration:**

| Level | Method | Example |
|-------|--------|---------|
| **Soft Constraint** | Physics loss term | L = L_data + λ L_physics |
| **Hard Constraint** | Architecture design | Conservation law enforced |
| **Embedded Equation** | Computational graph | Differential equation in forward pass |

**Design Rule:**
```
Physical Law -> Computational Graph Node
Network Parameters -> Physical Parameters
Output -> Physics-Satisfying Solution
```

### 2. Holographic QCD Pattern (from 2604.02906)

**AdS/CFT Correspondence in Neural Networks:**
- 5D AdS₅ Dirac equation embedded in network
- String diffusion kernel as transformation layer
- Proton mass constraint: M_p ≡ 938 MeV
- Physical parameters guide network weights

**Architecture Template:**
```
Input: Experimental data (F_2 structure function)

Physics-Guided Layers:
  1. AdS₅ geometry encoding (spatial embedding)
  2. Dirac equation solver (differential layer)
  3. Diffusion kernel transform (propagation layer)
  
Physical Constraints:
  - Proton mass bound
  - Energy conservation
  - Gauge symmetry

Output: Physics-constrained predictions
```

### 3. Symmetry Preservation Patterns

**Symmetry Types to Embed:**

| Symmetry | Embedding Method | Example |
|----------|------------------|---------|
| Gauge | Equivariant layers | U(1), SU(N) |
| Translational | Convolution | Periodic systems |
| Rotational | Spherical harmonics | Molecular systems |
| Lorentz | Tensor structure | Field theory |

**Implementation:**
```python
# Example: Embedding gauge symmetry
class GaugeEquivariantLayer(nn.Module):
    def forward(self, x):
        # Ensure output transforms same as input under gauge group
        return gauge_transform(self.linear(x))
```

## Implementation Checklist

### Step 1: Identify Physical Laws
1. List governing equations (ODE/PDE)
2. Identify conserved quantities
3. Determine symmetries and invariances
4. Note physical parameter bounds

### Step 2: Choose Embedding Level
1. **Soft**: For approximate physics (training guidance)
2. **Hard**: For exact physics (output guarantee)
3. **Embedded**: For physics-first (architecture priority)

### Step 3: Design Architecture
1. Map physics to network structure
2. Create physics-guided layers
3. Implement constraint modules
4. Define physics loss terms

### Step 4: Validate Physics
1. Check conservation laws at output
2. Verify symmetry transformations
3. Test parameter bounds
4. Compare to analytical solutions

## Example Architectures

### Example 1: Holographic QCD Proton Model

```
Physics: Quantum Chromodynamics in non-perturbative regime
Equations: AdS₅ Dirac equation, string diffusion kernel
Constraints: Proton mass M_p = 938 MeV

Architecture:
  Input: Bjorken-x, Q² (kinematic variables)
  
  Geometry Encoding:
    - AdS₅ spatial coordinates embedding
    - Warp factor integration
  
  Physics-Guided Core:
    - Dirac equation solver (differential layer)
    - Diffusion kernel transform
    - Holographic mapping
  
  Output: Structure function F₂(x, Q²)
  
  Physical Validation:
    - Mass constraint check
    - Regge limit behavior
    - Deep inelastic scaling

Benefits:
  - Predictions satisfy QCD physics
  - Works in transition regime (no pure theory)
  - Extrapolates to unmeasured regions
```

### Example 2: Fluid Dynamics Simulator

```
Physics: Navier-Stokes equations
Equations: Conservation of mass, momentum, energy
Constraints: Incompressibility (div v = 0)

Architecture:
  Input: Initial velocity field
  
  Conservation Layers:
    - Mass: divergence-free enforcement
    - Momentum: pressure-velocity coupling
    - Energy: dissipation modeling
  
  Physics-Guided Propagation:
    - Advection term (convective layer)
    - Diffusion term (viscous layer)
    - Pressure correction
  
  Output: Time-evolved velocity field
  
  Physical Validation:
    - Zero divergence check
    - Energy conservation
    - Boundary condition satisfaction

Benefits:
  - Exact conservation laws
  - Stable long-time evolution
  - No spurious numerical artifacts
```

### Example 3: Quantum Field Theory

```
Physics: Topological field theory (BKT transition)
Equations: Neural network field theory
Constraints: Topological quantum numbers

Architecture:
  Input: Temperature, field configuration
  
  Topological Encoding:
    - Discrete quantum numbers as parameters
    - Vortex/anti-vortex detection
    - Spin-wave modes
  
  Field Theory Layers:
    - Statistical ensemble of fields
    - Network architecture as field definition
    - Parameter density as field measure
  
  Output: Correlation functions, critical points
  
  Physical Validation:
    - BKT transition recovery
    - T-duality verification
    - Spin-wave critical line

Benefits:
  - Recovers known physics exactly
  - Extends to unexplored regimes
  - Topological structure preserved
```

## Common Patterns from Literature

### Pattern: Differential Equation as Layer
**From:** Physics-Informed Neural Networks (PINNs)
**Key Insight:** ODE/PDE can be forward pass operations
**Application:** Use autograd for automatic physics satisfaction

### Pattern: Conservation as Architecture
**From:** Symplectic neural networks
**Key Insight:** Hard constraints > soft constraints for physics
**Application:** Design layers that conserve by construction

### Pattern: Symmetry as Transformation
**From:** Gauge-equivariant neural networks
**Key Insight:** Network should respect group structure
**Application:** Use equivariant layers for symmetry groups

## Key Papers Reference

- **Physics-Guided NN for Holographic QCD** (2604.02906): PGNN with AdS₅ Dirac equation
- **Topological Effects in Neural Network Field Theory** (2604.02313): Topological quantum numbers
- **PINNs** (Raissi et al. 2019): Physics-informed neural networks
- **Equivariant NN** (Cohen & Welling 2016): Group theory in architectures

## Tools Used

- `exec`: Run physics simulations, solve ODEs
- `read`: Load physical equations, domain knowledge
- `write`: Document physics-guided architectures
- `edit`: Modify network configurations

## Error Handling

### Physics Violation
**Symptom:** Output violates conservation law
**Solution:** Strengthen hard constraint embedding

### Numerical Instability
**Symptom:** Physics-guided layer diverges
**Solution:** Add regularization, check discretization

### Over-constrained Network
**Symptom:** Network cannot learn due to too many constraints
**Solution:** Relax some constraints to soft penalties

## Related Skills

- **quantum-classical-hybrid-nn**: Quantum computing integration
- **neural-dynamics-universal-translator**: Neural dynamics modeling
- **pinn-neuronal-parameter-estimation**: PINN for neuron models

## Notes

- Physics embedding is architecture-first, not loss-first
- Hard constraints guarantee physics but may limit flexibility
- Soft constraints allow learning but may violate physics
- Validate against analytical solutions when available
- Consider computational cost of physics layers