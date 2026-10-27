---
name: delay-phase-reduction-neural-mass
description: Use when reducing delayed neural-mass nets to phase models.
category: ai_collection
version: 1.0
author: neuroscience-cron 2026-10-27
license: MIT
trigger_words:
  - delay-coupled neural mass
  - phase interaction function
  - Wilson-Cowan delay
  - synchrony bands
  - twisted states
  - harmonic balance iPRC
  - metastability band edges
---

# Delay Phase Reduction for Neural Mass Networks

Source: Nelson & Crofts, "Phase response approach to networked neural activity models with delays", arXiv:2610.35638 (26 Oct 2026). A single function of the ISOLATED node — the phase interaction function H — predicts where delay-coupled Wilson-Cowan networks switch between synchrony and anti-phase, why the bands repeat with the oscillation period, where metastability peaks, and which topology-dependent states (anti-phase, twisted) can exist.

## When to Use

- Networks of delay-coupled neural mass / oscillator models where delay-dependent synchrony bands, multistability, or metastability need EXPLANATION, not just simulation sweeps.
- Any delay-differential oscillator network where you want to separate node-dynamics effects (H, its zeros) from network-structure effects (Laplacian spectrum, bipartiteness).
- Brain-scale models (The Virtual Brain style) where inter-regional conduction delay rho is the control parameter.

## 1. Model class

Delayed Wilson-Cowan network, n nodes, two distinct delays:

```
du_i/dt = -u_i + c1 f(u_i(t-tau)) + c2 f(v_i(t-tau)) + eps * sum_j w_ij f(u_j(t-rho)) + P
dv_i/dt = -v_i + c3 f(u_i(t-tau)) + c4 f(v_i(t-tau)) + Q
f(x) = 1/(1+e^{-beta x})
```

- tau = intra-nodal delay (synaptic/dendritic, INSIDE the node — enters the node's own dynamics); rho = inter-nodal delay (conduction between regions — enters ONLY as a phase lag after reduction). Biologically rho >= tau.
- **W = D^-1 A must be row-stochastic (each row sums to 1)** so synchronous solutions exist. Reference params: beta=60, P=0.65, Q=0.5, c1=c3=-1, c2=-0.4, c4=0, tau=0.5, T=1.681635, slowest Floquet exponent mu1 = -0.2098.

## 2. Phase reduction recipe

1. Compute the uncoupled node's limit cycle x_gamma and iPRC Z from the DELAYED adjoint equation:
   `dZ/dt = Z(t) - DF2^T(t+tau) Z(t+tau)`, normalized so that theta_dot = omega on the cycle.
   Only Z_u matters when network input enters the excitatory equation only.
2. **Harmonic balance** (Nicks et al.) with M=64 Fourier modes is the efficient solver; validate against backward integration of the adjoint (agreement 2e-7) and direct pulse perturbation (0.5% peak-to-peak). Steep firing-rate functions (beta=60) need M>=64; spectral convergence of the iPRC: max diff 1.4e-3 (M=32) -> 3e-7 (M=64).
3. Phase interaction function (convolution on the cycle):
   `H(chi) = (1/2pi) * Int_0^{2pi} Z_u(theta) f(u_gamma(theta+chi)) dtheta`
4. Phase model: `theta_i_dot = omega + eps * sum_j w_ij H(theta_j - theta_i - omega rho)`. Inter-nodal delay enters ONLY as the phase lag omega*rho (replace by Omega*rho, fixed self-consistently by the locked state, Eq: Omega = omega + eps sum_j w_ij H(psi_j - psi_i - Omega rho)).
5. **Band repetition law: every stability boundary is a zero of H' shifted by the phase lag Omega*rho; therefore all band structure repeats in rho with the oscillation period T.** For the reference node H' has exactly two zeros chi* = -0.12, 2.66 — from these two numbers the whole (rho, state) diagram follows without any further network simulation.

## 3. Stability of phase-locked states

Linearization gives a weighted graph Laplacian L_psi with edge weights `w_ij H'(psi_j - psi_i - Omega rho)`; stable iff all non-zero eigenvalues have positive real part.

- **Synchrony** (exists due to row-normalization): stable iff `H'(-Omega*rho) > 0` — INDEPENDENT of topology. Topology only sets convergence rate eps*H'(-Omega rho)*Lambda_2 (spectral gap). Same criterion holds for directed strongly connected networks.
- **Anti-phase two-cluster**: exists iff the network is BIPARTITE (V1 at phase 0, V2 at phase pi); stable iff `H'(pi - Omega*rho) > 0`. Complete graphs and macaque connectomes (Lambda_n = 1.42 < 2) are NOT bipartite -> never anti-phase. Check bipartiteness via Lambda_n = 2.
- **Twisted states on rings** (theta_j = Omega t + j*psi, psi = 2 pi q/n): stable iff `S_q = H'(psi - Omega rho) + H'(-psi - Omega rho) > 0`. Circulant L_psi decouples into Fourier modes; Re sigma_k = -(eps/2)(a+b)Lambda_k with a = H'(psi - Omega rho) forward, b = H'(-psi - Omega rho) backward; imaginary parts (eps/2)(a-b) sin(phi_k) make perturbations travel but don't affect stability.
- **Two nodes**: flow on a circle, always locks; in the narrow windows where neither synchrony nor anti-phase is stable, a mirror pair +/-phi* (born in pitchfork bifurcations at each band edge) is selected by initial condition.

## 4. Predictions validated against full DDE networks

- Two nodes: phase-locked state selection matches full dde23 simulations across all rho; collective-frequency error scales as eps^2 (slopes 1.94-1.98) up to eps=0.2 (<2% error), grows abruptly near the synchronous Hopf (eps~0.3).
- 6-node ring: four twisted states q=0..3 each stable where S_q>0; full model agrees at 93-96% of grid points for eps<=0.1 (residuals sit next to borders with slow convergence). MULTISTABILITY: q=1/q=2 stable over bands as wide as synchrony/anti-phase, but from random initial phases reached in only 3-5% of runs (anti-phase 41%, synchrony 21%, unsettled 29%) — small basins of attraction, so earlier simulations missed them.
- Macaque connectome (CoCoMac, n=47, non-bipartite): synchrony band same as complete network at weak coupling (explains noted resemblance); phase model reproduces both <R> and metastability <S_R>; **metastability peaks exactly at the predicted band edges where the stability margin H'(-Omega rho) -> 0** and relaxation becomes slow.
- "Moderate synchrony" of sparse networks at weak coupling is slow convergence + multistability (controlled by Lambda_2), NOT a distinct dynamical regime.

## 5. Validity limits (when NOT to use the phase reduction)

- **Coupling bound: eps << |mu1|** (slowest nontrivial Floquet exponent; here ~0.21). Disagreement away from borders stays <7% for eps<=0.2, jumps to 40-50% beyond |mu1| — the Floquet exponent is the practical failure coupling, not a formal bound.
- Near predicted borders (S_q small) disagreement is larger at ALL eps — these are also where torus breakdown and weak chaos occur.
- Between |mu1| and the network Hopf envelope (eps~0.35-0.37, rightmost root of the linearized DDE over all modes; synchronous mode alone gives 0.3125-0.3705) lies an intermediate regime (higher-codimension bifurcations, phase clusters) OUTSIDE phase-only description.
- Extension path: the node has a single slow REAL Floquet exponent separated by >10x from the rest -> phase-AMPLITUDE reduction retaining that one amplitude direction is the natural next step; it should also absorb the O(eps^2) frequency shift (mean coupling input displaces the cycle along the slow Floquet direction).

## 6. Numerical protocol

- Node: harmonic balance M=64 (limit cycle, iPRC, mu1 via harmonic-balance eigenproblem or Chebyshev pseudospectral monodromy).
- Full network: MATLAB dde23, reltol<=1e-6, history = limit cycle at chosen initial phases x_j(t) = x_gamma(t + theta_j^0/omega).
- Phase model: Euler step 0.01 with delayed phases retained.
- Protophase from full model: theta_j = 2 pi k at k-th maximum of u_j, linear interpolation between maxima.
- Order parameters: Kuramoto R(t)=|mean e^{i theta}|; bipartite R_bip (s_j e^{i theta_j}, s_j=+-1); ring twist R_q = |n^-1 sum_j e^{i(theta_j - 2 pi q j/n)}|; metastability <S_R> = time SD of R(t).

## Reuse recipe

1. Compute H ONCE for the node (harmonic balance). Find zeros of H'.
2. Synchrony band = where H'(-Omega rho)>0 (self-consistent Omega); bands repeat with period T in rho — no network sweep needed.
3. Check Lambda_n=2 (bipartite?) to know if anti-phase is even possible; Lambda_2 sets how slow convergence will be.
4. For rings, list S_q>0 intervals for q=0..n/2 -> predicts coexisting twisted states; sample initial conditions carefully (small basins).
5. Place metastability where H'(-Omega rho)=0 (vanishing stability margin) — candidate mechanism for flexible brain coordination.
6. Report validity: quote eps vs |mu1|; if eps > |mu1|, use phase-amplitude or direct harmonic-balance continuation of the full network instead.

## Related skills

- [[bipartite-oscillator-synchronization]] — bipartite sync modes for E/I networks
- [[adaptive-delay-frequency-bursting]] — adaptive delay-coupled oscillators
- [[kuramoto-control-theory]] — complex-valued Kuramoto control framework
- [[neural-fields-*]] — neural field PDE methods (alternative to mass models)
