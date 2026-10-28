---
name: p-adic-avalanches-upper-critical-dimension
description: Use for p-adic/ultrametric neural avalanche criticality.
category: ai_collection
trigger: p-adic neuroscience, ultrametric neural network, neural avalanche exponent 3/2, upper critical dimension, Taibleson-Vladimirov operator, hierarchical connectome criticality, Buice-Cowan field theory
---

# p-Adic Hierarchical Neural Avalanches: Upper Critical Dimension Nc = 2σ

Source: W. A. Zúñiga-Galindo, "Hierarchical connectivity sets the upper critical dimension of neural avalanches", arXiv:2610.36404 (cond-mat.dis-nn, q-bio.NC, Oct 2026). Mathematical companion: arXiv:2610.36400 (exact discretization, operator uniqueness, heat-kernel estimates, one-loop equations). Simulation code/data: https://wazuniga.github.io/padic-BC/

## When to use

- The cortical-avalanche puzzle: Beggs–Plenz τS = 3/2 demands mean-field directed percolation (DP), but Euclidean DP has upper critical dimension Nc = 4 and a cortical sheet is effectively N = 2–3 → Euclidean theory with local coupling predicts anomalous exponents (1D: τS ≈ 1.108). Use this framework when hierarchical/modular/self-similar connectivity is the missing ingredient.
- Predicting whether avalanche statistics are mean-field from measurable hierarchical coupling decay (extract σ from connectome data organized by modules; falsifiable prediction).
- Modeling neural dynamics on ultrametric (p-adic) neuron spaces, log-periodic/discrete-scale-invariance signatures in neural data, or Dyson-hierarchical-style criticality in brain models.

## Core mechanism: connectivity selects the diffusion operator

1. **p-adic neuron space.** Neurons are points of Q_p^N (ultrametric: strong triangle inequality, balls are disjoint or nested). p-adic distance between two neurons = level of their last common ancestor in the module tree. A depth-l network G_l = (Z_p/p^l Z_p)^N is an EXACT restriction of the continuum theory (no lattice-spacing approximation: fields constant on balls of radius p^(-l) give the same action for every l).
2. **Buice–Cowan effective-spike model.** Spikes decay at rate α; neuron i fires at rate f(Σ_j w_ij n_j), f(0)=0 (absorbing state), f'(0)>0, f''(0)<0 (saturation). Doi–Peliti action S = ∫ φ̃(∂t + μ + W)φ + ... Mean-field equation = hierarchical Wilson–Cowan: ∂t a = −αa + f(w⋆a).
3. **Kernel → operator selection (the key step).** In R^N every short-range kernel reduces to −D∇² (finite second moment, Taylor expansion). Over Q_p^N locally constant functions have NO Taylor expansion → no reduction: each kernel keeps its own operator. The self-similar hierarchical kernel w(∥x∥p) = Cw·∥x∥p^(−N−σ) (attenuation p^(−(N+σ)) per level) selects EXACTLY the Taibleson–Vladimirov operator D^σ (the unique isotropic pseudodifferential operator on Q_p^N homogeneous of degree σ): symbol A_w(ξ) = κW·∥ξ∥p^σ, with κW = f'(0)·Cw·(1−p^(−σ−N))/(p^σ−1). Heat kernel has power-law tails Zt(x) ≍ κW·t·[(κW·t)^(1/σ) + ∥x∥p]^(−N−σ).
4. **Ultrametric DP universality.** Reggeon field theory with W replacing −D∇² keeps rapidity reversal. Power counting: [ψ]=[ψ̃]=N/2, [g]=σ−N/2, z=σ → **Nc = 2σ**. Mean-field exponents above Nc (exact): β=1, ν∥=1, ν⊥=1/σ, z=σ, τS=3/2; log corrections at N=Nc.
5. **Euclidean contrast.** Lévy-flight DP also gives Nc=2σ but ONLY for σ<2 (σ≥2 → finite second moment → Laplacian → Nc=4). Over Q_p^N NO local operator exists → every σ>0 is a distinct universality class, Nc=2σ ranges over (0,∞): N=1 needs σ≤1/2, N=2 needs σ≤1 for mean-field τS=3/2. Unlike DP on a Cayley tree (mean-field for any coupling due to exponential site growth), this is Dyson-hierarchical-like.

## Ginzburg criterion (fluctuation vs mean-field validity)

- One-loop correction small iff (g²/4)·I2(μ) ≪ 1 with I2(μ)=∫d^Nξ/[μ+A_w(ξ)]². I2(0) finite ⟺ N>2σ.
- For N<2σ, as μ→0+: I2(μ) ≃ (1−p^(−N))·κW^(−N/σ)·μ^(N/σ−2)·Φ(s), μ/κW = p^(σs), Φ(s)=Σ_{k∈Z} p^((k−s)N)/(1+p^(σ(k−s)))² — periodic in s, period 1.
- In ultrametric diffusion length ℓW=(κW/μ)^(1/σ): **(1−p^(−N))/4 · g²/κW² · ℓW^(2σ−N) · Φ(s) ≪ 1**. g² ∝ f'(0)|f''(0)| = spike-count noise from branching+saturation (vanishes for linear f → mean-field exact). Physical reading: perturbation spreads over a ball of ℓW^N neurons during lifetime 1/μ; if N>2σ the ball outgrows the noise → mean-field improves approaching criticality; if N<2σ coupling decays too fast up the hierarchy → fluctuations dominate near criticality.
- Finite network (diameter L): mean-field fails in the window p^(−l) ≪ ℓW ≪ L only if Ginzburg number Gi = g²·L^(2σ−N)/κW² ≳ 1; otherwise finite-size rounding comes first.
- **Log-periodic signature**: Φ(s) makes the criterion periodic in ln μ with period σ·ln p (discrete scale invariance x→p^(−1)x, t→p^σ t — impossible in continuous-scale Euclidean theory). Amplitude of first harmonic ≈ |ω1|·e^(−π|ω1|), ω1=2π/(σ ln p): negligible for p=2 (~5e−11), 2e−3 for p=7, 0.07 for p=31, 0.24 for p=101. Measurable log-periodicity ⟹ large σ ln p (coarse hierarchy).

## Simulation protocol (validated against exact controls)

- Tree p=2, N=1, l=40 → **2^40 ≈ 1.1×10^12 neurons** (⚠ pdftotext AND fitz both render this as "240 neurons" — superscript drop; confirmed by Fig. 3 caption "l=40" and boundary-never-reached statement). w_ij ∝ 2^(−k(1+σ)) for smallest common module of 2^k neurons. No self-coupling, Σw=1, α=1, f(s)=fmax(1−e^(−s/s0)), s0=0.25.
- Event-driven Gillespie + thinning: each spike attempts downstream spike at rate b=f'(0)·w0/α, target chosen ∝ w_ij/w0, accepted with probability f(s_i)/[f'(0)s_i] — saturation exact, no approximation.
- Spreading from single seed (Grassberger–de la Torre): locate critical b_c by bisection requiring pure power-law N(t) to t=10³; 2×10⁵ runs; P(t)∝t^(−δ), N(t)∝t^ϑ on 30≤t≤10³; τS by truncated power-law MLE (10≤S≤2000, Clauset–Shalizi–Newman) AND scaling relation τS = 1 + δ/(1+ϑ+δ).
- Controls calibrate fit bias ≈ +0.03: pure branching (δ,ϑ,τS)=(1,0,3/2); 1D DP chain (0.159, 0.314, 1.108).
- Results (N=1): σ=0.25 → τS≈1.53 (mean-field); σ=0.5=N/2 → 1.46–1.49 (log corrections); σ=0.75 → 1.36–1.39; σ=1 → 1.28–1.32; σ=1.5 → 1.17–1.23 → approaching 1D DP 1.11. b_c drifts from 1 (1.000) to 3.157 as σ grows.
- **Mechanism**: small σ → most new spikes land far from active neurons (ultrametric: most pairs are far) → no crowding → branching avalanches; large σ → activity trapped in small modules → crowding + saturation penalties → non-mean-field.

## Reuse patterns

- Substitute for Euclidean dimension whenever a brain network is hierarchical: the coupling-decay exponent σ (not spatial dimension) is the control parameter for universality.
- Recipe for falsification from data: (1) organize connectome into module hierarchy, (2) fit log(w) vs hierarchical level → slope −(N+σ), (3) theory predicts mean-field iff σ ≤ N/2.
- The kernel→operator selection lemma generalizes: ANY isotropic translation-invariant dynamics on Q_p^N picks D^σ with σ set by the kernel tail — reusable for nonlocal p-adic Wilson–Cowan, p-adic cellular neural networks (Zúñiga-Galindo & Zambrano-Luna), ultrametric diffusion models.
- Griffiths-phase extension (Moretti–Muñoz): quenched level-dependent heterogeneity should produce extended critical regions interpolating between the sharp p-adic transition and modular-network Griffiths phases.

## Pitfalls

- N counts neuron-space dimensions ONLY; time is an extra coordinate (as in Buice–Cowan).
- Do not interpret "240 neurons" in the extracted text literally — it is 2^40 (verified superscript corruption).
- Adding the same constant to all layer gates shifts every cycle mean equally → critical structure depends only on relative gates (same invariance as the max-plus layer-composition model in arXiv:2610.37587).
- p-adic RG (Lerner–Missarov; Abdesselam–Chandra–Guadagni) needed for exponents at N<2σ; not yet computed analytically — the simulation interpolation between 3/2 and Euclidean DP is the only current evidence.
- Log-periodic corrections are NOT numerical noise: they are the discrete-scale-invariance signature, but with amplitude ~e^(−π²/(σ ln p)) they are invisible for fine hierarchies (p=2).

## Related

- Buice–Cowan field theory of spiking networks (PRE 75, 051919 (2007)) — directed-percolation class of the absorbing-state transition.
- Dyson hierarchical model; Parisi ultrametricity in spin glasses (here the ULTRAMETRICITY IS IN THE ARCHITECTURE, not the state space).
- Companion paper arXiv:2610.36400 — full mathematical construction (operator selection/uniqueness, heat kernels, loop-corrected hierarchical Wilson–Cowan, small-world property, self-organization).
- Contrast skills: griffiths-phase-brain-criticality (disorder mechanism), hierarchical-brain-criticality (empirical), neutral-theory-neural-dynamics (non-critical null), self-organized-criticality frameworks — this skill supplies the CONNECTIVITY-GEOMETRY mechanism for why 3/2 appears at low embedding dimension.
