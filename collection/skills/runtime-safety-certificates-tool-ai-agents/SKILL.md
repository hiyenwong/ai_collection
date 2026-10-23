---
name: runtime-safety-certificates-tool-ai-agents
description: "Use when certifying runtime safety of LLM agents via log-driven shields. Controller-agnostic PAC bounds."
category: systems-engineering
---

# Controller-Agnostic Runtime Safety Certificates for Tool-Using AI Agents

Source: arXiv:2610.16865 (Baheri & Wei, RIT/GWU, 12 Oct 2026). Wraps opaque LLM agents in a
**runtime shield** carrying a distribution-free PAC certificate on the probability of an
irreversible (unsafe) action within a bounded task horizon — **uniform over every controller
respecting the filter**, so the model can be swapped without recomputation.

## Problem Framing (the reusable abstraction)

- The LLM is an **opaque, frequently-replaced feedback controller**; the tool environment is
  the **plant**. Closed loop can't be analyzed directly — treat it as unknown and supervise it.
- Irreversible actions (delete, wire payment) make the spec a **finite-horizon reach-avoid**
  requirement: bound Pr[∃t ≤ T: s_t ∈ S_u].
- What agents offer is **logs**, not models: a data-driven robust-control treatment.

## The Certificate Pipeline (5 steps, all reusable)

1. **Predicate abstraction φ: H → S**: map the unbounded transcript to a finite vector of
   Boolean safety predicates ("holds write capability", "inside protected directory",
   "irreversible call executed", "has confirmation"). Tool-call types = actions; HALT = hand
   control to human, always permitted. Any dependence not captured by the action must live in
   the state. Assumption A1 (abstract Markovness): given (s_t, a_t), the next abstract state
   is independent of the rest of the transcript.
2. **Committed-budget kernel estimation from closed-loop logs**: logs are adaptively visited
   (closed-loop identification pathology: N(s,a) is random and correlated with successors).
   Fix per-row budgets n_0(s,a) BEFORE seeing data; use exactly the first n_0 successors;
   rows that fall short take the **vacuous confidence set** (whole simplex) — loosens the
   certificate, never invalidates it. Estimator = truncated empirical distribution.
3. **Distribution-free L1 confidence sets** (Weissman et al.): radius
   β_{s,a} = sqrt(k_{s,a}·ln(2k_{s,a}−2)·R/δ / (2·n_0)) over R rows, set = L1 ball ∩ simplex
   ∩ support constraint supp q ⊆ K_{s,a} (candidate successor set — enlarge safely, omit
   never). Validity for adaptive logs via Azuma–Hoeffding on martingale differences + union
   bound (Lemma 2).
4. **Robust reach-avoid value iteration** (worst case over controllers AND kernels):
   V̄_k(s) = max_{a∈D(s)} σ(C_{s,a}; V̄_{k−1}). Inner oracle σ = support function of the L1
   ball, solved in closed form: shift mass min(β/2,1) from smallest-V entries to largest,
   capped by donor/receiver capacity — O(k log k).
5. **PAC guarantee (Thm 1)**: with prob ≥ 1−δ over the log draw, EVERY admissible controller
   π ▷ D satisfies V^π_T ≤ V̄_T(s_0). If V̄_T(s_0) ≤ ε → certified budget. Bound tightens at
   O(√(T/M)) when relevant rows are covered (persistent-excitation analogue).

## Least-Restrictive Shield Synthesis (Alg 1)

Maximize kept autonomy Π(D) s.t. certified budget. Greedy: forbid one action at a time,
ranked by **risk reduction per unit cost**, where cost = reference-policy occupancy ρ(s,a) +
floor. Key insight: **weight removals by task usage, not count** — actions the task never
uses get forbidden first, so the synthesizer **fences the hazard instead of moating the
agent** (keeps a route to the goal). Always returns certified (fallback = all-HALT, V̄=0).
Cor 2: choosing D from the logs that certify it is valid — no sample splitting.

## Violation Tolerance (Prop 2)

If A1 fails by η (history-conditioned successor laws vary within L1 ball η), run VI on
β+η-radius sets: certificate inflates by only T·η/2. Declare η as a tolerance like
unmodeled-dynamics bounds; test A1 on logs via likelihood-ratio tests with 5% FDR.

## Empirical Anchors

- Grid (7×7, known kernel): cert 0.072 vs adversarial true risk 0.010; 100 independent
  datasets × 2 sizes — true risk ≤ certificate AND ≤ budget in ALL trials.
- File-system sandbox (M=4000, ε=0.05): hazards NEVER appear in logs — plug-in MDP baseline
  certifies zero risk and fails on every seed; count-threshold baseline safe but uncertified
  and forbids 80.2% of live pairs; robust shield forbids 4.2%.
- 7 LLM controllers (scripted + Qwen2.5 1.5B/3B/7B, τ∈{0,1}) × 150 episodes with 30%
  prompt-injection attacks: **zero unsafe outcomes across 1050 episodes**. 7B hijack rate
  79.5% without shield → 0 with; intervention rate only 6.5% blocked calls. For 3B the
  shield RAISES success 3.3%→38.7% (blocking an escalation makes the model go back for the
  skipped confirmation — a "block and ask again" rule beats immediate HALT substitution).
- Certificate tightens with log slope −0.70 vs theoretical M^(−1/2); surplus-sample
  truncation costs coverage (50.5% pairs forbidden vs 25.5% if all samples usable).

## Reusable Patterns

- **Interface-owned certificates**: assume kernel independence from controller identity (A4);
  the certificate then belongs to the (environment, interface, permissions, abstraction,
  harm-definition) tuple, not the model. Model churn stops invalidating safety arguments.
- **Unseen action = maximal uncertainty**: an action never observed in a state is NOT proof
  of safety — the vacuous-set rule blocks it if it could reach harm. Logs must cover normal
  operation, not hazards.
- **Blocked ≠ executed**: count only executed calls in the horizon; a blocked proposal
  causes no transition and doesn't advance time. Let "block and ask again" (with a
  consecutive-refusal HALT cap) be an admissible composite controller — it preserves
  recoverability semantics better than immediate HALT.
- **Weissman L1 balls + robust DP** as the anytime-data upgrade of HMM/MDP safety filters:
  no conjugate priors, no Bayesian credibility debate, valid under adaptive sampling.

## Scope & Caveats

- Certificate is about the ABSTRACTION: if predicates don't make the loop Markov, the bound
  inflates by T·η/2 but the abstraction choice remains the main assumption (testable on
  logs, not provable). Future work: learn abstraction on held-out data.
- Environments adapting to agent identity are excluded (A4). Infinite action spaces need
  argument-class refinement in the action or predicates.
- Greedy synthesis is not optimal; each candidate-removal evaluation costs one batched VI
  (seconds on a CPU core at 7×7 scale).
- Code: https://github.com/SAILRIT/Agentshield-certificates
