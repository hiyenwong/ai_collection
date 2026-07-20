---
name: fermi-dirac-quantized-neurons
description: "Fermi-Dirac quantization methodology for neural networks — reinterprets classical neurons as parameterized Hamiltonians and replaces variables with quantum operators. BQP-complete for certain decision problems. Use when: designing quantum neural architectures, quantizing activation functions (ReLU, GeLU, sigmoid), building hybrid quantum-classical neural algorithms, analyzing quantum advantage in neural computation, or studying the quantum-classical boundary in machine learning."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.24386"
  published: "2026-05-23"
  authors: "Alexander He, Nana Liu, Mark M. Wilde"
  tags: [quantum, neural-networks, fermi-dirac, quantization, bqp, activation-functions]
---

# Fermi-Dirac Quantized Neurons

Canonical quantization framework that reinterprets classical neurons as parameterized classical Hamiltonians, then replaces classical variables with quantum operators to yield quantum Hamiltonian neurons. Proves BQP-completeness for the associated decision problem.

## Core Methodology

### Classical-to-Quantum Neuron Mapping

1. **Classical neuron**: activation function f applied to parameterized classical Hamiltonian H(θ, x)
2. **Quantization**: replace classical variables (x, p) → quantum operators (x̂, p̂) with [x̂, p̂] = iℏ
3. **Quantum neuron output**: ⟨ψ|f(Ĥ(θ, x̂, p̂))|ψ⟩ where f acts on the quantum Hamiltonian as an operator function
4. **Measurement**: observable expectation value replaces classical scalar output

### Quantized Activation Functions

Key quantization targets:
- **Smooth ReLU**: f(x) = x·σ(x/β) → f(Ĥ) via spectral theorem
- **GeLU**: f(x) = x·Φ(x) where Φ is Gaussian CDF → requires operator-valued Gaussian integration
- **Sigmoid Linear Unit (SiLU)**: f(x) = x/(1+e^{-x}) → rational function of e^{Ĥ}
- **Gaussian-smoothed ReLU**: convolution with Gaussian kernel → operator exponential

For each, the activation observable is computed via spectral decomposition of Ĥ.

### Hybrid Quantum-Classical Algorithm

```
Forward pass:
  1. Prepare |ψ⟩ on quantum device
  2. Apply Ĥ(θ, x) evolution: e^{-iĤt}
  3. Measure ⟨f(Ĥ)⟩ via Hamiltonian simulation + observable estimation
  
Gradient computation:
  1. Parameter-shift rule: ∂θ⟨f(Ĥ)⟩ = ½[⟨f(Ĥ(θ+π/2))⟩ - ⟨f(Ĥ(θ-π/2))⟩]
  2. Classical optimizer updates θ using quantum-evaluated gradients
```

### BQP-Completeness Proof Sketch

The decision problem "does a Fermi-Dirac neuron with given parameters output ≥ threshold?" is BQP-complete:
- **BQP-hard**: universal quantum computation can be encoded in a single Fermi-Dirac neuron with appropriate activation
- **In BQP**: quantum circuits can efficiently evaluate the neuron output via Hamiltonian simulation

## Mathematical Framework

The quantization map Q: C^∞(phase space) → Operators follows:
- Position/momentum: Q(x_j) = x̂_j, Q(p_j) = -iℏ∂/∂x_j
- Hamiltonian: Q(H(x,p,θ)) = Ĥ(x̂,p̂,θ)
- Activation: f(H) → f(Ĥ) via functional calculus (spectral theorem for self-adjoint operators)

The Fermi-Dirac distribution enters through:
- n_F(E) = 1/(e^{β(E-μ)} + 1) as a natural quantum activation function
- Thermal states ρ = e^{-βĤ}/Z provide natural mixed-state neuron initialization

## Error Handling

### Hamiltonian Simulation Errors
- Trotterization error scales as O(t²/n) for n Trotter steps
- Use qubitization or LCU methods for O(t) scaling when available

### Gradient Estimation
- Parameter-shift requires 2 evaluations per parameter
- For noisy hardware: use stochastic parameter shift or finite-difference fallback

### Activation Function Quantization
- Non-analytic activations (e.g., hard ReLU) require regularization
- Use smooth approximations with parameter β → ∞ for sharp limit
