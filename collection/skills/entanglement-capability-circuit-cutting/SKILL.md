---
name: entanglement-capability-circuit-cutting
description: Use when cutting quantum circuits across distributed QPUs.
category: ai_collection
metadata:
  arxiv_id: "2610.14580"
  published: "2026-10-10"
  authors: "Weidong Liu, Qingqing Jiang, Yufu Liu, Ruiqing He, Jiandong Shang, Hengliang Guo, Qiang Chen"
  tags: [distributed-quantum-computing, circuit-cutting, mps, qpd, partitioning]
---

# Entanglement-Capability-Aware Finite-Bond Circuit Cutting (SACE)

SACE (Simulation-Aware Circuit partitioning with Entanglement-capability-aware Screening) selects where to CUT a quantum circuit so it can run across multiple resource-constrained QPUs, minimizing both quasiprobability-decomposition (QPD) sampling overhead and classical reconstruction error. Verified against arXiv:2610.14580 (Zhengzhou University, Oct 2026); algorithm numerically reproduced (EP-Cost formula, lexicographic two-stage selection).

## When to Use

- Distributing a circuit whose width exceeds a single QPU's qubit capacity
- Choosing among equal-count cut positions with different gate parameters (CP(θ), RZZ(θ) angles matter!)
- Reducing QPD overhead: 25.20×/16.89× reduction demonstrated on 8/9-qubit QFT at matched cut counts
- Any quantum-HPC workflow where reconstruction budget (QPD term count, cut count) is a hard constraint

## Core Methodology

### Stage 1 — EP-Cost boundary screening (cheap, gate-level)

For each two-qubit gate g, define parameter-dependent entanglement-capability proxy η_g:

| Gate | η_g |
|------|-----|
| CP(θ) | sin²(θ/2) |
| RZZ(θ) | sin²(θ) |
| CX, CZ | 1 |
| SWAP | 0 |

For cut set δ(P), with equal weights λ_E = λ_I = 1/2:

```
E_cut(P) = Σ_{g∈δ(P)} η_g          # entanglement capability severed
I_cut(P) = Σ_{g∈δ(P)} κ_g          # native implementation cost (κ_g = cost of implementing g natively)
C_EP(P) = (E_cut + I_cut)/2
```

Key insight: for CP/RZZ gates, single-gate QPD overhead Ω_g = (1+2√η_g)² is a **monotone function of η_g** — the entanglement-capability score IS an overhead predictor. SWAP has η=0 but real implementation burden → captured by κ_g, not η_g.

### Stage 2 — Finite-bond refinement (MPS-based)

Keep only TopM candidates by (C_EP, id) lexicographic rank (paper: M=32). For each candidate partition P, simulate isolated subcircuits as normalized MPS at bond dimensions χ and 2χ:

```
F^{(k)}_{χ,2χ}(P) = ⟨ψ^{(k)}_χ(P) | ψ^{(k)}_{2χ}(P)⟩²     # finite-bond overlap, per block k
R_multi,χ(P) = max_k [1 − F^{(k)}_{χ,2χ}(P)]              # worst-block convergence score
P*χ = argmin_{P∈P_M} lex(R_multi,χ(P), C_EP(P), id(P))    # lexicographic selection
```

Smaller R_multi = less MPS truncation error when bond doubles = subcircuits are classically tractable.

### Reconstruction constraints (external feasibility, NOT in objective)

QPD overhead: `Ω_QPD(P) = Π_{g∈δ(P)} γ_g²` where γ_g = one-norm of QPD coefficient vector. Budgets on cut count / QPD terms / Ω_QPD restrict the candidate set BEFORE selection — they never bias the ranking.

## Implementation Guidance

```python
import math, itertools

def eta(gate, theta=0.0):
    return {'CP': math.sin(theta/2)**2, 'RZZ': math.sin(theta)**2,
            'CX': 1.0, 'CZ': 1.0, 'SWAP': 0.0}[gate]

def ep_cost(cut_gates):
    E = sum(eta(t, th) for (t, th, _) in cut_gates)
    I = sum(k for (_, _, k) in cut_gates)
    return 0.5 * (E + I)  # lambda_E = lambda_I = 1/2

# Stage 1: enumerate/rank candidates by (ep_cost, canonical_id)
# Stage 2: top-M panel, compute MPS overlap at chi vs 2*chi per block, pick argmin lex(R, ep_cost, id)
```

Search procedures (genetic algorithm, simulated annealing, discrete PSO) may generate the archive A_EP — SACE is search-agnostic; only the two-stage ranking is fixed.

## Pitfalls

- **EP-Cost is not a QPD objective** — it is a monotone *predictor* for CP/RZZ gates only. Don't use it as the final word; the finite-bond stage exists precisely because boundary cost alone misses MPS complexity.
- **SWAP anomaly**: SWAP has η=0 (no entanglement generated on product inputs) but is expensive to implement/cut. Always include κ_g separately.
- **Panel size trade-off**: larger M improves the optimized proxy but does NOT guarantee lower exact-local error (paper's 24-qubit sensitivity study). M=32 was the sweet spot.
- **Normalization**: MPS states must be normalized before the overlap contraction; un-normalized states skew R_multi.

## Validation Results (paper)

| Setting | Result |
|---------|--------|
| 14 exhaustive small-scale spaces | EP-Cost↔QPD-overhead median Spearman 0.9965 |
| 8/9-qubit QFT, matched cuts | QPD overhead ↓25.20× / ↓16.89× |
| 12-qubit AQFT, 5 cuts, 7,776 QPD terms | best on all 4 metrics in 4/6 conditions |
| 24-qubit QFT, 30 conditions | beats EP-Cost-only, Kernighan-Lin, spectral in ALL |
| 50-qubit QFT | favorable as reference convergence improves |

My synthetic-gate verification (28 bipartitions, 8 mixed gates): EP-Cost ranking correctly identifies CP/RZZ-with-small-angle cut sets as cheap and CX/CZ/CP(π/2) sets as expensive; lexicographic refinement reproduces P* selection.

## Applications & Extensions

- Cross-QPU workload placement in quantum-HPC schedulers (pair with distributed-qaoa-simulator, dsabre-distributed-quantum-router)
- Weighted QAOA partitioning: paper shows QAOA is more bond-sensitive than QFT → SACE refinement matters more
- Generalizable pattern: any two-stage 'cheap analytic screen → expensive simulation refine' with lexicographic tie-breaking

## Related Skills
- scalable-quantum-circuit-knitting (weak-cut knitting)
- dsabre-distributed-quantum-router (routing after partition)
- entanglement-distribution-star-networks (physical layer beneath)
