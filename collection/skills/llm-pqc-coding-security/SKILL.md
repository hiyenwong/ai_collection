---
name: llm-pqc-coding-security
description: "LLM-assisted post-quantum cryptography coding security patterns — analyzing secure coding drift, constant-time execution requirements, side-channel resistance, and gamified remediation strategies for PQC implementations."
version: 1.0
author: "R. D. N. Shakya, C. P. Wijesiriwardana, S. M. Vidanagamachchi, Nalin A. G. Arachchilage"
arxiv_id: "2606.19474"
published: 2026-06-17
categories: ["cs.CR", "cs.AI", "cs.SE"]
keywords: ["post-quantum cryptography", "LLM code generation", "secure coding", "constant-time execution", "side-channel resistance", "gamified security", "coding drift", "PQC implementation"]
activation_keywords: ["PQC coding", "post-quantum security", "LLM code audit", "constant-time implementation", "side-channel attack prevention", "gamified security training", "量子密码实现", "PQC代码安全", "LLM生成代码安全"]
---

# LLM-Assisted Post-Quantum Cryptography Coding Security

## Core Problem

The transition to Post-Quantum Cryptography (PQC) introduces significant implementation complexity:

1. **Constant-time execution**: PQC algorithms must execute in constant time to prevent timing attacks
2. **Side-channel resistance**: Protection against power analysis, electromagnetic, and cache-based attacks
3. **Precise parameter selection**: NIST PQC standards require exact parameter configurations
4. **Compiler optimization hazards**: Compilers may introduce timing variations despite source-level constant-time code

**New phenomenon**: LLM-assisted PQC development exhibits **secure coding drift** — gradual degradation of security-critical patterns as LLMs generate code that appears correct but violates subtle security constraints.

## Secure Coding Drift in LLM Development

### What is Coding Drift?

When LLMs generate PQC code, security violations accumulate gradually:

```
Iteration 1: Perfectly secure implementation (reference)
Iteration 2: Minor timing variance introduced (compiler hint missing)
Iteration 3: Side-channel vulnerable pattern (data-dependent branching)
Iteration N: Multiple vulnerabilities compound → exploitable
```

### Why LLMs Drift

1. **Training data gap**: Most training data predates PQC standards (NIST FIPS 203/204/205 published 2024)
2. **Security-blind optimization**: LLMs optimize for functionality, not security invariants
3. **Context window limits**: Security constraints span multiple code regions beyond context window
4. **No security feedback**: Standard LLM workflows lack security validation loops

### Gamified Fix Framework

The paper proposes **gamified remediation** to combat coding drift:

#### Gamification Components

| Component | Description |
|-----------|-------------|
| **Security Score** | Quantitative measure of code security posture |
| **Challenge Levels** | Progressive difficulty in identifying vulnerabilities |
| **Immediate Feedback** | Real-time vulnerability detection and explanation |
| **Achievement System** | Rewards for maintaining security over iterations |
| **Peer Comparison** | Benchmarking against other developers/implementations |

## PQC Implementation Security Checklist

### Constant-Time Execution

```python
# ❌ BAD: Data-dependent branching
if secret_key[i] > 0:
    result += table[secret_key[i]]

# ✅ GOOD: Constant-time table lookup
for j in range(table_size):
    mask = constant_time_eq(j, secret_key[i])
    result |= mask & table[j]
```

### Side-Channel Resistance

```python
# ❌ BAD: Memory access pattern reveals secret index
value = secret_array[secret_index]

# ✅ GOOD: Constant-time array access
result = 0
for i in range(len(secret_array)):
    mask = constant_time_eq(i, secret_index)
    result |= mask & secret_array[i]
```

### Parameter Validation

```python
# NIST PQC parameter validation
ML_KEM_512_PARAMS = {
    'n': 256,
    'k': 2,
    'eta1': 3,
    'eta2': 2,
    'du': 10,
    'dv': 4,
}

def validate_pqc_parameters(algorithm, params):
    """Validate PQC parameters match NIST specification."""
    expected = get_nist_params(algorithm)
    return all(params[k] == expected[k] for k in expected)
```

### Compiler Safety

```c
// Prevent compiler from optimizing away security-critical operations
__attribute__((optimize("O0"))) 
void secure_memset(void *ptr, int val, size_t len) {
    volatile unsigned char *p = ptr;
    while (len--) *p++ = val;
}
```

## LLM Code Review for PQC

### Automated Review Patterns

When reviewing LLM-generated PQC code, check:

1. **Data-dependent branching**: Any `if/switch` on secret data
2. **Early returns**: Function exits based on secret values
3. **Variable-time operations**: Division, modulo on secret data
4. **Memory access patterns**: Array indexing with secret indices
5. **Loop bounds**: Loop iterations depending on secret values
6. **Error handling**: Error paths that differ based on secrets
7. **Random number generation**: Use of CSPRNG, not `rand()`
8. **Memory cleanup**: Secure zeroing of secret buffers

### Review Prompt Template

```
Review this PQC implementation for security:

1. Identify all data-dependent control flow on secret values
2. Check for timing-vulnerable operations
3. Verify constant-time memory access patterns
4. Validate parameter correctness against NIST standards
5. Check for side-channel vulnerable error handling
6. Verify secure memory cleanup

For each finding, rate severity:
- CRITICAL: Exploitable side-channel
- HIGH: Potential timing leak
- MEDIUM: Suboptimal security pattern
- LOW: Style/robustness issue
```

## Security Metrics

### Coding Drift Index (CDI)

```
CDI = Σ(vulnerability_weight_i × iteration_distance_i) / total_iterations

Where:
- vulnerability_weight: CRITICAL=4, HIGH=3, MEDIUM=2, LOW=1
- iteration_distance: How many generations ago the vulnerability was introduced
- Lower CDI = better security maintenance
```

### Security Score Calculation

```
Security Score = 100 - (CRITICAL × 25 + HIGH × 15 + MEDIUM × 5 + LOW × 1)
Range: 0 (insecure) to 100 (perfect)
```

## Integration with Development Workflow

### Pre-commit Security Hook

```bash
#!/bin/bash
# Pre-commit PQC security check
echo "Running PQC security analysis..."
# Check for data-dependent branching on secrets
grep -rn "if.*secret\|if.*key\|if.*password" src/ | \
    grep -v "constant_time" | \
    grep -v "# skipcq"
```

### CI/CD Pipeline Integration

1. **Static Analysis**: Constant-time verification tools (ct-verif, dudect)
2. **Dynamic Analysis**: Timing measurement with statistical tests
3. **LLM Review**: Automated LLM-assisted security review
4. **Score Tracking**: Monitor security score over commits
5. **Alert System**: Trigger review when score drops below threshold

## Activation Triggers

Use this skill when:
- Reviewing LLM-generated cryptographic code
- Implementing NIST PQC standards (ML-KEM, ML-DSA, SLH-DSA)
- Setting up secure coding practices for PQC migration
- Designing gamified security training programs
- Auditing codebases for PQC compliance
- 审查大语言模型生成的后量子密码代码
- 实施 NIST 后量子密码标准

## Related Skills

- `cross-layer-crypto-analysis` — Cross-layer cryptographic security analysis
- `post-quantum-cryptographic-protocol-analysis` — PQC protocol analysis
- `security-guardrails` — Mandatory security guardrails
- `quantum-safe-pqc-deployment` — PQC production deployment

## Further Reading

- NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA)
- Bernstein et al. "How to write a constant-time implementation"
- NIST PQC Standardization Project: https://csrc.nist.gov/projects/post-quantum-cryptography

---

**Key Insight**: LLM-assisted PQC development requires active security monitoring. Secure coding drift accumulates silently across generations — without explicit security validation, even well-intentioned LLM-generated code becomes vulnerable. Gamified approaches can maintain developer engagement while catching drift early.
