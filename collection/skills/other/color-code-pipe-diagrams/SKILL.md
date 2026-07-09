---
name: color-code-pipe-diagrams
description: "Lattice surgery compilation methodology for color codes using pipe diagrams — extends surface-code pipe diagram framework to triangular color codes on 6.6.6 lattice. Enables distance-independent spacetime optimization, correlation surface realization, and automated compilation to syndrome extraction circuits."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2607.05501"
  published: "2026-07-06"
  authors: "Laura S. Herzog, Gilad Kishony, Robert Wille, Austin Fowler"
  tags: [quantum, qec, lattice-surgery, color-code, pipe-diagram, compilation]
---

# Color Code Pipe Diagrams

## Description
Extends pipe diagram lattice surgery compilation from surface codes to **triangular color codes** on 6.6.6 lattice. Color codes offer reduced qubit overhead and transversal single-qubit Clifford gates vs surface codes, but lacked analogous spacetime optimization framework. Provides foundation for automated lattice surgery compilation and diagrammatic optimization in color code FTQC architectures.

## Activation Keywords
- color code pipe diagrams
- lattice surgery color code
- color code compilation
- 6.6.6 lattice
- color code spacetime optimization
- pipe diagram quantum
- ZX diagram color code
- 彩色码管道图

## Core Concepts

### Why Color Codes vs Surface Codes
| Property | Surface Code | Color Code (6.6.6) |
|----------|-------------|-------------------|
| Qubit overhead | Higher | Lower |
| Transversal Cliffords | Limited | Full set |
| Lattice surgery framework | Established (pipe diagrams) | **This paper** |
| Spacetime optimization | Mature | **New contribution** |

### Pipe Diagram Framework for Color Codes
1. **Representation**: Map triangular color code on 6.6.6 lattice to pipe diagrams
2. **ZX correspondence**: Establish correspondence between color code pipes and ZX-diagrammatic computation
3. **Distance-independent constructions**: Correlation surfaces, stabilizers, syndrome extraction circuits
4. **Compact spacetime embeddings**: Leverage color code geometry for efficient logical computation layouts

### Key Results (arXiv:2607.05501)
- First pipe diagram representation for triangular color code on 6.6.6 lattice
- Distance-independent constructions of correlation surfaces and stabilizers
- Explicit syndrome extraction circuit realizations
- Demonstrated potential for compact spacetime embeddings
- Foundation for automated color code lattice surgery compilation

## Instructions for Agents

### Step 1: Problem Selection
- Identify if target QEC code is surface code or color code
- For color codes, use pipe diagram framework (not surface code pipe diagrams)
- Assess qubit overhead tradeoff: color codes use fewer physical qubits per logical

### Step 2: Pipe Diagram Construction
1. Map color code lattice (6.6.6) to pipe representation
2. Establish ZX-diagrammatic correspondence for logical operations
3. Construct distance-independent pipe diagrams for target computation

### Step 3: Spacetime Optimization
1. Design compact spacetime embeddings using color code geometry
2. Optimize correlation surface layouts
3. Compile to executable syndrome extraction circuits

### Step 4: Verification
- Verify correlation surfaces match expected logical behavior
- Check stabilizer measurement patterns
- Validate syndrome extraction circuit correctness

## Error Handling
- **No established framework for target code**: Surface code pipe diagrams ≠ color code pipe diagrams — different lattice geometry requires different constructions
- **ZX-diagram mismatch**: Color code ZX correspondence differs from surface code; verify mapping before optimization

## Related Skills
- lattice-surgery-surface-code — Surface code lattice surgery (different code, different pipe diagrams)
- distributed-quantum-error-correction — Distributed QEC patterns
- quantum-fault-tolerance-benchmark — QEC benchmarking
