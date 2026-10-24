---
name: vqa-basin-quality-optimizer-selection
description: Basin-quality diagnostics for deciding local vs global optimizers in variational quantum algorithms. Use when QAOA/VQE landscapes are multimodal.
category: ai_collection
---

# VQA Basin-Quality Optimizer Selection

Methodology from "Optimization Geometry of QAOA and Variational Quantum Algorithms" (arXiv:2610.05524, Novák, Zelinka, Illésová, Das, Beseda). Decides when multistart local search (BFGS) suffices vs when a global evolutionary solver (jSO/adaptive DE) is worth its budget, using two SEPARATE landscape diagnostics instead of vague "multimodality".

## Core Principle

**Local-minimum COUNT alone never justifies a global optimizer.** The decision variable is the QUALITY SPREAD of local-search endpoints (basin heterogeneity). Two regimes:

| Regime | Signature | Optimizer choice |
|---|---|---|
| **Rastrigin-like** (many minima, similar values) | high minima/line count, low `g_med`, high `p_near` | Multistart BFGS — extra minima are harmless, restarts are cheap exploration |
| **Schwefel-like** (fewer minima, very unequal values) | elevated `g_med`, high `p_poor` | Global DE — falling into the wrong basin is materially costly |

Verified head-to-head (MaxCut, N=10 3-regular graphs, exact statevector, 15k FEs each, FE-matched):
- Independent depth p=6 vs standard p=3: line-minima rose 12.00→14.75, but `g_med` stayed ~2pp and jSO LOST to multistart BFGS by 4.63pp.
- Parameter tying r=6 (18 physical layers, D=6 free params): `g_med` jumped to 16.74pp, `p_poor`=82.81%, and jSO WON by +1.88pp — its advantage persists against function-evaluation-MATCHED multistart, not just single-run local.

## The Four Diagnostics (compute BEFORE choosing an optimizer)

Given m random-start BFGS endpoints e_1..e_m, normalized as physical error ε_phys(θ) = (E(θ)−E₀)/(E_max−E₀) over the Hamiltonian spectral range:

1. **p_near** = fraction of starts ending within 0.01 of best sampled endpoint → accessibility of a good basin.
2. **g_med** = median(e_i − e_min) → typical cost of landing in the wrong basin.
3. **p_poor** = fraction of starts ending >0.05 above best → how often local search is materially misdirected.
4. **Minima per line** = mean local minima along random wrapped 1D lines (optionally Fourier entropy for wavelength concentration) → directional multimodality.

Rule: `g_med` and `p_poor` (quality spread) outrank minima count for the local-vs-global decision. Local Hessian conditioning is NOT diagnostic — difficult basin organization coexists with mild local curvature.

## Landscape-Design Levers (what to change when diagnostics are bad)

The classical objective E(θ)=⟨ψ(θ)|H|ψ(θ)⟩ is shaped JOINTLY by three levers; they move the diagnostics independently:

- **Physical model**: frustration, mixed locality (e.g. 2+3-local couplings), chemistry Hamiltonians → mixed locality gave FEWER but more separated low-energy regions.
- **Ansatz class**: hardware-efficient vs Hamiltonian-variational vs QAOA layers.
- **Parameterization** (the subtle one):
  - *Parameter tying* (share one angle across r layers): keeps search dimension low but couples each variable across stages — this is the regime that creates basin heterogeneity AND where DE wins. Parameter count is a poor proxy for difficulty.
  - *Nonlinear reparameterization*: folds simple physical motion into multimodal coordinates.
  - *Independent depth increase*: raises minima count WITHOUT raising quality spread → don't switch optimizers for depth alone.

## Workflow

1. Exact (statevector) evaluation of E(θ); normalize to ε_phys.
2. Run 64–128 random-start BFGS in the bounded parameter box; collect endpoints.
3. Compute p_near, g_med, p_poor; run ~8 wrapped random-line probes for minima/line.
4. Decide: p_near high & g_med low → multistart local. g_med high & p_poor large → allocate budget to adaptive DE (jSO-class), which keeps improving late in the budget.
5. If bad diagnostics: redesign parameterization (untie, linearize coords) before blaming the optimizer.

## Scope & Limits

- Exact objectives only (no shot noise): BFGS reliability degrades under finite-shot noise; DE tolerates stochastic evaluations better but noise inflates its budget. Do not transfer rankings quantitatively to hardware.
- No barren plateaus in studied instances — this methodology addresses basin-structure difficulty, a separate trainability mechanism from gradient-magnitude collapse.
- Endpoint statistics relate to optimizer behavior more directly than pullback/Fubini–Study metrics or Hessian spectra; don't conflate these geometric descriptions.

## Reusable Beyond Quantum

The diagnostic pair (multimodality count vs endpoint-quality spread) transfers to any nonconvex objective where model construction is under your control: neural architecture parameter sharing (tied weights in recurrent/shared-depth networks behave like tied QAOA angles), physics-informed losses, and hyperparameter landscapes.
