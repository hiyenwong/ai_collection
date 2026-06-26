---
name: quantum-group-codes-non-clifford
description: "Quantum group codes methodology using classical quasi group codes to define CSS codes supporting transversal multi-control-Z gates with addressable and parallelizable non-Clifford logic. Leverages class field theory from number theory for code construction with quasi-quadratic decoding."
---

# Quantum Group Codes for Non-Clifford Logic

## Description
Methodology for constructing quantum CSS codes from classical quasi group codes that support transversal multi-control-Z (C^mZ) gates which are both addressable and parallelizable. Uses algebraic geometry (AG) codes lifted via class field theory to build codes with improved decoding complexity (quasi-quadratic vs cubic) and enables efficient magic-state distillation.

## Activation Keywords
- quantum group codes
- non-Clifford logic
- transversal gates
- class field theory quantum codes
- AG codes quantum
- magic state distillation
- CSS codes non-Clifford
- quasi group codes
- 量子群码
- 非Clifford逻辑
- 横截面门

## Tools Used
- read: Read paper abstracts and existing skill documentation
- terminal: Run quantum circuit simulations and code analysis
- write: Create SKILL.md and reference documentation
- web_search: Search for related quantum error correction literature

## Core Concepts

### Classical Quasi Group Codes
- **Foundation**: Classical quasi group codes defined over finite fields F_q
- **Property**: Codes where the product is associative up to an invertible normalized cocycle
- **Application**: Define quantum CSS codes via the standard CSS construction from classical codes

### Transversal Multi-Control-Z Gates
- **C^mZ Gate**: Multi-controlled Z gate applied transversally at the logical level
- **Addressability**: Individual qubits can be targeted independently
- **Parallelizability**: Multiple C^{m-1}Z gates can be executed simultaneously
- **Advantage**: Avoids need for costly magic-state distillation for each gate

### Algebraic Geometry Code Lifting
- **Input**: Good quantum AG code over F_q with transversal C^mZ gate
- **Lifting Procedure**: Applied to underlying classical AG code using class field theory
- **Output**: Quantum group code over F_{q^2} supporting transversal C^mZ and parallelizable C^{m-1}Z
- **Decoding Complexity**: Quasi-quadratic time decoder with linear decoding radius (vs cubic for previous quantum AG codes)

### Number Theory Connection (Class Field Theory)
- **Ray Class Fields**: Used to construct the lifting procedure
- **Stark Units**: May enter SIC overlaps in the construction (related to arXiv:2606.23535)
- **Maximal Rings of Integers**: Attached to ray class fields for code parameters

## Usage Patterns

### Pattern 1: Non-Clifford Gate Implementation
When implementing non-Clifford gates in fault-tolerant quantum computing:
1. Start with a classical quasi group code over F_q
2. Apply the lifting procedure via class field theory
3. Obtain quantum group code over F_{q^2} with transversal C^mZ
4. Verify addressability and parallelizability of C^{m-1}Z gates
5. Use quasi-quadratic decoder for error correction

### Pattern 2: Magic-State Distillation Optimization
When optimizing magic-state distillation protocols:
1. Identify the C^mZ gate depth requirements
2. Select quantum group codes with appropriate m parameter
3. Leverage parallelizable C^{m-1}Z gates to reduce circuit depth
4. Achieve almost linear speedup over state-of-the-art protocols

### Pattern 3: Class Field Theory Code Construction
When constructing quantum codes from number-theoretic objects:
1. Select base field F_q and target extension F_{q^2}
2. Identify appropriate ray class field for the construction
3. Apply AG code lifting procedure
4. Verify code parameters (distance, rate, transversality)
5. Analyze decoding complexity (target: quasi-quadratic)

## Mathematical Framework

### CSS Code Construction
```
Classical quasi group code C ⊆ F_q^n
    ↓ (lifting via class field theory)
Quantum group code Q ⊆ F_{q^2}^{2n}
    ↓ (CSS construction)
[[n, k, d]]_q quantum code with transversal C^mZ
```

### Decoding Complexity
- Previous quantum AG codes: O(n^3) decoder
- Quantum group codes: O(n^2 log^c n) quasi-quadratic decoder
- Decoding radius: Linear in code distance

## Error Handling
### Code Parameter Selection
- If code distance is too small: Increase extension degree or base field size
- If decoding fails: Verify quasi-quadratic decoder assumptions hold
- If transversality not achieved: Check class field theory lifting conditions

## References
- arXiv:2606.27211 - Quantum group codes for non-Clifford logic (Gasnier, Guémard 2026)
- arXiv:2606.23535 - How Stark units enter SIC overlaps (related number theory)
- Quantum error correction: CSS code construction
- Class field theory: Ray class fields and Stark units
