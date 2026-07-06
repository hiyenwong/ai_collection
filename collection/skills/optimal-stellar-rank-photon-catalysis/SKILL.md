---
name: optimal-stellar-rank-photon-catalysis
description: "Methodology for provably optimal generation of non-Gaussian quantum states (squeezed cat states) via photon catalysis, characterized using stellar rank formalism — enables systematic comparison of fidelity against theoretical maximum for given non-Gaussian resources."
---

# Optimal Stellar Rank Approximation of Squeezed Cat States with Photon Catalysis

## Description

A methodology for analyzing and optimizing photon catalysis protocols for generating non-Gaussian quantum states (specifically squeezed coherent state superpositions / "cat states") in bosonic platforms. Uses the stellar rank formalism to characterize the non-Gaussian complexity of both input resources and generated states, enabling provable optimality claims. Identifies parameter regimes for high-fidelity approximations with minimal resources, and benchmarks against Gaussian boson sampling-inspired protocols. Based on arXiv:2607.02427 (Nauth, Walk & Datta, 2026).

## Activation Keywords

- stellar rank photon catalysis
- squeezed cat state generation
- non-Gaussian state optimization
- photon catalysis protocol
- bosonic quantum state generation
- stellar rank formalism
- 光子催化生成猫态
- 恒星秩形式化
- non-Gaussian resource complexity

## Tools Used

- exec: Run Python scripts for stellar rank computation, fidelity optimization, and loss modeling
- read: Read quantum state definitions, stellar rank specifications
- write: Output optimized protocol parameters and fidelity analysis

## Usage Patterns

### Cat State Generation Design
Given target squeezed cat state parameters, find optimal photon catalysis protocol achieving maximum fidelity for given non-Gaussian resource budget.

### Resource Complexity Analysis
Compare different non-Gaussian state generation protocols by their stellar rank — determine if a protocol is provably optimal or has room for improvement.

### Loss-Tolerant Protocol Design
Model experimental imperfections (losses across all optical modes) and identify parameter regimes robust to realistic conditions.

## Instructions for Agents

### Step 1: Characterize Input Resources via Stellar Rank

1. **Define stellar rank**: The stellar rank of a quantum state is the number of zeros of its Husimi Q-function in phase space. For Fock state |n⟩, stellar rank = n. For squeezed vacuum, stellar rank = 0 (Gaussian).
2. **Compute combined stellar rank**: For photon catalysis between |n⟩ (Fock) and |sqz⟩ (squeezed), the combined input stellar rank = n (only the Fock state contributes non-Gaussianity).
3. **Characterize measurements**: Post-selection measurements also carry stellar rank — include in total resource accounting.

### Step 2: Construct Photon Catalysis Protocol

1. **Setup**: Interfere a low-number Fock state |n⟩ with a squeezed state |ξ⟩ on a beamsplitter.
2. **Post-select**: Measure one output port in the Fock basis, conditioning on a specific outcome.
3. **Output state**: The unmeasured port yields a non-Gaussian state — typically a squeezed coherent state superposition (cat state).

### Step 3: Evaluate Fidelity Against Stellar Rank Bound

1. **Compute maximum achievable fidelity**: For any protocol with the same total stellar rank of inputs, compute the theoretical maximum fidelity to the target state.
2. **Compare catalysis fidelity**: Calculate the actual fidelity achieved by the photon catalysis protocol.
3. **Optimality proof**: If catalysis fidelity equals the stellar rank bound, the protocol is provably optimal — no other protocol with the same non-Gaussian resources can achieve higher fidelity.

### Step 4: Benchmark Against Alternatives

Compare photon catalysis with:
- Gaussian boson sampling-inspired protocols
- Direct heralded generation protocols
- Deterministic Fock state sources

Metrics: success probability, state quality (fidelity), resource complexity (stellar rank).

### Step 5: Model Experimental Imperfections

1. **Loss modeling**: Apply beam splitter model for loss in each optical mode using Fock basis truncation.
2. **Robustness analysis**: Vary loss parameters and compute fidelity degradation curves.
3. **Identify robust regimes**: Find parameter combinations where fidelity remains high (>0.95) under realistic loss rates (1-5%).

## Key Mathematical Concepts

### Stellar Rank Formalism

The stellar function of a pure state |ψ⟩ is:
$$S_ψ(z) = ⟨z^*|ψ⟩$$
where |z⟩ is a coherent state. The stellar rank r is the number of zeros of S_ψ(z) in the complex plane.

- Gaussian states: r = 0
- Single photon: r = 1
- Fock state |n⟩: r = n
- Cat state |α⟩ + |-α⟩: r = 2 (two zeros in phase space)

The stellar rank is non-increasing under Gaussian operations and additive under tensor products.

### Photon Catalysis Transformation

The beamsplitter transformation between |n⟩ and |ξ⟩ followed by Fock measurement |m⟩:
$$|ψ_{out}⟩ ∝ ⟨m|_{BS} BS(θ)(|n⟩ ⊗ |ξ⟩)$$

The output stellar rank ≤ n + m, providing a hard bound on achievable non-Gaussianity.

### Optimality Criterion

A protocol is provably optimal if:
$$F_{catalysis}(target) = max_{all protocols with same stellar rank} F(protocol, target)$$

This requires computing the maximum fidelity achievable by any state with stellar rank ≤ r to the target — a convex optimization over the stellar rank submanifold.

## Error Handling

### No Optimal Regime Found
If catalysis doesn't achieve stellar rank bound:
- Increase input Fock number n
- Optimize beamsplitter angle θ
- Consider multi-stage catalysis (sequential catalysis steps)

### Loss Too High
If fidelity degrades significantly under realistic losses:
- Use higher squeezing to compensate
- Switch to deterministic Fock state sources (better loss tolerance)
- Apply error mitigation via post-selection filtering

### Target State Too Complex
If target stellar rank exceeds input resources:
- Cannot achieve high fidelity — stellar rank is a hard limit
- Either increase input resources or accept lower-fidelity approximation
- Consider approximate targets with lower stellar rank

## Examples

### Example 1: Squeezed Cat State |α⟩ + |-α⟩

Input:
- Fock state |1⟩ (stellar rank 1)
- Squeezed state |ξ⟩ with r = 0.5 (stellar rank 0)
- Beamsplitter angle θ = π/4

Output:
- Achieved fidelity to target cat state: 0.97
- Stellar rank bound: 0.97 (protocol is provably optimal)
- Success probability: 0.15

### Example 2: Loss Analysis

Input:
- Same protocol as Example 1
- 3% loss per mode

Output:
- Fidelity after loss: 0.94
- Still above 0.9 threshold for fault-tolerant applications
- Optimal regime identified for near-term photonic implementations

## Resources

- arXiv:2607.02427 — "Optimal stellar rank approximation of squeezed cat states with photon catalysis" (Nauth, Walk & Datta, 2026)
- Stellar rank theory for quantum optics (Bartlett & Sanders framework)
- Gaussian boson sampling and non-Gaussian state generation

## Related Skills

- `quantum-error-correction-methods` — bosonic QEC using cat states
- `generalized-kerr-cat-qubit-codes` — cat-state-based quantum error correction
- `optimal-stellar-rank-photon-catalysis` — umbrella skill
- `quantum-optical-neuron` — optical quantum state processing
