---
name: chimera-higher-order-neuronal-hypergraphs
description: Use when modeling chimeras on neuronal hypergraphs.
category: ai_collection
trigger: chimera states, neuronal hypergraph, higher-order interactions, FitzHugh-Nagumo, clique projection, attractive-repulsive coupling
---

# Chimera States in Neuronal Hypergraphs with Higher-Order Interactions

Methodology from arXiv:2610.31997 (Nguessap, Njougouo, Ferreira, Oct 2026, nlin.AO): a generalized
framework for FitzHugh–Nagumo (FHN) neuronal networks on d-uniform hypergraphs with competing
attractive chemical and repulsive electrical many-body coupling, plus a systematic comparison against
clique-projected pairwise networks. Central lesson: **chimera emergence is governed by the functional
form of coupling and the attractive/repulsive balance — not by topology or interaction order alone**;
clique projections can preserve, suppress, OR promote chimera states relative to the original hypergraph.

## Model

Isolated FHN (excitable regime): `εẋ = x − x³/3 − y`, `ẏ = x + a`, with ε = 0.05, a = 0.5.

Hypergraph dynamics (d-uniform, (d+1)-body hyperedges, adjacency tensor A^(d)):

```
εẋᵢ = xᵢ − xᵢ³/3 − yᵢ
      + σe · Σ_{j1..jd} A^(d)_{i,j1…jd} [ P^(d)(x_j1,…,x_jd) − xᵢ ]      (electrical, repulsive: σe < 0)
      + σc · (x_s − xᵢ) · Σ_{j1..jd} A^(d)_{i,j1…jd} Π_ℓ S(x_jℓ)          (chemical, attractive: σc > 0)
ẏᵢ = xᵢ + a
```

Electrical polynomial P^(d) (odd under simultaneous sign reversal; diffusive-like, vanishes at sync):
- d odd:  `P^(d) = Π_{ℓ=1}^{d} x_jℓ`, degree p_d = d
- d even: `P^(d) = x_j1² · Π_{ℓ=2}^{d} x_jℓ`, degree p_d = d+1 (permutation invariance restored by tensor symmetry)
- Property: `P^(d)(x,…,x) = x^{p_d}` → coupling vanishes under complete synchronization.

Chemical sigmoid: `S(x) = 1/(1+exp(−λ(x−θ_s)))`, λ = 10, θ_s = −0.25, reversal potential x_s = 2.0.

### Clique projection (pairwise counterpart)
Replace each hyperedge by a complete graph, matching effective order with exponent q:

```
εẋᵢ = xᵢ − xᵢ³/3 − yᵢ + σe Σ_j A_ij [x_j^q − xᵢ^q] + σc (x_s − xᵢ) Σ_j A_ij [S(x_j)]^q
```

Biophysical mapping (key interpretive tool):
- Hypergraph multiplicative chemical coupling ≈ **NMDA coincidence detection / dendritic supralinear integration**
- Clique pairwise summation ≈ **AMPA linear integration**
Same structural connectivity, fundamentally different interaction rules — coupling form matters as much as topology.

## Simulation protocol
- N = 504 FHN oscillators, nonlocal nonregular topology (chimera-enhancing, per Ref [42])
- RK4, dt = 0.05, T = 1500 time units (3×10⁴ steps); discard first 97% as transient
- Sweep (σe, σc) 2-D parameter space for d = 2, 3, 4 (3-, 4-, 5-body hyperedges)

## Strength of Incoherence (SI) classifier
`zᵢ = xᵢ − x_{i+1}` (periodic boundary), partition into M equal bins, local std σ_m per bin, then
`SI = 1 − (1/M) Σ_m Θ(δ − σ_m)`. SI ≈ 0 coherent; SI ≈ 1 incoherent; 0 < SI < 1 → chimera.

## Key findings
1. Increasing d contracts the coherent region; at d = 4 incoherence dominates much of parameter space.
2. Genuine HOIs often support **broader chimera regions** (d=2: broad SI≈0.5 zone for σe<0.2 that is
   strongly suppressed under clique projection).
3. Clique projection qualitatively reproduces d = 2 but diverges progressively for d = 3, 4
   (d = 4 shows numerically divergent trajectories in parts of the space).
4. **Counter-intuitive regime**: clique projections can exhibit well-formed chimeras where the original
   hypergraph is FULLY incoherent — d=3 at (σe,σc)=(−0.066, 0.408), d=4 at (−0.025, 0.18).
5. Consequence: pairwise reduction does NOT simply suppress chimeras (contra prior refs [39,42,44]);
   it qualitatively REORGANIZES the dynamics. Chimera formation depends on coupling-function form +
   attractive/repulsive balance.

## When to use
- Modeling collective brain dynamics with hypergraphs/simplicial structures beyond pairwise synapses
- Deciding whether a higher-order neuronal model can be replaced by a pairwise (clique) approximation
- Studying epilepsy-onset analogies (chimera collapse) or unihemispheric-sleep-like partial coherence
- Designing FHN/Kuramoto-style chimera sweeps with excitatory-vs-inhibitory (chemical vs electrical) balance

## Implementation skeleton
```python
# hyperedge interaction, per node i, over hyperedges containing i
# d odd:  P = np.prod(X[j, :d], axis=0);  d even: P = X[j,0]**2 * np.prod(X[j,1:d], axis=0)
# electrical: sigma_e * (P - x_i);  chemical: sigma_c * (x_s - x_i) * np.prod(S(X[j,:d]))
# clique:    sigma_e * (x_j**q - x_i**q) + sigma_c*(x_s-x_i)*S(x_j)**q
# SI: z = np.roll(x, -1) - x ... wait: z_i = x_i - x_{i+1}; bin std over M bins; SI = 1 - mean(Heaviside(delta - sigma_m))
```
Sweep (σe ∈ [−0.15, 0], σc ∈ [0, 0.5]) coarsely first; refine near SI≈0.5 boundaries; verify candidate
chimera parameter points with spatiotemporal plots + snapshots (chimera = coherent blob + incoherent background).

## Pitfalls
- Even-d polynomial is not individually permutation-invariant; the full coupling IS via tensor symmetry + summation.
- Strongly repulsive σe drives SI→1 (full incoherence) — chimera lives at intermediate balance, easy to miss on coarse grids.
- d = 4 clique projections can numerically diverge; clip/monitor trajectories.
- SI bin count M and threshold δ must match Ref [50] (Gopal et al.) conventions for comparability.

## References
- arXiv:2610.31997 — source framework (attractive chemical + repulsive electrical HOIs, d=2..4)
- Gopal et al. — Strength of Incoherence measure
- Kuramoto & Battogtokh 2002 / Abrams & Strogatz 2004 — chimera states
- Andrzejak et al. 2016 — chimera collapse vs epileptic seizure analogies
