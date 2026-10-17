---
name: grover-walk-pst-abelian-cayley-classification
description: Complete algebraic classification of perfect state transfer in Grover walks on Cayley graphs.
category: ai_collection
trigger_words: [perfect state transfer, Grover walk, Cayley graph, abelian group, discrete-time quantum walk, algebraic integer, Chebyshev polynomial, connection set, circulant graph, quantum state routing, vertex-transitive graph]
---

# Grover Walk Perfect State Transfer on Abelian Cayley Graphs — Complete Classification

**Source**: Bhakta & Bhattacharjya, arXiv:2610.21946 (math.CO/quant-ph, IIT Guwahati, Oct 2026). Complete classification of connected Cayley graphs over finite abelian groups exhibiting perfect state transfer (PST) in Grover walks — closing the valency question beyond 4 and extending Kubota–Yoshino's circulant classification (JCTA 2025) to ALL finite abelian groups.

**Numerically verified 2026-10-16**: all 3 positive cases (τ_min matches theory exactly) + 3 anti-examples confirmed via Chebyshev recurrence simulation.

## Core Results

### Theorem 1.2 (Valency restriction, ANY finite group)
If Cay(Γ,S) exhibits PST then |S| ∈ {1, 2, 4}. **No Cayley graph with valency 3 or ≥5 exhibits PST in Grover walks** — for any finite group, not just abelian.

### Theorem 1.3 (Valency-4 characterization)
For abelian Γ with |S|=4, ⟨S⟩=Γ: PST ⟺ ∃ a,h ∈ Γ with **ord(h)=2**, **4 ∤ |Γ|/2**, and
**S = {a, −a, a+h, −a+h}**.
Transfer is always from u to **u+h only**, at minimum time **τ_min = lcm(2, |Γ|/2)**.

### Theorem 1.4 (Complete classification up to group isomorphism)
All PST-realizing pairs (Γ,S), up to equivalence:
| Case | Γ | S | h | τ_min |
|------|-----|-----|-----|-------|
| (i) | Z₂ | {1} | 1 | 1 |
| (ii) | Z₂×Z₂ | {(1,0),(0,1)} | (1,1) | 2 |
| (iii) | Z₂ₙ, n≥2 | {1,−1} | n | n |
| (iv) | Z₂ₘ, m≥3, 4∤m | {±1, m±1} | m | lcm(m,2) |
| (v) | Z_m×Z₂, m≥6, m≡2 (mod 4) | {(±1,0),(±1,1)} | (0,1) | lcm(m,2) |

## Reusable Methodological Patterns

### Pattern 1: Chebyshev discriminant bridge (Grover walk → classical spectrum)
The vertex-type state Φu = N*e_u evolves as: **N U^τ N* = T_τ(P)** where P = N R N* is the *discriminator* (random-walk matrix P = A/d for d-regular G) and T_τ = Chebyshev of the first kind. **PST from u to v ⟺ T_τ(P) e_u = e_v** — and crucially the phase γ is forced to **+1** (proof: apply √deg-weighting w with Pw=w ⇒ γ=1; no complex phases survive).
- Use this whenever analyzing coined/bipartite DTQW dynamics: project the arc-space unitary U down to vertex space via N, study the WALK OF A MATRIX through T_τ(P), never the 2|E|-dim space directly.

### Pattern 2: Vertex-transitivity upgrade (single vertex ⇒ permutation matrix)
For Cayley graphs: **PST between one vertex pair ⟺ T_τ(P) is a fixed-point-free involutory permutation matrix**. Since T_τ(P) is a polynomial in A, it commutes with ALL translations M_x; one transfer forces the full permutation structure σ(x)=x+h, σ²=id, h an involution. **|Γ| is forced even**.
- General principle: on a vertex-transitive graph, verify the spectral condition at ONE vertex, then the group action propagates it everywhere. Conversely, uniqueness: for abelian Cayley graphs T_τ(P) = M_{v−u} exactly (Lemma 4.1), so the transfer partner is u+h and no one else.

### Pattern 3: Algebraic-integer eigenvalue sieving (the key novelty)
The engine of the impossibility proofs, transferable to ANY "spectral values must lie in intersection of two rings" argument:
1. **PST ⇒ every eigenvalue µ of P satisfies T_τ(µ) = ±1 ⇒ µ = cos(jπ/τ) ⇒ 2µ is an algebraic integer** (Lemma 2.5).
2. **Regularity ⇒ dµ is an algebraic integer** (eigenvalue of integer matrix A).
3. Odd d: µ = dµ − (d−1)/2·(2µ) is itself an algebraic integer; all conjugates lie in [−1,1] ⇒ **µ ∈ {−1,0,1}** (Kronecker-style Lemma 2.6); then T_τ(P) ∈ {P, I, 2P²−I} can never be fixed-point-free. **Kills all odd valencies > 1.**
4. **Trace inequality Lemma 2.7**: for symmetric rational M with all-algebraic-integer eigenvalues, trace(M²) ≥ rank(M), and if 2 ∈ Spec(M) then trace(M²) ≥ rank(M)+3. With trace(B²)=4n/d and ker-dimension bounds: **d < 8**. **Kills all valencies ≥ 8.**
- Residual valency 6 eliminated by the 2×2 block decomposition below.

### Pattern 4: Involution block decomposition (σ-pairing of vertices)
T_τ(P) = [[O,I],[I,O]] pairs vertices {x_i, y_i}, y_i = x_i + h. Commutativity AT_τ(P)=T_τ(P)A forces **A = [[C,D],[D,C]]**. The ±1 eigenspaces of T_τ(P) reduce B=2P to two m×m blocks **B± = (2/d)(C±D)** with trace formula trace(B±²) = m(4±r)/d·... (r = # common neighbors of paired vertices, provably even, vertex-independent by transitivity). Spectral radius bounds on B−: every eigenvalue of B− in [−1,1] with all conjugates ⇒ Spec(B−) ⊆ {−1,0,1}; parities of τ (mod 4) then force **B− = 0 ⇒ C = D ⇒ S + h = S** — the connection set is invariant under the transfer involution. This is the structural fingerprint: **PST connection sets are h-symmetric coset unions**.

### Pattern 5: Translation-matrix diagonalization (why the classification terminates)
Abelian ⇒ A = Σ_{s∈S} M_s with M_s commuting permutation matrices ⇒ simultaneous eigenbasis (characters χ): eigenvalue at χ is (1/|S|) Σ_{s∈S} χ(s). The explicit τ_min computations close via cos-identities: e.g. case (iii) P = (M₁+M₋₁)/2 gives T_t(P) = (M^t + M^{−t})/2, so T_n(P) = M_n exactly when n ≡ −n (mod 2n). **Transfer time arithmetic = modular condition on powers.**

## When to Use

- Designing/verifying quantum state routing on graph-based discrete-time quantum walks (coined Grover walks): the (Γ,S) table IS the complete hardware design space for abelian topologies.
- Ruling out PST quickly: valency ∉ {1,2,4} or connection set not h-symmetric ⇒ impossible without further computation.
- Any spectral-graph-theory impossibility proof needing "eigenvalues in Z̄ ∩ [−1,1] ⇒ {−1,0,1}" or trace-vs-rank algebraic-integer inequalities.
- Contrast with the Szegedy signed-graph approach (`szegedy-signed-graph-quantum-routing`): that route ENGINEERS PST via phase gadgets on general graphs; this classification gives the CLOSED-FORM complete design space for the abelian Cayley subclass with no engineering freedom.
- Extends continuous-time PST intuition: DTQW PST is strictly rarer (CT walks admit PST on more graphs; the Grover coin constraint + γ=1 forcing is what enables the tight classification).

## Numerical Verification Protocol (reused from this session)

```python
# Verify PST claim on Cay(Γ,S) in O(n³·τ):
# 1. Build P = A/d for d-regular Cayley graph via translation closure
# 2. Recurrence T_0=I, T_1=P, T_{t+1}=2P·T_t − T_{t−1}
# 3. PST from u to v at τ ⟺ T_τ(P)[:,u] == e_v  (γ=1 forced)
# Verified: Z6×Z2 case(v) τ=6 ✓; Z6 case(iv) τ=6 ✓; Z10 cycle τ=5 ✓;
#           Z8 S={1,7,3,5} (4|m) no PST ✓; Z14 valency-6 no PST ✓; K4,4 no PST ✓
```

## Key References
- Kubota & Yoshino, JCTA 216 (2025) 106064 — circulant valency ≤4 classification (base case extended here)
- Kubota & Segawa, LAA 646 (2022) — Chebyshev discriminant method N U^k N* = T_k(P)
- Guo & Schmeits, EJC 33(4) (2026) — phase γ=1 forcing
- Zhan, QIP 18:369 (2019) — first infinite valency-4 circulant PST family
- Bhakta & Bhattacharjya, arXiv:2610.21946 (this paper)
