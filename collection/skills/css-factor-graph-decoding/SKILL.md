---
name: css-factor-graph-decoding
description: "Factor-graph formulation for CSS quantum error correction syndrome decoding using Joint BP and Four-State BP algorithms. Use when implementing or analyzing quantum error correction decoders, CSS code syndrome processing, factor-graph based decoding, belief propagation for quantum codes, or when working with stabilizer codes and quantum LDPC codes."
---

# CSS Factor-Graph Syndrome Decoding

Methodology from Kasai (2026) "A Factor-Graph Formulation of CSS Syndrome Decoding: Joint BP and Four-State BP" (arXiv:2605.05132).

## Core Insight

CSS codes decompose Pauli errors into X and Z components, each constrained by separate parity-check matrices (H_X, H_Z). The joint posterior forms a binary factor graph with **two coupled Tanner graphs** linked by local joint priors at each qubit.

## Two Algorithms

### 1. Joint BP (Belief Propagation)

- Runs standard sum-product on the coupled factor graph
- X and Z components processed simultaneously
- Messages passed between both Tanner graphs via joint prior
- Equivalent to maximum a posteriori (MAP) estimation under independence assumptions

### 2. Four-State BP

- Treats each qubit error as a 4-state variable: {I, X, Y, Z}
- Single factor graph with 4-ary variables instead of binary pairs
- Captures X-Z correlation explicitly in message structure
- More accurate than Joint BP for codes with X-Z correlations

## When to Use

| Scenario | Recommended |
|----------|-------------|
| Standard CSS code, no X-Z correlation | Joint BP |
| Code with X-Z correlated errors | Four-State BP |
| Fast decoding needed | Joint BP (parallelizable) |
| Maximum accuracy | Four-State BP |

## Implementation Pattern

```python
def css_factor_graph_decode(syndrome_x, syndrome_z, H_x, H_z, method="joint_bp"):
    """
    Decode CSS code using factor-graph BP.
    
    Args:
        syndrome_x: X-syndrome measurements (binary vector)
        syndrome_z: Z-syndrome measurements (binary vector)  
        H_x: X-check matrix (binary)
        H_z: Z-check matrix (binary)
        method: "joint_bp" or "four_state_bp"
    
    Returns:
        Estimated Pauli error (string of I/X/Y/Z)
    """
    # 1. Build coupled Tanner graph
    #    - Variable nodes: qubits (N nodes)
    #    - Check nodes: H_x checks + H_z checks
    #    - Edges: from H_x and H_z structure
    
    # 2. Initialize messages
    #    - Prior at each qubit based on channel model
    #    - Joint prior couples X and Z components
    
    # 3. Run sum-product iterations
    #    - Variable-to-check messages
    #    - Check-to-variable messages (parity constraints)
    #    - Joint prior updates between X/Z components
    
    # 4. Marginalize to get error estimate
    #    - Most likely Pauli error per qubit
    
    pass
```

## Key Advantages

1. **Unified framework**: Both X and Z decoding in one graph
2. **Correlation capture**: Four-State BP handles X-Z error correlations
3. **Parallelizable**: Joint BP naturally parallel across qubits
4. **Extensible**: Framework extends to non-CSS codes

## Pitfalls

- Joint BP assumes X-Z independence; degrades when errors are correlated
- Four-State BP has 4x message complexity vs binary BP
- Convergence not guaranteed for graphs with short cycles
- Need proper scheduling (flooding vs layered) for convergence

## Related Concepts

- CSS codes: Calderbank-Shor-Steane quantum error correction codes
- Tanner graphs: Bipartite graph representation of parity-check codes
- Sum-product algorithm: Belief propagation on factor graphs
- Quantum LDPC: Low-density parity-check quantum codes

## Activation Keywords

- CSS decoding, syndrome decoding, quantum error correction
- factor graph decoding, belief propagation quantum
- Joint BP, Four-State BP, quantum LDPC decoding
- stabilizer code decoding, Pauli error correction
