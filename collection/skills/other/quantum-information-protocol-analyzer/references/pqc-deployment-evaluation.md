# PQC Deployment Evaluation (arXiv: 2605.06881)

## Source
**Title**: Toward Quantum-Safe 6G: Experimental Evaluation of Post-Quantum Cryptography Techniques
**Authors**: Ananya Kudaloor, Adnan Aijaz
**arXiv**: 2605.06881 (May 2026, IEEE Communications Standards Magazine)

## Key Findings

### Computational Performance (Acceptable)
- ML-KEM key gen/encap: ~0.1-1ms across platforms
- ML-DSA signing: ~0.5-2ms
- Falcon signing: competitive, slightly slower than ML-DSA but smaller signatures

### Size Expansion (Critical Bottleneck)
| Algorithm | Size | Classical Equivalent | Expansion Factor |
|-----------|------|---------------------|------------------|
| ML-KEM-768 ciphertext | ~1184 bytes | ECDH ~32 bytes | ~37x |
| ML-DSA-65 signature | ~2420 bytes | ECDSA ~64 bytes | ~38x |
| Falcon-512 signature | ~897 bytes | ECDSA ~64 bytes | ~14x |

### Impact on Wireless Systems
- Handshake reliability drops on lossy channels due to packet fragmentation
- MTU exceeded → IP fragmentation → increased loss probability
- Edge/IoT most affected (limited bandwidth, higher loss rates)

### Recommended Deployment Patterns
1. **Core**: Hybrid TLS 1.3 (X25519 + ML-KEM-768) — overhead acceptable
2. **Edge**: Falcon for signatures (smallest), ML-KEM-512 for KEM
3. **IoT**: Pre-provisioned keys + connection pooling to amortize handshake costs
