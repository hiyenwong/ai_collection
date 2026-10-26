---
description: Use when proving size-free MLSI for quantum Gibbs samplers.
name: size-independent-mlsi-quantum-gibbs
category: ai_collection
version: 1.0
author: quantum-cron-2026-10-25
license: MIT
metadata:
  hermes:
    tags: [quantum-computing, mlsi, log-sobolev-inequality, gibbs-sampler, mixing-time, kms-detailed-balance, renyi-2-divergence, quantum-aep, rapid-mixing]
    related_skills: [gibbs-state-analysis, dissipative-thermal-state-prep, retrodictive-quantum-f-divergences]
---

# Size-independent Log-Sobolev Inequalities for Quantum Gibbs Samplers

Methodology from arXiv:2610.31571 — "Size-independent Logarithmic Sobolev Inequalities for Quantum Gibbs Samplers" (Hongrui Chen, Zhiyan Ding, Jianfeng Lu; quant-ph, 22 Oct 2026, 59 pp). First MLSI and L2-LSI constants independent of system size for quantum Gibbs samplers satisfying KMS detailed balance with non-commuting Hamiltonians.

## One-Line Summary

Prove size-free functional-inequality constants for KMS-symmetric Gibbs samplers by (A) transporting the infinite-temperature product-state L2-LSI to the target Gibbs state along a unitary temperature path, then (B) upgrading the resulting size-free sandwiched-Renyi-2 decay to relative-entropy (MLSI) decay via a tensor-power argument with the quantum asymptotic equipartition property (AEP).

## When to Use / Activation

- Bounding mixing times or entropy decay of quantum Gibbs samplers (Davies generators, Gaussian KMS sampler, QLangevin, heat-bath / regularised heat-bath).
- You need MLSI or L2-LSI constants that do NOT deteriorate with system size (rapid mixing O(log n + log 1/eps)).
- Transferring a functional inequality from a free/product reference state to an interacting Gibbs state.
- The dynamics are KMS-symmetric (not GNS-symmetric) so no Riemannian gradient-flow formulation of relative entropy is available.

## What Was Broken Before

- Commuting Hamiltonians (Davies): size-free MLSI via local conditional expectations + spatial entropy factorization. These tools fail for non-commuting H.
- Non-commuting KMS samplers, prior state of the art (all with log-in-n losses): heat-bath MLSI Omega(1/log n) via entropy quasi-factorization; Gaussian KMS sampler MLSI Omega(1/log^4 n) via Renyi-2 decay + hypercontractivity.
- Spectral-gap / oscillator-norm / quantum-Wasserstein approaches give fast or rapid mixing but not entropy-rate constants; hypercontractivity transfer is where the log losses enter.

## Core Result (Theorem 3.2)

For the Gaussian KMS Gibbs sampler (jump ops built from on-site nonidentity Paulis S_{x,u}, Gaussian filter gamma_beta(w) = exp(-(beta w + 1)^2 / 2), coherent correction H^coh = (i/2) tanh(beta ad_H / 4) Q_beta), there exists kappa > 0 with:
- (i) 1D open chains at ANY fixed 0 < beta < inf: kappa depends only on (beta, q);
- (ii) finite-range systems on Z^d boxes with beta J <= beta_0: kappa depends only on (d, R_0, q);

such that for every state rho and t >= 0:
  e^{D2}(e^{t L*} rho || sigma_beta) <= e^{-kappa t} e^{D2}(rho || sigma_beta)
  D(e^{t L*} rho || sigma_beta)     <= e^{-kappa t} D(rho || sigma_beta)
hence alpha_1(L) >= kappa/2 (MLSI) and alpha_2(L) >= kappa (L2-LSI), and mixing time is O(log n + log(1/eps)) in both regimes.

## The Reusable Proof Pattern (five steps)

### Step 0 — Vectorize into the doubled Hilbert space
Work with |Y> = Gamma_{sigma}^{1/2} |X> on H (x) H, where Gamma_sigma is the modular operator. Use the weighted generator L_sigma = Gamma_sigma^{1/2} L Gamma_sigma^{-1/2}; its negative -L_sigma is positive semidefinite (the "parent Hamiltonian" of the sampler) and factorizes into squared KMS norms of quasi-local terms (Chen-Rouze Bohr-frequency decomposition). The target L2-LSI becomes: find size-free C_beta with
  D(Y^2 || sigma) <= C_beta <Y|(-L_sigma)|Y>  for all Hermitian Y, ||Y||_2 = 1,  giving alpha_2 >= 2/C_beta.

### Step 1 — Base L2-LSI at s = 0 (infinite temperature)
sigma_0 = I / 2^{q|Lambda|} is a product state. The s -> 0+ limit of the KMS sampler is a sum of single-site depolarizing generators
  L_{0,*}(rho) = e^{-1/4}/sqrt(2) * sum_{x,u} (S_{x,u} rho S_{x,u} - rho),
for which the product-state L2-LSI holds explicitly:
  D(Y^2 || sigma_0) <= C_0 <Y|(-L_{sigma_0})|Y>,  C_0 = 2*sqrt(2)*e^{1/4}*q / 4q.

### Step 2 — Interpolate the temperature
sigma_s = e^{-sH} / Tr e^{-sH}, s in [0, beta]; each L_{s,*} is the same sampler family at inverse temperature s (filter, jumps, coherent correction all s-dependent).

### Step 3 — Build the unitary transport U_s (quantum Moser construction)
- Centered Poisson equation: d/ds |Omega_{sigma_s}> = -L_{sigma_s} |T_s>, with <Omega_{sigma_s}|T_s> = 0. Unique Hermitian solution because -L_{sigma_s} is invertible on the orthogonal complement of the Gibbs vector (primitivity).
- Sylvester equation (symmetrized multiplication): (f_s Omega_{sigma_s} + Omega_{sigma_s} f_s)/2 = T_s gives the potential f_s.
- Transport generator in commutator form G_s (classical analogue: Moser's flow on square-root densities keeps relative entropy along the flow). Unitarity preserves Hermiticity and HS norm, so Y_s = U_s(Y_0) keeps Y_s^2 a state.
- Quasi-locality of the flow: follows from LOCAL RAPID MIXING (Condition 5.4), which reduces to REGIONAL rapid mixing (Prop 6.7): t_mix^{[R],s}(1/4) <= C_reg (1+R)^a with a < 1 for all balls and all s in [0,beta] suffices. Polynomial-in-R regional mixing is enough.

### Step 4 — Energy/entropy variation bounds + Gronwall transport (Proposition 4.1)
Maintain along the path:
  d/ds D(Y_s^2 || sigma_s)       <= C_S <Y_s|(-L_{sigma_s})|Y_s>
  d/ds <Y_s|(-L_{sigma_s})|Y_s>  <= C_E <Y_s|(-L_{sigma_s})|Y_s>.
The derivative calculations reduce to the LOCAL ACTION-ENERGY INEQUALITY (Condition 6.3): sum_alpha ||R_{s,alpha}|Y>||_2^2 <= C <Y|(-L_{sigma_s})|Y> for the quasi-local derivative families; practically checkable via Condition 6.4 (quasi-local norm decay with exponent p_0 where min{p_0, b} > d + a). Gronwall along s transports the s=0 inequality to s=beta with
  C_beta = (C_0 + beta C_S) * e^{beta C_E}
— every ingredient size-free, so C_beta is size-free; kappa = 2/C_beta.

### Step 5 — Tensor-power + AEP upgrade to MLSI (Theorem 3.3 + Corollary 7.1)
- Divergence chain: D <= e^{D2} <= D_max, and e^{D2}(nu||tau) <= D_max(nu||tau).
- Quantum AEP (smooth max-relative entropy): rho^{(x)m} is trace-close to states nu_m with (1/m) D_max(nu_m || sigma^{(x)m}) <= D(rho||sigma) asymptotically. The approximants nu_m are CORRELATED across copies — so the contraction hypothesis must hold for correlated inputs, not just product inputs.
- Hypothesis: uniform Renyi-2 contraction on ALL tensor powers: e^{D2}(Phi^{(x)m}(nu) || sigma^{(x)m}) <= a e^{D2}(nu || sigma^{(x)m}) for all m and all states nu.
- Chain: superadditivity of D w.r.t. sigma^{(x)m} + partial-trace average + uniform continuity of D(.||sigma) in trace distance gives D(Phi(rho)||sigma) <= a D(rho||sigma).
- Closure requirement (Corollary 7.1): the Hamiltonian class must contain independent copies with tensor-sum samplers — H^{(m)} = sum_j H^{(j)} in the class, L_{H^{(m)}} = sum_j L_H^{(j)} — and the Renyi-2 rate must be uniform in m. Then alpha_1 >= kappa/2.

## Verification Recipes (the two regimes of Theorem 3.2)

- 1D, any finite beta: block the chain into overlapping pairs (fixed grouping + interaction rescaling, H = sum_i h_{i,i+1}, ||h|| <= 1); regional rapid mixing is known at all finite temperatures (Renyi-2 rapid-mixing results apply regionally); Condition 6.4 verified with quasi-local norms (Appendix D.2). kappa = kappa(beta, q).
- d-dimensional, high temperature: finite-range H with beta J <= beta_0(d, R_0, q); perturbative rapid mixing regionally; Condition 6.4 verified (Appendix D.3). kappa = kappa(d, R_0, q).

## Key Equations (cheat sheet)

- Weighted generator: L_sigma(Y) = Gamma_sigma^{1/2} L Gamma_sigma^{-1/2}(Y); -L_sigma >= 0.
- L2-LSI: 2 Ent_{2,sigma}(X) <= (2/alpha_2) E_{2,sigma}(X); alpha_2(L) >= 2/C_beta.
- Transport constant: C_beta = (C_0 + beta C_S) e^{beta C_E}; kappa = 2/C_beta; alpha_1 >= kappa/2.
- Base constant: C_0 = 2 sqrt(2) e^{1/4} q / 4q (q qubits per site).
- Renyi-2 -> MLSI bridge: D <= e^{D2} <= D_max; AEP: (1/m) D_max(nu_m||sigma^{(x)m}) <= D(rho||sigma) + o(1).
- Mixing readout: D(rho_t||sigma) <= e^{-alpha_1 t} D(rho_0||sigma); with D(rho_0||sigma) <= qn ln 2 for the maximally mixed start, t_mix(eps) = O(log n + log(1/eps)).

## Pitfalls / Sharp Edges

- Renyi-2 decay on a single system does NOT imply relative-entropy decay: the tensor-power argument needs the contraction uniformly over every m and for correlated input states (the AEP approximants are correlated). Check closure of the Hamiltonian class under independent copies first.
- Hypercontractivity is the log-loss route; the tensor-power + AEP route transfers the rate without loss. Do not combine step 5 with hypercontractivity.
- KMS symmetry is strictly weaker than GNS symmetry: no gradient-flow formulation, so start from L2-LSI (Renyi-2), never from a MLSI ansatz at the interacting temperature.
- Constants may depend on (beta, q) in 1D or (d, R_0, q) at high temperature, but never on |Lambda|. If your verification of Condition 6.4 picks up n-dependent exponents, the transport breaks.
- Local (not global) rapid mixing is what quasi-locality of the transport generator needs; regional polynomial mixing t_mix(1/4) <= C(1+R)^a with a < 1 is sufficient (Prop 6.7).
- Primitivity (unique full-rank invariant state) is required twice: invertibility of -L_sigma off the Gibbs vector (Poisson equation) and faithfulness of sigma (continuity of D(.||sigma)).

## Related Skills

- gibbs-state-analysis — entanglement/structure of high-temperature Gibbs states (complementary: state structure vs sampler dynamics)
- dissipative-thermal-state-prep — dissipative state preparation with rigorous error bounds (same sampler toolbox, different objective)
- lindbladian-learning-qec (collection/skills) — inverse problem: learning the Lindblad generators this skill analyzes

## References

- arXiv:2610.31571 — Chen, Ding, Lu, "Size-independent Logarithmic Sobolev Inequalities for Quantum Gibbs Samplers" (2026)
- Gaussian KMS Gibbs sampler [21] and the broader KMS family [1]; Renyi-2 rapid mixing for 1D Gaussian KMS [15]; entropy quasi-factorization for heat-bath [12]; quantum AEP for smooth max-relative entropy [22, 64]; Moser's classical transport [36]; Dirichlet-form factorization [13, 14, 20]. Full bibliographic details in the paper's reference list.
