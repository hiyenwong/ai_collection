---
name: ft-resource-estimation-uncertainty-propagation
description: Use when reporting quantum resource estimates as intervals.
category: ai_collection
version: "1.0.0"
source: arXiv:2610.10490
source_title: "Standard estimators cannot represent fault-tolerant workloads at measured error rates: evaluated, evidence-based uncertainty for quantum resource estimation"
authors: "Furqan Nasir, Sher Jeel Ahmad (FAST-NUCES, City University Peshawar, UET Peshawar)"
published: 2026-10-07
categories: quant-ph, quantum-error-correction
trigger_words:
  - fault-tolerant resource estimation
  - surface code cost model
  - uncertainty quantification
  - evidence-based prior
  - Shapley sensitivity
  - censoring envelope
  - physical qubit interval
  - magic-state factory
  - post-quantum cryptography migration
---

# Evidence-Based Uncertainty Propagation for Fault-Tolerant Resource Estimation

## Core Method

A resource estimator maps hardware/architecture parameters **x** = [p_phys, t_cycle, τ_factory, γ_route, t_decode] through cost model f to output y = (physical qubits, code distance, runtime, factory requirement). Since parameters carry evidence-based priors p(x), the honest estimate is a **distribution p(y) = ∫ f(x,W) p(x) dx**, not a point.

## Three Coupled Findings (RSA-2048/ECC-256/AES-256/Hubbard-QPE on superconducting surface code)

1. **Parametric uncertainty is large**: median measured 2Q gate error across 5 large-array devices (Willow 3.0e-3, Heron 2.96e-3, Zuchongzhi-3 3.8e-3, Sycamore 5.0e-3) is **4.0×10⁻³ — 4× the 10⁻³ planning convention**. Propagating this widens the 90% physical-qubit interval to **~40× span** (RSA-2048: 2.86×10⁷ → 1.18×10⁹) and lifts the median **4.6× above** the conventional point estimate (1.01×10⁸ vs 2×10⁷).
2. **Structural disagreement is real**: 5 independently structured cost models (analytic Fowler-2012, Litinski-2019 lattice surgery, compact-block Fowler-Gidney, Azure QRE, Qualtran) disagree by a **stable factor of 2.0** at matched inputs; the two third-party tools agree with each other to ~10% (ECC-256: <1%), bracketing the band — model-form uncertainty no single tool reveals.
3. **Standard estimators censor the measured regime**: Azure QRE (code-distance cap 50) censors 80.9% of evidence-based draws for RSA-2048; Qualtran (fixed distillation factory) censors 95.4%; feasible only up to ~1.7×10⁻³ error — **below the measured median 4×10⁻³**. AES-256 T-count 6.07×10⁴³ overflows Azure's 64-bit gate counter (max ~1.8×10¹⁹) outright. Loosening the error budget 50× only drops Azure censoring 81%→71%.

## Framework Components (qre-uq, open, tool-agnostic)

- **Single input/output schema + thin adapters**: each backend estimator gets an adapter translating a fixed parameter record (with platform tag) to native inputs; quantities a tool cannot compute are reported as **missing, never zero** — failure region becomes observable data.
- **Evidence-based prior library**: per-parameter truncated lognormal fitted by weighted maximum likelihood on documented measurement tables (conventions unified: Pauli error ↔ average-gate error converted before fitting). Elicitation hazards handled: correlated sources grouped, small-scale records down-weighted, **survivorship factor 1.3** (typical deployed device underperforms best reported chip) — swept and sensitivity reported.
- **Correlated-input sensitivity**: Sobol indices lose clean variance interpretation under dependence → **Shapley effects as primary** (exact 5-input from 32 subset costs under Gaussian copula coupling error rate↔cycle time).
- **Pre-registered three-layer evaluation** (OSF 3d9m2): Layer 1 numerical correctness (closed-form benchmark quantiles within 2% tolerance), Layer 2 leave-one-source-out prior-predictive coverage (**sensitivity-weighted primary metric** reaches ~99% at nominal 90%; pooled 62% shortfall comes entirely from low-sensitivity params like decoder reaction time), Layer 3 expanding-window hindcast (exploratory; misses are downward = technological drift, not miscalibration).
- **Censoring as measurement**: draws where a backend fails are retained as missing-valued rows with success flag false → the fraction of evidence-space a tool cannot represent is itself a reported result.

## Reusable Patterns

1. **Never report a point resource estimate**: report interval + censored fraction + error-rate assumption. A migration deadline anchored at the 10⁻³ convention is pinned to the low end of a 40×-wide, upward-shifted distribution.
2. **Convention-vs-evidence gap as first-class result**: tools provisioned at the planning point (distance cap, fixed factory) silently refuse most of measured parameter space — the mismatch itself is the finding, robust across independently-built tools that hit the wall by different mechanisms (cap vs factory budget).
3. **Model-form uncertainty band**: run several defensible cost models on identical draws; max/min median ratio (~2×) is the structural uncertainty. Third-party concordance inside the band converts "we tuned a spread" into evidence.
4. **Inverse-transform sampling with truncation via quantile-range restriction** (preserves Latin-hypercube/Sobol space-filling structure rather than discarding out-of-range points); single seed fully determines a run; shard-splitting for resumable long sweeps.
5. **Sensitivity-weighted coverage**: judge calibration by how much each parameter drives the output, not naive pooling — pooled coverage is dominated by irrelevant wide-design priors (routing overhead, factory throughput) that don't affect the interval.
6. **Honest scope labeling**: "evaluated" means the dominant parameter's calibration is tested and holds — not full validation against reality; exploratory layers labeled as such; survivorship factor reported as judgment with sensitivity sweep (removal shrinks magnitudes 4.6×→2.9×, 40×→23× span, conclusions survive).

## Key Numbers

| Workload | Median qubits | 90% span | Azure censor | Qualtran censor |
|---|---|---|---|---|
| RSA-2048 | 1.01×10⁸ | 41× | 80.9% | 95.4% |
| ECC-256 | 4.54×10⁷ | 41× | 86.8% | 99.7% |
| AES-256 | 1.32×10⁹ (T-overflow) | 41× | 100% | 100% |
| Hubbard QPE | 1.61×10⁷ | 41× | 79.8% | 97.6% |

## Application Checklist

- [ ] Fit priors from documented measurement tables (unify error conventions first)
- [ ] Group non-independent sources; down-weight unrepresentative records; add + sweep survivorship factor
- [ ] Push priors through ≥2 structurally distinct cost models + ≥2 third-party tools via adapters
- [ ] Record censored fraction per tool as a headline output
- [ ] Compute Shapley (not Sobol) effects under copula-coupled dependence
- [ ] Pre-register evaluation metrics before confirmatory runs; report sensitivity-weighted coverage
- [ ] Output = interval + censored fraction + assumption statement, never a bare point
