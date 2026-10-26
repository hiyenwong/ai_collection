---
name: ahgq-affine-pricing-group-quantization
description: "AHGQ: unify affine pricing operator and Riccati transform via group quantization + thin-path holonomy. Use for geometric finance, Heston/CIR structure."
category: ai_collection
trigger: affine pricing, group approach quantization, holonomy, Riccati flow, symplectic transport finance, Heston geometric structure, thin-path groupoid, Poincare-Cartan pricing
---

# Affine Holonomy Group Quantization (AHGQ) for Affine Pricing Models

**Source**: arXiv:2609.28863 (Santiago García, Sep 2026, q-fin.MF)

## Core Idea

Affine pricing models (Black-Scholes, Vasicek, CIR, Heston) have two standard formulations that are usually treated as separate facts:
1. **Coordinate-space pricing operator** L^A (PDE generator)
2. **Exponential-affine transform** governed by **generalized Riccati ODEs**

AHGQ shows both arise as **complementary polarizations of one geometric structure** (Group Approach to Quantization, GAQ, of Aldaya–de Azcárraga; Kostant–Souriau geometric quantization lineage). The contribution is structural organization, not new formulas.

## The Affine Pricing Symbol

State x ∈ R^d, conjugate momentum p (doubles as the transform variable). Collect ALL model coefficients (drift b, linear drift B, covariance A₀ + Σx_jA_j, killing c + dᵀx) in one phase-space function:

```
C^A(x,p) = F(p) + xᵀ R(p)
F(p)  = bᵀp + ½pᵀA₀p − c                       (state-independent part)
R(p)  = Bᵀp + (½pᵀA₁p, ..., ½pᵀA_d p)ᵀ − d     ("Riccati symbol": becomes RHS of Riccati ODEs)
```
Financial admissibility: A(x) = A₀ + Σ x_jA_j ⪰ 0 (positivity needed only for finance, NOT for the geometry).

## The Two-Sector Decomposition (the central trick)

Split the symbol by geometric role:
```
C^A = C_s + C_H
C_s(x,p) = ½pᵀA₀p + xᵀBᵀp     (homogeneous quadratic sector)
C_H(x,p) = bᵀp − xᵀd − c + ½Σ_j x_j·pᵀA_jp   (complementary affine sector)
```

**Chain 1 — symplectic sector (finite-dimensional, exact)**:
```
C_s → K_s (Hamiltonian matrix, K_sᵀJ + JK_s = 0) → M_s(t) = exp(tK_s) ∈ Sp(2d,R)
    → G_s := R ⋉_{M_s} R^{2d}  (semidirect-product Lie group)
    → central extension G̃_s = G_s × R₊ via symplectic 2-cocycle ε²_s(g',g) = ½a'ᵀM_s(t)ᵀJa
```
Note the central fiber is **R₊ (positive scale/discount factor), not U(1) phase** — the geometric-quantization phase becomes a pricing scale.

**Chain 2 — holonomy sector (path-dependent)**:
```
C_H → α_H = C_H(x,p)dt (1-form on G_s) → thin-path groupoid G_A ⇒ G_s
    → H_H[γ] = exp(−∫_γ C_H(x,p)dt)   (multiplicative holonomy; H_H[γ₂∘γ₁] = H_H[γ₂]H_H[γ₁])
```
Thin-homotopy invariance: dα_H is a 2-form, thin homotopies have rank ≤1 differentials, so Stokes gives invariance. Holonomy acts on the R₊ central fiber: ζ ↦ ζ·H_H[γ].

**State-dependent covariance (A_j ≠ 0) lives in the holonomy sector** — this is where CIR/Heston's x-proportional volatility enters the geometry.

## Affine Poincaré–Cartan Form

Combine: vertical field V_H = −C_H·Ξ (Ξ = ζ∂_ζ central generator); affine time lift E^A = L_t^s + V_H. Horizontality restored by adding C_H dt:

```
Θ = dζ/ζ + ½(−aᵀJ_{2d}da) + C^A(x,p)dt = dζ/ζ + ½(pdx − xᵀdp) + C^A dt
curvature: ω = −dxᵀ∧dp + dC^A∧dt
```

**Characteristic field** (rank-1 characteristic module, dt(X_Θ)=1):
```
X_Θ = ∂_t + R(p)ᵀ∇_p − (b + Bx + A(x)p)ᵀ∇_x + η^A(x,p)Ξ
η^A = ¼(pᵀ∇_p + xᵀ∇_x)C^A − ½C^A = ¼c − ½bᵀp + ¼(pᵀ(A(x)−A₀)p + xᵀd)·...
```
(The linear drift B does NOT contribute to the central amplitude η^A.)

## Polarizations → the Two Standard Representations

### Momentum polarization → Riccati transform (Prop 6.1)
```
P_mom = span{L_x1..L_xd}:  Ψ_mom = ζ·exp(½xᵀp)·χ(t,p)
Reduced operator:  X_Θ^mom = ∂_t + R(p)ᵀ∇_p − F(p)
Characteristics:  ṗ = R(p)          ← generalized Riccati system
                  χ̇ = F(p)χ         ← scalar amplitude (affine transform exponent)
Propagator:  K(t;x;u) = exp(φ(t,u) + ψ(t,u)ᵀx),  φ(t,u) = ∫₀ᵗ F(ψ(s,u))ds
European price:  V = ∫_Γ K(t,x;u)·f̂(u)du  (superpose propagated transform modes)
```
Scalar Riccati components (Heston, CIR) integrable via projective SL(2,C) flow.

### Coordinate polarization → pricing PDE (Prop 6.2)
```
P_coord = span{L_p1..L_pd}:  Ψ_coord = ζ·exp(−½xᵀp)·V(t,x)
Canonical operators (transport-rotated right-invariant fields):
  P := ∇x + ½pΞ  →  ∇x ;   X := −∇p + ½xΞ  →  x ;   [P, Xᵀ] → I_d
Ordered symbol Ĉ^R = F(P) + XᵀR(P) reduces to:
  L^A = (b + Bx)ᵀ∇x + ½Tr(A(x)∇x²) − c + dᵀx     ← standard affine pricing operator
Consistency: (∂_t − L^A)K = 0 — the momentum propagator solves the coordinate PDE.
```

## Model Instantiations (fill-in tables)

| Model | F(p) | R(p) | C_s | C_H |
|---|---|---|---|---|
| Black-Scholes | (r−δ−σ²/2)p + ½σ²p² − r | 0 | ½σ²p² | (r−δ−σ²/2)p − r |
| Vasicek | ½σ²p² + κθp | −κp − 1 | ½σ²p² − κxp | κθp − x |
| CIR | κθp | ½σ²p² − κp − 1 | −κxp | κθp − x + ½σ²xp² |
| Heston | (r−δ)p_x + κθp_v − r | (½(p²ₓ−p_x), (ρσ_v p_x − κ)p_v + ½σ²_v p²_v) | −½vp²ₓ + κvp_v | rest |

CIR specialization: ṗ = ½σ²p² − κp − 1, φ̇ = κθp — standard CIR Riccati; unit payoff p(0)=0 → K = exp(φ + ψx).

## Boundary Case (credit modeling, Appendix B)

- Affine rate-linked default intensity: stays INSIDE the construction
- Inverse-power equity intensity: produces **discrete momentum translations** → breaks finite-dimensional Riccati closure → outside affine class (nonlocal transform dynamics, future work)

## Reusable Patterns

1. **Symbol decomposition as modeling compass**: any quadratic-in-momentum generator splits into (i) an exactly tractable symplectic sector (closed Lie group, no approximation) and (ii) a multiplicative path-holonomy sector. Decide which model features land in which sector BEFORE choosing solution methods.
2. **R₊ central fiber instead of U(1)**: geometric quantization machinery repurposed for pricing/discounting scales — portable to other semiclassical finance constructions (path-integral pricing, phase-space actions: L^A = ½pᵀẋ − ½xᵀṗ + C^A).
3. **Polarization = representation switch**: momentum polarization → transform methods (Riccati); coordinate polarization → PDE methods. Both provably consistent via the shared characteristic field — useful when a model needs closed-form transform AND PDE numerics on the same footing.
4. **Riccati symbol R(p) as data structure**: collect all state-dependent drift/covariance/killing coefficients into one vector-valued function; the Riccati ODEs, the pricing operator, and model classification all read off from (F, R) alone.
5. **Closure test for extensions**: adding a new model feature preserves affine tractability iff its contribution to R(p) stays polynomial of degree ≤ 2 in p (inverse-power intensity fails this — momentum translations).

## Pitfalls

- The construction is time-homogeneous, continuous-path only; jumps/Lévy need extension.
- Positivity A(x) ⪰ 0 is a financial requirement, not geometric — the machinery runs without it, but prices may be invalid.
- Coordinate polarization closes under time evolution only when A₀ = 0 (Heston, CIR fine; Black-Scholes/Vasicek Gaussian models need care — momentum polarization always closes).
- B (linear drift) is invisible to the central amplitude η^A — errors in B do not show up in η diagnostics.

## Related Skills / KG

- `mathematical-quantization` — Kohn-Nirenberg / Lie group quantization, affine group cocycles (same lineage)
- `flow-loops-quantum-groups` — quantum group invariants + Morse theory
- KG id=2717 Quantum Advantage in Trading (q-fin.TR); id=9183 coherent-feedback H∞ quantum control (Riccati)
