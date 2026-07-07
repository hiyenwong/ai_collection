---
name: low-rank-gluing-compositionality
description: "Mathematical framework for compositional computation in inhibition-dominated threshold-linear networks via low-rank gluing rules. Proves how structural modularity enables functional compositionality - component subnetworks' fixed points determine global network dynamics. Activation: compositionality, threshold-linear networks, TLN, fixed points, modular network, network assembly, gluing rules, low-rank coupling, inhibition-dominated, neural circuit design, computational primitives"
metadata:
  arxiv_id: "2606.07336"
  published: "2026-06-05"
  authors: "Juliana Londono Alvarez"
  category: "computational neuroscience, neural dynamics, network theory"
license: Complete terms in LICENSE.txt
---

# Low-Rank Gluing Compositionality in Threshold-Linear Networks

Mathematical framework proving how modular network structure supports compositional computation via specific low-rank couplings between subnetworks.

## Core Theory

### Compositional Computation Problem

Brains generate complex behaviors from stable structures via **compositionality** - decomposing tasks into reusable primitives. This skill provides the mathematical proof for how structural modularity enables functional compositionality.

**Key Question**: How do component subnetworks combine to preserve their individual computations while forming new global behaviors?

### Threshold-Linear Networks (TLNs)

Inhibition-dominated TLNs model biological neural circuits:

```
dx/dt = -x + [Wx + b]₊
```

where:
- `x`: neuron activity vector
- `W`: weight matrix (inhibition-dominated means negative diagonal)
- `b`: external input
- `[·]₊`: ReLU nonlinearity (threshold-linear)

**Fixed points** satisfy: `x* = [Wx* + b]₊`

### Low-Rank Gluing Rules

**Novel contribution**: Introduces `low-rank gluings` - a class of modular network assembly where:

1. **Component subnetworks** have arbitrary internal connectivity `W₁, W₂, ...`
2. **Inter-network couplings** are **low-rank matrices** `C_{ij} = UV^T` (rank `<<` dimension)
3. **Global fixed points** = composition of component fixed points

**Theorem**: If subnetworks have fixed points `x₁*, x₂*, ...`, then the glued network's fixed points are precisely combinations of these component fixed points, provided the gluing satisfies specific rank conditions.

## Methodology

### When to Use This Framework

Use when:
- Designing modular neural circuits with compositional properties
- Analyzing how network architecture enables task decomposition
- Proving stability/computation preservation in network assembly
- Understanding fixed point structure in recurrent networks

### Design Procedure

1. **Define component subnetworks**:
   - Specify individual weight matrices `W_i` (inhibition-dominated)
   - Compute their fixed points `x_i*` (solve `x = [Wx + b]₊`)
   - Verify component computations are distinct primitives

2. **Design gluing couplings**:
   - Choose coupling rank `r` (typically `r = 1` or `r = 2`)
   - Construct `C_{ij} = U_{ij} V_{ij}^T` where:
     - `U_{ij}`: output pattern from network `i`
     - `V_{ij}`: input pattern to network `j`
   - Ensure coupling respects fixed point structure

3. **Assemble global network**:
   ```
   W_global = [W₁   C₁₂  C₁₃]
              [C₂₁  W₂   C₂₃]
              [C₃₁  C₃₂  W₃ ]
   ```

4. **Verify compositional fixed points**:
   - Solve global fixed point equations
   - Confirm global solutions = combinations of component solutions
   - Check inhibition dominance preserved

### Mathematical Tools

- **Fixed point analysis**: Solve nonlinear systems via iterative methods or convex relaxations
- **Low-rank matrix theory**: Use singular value decomposition to constrain coupling structure
- **Lyapunov stability**: Prove attractor stability via spectral analysis

## Implementation Patterns

### Pattern 1: Primitive Composition

```python
# Define two primitives (e.g., "reach" and "grasp")
W_reach = inhibition_dominated_network(n=50, bias=b_reach)
W_grasp = inhibition_dominated_network(n=30, bias=b_grasp)

# Compute individual fixed points
x_reach_star = solve_fixed_point(W_reach)
x_grasp_star = solve_fixed_point(W_grasp)

# Glue with rank-1 coupling
U = output_pattern(x_reach_star)  # What "reach" produces
V = input_pattern_for_grasp()     # What "grasp" needs
C = U @ V.T  # Rank-1 gluing

# Assemble "reach+grasp" network
W_combined = block_matrix([[W_reach, C], [C.T, W_grasp]])

# Verify: x_combined_star = [x_reach_star, x_grasp_star]
```

### Pattern 2: Hierarchical Composition

Nested gluings enable hierarchical task decomposition:

```
Primitive A → (A+B) → (A+B+C) → Full behavior
   ↑           ↑           ↑
 Rank-1      Rank-2      Rank-3
 gluings     gluings     gluings
```

## Key Results

1. **Fixed Point Preservation**: Component fixed points survive gluing - no destruction of primitive computations

2. **Compositional Emergence**: Global fixed points = union of component fixed points + new combinations (when couplings create novel task-specific states)

3. **Stability Guarantee**: Low-rank gluings preserve inhibition dominance → stable attractors

4. **Efficiency**: Small coupling rank (`r << n`) minimizes connection cost while enabling composition

## Pitfalls

- **Rank too high**: High-rank couplings destroy fixed point structure → non-compositional dynamics
- **Excitatory coupling violates inhibition dominance**: Ensure couplings don't destabilize attractors
- **Component fixed points unstable**: Must verify individual network stability before gluing
- **Mismatched primitive semantics**: Gluing requires semantic compatibility (output of A must be valid input to B)

## Applications

- **Motor control**: Compose reach + grasp + manipulate primitives
- **Language processing**: Compose phoneme → syllable → word primitives
- **Reasoning**: Compose inference steps via gluing rules
- **Circuit design**: Build compositional neuromorphic processors

## Extensions

- **Learnable gluings**: Train coupling matrices via gradient descent
- **Dynamic gluings**: Time-varying couplings for sequential composition
- **Multi-scale composition**: Glue at neuron, population, and network levels

## References

- Original paper: arXiv:2606.07336 (Londono Alvarez, 2026)
- Related: Hopfield networks, reservoir computing, fixed point theory
- See also: `cortico-cerebellar-modularity-rnn` (cerebellar compositional architecture)

---

**Activation**: compositionality, fixed points, threshold-linear networks, TLN, modular networks, low-rank coupling, network assembly, gluing rules, inhibition-dominated networks, computational primitives, neural circuit design