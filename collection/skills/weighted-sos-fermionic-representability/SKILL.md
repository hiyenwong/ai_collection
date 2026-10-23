---
name: weighted-sos-fermionic-representability
description: Weighted-SOS witnesses for fermionic RDM representability.
category: ai_collection
source_title: "A constructive solution to the n-representability problem"
source_arxiv: "2610.20737"
---

# Weighted SOS Fermionic n-Representability

**Source**: Rubin & DePrince III (Google Quantum AI / FSU), arXiv:2610.20737 (Oct 2026). Constructive solution to the 60-year fermionic quantum marginal (n-representability) problem: a complete, parameterized family of ALL two-body witnesses at each level of a weighted sum-of-squares (wSOS) hierarchy, replacing ad-hoc representability conditions (DQG, T1T2') with systematic algebra.

## When to Use
- Certifying physicality of a candidate 2-particle reduced density matrix (2-RDM) in v2RDM methods
- Deriving tight lower-bound energy certificates for chemistry Hamiltonians (avoiding sign problem of QMA-completeness in practice)
- Generating complete constraint sets for SDP relaxations over fermionic marginals
- Any noncommutative polynomial optimization with a fixed-particle-number constraint

## Core Methodology

### 1. Degree-d SOS cone as Gram matrices
Let `o_1...o_L` be distinct normal-ordered fermionic monomials of degree ≤ d (in `a_i, a†_i`), vector `o⃗_d`. Every sum-of-squares operator `W = Σ_k R_k†R_k` equals `W = o⃗_d† G o⃗_d` with `G ⪰ 0` (Gram factorization `G = C†C`; rows of C give the R_k). The cone: `Σ_d = {Φ_d(G) : G ⪰ 0}`.

### 2. Nullspace truncation (the two-body projection)
Products `o_i† o_j` normal-order to operators of degree up to 2d. Collect the expansion coefficients `Γ_ij^{(m,γ)}` (via Wick's theorem w.r.t. true vacuum). Require ALL degree-m>4 coefficients to vanish:

```
A_trunc(d) vec(G) = 0     (one linear row per high-degree operator O_γ^(m), m>4)
```

**Theorem (completeness)**: `Σ_{d,≤2} = {Φ_d(G) : G ⪰ 0, A_trunc(d)vec(G)=0}` — the nullspace conditions capture EVERY at-most-two-body operator admitting a degree-d SOS representation. Nullspace basis `{B_ℓ}` gives `G = Σ_ℓ x_ℓ B_ℓ ⪰ 0` — an SDP over PSD cone × free coordinates.

### 3. Weighted SOS (why unweighted SOS is incomplete)
An unweighted SOS is nonnegative on ALL of Fock space; a valid p-particle witness only needs nonnegativity on the fixed-p sector (may have negative eigenvalues on N≠p). The fix — multiply by the particle-number projector weight: define `W_N(f) = f·r + r·f†` where `r = N − η` (η = target particle number) and f is a Hermitian, particle-conserving multiplier polynomial of degree ≤ 2d−2. The weighted cone `w_n Σ_d` = SOS + allowed multiplier terms, with joint nullspace cancellation: **sextic SOS and multiplier coefficients cancel JOINTLY** (neither vanishes separately — this is the key SDP structure):

```
max E_SOS
s.t.  h − E_SOS·e_0 = A_{≤4} g + B_{≤4} z
      0            = A_6 g + B_6 z
      G ⪰ 0, z unrestricted
```

Free Hermitian multiplier matrices split as `F(q) = P_q − M_q` with both PSD — 6 PSD blocks represent the multiplier exactly (dimensions 1, R, R² for q=0,2,4).

### 4. Degree-2 multiplier sufficiency (main theorem)
`E*_{3,2} = E*_{3,4}` — degree-≤2 particle-number multipliers preserve the supremal energy bound at every SOS level d ≥ 2 when the FULL generator space V_d is used. Proof technique: write the quartic multiplier shift as cubic cross terms `Σ_i φ_i* Z_i + Z_i* φ_i ∈ V_3` (with `φ_i = Σ F_{pq;is} a†_s a_q a_p`, `Z_i = a_i r`), then complete the square and absorb the difference into a new SOS member. Higher-degree multipliers are NEVER needed.

### 5. CAR normal-ordering identity (the engine)
`E_{2k}(I;J)·N = k·E_{2k}(I;J) + Σ_s E_{2k+2}(Is; Js)` — this converts the particle-number constraint into RDM consistency relations: trace(1RDM)=η, 2RDM→1RDM contraction, 3RDM→2RDM contraction. The multiplier polynomial is exactly what supplies the missing 2-RDM↔3-RDM consistency maps that v2RDM DQGT1T2' lacks.

## Numerical Result
Richardson pairing Hamiltonian (8 modes, 3-particle sector): DQG and DQGT1T2' both give lower bounds BELOW exact energy; the complete degree-3 wSOS recovers the EXACT ground-state energy within solver accuracy (residual 1e-5 Frobenius). Software: p†q fermionic computer algebra + libsdp. Multiplier degrees 0 (scalar) insufficient; 2 and 4 both exact (and provably equal).

## Workflow
1. Enumerate normal-ordered monomial basis V_d for d ≤ n (particle number)
2. Symbolically normal-order all `o_i† o_j` (Wick/CAR) → coefficient tensor Γ
3. Build A_trunc(d) from all degree>4 coefficients; compute nullspace basis {B_ℓ} symbolically
4. Set up weighted SDP with joint sextic cancellation (A_6 g + B_6 z = 0)
5. Solve SDP (libsdp/similar first-order solver); energy = certified lower bound

## Pitfalls
- Unweighted SOS misses witnesses negative off the p-sector — fixed-particle simulations REQUIRE the weighted form
- The 2012 constructive claim was incomplete: it did not exhaust the two-body witness cone for fixed particle number
- Nullspace equations must be derived symbolically (generic structure), not for one basis size — index-permutation mapping for (I,J) needed since A_σ(I)A_τ(J)† normal-orders to non-canonical label orderings
- Particle conservation partitions G by level sets S_η (ΔN(σ)=η): xxxx/xxox.../ooxx/... — enforce per block, not per entry

## References
- Rubin & DePrince III, arXiv:2610.20737 (2026)
- NPA hierarchy connection: Doherty-Parrilo-Spedalieri 2010 noncommutative optimization
- p†q library (fermionic symbolic algebra); v2RDM DQG/T1T2' conditions as subcones
