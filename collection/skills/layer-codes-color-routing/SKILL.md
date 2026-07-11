---
name: layer-codes-color-routing
description: "4D and 5D Layer Codes through Color Routing — CSS code construction generalizing Layer codes to d dimensions using qLDPC embedding and color routing. Saturates d-dimensional BPT bounds exactly, modular architecture for network patches. Activation: layer codes, color routing, qLDPC codes, CSS codes, BPT bounds, quantum error correction, dimensional generalization."
---

# 4D and 5D Layer Codes through Color Routing

CSS code construction that generalizes Layer codes to arbitrary dimensions using **color routing**. Based on arXiv:2605.18961.

## Core Contribution

From a D-dimensional qLDPC code with energy barrier Δ, construct a (D+1)-dimensional Layer code with:
- Parameters: [[n^{(D+1)/D}, k, d^{(D+1)/D}]]
- Energy barrier: Δ · n^{1/D}
- **Saturates the d-dimensional BPT bounds exactly** when using good qLDPC codes as input

## Color Routing

The key innovation that overcomes hurdles from previous generalization attempts:

- **Problem**: Higher-dimensional Layer codes have complex check layer structures and line defects that don't generalize cleanly
- **Solution**: Color routing resolves the structure by assigning colors to different check types, enabling clean separation of check layers
- **Result**: Modular construction that works for any dimension d ≥ 4

## Key Properties

### Dimensional Scaling
| Input Dimension | Output Dimension | Scaling |
|----------------|------------------|---------|
| D | D+1 | n^{(D+1)/D} physical qubits |
| Energy barrier Δ | Energy barrier Δ·n^{1/D} | Improved protection |

### BPT Bound Saturation
- BPT (Bravyi-Poulin-Terhal) bounds limit code parameters in d dimensions
- This construction **exactly saturates** the bounds using good qLDPC codes
- No previous construction achieved this in d > 3

### Modular Architecture
- Higher-dimensional Layer Codes are **modular**
- Well-suited to architectures composed of **modular network patches**
- Overcomes physical limitation to three spatial dimensions through logical encoding

## When to Use

- Designing fault-tolerant quantum memory in higher dimensions
- Building modular quantum error correction architectures
- Analyzing tradeoffs between code distance, rate, and energy barrier
- Understanding BPT bounds and their achievability
- Quantum network patch design for distributed quantum computing

## Design Patterns

### Pattern 1: Dimensional Lifting
1. Start with a good D-dimensional qLDPC code
2. Apply Layer code construction with color routing
3. Obtain (D+1)-dimensional code with improved parameters
4. Energy barrier scales as Δ · n^{1/D}

### Pattern 2: BPT-Optimal Design
1. Choose input qLDPC code that approaches BPT bounds in D dimensions
2. Apply Layer construction → automatically saturates (D+1)-dimensional BPT bounds
3. Verify: [[n^{(D+1)/D}, k, d^{(D+1)/D}]] parameters

### Pattern 3: Modular Network Architecture
1. Decompose physical layout into network patches
2. Map each patch to a module of the Layer code
3. Use color routing to define inter-patch connections
4. Logical operations commute across patch boundaries

## Mathematical Framework

### CSS Code Construction
- X and Z checks defined on different dimensional structures
- Color assignment partitions checks into non-interfering groups
- Line defects resolved through careful color-to-dimension mapping

### Energy Barrier
- Original D-dim code: energy barrier Δ
- Layer construction: Δ' = Δ · n^{1/D}
- For constant Δ input: barrier grows as n^{1/D}

### Code Parameters
From D-dim qLDPC [[n, k, d]] with barrier Δ:
- (D+1)-dim Layer code: [[n^{(D+1)/D}, k, d^{(D+1)/D}]]
- Energy barrier: Δ · n^{1/D}
- BPT bound: saturated for good qLDPC inputs

## Implementation Considerations

1. **Input code selection**: Good qLDPC codes (asymptotically good) are required for BPT saturation
2. **Color assignment**: Must be consistent across all check layers
3. **Line defect resolution**: Color routing handles crossings that previously blocked generalization
4. **Modular deployment**: Each module can be implemented on separate hardware patches

## Related Concepts

- qLDPC codes (quantum low-density parity-check)
- CSS codes (Calderbank-Shor-Steane)
- BPT bounds (Bravyi-Poulin-Terhal)
- Layer codes (original 3D construction)
- Quantum memory and fault tolerance
- Topological quantum error correction

## References

- arXiv:2605.18961 — "4D and 5D Layer Codes through Color Routing" (Yuan & Baspin, May 2026)
- Categories: quant-ph, cs.IT, math-ph
