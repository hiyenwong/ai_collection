---
name: energy-constrained-two-way-pure-loss-capacities
description: "Pure-loss channel two-way capacities Q2=K=g(N)-g((1-n)N)."
category: ai_collection
trigger: two-way capacity, secret-key capacity, pure-loss channel, energy-constrained quantum Shannon theory, bosonic channel converse
---

# Energy-Constrained Two-Way Capacities of the Pure-Loss Channel

**arXiv**: 2610.12365 (Falco, Mele, Lami, Giovannetti — Scuola Normale Superiore Pisa / Caltech IQIM / NEST, submitted 8 Oct 2026)

## Core Result (Theorem 1.1)

For the single-mode pure-loss channel `L_η` (transmissivity `η ∈ [0,1]`) under average input photon-number constraint `N`:

```
Q₂(L_η, N) = K(L_η, N) = g(N) − g((1−η)N)
```

where `g(x) = (x+1)log₂(x+1) − x·log₂ x` is the thermal entropy function. This is **the last missing capacity formula for the pure-loss channel**, completing the full capacity picture of bosonic quantum communication under pure loss.

- Both capacities equal the **reverse coherent information** of the two-mode squeezed vacuum (TMSV) — achievability matches converse exactly.
- Model: adaptive LOCC (unbounded two-way classical communication), no preshared entanglement, energy constraint `(1/n)Σᵢ Tr[n̂ρ̄_Sᵢ] ≤ N` on unconditional inputs; authenticated public classical channel; Eve gets all channel environments + transcript.
- Limits: `N=0` or `η=0` → 0; `η=1` → `g(N)`; `N→∞` → `−log₂(1−η)`, recovering the PLOB unconstrained capacity [PLOB17].
- For `η ≤ 1/2` the unassisted quantum/private capacity `Q = P = max{0, g(ηN) − g((1−η)N)}` vanishes, but `Q₂ = K` stays positive (e.g. `η=1/2, N=1` gives ≈0.6226 qubits/use) — two-way assistance rescues communication in the strong-loss regime.

## Reusable Proof Methodology

The paper is a template for solving channel-capacity converse problems with energy constraints. Four modular techniques:

### 1. Covariance-based LOCC simulation (Section 2.2)
If a channel `T` is covariant under a compact group whose **input representation is irreducible** (`T(U_g ρ U_g†) = W_g T(ρ) W_g†`), it is exactly simulable by LOCC from its normalized Choi state `Ω_T`:
- Alice measures input + her Choi half with the Bell POVM (Haar measure; finitely many outcomes suffice by finite weighted convexity / Schur's lemma);
- Conditional on outcome g, Bob applies `W_g†` — implementing T exactly, also on inputs correlated with other systems.
- Consequence: for ANY input ρ, `ER(output) ≤ ER(input) + ER(Ω_T)` — the resource term is independent of local memories.

### 2. Photon-number sector decomposition (Section 3)
- Fix k photons in m modes: sector `H_{m,k} = Sym^k(C^m)`, dim `d_k = C(m+k−1,k)`; passive mode transformations `U∈U(m)` act as `U^⊗k` restricted to the sector — irreducible representation.
- Symmetric-subspace resolution: `∫|u;k⟩⟨u;k| dμ(u) = π_k = Π_{m,k}/d_k`.
- Condition on J = number of photons LOST: `Pr(J=j|k) = C(k,j) q^j η^{k−j}` with `q=1−η` — binomial, state-independent (proof via Vandermonde's identity on the branch isometries).
- Branch identity: `V_{k,j}|u;k⟩ = |u;k−j⟩_B |u;j⟩_E` — environment marginals of sector Choi states are π_j.
- Sector entanglement bound with an EXPLICIT separable witness: `σ_{k,j} = ∫|ū;k⟩⟨ū;k|_R ⊗ |u;k−j⟩⟨u;k−j|_B dμ(u)` gives `ER(Ω_{k,j}) ≤ log₂d_k − log₂d_j`, and convexity yields `ER(Ω_{m,k}) ≤ c_m(k) := log₂d_k − Σⱼ b_{k,j} log₂d_j`.

### 3. Dephasing cost accounting (Lemma 2.1 + Step 1 of Lemma 4.1)
Coherences between photon-number sectors cost at most the Shannon entropy of the sector distribution:
```
ER(ρ) ≤ ER(Δρ) + D(ρ‖Δρ) ≤ ER(Δρ) + H(K)
```
This is the required "non-lockability" bound (cf. HHHO05a): dephasing cannot increase relative entropy of entanglement by more than H(K). Phase covariance `Δ_B ∘ L_η = L_η ∘ Δ_S` (channel intertwines phase rotations `e^{iθN̂}`) reduces the unconditioned case to sector-wise bounds plus the entropy penalty:
```
ER(ω) − ER(ρ) ≤ H(K) + E log₂ d_K − E log₂ d_J
```

### 4. Amortized regularization + privacy test (Corollary 4.2 + Lemma 5.1)
- **Thermal comparison (Step 3)**: auxiliary states `ζ = Σ p_k π_k` and `ζ' = L_q^{⊗m}(ζ)` satisfy `S(ζ) − S(ζ') ≤ m·f_η(ν)` via data processing against tensor thermal states (binomial thinning `L_q(τ_x) = τ_{qx}`); the leftover `H(J) ≤ g(qmν)` by comparison with a geometric distribution.
- **Amortization**: group r copies — residual dephasing cost `g(qrν)` grows only logarithmically in r, so divided by r it vanishes: `ER^∞(output) ≤ ER^∞(input) + f_η(ν)`.
- **Infinite-dimensional limit (Step 4)**: finite-rank projections `T_L` filter down; trace-norm convergence + lower semicontinuity of ER (LS23 Cor. 20) lift the finite-dimensional bound — no entropy assumption on memories needed.
- **Privacy test**: for a private state `γ` with key dimension d and privacy-test projector `Π_γ = U(Φ_d ⊗ I)U†`: `Tr(Π_γ ω) ≥ F(ω,γ)` and `Tr(Π_γ σ) ≤ 1/d` for every separable σ. Tensor-power counting via expansion of `(I+(2^t−1)Π)^⊗r` and subset bounds `d^−|S|` converts a fidelity promise into `ER^∞(ω) ≥ (1−ε)log₂d − h₂(ε)` — **dimension-independent of shield systems**.
- **Adaptive telescoping (Prop 5.2)**: keep all would-be-discarded local systems; intermediate LOCC maps cannot increase ER^∞; per use i the state gain is ≤ f_η(νᵢ); Jensen (f_η concave — `f''(x) = −η/(ln2·x(x+1)(qx+1)) ≤ 0`, nondecreasing) gives `Σᵢ f_η(νᵢ) ≤ n·f_η(N)`.
- **Error conversion**: key error e → private-state infidelity ε = 2e−e² via Uhlmann + shield-space unitary extension (countably infinite Schmidt complement).

### Achievability (Section 5.3)
Feed TMSV `|ψ_N⟩ = √(1/(N+1)) Σ (N/(N+1))^{k/2} |k⟩|k⟩` through the channel; Bob→Alice reverse hashing (Devetak–Winter [DW05], GPLS09) achieves `S(R) − S(RB) = g(N) − g(qN)` per mode. A finite-dimensional truncation (Fock cutoff L) preserves the exact photon budget: means converge, relative entropies to thermal states → 0. Measuring distilled maximally entangled states yields the same number of secret bits → `f_η(N) ≤ Q₂ ≤ K ≤ f_η(N)`.

## Key Lessons / Patterns

- **Exact capacity collapse**: achievability (reverse coherent information of TMSV) and converse (amortized regularized ER) meet at a single-letter thermal-entropy expression — rare in quantum Shannon theory, where regularized quantities usually stay open.
- **Memory-correlated inputs handled by amortization**, not by assuming product structure — the ER^∞ telescoping absorbs arbitrary adaptivity/LOCC.
- **Symmetry simulation beats squashing**: earlier two-way bosonic upper bounds used squashed entanglement (loose); exact covariant-LOCC simulation from irreducible sector representations gives the tight bound.
- **Energy constraint smooths the converse**: photon budget → concavity → Jensen step; unconstrained PLOB recovered as `N→∞` limit.
- **Privacy test survives regularization**: the tensor-power argument is shield-dimension-independent — this is what makes the KEY converse work where naive ER arguments fail.
- AI note (from the paper): the main result was obtained on 17 Sep 2026 **with a single prompt of ChatGPT Astra (OpenAI)**, independently confirmed by [Pir26a] — an existence proof of AI-assisted theorem discovery in quantum Shannon theory.

## Application Checklist

When facing a converse problem for a quantum channel capacity with constraints:
1. Check for compact-group covariance with irreducible input action → try exact LOCC simulation from the Choi state.
2. Decompose the input space into irreducible sectors (photon-number sectors here); compute sector-wise ER bounds with explicit separable witnesses.
3. Bound the cost of sector coherences by the Shannon entropy of the sector variable (non-lockability).
4. Amortize over r copies; verify residual terms are o(r) (logarithmic growth suffices).
5. For KEY rates: convert final protocol state to an approximate private state (Uhlmann + shield extension), then apply the tensor-power privacy test — never a naive single-copy ER bound.
6. Apply Jensen to the per-use bound under the constraint budget (check concavity of the per-use function).
7. Match with a Gaussian achievability scheme (TMSV + reverse hashing / Devetak–Winter).

## Full Capacity Table (single-mode pure-loss, reference N=1)

| Capacity | Formula | Assistance | Ref |
|---|---|---|---|
| C (classical) | g(ηN) | none | GGL+04 |
| CE (classical) | g(N)+g(ηN)−g((1−η)N) | entanglement-assisted | GLMS03 |
| QE (quantum) | CE/2 | entanglement-assisted | BSST02 |
| Q = P | max{0, g(ηN)−g((1−η)N)} | none | WHG12, WQ18 |
| **Q₂ = K** | **g(N)−g((1−η)N)** | **two-way LOCC (this paper)** | 2610.12365 |

## Related Local Skills
- `no-go-gaussian-quantum-repeaters` — Gaussian repeaters cannot beat direct transmission on pure-loss channels (the unconstrained counterpart this paper completes)
- `ppt-entanglement-distillation` — PPT distillation analysis (related bosonic channel program)
- `post-quantum-crypto-security-bounds` — key-rate security bounds program

## References
- [PLOB17] Pirandola-Laurenza-Ottaviani-Banchi — unconstrained bound `−log₂(1−η)`
- [DSW18] Davis-Shirokov-Wilde — energy-constrained two-way capacity framework
- [DW05] Devetak–Winter — distillation of secret key and entanglement
- [GPLS09] Giovannetti-Lloyd-Maccone-Shor — reverse coherent information achievable rates
- [WTB17] Winick-Tomamichel-Berta — privacy test lemmas
- [LS23] Lower semicontinuity of relative entropy of entanglement
- [Pir26a] independent simultaneous result (noted in paper)
