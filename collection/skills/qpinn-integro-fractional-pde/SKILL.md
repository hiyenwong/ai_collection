---
name: qpinn-integro-fractional-pde
description: "Quantum Physics-Informed Neural Networks for solving integro-differential equations (IDEs) and fractional integro-partial differential equations (FIPDEs) using variational quantum circuits with affine feature maps."
trigger_words:
  - "quantum PINN"
  - "quantum physics-informed neural network"
  - "QPINN"
  - "integro-differential equation"
  - "fractional PDE"
  - "fractional integro-partial differential equation"
  - "quantum trial solution"
  - "affine feature map quantum"
  - "numerical quadrature QPINN"
  - "auxiliary function QPINN"
  - "quantum Fourier approximation"
arxiv_id: "2606.26865"
paper_title: "Quantum Physics-Informed Neural Networks for Solving Integro and Fractional PDEs"
created_at: "2026-06-26"
category: "quantum"
---

# QPINN Integro-Fractional PDE

## Description

Quantum Physics-Informed Neural Network (QPINN) methodology for solving integro-differential equations (IDEs) and fractional integro-partial differential equations (FIPDEs). Uses variational quantum circuits with affine feature maps to produce trial solutions with explicit trigonometric structure, proven to achieve O(n^{-1/2}) convergence rate. Two variants: N-QPINN (numerical quadrature) and A-QPINN (auxiliary function reformulation).

## Activation Keywords
- quantum PINN
- QPINN
- quantum physics-informed neural network
- integro-differential equation quantum
- fractional PDE quantum
- quantum trial solution
- affine feature map quantum
- N-QPINN
- A-QPINN
- quantum Fourier approximation

## Tools Used
- web_search: Find arxiv papers on quantum PINN and fractional PDEs
- write_file: Create QPINN implementation scripts
- terminal: Run quantum circuit simulations
- skill_manage: Update related QPINN skills

## Usage Patterns

### Pattern 1: Solving Integro-Differential Equations with N-QPINN
Use N-QPINN when the IDE has nonlocal integral operators that can be handled via numerical quadrature:
1. Construct affine feature map: encode input x → quantum state |φ(x)⟩
2. Apply variational quantum circuit with trainable parameters θ
3. Use automatic differentiation for local derivatives of quantum trial solution
4. Apply high-order numerical quadrature for nonlocal integral terms
5. Minimize physics-informed loss combining PDE residuals and boundary conditions

### Pattern 2: Solving Fractional PDEs with A-QPINN
Use A-QPINN when fractional operators make quadrature expensive:
1. Introduce auxiliary variables to reformulate fractional IDE as coupled PDE system
2. Build multi-output quantum neural network
3. Simultaneously represent solution and auxiliary variables
4. Eliminate numerical quadrature entirely through system reformulation

### Pattern 3: Convergence Analysis
The proven O(n^{-1/2}) convergence rate extends classical Fourier approximation theory to quantum circuits:
- n = number of quantum circuit parameters
- Convergence holds in L²(μ) norm
- Applicable to any nonlinear IDE/FIPDE with smooth coefficients

## Instructions for Agents

### Step 1: Problem Classification
Determine if the target equation is:
- **IDE** (integro-differential): Contains integral operators + derivatives → Use N-QPINN
- **FIPDE** (fractional integro-partial): Contains fractional derivatives + integral terms → Use A-QPINN for efficiency
- **Standard PDE**: Consider classical PINN unless quantum advantage is needed

### Step 2: QPINN Architecture Design
1. **Feature Map**: Use affine encoding φ(x) = Rx(θ₁)Rz(θ₂)... for input encoding
2. **Ansatz**: Variational quantum circuit with entangling layers
3. **Output**: Trigometric structure from quantum measurement expectation values
4. **Training**: Gradient-based optimization of circuit parameters

### Step 3: Implementation
```
# N-QPINN pattern
1. Encode spatial/temporal domain into quantum states
2. Compute derivatives via parameter-shift rule
3. Evaluate integrals via Gaussian quadrature on quantum circuit
4. Construct loss: L = L_PDE + L_BC + L_IC
5. Optimize with gradient descent

# A-QPINN pattern
1. Reformulate fractional PDE as coupled system via auxiliary variables
2. Build multi-output quantum network (one output per variable)
3. Train jointly on all equations in coupled system
4. Extract primary solution from network output
```

### Step 4: Validation
- Compare against analytical solutions when available
- Benchmark against classical PINN baselines
- Verify convergence rate matches O(n^{-1/2}) theoretical bound
- Test on multiple problem instances for robustness

## Error Handling
### Quadrature Error in N-QPINN
If numerical quadrature fails for highly oscillatory integrals:
- Switch to A-QPINN auxiliary function reformulation
- Increase quadrature order or use adaptive quadrature

### Barren Plateaus
If gradient vanishes during training:
- Reduce circuit depth
- Use layer-wise training
- Apply parameter initialization strategies from quantum control literature

### Convergence Issues
If convergence is slower than O(n^{-1/2}):
- Verify smoothness of coefficients
- Check boundary condition encoding
- Consider increasing number of measurement shots

## Resources
- arXiv:2606.26865 - Quantum Physics-Informed Neural Networks for Solving Integro and Fractional PDEs
- Related skills: `hybrid-quantum-fbpinn`, `pinn-neuronal-parameter-estimation`, `qcpikan-quantum-pinn-pde`
