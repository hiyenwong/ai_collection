---
name: quantum-verifiable-blind-computing
description: "Comparative analysis and design framework for verifiable blind quantum computing (VBQC) client architectures. Covers emission-based, measurement-based, and rotation-based client designs with single-server, single-client protocols using measurement-based quantum computation. Evaluates security proofs, protocol execution rates, error behavior, and hardware cost trade-offs. Activation: verifiable blind quantum computing, VBQC client architecture, blind quantum computation, quantum client design, quantum cloud security, verifiable quantum delegation."
metadata:
  arxiv_id: "2607.05650"
  published: "2026-07-09"
  tags: [quantum, blind-computing, verifiability, client-architecture, systems-engineering, security]
---

# Verifiable Blind Quantum Computing Client Architectures

## Description

Framework for selecting and comparing client architectures in verifiable blind quantum computing (VBQC), where a client delegates quantum computations to a remote server without revealing input, computation, or output, while also verifying correct execution.

## Client Architecture Categories

### 1. Emission-Based Clients
- Client prepares and sends quantum states to server
- Server performs measurements and returns classical results
- **Hardware**: Requires quantum state preparation capability (e.g., single-photon source)
- **Security**: Information-theoretic security based on measurement-based quantum computation (MBQC)

### 2. Measurement-Based Clients
- Client performs measurements on qubits returned by server
- Server prepares entangled resource states
- **Hardware**: Requires quantum measurement capability only
- **Trade-off**: Lower hardware complexity than emission-based, but requires quantum communication in both directions

### 3. Rotation-Based Clients
- Client applies rotations to qubits before/after server processing
- Server performs entangling operations
- **Hardware**: Requires quantum rotation gates on client side
- **Trade-off**: Intermediate complexity between emission and measurement-based

## Evaluation Dimensions

### Security Guarantees
- **Blindness**: Server learns nothing about input, computation, or output
- **Verifiability**: Client can detect if server deviates from protocol
- **Information-theoretic security**: Security does not depend on computational assumptions

### Protocol Execution Rate
- Each architecture has different rates at which protocol rounds can be executed
- Rate equations depend on: communication latency, quantum operation speed, classical processing overhead
- Emission-based typically fastest (one-way communication), measurement-based slowest (two-way)

### Error Behavior
- Different architectures have different error propagation characteristics
- Emission-based: errors introduced at preparation stage
- Measurement-based: errors introduced at measurement stage
- Rotation-based: errors compound through rotation operations

### Hardware Cost
- Emission-based: highest (quantum state preparation)
- Measurement-based: medium (quantum measurement only)
- Rotation-based: medium-high (quantum rotation gates)

## Usage Patterns

### Pattern 1: Architecture Selection for Matter-Qubit Server
1. Identify server type (matter-qubit vs. photonic)
2. Determine available client-side quantum capabilities
3. Evaluate security requirements (blindness only vs. verifiability)
4. Compare protocol execution rates for target application
5. Select architecture minimizing hardware cost while meeting security and performance requirements

### Pattern 2: Security Proof Verification
1. Identify the specific VBQC protocol variant
2. Check that the security proof covers the chosen client architecture
3. Verify assumptions about server capabilities and adversarial model
4. Ensure protocol parameters (number of trap qubits, verification rounds) meet target security level

## Pitfalls

- **Protocol-server mismatch**: Some security proofs assume specific server capabilities. Verify compatibility between client architecture proof and actual server implementation.
- **Rate underestimation**: Protocol execution rate equations often assume ideal conditions. Add 20-50% margin for real-world overhead from classical communication latency and error correction.
- **Hardware over-specification**: Don't assume emission-based is always best. For many applications, measurement-based provides sufficient security at lower hardware cost.
- **Single-server limitation**: This framework covers single-server, single-client protocols only. Multi-server or multi-client VBQC requires different analysis.

## Related Skills

- `quantum-verification-cryptographic` — classical verification of quantum computation
- `blind-quantum-computation` — blind quantum computing protocols
- `quantum-network-security` — security patterns for quantum networks
