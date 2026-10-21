---
name: conformal-koopman-deadline-certificates
description: Conformal Koopman consensus-deadline certificates.
category: systems-engineering
---

# Conformal Koopman Deadline Certificates

**Source**: arXiv:2610.28285 (Dey & Marchetti, SETU / Trinity College Dublin) — verified numerically 2026-10-22 (17/17 checks passed, incl. full fleet simulation).

**Use when**: certifying WHEN a nonlinear multi-agent fleet reaches consensus on randomly switching communication networks, with a stated probability, from finite simulation data; when worst-case bounds are vacuous (10^164 rounds) and linearized deadlines are missed in real runs; when one calibration must serve every tolerance.

## The Pattern: Split the Certificate Into Shape x Constant

Randomly-switching nonlinear fleets (saturated tanh coupling, Markov-modulated graphs) have no closed-form convergence time. Two mature tools each cover half:

1. **Annealed Koopman operator** gives the SHAPE: averaging the dynamics over the random switching yields a LINEAR operator for ANY agent nonlinearity. Its subdominant eigenvalue |lambda2| sets the geometric decay rate rho-hat. (Koopman leaves the constant open; classical C = kappa(W) inflates deadlines 1.9-3.2x.)
2. **Split conformal prediction** gives the CONSTANT with a coverage guarantee and needs only ~200 short runs (50 rounds each).

Deadline: **T_b(eps) = ceil( log(eps/q_{1-delta}) / log(rho-hat) )** — one calibration serves EVERY tolerance eps simultaneously (the single envelope event covers all).

## The Annealed Koopman Operator

For bounded observables g on joint state (belief x, mode m):

```
(Kg)(x, m) = Sum_{m'} P_{mm'} * g(F_m(x), m')
```

- **Linear in g for ANY nonlinearity of F_m** (it is a conditional expectation).
- ||K||_inf = 1, K*1 = 1, so eigenvalue 1 (consensus); all eigenvalues in the closed unit disc.
- Subdominant |lambda2| = decay rate of expected disagreement.
- Eigenfunction phi1 at eigenvalue 1 is a bounded martingale, so phi1(z0) = E[x_inf | z0] (the collective decision the fleet is committed to at t=0).

**EDMD estimation**: slow coordinates y = V^T x from the pi-averaged Laplacian's q left eigenvectors; dictionary Psi(x, m) = B(x) (x) e_m^T (monomials in y up to degree d); K-hat = argmin ||Psi_plus - Psi K||_F via least squares. Subdominant eigenvalue gives rho-hat. (Verified reproduction: N=20 fleet gave rho-hat=0.9528 vs paper's 0.9520, lift dim 63.)

Warning: **spurious near-unit eigenvalues** — dictionary enrichment creates them; they lengthen the deadline 29-fold. Filter by checking the eigenfunction actually varies on transients.

## Split Conformal Calibration

Nonconformity score for a trajectory zeta (d_k = disagreement at round k, d_0 = initial):

```
s(zeta) = max_{k0 <= k <= K_cal} d_k / (rho-hat^k * d_0)    -- smallest C s.t. d_k <= C * rho-hat^k * d_0 along zeta
```

Conformal quantile: **q_{1-delta} = s_( ceil((1-delta)(n+1)) )** — for n=200, delta=0.1: the 181st smallest score (verified exact).

Coverage: Pr{ d_k <= q * rho-hat^k * d_0 for all k in [k0, K_cal] } >= 1-delta (exchangeability only — no distributional assumption).

## The Two Assumptions

- **Assumption 1 (Exchangeability)**: calibration and deployment trajectories drawn i.i.d. from one fixed initial distribution (holds at commissioning).
- **Assumption 2 (Post-transient dominance)**: the ratio d_k/(rho-hat^k d_0) is non-increasing after burn-in k0. Reflects that sample-path decay is slower than the annealed rate. CHECK EMPIRICALLY; it lets a 50-round calibration cover tolerances reached thousands of rounds later.

## Why Each Baseline Fails (N=60 network 1, eps=1e-2, slowest run = 90 rounds)

| Method | Deadline | Coverage | Cost |
|---|---|---|---|
| Worst-case ergodicity W | >10^164 | deterministic | 0 |
| Linearised spectral L (rho_L=0.930) | 64 | 85.2% (misses 1-in-7) | 0 |
| Koopman, assumed C=1 (K) | 117 | 100% (but unjustified) | 35 |
| Direct CP on convergence times | 67 | 93.0% | 8x10^5 rounds per tolerance |
| **Conformal Koopman (CK)** | **104** | **100%** | **10^4 rounds once** |

- W: contraction eta = h * a_min * tanh(D0)/D0 = 1.7e-3 per block of N-1 rounds, eta^59 ~ 10^-164 (verified).
- L fails because tanh saturates: at the mean initial separation 2/sqrt(pi) ~ 1.13 the pull is 28.2% below linear (verified) — saturation slows the real fleet (halving 17.5 vs 9.5 rounds; my N=20 sim: 10.2 vs 6.3).
- Direct CP recalibrates per tolerance at 80x the cost — CK's tolerance-simultaneity is the key saving.
- Estimation error in rho-hat is ABSORBED by q_{1-delta} (same rho-hat appears in score and deadline; errors only lengthen T_b) — no eigenvalue perturbation bounds needed.

## Decision Certificate (Corruption Robustness)

The decision is D(z0) = sign phi1(z0). Nominal robustness radius rho-hat(z0) = |phi1-hat(z0)| / ||grad_y phi1-hat(z0)|| (distance to boundary in slope units). Certify with the conformal quantile of estimation-error scores s_i = |phi*(z0) - phi1-hat(z0)| / ||grad phi1-hat||:

```
rho-hat_CP = max( rho-hat(z0) - q_{1-delta}, 0 )   -- decision flips with prob <= delta under ||delta_y|| <= rho-hat_CP (first order)
```

Corrects a nominal margin that worst-case perturbations exceed in 13.3% of cases.

## Verification Anchors (reproduced 2026-10-22)

- Deadline formula at (rho-hat=0.961, q=0.615): eps=1e-1 -> 46, 1e-2 -> 104, 1e-3 -> 162, 1e-4 -> 220 (matches Table I; 104 exact).
- Halving rounds: ln2/(-ln 0.961) = 17.42; ln2/(-ln 0.930) = 9.55.
- Eta chain: h*a_min*tanh(6)/6 = 1.6666e-3; eta^59 = 10^-163.9; W deadline ~ 10^166.
- Full N=20/M=3 fleet sim + EDMD (lift 63): eigenvalue 1 exact, rho-hat=0.9528, nonlinear halving 10.2 > linearised 6.3 rounds (saturation confirmed), one calibration covered 100% of 100 test runs at eps in {1e-1, 1e-2, 1e-3}, envelope crossing 4% <= 10%.

## Reuse Beyond Consensus

The pattern 'anneal the randomness to get a linear operator, then spectral SHAPE + conformally calibrated CONSTANT' applies whenever: (a) dynamics are nonlinear but the random driver (switching, dropout, delay) is exogenous with known/estimable statistics; (b) a scalar performance envelope of form C*rho^k is needed with a coverage guarantee; (c) worst-case constants are astronomically loose. Candidates: epidemic thresholds on switching contact graphs, federated averaging convergence under stochastic participation, opinion dynamics, platoon string stability over lossy channels.
