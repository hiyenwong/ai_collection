---
name: neural-vft-conjugate-flow-learning
description: Use when fitting ODE flows that must satisfy the group law.
version: 1.0
author: neuro-cron 2026-10-25
license: MIT
category: ai_collection
trigger: exact flow learning, conjugacy ODE, invertible neural network dynamics, action-angle recovery, Floquet spectrum learning, neural population dynamics fitting
metadata:
  arxiv_id: "2610.29039"
  paper: "Neural Vector Field Transformations - Learning the Flow of Autonomous Systems by Conjugation to Explicitly Integrable Reference Flows"
  paper_author: "Andrew Qing He (Duke University)"
  published: "2026-10-21"
  pages: 19
  hermes:
    tags: [dynamical-systems, ode-learning, invertible-networks, conjugacy, hamiltonian, neural-dynamics]
    related_skills: [koopman-stability-preserving-id, koopman-spectral-residual-scaling, neural-dynamics-universal-translator]
---

# Neural Vector Field Transformations (Conjugate-Flow Learning)

Represent the flow of an autonomous ODE `dx/dt = f(x)` as a **conjugate of an explicitly
integrable reference flow** by an invertible neural network:

```
Phi_t(x) = F_theta^{-1}( Psi_t( F_theta(x) ) )
```

Unlike time-input networks (break the group law) or learned time-h maps (group law only on the
grid, must be iterated), this is **an exact flow for every parameter value**: `Phi_0 = id`,
`Phi_s . Phi_t = Phi_{s+t}` hold at rounding level (1e-15..1e-13) with t a continuous argument.
Motivation: the rectification theorem (every field is locally conjugate to a translation), made
global by choosing a reference that shares the target's qualitative behavior.

## When to Use
- Fit neural/physical dynamics where the model must be an **exact flow**: no accumulated error
  from stepping (time-uniform error bound: `|Phi_t^theta - Phi_t| <= eps' + Lip(F^-1) Lip(Psi_t) eps`).
- Recover **conjugacy invariants** of a system: equilibrium spectra, periods + Floquet
  multipliers of limit cycles, frequency-amplitude relations of centers, action-angle variables.
- Neural population dynamics after dimensionality reduction (rotational/oscillatory low-dim
  trajectories, exactly the regime of neural-latent ODE fitting).
- Hamiltonian targets needing an **exactly symplectic learned flow** for any t.
- NOT for chaotic attractors (not conjugate to any integrable flow), non-autonomous/forced
  systems, or multi-basin targets without an atlas of charts (one F per invariant region).

## Hard rules (the invariants must live in the reference)
A C^1 conjugacy preserves: (a) equilibrium Jacobian spectra (similar matrices), (b) periods and
monodromy/Floquet multipliers of periodic orbits, (c) first integrals, omega-limit sets,
period-vs-energy relations of centers. Consequences:
1. **A fixed reference can only fit targets sharing its invariants.** E.g. the Hopf normal form has
   mu_F = -2*lambda_0, so Van der Pol (lambda_0=0.750, mu_F=-1.684) is NOT representable on that
   reference. The reference must carry these numbers as **learnable parameters**.
2. **Orientation is not learnable.** Affine coupling nets have det(DF)>0, symplectic nets det=1,
   so the rotation sense (sign of frequency parameters) must be set BEFORE training from
   Df(x*) or from the mean signed increment of the polar angle along data. Wrong sign = the
   optimizer must drive frequency through zero (orientation barrier) and lands 4-5x too slow.
3. **Resonance**: near resonant equilibria (lambda_j = sum m_i lambda_i) the reference must
   contain the resonant normal-form monomials (Poincare-Dulac/Sternberg obstruction).
4. **Translation reference only for dispersive flows** (Bhatia-Szego: parallelizable iff
   dispersive). Any recurrence (cycles, equilibria) needs a richer reference.

## Reference-flow menu (explicit integral curves, learnable invariants)
- **Skew products over first integrals**: `dI/dt = 0, dtheta/dt = h(theta, I)` — I never
  integrated, so dependence on I is arbitrary. Gives translation, shear, action-angle.
- **Action-angle** (n=2d): pairs rotated by angle w_i(I)*t with I_i = |pair|^2/2. For d>=2 it is
  Hamiltonian **iff w = grad K** (closedness of the one-form); parametrize `w(I) = w0 + grad K(I)`
  with a scalar network K. A vector-valued w breaks symplecticity and no symplectic F repairs it.
- **Linear flow** `Psi_t = e^{At}` with full learnable A (evaluated by differentiable matrix exp);
  the n^2-n non-spectral entries are centralizer freedom removed by the Jacobian anchor.
  (Bizzi et al. 2025 neural conjugate flows = the affine special case.)
- **Radial quadrature planar flow** (equilibrium + limit cycle): prescribe `ds/dt = h(s)`,
  `dtheta/dt = w(s)` with decoupled `h(s) = s(s*-s)R(s)`, R(s) = R0 + (R1-R0)*4u/(1+u)^2,
  u = s/s*. Then origin rate lambda0 = s* R0/2, Floquet exponent mu_F = -s* R1, radius s*,
  and frequencies w(0), w(s*) are all **independent** — required by rule 1. Evaluate by
  subtracting the logarithmic singularities of 1/h analytically, Gauss-Legendre quadrature for
  the smooth remainder, bisection + Newton inversion with gradient flow-through.

## Training recipe (each component decisive in experiments, 3 seeds)
- **R1 — relative push-forward residual + scale-free sampling + anchors**:
  - Use the PUSH-FORWARD residual `|DF^-1(F(x)) g(F(x)) - f(x)|^2` (= |f_theta - f|^2, one
    JVP by forward-mode AD). The pull-back form rewards shrinking latent coordinates and makes
    F^-1 ill-conditioned whenever the reference is scale-invariant in some directions.
  - Make it RELATIVE: divide by `|f(x)|^2 + eps`, eps=1e-6. Near an equilibrium the plain
    residual carries no weight exactly where the spectrum lives.
  - Sample log-uniformly in radius: half of each collocation batch at |x| in [1e-3, 1] with
    uniform direction, so every decade of |x| has the same number of points.
  - Point anchors as penalties: `F(0) = 0` and `DF(0) = I`. The Jacobian anchor forces the
    reference spectrum to equal that of Df(x*) (turns an invariant into a locally observable
    quantity) and removes centralizer drift.
- **R2 — symplectic architecture + gradient-form frequency** (Hamiltonian targets only):
  SympNet gradient modules (q,p) -> (q, p + grad V(q)) alternating with (q,p) -> (q + grad T(p), p).
- **R3 — initialize invariants from field or data, never at defaults**: spectrum from Df(x*)
  when known; from data: rotation sense/rate = mean signed increment of unwrapped polar angle,
  Floquet exponent = mean slope of log-distance to cycle, eigenvalues = least-squares on finite
  differences near the equilibrium. Estimates land within 0.2-5% of truth; the oracle run says
  **keep them frozen rather than released** — trained invariants drift 13-25% off because
  short-lag data loss does not see them.
- **Data loss (regime 2/3)**: original-space pair residual `|x_k - Phi^theta_dt(x_j)|^2` on random
  pairs, NOT the latent residual (which collapses the cycle interior). Lag curriculum: start
  small, double max lag when running loss falls below a threshold tied to the noise floor.
  Stratify pairs: equal shares from equilibrium neighborhood / transient / attractor, so every
  invariant is seen by some pairs.
- Architecture: 6-12 affine coupling blocks, width 64, scale bound `s_max = 1` (with s_max=3
  the residual multiplies Jacobians of all blocks and stalls; lowering s_max and adding blocks
  broke a plateau with FEWER parameters). Train: Adam + cosine decay (6-15k steps, fresh batches
  of 2048) then L-BFGS on a fixed batch, double precision.

## Diagnostics — conjugacy vs interpolant (training loss is NOT reliable)
Models whose trajectory errors differ 25x have plain equation losses within 20%.
1. **Relative residual on spheres**: average |f_theta - f|/|f| over |x| = r for r from 1e-3 to
   domain size — must be FLAT across decades. Growth as r -> 0 = wrong invariants hidden where
   |f| is small.
2. **Jacobian deviation**: ||DF(x) - I|| over sphere radius r must grow LINEARLY in r. A jump
   to O(1) within r < 1e-2 = the anchor is satisfied at a point and circumvented next to it
   (degenerate DF(0) confines the mismatch to a ball uniform sampling never sees).
3. **Latent view (acceptance test)**: true trajectories mapped by F must be reference orbits
   (lines/circles/spirals of e^At/hyperbolae). If not: a local interpolant that the exact group
   law extrapolates to nonsense beyond trained lags — reject regardless of loss.

## Four failure modes (what removed each)
1. **Bifurcation barrier**: changing stability type requires an eigenvalue crossing 0
   (non-hyperbolic). Optimizer avoids crossing; wrong phase portrait fits the box (a distant
   sink mimicking the unstable direction). Fix: equilibrium point anchor F(x*)=0, or init from
   Df(x*).
2. **Degenerate Jacobian / circumvented anchor**: point anchor satisfied while DF(0) made
   singular, mismatch hidden in a tiny ball; equation loss 2.4e-4 with garbage spectrum.
   Fix: R1 (relative residual + log-uniform sampling + Jacobian anchor) — ball anchors work but
   are inconsistent with exact conjugacy by O(|x|^2).
3. **Orientation barrier**: wrong rotation sign never flips (or lands 4-5x too slow). Fix: R3,
   costs nothing.
4. **Data-only limit cycle (open)**: Van der Pol from data — best run gives a valid conjugacy on
   the data region but Floquet exponent 17% off. Oracle run (true invariants frozen, F trained)
   fits WORSE: obstacle is the expressivity of a coupling network on a relaxation-type cycle,
   not invariant identifiability. Data-estimated invariants are more trustworthy than trained.

## Evidence (final configs, 3 seeds where starred)
- 3D nonlinear sink: spectrum {-1/2 +- 2i, -1} recovered to 8.3e-3 max deviation*.
- 6D sink (2 complex pairs with different damping + 2 real eigenvalues an order apart): all
  six eigenvalues within 2.3%*; doubling dimension changed neither recipe nor budget (108 min).
- 4D integrable Hamiltonian: action-angle frequencies and actions to median 0.09%/0.22%,
  exactly symplectic flow*.
- Lotka-Volterra (regime 3): all 4 parameters to 2.3e-3. Pendulum librations: frequency map
  recovered. Planar saddle: spectrum (0.98, -0.98) discovered during training.
- Negative: on a dispersive (non-recurrent) field a plain time-input PINN is 8x MORE accurate
  inside its training horizon — the conjugacy structure costs optimization difficulty; use it
  when you need the structure, not on easy one-pass problems.

## Relation to other dynamics-learning skills
- Koopman methods (koopman-*, diffeomorphic linearization): VFT is the same program with the
  conjugacy made explicit — invariants are named parameters, and the reference need not be linear.
- Action-angle networks / SympNets / HNN: the symplectic special case; VFT adds which frequency
  parametrizations keep the reference Hamiltonian (grad-form lemma).
- Neural ODE / neural flows / learned time-h maps: trade exact group law for ease of fitting;
  VFT keeps the law exactly and pushes all difficulty into fitting F — the honest comparison
  (Experiment 1) shows where each wins.
- Bramburger et al. conjugate Poincare maps: discrete-time analog with autoencoders.
