---
name: quantum-crypto-exposure-measurement
description: Formal framework for measuring quantum cryptographic exposure under HNDL (Hard Non-Delegatable Leakage) threat model. Provides mathematical basis for quantifying information leakage in quantum cryptographic systems and assessing security exposure. Use when: quantum cryptographic security analysis, information leakage measurement, threat modeling for quantum systems, security exposure quantification.
---

# Quantum Cryptographic Exposure Measurement

## Core Concept

Provides a formal mathematical basis for measuring quantum cryptographic exposure under the HNDL (Hard Non-Delegatable Leakage) threat model. This framework enables:
- Quantitative measurement of information exposure in quantum systems
- Security assessment under non-delegatable leakage assumptions
- Formal bounds on adversary knowledge

## Key Components

### HNDL Threat Model
- **Hard Leakage**: Leakage that cannot be prevented by cryptographic means
- **Non-Delegatable**: Security properties that cannot be transferred to third parties
- **Quantum-Specific**: Accounts for quantum measurement disturbance and no-cloning

### Exposure Metrics
1. **Information Exposure (IE)**: Quantifies leaked quantum information
2. **Security Margin (SM)**: Gap between exposure and acceptable threshold
3. **Resilience Score (RS)**: System's ability to withstand exposure events

### Measurement Framework
- Define quantum system state space and adversary capabilities
- Model leakage channels (side-channel, protocol-level, implementation)
- Compute exposure bounds using quantum information theory
- Validate against known attack vectors

## Implementation Patterns

### Exposure Assessment
1. Identify quantum information assets and their quantum states
2. Map all potential leakage channels
3. Quantify exposure per channel using IE metrics
4. Aggregate to total system exposure
5. Compare against security thresholds

### Threat Modeling
1. Enumerate adversary capabilities (quantum computing power, measurement access)
2. Model attack scenarios within HNDL assumptions
3. Calculate worst-case exposure bounds
4. Design countermeasures for high-exposure paths

## Applications

- **QKD Security Analysis**: Measure key exposure in quantum key distribution
- **Quantum Network Security**: Assess exposure in quantum communication networks
- **Post-Quantum Migration**: Evaluate exposure during transition periods
- **Quantum Hardware Testing**: Side-channel exposure assessment

## Activation Keywords
- quantum cryptographic exposure
- HNDL threat model
- quantum security measurement
- information leakage quantum
- quantum threat modeling
- cryptographic exposure quantification
- 量子密码暴露测量

## Related Skills
- quantum-resistant-networks
- post-quantum-cryptographic-protocol-analysis
- quantum-information-protocol-analyzer
