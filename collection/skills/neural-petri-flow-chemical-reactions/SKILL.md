---
name: neural-petri-flow-chemical-reactions
description: "Neural Petri Flow (NPF) methodology: architecture that remains a valid Petri net for every weight value by hard-wiring conservation (firing form m'=m+Cσ) and enabling rule as parameter-free layers, learning only the rate law. Maps chemistry to Petri semantics (places=bonds/valence, tokens=bond order, transitions=form/break bond). Use when modeling chemical reactions, reaction networks, or any system with conserved quantities where learned models violate conservation laws."
category: ai_collection
activation:
  - Petri net
  - chemical reaction
  - reaction network
  - conservation law
  - rate law learning
  - atom mapping
  - reaction classification
  - valence
  - equivariant chemistry model
  - forward reaction prediction
---

# Neural Petri Flow for Chemical Reactions

**Source**: arXiv:2610.08750 (2026-10-06, cs.LG/physics.chem-ph/q-bio.QM) — Escrig Molina, Probst.

## Core Idea

Petri nets map naturally to chemistry, but learned models built on them (message-passing scaffolds) do **not** guarantee Petri semantics. Central question: **what architecture remains a Petri net for every value of its weights?**

Answer from Petri theory:
- **Conservation forces the firing form**: `m' = m + Cσ` (state update via incidence matrix × firing vector)
- **Non-negativity + locality force the enabling rule** (transition fires only when inputs present)
- The **rate law** (propensity of each transition to fire) remains FREE — this is what should be learned.

**NPF = parameter-free conservation/enabling layers + learned rate law (or readout for classification).** Guarantees hold by construction, not by training.

## Chemistry ↔ Petri Semantics Map

| Chemistry | Petri net |
|-----------|-----------|
| Bond between atoms / free valence | Places |
| Unit of bond order | Tokens |
| Forming / breaking a bond | Transition |
| Valence budgets of atoms | Conserved quantities |
| Valence rule | Enabling rule |

## Unified Task Framing: One Firing Vector

On a **valence net** (Petri net of bond changes with atom valence budgets), three tasks become predictions on the same object — the **minimum firing vector** σ:

1. **Atom mapping**: σ aligns reactant atoms to product atoms
2. **Reaction classification**: σ characterizes reaction type
3. **Forward prediction**: applying σ to reactants predicts products

## Results

| Task | NPF (untrained) | Baseline |
|------|-----------------|----------|
| Atom mapping, Golden set curated | **88.8%** | RXNMapper 85.6% |
| Atom mapping, EnzymeMap enzymatic | **88.7%** | RXNMapper 77.9% |
| Forward prediction, USPTO-480K | trained on firing vectors, competitive | — |

The untrained minimum firing vector alone beats trained baselines — the **structure does most of the work**.

## Reusable Patterns

### Pattern 1: Hard-Wire Invariants, Learn Only What's Free
Identify which parts of a domain's semantics are **forced by theory** (conservation → firing form; non-negativity → enabling rule) and implement them as **parameter-free layers**. Reserve learnable capacity exclusively for the genuinely underdetermined part (rate law / propensity). This eliminates constraint-violation failures by construction.

### Pattern 2: Conservation as Architecture, Not Loss
Instead of penalizing conservation violations with a soft loss term, use the state-update algebra `m' = m + Cσ` so conservation holds **exactly for every weight**. Soft penalties leak; algebraic structure doesn't.

### Pattern 3: One Latent Object, Many Readouts
Reformulate multiple task-specific pipelines (mapping/classification/forward-synthesis) as readouts on a **single shared latent** (the firing vector σ). Cross-task consistency becomes free, and untrained structure (minimum σ) already solves task(s) — a strong zero-shot baseline before any training.

### Pattern 4: Minimum-Firing-Vector Zero-Shot Baseline
Before training any model over a structured transition system, compute the **minimum feasible firing vector** (optimization over the incidence matrix). If it solves the task zero-shot (as here: 88.8% atom mapping), the learned component only needs to close the residual gap.

## When to Use

- Reaction network modeling / retro-synthesis / forward synthesis prediction
- Any learned dynamical model that keeps violating **conserved quantities** (mass, charge, valence, energy, momentum)
- Systems with clear transition semantics: chemical reaction networks, metabolic pathways, queueing/flow systems, protocol state machines
- When interpretability of "which transitions fired" is required (σ is directly readable)

## When Not to Use

- No natural conservation structure or transition algebra (use plain GNN/transformer)
- Pure property regression on static graphs (no transitions to model)

## Implementation Notes

- Incidence matrix C: places × transitions, entries +1 (produces) / −1 (consumes)
- Enabling rule layer: gate σ_t by `m[p] ≥ pre(p,t)` — implement as masking, never as penalty
- Rate law: any monotone ML head over place markings (MLP/attention over local inputs only — locality is part of the theory)
- Minimum firing vector: solve min ‖σ‖₁ s.t. m + Cσ ≥ 0 — LP-style optimization, no learning
- Valence nets: build places from free valence per atom + bond placeholders; tokens = bond order units

## Related Skills

- `hybrid-quantum-classical-reservoir-computing` — alternative structured chemical dynamics
- `generative-ml-quantum-selected-ci` — quantum chemistry with ML selection

## References

- arXiv:2610.08750 — Neural Petri flows for chemical reactions
- Petri net theory: firing form derivation from conservation
- RXNMapper, EnzymeMap — atom mapping baselines
