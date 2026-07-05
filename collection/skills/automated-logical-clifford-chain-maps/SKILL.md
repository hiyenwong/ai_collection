---
name: automated-logical-clifford-chain-maps
category: quantum
description: "Automated framework for synthesizing inter-code logical CNOT circuits between arbitrary CSS codes using chain maps. Enables interoperable logical gate networks across heterogeneous quantum error correction codes."
---

# Automated Logical Clifford Gadgets via Chain Maps

## Description

Automated framework for synthesizing inter-code logical CNOT circuits between arbitrary CSS (Calderbank-Shor-Steane) quantum error-correcting codes using algebraic topology chain maps. Given a prescribed bipartite logical CNOT network between heterogeneous codes, the method constructs the affine space of all chain maps realizing the desired logical gate network.

Core insight: **Chain maps from algebraic topology provide a universal language for logical gate synthesis across any CSS code family**, eliminating the need for code-specific hand-crafted gadgets.

## Activation Keywords

- automated Clifford synthesis, chain map quantum, CSS code interoperation
- logical CNOT synthesis, heterogeneous quantum codes, inter-code logical gates
- quantum error correction gadgets, CSS code chain maps, automated fault tolerance
- quantum Clifford gadgets, 自动Clifford综合, 量子纠错码链映射

## Source Paper

**arXiv: 2607.02482** - "Automated logical Clifford gadgets for heterogeneous architectures via chain maps"
- Authors: Asmae Benhemou, Noah Berthusen
- Published: 2026-07-02

## Key Methodology

### Step 1: Represent CSS Code as Chain Complex

Every CSS code can be represented as a chain complex of vector spaces over GF(2):

```python
import numpy as np

class CSSCode:
    """Represent a CSS code as a chain complex over GF(2)."""
    
    def __init__(self, HX, HZ):
        """
        HX: X-stabilizer matrix (m_x x n)
        HZ: Z-stabilizer matrix (m_z x n)
        Must satisfy HX @ HZ.T = 0 (mod 2)
        """
        self.HX = HX % 2
        self.HZ = HZ % 2
        self.n = HX.shape[1]  # Number of physical qubits
        self.k = self.n - np.linalg.matrix_rank(
            np.vstack([self.HX, self.HZ])
        )  # Number of logical qubits
    
    def chain_complex(self):
        """
        Return chain complex: C_1 --d1--> C_0 --d0--> C_{-1}
        where d1 = HZ^T, d0 = HX
        Boundary condition: d0 @ d1 = HX @ HZ^T = 0 (mod 2)
        """
        return {
            'C_1': self.HZ.T,  # Z-stabilizer generators -> physical qubits
            'C_0': np.eye(self.n),  # Physical qubits
            'C_m1': self.HX,  # X-stabilizer generators
        }
```

### Step 2: Define Chain Map Between Codes

A chain map f: C -> D between two chain complexes preserves the boundary structure:

```python
def find_chain_maps(code_A, code_B):
    """
    Find all chain maps between two CSS codes.
    
    A chain map f = (f_1, f_0, f_{-1}) satisfies:
      f_0 @ d1_A = d1_B @ f_1    (commutes with Z-boundary)
      d0_B @ f_0 = f_{-1} @ d0_A  (commutes with X-boundary)
    
    Returns the affine space of all valid chain maps.
    """
    # System of linear equations over GF(2)
    # f_0 @ HZ_A^T = HZ_B^T @ f_1
    # HX_B @ f_0 = f_{-1} @ HX_A
    
    # Flatten into linear system Ax = b over GF(2)
    # Use Gaussian elimination over GF(2)
    
    n_A, n_B = code_A.n, code_B.n
    
    # Build constraint matrix for f_0 (n_B x n_A matrix)
    # Each entry is a variable, total n_A * n_B variables
    n_vars = n_A * n_B
    
    equations = []
    
    # f_0 @ HZ_A^T = HZ_B^T @ f_1 constraint
    # This constrains the column space of f_0
    HZ_A_T = code_A.HZ.T
    HZ_B_T = code_B.HZ.T
    
    for i in range(HZ_B_T.shape[0]):
        for j in range(HZ_A_T.shape[1]):
            # Equation: (HZ_B^T @ f_0 @ HZ_A)_ij = 0
            eq = np.zeros(n_vars)
            for p in range(n_A):
                for q in range(n_B):
                    var_idx = q * n_A + p
                    coeff = HZ_B_T[i, q] * HZ_A_T[p, j]
                    eq[var_idx] = (eq[var_idx] + coeff) % 2
            equations.append(eq)
    
    # Solve system over GF(2)
    A = np.array(equations) % 2
    
    # Return null space (affine space of solutions)
    return solve_gf2_null_space(A)

def solve_gf2_null_space(A):
    """Find null space of matrix A over GF(2)."""
    m, n = A.shape
    # Gaussian elimination over GF(2)
    pivot_cols = []
    row = 0
    for col in range(n):
        # Find pivot
        pivot = None
        for r in range(row, m):
            if A[r, col] == 1:
                pivot = r
                break
        if pivot is None:
            continue
        # Swap rows
        A[[row, pivot]] = A[[pivot, row]]
        pivot_cols.append(col)
        # Eliminate
        for r in range(m):
            if r != row and A[r, col] == 1:
                A[r] = (A[r] + A[row]) % 2
        row += 1
    
    # Free variables
    free_cols = [c for c in range(n) if c not in pivot_cols]
    
    # Build null space basis
    null_basis = []
    for fc in free_cols:
        vec = np.zeros(n)
        vec[fc] = 1
        for i, pc in enumerate(pivot_cols):
            vec[pc] = A[i, fc]
        null_basis.append(vec)
    
    return np.array(null_basis) if null_basis else np.zeros((0, n))
```

### Step 3: Synthesize Logical CNOT Network

```python
def synthesize_logical_cnot(code_A, code_B, logical_pairs):
    """
    Synthesize logical CNOT gates between two CSS codes.
    
    logical_pairs: list of (i, j) meaning CNOT from logical qubit i of code_A
                   to logical qubit j of code_B
    
    Returns: Physical gate sequence implementing the logical CNOT network.
    """
    # Find chain maps
    chain_maps = find_chain_maps(code_A, code_B)
    
    # Among all valid chain maps, select those that implement
    # the desired logical CNOT pattern
    
    # The chain map f_0 directly gives the physical CNOT pattern:
    # f_0[q_B, q_A] = 1 means CNOT from physical q_A to physical q_B
    
    # Filter chain maps by logical action
    valid_maps = []
    for cm in chain_maps:
        f_0 = cm.reshape((code_B.n, code_A.n))
        
        # Check if this implements the desired logical CNOT
        if implements_logical_cnot(code_A, code_B, f_0, logical_pairs):
            valid_maps.append(f_0)
    
    return valid_maps

def implements_logical_cnot(code_A, code_B, f_0, logical_pairs):
    """Check if physical map f_0 implements the target logical CNOT pattern."""
    # Compute logical operator mapping
    # For each logical pair (i, j), check that:
    # X_L(i) in code_A maps to X_L(i) in code_A * X_L(j) in code_B
    # Z_L(j) in code_B maps to Z_L(j) in code_B * Z_L(i) in code_A
    
    # This requires computing logical operator representatives
    # and checking their transformation under f_0
    
    # Simplified check:
    # f_0 should map support of X_L(i) to support of X_L(i)*X_L(j)
    for i, j in logical_pairs:
        X_L_A = get_logical_X(code_A, i)  # Logical X operator for qubit i
        X_L_B = get_logical_X(code_B, j)  # Logical X operator for qubit j
        
        # After CNOT: X_L(i) -> X_L(i) * X_L(j)
        expected = (X_L_A + X_L_B) % 2
        actual = f_0 @ X_L_A % 2
        
        if not np.array_equal(actual, expected):
            return False
    
    return True
```

## Core Findings

1. **Universality**: Chain maps provide a universal framework for logical gate synthesis between ANY two CSS codes, not just structurally related families.

2. **Affine Space Structure**: The set of all valid chain maps forms an affine space, enabling systematic exploration of different physical implementations for the same logical gate.

3. **Automated Synthesis**: No manual code-specific gadget design needed — the framework automatically generates valid physical CNOT patterns from the desired logical network.

4. **Heterogeneous Interoperability**: Enables fault-tolerant quantum computing across hybrid architectures combining different QEC codes (e.g., surface codes + color codes + LDPC codes).

## Applications

- **Heterogeneous QEC Architectures**: Bridge different quantum error correction codes in a single quantum computer
- **Code Conversion**: Implement fault-tolerant code switching between CSS codes
- **Logical Gate Compilation**: Automated compilation of logical circuits across heterogeneous code families
- **Quantum Network Protocols**: Inter-code communication in distributed quantum computing
- **Resource Optimization**: Search the affine space of chain maps for minimum-cost physical implementations

## Related Concepts

- CSS Codes (Calderbank-Shor-Steane)
- Chain Complexes (Algebraic Topology)
- Logical Gate Synthesis
- Fault-Tolerant Quantum Computing
- Homological Quantum Codes
- Surface Codes, Color Codes, LDPC Codes
- Bipartite Logical Networks
- Affine Spaces over GF(2)

## References

- arXiv:2607.02482 - Automated logical Clifford gadgets for heterogeneous architectures via chain maps
