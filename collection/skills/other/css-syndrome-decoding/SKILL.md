---
name: css-syndrome-decoding
description: "Factor-graph formulation of CSS quantum error correction syndrome decoding using joint belief propagation and four-state BP. Enables efficient classical decoding for CSS codes."
---

# CSS Syndrome Decoding via Factor Graphs

## Description
Factor-graph based approach to CSS (Calderbank-Shor-Steane) code syndrome decoding. Formulates the posterior probability of Pauli errors as a binary factor graph with two Tanner graphs coupled by local joint priors. Implements sum-product (belief propagation) algorithms including Joint BP and Four-State BP for efficient decoding.

Based on: Kasai. "A Factor-Graph Formulation of CSS Syndrome Decoding: Joint BP and Four-State BP" (arXiv: 2605.05132)

## Activation Keywords
- css syndrome decoding
- quantum error correction decoding
- factor graph decoding
- belief propagation QEC
- CSS code decoder
- Tanner graph quantum
- 量子纠错解码
- CSS码译码

## Core Concepts

### CSS Codes
- CSS codes constructed from two classical linear codes C_X and C_Z
- X-type and Z-type stabilizers measured separately
- Syndrome = (s_X, s_Z) from measurement outcomes
- Decoding: find most likely error given syndrome

### Factor Graph Representation
- Binary factor graph with two Tanner graphs
- X-check Tanner graph for X errors (coupled to s_X)
- Z-check Tanner graph for Z errors (coupled to s_Z)
- Coupling: local joint prior at each qubit (Pauli errors are not independent)

### Belief Propagation (BP)
- Sum-product algorithm on factor graph
- Messages: probability distributions over error states
- Joint BP: processes X and Z errors simultaneously
- Four-State BP: handles all four Pauli states (I, X, Y, Z) at each qubit

## Key Patterns

### Pattern 1: Factor Graph Construction
1. Build X-check Tanner graph from H_X parity check matrix
2. Build Z-check Tanner graph from H_Z parity check matrix
3. Add qubit nodes connecting both graphs
4. Initialize priors based on error model (depolarizing, biased, etc.)

### Pattern 2: Joint Belief Propagation
1. Initialize messages from priors
2. Iterate: check-to-variable → variable-to-check messages
3. Coupling step: update joint distribution at each qubit
4. Marginalize to get most likely error configuration
5. Check convergence (syndrome satisfied or max iterations)

### Pattern 3: Four-State BP
1. Track full Pauli distribution {I, X, Y, Z} at each qubit
2. Messages are 4-dimensional probability vectors
3. Check nodes process X and Z constraints separately
4. Qubit nodes combine X and Z information into joint Pauli state
5. More accurate than independent X/Z decoding (handles Y = XZ correlation)

## Implementation Guide

### Step 1: CSS Code Definition
```python
import numpy as np

class CSSCode:
    def __init__(self, H_X, H_Z):
        self.H_X = np.array(H_X)  # X-check matrix (m_X × n)
        self.H_Z = np.array(H_Z)  # Z-check matrix (m_Z × n)
        self.n = H_X.shape[1]      # number of qubits
        # Verify CSS condition: H_X @ H_Z^T = 0 (mod 2)
        assert np.all((self.H_X @ self.H_Z.T) % 2 == 0)
    
    def syndrome(self, error_X, error_Z):
        s_X = (self.H_X @ error_X) % 2
        s_Z = (self.H_Z @ error_Z) % 2
        return s_X, s_Z
```

### Step 2: Factor Graph Construction
```python
def build_factor_graph(css_code):
    """Build factor graph for CSS syndrome decoding."""
    H_X, H_Z = css_code.H_X, css_code.H_Z
    n = css_code.n
    
    # Variable nodes: n qubits
    # Check nodes: m_X X-checks + m_Z Z-checks
    # Edges: from H_X and H_Z nonzero entries
    
    factor_graph = {
        'qubit_nodes': list(range(n)),
        'x_check_nodes': list(range(n, n + H_X.shape[0])),
        'z_check_nodes': list(range(n + H_X.shape[0], n + H_X.shape[0] + H_Z.shape[0])),
        'edges_x': np.argwhere(H_X),
        'edges_z': np.argwhere(H_Z) + [0, H_X.shape[0]],
    }
    return factor_graph
```

### Step 3: Joint BP Decoder
```python
def joint_bp_decode(css_code, syndrome_X, syndrome_Z, 
                    p_error=0.01, max_iter=50):
    """Joint BP decoder for CSS codes."""
    n = css_code.n
    
    # Initialize beliefs
    # P(X error) = p_error / 3 (for each X, Y, Z in depolarizing)
    # P(no error) = 1 - p_error
    
    beliefs_X = np.full(n, p_error / 3)
    beliefs_Z = np.full(n, p_error / 3)
    
    for iteration in range(max_iter):
        # Variable-to-check messages
        # Check-to-variable messages
        # Update beliefs
        
        # Coupling: update joint distribution
        # P(I), P(X), P(Z), P(Y) at each qubit
        
        # Check convergence
        if syndrome_satisfied(css_code, beliefs_X, beliefs_Z, 
                             syndrome_X, syndrome_Z):
            break
    
    # Decode: threshold beliefs
    error_X = (beliefs_X > 0.5).astype(int)
    error_Z = (beliefs_Z > 0.5).astype(int)
    
    return error_X, error_Z
```

### Step 4: Four-State BP Decoder
```python
def four_state_bp_decode(css_code, syndrome_X, syndrome_Z,
                         p_error=0.01, max_iter=50):
    """Four-state BP decoder tracking full Pauli distribution."""
    n = css_code.n
    
    # State space: {I, X, Z, Y}
    # beliefs[i] = [P(I), P(X), P(Z), P(Y)] at qubit i
    beliefs = np.zeros((n, 4))
    beliefs[:, 0] = 1 - p_error  # P(I)
    beliefs[:, 1:] = p_error / 3  # P(X), P(Z), P(Y)
    
    for iteration in range(max_iter):
        # X-check processing (affects X and Y components)
        # Z-check processing (affects Z and Y components)
        # Joint update at qubit nodes
        
        pass
    
    # Decode: most likely state at each qubit
    decoded = np.argmax(beliefs, axis=1)
    return decoded
```

## Tools Used
- python: Decoder implementation
- numpy: Linear algebra, probability
- scipy: Sparse matrix operations for large codes
- stim: Quantum circuit simulation for testing
- pymatching: Alternative minimum-weight perfect matching decoder

## Error Handling
- If BP doesn't converge: use BP+OSD (ordered statistics decoding)
- For degenerate codes: use BP+MLD hybrid approach
- If factor graph has many short cycles: use belief propagation with damping

## Related Skills
- quantum-error-correction-methods
- quantum-fault-tolerance-verification
- quantum-ml-patterns

## References
- arXiv: 2605.05132 - Factor-Graph CSS Syndrome Decoding
- CSS Codes: Calderbank et al., IEEE Trans. IT 44, 1369 (1998)
- BP for QEC: Poulin & Chung, QIC 8, 085 (2008)
