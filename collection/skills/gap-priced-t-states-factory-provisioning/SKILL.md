---
name: gap-priced-t-states-factory-provisioning
description: Use for T-state budget and factory allocation. Pareto DP.
category: ai_collection
---

# Gap-Priced |T⟩-States (GP|T⟩-S): Dynamic Post-Selection + Budget-Aware Factory Provisioning

**Paper**: arXiv:2610.19299 (Poster, Sethi, Liu, Baker, Iancu — UT Austin / LBNL, 13 Oct 2026)

## Core Problem

Magic |T⟩-state preparation dominates surface-code FTQC cost. Cultivation (grow + post-select on a **complementary gap** observable) and distillation (15-to-1 factories) are normally provisioned **statically**: a fixed fidelity target is chosen and surplus error budget is silently wasted. GP|T⟩-S treats the total T-error budget ε as an **expendable resource** and co-optimizes cultivation cutoff + factory fleet across it.

## Method Blueprint

### 1. Gap-as-price: cultivation states are a priced commodity
- Each cultivated state carries a measured **complementary gap**; the gap maps to an output-fidelity estimate (distributions from Google's cultivation data, d_cult=5, d_esc=15, p=1e-3, processed via INJEQT).
- **Budget slack → speed**: the scheduler dynamically relaxes the cultivation gap cutoff G (accepting lower-fidelity states) whenever the rate-weighted infidelity still meets ε/n_T, harvesting higher production rate instead of hoarding fidelity.

### 2. Robust cutoff selection under non-monotonic data
- Empirical gap→LER curves are NOT monotonic (finite-shot dips/bumps). Do not pick the smallest per-gap LER; **scan suffixes**: a cutoff G is feasible iff the **aggregate LER of the entire acceptance suffix** (all states with gap ≥ G) meets budget, and re-evaluate recursively as G moves. This is the statistically correct estimator of realized infidelity when production is throttled at G.

### 3. Factory catalog beyond the 35p³ black box
- The 35p³ fidelity figure holds only for large factories; **across sizes, output infidelity spans ~5 orders of magnitude** (small factories dominated by their own logical errors — fidelity decouples from input below saturation). A catalog must record (size → {qubit cost q, output rate r, output infidelity p_out}) jointly, not a scalar.
- 15-to-1 factories are Z-error sensitive → set measurement distance d_m = d_x (production rate tied to size).
- **Cultivating factories**: embed PureMagic cultivation INSIDE the factory routing channels — single-level footprint reaching fidelities that otherwise require (15-to-1)×(20-to-4) two-level distillation (e.g. dx=25/27/29 rows reach 1e-12–2e-14).

### 4. Allocation problem = Pareto-front DP
Decision variables: factory count, size, timing, edge placement, and target gap cutoff — jointly. Constraints: port cap P per edge, corner overhang flags c_L/c_R for ring closure, routing pressure (longer routing ancillas monopolize channels).
- **Exact DP**: bounded-knapsack over factory-type multisets bucketed by instance count; per-edge tables built by EXTEND (append factory, shift right) + MERGE (column-wise union + dominance update); entries carry (q, r, tangent length t, infidelity-weighted rate φ = Σ r(f)·p_out(f)). Dominated entries deleted on insertion; incomparable kept. Four edge tables joined around the ring; corner-flag conflicts discarded.
- Feasibility: cutoff G feasible iff rate-weighted infidelity of cultivation + distillation sources ≤ ε/n_T; take the LOWEST feasible G (converts leftover budget into supply rate).
- Output: Pareto front over (qubits q, cycles r, budget slack) → pick min spacetime / min time / min space.
- **Relaxed allocator**: 1,326× faster than exact DP on Heis-16 (23 ms vs 30.4 s), 6,445× on Heis-36 (44 ms vs 281 s); matches time within 0.5% but over-provisions space ≈ 12.8k qubits (0.45× compute core). Trade: exact front vs orders-of-magnitude cheaper solve.

### 5. Results (16 BenchPress benchmarks × 2 budgets = 32 pairs)
- Beats cultivation-only and single-factory baselines in **all 32 pairs**, both metrics, never exceeding budget.
- Logical cycles −69% avg (min 12%, max 99%); space-time volume −58% avg. Geomean **5.5× speedup** in cycles, **3.4×** in volume.
- ε=1e-3 (cultivation-feasible): gains come from slack-harvesting — 35–65% cycle cuts on small, 12–32% on large benchmarks. ε=1e-5 (cultivation infeasible): factories essential — 81–95% cycle cuts.
- Weakest cases (knn-129, wstate-118 @ ε=1e-3): per-T budget already tight → little slack to harvest (12%/14% cycles). **Design lesson: slack-harvesting gains scale with budget surplus; audit where the budget actually binds before promising speedups.**

## Reusable Engineering Patterns

1. **Budget-as-resource scheduling**: any statically-provisioned fidelity/quality target wastes slack; re-formulate as runtime-consumed budget and give the scheduler post-selection control (works for any post-selectable resource: magic states, verified prefixes, QEC postselection).
2. **Suffix-aggregate feasibility**: when per-item quality estimates are noisy/non-monotonic, feasibility of a cutoff = aggregate quality of the full acceptance suffix, evaluated recursively — never select on pointwise values.
3. **Catalog with coupled (size, rate, fidelity) tuples**: black-box scalars (35p³) hide 5 orders of magnitude; characterize components across sizes and keep incomparable entries (Pareto) in the catalog.
4. **Hybrid production hierarchies**: embed cheaper noisy production inside the transport/routing footprint of expensive producers (cultivating factories) — reach two-level fidelity at one-level footprint.
5. **DP with dominance pruning on structured domains**: EXTEND/MERGE table operators + on-insertion dominance deletion turn ring placement into a tractable bounded knapsack; keep the relaxed allocator as a fast path (minutes → milliseconds) with quantified over-provisioning.
6. **Gap cutoff as the free variable linking stages**: one scalar (acceptance threshold) couples cultivation and distillation stages — co-optimize it with fleet allocation rather than fixing it per stage.

## Key Numbers

| Quantity | Value |
|---|---|
| Benchmarks | 16 BenchPress (T counts 1.4e4 – 8.2e5) |
| Budgets | ε = 1e-3, 1e-5 total T-error |
| Cycle speedup (geomean) | 5.5× |
| Space-time reduction (geomean) | 3.4× |
| Exact DP vs allocator | 30.4 s → 23 ms (Heis-16); 281 s → 44 ms (Heis-36) |
| Cultivating factory best fidelity | 2.14e-14 (dx=29, dz=13, dcult=5) |

## Related Skills
- [[cornucopia-modular-quantum-architecture]] — modular FTQC blocks consuming these T-states
- [[logical-catalyst-dyadic-phase]] — cultivation protocol family
- [[puremagic-lattice-surgery-scheduler]] — base scheduler extended by GP|T⟩-S
- [[ft-resource-estimation-uncertainty-propagation]] — resource estimates as intervals
