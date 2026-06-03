---
name: partial-qec-metrology
description: "Partial Quantum Error Correction (QEC) for quantum metrology methodology. Uses subset of stabilizer checks to suppress local noise while maintaining super-SQL sensing performance, avoiding full QEC overhead. Applicable to quantum sensing, error-corrected metrology, NISQ sensing protocols. Activation: partial QEC metrology, quantum metrology error correction, super-SQL sensing, quantum sensing with QEC, QEC-assisted metrology, stabilizer check subset sensing, quantum error correction metrology."
---

# Partial QEC Metrology

Methodology for error-corrected quantum metrology using **partial** quantum error correction (QEC) — a subset of stabilizer checks suffices to suppress local noise while maintaining super-standard-quantum-limit (super-SQL) sensing performance.

## Core Principle

Standard QEC-assisted metrology requires full error correction (measuring all checks) to restore the Heisenberg limit. Partial QEC shows that encoding probe states into superpositions of energetically different states of the underlying quantum code allows error correction using only a **subset of checks** to suppress noise both before and after phase imprinting.

## Key Results

For noise parallel to phase imprinter of operator weight $l$:
- Noise suppression factor: $p^\delta$ where $p$ is noise strength
- $\delta = \lfloor (l+1)/2 \rfloor$
- Super-SQL performance maintained as system scales

## Workflow

### Step 1: Choose Quantum Code

Select a quantum error-correcting code with appropriate distance:
- Stabilizer code with check operators $\{S_i\}$
- Code distance $d$ determines noise suppression capability

### Step 2: Design Probe States

Encode probe states as superpositions of energetically different states:
$$|\psi\rangle = \alpha |E_1\rangle + \beta |E_2\rangle$$
- Energy gap between states provides phase sensitivity
- Check which subset of stabilizers is needed for noise suppression

### Step 3: Identify Minimal Check Subset

For noise of weight $l$ parallel to phase imprinter:
1. Compute $\delta = \lfloor (l+1)/2 \rfloor$
2. Select minimum check subset achieving $p^\delta$ suppression
3. Verify checks are local operators (avoid non-local connectivity)

### Step 4: Adaptive Weight-Increasing Strategy

To maintain super-SQL as system scales:
1. Monitor noise suppression performance
2. Increase imprinter weight adaptively
3. Trade off between phase sensitivity and noise resilience

### Step 5: Noise Analysis

Analyze tradeoff between:
- Number of checks measured (resource cost)
- Noise suppression achieved
- Phase estimation precision (Fisher information)

## Implementation

### Stabilizer Check Selection

```python
def select_minimal_checks(stabilizers, noise_operators, target_delta):
    """Select minimal subset of stabilizer checks for noise suppression."""
    # For each noise operator of weight l:
    # delta = floor((l+1)/2)
    # Need checks that anticommute with noise operators
    # Minimize number of checks while achieving target_delta
    pass
```

### Fisher Information Analysis

```python
def compute_fisher_info(partial_checks, noise_strength, imprinter_weight):
    """Compute quantum Fisher information under partial QEC."""
    delta = (imprinter_weight + 1) // 2
    suppression = noise_strength ** delta
    # QFI scales with suppression factor
    return suppression
```

## Advantages over Full QEC

1. **Reduced overhead**: Fewer measurements needed
2. **Local operations**: All checks are local operators
3. **NISQ-compatible**: Lower circuit depth requirements
4. **Scalable**: Adaptive strategy maintains performance at scale

## Use Cases

- Quantum sensing in noisy environments
- NISQ-era metrology protocols
- Distributed quantum sensor networks
- Quantum clock synchronization
- Magnetic field sensing with error mitigation

## Related Skills

- `quantum-statistical-metrology`: General quantum metrology patterns
- `quantum-noise-robust-metrology`: Robust frequency estimation
- `distributed-quantum-error-correction`: Distributed QEC patterns
- `composite-quantum-gates-error-cancellation`: Error cancellation methods

## References

- arXiv:2605.08341 — Chen, Wang, Zhou (2026)
- PRL 112, 080801 (2014) — Kessler et al. full QEC metrology
- PRL 112, 150802 (2014) — Arrad et al. full QEC metrology
