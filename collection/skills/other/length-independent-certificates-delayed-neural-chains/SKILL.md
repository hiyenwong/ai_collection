---
name: length-independent-certificates-delayed-neural-chains
description: Fixed-size LMI certifies chains of delayed neural modules.
category: ai_collection
---

# Length-Independent Stability and L2-Gain Certificates for Chains of Delayed Neural Modules

**Source**: Ö.F. İşcanlı, arXiv:2610.25147 (cs.NE, Oct 2026; submitted to IEEE Trans. SMC: Systems). 11 pages, exact-rational-arithmetic verified.

## When to use

- Chains or rings of coupled neural modules (recurrent modules, neural-ODE blocks, spatially interconnected arrays) with a local delay tau_1 AND a transmission delay tau_2, where the number of modules N is a design parameter or unknown in advance.
- Need: one fixed-size certificate that certifies global asymptotic stability + a common L2-gain bound for ALL lengths, instead of per-length LMIs whose variables grow with N.
- Delays may be time-varying with NO rate bound and no relation between tau_1, tau_2 (rate-free setting).

## Model class

Network (eq 1): ydot(t) = -D y(t) + A g(y(t)) + B1 g(y(t - tau_1(t))) + B2 g(y(t - tau_2(t))) + w(t), z = y.

- N modules of two ALTERNATING types t(i) in {1,2}; module-local D_t > 0 diag, A_t, B1_t (2x2 per module). B2 couples neighbours: forward block F_f, backward F_b (paper: (kappa*Ghat, -kappa*Ghat^T), skew pattern).
- (H1) slope restriction: l- <= (g(a)-g(b))/(a-b) <= l+ for all a != b. Any activations in the sector work, possibly different per neuron. SiLU satisfies l- = -1/10, l+ = 11/10 (Lemma 1; numerically re-verified: sup f' = 1.09984 at r = 2.3994, root of r*tanh(r/2) = 2, f'(r) = 1/2 + r/4).
- (H2) tau_k : [0,inf) -> [0, tau_bar_k] continuous only — no differentiability, no rate bound, no relation between the two delays.
- (H3) arbitrary continuous history. Extensions: module-wise independent delays (Remark 2, delays per module tau_k^(i)); constant inputs -> shifted globally attracting unique equilibrium (Remark 1, Forti-Tesi homeomorphism argument); d states/module -> LMI orders 48d / 52d.

## Method pipeline

1. **Rate-free LKF with FIXED integration limits** (eq 4): V = y'Py + 2*sum_i pi_i * integral_0^{y_i} g_i + sum_k integral_{t-tau_bar_k}^t y'S_k y + double-integral terms with R_k. No integration limit depends on tau_k(t), so Vdot involves delays only through delayed states — no tau_dot_k terms appear. Bounds use Wirtinger-based inequality (F_k, eq 5) with R_hat_k = diag(R_k, 3R_k) + reciprocally convex combination; sector terms S(Y,G;T) = (1/2)Sym (G - L- Y)'T(L+ Y - G) applied at the THREE instants t - tau_j(t), j=0,1,2 AND on pairwise activation DIFFERENCES (multiplier T_ab).
2. **Type-periodic (module-local, tiled) variables**: P_t, S_{k,t}, R_{k,t}, X_{k,t} in R^{4x4}, diagonal Pi_t, T_{j,t}, T_{ab,t} — repeated per module TYPE. Local conditions (eq 11): P_t + Pi_t L- > 0, slack PSD conditions.
3. **Cell reduction** (Lemma 3): a cell = type-1 module + type-2 module; cell state zeta_j in R^48. Coupling splits into intra-cell a0 and inter-cell a+/- (B2,0 / B2,+ / B2,-). In cell order the certificate matrix of ANY open chain is block-tridiagonal T_K(Xi_0, Xi_1) with THE SAME two cell blocks (eq 13-14); open chains add the favourable-sign boundary term -A_out'(I_2 (x) R_c)A_out; rings (even N >= 4) are C_K(Xi_0, Xi_1).
4. **Single cell LMI** (Theorem 2): find symmetric Y (order 48) with
   M = [[Y, -Xi_1], [-Xi_1', -Xi_0 - I - Y]] >= eps*I  (order 96; order 104 with the gain blocks Xi_tilde)
   => every network in the family (all open chains N >= 1, both starts, all rings even N >= 4) satisfies GAS and the same L2-gain bound gamma. Fixed 1298 scalar variables, independent of N. Compare per-length state of the art (Zhai et al. 2025 at order one): 155,648 variables, LMI order 608 at N = 16.
5. **Exactness of the cell reduction** (Lemma 4, operator Fejer-Riesz theorem): the cell LMI is EQUIVALENT (up to margin eps) to requiring the tiled variables to certify every length — spectral form: H0 + z*H1 + conj(z)*H1' >= 0 for every |z| = 1, with H0 = -Xi_0 - I, H1 = -Xi_1. The reduction adds no conservatism of its own; conservatism lives only in the functional and the variable restriction.
6. **Certified regions** (Corollary 1): Xi(kappa) affine in coupling; convexity identity (eq 18): (1-theta)Xi(k-) + theta*Xi(k+) - Xi(k_theta) = theta(1-theta)(k+ - k-)^2 * A_c' R~ A_c >= 0. Verifying the LMI at two endpoints kappa-, kappa+ with separate Y-, Y+ certifies the whole interval; scaling delays along a fixed direction certifies rectangles [k-, k+] x [0, s] of the (kappa, s) plane.
7. **Computation + exact verification**: CVXPY + Clarabel (chordal decomposition); bisection on delay scale / coupling; candidate certificates then VERIFIED IN EXACT RATIONAL ARITHMETIC — replace doubles by exact rationals, sector exactly [-1/10, 11/10], LDL^T factorization WITHOUT pivoting: positive pivots prove positive definiteness. Solver only proposes; the exact check decides, independent of solver tolerances.

## Conservatism assessment protocol

- Outer bound: unstable LINEAR members g(y) = S y (slope-vertex patterns, cell-periodic on rings). For constant delays the DFT over cells decouples rings into cell symbols Delta_theta(lambda) (eq 19, theta = 2*pi*m/K); a root with Re lambda > 0 => the class contains an unstable member => NO certificate can exceed it. Roots by pseudospectral collocation (33 Chebyshev nodes) + Newton refinement.
- kappa_out(s) = smallest coupling with an unstable member => certified kappa reaches 92% (short delays s=1/16), 87%, 79%, 79% (s=1/4, 1/2, 1); falls to 65%/36%/22% at s=2/4/8 (gap widens with delay).
- Gain lower bounds gamma_lb: sigma_max of the inverse characteristic matrix at lambda = i*omega over members + frequency grid; certified gains exceed lower bounds by <= 33-50% at nominal; <= 11% for weak coupling kappa <= 1/4.
- Baselines: delay-independent M-matrix test (Zhang 2003, cell-periodic Perron vector covers every length) certifies only kappa < 0.328 — less than 1/11 of the certified 15/4 at s=1/16. Linearization at the origin (S = I/2 for SiLU) loses stability at kappa_SiLU = 7.33 (s=1/4) — far BEYOND the true outer bound: origin-linearization and delay-independent tests both misjudge admissible coupling by large factors.

## Key quantitative findings

- Price of uniformity s*_N/s* = 1.85-2.62 at N=2 but 1.02-1.07 at N=8-16: certifying all lengths at once costs little for long chains; per-length certificates of the same functional at N=16 raise the certified delay scale by only 2-7%.
- Difference sector terms (T_ab) are essential at strong coupling: removing them shrinks certified coupling 15/4 -> 103/64 at s=1/16, raises certified gains by 3.1-6.0x, lowers certified tau_bar_2 by 37-61%.
- Independent delays: certified pairs (tau_bar_1, tau_bar_2) e.g. (2, 19/32) and (0, 45/32) reach well beyond the common-delay bound d_bar* = 15/16; the two delays trade off mildly (8x local delay still admits 42% of the transmission bound).
- Simulations: heterogeneous activations (SiLU, 1.1*tanh, piecewise-linear) decay below 2.1e-39 by t=100; constant-input trajectories reach the Newton equilibrium within 2.6e-14 — matches Remark 1.
- Wall time: cell problem 7.7 s (stability) / 17.3 s (gamma^2 minimization); per-N exact verification grows 0.42 s (N=2) -> 143 s (N=16); chordal per-N variant fails at N=64 (address-space limit).

## Pitfalls / lessons

- Fixed integration limits are what buy rate-freeness: any limit depending on tau_k(t) drags in tau_dot_k and forces rate assumptions.
- Two delays WITHOUT rate bounds + slope-restricted activations + delayed-activation coupling did NOT fit prior repetition-exploiting criteria (identical-subsystem sync / linear spatially interconnected LMIs) — the cell LKF here is the first covering this combination.
- Do not assess a certificate only against other criteria — rank against an OUTER bound from unstable members of the model class (that is what the 92%/79% numbers mean).
- Exact rational verification is cheap and removes all solver-tolerance doubt; LDL^T without pivoting is the proof primitive (positive pivots == positive definiteness).
- Sector terms on activation DIFFERENCES (not just at the three instants) are the single highest-value functional ingredient at strong coupling.

## See also
- adaptive-delay-frequency-bursting (delay-coupled oscillators, dynamics side)
- discountinued-mpc-robustness / contraction-theory-control-optimization (other fixed-size certificates via contraction)

## Trigger words
length-independent certificate, size-uniform LMI, delayed neural modules, chain of neural networks, ring of modules, Lyapunov-Krasovskii functional, rate-free delays, time-varying delay without rate bound, L2-gain certificate, type-periodic variables, cell reduction, Fejer-Riesz, block tridiagonal certificate, certified coupling region, exact rational arithmetic verification, SiLU slope sector, spatially interconnected systems