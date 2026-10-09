---
name: fault-equivalent-circuit-reduction
description: Use when optimizing QEC circuits via fault-preserving rewrites. Automated Bell-pair reduction search.
category: ai_collection
---

# Fault-Equivalent Circuit Reduction

Automated search over **fault-equivalent rewrites** that reduce QEC circuit resources (ancillas + CNOTs) while *provably inheriting* the input circuit's fault-tolerance properties — no per-candidate FT re-verification needed.

Source: "Automated reduction of fault-tolerant circuits" (Jeon, Lee, Kim; arXiv:2610.09749, Oct 2026)

## Core Principle

Fault equivalence is stronger than ideal-map equivalence: two circuits are fault-equivalent when every undetectable fault pattern of weight < w in one has a no-greater-weight counterpart with the same faulty map in the other (both directions). Rewrites validated in this relation **compose and transit**, so every circuit reachable from a fault-tolerant input is itself fault-tolerant at the same distance.

Correctability is judged by **stabilizer-coset weight** `wtS(E) = min_s wt(E·s)`, not physical weight — errors differing by a stabilizer act identically on the codespace.

## The Rewrite Set

**Enabling rules** (do NOT reduce resources; only restructure to expose patterns):
1. **Restricted commutation** — swap two CNOTs sharing an initialized qubit (control in |+⟩ or target in |0⟩). Fails on arbitrary input states.
2. **Basis swap** — exchange roles of the two wires preparing |Φ+⟩ (state invariant under qubit exchange).
3. **Target swap** — redirect the second CNOT's endpoint in a three-qubit pattern.

**Reducing rule**:
4. **Bell-pair reduction** — removes one Bell-pair qubit + its CNOT. Two hard constraints:
   - The pair must evolve **factorized** as U ⊗ V until measurement (no joint gate after preparation).
   - The eliminated outcome may only feed a **parity** with other outcomes (relabeling m⊕q, fixing m=0) — never serve as an independent flag. This is classical record relabeling, NOT postselection.

The transpose identity `(U⊗V)|Φ+⟩ = (UV^T ⊗ I)|Φ+⟩` + outcome-0 effect yields the reduced circuit; scalar 1/√2 factors are irrelevant.

## Search Algorithm (Breadth-First Composite Reductions)

```
Q ← [C0]; T ← ∅
while Q nonempty:
    C ← dequeue(Q); terminal ← true
    for each composite reduction M in FindCompositeReductions(C):
        C' ← Apply(C, M)   # enabling seq (0+ rules) → one Bell reduction
        if C' valid: terminal ← false; enqueue(C')
    if terminal: T ← T ∪ {C}
return T
```

Key design decisions:
- Enabling rewrites are **never chained speculatively** — only applied when they immediately expose a Bell pair. This bounds branching.
- Each composite transition removes exactly **1 ancilla + 1 CNOT** → resource cost strictly decreases → search depth bounded by Bell-reduction count. Terminates.
- Search states are **circuits, not ZX diagrams**: each step is circuit → ZX translation → single fault-equivalent rewrite → circuit re-extraction. Avoids the huge ZX branching factor while validity comes from ZX edge-flip noise reasoning (atomic fault = single-edge Pauli on a directionless diagram; correlated multi-qubit faults via fault gadgets).
- No dedup across paths (same circuit reachable twice is reprocessed) — costs time, not soundness.

## Candidate Selection: Sequential Race

For large candidate pools (391 circuits from a Steane/Goto baseline):
- Escalating shots: 10³ → 5×10³ → 2.5×10⁴ → 10⁵ → 10⁶
- Eliminate at α = 0.05 at each stage; final survivors get the full budget
- Race in the **harder basis/noise model** (e.g. |+⟩L memory under dephasing idle)

## Flag Handling: Decode, Never Reject

Raised verification flags select a **flag-conditioned lookup table** (enumerate all single faults, keep those raising the flag, map residual syndromes → corrections, mod stabilizer group) instead of discarding shots. Properties:
- All reported logical rates are **unconditional** — fair comparison across circuit families
- Near-quadratic log-log slopes (1.94–1.97) verify no first-order failure mode (a miscorrected single fault would give slope ≈ 1)
- Fewer upstream gates → fewer flag firings (0.062 vs 0.072/cycle at p=1e-3) — flags decoded, so this is a diagnostic not a yield

## Verified Results ([[7,1,3]] Steane)

| Case | Before | After | Δ logical error |
|---|---|---|---|
| Shor-style SE (per round) | 30 ancillas, 54 CNOTs | 18 ancillas, 42 CNOTs | −21% @ p=1e-3 (−13…−23% over 1e-4…1e-2) |
| Steane dynamic SE (Goto prep) | 8 ancillas | 4 ancillas, 14 CNOTs, better CNOT depth | −15% @ depol idle 3p/10, −10% @ p/10 |

Baseline noise model (Quantinuum H2-motivated): 2Q gate p, 1Q gate 3p/100, SPAM p, idle depolarizing p/10. Toolchain: Stim + lookup-table decoder.

## When to Use

- Optimizing syndrome-extraction / state-prep / verification gadgets for small codes where ancilla count matters
- Any setting where circuit must stay fault-tolerant **by construction** and exhaustive re-verification of every candidate is too expensive
- Extension path: new reducing rules beyond Bell pairs; the enabling+reducing composite framework is rule-agnostic
