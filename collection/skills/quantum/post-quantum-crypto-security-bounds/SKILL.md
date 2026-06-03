---
name: post-quantum-crypto-security-bounds
description: Tight quantum-security bounds and parameter optimization for NIST PQC finalists SPHINCS+ and NTRU. Covers quantum attack modeling with decoherence effects, entropy concentration inequalities, and lattice parameter optimization using quantum lattice entropy. Use when evaluating post-quantum cryptography security, optimizing PQC parameters, or analyzing quantum-resistant cryptosystems.
---

# Post-Quantum Crypto Security Bounds

## Description

Establishes tight security bounds for NIST PQC finalists SPHINCS+ (hash-based) and NTRU (lattice-based) under quantum attack models. Incorporates realistic quantum hardware constraints including decoherence and parallelization limits.

## Activation Keywords

- post-quantum cryptography security
- SPHINCS+ parameter optimization
- NTRU lattice security
- quantum attack modeling
- PQC security bounds
- quantum lattice entropy
- decoherence-aware security
- 后量子密码安全界
- NIST PQC evaluation
- quantum-resistant parameters

## Tools Used

- exec: Run security bound calculations
- read: Access cryptographic parameter tables
- write: Generate security reports

## Core Analysis Framework

### Quantum Attack Model

Incorporates realistic quantum constraints:

1. **Decoherence Time (τ_d)**: Limits circuit depth
2. **Parallelization Limits**: Qubit availability constraints
3. **Gate Error Rates**: Affects Grover/quantum search success
4. **Memory Constraints**: Classical-quantum interface limits

### SPHINCS+ Optimization

- **Entropy Concentration**: New inequalities reduce parameters by 15-20%
- **Hash Tree Depth**: Optimal depth vs security tradeoff
- **Signature Size**: Minimize while maintaining security level
- **Quantum Security Level**: NIST Level 1/3/5 under quantum attacks

### NTRU Parameter Optimization

- **Quantum Lattice Entropy**: H_Q(Λ) characterizes lattice hardness
- **Dimension Selection**: Optimal n for security/performance
- **Modulus Optimization**: q selection for quantum resistance
- **Decoding Radius**: Impact on quantum attack complexity

## Security Analysis Patterns

### SPHINCS+ Security Calculation

```python
def sphincs_quantum_security(n, h, d, tau_d):
    """Calculate quantum security level for SPHINCS+
    
    Args:
        n: Hash output length
        h: Tree height
        d: Layers
        tau_d: Decoherence time
    """
    # Classical security
    classical = min(n, h)
    
    # Quantum reduction (Grover)
    quantum_grover = classical / 2
    
    # Decoherence-limited security
    quantum_real = min(quantum_grover, tau_d * clock_rate)
    
    return quantum_real
```

### NTRU Lattice Security

```python
def ntru_quantum_security(n, q, tau_d):
    """Calculate quantum security for NTRU lattice
    
    Args:
        n: Lattice dimension
        q: Modulus
        tau_d: Decoherence time
    """
    # Quantum lattice entropy
    H_Q = quantum_lattice_entropy(n, q)
    
    # BKZ quantum complexity
    bkz_quantum = quantum_bkz_complexity(n, H_Q)
    
    # Decoherence constraint
    security = min(bkz_quantum, tau_d_based_bound(tau_d))
    
    return security
```

## Security Parameters

| Scheme | Classical Bits | Quantum Bits (Ideal) | Quantum Bits (Realistic) |
|--------|---------------|---------------------|-------------------------|
| SPHINCS+ Level 1 | 128 | 64 | 80-100 |
| SPHINCS+ Level 3 | 192 | 96 | 120-150 |
| SPHINCS+ Level 5 | 256 | 128 | 160-200 |
| NTRU Level 1 | 128 | 64 | 85-110 |
| NTRU Level 3 | 192 | 96 | 130-160 |
| NTRU Level 5 | 256 | 128 | 170-210 |

## Error Handling

### Invalid Parameters

If parameters don't meet security requirements:
- Increase dimension/hash length
- Verify quantum attack model assumptions
- Check decoherence time estimates

### Security Bound Calculation Failure

If bounds cannot be computed:
- Verify input parameter ranges
- Check mathematical assumptions
- Use conservative default values

## References

- arXiv:2508.19250 - Tight Quantum-Security Bounds for SPHINCS+ and NTRU
- NIST PQC Standardization Process
- Quantum lattice reduction algorithms
