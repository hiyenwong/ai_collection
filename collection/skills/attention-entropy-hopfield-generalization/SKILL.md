---
name: attention-entropy-hopfield-generalization
description: "Use for attention-Hopfield REM phase diagram, memorization."
category: ai_collection
---

# Attention Entropy: Generalization vs Memorization in Exponential Hopfield Networks

arXiv 2610.22191 (Alemanno, 2026) — "Attention over noisy examples: generalization and memorization in the exponential Hopfield network". Transfers the *Hebbian learning from examples* protocol to the exponential Hopfield model, whose zero-temperature update is one softmax-attention step with training examples as keys/values. Yields a closed-form phase diagram of when an attention head generalizes (retrieves an unseen archetype) vs memorizes (returns the closest training example), and identifies overfitting as the freezing transition of a Random Energy Model (REM).

## Core Setup

- Archetypes ξ^μ ∈ {−1,+1}^N (never shown). Dataset: M blurred examples per archetype, η_i^{μa} = ξ_i^μ χ_i^{μa}, P(χ=±1)=(1±r)/2. Query = fresh example of quality q.
- Control parameters: load α = K/N, dataset entropy ρ = (1−r²)/(Mr²), softmax inverse temperature β (logit scaled βN·m). Quality relation: **r = 1/√(1+ρM)**.
- One update: h_i = Σ_b w_b k_{b,i}, w_b = softmax(βN·m_{k_b}(σ)); σ^{(1)} = sign(h). This IS one attention head (keys=values=examples, query=state).
- Observables: W = Σ_a w_{1a} (weight on correct class), M_eff = (Σw)²/Σw² (participation ratio of within-class weights; M_eff=M → pools all, M_eff=O(1) → condensed), n_max = max overlap with a training example (→1 means memorization), m^{(1)} = overlap with archetype (generalization).

## Closed-Form Theory (signal-to-noise analysis)

**One-step magnetization** (majority-rule form with attention entropy):
```
m(1) = erf( 1/√(2·ρ_eff) ),      ρ_eff = V / (rW + τq)²,   τ = tanh β
V = (1−r²)W²/M_eff  +  (1−W)²/(K−1) · (r² + (1−r²)/M_eff)  +  τ²(1−q²)
```
**Weight of correct class** (annealed approx, valid x ≲ √(2 ln M)):
```
W(β) = [1 + (K−1)·exp(−Nβqr + Nβ²r²/2)]⁻¹
```
**Condensation of the softmax** (REM over M within-class levels, x = β√(N(1−r²))):
```
M_eff = M·Φ_M(x),   Φ_M(x) = E[(Σ e^{xz_a})² / (M·Σ e^{2xz_a})],  z_a iid N(0,1)
Φ_M(0)=1;  Φ_M ≈ 1−(1−M⁻¹)x² for small x;  freezing at x_c = √(2 ln M)
frozen phase (x > x_c): E[Σ_a w_a²] = 1 − x_c/x  (Poisson–Dirichlet weights)
```

## The Three Regimes (phase diagram in (β, ρ))

Generalization window **β_lo < β < β_hi** with edges of different scaling:
```
β_lo = ln[(K−1)(1+ρ)/ρ] / (2Nqr)        (crosstalk edge, scales 1/N)
β_hi ≈ √(2 ln M / (N(1−r²)))            (condensation edge, scales 1/√N)
⇒ window widens as √N; optimal β* ≈ 1.3–1.8 × β_lo
```
1. **Crosstalk** (2βNr² ≲ ln K): W ≪ 1, correct class drowned by K−1 wrong classes — pairwise-like, ρ_eff ≈ ρ + (1+ρ)(1−W)²/[(K−1)W²].
2. **Prototype** (ln K ≲ 2βNr², x ≲ 1): W→1, M_eff≈M, ρ_eff→ρ, **load drops out** — crosstalk ∼ e^{−Nβ}, so learnable archetypes grow as **exp(c√N)** (Eq 19: window non-empty iff (K−1)(1+ρ)·√(2N ln M) ≲ 2r²/(ρ√(1−r²))). Labels unneeded: softmax finds the correct class by itself.
3. **Memorization** (x ≳ √(2 ln M)): softmax freezes on the training example closest to the query; n_max→1, m^{(1)}→r (+selection bias). Overfitting = REM freezing = **1-RSB**, vs full-RSB spin glass in the pairwise model. The exponential model is the least glassy member of the Hebbian family (REM is p→∞ of p-spin).

**Maximum of m(1) lies inside the window**: pooling loss (∝x²) and crosstalk (∝e^{−Nβ}) balance when pooling/crosstalk = Nβ*r²·ln K; optimum does NOT remove crosstalk, stops when it is a 1/ln K fraction of pooling loss. W* < 1 at optimum (0.39–0.75 in explored range).

## Reusable Diagnostics & Methods

1. **Memorization diagnostic for any attention head whose keys are examples**: compute participation ratio M_eff of attention weights; drop to O(1) = memorization. Departure of M_eff/M from Φ_M(x) measures data structure (sub-clusters: F-MNIST condenses later with a tail; MNIST follows Φ_M exactly).
2. **Real-data calibration**: replace theoretical (r, q) by measured mean m̄ and conditional std σ_m of within-class overlaps m_{η^{μa}}(σ⁰): ρ = Nσ_m²/(M·m̄), x = βNσ_m (= β√(N(1−r²)) on synthetic data). Window formula: β_lo = ln[(K−1)(1+ρ)/ρ]/(2N·m̄), β_hi = √(2 ln M)/(N·σ_m).
3. **Structured-data operating point**: on hierarchical classes (sub-clusters per class) the class prototype is a poor target; the best accuracy lies BEYOND the condensation edge (β ≈ 2.3–2.4 β_hi on MNIST/F-MNIST, M_eff/M ≈ 0.01–0.04), where softmax reads out a **local sub-prototype** — temperature does what a hidden layer of sub-prototypes did in [13].
4. **Hebbian reading of gradient descent**: first CE-gradient steps are Hebbian (keys ∝ class sums → prototypes); later steps fit example noise (gap grows with noise 1−r²); weight decay ~1e-2 on keys restores prototype alignment (cosine 0.4→0.7) and test accuracy. Early stopping / weight decay = distance from Hebbian solution.
5. **Iterated vs single application**: with keys=examples, fixed points of the iterated softmax map are the EXAMPLES; the unseen archetype is an attractor only for ρ ≲ 0.06. Single application generalizes over a wider range — one reason feed-forward attention use is not a loss.

## Verified Implementation Sketch (MC, all checks PASS 2026-10-16)

```python
import numpy as np
from math import erf, sqrt, log, exp, tanh
rng = np.random.default_rng(42)

def phi_M(x, M, ntrial=20000):                     # participation ratio of REM Gibbs measure
    if x == 0: return 1.0
    z = rng.standard_normal((ntrial, M)); e = np.exp(x*z)
    return float(((e.sum(1)**2) / (M*(e**2).sum(1))).mean())

def one_attention_step(N, K, M, rho, beta, q=None):
    r = 1/sqrt(1 + rho*M);  q = q or r            # fresh test example
    xi = rng.choice([-1,1], (K, N))               # archetypes (never trained on)
    chi = rng.choice([-1,1], (K, M, N), p=[(1-r)/2,(1+r)/2])
    eta = xi[:,None,:] * chi                       # examples = keys = values
    chi0 = rng.choice([-1,1], N, p=[(1-q)/2,(1+q)/2])
    sigma0 = xi[0]*chi0                            # query of archetype 1
    keys = eta.reshape(K*M, N)
    w = np.exp(np.log(np.clip(beta*N*(keys@sigma0)/N, -500, None)))
    w = np.exp(beta*(keys@sigma0) - (beta*(keys@sigma0)).max()); w /= w.sum()
    Wc, Meff = w[:M].sum(), (w[:M].sum()**2)/(w[:M]**2).sum()
    s1 = np.sign(w @ keys)                        # one-step output
    m1 = (xi[0] @ s1)/N                           # generalization overlap
    nmax = ((keys @ s1)/N).max()                  # memorization overlap
    return dict(W=Wc, Meff=Meff, m1=m1, nmax=nmax, r=r)

def rho_eff(rho, r, q, beta, W, Meff, K, M):       # Eq (15)
    tau = tanh(beta)
    V = (1-r**2)*W**2/Meff + (1-W)**2/(K-1)*(r**2+(1-r**2)/Meff) + tau**2*(1-q**2)
    return V/(r*W + tau*q)**2

# Window edges
# beta_lo = log((K-1)*(1+rho)/rho)/(2*N*q*r);  beta_hi = sqrt(2*log(M)/(N*(1-r**2)))
# m1 theory = erf(1/sqrt(2*rho_eff)) — valid while Meff/M > 0.3; overestimates by ≤0.1 once condensed
```

**Verification status (N=1000, K=100, M=16, ρ=0.2)**: W(β) within 0.005 of MC at all six β from crosstalk to memorization; M_eff=Φ_M·M within 0.2; m(1)=erf(1/√(2ρ_eff)) within 0.02 while Meff/M>0.3, overestimate 0.08–0.11 in condensed regime (matches paper's Remark 2); REM frozen-phase E[Σw²]=1−x_c/x confirmed at x=10 (x=5 is the expected finite-M crossover); small-x expansion exact. Window edges β_lo=0.013, β_hi=0.085 (ratio 6.4, grows with N).

## When to Use

- Analyzing/designing attention heads over small example sets (few-shot, retrieval-augmented, kNN-attention) — choose β inside the window to pool the correct class, or beyond β_hi deliberately for local sub-prototype readout on clustered data.
- Diagnosing memorization vs generalization in attention: participation ratio of weights is the direct observable; theory curve Φ_M(x) is the null (exchangeable keys).
- Theorizing attention temperature (softmax sharpness) scaling with model/data size: crosstalk edge ~1/N, condensation edge ~1/√N.
- Connects: dense associative memory / Modern Hopfield (Krotov-Hopfield, Ramsauer et al.), learning from examples in pairwise nets, REM (Derrida), hierarchical REM for ultrametric sub-clusters. Distinct from storage-capacity results: here capacity for LEARNING from examples is exp(c√N), limited by condensation not crosstalk.

## Limits

- Gaussian SNR theory quantitative only while softmax pools many examples (M_eff/M ≳ 0.3); error ≤0.1 once condensed.
- Unstructured data assumption; structured classes need hierarchical REM (levels of condensation ↔ ultrametric organization).
- Single head, binary vectors, noiseless dynamics; extension to learned projections (logits ≠ overlaps) open.

## Reference

- arXiv:2610.22191 — F. Alemanno, "Attention over noisy examples: generalization and memorization in the exponential Hopfield network" (15 Oct 2026, 15pp). Code: github.com/francescoalemanno/hebb-attention
- Related: phase-kernel-dense-associative-memory (capacity via phase kernels), kernel-hopfield-*.skills (attractor geometry), exponential Hopfield storage capacity (Lucibello-Mézard PRL 2024).
