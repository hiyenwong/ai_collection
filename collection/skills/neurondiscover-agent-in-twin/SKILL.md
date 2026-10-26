---
name: neurondiscover-agent-in-twin
description: Agent-in-Twin mechanistic discovery under twin confounding.
category: ai_collection
---

# NeuronDiscover: Agent-in-Twin Mechanistic Discovery

**arXiv:2609.35338** — "NeuronDiscover: Agent-in-Twin for Mechanistic Discovery in Neuronal Microenvironments with World Action Models" (Xu, Fu, Han, Xie; Peking University, submitted 28 Sep 2026, cs.LG/q-bio.NC)

Use when: designing autonomous scientific discovery agents, separating mechanism from model error in simulation-based inference, building closed-loop "self-driving biology" systems, or doing Bayesian experiment design where the *simulator itself is uncertain* (twin confounding). Trigger words: twin confounding, agent-in-twin, mechanistic discovery, MIOY graph, world action model, discrepancy-aware design.

## 1. Core Problem: Twin Confounding

**Definition.** Two explanations ξ=(h,z) and ξ′=(h′,z′) are observationally indistinguishable at resolution ε when d_E(ξ,ξ′)=sup_e d(P^e_ξ, P^e_ξ′) ≤ ε. **Twin confounding** occurs when the indistinguishable pair differs in *both* the mechanism h and the twin discrepancy z — the available experiments cannot separate "the biology changed" from "the digital twin is wrong."

Key insight: **predictive accuracy cannot settle mechanistic claims.** A clearance change may reflect altered boundary exchange, model error, or measurement bias. Discovery must therefore carry a *joint mechanism–discrepancy belief* b_t(H, Z, N, S_t) over mechanism H, twin discrepancy Z, nuisance N, and state.

## 2. Architecture: Agent-in-Twin Loop

Four coupled components (the computational core of a self-driving-lab loop):

1. **World Action Model (WAM)** — one typed joint law answers forward, inverse, and sensing queries:
   - Q_θ(S_0:T, H, A_0:T−1, Y_0:T, G, V | C) — states, actions, observations keep physical units
   - Forward: Q(S,Y | S_0,H,A,C); Inverse proposal: Q(H,A | S_0,G,Γ,C)
   - Backbone = coarse mechanistic solver + learned neural residual: S_{t+1} = F_mech(S_t, I_t, H, C) + R_θ(...)
   - Discrete/masked diffusion backbone with token codebooks (physical units preserved); 6-term loss: L_joint + λ_dyn L_dec + λ_phys L_phys + λ_int L_Δ + λ_coh L_cyc + λ_val L_valid
2. **Scientific Agent** — maintains belief b_t, evidence K_t, budget B_t; selects (action, query template) via policy π_ω(·|b_t, G_t, K_t, B_t). LLM is an *optional proposal interface* (localized benefit only: +0.60 relations on vocabulary-extending tasks, zero elsewhere — deterministic controller preferable on closed vocabularies).
3. **Freeze protocol** (pre-registration): action, endpoint, falsifier, and analysis fixed BEFORE outcome release → conditionally super-uniform test keeps Pr(p ≤ α) ≤ α despite arbitrary pre-outcome search (Prop. 6); sequential correction across rounds.
4. **Independent reference** — frozen finer-mesh solver or registered recording adjudicates correctness; labels evaluator-only.

## 3. The MIOY Graph (the key data structure)

G_t = (M_t, I, O, Y, E_t): Mechanism–Intervention–Observation–Outcome relations, each carrying **scope predicates, uncertainty, support, and counterevidence**. Supported relations compile into **Executable Mechanistic Programs (EMPs)** carrying discrepancy-adjusted acceptance bounds, observation triggers, validity conditions, and stopping rules.

**Typing prevents confound-hiding:** an observation node may explain the *observed* endpoint but never the *physical* endpoint — so "the sensor gain changed" cannot be silently charged to a mechanism. Untyping raises false support 5.0% → 13.5%.

**Scope-narrowing beats overwriting:** when a later context defeats a supported effect, birth a scope-narrowed version rather than editing the contradicted relation in place (overwriting: 7.5% false support; unscoped: 9.5%). Resolutions barely move — typing/scoping is what makes relations close *for the right reason*.

**Case study (three role bindings of one outcome):** AQP4-proxy reduction lowers tracer retention. Three accounts fit equally: boundary exchange κ_I, parenchymal diffusivity D_I, or *sensor gain a_j* (pure observation account). Calibrated flux at nonzero contrast constrains κ_I; spatial profiles test D_I; a gain-control intervention with no physical intervention isolates a_j. Support withheld until discriminated.

## 4. Experiment Selection Under Joint Belief

- **Identifiability floor (Prop. 1):** local response r_e ≈ J^mech_e Δh + J^wam_e Δz; (∆h,∆z) identifiable to first order iff Λ(E)=Σ_e J_e^⊤ Σ_ξ^{−1} J_e ≻ 0. Below the floor, design improves the *weakest direction* (smallest singular value minus operator uncertainty), not EIG.
- **Acquisition above floor:** α_t(e) = I(Y_e; H,Z | e, K_t) + λ_F F_t(e) − λ_C C(e) − λ_V RV(e), where F_t rewards specified falsification opportunity.
- **Joint mechanism–discrepancy EIG beats plug-in EIG** (3.8 vs 2.9 relations/world; 5% vs 11% false support) and nested-filter BAD-PODS-style baselines (+0.60). Cost: online time ratio 2.9 — gain bought with compute, not experiments.
- **Forward verification of programs:** with n_a pre-fixed rollouts over a frozen program set, simultaneous bounds P(G) ≥ p̂_g − ε_a − δ_a, P(V) ≤ p̂_v + ε_a − δ_a (ε_a = log(2K/α)/2n_a); accept when lower goal bound ≥ τ_g and upper violation bound ≤ τ_v. Two-sample event calibration supplies δ_a; total failure ≤ α+β.

## 5. Benchmark Design (reusable evaluation pattern)

- 32 independent source units split BEFORE episode construction; 3 replicates averaged before paired estimation; 16 experiments/task matched budget
- Every contrast **paired within source**; cluster-bootstrap 95% CI + Holm-corrected randomization tests
- **Abstention scored as unresolved for every method** (no free lunch from declining to answer); unsupported/failed tasks retained in denominators
- Adaptive observation: 4.0 correct relations/world vs 2.8 fixed sensing on same WAM
- Donor-disjoint transfer (Allen current-clamp recordings): 1.94 vs 1.53 relations/assigned world

## 6. Headline Results

| Contrast | Difference | 95% CI | Holm p |
|---|---|---|---|
| Graph revision vs fixed hypothesis graph | +0.80 relations | [+0.57, +1.03] | <0.001 |
| vs strongest baseline (external tool agent) | +0.60 | [+0.41, +0.79] | <0.001 |
| Joint vs plug-in EIG | +0.90 | [+0.65, +1.15] | <0.001 |
| Discrepancy-adjusted verification (risk) | −6.0 pp | [−7.59, −4.41] | <0.001 |

- Resolutions: 4.0 (Agent-in-Twin) vs 3.4 (strongest baseline) vs 3.2 (fixed graph); scope accuracy 75%→82%; false support 7%→5%
- **Strongest forward predictor ≠ best discoverer:** the neural operator had the best rollout error yet trailed the hybrid by 0.10 relation-status macro-F1 — calibrated uncertainty, not point accuracy, drives discovery
- Discrepancy-adjusted verification: accepted-program failure 15%→9% at 60% acceptance coverage

## 7. Implementation Checklist

1. Represent every hypothesis as a typed, scoped relation — never a bare parameter value
2. Carry twin discrepancy Z as an explicit belief coordinate alongside mechanism H
3. Freeze (action, endpoint, falsifier, analysis) before each outcome; adjudicate independently
4. Check the identifiability floor Λ(E) ≻ 0 before ranking experiments by information gain
5. On contradiction: narrow scope, never overwrite
6. Accept programs only with simultaneous goal/violation bounds from pre-fixed rollout counts
7. Score abstentions as unresolved; keep failed tasks in denominators

**Limits:** correctness adjudicated within declared model worlds; binding the loop to a physical instrument (real autonomous lab) is the stated next step; ionic-mechanism claims on recordings still require separate perturbation evidence.
