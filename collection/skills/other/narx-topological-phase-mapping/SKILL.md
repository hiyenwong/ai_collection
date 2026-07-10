---
name: narx-topological-phase-mapping
description: "NARX neural network methodology for deterministic mapping of topological phase transitions in quantum systems. Uses autoregressive exogenous inputs to discover functional identities between topological invariants and critical parameters."
---

# NARX Topological Phase Mapping

## Description

NARX (Nonlinear Autoregressive with Exogenous Inputs) neural network methodology for deterministically mapping topological phase transitions in quantum systems. Achieves numerical-precision-level accuracy (MSE ~10^{-27}) when correctly configured, revealing exact functional identities between topological invariants and critical parameters. Applicable to any quantum system where analytical solutions for phase transitions are elusive.

## Activation Keywords

- narx topological phase
- autoregressive exogenous neural network quantum
- NARX phase transition mapping
- deterministic phase boundary discovery
- neural network topological invariant
- 神经网络拓扑相变
- 自回归外生网络量子
- winding number neural mapping

## Core Concepts

### Three Architecture Comparison

The methodology compares three dynamic neural network architectures:

1. **NAR (Nonlinear Autoregressive)**: Uses only past outputs as feedback. Good for local trend capture but limited for complex phase mappings.

2. **NARX (Nonlinear Autoregressive with Exogenous Inputs)**: Combines autoregressive feedback with immediate external context. **Superior architecture** — achieves MSE of 10^{-27} (numerical precision limit) at optimal delay d=1.

3. **NIO (Nonlinear Input-Output)**: Uses only exogenous inputs without autoregressive feedback. Fails to resolve phase transitions despite increased neuronal capacity.

### Key Findings

- **Deterministic Identity**: NARX achieving numerical-precision MSE implies the relationship between the topological invariant (winding number W) and critical parameter (c_crit) is mathematically deterministic, not just approximable.
- **Optimal Delay = 1**: The best performance at d=1 means the phase transition depends on the immediate previous state + current external input, not long-range temporal dependencies.
- **Complexity Paradox**: NARX accuracy *collapses* at higher delays (d=4), confirming the model captures a precise dynamic mapping rather than learning trivial patterns. This is a validation signal, not a bug.
- **Both Components Essential**: Autoregressive feedback AND immediate exogenous context are both required. Removing either (NAR or NIO) degrades performance dramatically.

## Mathematical Framework

### NARX Model

y(t) = f(y(t-1), ..., y(t-d), u(t), u(t-1), ..., u(t-d)) + ε

Where:
- y(t) = target parameter (e.g., c_crit)
- u(t) = exogenous input (e.g., winding number W)
- d = delay parameter
- f = nonlinear function approximated by neural network

### Phase Transition Mapping

For a quantum system characterized by:
- Topological invariant: W ∈ ℤ (winding number, Chern number, etc.)
- Control parameter: λ (measurement strength, coupling, etc.)
- Critical value: λ_crit(W) where phase transition occurs

The NARX learns: λ_crit(W) = f(W, λ_crit(W-1))

## Usage Patterns

### Pattern 1: Discovering Critical Parameters

Use when you have a quantum system with a known topological invariant but unknown critical parameter values:

1. Define topological invariant W as exogenous input u(t)
2. Set target y(t) = critical parameter value at each W
3. Train NARX with delay d=1
4. If MSE approaches numerical precision (~10^{-27} in float64), a deterministic functional identity exists
5. Extract the learned function for analytical study

### Pattern 2: Architecture Comparison for Validation

Compare NAR vs NARX vs NIO to validate the mapping quality:
- If NARX >> NAR ≈ NIO: phase transition has both temporal and external dependencies
- If NAR ≈ NARX >> NIO: mainly autoregressive (temporal) dynamics
- If NIO >> NAR ≈ NARX: mainly driven by external inputs
- If all similar: no strong structure in the data

### Pattern 3: Delay Sweep for Complexity Analysis

Sweep delay d from 1 to 4+:
- Optimal at d=1: immediate dependency (most common for phase transitions)
- Optimal at d>1: longer-range temporal dependencies
- Accuracy collapse at higher d: confirms non-trivial, high-precision mapping (complexity paradox as validation)

## Instructions for Agents

### Step 1: Problem Formulation

Identify:
- **Topological invariant**: What integer-valued quantity characterizes the phases? (winding number, Chern number, Z2 invariant, etc.)
- **Control parameter**: What continuous parameter drives the phase transition?
- **Critical boundary**: What is the critical value as a function of the invariant?

### Step 2: NARX Configuration

```python
# Key hyperparameters
delay = 1              # Start with d=1, always optimal for phase transitions
n_hidden = [64, 32]   # Two-layer network sufficient
activation = 'tanh'   # Smooth activation for differentiable mappings
max_epochs = 1000     # More epochs for precision convergence
precision_threshold = 1e-15  # Float64 machine epsilon
```

### Step 3: Training Protocol

1. Generate data: For each topological sector W, compute c_crit via numerical method
2. Split: 80/20 train/test (deterministic mapping doesn't need large datasets)
3. Train NARX with d=1
4. Monitor MSE convergence
5. If MSE < 10^{-15}: deterministic identity likely discovered
6. If MSE plateau > 10^{-10}: try NAR or increase network capacity

### Step 4: Validation

1. **Complexity paradox check**: Verify NARX degrades at d=4 (confirms non-trivial mapping)
2. **Architecture comparison**: Train NAR and NIO, confirm NARX superiority
3. **Analytical extraction**: Use symbolic regression on NARX predictions to find closed form
4. **Physical consistency**: Verify learned mapping respects known symmetries and boundary conditions

## Error Handling

### NARX Fails to Converge
- Check if topological invariant is correctly computed
- Try symbolic preprocessing (normalize W range)
- Consider if the phase transition is genuinely stochastic (not deterministic)

### All Architectures Perform Poorly
- The relationship may not be a clean function (multi-valued, discontinuous)
- Consider adding more exogenous inputs (system size, boundary conditions)
- Check for numerical precision issues in the ground truth computation

### NARX Too Good (MSE < 10^{-20})
- This is the expected outcome for deterministic phase transitions
- Use this as evidence that a closed-form analytical solution exists
- Apply symbolic regression to extract the exact functional form

## Examples

### Example: Quantum Walk Phase Transition

System: Quantum walk with weak measurements
- Invariant: Winding number W ∈ {-1, 0, +1}
- Control: Measurement strength c
- Target: c_crit(W) where topological phase transition occurs

NARX configuration:
- Input: W (exogenous)
- Feedback: c_crit(W-1)
- Delay: d=1
- Result: MSE = 10^{-27} → deterministic identity c_crit(W) = f(W)

### Example: Topological Insulator Band Inversion

System: 2D topological insulator
- Invariant: Chern number C
- Control: Mass parameter m
- Target: m_crit(C) where band inversion occurs

NARX would learn: m_crit(C) = f(C, m_crit(C-1))

## Resources

- arXiv:2605.27300 — "Deterministic Mapping of Topological Phases via Autoregressive Exogenous Neural Networks"
- NARX neural networks: Billings (2013) "Nonlinear System Identification: NARMAX Methods"
- Topological phases: Bernevig & Hughes, "Topological Insulators and Topological Superconductors"
