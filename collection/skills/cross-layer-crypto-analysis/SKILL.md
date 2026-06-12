---
name: cross-layer-crypto-analysis
description: "Cross-layer cryptographic security analysis skill for evaluating message transformations across network protocol stack. Analyzes encryption, authentication, and encapsulation at each layer (application, transport, network, link, physical). Use when: (1) evaluating post-quantum security of network protocols, (2) auditing cryptographic operations across OSI/TCP layers, (3) analyzing message transformation security, (4) assessing quantum vulnerability of network stack, (5) security audit of protocol layer interactions."
---

# Cross-Layer Cryptographic Analysis

Analyze cryptographic transformations across network protocol stack layers for security evaluation, particularly post-quantum readiness.

## Activation Keywords
- cross-layer crypto analysis
- protocol stack security
- post-quantum protocol analysis
- network layer encryption audit
- OSI layer security
- 跨层密码分析
- 协议栈安全
- 后量子协议

## Tools Used
- **exec**: Run security analysis scripts, query cryptographic standards
- **read**: Load protocol specifications, security frameworks
- **write**: Generate security reports, audit findings
- **web_search**: Search for cryptographic vulnerabilities, post-quantum standards

## Usage Patterns

### Pattern 1: Full Stack Security Audit
Analyze all protocol layers for cryptographic operations and quantum vulnerability:
```
分析整个协议栈的密码学安全
```

### Pattern 2: Layer-Specific Analysis
Focus on specific layer's cryptographic mechanisms:
```
分析传输层的量子安全威胁
```

### Pattern 3: Post-Quantum Readiness Assessment
Evaluate quantum vulnerability of existing cryptographic implementations:
```
评估 TLS 1.3 的后量子安全状态
```

## Instructions for Agents

### Phase 1: Protocol Stack Mapping

Map the network stack layers and identify cryptographic operations at each layer:

```
OSI Model Layers:
┌─────────────────────────────────────┐
│ 7. Application Layer                │  HTTPS, application encryption
├─────────────────────────────────────┤
│ 6. Presentation Layer               │  SSL/TLS encryption
├─────────────────────────────────────┤
│ 5. Session Layer                    │  Session management
├─────────────────────────────────────┤
│ 4. Transport Layer                  │  TCP/UDP, transport security
├─────────────────────────────────────┤
│ 3. Network Layer                    │  IPsec, network encryption
├─────────────────────────────────────┤
│ 2. Data Link Layer                  │  MAC, link encryption
├─────────────────────────────────────┤
│ 1. Physical Layer                   │  Physical security
└─────────────────────────────────────┘
```

For each layer, document:
- **Cryptographic algorithms**: RSA, AES, ECC, SHA, etc.
- **Security operations**: Encryption, authentication, integrity
- **Message transformations**: Encapsulation, encoding
- **Quantum vulnerability**: Vulnerable to Shor/Grover algorithms?

### Phase 2: Transformation Analysis

For each message transformation across layers:

```python
def analyze_transformation(layer, operation, algorithm):
    """Analyze cryptographic transformation"""
    
    analysis = {
        "layer": layer,
        "operation": operation,  # encrypt, auth, encapsulate
        "algorithm": algorithm,
        "quantum_vulnerable": is_quantum_vulnerable(algorithm),
        "pq_alternative": get_pq_alternative(algorithm),
        "security_level": calculate_security_bits(algorithm),
        "recommendation": generate_recommendation(algorithm)
    }
    
    return analysis
```

#### Quantum Vulnerability Assessment

| Algorithm | Quantum Attack | Vulnerability | PQ Alternative |
|-----------|---------------|---------------|----------------|
| RSA | Shor | ✗ HIGH | CRYSTALS-Kyber |
| ECC | Shor | ✗ HIGH | CRYSTALS-Dilithium |
| AES-128 | Grover | ◐ MEDIUM | AES-256 |
| SHA-256 | Grover | ◐ LOW | SHA-384/512 |
| DH | Shor | ✗ HIGH | SIKE (broken), Kyber |

### Phase 3: Security Audit Checklist

Generate comprehensive audit findings:

```markdown
## Cross-Layer Cryptographic Security Audit

### Application Layer (Layer 7)
- **Protocols**: HTTPS, application-specific encryption
- **Algorithms**: [list algorithms]
- **Quantum Status**: [vulnerable/safe]
- **Recommendations**: [pq migration plan]

### Transport Layer (Layer 4)
- **Protocols**: TLS 1.3, DTLS
- **Algorithms**: [list algorithms]
- **Quantum Status**: [vulnerable/safe]
- **Recommendations**: [pq migration plan]

### Network Layer (Layer 3)
- **Protocols**: IPsec, VPN
- **Algorithms**: [list algorithms]
- **Quantum Status**: [vulnerable/safe]
- **Recommendations**: [pq migration plan]

### Link Layer (Layer 2)
- **Protocols**: WPA3, MAC security
- **Algorithms**: [list algorithms]
- **Quantum Status**: [vulnerable/safe]
- **Recommendations**: [pq migration plan]

### Quantum Risk Summary
- **High Risk**: [count] algorithms vulnerable to Shor
- **Medium Risk**: [count] algorithms vulnerable to Grover
- **Safe**: [count] quantum-resistant algorithms

### Migration Priority
1. [Immediate] Replace RSA/ECC with PQ alternatives
2. [Near-term] Upgrade symmetric key sizes
3. [Long-term] Implement hybrid PQ/classic schemes
```

### Phase 4: Post-Quantum Standards Reference

Current NIST PQC standards (2024):

- **CRYSTALS-Kyber**: Key encapsulation (replacement for RSA/ECDH)
- **CRYSTALS-Dilithium**: Digital signatures (replacement for RSA/ECDSA)
- **Falcon**: Digital signatures (lattice-based)
- **SPHINCS+**: Hash-based signatures

Implementation considerations:
- Hybrid mode: Classic + PQ algorithms during transition
- Performance impact: PQ algorithms larger keys/signatures
- Compatibility: Check protocol support for PQ algorithms

## Error Handling

### Algorithm Not Recognized
```
If algorithm not in database:
  1. Search web for algorithm specifications
  2. Determine if symmetric/asymmetric
  3. Assess quantum vulnerability based on type
  4. Document finding for future reference
```

### Layer Mapping Unclear
```
If protocol layer unclear:
  1. Refer to OSI model specification
  2. Identify protocol's primary function
  3. Map to closest matching layer
  4. Document uncertainty in report
```

## Examples

### Example 1: TLS Security Audit

```
User: 分析 TLS 1.3 的跨层密码安全

Agent Process:
1. Maps TLS to Presentation/Transport layers
2. Analyzes cryptographic operations:
   - Key exchange: ECDHE (vulnerable to Shor)
   - Authentication: RSA-PSS/ECDSA (vulnerable to Shor)
   - Encryption: AES-128-GCM (vulnerable to Grover)
   - Integrity: SHA-256 (vulnerable to Grover)
3. Generates audit report with PQ recommendations
4. Suggests migration: TLS with Kyber + Dilithium
```

### Example 2: Full Stack Analysis

```
User: 评估我的网络协议栈的后量子安全

Agent Process:
1. Maps all protocol layers (OSI model)
2. Identifies cryptographic operations at each layer
3. Assesses quantum vulnerability for each algorithm
4. Prioritizes migration based on risk level
5. Generates comprehensive audit report
```

## Related Skills
- **security-guardrails**: Security best practices
- **crypto-analysis**: Cryptographic algorithm analysis
- **network-security**: Network security frameworks

## Resources
- NIST PQC Standards: https://csrc.nist.gov/projects/post-quantum-cryptography
- IETF PQC Drafts: https://datatracker.ietf.org/
- OWASP Crypto Guide: https://cheatsheetseries.owasp.org/

## Notes
- Focus on practical security assessment
- Prioritize high-risk algorithms (RSA, ECC)
- Recommend hybrid transition strategy
- Document migration timeline