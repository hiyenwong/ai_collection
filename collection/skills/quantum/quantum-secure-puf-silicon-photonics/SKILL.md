---
name: quantum-secure-puf-silicon-photonics
description: "Quantum readout protocol methodology for Physical Unclonable Functions (PUFs) using silicon photonics integrated circuits. Combines single-photon states with Mach-Zehnder interferometer mesh PUFs for hardware security authentication with equal error rates as low as 10^-14. Activation: quantum PUF, physical unclonable function, silicon photonics security, quantum authentication, hardware security primitive."
category: information-science
tags: ["quantum", "security", "hardware", "photonics", "PUF", "authentication", "silicon"]
related_skills: ["quantum-secure-networks", "post-quantum-cryptographic-protocol-analysis"]
source_paper: "arXiv:2605.14959"
---

# Quantum-Secure PUF via Silicon Photonics

Quantum readout protocol methodology for Physical Unclonable Functions (PUFs) using silicon nitride (SiN) programmable photonic Mach-Zehnder interferometer meshes. Combines single-photon quantum states with hardware PUFs for ultra-high security authentication.

## Source

**Paper**: "Quantum-Secure Physical Unclonable Function enabled by Silicon Photonics Integrated Circuits"
**Authors**: G. Sarantoglou, N. Tzekas, G. Moustakas, G.A. Karydis, V. Kaminski, E. Protsenko, K. Gradkowski, A. Bazin, C. Vigliar, A. Bogris, C. Mesaritakis
**arXiv**: [2605.14959](https://arxiv.org/abs/2605.14959) (May 2026)
**Journal**: Submitted to IEEE JLT
**Categories**: physics.optics, quant-ph

## Core Concepts

### What is a PUF?

A Physical Unclonable Function exploits inherent physical complexity from manufacturing variations to create a unique, unclonable hardware fingerprint. Each device has uncontrollable microscopic variations that serve as a secret signature.

### Quantum Readout Innovation

Traditional PUFs use classical light for challenge-response. This paper introduces **quantum readout** using single-photon states:

1. **Maximally mixed quantum states** conceal the underlying unitary transformation from passive eavesdropping
2. **Single-photon detection** provides quantum-level security guarantees
3. **Monte Carlo analysis** of false acceptance/rejection rates as a function of detected events

### Architecture

```
Challenge (classical) → SiN MZI Mesh → Quantum State Preparation → Single-Photon Detection → Response (quantum)
                                ↑
                    Unitary transformation from
                    fabrication variations (secret)
```

**Silicon Nitride (SiN) Mach-Zehnder Interferometer (MZI) Mesh**:
- Programmable photonic circuit implementing unitary transformation
- Fabrication variations create unique, unclonable transformation per device
- Compatible with standard CMOS fabrication processes
- Suitable for quantum and AI applications

## Security Analysis

### Threat Model

| Threat | Countermeasure |
|--------|---------------|
| Passive eavesdropping | Maximally mixed quantum states conceal unitary transformation |
| Cloning attack | Uncontrollable fabrication variations are physically unclonable |
| Similar-device attack | Monte Carlo analysis quantifies security against devices from same fab |
| Challenge-response interception | Quantum no-cloning theorem prevents state duplication |

### Performance Metrics

- **Equal Error Rate (EER)**: As low as **10^-14** — exceptional authentication accuracy
- **False Acceptance Rate (FAR)**: Decreases with number of detected events
- **False Rejection Rate (FRR)**: Trade-off with FAR based on error correction threshold
- **Number of detected events**: Primary parameter controlling security level

### Monte Carlo Security Assessment

```python
# Security evaluation framework (from paper methodology)
def evaluate_puf_security(num_events, num_errors_corrected, num_simulated_devices):
    """
    Evaluate PUF authentication performance via Monte Carlo simulation.
    
    Args:
        num_events: Number of single-photon detection events
        num_errors_corrected: Error correction capacity
        num_simulated_devices: Number of adversary devices from same fab conditions
    
    Returns:
        FAR: False Acceptance Rate
        FRR: False Rejection Rate
        EER: Equal Error Rate (where FAR == FRR)
    """
    # Simulate legitimate device responses
    legitimate_responses = simulate_quantum_responses(
        num_events, device_type="legitimate"
    )
    
    # Simulate adversary device responses (same fab conditions)
    adversary_responses = simulate_quantum_responses(
        num_events, device_type="adversary", num_devices=num_simulated_devices
    )
    
    # Calculate overlap distributions
    far = calculate_false_acceptance(legitimate_responses, adversary_responses)
    frr = calculate_false_rejection(legitimate_responses, threshold)
    
    return far, frr, equal_error_rate(far, frr)
```

## Implementation Guidelines

### Hardware Requirements

1. **SiN MZI Mesh**: Silicon nitride programmable photonic circuit
   - Standard CMOS-compatible fabrication
   - Multiple MZI stages for sufficient unitary complexity
   - Phase shifters for programmability

2. **Single-Photon Source**: 
   - Weak coherent pulse or true single-photon source
   - Compatible wavelengths with SiN waveguides (typically 1550nm)

3. **Single-Photon Detectors**:
   - Superconducting nanowire or avalanche photodiode detectors
   - Low dark count rate for high signal-to-noise ratio

### Protocol Steps

1. **Enrollment Phase**:
   - Characterize device response to challenge set
   - Store reference response template securely

2. **Authentication Phase**:
   - Send classical challenge to PUF device
   - Prepare maximally mixed quantum input state
   - Measure single-photon output
   - Compare response to enrolled template

3. **Error Correction**:
   - Apply error correction to account for environmental variations
   - Adjust threshold based on desired security level

## Integration Patterns

### Pattern 1: Hardware Root of Trust

Use quantum PUF as hardware root of trust in secure systems:
- Device authentication before key release
- Secure boot chain verification
- Tamper-evident hardware attestation

### Pattern 2: Quantum Key Distribution Enhancement

Integrate quantum PUF with QKD systems:
- PUF-based authentication prevents man-in-the-middle on QKD classical channel
- Complementary security layers (information-theoretic + hardware-based)

### Pattern 3: IoT Device Authentication

Lightweight hardware authentication for IoT:
- No secret key storage needed (physical variation IS the secret)
- Resistant to physical cloning attacks
- Compatible with silicon photonics for integrated systems

## Advantages Over Classical PUFs

| Feature | Classical PUF | Quantum PUF (this method) |
|---------|--------------|--------------------------|
| Eavesdropping resistance | Limited | Quantum-level (no-cloning theorem) |
| Cloning resistance | Physical difficulty | Fundamental physics |
| Error rate | ~10^-6 to 10^-9 | ~10^-14 |
| Modeling attack resistance | ML-vulnerable | Quantum state complexity |

## Pitfalls

- **Fabrication tolerance**: Requires sufficiently high fabrication variation for uniqueness, but low enough for device functionality
- **Environmental sensitivity**: Temperature and stress variations affect MZI phase — requires environmental compensation or error correction
- **Single-photon source quality**: Imperfect single-photon sources reduce security guarantees
- **Detector dark counts**: High dark count rates increase false rejection rates
- **Scalability**: MZI mesh complexity scales with number of ports — practical limits on challenge space size
- **CMOS compatibility**: SiN process must be compatible with existing foundry processes for cost-effective production

## Activation

Use this skill when:
- Designing hardware security primitives with quantum-level guarantees
- Evaluating Physical Unclonable Functions for high-security applications
- Integrating silicon photonics into security architectures
- Comparing classical vs. quantum authentication methods
- Building tamper-resistant hardware root of trust systems
- Researching quantum-classical hybrid security protocols
