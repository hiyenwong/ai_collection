---
name: refactoring-as-propositions
description: "Proved refactoring methodology for cyber-physical hybrid systems using differential refinement logic (dRL). Enables formal verification that system modifications preserve safety properties without full re-verification. Use when designing, modifying, or verifying CPS/hybrid systems, performing safe refactoring of control systems, or establishing formal safety guarantees for iterative system design."
---

# Refactoring-as-Propositions Methodology

Proving CPS refactorings preserve safety properties via differential refinement logic (dRL).
Accepted at IJCAR 2026. arXiv: 2605.15001.

## Core Principle

Represent system refactorings as **propositions** rather than opaque transformations.
Prove that a refactored system preserves required properties by transferring the proof
along the modification — not re-verifying the entire system.

## Differential Refinement Logic (dRL)

dRL extends differential dynamic logic (dL) with refinement judgments:

```
α ⊑ β
```

Meaning: system β refines system α — every behavior of β is also a behavior of α.

### Key Inference Rules

1. **Refinement Transitivity**: If α ⊑ β and β ⊑ γ, then α ⊑ γ
2. **Sequential Refinement**: (α₁;α₂) ⊑ (β₁;β₂) if α₁ ⊑ β₁ and α₂ ⊑ β₂
3. **Choice Refinement**: (α ∪ β) ⊑ (α' ∪ β') if α ⊑ α' and β ⊑ β'
4. **Loop Refinement**: α* ⊑ β* if α ⊑ β
5. **Auxiliary Variable Introduction**: Adding ghost/auxiliary variables preserves refinement

### Refactoring Proof Pattern

```
Given:    ⊢ [α]φ    (original system α satisfies property φ)
Given:    ⊢ α ⊑ β   (refactored β refines original α)
Conclude: ⊢ [β]φ    (refactored system also satisfies φ)
```

The proof obligation reduces to showing α ⊑ β, which is often local and modular.

## Refactoring Patterns

### Pattern 1: Auxiliary Variable Introduction

When adding ghost variables for analysis:
```
α = (x' = f(x))
β = (x' = f(x), y' = g(x, y))   // y is auxiliary
Then: α ⊑ β  (auxiliary variables don't add behaviors)
```

### Pattern 2: Controller Decomposition

Splitting a monolithic controller:
```
α = (ctrl₁ ⊕ ctrl₂)    // monolithic choice
β = (mode=1 → ctrl₁ | mode=2 → ctrl₂)  // decomposed with mode flag
If decomposition is sound: α ⊑ β
```

### Pattern 3: Plant Model Refinement

Refining physical plant model with more detail:
```
α = (x' = f(x))          // simple model
β = (x' = f(x) + ε, |ε| < δ)  // bounded disturbance model
If β's behaviors ⊆ α's over-approximation: α ⊑ β
```

## Automation Strategy

1. **Symbolic Proof**: Use KeYmaeraX or similar dL provers
2. **Modular Decomposition**: Break system-wide proofs into local refinement proofs
3. **Proof Transfer**: Carry existing safety proofs through refinement chains
4. **Incremental Verification**: Only prove the delta, not the full system

## Application Workflow

1. **Identify Refactoring**: What system component is being modified?
2. **Express as Refinement**: Write α ⊑ β where α = original, β = refactored
3. **Decompose Proof**: Break into sub-refinements for each component
4. **Prove Local**: Show each local refinement holds
5. **Compose**: Chain refinements via transitivity
6. **Transfer Property**: Apply refinement to carry [α]φ → [β]φ

## When to Use

- Modifying CPS controllers while preserving safety guarantees
- Adding monitoring/auxiliary variables to verified systems
- Decomposing monolithic controllers into modular architectures
- Refining plant models with additional physical detail
- Iterative design of hybrid systems requiring re-verification

## Pitfalls

- dRL refinements are **not** bidirectional: α ⊑ β ≠ β ⊑ α
- Auxiliary variables must be truly non-interfering (not affecting control flow)
- Loop refinements require matching termination conditions
- Hybrid system refinements must handle both discrete jumps and continuous flows
