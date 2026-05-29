---
name: bell-probability-factorization
description: "Statistical foundations of Bell's theorem — why probability factorization fails in quantum systems. Covers the mathematical structure of Bell inequalities, joint probability distributions, local hidden variable models, and the statistical conditions under which factorization P(A,B|a,b,λ) = P(A|a,λ)P(B|b,λ) breaks down. Use when: Bell's theorem, quantum nonlocality, probability factorization, local hidden variables, Bell inequalities, CHSH inequality, quantum correlations, statistical foundations of quantum mechanics, joint distributions in quantum systems."
metadata:
  arxiv_id: "2605.29589"
  published: "2026-05-29"
  tags: [bell-theorem, probability, nonlocality, statistics, quantum-foundations, joint-distributions]
---

# Bell's Theorem: Statistical Foundations

## Core Claim

Bell's theorem is fundamentally a statement about **probability factorization**:

> No local hidden variable model can reproduce quantum correlations because the factorization assumption P(A,B|a,b,λ) = P(A|a,λ)·P(B|b,λ) is incompatible with quantum predictions.

## Mathematical Framework

### Factorization Assumption

A local hidden variable model assumes:

```
P(A,B | a,b) = ∫ P(A|a,λ) · P(B|b,λ) · ρ(λ) dλ
```

Where:
- A, B: measurement outcomes
- a, b: measurement settings
- λ: hidden variable
- ρ(λ): probability distribution over λ

### Why Factorization Fails

1. **Quantum entanglement** creates correlations that cannot be decomposed into product form
2. The quantum joint probability: P(A,B|a,b) = |⟨ψ|E_A(a)⊗E_B(b)|ψ⟩|²
3. This does NOT factorize for entangled states |ψ⟩ ≠ |ψ_A⟩⊗|ψ_B⟩

### CHSH Inequality

The statistical consequence of factorization:

```
|E(a,b) + E(a,b') + E(a',b) - E(a',b')| ≤ 2
```

Where E(a,b) = Σ_{A,B} A·B·P(A,B|a,b)

**Quantum violation**: Maximum = 2√2 (Tsirelson bound)

## Statistical Interpretation

### Key Insight

The failure of factorization is a **statistical** phenomenon, not a physical one:

- Classical systems: Joint distributions factorize under conditional independence
- Quantum systems: Measurement outcomes are not conditionally independent given any classical λ
- This means: no classical probability space can reproduce quantum statistics

### Implications for Statistical Modeling

When building statistical models of quantum or quantum-like systems:

1. **Do NOT assume conditional independence** between subsystems
2. **Use quantum probability** (Hilbert space formalism) when classical factorization fails
3. **Test for Bell inequality violation** as a diagnostic for non-classical correlations
4. **Consider contextuality**: P(A|a) may depend on whether B is also measured

## Applications

### 1. Quantum Randomness Certification

Bell violation certifies that outcomes are genuinely random (not pre-determined by any λ).

### 2. Device-Independent Cryptography

Security proofs that do not assume internal device structure — rely solely on observed correlations violating Bell inequalities.

### 3. Statistical Testing for Quantum Advantage

Compare classical vs. quantum model fits to experimental data using Bell-type statistics.

## Pitfalls

- **Detection loophole**: Low detection efficiency can mimic factorization failure. Require η > ~82.8% for loophole-free tests.
- **Memory loophole**: Reusing hidden variables across trials invalidates i.i.d. assumption. Use fresh λ per trial.
- **Fair sampling**: Assuming detected particles represent the full ensemble may introduce bias.
- **Not a "communication" result**: Bell violation does NOT imply faster-than-light signaling. Correlations are non-signaling.

## Activation

Keywords: Bell theorem, probability factorization, quantum nonlocality, CHSH inequality, local hidden variable, joint distribution, quantum correlation, statistical quantum mechanics
