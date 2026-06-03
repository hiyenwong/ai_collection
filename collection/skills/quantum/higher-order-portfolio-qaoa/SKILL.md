---
name: higher-order-portfolio-qaoa
description: "Higher-order moment portfolio optimization and scheduling using Quantum Approximate Optimization Algorithm (QAOA) with HUBO (Higher-Order Unconstrained Binary Optimization) formulations that go beyond standard QUBO, enabling more complex constraint modeling while reducing qubit requirements. Includes non-Abelian mixer designs for hybrid oscillator-qubit processors."
---

# Higher-Order Portfolio QAOA

## Description
Methodology for formulating portfolio optimization, industrial scheduling, and logistics routing problems as Higher-Order Unconstrained Binary Optimization (HUBO) problems and solving them with QAOA on both NISQ and fault-tolerant quantum processors. Captures complex process intricacies difficult to express with quadratic (QUBO) form while reducing the number of binary variables, thus lowering qubit demand. Includes non-Abelian mixer designs for hybrid continuous-variable/discrete-variable (CV-DV) quantum processors.

## Activation Keywords
- HUBO optimization
- higher-order QAOA
- beyond QUBO
- higher-order binary optimization
- quantum optimization beyond quadratic
- HUBO portfolio
- higher-order unconstrained
- non-Abelian mixer
- hybrid oscillator-qubit QAOA
- 高阶量子优化
- HUBO 组合优化

## Core Concepts

### HUBO vs QUBO
- **QUBO**: Quadratic Unconstrained Binary Optimization — limited to pairwise interactions (2-body terms)
- **HUBO**: Higher-Order Unconstrained Binary Optimization — supports k-body interactions (k > 2)
- **Advantage**: HUBO captures complex correlations directly without quadratic reduction overhead
- **Trade-off**: Higher-order terms require more sophisticated quantum circuits but fewer total qubits

### Mathematical Framework
```
HUBO: minimize f(x) = Σ_i c_i x_i + Σ_{i<j} c_{ij} x_i x_j + Σ_{i<j<k} c_{ijk} x_i x_j x_k + ...
where x_i ∈ {0, 1}
```

### Non-Abelian Mixer for Hybrid CV-DV Processors
- Standard QAOA uses transverse-field mixer: H_M = Σ X_i
- Non-Abelian mixer: exploits hybrid oscillator-qubit native gates
- Enables better exploration of solution space for HUBO problems
- Hardware-native: matches actual gate set on hybrid CV-DV processors

### QAOA Mapping for HUBO
1. **Cost Hamiltonian**: Encode HUBO objective as diagonal Hamiltonian H_C
2. **Mixer Hamiltonian**: Choose hardware-native mixer (e.g., transverse-field, non-Abelian)
3. **Ansatz**: U(β,γ) = e^{-iβ_p H_M} e^{-iγ_p H_C} ... e^{-iβ_1 H_M} e^{-iγ_1 H_C}
4. **Classical Optimization**: Optimize parameters (β, γ) to minimize ⟨ψ|H_C|ψ⟩

## Usage Patterns

### Pattern 1: Industrial Scheduling as HUBO
When scheduling problems have complex correlated rules (e.g., assembly-line dependencies), formulate as HUBO to capture higher-order interactions natively.

### Pattern 2: Portfolio Optimization with Higher-Order Moments
Beyond mean-variance (quadratic), incorporate skewness (3-body) and kurtosis (4-body) terms directly in HUBO formulation.

### Pattern 3: Logistics Routing
Transport routing with multi-stop dependencies and time-window constraints naturally maps to higher-order terms.

### Pattern 4: Non-Abelian Mixer on Hybrid Processors (arXiv:2605.30234)
- For hybrid oscillator-qubit platforms, design hardware-native non-Abelian mixer
- Develop hybrid ansatz combining continuous-variable and discrete-variable components
- Benchmark against standard transverse-field mixer using approximation ratio

## Instructions for Agents

### Step 1: Problem Analysis
- Identify the optimization objective and constraints
- Determine if higher-order interactions exist (3+ variables coupled)
- Estimate qubit requirements for QUBO vs HUBO formulations

### Step 2: HUBO Formulation
- Express objective as polynomial in binary variables
- Group terms by order (1-body, 2-body, 3-body, ...)
- Identify which constraints can be encoded directly vs. penalized

### Step 3: Quantum Mapping
- Map binary variables to qubits (or qudits for higher-order)
- Construct cost Hamiltonian from HUBO polynomial
- Select appropriate mixer (standard transverse-field or problem-specific non-Abelian)

### Step 4: QAOA Execution
- Set initial parameters (often from classical relaxation)
- Run quantum circuit at depth p
- Classically optimize parameters using gradient-free methods

### Step 5: Result Analysis
- Extract solution from measurement statistics
- Compare approximation ratio against classical baselines
- Analyze resource scaling with problem size

## Error Handling

### HUBO-to-QUBO Reduction
If quantum hardware only supports 2-body interactions:
- Use reduction techniques (ancilla qubits, penalty methods)
- Trade-off: introduces additional qubits but enables execution on standard hardware

### Barren Plateaus
- Use problem-informed initialization
- Layerwise training strategy
- Monitor gradient norms during optimization

### Hardware Limitations
- For NISQ: limit circuit depth, use error mitigation
- For fault-tolerant: leverage full higher-order native gates

## Resources
- arXiv:2605.30252 — Quantum optimization beyond QUBO for industrial logistics and scheduling
- arXiv:2605.30234 — Non-Abelian Mixer for QAOA on Hybrid Oscillator-Qubit Quantum Processors

## Related Skills
- quantum-portfolio-optimization
- quantum-optimization-qaoa
- quantum-computing-patterns
