---
name: one-shot-quantum-signatures
description: Quantum algorithm for one-shot signatures using affine coset superposition and puncturable PRFs. Provides circuit-level implementation for delegated signatures, secured token transfer, and publicly verifiable randomness. Use when implementing quantum signature schemes, building quantum-secure authentication protocols, or designing quantum token systems.
---

# One-Shot Quantum Signatures

## Core Methodology

Two-stage protocol: key generation produces classical public key / quantum secret key pair, then signing processes the quantum secret key with a message string to produce a classical signature.

### Architecture

1. **Key Generation**: Prepare superposition over elements of a random affine coset determined by output of a puncturable pseudorandom function
2. **Signing**: Process quantum secret key with message string through coset membership testing circuit
3. **Verification**: Classical verifier checks signed message efficiently

### Complexity

- Logical qubits: Theta(kappa * log(r) + n + l)
- Gate complexity: Theta(n^3 + n*l)
- Parameters: r = public key size, n+l = signature size, l = message size, kappa = Omega(n) security parameter

### Security Properties

- No algorithmic error in construction
- Signed message efficiently checked by classical verifier
- Requires obfuscation for security against classical and quantum polynomial-time attacks