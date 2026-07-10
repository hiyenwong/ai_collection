---
name: quantum-information-protocol-analyzer
description: "Analyze quantum information protocols (QKD, quantum cryptography, quantum communication) from research papers. Extract protocol design patterns, security analysis methods, and implementation guidelines. Triggered by: quantum protocol, QKD analysis, quantum cryptography, quantum communication protocol, 量子协议分析, quantum information security."
---

# Quantum Information Protocol Analyzer

## Description

Analyzes quantum information protocols from academic papers, extracting reusable patterns for:
- **QKD protocols** (BB84, E91, decoy-state, CV-QKD)
- **Quantum cryptography** (quantum secret sharing, quantum digital signatures)
- **Quantum communication** (quantum teleportation, quantum dense coding)
- **Security analysis methods** (information-theoretic security, entanglement-based security)

## Related Protocols

### Quantum Subliminal Learning (arXiv:2605.29557)
**Pattern**: Quantum science and machine learning convergence paradigm. Explores learning mechanisms operating below classical detection thresholds using quantum states.
- ML as physical science — ML principles rooted in physical quantum phenomena
- Subliminal information processing — quantum states enable learning beyond classical detection
- Superconducting quantum circuits as hardware foundation for quantum-classical learning
- Entanglement-enhanced information transfer for learning acceleration
**Trigger**: quantum ML convergence, quantum information science, subliminal learning, quantum-classical fusion

## Activation Keywords

- quantum protocol analysis
- QKD analysis
- quantum cryptography
- quantum communication protocol
- 量子协议分析
- quantum information security
- quantum secret sharing
- quantum network protocol

## Tools Used

- `read`: Read research papers, SKILL.md files
- `write`: Create analysis reports, protocol summaries
- `exec`: Run protocol simulation scripts
- `web_search`: Search for latest quantum protocol papers
- `web_fetch`: Fetch paper content from arxiv/Semantic Scholar

## Core Protocol Types

### 1. Quantum Key Distribution (QKD)

| Protocol | Mechanism | Security Basis | Key Rate |
|----------|-----------|----------------|----------|
| **BB84** | Single photon encoding | Uncertainty principle | ~1 kbps |
| **E91** | Entanglement-based | Bell inequality | ~100 bps |
| **Decoy-state** | Decoy pulses | Photon number statistics | ~10 Mbps |
| **CV-QKD** | Continuous variables | Gaussian modulation | ~100 Mbps |

### 2. Quantum Cryptography

- **Quantum Secret Sharing**: Split secrets using quantum entanglement
- **Quantum Digital Signatures**: Unforgeable signatures via quantum states
- **Quantum Money**: Quantum state-based currency verification

### 3. Quantum Communication

- **Quantum Teleportation**: Transfer quantum states without physical transfer
- **Quantum Dense Coding**: Send 2 bits via 1 qubit with entanglement
- **Quantum Error Correction**: Protect quantum information from decoherence

## Analysis Workflow

### Step 1: Protocol Identification

```python
def identify_protocol(paper):
    """Identify protocol type from paper content."""
    
    keywords = {
        'QKD': ['key distribution', 'BB84', 'E91', 'decoy', 'CV-QKD'],
        'Secret Sharing': ['secret sharing', 'quantum sharing'],
        'Digital Signature': ['digital signature', 'quantum signature'],
        'Teleportation': ['teleportation', 'state transfer'],
        'Error Correction': ['error correction', 'QECC', 'surface code']
    }
    
    for protocol_type, terms in keywords.items():
        if any(term in paper.lower() for term in terms):
            return protocol_type
    
    return 'General Quantum Protocol'
```

### Step 2: Extract Protocol Components

For each identified protocol, extract:

1. **Input requirements**: Quantum resources needed (qubits, entanglement, channels)
2. **Process steps**: Quantum operations sequence
3. **Output metrics**: Key rate, fidelity, security level
4. **Security assumptions**: Trust models, adversarial capabilities
5. **Implementation challenges**: Hardware requirements, error tolerance

### Step 3: Security Analysis Extraction

```markdown
## Security Analysis Framework

### Information-Theoretic Security
- Shannon entropy analysis
- Mutual information bounds
- Holevo bound application

### Composability
- Sequential composition
- Parallel composition
- Universal composability framework

### Attack Models
- Individual attacks
- Collective attacks
- Coherent attacks
- Side-channel attacks
```

### Step 4: Implementation Guidelines

Extract practical implementation notes:

- **Hardware requirements**: Photon sources, detectors, channels
- **Error thresholds**: Maximum tolerable error rates
- **Distance limits**: Maximum transmission distance
- **Rate optimization**: Parameter tuning for key rate

## Protocol Pattern Extraction

### Pattern 1: Prepare-and-Measure QKD

```
1. Alice prepares quantum states (random basis choice)
   |ψ⟩ ∈ {|0⟩, |1⟩, |+⟩, |−⟩} for BB84
   
2. Alice sends to Bob via quantum channel
   
3. Bob measures (random basis choice)
   
4. Public discussion: basis reconciliation
   
5. Error estimation: sample subset
   
6. Privacy amplification: extract secure key
   
7. Authentication: classical channel security
```

### Pattern 2: Entanglement-Based Protocol

```
1. Entangled state preparation (EPR pairs)
   |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
   
2. Distribution to Alice and Bob
   
3. Measurement in chosen bases
   
4. Bell test for security verification
   
5. Key extraction from correlated outcomes
   
6. Entanglement purification (if needed)
```

### Pattern 3: Quantum Secret Sharing

```
1. Secret encoding into quantum state
   
2. State distribution to multiple parties
   
3. Access structure: authorized subsets can reconstruct
   
4. Security: unauthorized subsets get no information
   
5. Reconstruction via quantum operations
   
6. Verification of secret integrity
```

## Output Format

### Protocol Analysis Report

```markdown
# Quantum Protocol Analysis: [Protocol Name]

## Source Paper
- **Title**: [Paper title]
- **arxiv ID**: [arxiv ID]
- **Authors**: [Authors]

## Protocol Overview
- **Type**: [QKD/Cryptography/Communication]
- **Mechanism**: [Brief description]
- **Security Basis**: [Information-theoretic/Computational]

## Protocol Specification

### Parameters
| Parameter | Value | Description |
|-----------|-------|-------------|
| Key length | N bits | Target key size |
| Error threshold | 11% | Maximum QBER |
| Distance | 100 km | Transmission distance |

### Quantum Operations
1. [Step 1 description]
2. [Step 2 description]
...

### Classical Post-Processing
1. [Reconciliation method]
2. [Privacy amplification]
3. [Authentication]

## Security Analysis

### Information Bounds
- **Holevo bound**: χ ≤ S(ρ) - ∑ p_x S(ρ_x)
- **Key rate**: r = I(A:B) - I(A:E)

### Attack Resistance
- [Individual attacks]: [Analysis]
- [Collective attacks]: [Analysis]
- [Coherent attacks]: [Analysis]

## Implementation Notes

### Hardware Requirements
- [Photon source type]
- [Detector specifications]
- [Channel requirements]

### Practical Challenges
- [Challenge 1]
- [Challenge 2]

## Reusable Patterns

### Pattern: [Pattern name]
[Pattern description]

### Applicability
[Where this pattern can be reused]

## Related Protocols
- [Protocol 1]: [Similarity]
- [Protocol 2]: [Difference]
```

## Research Integration

### Adding to Knowledge Graph

```python
# Add protocol to kg.db
kg_tool.add-entity kg.db protocol "[Protocol Name]"
kg_tool.add-entity kg.db paper "[Paper Title]"

# Create relations
kg_tool.add-relation kg.db paper_id protocol_id "has_protocol"

# Add keywords
kg_tool.add-entity kg.db keyword "[key terms]"
kg_tool.add-relation kg.db protocol_id keyword_id "has_keyword"
```

### Vector Embedding

```python
# Generate embedding for protocol description
embedding = embedding_model.encode(protocol_summary)

# Store in kg_vectors
INSERT INTO kg_vectors (entity_id, embedding)
VALUES (protocol_id, embedding_blob)
```

## Best Practices

1. **Prioritize security analysis**: Quantum protocols are primarily security tools
2. **Extract implementation constraints**: Practical limits are crucial
3. **Compare with classical alternatives**: Highlight quantum advantages
4. **Note hardware requirements**: Implementation feasibility depends on this
5. **Track parameter ranges**: Optimal values affect performance

## Extended Scope: Quantum Channel Capacity Analysis (2026-06-28)

This skill now also covers **quantum channel capacity analysis** as a fundamental metric for evaluating protocol feasibility:

### Quantum Capacity via Symmetry (arXiv: 2605.09138)
- **quantum-capacity-symmetry** — Optimizing quantum channel capacity thresholds using representation-theoretic symmetry
  - First improvement in depolarizing channel capacity threshold in 18 years
  - Coherent information optimization over symmetric subspaces
  - Kraus operator annihilation → environment entropy reduction via code degeneracy
  - **Trigger**: quantum capacity, depolarizing channel, coherent information optimization

### Capacity-Aware Protocol Design
When designing or analyzing quantum communication protocols:
1. Check channel capacity bounds (hashing bound, symmetry-enhanced bounds)
2. Identify if channel has exploitable symmetries (unitary covariance, permutation invariance)
3. Compute coherent information over symmetric subspaces for improved rates
4. Use capacity results to determine feasible transmission rates and error thresholds

## Extended Scope: Post-Quantum & Information-Theoretic Security (2026-05-31)

This skill's scope has been broadened beyond purely quantum protocols to include **post-quantum cryptographic deployment** and **information-theoretic privacy protocols** that serve the same security goals in the quantum-threat landscape.

### Post-Quantum Cryptography (PQC) Deployment
- **quantum-safe-6g-pqc-evaluation** (arXiv: 2605.06881) — NIST PQC benchmarking for 6G/IoT networks
  - ML-KEM/Kyber, ML-DSA/Dilithium, Falcon size expansion analysis
  - Three deployment patterns: hybrid handshake, size-optimized, asynchronous PQC
  - Key insight: ciphertext/signature size (not computation) is the bottleneck

### Quantum Hardware Security
- **quantum-secure-puf-silicon-photonics** (arXiv: 2605.14959) — Quantum readout PUFs using SiN MZI meshes
  - Single-photon states + maximally mixed input for eavesdropper concealment
  - EER as low as 10^-14 via Monte Carlo security analysis
  - CMOS-compatible fabrication for scalable deployment

### Information-Theoretic Privacy
- **dpf-error-detecting-pir-rings** (arXiv: 2604.00411) — DPF-based IT-PIR over rings
  - Distributed Point Functions with algebraic error detection
  - Ring-based construction more efficient than field-based
  - Multi-server with adversarial tolerance

### Unified Security Taxonomy

| Layer | Protocol Type | Example | Security Model |
|-------|--------------|---------|---------------|
| Quantum | QKD, quantum teleportation | BB84, E91 | Information-theoretic (quantum physics) |
| Post-Quantum | Lattice-based, code-based | ML-KEM, ML-DSA | Computational (hardness assumptions) |
| Hardware | PUFs, quantum readout | SiN MZI mesh PUF | Physical unclonability + quantum states |
| Information-Theoretic | IT-PIR, DPF | Ring-based PIR | Information-theoretic (no computational assumptions) |

## Related Skills

- **quantum-network-protocol-designer**: Design new quantum protocols
- **quantum-finance-analysis**: Quantum applications in finance
- **quantum-algorithm-implementation-guide**: Implement quantum algorithms
- **post-quantum-cryptographic-protocol-analysis**: PQC protocol design and analysis
- **quantum-resistant-networks**: Post-quantum network architecture
- **quantum-safe-6g-pqc-evaluation**: NIST PQC deployment evaluation for 6G/IoT
- **quantum-secure-puf-silicon-photonics**: Quantum PUF authentication via silicon photonics
- **dpf-error-detecting-pir-rings**: Information-theoretic private information retrieval
- **quantum-entanglement-channel-discrimination**: MEWC/MEBC framework — entanglement resource trade-offs for channel discrimination and phase transitions

## References

- Nielsen & Chuang: Quantum Computation and Quantum Information
- Scarani et al.: The security of practical quantum key distribution
- Lo et al.: Decoy state quantum key distribution
- Renner: Security of Quantum Key Distribution
- **[references/pqc-deployment-evaluation.md](references/pqc-deployment-evaluation.md)** — NIST PQC benchmarking results for 6G/IoT deployment (ML-KEM, ML-DSA, Falcon size/computation trade-offs)

## Notes

- Quantum information protocols are distinct from quantum algorithms
- Security proofs often use information-theoretic arguments
- Practical implementations require careful parameter tuning
- Hardware advances directly affect protocol feasibility