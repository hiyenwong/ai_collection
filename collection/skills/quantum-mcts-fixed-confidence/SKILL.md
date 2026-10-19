---
name: quantum-mcts-fixed-confidence
description: Quantum speedup for Monte Carlo tree search. Use when combining quantum oracles with game tree search.
category: ai_collection
---

# Quantum Monte Carlo Tree Search with Fixed Confidence (QMCTS)

Source: arXiv:2609.33132 (Hu, Hu, Zhou — Fudan/GaTech, Sep 2026). Related: arXiv:2609.35511 (quantum stochastic games, expectiminimax nesting).

## Core Problem
Fixed-confidence MCTS on a MAX-MIN game tree with stochastic Bernoulli leaves: identify an ε-optimal root move with probability ≥ 1−δ while minimizing queries. Classical fixed-confidence methods (UGapE-MCTS) scale **quadratically** in inverse gap/precision (O(d²) per leaf); QMCTS achieves **linear** scaling O(d) — a quadratic query speedup, proven near-optimal by a matching lower bound on pivotal leaves.

## Quantum Oracle Model
Each leaf ℓ with Bernoulli mean µℓ gets a unitary oracle:
```
Uℓ |0⟩ = √(1−µℓ)|0⟩ + √µℓ |1⟩
```
- One query to Uℓ (or Uℓ†) prepares a coherent quantum sample; measuring gives one classical Bernoulli draw.
- Classical simulator (Boolean circuit) → reversible quantum circuit with polynomial overhead.
- Query complexity replaces sample complexity as the cost measure.

## Three Key Design Principles

### 1. Lazy-Measurement Principle (the central constraint)
Classical sequential MCTS reuses intermediate estimates to decide sampling/elimination. In quantum, every intermediate estimate requires measurement → state collapse → quantum advantage destroyed. **Fix**: measure only ONCE per iteration, at the end. Balance measurement frequency against adaptivity.

### 2. QMC Subroutine (Kothari-O'Donnell quantum mean estimation)
Estimate leaf mean µℓ to precision α with failure prob η using **O((1/α)log(1/η))** queries vs classical O((1/α²)log(1/η)) samples (Hoeffding). Quadratic precision advantage.

### 3. Geometric Threshold Elimination on Tree Structure
- Iteration r uses threshold γr = 2⁻ʳ; QMC parameters αr = γr/2, ηr = δ/(2Lr²) (Lr = active leaf count).
- Propagate leaf estimates upward via MAX/MIN recursion.
- Eliminate any child c with empirical gap ĝr(s,c) > γr (reverse topological order), with entire subtree.
- Stop when one root move remains or γr ≤ ε.
- Error budget: union bound over active leaves keeps all estimates accurate w.p. 1−δ.

## Effective Difficulty & Bounds
Per-leaf difficulty: **dℓ,ε = Δℓ ∨ Δ⋆ ∨ ε** where Δℓ = max local edge gap on root-to-leaf path, Δ⋆ = root performance gap.

- **QMCTS upper bound**: O(Σℓ (1/dℓ,ε) · log(L/δ) + log²(1/dℓ,ε)) — linear in 1/d
- **Classical (CMCTS)**: O(Σℓ (1/d²ℓ,ε) · ...) — quadratic
- **Lower bound** (adaptive quantum, via new sequential quantum phase-testing): Ω(Σ_{pivotal ℓ} (1/dℓ,ε) log(1/δ)) — bounds MATCH up to log factors on uniformly pivotal instances
- Pivotal leaves = leaves that can affect the root decision; non-pivotal query cost is the price of not knowing tree relevance in advance (open gap).

## Hybrid MCTS (practical takeaway)
Pure QMCTS wastes queries at coarse precision (thousands of active leaves × QMC each); classical sampling is cheaper there and reuses past samples. **Hybrid rule**: per leaf, compare query cost of fresh QMC (1/α·log(1/η)) vs additional classical samples (log(2/η)/2α²) — decide BEFORE querying, switch when quantum becomes cheaper.
- Lichess depth-11 tree (9509 nodes): at 1/ε=1024, Hybrid = 11.7M queries vs QMCTS 35.1M vs CMCTS 47.1M.
- IBM hardware (depth-2 tree): QMCTS 68k vs CMCTS 306k queries (4.5× fewer, 77.7% reduction).

## Companion: Quantum Stochastic Games (arXiv:2609.35511)
Expectiminimax trees (m adversarial + m chance layers). Two speedups must survive **nesting**: √deg extremum (adversarial) + ε⁻¹ mean estimation (chance). Naive composition loses both.
- **Chance layers**: derandomised multilevel Monte Carlo — telescoping level differences; second moment of level-n difference falls 2⁻ⁿ while sample cost rises 2^(n/2) → total ε⁻¹ not ε⁻ᶜ.
- **Adversarial layers**: coherent binary search over value with fixed amplitude-amplification schedule (not Dürr-Høyer — no intermediate measurement, brackets true extremum).
- **Interface lemmas**: (a) convert RMSE guarantee (from mean estimator) ↔ uniform guarantee (needed by extremum); (b) binary search avoids the √deg RMSE amplification that any estimate-extremum argument suffers.
- Result: Õ(deg^(m/2) ε⁻¹) vs classical Õ(deg^m ε⁻²); applies to any Lipschitz parent-of-children passing function with linear chance nodes and a sublinear quantum extremum routine.

## Reusable Patterns
1. **Lazy measurement**: in quantum-versions of adaptive classical algorithms, batch all measurements to iteration boundaries; design elimination rules to tolerate one-iteration-stale estimates.
2. **Geometric thresholds + per-leaf confidence budgeting** (ηr = δ/(2Lr²)): generic fixed-confidence identification template.
3. **Cost-based classical↔quantum switching**: when both backends solve the same subtask, compute each one's cost formula from current (α, η) and dispatch per-subtask — no fixed crossover point.
4. **RMSE↔uniform error conversion lemmas**: needed whenever a mean-estimation guarantee feeds an extremum/search primitive.
5. **Pivotal-element lower bounds**: characterize which problem components actually affect the final decision; query complexity is driven only by those.
6. **Sequential quantum phase-testing**: new lower-bound tool for adaptive quantum algorithms — reduce identification problems to phase-testing collections.

## Verification Checklist (from paper experiments)
- Log-log slope of query cost vs 1/Δ and 1/ε: QMCTS ≈ 0.96/0.95 (linear), classical ≈ 2.0 (quadratic).
- 100% empirical success on ε-optimal identification across all settings.
- Hybrid crossover appears as quantum-advantage regime only at high precision.
