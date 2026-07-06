---
name: automated-logical-clifford-chain-maps
description: "Automated framework for synthesizing inter-code logical Clifford (CNOT/CZ) gates between arbitrary CSS quantum error-correcting codes using chain maps — recovers known transversal constructions and finds new low-depth solutions for heterogeneous QEC architectures."
---

# Automated Logical Clifford Gadgets for Heterogeneous Architectures via Chain Maps

## Description

A methodology for automated synthesis of inter-code logical Clifford gates (CNOT, CZ) between arbitrary CSS quantum error-correcting codes using homological chain maps. Given a prescribed bipartite logical gate network between CSS codes, the method constructs the affine space of chain maps realizing the desired logical action, then searches this space for shallow and sparse physical circuit candidates. Applicable to code switching, magic-state injection, Pauli product measurements, and operations on concatenated codes. Based on arXiv:2607.02482 (Benhemou & Berthusen, 2026).

## Activation Keywords

- automated logical Clifford gadgets
- chain map QEC synthesis
- inter-code logical CNOT
- CSS code interface synthesis
- heterogeneous QEC architectures
- logical Clifford gate synthesis
- automated Clifford gadgets
- chain map quantum error correction
- 逻辑 Clifford 门合成
- CSS 码接口合成

## Tools Used

- exec: Run Python scripts for chain map construction and circuit search
- read: Read code definitions (parity check matrices), CSS code specifications
- write: Output synthesized circuits, chain maps, and circuit diagrams

## Usage Patterns

### Code Switching Interface Design
Given two CSS codes (e.g., surface code and color code), synthesize the minimum-depth physical circuit implementing logical CNOT between them.

### Magic-State Injection
Synthesize low-depth circuits for injecting magic states across heterogeneous code families with distance-preserving guarantees.

### Concatenated Code Operations
Design bespoke chain maps for logical operations on concatenated code structures, optimizing spacetime tradeoffs.

## Instructions for Agents

### Step 1: Define Input Codes

Parse the CSS code specifications:
- X and Z parity check matrices (H_X, H_Z) for each code
- Logical operator representatives (X_L, Z_L) for each code
- Target logical gate network (which qubits need CNOT/CZ connections)

### Step 2: Construct Chain Map Affine Space

1. **Formulate chain complexes**: Represent each CSS code as a chain complex C_1 → C_0 → C_{-1} with boundary maps derived from parity check matrices.
2. **Define target logical action**: Specify the bipartite logical gate network as a set of desired logical CNOT/CZ mappings between codes.
3. **Solve chain map equations**: The chain map f must satisfy:
   - ∂ ∘ f = f ∘ ∂ (commutes with boundary maps)
   - f maps logical operators to correct targets modulo stabilizers
   - This defines an affine subspace of valid chain maps.

### Step 3: Search for Optimal Physical Circuits

1. **Parameterize the affine space**: Find a particular solution + homogeneous solutions.
2. **Optimize for depth**: Among all valid chain maps, search for those minimizing:
   - Circuit depth (number of time steps)
   - Gate count (sparsity of the circuit)
   - CNOT count
3. **Use sparse recovery**: Apply l_0/l_1 minimization to find sparse chain maps corresponding to shallow circuits.

### Step 4: Validate and Enhance

1. **Check distance preservation**: Verify the synthesized circuit preserves code distance, or document partial distance preservation.
2. **Add flag measurements**: For distance-preserving variants, add minimal flag qubit measurements.
3. **Generate circuit diagram**: Output the physical gate sequence with qubit mappings.

### Step 5: Benchmark

Compare against:
- Known transversal constructions (should recover these as special cases)
- Code-specific ad-hoc constructions
- Spacetime volume metrics

## Key Mathematical Concepts

### Chain Maps for CSS Codes

A CSS code corresponds to a chain complex:
```
C_1 → C_0 → C_{-1}
```
where C_0 represents physical qubits, C_1 represents X-stabilizers, and C_{-1} represents Z-stabilizers.

A chain map between two CSS codes is a collection of linear maps that commute with the boundary operators. The space of such maps forms an affine space when constrained to implement specific logical operations.

### Affine Space Construction

Given codes A and B with parity checks (H_X^A, H_Z^A) and (H_X^B, H_Z^B), and target logical gate L:
1. Solve: H_X^B ∘ f = f ∘ H_X^A (X-boundary commutation)
2. Solve: H_Z^B ∘ f = f ∘ H_Z^A (Z-boundary commutation)
3. Constrain: f(X_L^A) = X_L^B (logical action)
4. The solution space is affine: f = f_particular + Σ α_i · f_homogeneous_i

### Sparse Recovery

The circuit depth correlates with the sparsity of the chain map matrix. Use:
- L1 minimization (basis pursuit) for convex relaxation
- Greedy sparse recovery for larger codes
- Iterative pruning to reduce gate count

## Error Handling

### No Valid Chain Map Found
If the affine space is empty for the target logical action:
- Relax the target: allow approximate logical gates with bounded error
- Increase code distance or add ancilla qubits
- Fall back to code switching via intermediate codes

### Circuit Too Deep
If the optimal chain map yields unacceptable depth:
- Apply circuit optimization passes (gate cancellation, commutation)
- Use flag qubit measurements to reduce distance requirements
- Consider alternative code pairs

### Distance Not Preserved
- Document the distance degradation
- Add flag measurements to recover full distance
- Use the partial-distance-preserving variant with appropriate error bounds

## Examples

### Example 1: Surface Code to Color Code CNOT

Input:
- Code A: [[7,1,3]] Steane code (color code)
- Code B: [[5,1,3]] surface code patch
- Target: Logical CNOT between logical qubits

Output:
- Chain map matrix (sparse, low-depth)
- Physical CNOT gate sequence (7 gates, depth 3)
- Verification: distance preserved with 2 flag measurements

### Example 2: Magic-State Injection

Input:
- Source: Small non-Clifford resource state
- Target: Large surface code patch
- Target gate: Logical T-gate via magic-state injection

Output:
- Chain map implementing state injection
- Spacetime volume: 12 qubit-steps (vs 48 for naive approach)

## Resources

- arXiv:2607.02482 — "Automated logical Clifford gadgets for heterogeneous architectures via chain maps" (Benhemou & Berthusen, 2026)
- Homological algebra for quantum error correction (standard reference)
- CSS code theory and stabilizer formalism

## Related Skills

- `automated-logical-clifford-chain-maps` — umbrella skill
- `quantum-error-correction-methods` — general QEC patterns
- `distributed-quantum-error-correction` — distributed QEC systems
- `quantum-compiler-routing` — qubit routing and compilation
