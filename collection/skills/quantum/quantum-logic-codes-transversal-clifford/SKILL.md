---
name: quantum-logic-codes-transversal-clifford
description: "Quantum Logic Codes methodology — high-rate non-LDPC CSS codes with complete depth-one/constant-depth transversal logical Clifford ISA. Constructs [[n,sqrt(n),Theta(n^beta)]] code families (beta~0.2823) possessing individually targeted S-bar, sqrt(X)-bar, and CZ-bar transversal gates. Tiling and concatenation preserve the depth-one ISA at scale. arXiv: 2606.13521"
category: quantum/error-correction
metadata:
  arxiv_id: "2606.13521"
  authors: "Adam Holmes"
  subjects: "quant-ph,math-ph"
  published_date: "2026-06-11"
---

## Context

Achieving universal transversal logical gates on quantum error-correcting codes remains a fundamental challenge. The Eastin-Knill theorem forbids universal transversal gate sets for any stabilizer code. Quantum Logic Codes break new ground by constructing a high-rate CSS code family that achieves a **complete transversal logical Clifford basis ISA** — S-bar, sqrt(X)-bar, and CZ-bar — all at depth-one (or constant-depth) for certain subfamilies.

## Core Methodology

### Code Family Parameters

The code family has parameters `[[n, sqrt(n), Theta(n^beta)]]` where:
- `n`: Physical qubits
- `sqrt(n)`: Logical qubits (high rate)
- `Theta(n^beta)`: Distance with `beta ≈ 0.2823` in demonstrated case

### Complete Transversal Logical Clifford Basis ISA

The code family possesses a constant-depth complete 2-local transversal logical Clifford basis instruction set architecture composed of:
- **S-bar gate**: Phase gate on each logical qubit, depth-one
- **sqrt(X)-bar gate**: Hadamard-equivalent, depth-one  
- **CZ-bar gate**: Controlled-Z between logical qubits, depth-one for odd distances and lengths L>=3

### Construction from Core Codes

1. **Base Code**: Start from a small `[[n_0, 2, d_0]]` code
2. **Tiling**: Tile out to form utility-scale logical qubit counts
3. **Concatenation**: Scale up through concatenation for higher distances and error suppression
4. **ISA Preservation**: The construction preserves the depth-one complete transversal logical Clifford basis ISA when composed with tiling and concatenation
5. **Scaling**: At scale, the complete logical Clifford basis ISA remains depth-one up to depth-two addressable operations between tiled cores

### Universal Lower Bounds

The work identifies universal lower bounds on circuit depth to generate a full logical Clifford algebra, establishing the theoretical foundation for why the construction achieves its efficiency.

### Novel Gate Constructions

- **Depth-one transversal S-bar in rotated surface code**: New construction
- **Depth-one intra-block CZ-bar in 2D-toric code**: Generalizes to all odd distances and all lengths L>=3

## Implementation Steps

### Step 1: Core Code Selection
```
Input: Target code parameters (n_0, k_0, d_0)
Output: Base CSS code with required structure

Requirements:
- Small code with [[n_0, 2, d_0]] parameters
- Compatible with transversal S-bar, sqrt(X)-bar, CZ-bar
```

### Step 2: Transversal Gate Verification
- Verify the core code supports all three transversal gates individually
- Check depth-one property for each gate
- Verify commutation relations for the Clifford algebra

### Step 3: Tiling Construction
```
Input: Core code, target logical qubit count
Output: Tiled code with sqrt(n) logical qubits

Process:
1. Tile core codes in 2D/3D lattice arrangement
2. Verify transversal gates compose correctly across tiles
3. Check that depth-one property is preserved
```

### Step 4: Concatenation for Distance Scaling
```
Input: Tiled code, target distance
Output: Concatenated code with Theta(n^beta) distance

Process:
1. Apply recursive concatenation
2. Verify ISA preservation at each level
3. Verify distance scaling follows Theta(n^beta)
```

### Step 5: Logical Clifford ISA Assembly
```
The complete logical Clifford basis ISA:
- S-bar: Apply to any logical qubit individually (depth-one)
- sqrt(X)-bar = H-bar: Apply to any logical qubit individually (depth-one)  
- CZ-bar: Apply between any pair of logical qubits (depth-one/constant-depth)

Combined with state injection (for T-gate), this gives universal quantum computation.
```

## Pitfalls

- **Non-LDPC Nature**: The codes are explicitly non-LDPC, meaning check weights grow with code size. **Implication**: Syndrome extraction is more complex than for LDPC codes. **Fix**: Design syndrome extraction circuits that exploit the structured check patterns.
- **Constant-Depth vs. Depth-One**: Depth-one holds for certain subfamilies; others achieve constant-depth. **Clarification**: "Constant-depth" means independent of code size but may be >1.
- **Addressable Operations**: Between tiled cores, operations may require depth-two addressing. **Implication**: Multi-tile logical operations need careful scheduling. **Fix**: Use depth-two addressable operations as a primitive.
- **Beta Parameter**: The demonstrated beta ≈ 0.2823 may not be optimal. **Implication**: Distance scaling could potentially be improved. **Fix**: Explore alternative core code constructions.
- **Eastin-Knill Compliance**: The construction respects Eastin-Knill by providing only the Clifford group (not universal). T-gate requires state injection or other non-transversal methods.

## Verification

1. **Code Parameters**: Verify `[[n, sqrt(n), Theta(n^beta)]]` scaling numerically for specific instances.
2. **Transversal Gates**: Verify each gate (S-bar, sqrt(X)-bar, CZ-bar) acts correctly on the code space.
3. **Depth Bounds**: Confirm the universal lower bounds on circuit depth for Clifford algebra generation.
4. **ISA Completeness**: Verify the three gates generate the full logical Clifford group.
5. **Scaling Preservation**: Verify ISA preservation through concatenation levels.

## Activation

quantum logic codes, transversal logical Clifford gates, high-rate CSS codes, depth-one logical gates, stabilizer quantum error correction, logical Clifford ISA, rotated surface code transversal gates, 2D toric code transversal CZ, non-LDPC CSS codes, code concatenation fault tolerance, complete Clifford basis transversal, quantum error correction instruction set architecture