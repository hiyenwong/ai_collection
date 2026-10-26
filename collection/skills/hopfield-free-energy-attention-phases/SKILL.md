---
name: hopfield-free-energy-attention-phases
description: Use for attention free-energy phase transitions.
---

# On the Statistical Mechanics of Attention (arXiv:2610.17347)

**One-line**: Transformer attention as the equation of motion of a modern-Hopfield free-energy landscape; sparse (α>1) attention admits first-order glassy↔robust-inference phase transitions with hysteresis, dense softmax (α=1) does not.

- **Authors**: Jerry Yao-Chieh Hu, Yu-An Chen, Maojiang Su, Han Liu (Northwestern / NTU)
- **Submitted**: 2026-10-12; cs.LG + cond-mat.dis-nn
- **Verified**: central formulas re-derived and numerically confirmed (branch crossing, spinodal Hessian zero, sparsemax retrieval map) at ε=0.30, d=64 — all match to 1e-5.

## Core Construction

1. **Free energy of a modern Hopfield model (MHM)** — patterns ξ∈R^{d×M}, query x∈R^d, overlap z_µ = ξ_µᵀx/√d:
   - Joint energy: H[x,p,ξ] = ½‖x‖² − Σ_µ z_µ p_µ, p on the M-simplex.
   - Generalized free energy: Γ_α(x) = (β/2)‖x‖² − Ω*_α[βz], where Ω*_α is the Fenchel conjugate of the NEGATIVE Tsallis entropy Ω_α = −Ψ_α.
   - Attention emerges as the equation of motion: ∇_z Γ = −βp ⟹ retrieval maps (Prop 3.3): α→∞ hardmax, α=2 sparsemax p_µ=(β/2)[z_µ−θ]₊, 1<α<2 entmax, α→1 softmax exp{βz_µ}/Σexp{βz_ν}.
   - The α-parameter IS the entropy choice: Tsallis α controls sparsity, hence which attention family the EOM realizes. Unifies temperature, entropy, sparsity, fluctuations in one object.

2. **Phase structure (the paper's main result)**:
   - **Sparse regime (α=2)**: retrieval states form multiple metastable branches. Coexistence point = energy crossing of branches (Def 4.2); spinodal = Hessian eigenvalue zero, branch annihilates (Def 4.3). FIRST-ORDER transitions with HYSTERESIS between up/down β-sweeps — glassy ↔ robust-inference phases.
   - **Dense regime (α=1, softmax)**: single branch, no hysteresis, continuous sharpening with β. No phase-transition-like behavior.

3. **Critical thresholds (well-separated keys, Gram G_µν = δ_µν + ε(1−δ))**:
   - Coexistence (k=1 vs k=2 branches): **β_coexist = 2/(1−ε)**
   - Spinodal of the k=2 branch: **β_jump = 2/(1−ε)** (they coincide under uniform + well-separation assumptions; in general β_jump ≠ β_coexist — Remark 4.2).
   - General spinodal: β_jump = 2/λ_max(PGP), P = I − 11ᵀ/k projector of the active support.
   - Hessian along antisymmetric direction: λ(β) = β − (β²/2)(1−ε) — crosses zero exactly at β*.

4. **Memory load κ = log(M)/d**: as κ grows, z_max decreases stepwise (delocalization); branch energies all decrease but retrieval accuracy falls — a **capacity-reliability trade-off**. Hysteresis window in κ as well.

5. **Thermal attention (Appendix D)**: with fluctuating queries/keys, EOMs become escort moments ∇_z W_α = βp^(esc); α→1 recovers Gibbs conditional expectation E[p|x]; α>1 amplifies high-density regions (sharper attention); 0<α<1 softer. Retrieval = Landau response: z_µ acts as an external field on the simplex.

## Verified Numerical Protocol (reproduce in ~30 lines of NumPy)

```python
# Two patterns, Gram [[1,eps],[eps,1]], d=64, eps=0.3
# Gamma(x) = beta/2*||x||^2 - Omega*_2[beta*z],  S_2(p)=1-||p||^2
# k=1 branch x1 = xi1/sqrt(d):        Gamma_k1 = -beta/2        (beta > beta*)
# k=2 branch x2 = (xi1+xi2)/(2 sqrt d): Gamma_k2 = -beta(1+eps)/4 - 1/2
# Coexistence: Gamma_k1 - Gamma_k2 = beta*eps/4 - 1/2 = 0  => beta* = 2/(1-eps)
# Spinodal: d2/dw2 along antisymmetric w: beta - (beta^2/2)(1-eps) = 0 => same beta*
```
Checked: crossing at β*=2.857143 both analytic & numeric (Γ=−1.428571); Hessian 0.000004≈0 at β*; p*=(β/2)[z−θ]₊ reproduces exact simplex argmax.

## Practical Implications (paper Sec 6 + G.2/G.3)

- **Attention should match the task**: trained-Transformer experiments — sparsemax wins selective retrieval (highest top-1 accuracy + least support/IRP); softmax wins uniform-aggregation over many relevant values. entmax-1.5 interpolates.
- **Path dependence**: in the sparse regime, raising vs lowering β (temperature annealing direction) selects DIFFERENT memories — retrieval depends on the continuation path and the initial query. Frozen-β inference: training at β=1 then inferring at high β breaks multi-memory aggregation (selectivity mismatch).
- **Memory-load cost**: context length M (exponential load κ=log M/d) monotonically reduces retrieval reliability in ALL attention families — a phase-diagram way to state context-interference.
- **Design rule**: pick α by task structure (sparse selection vs dense aggregation); β must be matched between train and inference; long contexts need redundancy or retrieval chunking to dodge the delocalization regime.

## When to Use / Triggers

- Analyzing softmax/sparsemax/entmax as a family from one free-energy object
- Predicting attention-map behavior under temperature (β = inverse-temperature of the score scaling) changes
- Explaining hysteresis or metastability in attention outputs under context-length sweeps
- Choosing attention sparsity α for selective vs aggregative downstream tasks
- Associative-memory view of KV-cache retrieval, context interference, capacity limits

## Key Formulas (quick reference)

| Object | Expression |
|---|---|---|
| Overlap | z_µ = ξ_µᵀx/√d |
| Free energy | Γ_α(x) = (β/2)‖x‖² − Ω*_α[βz] |
| Sparsemax map | p_µ = (β/2)[z_µ − θ]₊, Σp=1 |
| Softmax map | p_µ = exp(βz_µ)/Σ_ν exp(βz_ν) |
| Coexistence/spinodal (well-sep) | β* = 2/(1−ε) |
| General spinodal | β_jump = 2/λ_max(PGP) |
| Memory load | κ = log(M)/d |
| Tsallis-2 entropy | Ψ_2(p) = 1 − ‖p‖² |

## Relation to Existing Skills

- Complements `attention-entropy-hopfield-generalization` (that covers exponential-Hopfield learning from noisy examples; THIS covers the free-energy phase structure of the retrieval/inference side).
- Complements `phase-transition-attention-bayesian` (Bayesian emergence of attention patterns); here the transition is thermodynamic, with spinodal/coexistence formalism.
- The hysteresis finding mirrors freezing-melting physics (first-order transition analogy, Enninful et al. glass literature).

## Limitations (paper's own)

- Fixed-memory setting; no learned-key/query co-evolution across layers/heads.
- Prescribed correlation structures; realistic noise across Transformer depth untreated.
- Full-Transformer phase structure (heads × layers) remains open.
