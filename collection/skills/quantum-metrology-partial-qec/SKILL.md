---
name: quantum-metrology-partial-qec
description: "Quantum metrology enhanced by partial quantum error correction — using incomplete QEC codes to protect phase estimation and sensing precision beyond the standard quantum limit. Activation: quantum metrology, partial QEC sensing, phase estimation error correction, quantum sensing precision."
---

# Quantum Metrology via Partial Quantum Error Correction

## Description
Quantum metrology methodology using partial quantum error correction (QEC) to enhance sensing precision. Instead of full fault-tolerant QEC, leverages incomplete/partial error correction codes that protect the sensing subspace while allowing signal accumulation. Applicable to atomic clocks, magnetometry, and gravitational wave detection.

## Activation Keywords
- quantum metrology partial QEC
- phase estimation error correction
- quantum sensing precision
- QEC-enhanced metrology
- quantum sensor noise protection
- 量子精密测量纠错
- partial QEC sensing
- quantum magnetometry QEC

## Tools Used
- **terminal**: Run quantum sensing simulations
- **execute_code**: Implement partial QEC protocols in Python/Qiskit
- **web_search**: Find latest quantum metrology research

## Core Concepts

### Partial QEC for Metrology
- **Full QEC blocks signals**: Traditional QEC protects against ALL errors, including the signal itself
- **Partial QEC targets noise only**: Design codes that correct dominant noise while preserving signal subspace
- **Signal-to-noise enhancement**: Achieve precision scaling between SQL (1/√N) and HL (1/N)

### Protocol Design
1. **Noise Identification**: Characterize dominant noise channel (dephasing, amplitude damping, etc.)
2. **Signal Subspace Isolation**: Encode sensing state in subspace orthogonal to noise
3. **Partial Syndrome Measurement**: Measure only error syndromes that don't collapse signal
4. **Recovery with Signal Preservation**: Apply correction operators that maintain signal phase

### Mathematical Framework
```
Encoding: |ψ⟩ → U_enc |ψ⟩
Signal: U_φ = exp(-iφH) accumulates phase φ
Noise: Λ(ρ) = Σ K_i ρ K_i† (Kraus operators)
Syndrome: S = {projectors detecting noise, not signal}
Recovery: R(S) that inverts Λ without removing φ
```

### Code Families
- **Repetition Codes**: Protect against bit-flip while preserving phase sensing
- **Bosonic Codes**: GKP and cat codes for continuous-variable metrology
- **Stabilizer Codes**: Tailored stabilizers that commute with signal Hamiltonian
- **Dynamical Decoupling**: Time-domain partial correction via pulse sequences

## Implementation Pattern

### Step 1: Noise Characterization
```python
def characterize_noise(system, n_samples=1000):
    """Identify dominant noise channel for sensing system."""
    # Measure T1, T2, readout errors
    t1 = measure_relaxation(system, n_samples)
    t2 = measure_dephasing(system, n_samples)
    
    if t2 << t1:
        return "dephasing_dominant"
    elif t1 < 2*t2:
        return "relaxation_dominant"
    return "mixed_noise"
```

### Step 2: Partial QEC Code Design
```python
def design_partial_qec(noise_type, n_qubits=5):
    """Design partial QEC code for sensing."""
    if noise_type == "dephasing_dominant":
        # Use phase-flip code, preserve X-basis sensing
        return phase_flip_code(n_qubits)
    elif noise_type == "relaxation_dominant":
        # Use amplitude-damping code with signal subspace
        return amp_damping_code(n_qubits)
```

### Step 3: Metrology Protocol
```python
def partial_qec_metrology(state, phi, code, noise_model, n_rounds):
    """Enhanced metrology with partial QEC."""
    # Encode
    encoded = code.encode(state)
    
    for _ in range(n_rounds):
        # Signal accumulation
        encoded = apply_signal(encoded, phi)
        # Noise
        encoded = apply_noise(encoded, noise_model)
        # Partial correction (only correct noise, not signal)
        encoded = code.partial_correct(encoded)
    
    # Decode and measure
    decoded = code.decode(encoded)
    return measure_phase(decoded)
```

## Applications
- **Atomic Clocks**: Extend coherence time beyond physical T2
- **Magnetometry**: NV-center enhanced sensing with error protection
- **Gravitational Waves**: Optomechanical sensor noise suppression
- **Biological Sensing**: Quantum-enhanced biosensing in noisy environments

## Pitfalls
- **Over-Correction**: Full QEC removes the signal — verify partial code preserves signal Hamiltonian
- **Syndrome Extraction Overhead**: Measurement must be fast compared to signal accumulation
- **Code Distance Trade-off**: Higher distance = better noise protection but fewer logical qubits for sensing
- **Hardware Constraints**: Partial QEC requires fast mid-circuit measurement and feed-forward

## Verification
- Simulate Fisher Information: partial QEC should show enhanced FI vs unprotected
- Check SQL vs HL scaling: verify precision scaling improves toward 1/N
- Compare with dynamical decoupling: partial QEC should outperform DD for structured noise

## References
- arXiv:2605.08341 — Quantum metrology via partial quantum error correction
- Related: quantum Fisher information, Cramér-Rao bound, quantum advantage in sensing

## Related Skills
- `quantum-noise-robust-metrology` — Quantum metrology for robust frequency estimation
- `quantum-sensor-reliability` — Quantum sensor network reliability via RL optimization
- `spintune-quantum-sensor-reliability` — RL-based dynamical decoupling optimization
