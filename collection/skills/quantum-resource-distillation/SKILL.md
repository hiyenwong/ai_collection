---
name: quantum-resource-distillation
description: >
  Methodology for quantum resource distillation using the composite generalised quantum Stein's lemma.
  Covers optimal rates for distilling quantum resources (entanglement, magic, coherence) from noisy states
  via asymptotic conversion protocols. Use when: (1) analyzing quantum resource conversion rates,
  (2) designing distillation protocols for entanglement/magic states, (3) studying asymptotic quantum
  resource theory, (4) evaluating noisy-to-pure state conversion efficiency, or (5) researching
  quantum Stein's lemma applications. Activation: quantum resource distillation, quantum Stein's lemma,
  entanglement distillation, magic state distillation, quantum resource theory, asymptotic conversion,
  量子资源蒸馏, 量子斯坦因引理.
---

# Quantum Resource Distillation

## Description

Quantum resource distillation methodology based on the composite generalised quantum Stein's lemma
(arXiv:2605.15174). Provides framework for computing optimal conversion rates of quantum resources
(entanglement, coherence, magic) from noisy input states to pure target states in the asymptotic limit.

## Core Framework

### Quantum Stein's Lemma for Resource Distillation

The composite generalised quantum Stein's lemma establishes:
- **Optimal error exponent** = relative entropy between target and resource states
- **Achievable rate** = resource measure derived from hypothesis testing
- **Universality** — applies to all quantum resource theories satisfying basic axioms

### Key Mathematical Objects

1. **Resource measures**: Monotones quantifying "resourcefulness" of quantum states
2. **Distillation protocols**: LOCC or free operations converting n copies of ρ → m copies of target state
3. **Asymptotic rate**: lim (m/n) as n → ∞, measuring conversion efficiency
4. **Generalised relative entropy**: D(ρ||σ) — the fundamental quantity governing rates

### Distillation Rate Formula

For distilling target state ψ from noisy state ρ:
```
R_distill(ρ → ψ) = inf_σ D(ρ||σ) / D(ψ||σ_target)
```
where the infimum is over free states σ in the resource theory.

## Application Domains

### Entanglement Distillation
- Extract pure Bell pairs from mixed entangled states
- Rate governed by entanglement of distillation E_D(ρ)
- Fundamental limit: E_D(ρ) ≤ E_R(ρ) (relative entropy of entanglement)

### Magic State Distillation
- Extract non-Clifford magic states from noisy preparations
- Critical for fault-tolerant quantum computation
- Rate determined by magic monotones (mana, thauma)

### Coherence Distillation
- Extract pure coherent superpositions from mixed states
- Relevant for quantum metrology and sensing
- Coherence of distillation C_D(ρ) = S(Δ(ρ)) - S(ρ) in some theories

## Instructions for Agents

### Step 1: Identify Resource Theory
Determine the free operations and free states:
- Entanglement: LOCC operations, separable states
- Magic: Clifford operations, stabilizer states
- Coherence: Incoherent operations, diagonal states

### Step 2: Characterize Input State
Compute relevant resource measures for the input state ρ:
- Relative entropy of resource: D_R(ρ) = min_σ D(ρ||σ)
- Robustness of resource
- Other theory-specific monotones

### Step 3: Apply Stein's Lemma Bound
The optimal distillation rate is bounded by:
```
R ≤ D_R(ρ) / D_R(target)
```
This is the composite generalised quantum Stein's lemma result.

### Step 4: Check Achievability
Verify if the bound is achievable:
- Asymptotic regime: n → ∞ copies available
- One-shot regime: finite n, use hypothesis testing relative entropy
- Composite vs. simple hypothesis testing

## Limitations

- Results are asymptotic (n → ∞); finite-size corrections require one-shot analysis
- Assumes i.i.d. input states; correlated inputs need different treatment
- Specific rates depend on the resource theory's structure

## Related Skills

- quantum-ai-patterns: Reusable quantum AI research patterns
- quantum-error-correction-gauge-theory: QEC via gauge theories
- quantum-ml-patterns: Quantum ML research patterns
- ml-quantum-error-correction: ML for QEC
- quantum-fault-tolerance-verification: Quantum fault-tolerance verification

## Notes

- Based on Lami, Regula, Takagi (2026): "Universal quantum resource distillation via composite generalised quantum Stein's lemma"
- The composite Stein's lemma generalizes the standard result to multiple alternative hypotheses
- Key insight: a single information-theoretic quantity governs distillation across ALL resource theories
