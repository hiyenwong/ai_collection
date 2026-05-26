---
name: fermi-dirac-quantized-neurons
description: "Fermi-Dirac quantized neuron methodology — canonical quantization of classical neurons into quantum activation observables. Replaces classical variables with operators whose eigenvalues encode possible values, yielding quantum neurons that can learn functions classical neurons cannot. BQP-complete. Applicable to quantum ML, hybrid quantum-classical algorithms, quantum neural architecture design. Activation: quantized neuron, Fermi-Dirac machine, quantum activation, canonical quantization, quantum neuron."
---

# Fermi-Dirac Quantized Neurons Methodology

Based on arXiv:2605.24386 — "Fermi-Dirac machines as quantizations of neurons" by Alexander He, Nana Liu, Mark M. Wilde (May 2026).

## Core Insight

Classical neurons can be reinterpreted as **canonical quantizations** of classical Hamiltonian systems. By replacing classical variables with quantum operators, we get **quantized neurons** whose outputs are random variables with expectation values equal to activation observables applied to parameterized quantum Hamiltonians.

## Key Principles

### 1. Canonical Quantization of Neurons

A classical neuron: `output = σ(w·x + b)` where σ is activation function.

Quantized version:
- View classical neuron as activation σ applied to parameterized classical Hamiltonian H(w,x,b)
- Replace classical variables with quantum operators
- Eigenvalues encode possible values of classical variables
- When Hamiltonian consists of **commuting operators**, construction reduces exactly to classical neuron
- More generally: yields **activation observable** = σ(H_quantum)

### 2. Activation Observable

```
output = ⟨ψ| σ(H(θ)) |ψ⟩
```

Where:
- `|ψ⟩` is input quantum state
- `H(θ)` is parameterized quantum Hamiltonian
- `σ` is activation function (ReLU, sigmoid, GeLU, etc.)
- Output is random variable with expectation = activation observable

### 3. Hybrid Quantum-Classical Training Algorithms

Efficient algorithms for evaluating outputs and gradients:
- **Random sampling** — estimate expectation values
- **Hamiltonian simulation** — evolve under parameterized Hamiltonian
- **Hadamard test** — measure observables

### 4. Quantized Activation Functions

Supported quantized activations:
- **Smooth ReLU** — differentiable variant
- **Sigmoid Linear Unit (SLU)** — smooth transition
- **Gaussian-smoothed ReLU** — noise-robust
- **Gaussian Error Linear Unit (GeLU)** — transformer-style

### 5. Complexity: BQP-Complete

The computational decision problem based on Fermi-Dirac neurons is **BQP-complete**, providing complexity-theoretic evidence against efficient classical simulation.

## Workflow

### Step 1: Define Classical Neuron as Hamiltonian

```python
# Classical neuron: σ(w·x + b)
# Hamiltonian formulation: H(w, x, b) = w·x + b (diagonal in computational basis)
```

### Step 2: Quantize Variables

```python
# Replace scalars with operators:
# w → Ŵ (weight operator)
# x → X̂ (input operator)  
# b → B̂ (bias operator)
# H_quantum = Ŵ · X̂ + B̂
```

### Step 3: Apply Activation to Hamiltonian

```python
# σ(H_quantum) = activation observable
# Use spectral decomposition: σ(H) = Σ_i σ(λ_i) |i⟩⟨i|
```

### Step 4: Evaluate Output

```python
# output = ⟨ψ| σ(H(θ)) |ψ⟩
# Estimate via repeated measurement or Hadamard test
```

### Step 5: Compute Gradients

```python
# ∂output/∂θ = ⟨ψ| ∂σ(H)/∂θ |ψ⟩
# Use parameter-shift rule or finite differences
```

### Step 6: Train

```
for epoch in range(epochs):
    for batch in data:
        # Encode input as quantum state
        |ψ⟩ = encode(batch.x)
        
        # Forward pass
        output = ⟨ψ| σ(H(θ)) |ψ⟩
        
        # Compute loss and gradients
        loss = loss_fn(output, batch.y)
        grads = compute_gradients(H, σ, |ψ⟩)
        
        # Update parameters
        θ = θ - lr * grads
```

## Pitfalls

1. **Commuting operators reduce to classical** — Non-commutativity is essential for quantum advantage. Ensure Hamiltonian terms don't all commute.
2. **State preparation overhead** — Encoding classical data into quantum states can be expensive. Use amplitude/angle encoding wisely.
3. **Measurement shot noise** — Expectation values estimated from finite samples. More shots = more accurate but slower.
4. **NISQ limitations** — Current hardware noise limits circuit depth. Keep circuits shallow for near-term deployment.
5. **Activation function choice matters** — Smooth activations (GeLU, smooth ReLU) are more amenable to quantum implementation than discontinuous ones.

## Applications

- **Quantum neural networks** — building blocks for QNNs
- **Hybrid quantum-classical ML** — replace classical layers with quantized neurons
- **Quantum advantage demonstration** — learn functions classical neurons cannot
- **Quantum reservoir computing** — use as readout functions
- **Time-series forecasting** — see arXiv:2605.24252 for 100+ qubit scale applications

## Benchmarking

Based on arXiv:2605.24324 findings:
- **Amplitude encoding** removes magnitude info via unit-sphere normalization — use carefully
- **Angle encoding** can be geometrically redundant with raw linear features
- **Basis encoding** imposes binary Hamming geometry — poorly aligned with smooth decision surfaces
- **Fixed quantum-inspired encoding geometry alone** is NOT a reliable ML advantage source on classical data

## Verification

- Quantized neurons should reduce to classical neurons when all operators commute
- BQP-completeness means no efficient classical simulation exists for general case
- Numerical experiments show quantum neurons learn functions classical neurons cannot

## Related Papers

- arXiv:2605.24252 — Hybrid QML for multi-output time-series forecasting at 100+ qubit scale
- arXiv:2605.24324 — Matched spectral benchmark of quantum-inspired feature maps
