---
name: petri-net-supervisor-agentic-execution
description: Use when LLM agents call tools. Petri-net safety harness.
category: ai_collection
---

# Petri-Net Supervisory Control for Agentic AI Execution Harnesses

Source: Gu & Zhu (Queen's University Belfast / NYU), "Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action", arXiv:2610.31376 (eess.SY/cs.AI, Oct 2026).

## Problem

Prompt injection attacks the LLM itself — the component the attack is designed to manipulate. Four common defenses fail operationally: system-prompt policy is text in the same context window the attacker writes into; guardrail classifiers judge content; access control grants reusable permissions; sandboxing only limits damage. None tracks the OPERATIONAL STATE (which actions already occurred and what they consumed). Operational failures = out-of-order actions, approval replay, double-spent budgets, two agents holding one lock.

## Core construction

1. **AEPN (agentic execution Petri net)**: colored Petri net where each transition t carries labels — action ℓ(t) (tool/message name), responsible principal ω(t) (agent/human/environment), controllability χ(t)∈{c,u}. Marks are operational facts (capability, evidence, approval, budget unit); mark colors carry metadata (e.g. the cryptographic digest of an approved artifact).
2. **Admission rule (4 checks, in order)**: Admit(u)=1 ⟺ [α(u,M)=t≠⊥] ∧ [V(u,t,M)=1] ∧ [t∈En(M)] ∧ [t∈S(M)] — parse → validator → enabled → supervisor. Checks iii/iv depend only on (t,M), so an injected request whose preconditions are unmet or already spent is refused REGARDLESS of its wording. Trusted base = interface+validator+net+supervisor+log; the LLM and all content are untrusted.
3. **Consumable authorization**: spent conditions (p ∈ •t\t•) vs tested conditions (self-loop). Spent marks make each approval authorize exactly ONE execution. Monitor place enforces any linear firing-count constraint ηᵀy ≤ β via Pre(pc,t)=max{η(t),0}, Post(pc,t)=max{−η(t),0}, M0(pc)=β — guaranteed by net structure alone, no state enumeration. Counting rules are NOT regular (Myhill–Nerode): no finite automaton can count unspent approvals; Petri nets can.
4. **Colors bind approvals to objects**: guard of the execution transition requires the consumed mark's color = digest of the artifact actually executed ⇒ approval substitution prevented; per-digest counting holds by unfolding.
5. **Supervisor synthesis (offline)**: K⋆ = greatest marking set avoiding forbidden B and closed under uncontrollable firing (UPre iteration: W0=Q\B, W(j+1)=Wj\UPre(Q\Wj)). K↑ = joint fixed point alternating uncontrollable-closure removal with coreachability-to-terminal-F removal. S_K↑ = maximally permissive SAFE NONBLOCKING supervisor (exists iff M0∈K↑, Ramadge–Wonham adapted). Runtime admission = table lookup at current marking.
6. **Transfer to the running system (Theorem 1)**: net safety transfers under A1 initial correspondence, A2 step simulation, A3 safety reflection (M∉B ⇒ concrete state safe), A4 complete mediation: (a) every consequential action passes the admission rule (enforce via sandboxing + credential brokering), (b) every external event authenticated and fired in the kernel as an uncontrollable transition; an event matching no enabled uncontrollable transition ⇒ halt admission and escalate. All four assumptions are individually necessary (paper gives counterexamples).
7. **Replanning closed loop**: a refusal returns as an error and the agent may propose again; each retry costs one inference call. Intrusiveness J = expected total cost (ca per admitted call, 1 per refusal, terminal cost g). KEY COUNTERINTUITION: the maximally permissive supervisor can be ARBITRARILY more intrusive than a stricter safe one — when the proposer almost always requests the unsafe action after entering a safe region, admitting entry generates unbounded refusals (ratio → ∞ as request probability → 1).
8. **Value-threshold refinement (Theorem 2)**: S_Jmin(M) = {t ∈ S_K↑(M)∩Tc : Jmin(Mt) ≤ Jmin(M) + 1 − ca} ∪ Tu. Refuse t iff admission cost ca+Jmin(Mt) exceeds refusal cost 1+Jmin(M). Computed from a proposer model π(·|M) via stochastic-shortest-path Bellman equation / LP (polynomial in |Q|, |T|). Because it only REMOVES transitions from S_K↑, it is SAFE EVEN IF THE PROPOSER ESTIMATE IS WRONG — estimate errors affect only intrusiveness. A candidate Jmin is certifiable in O(|K↑||T|) independent of how it was computed.
9. **Fork ordering (Prop 2)**: for two orderable actions (e.g. tests vs security scan), the refinement refuses branch t1 at the fork iff 1/π2({1}) − 1/π1({2}) > 1/π2(∅) — and implements this ordering with ONE monitor place. Least-intrusive control IS an orchestration decision: it schedules the benign action first so the marking where premature requests occur is never reached.
10. **Synthesis as architecture feedback**: on the release agent, an honest controllability assignment (rollout completion uncontrollable) makes NO safe supervisor admit a one-phase deployment (K⋆ excludes every in-flight marking) — the defect is in the deployment mechanism, not the policy. Adding a controllable publish step AFTER the rollout starts (two-phase rollout) restores K↑=Q\B. Design rule: every consequential phase must end in a step the supervisor can refuse.

## Empirical results

- Injection sweep (10^4 episodes, scripted proposer): a classifier with false-negative rate 0.10/0.30 still yields ~15% unauthorized deployments at ZERO injection probability (it cannot block a benign-but-premature deploy); the Petri-net kernel yields 0 unauthorized deployments for every phrasing and every supervisor, completes every task, at ~1.5 refusals of benign proposals per episode.
- Release fork: with premature-request probability h after the tests, put the scan first iff h > 43/60; extra intrusion of the maximally permissive supervisor ΔJ = max{0, h/(2(1−h)) − 43/34} (verified: 55/17 at h=0.9, 395/17 at h=0.98).
- Example-1 closed forms J_SK↑(M0)=1+a/(1−b) vs J_S′(M0)=1/(1−a) reproduced by Monte Carlo of the replanning loop (2.67 vs 2.667; 2.00 vs 2.0).

## Implementation pattern

1. Enumerate operational facts → places; the agent's own consequential calls → controllable transitions; tool outcomes, human decisions, incidents → uncontrollable transitions. Boundedness check via P-invariants.
2. State every governance rule as a linear constraint on firing counts → one monitor place each (deployments ≤ approvals; rollouts ≤ change windows; calls ≤ budget).
3. Compute K⋆ then K↑; if M0∉K↑ the workflow design itself is defective — add a refuse-able step rather than weakening B.
4. Estimate the proposer π from logs; compute Jmin; apply the value-threshold refinement; re-verify safety is untouched.
5. Do NOT disclose the admitted set to the agent — refusals are an information channel (probing attack on protected actions).
6. Runtime: process admissions and event firings one at a time, atomically; log every proposal and every firing under its principal; halt+escalate on unmatched events.

## Scope and pitfalls

- Covers OPERATIONAL safety only (order, count, authorization), not argument content (that is the validator's job, unanalyzed) and not jailbreaks; it bounds what a hijacked agent can do to what the net allows at the current marking.
- A4(a) bypass (agent calling a tool directly, outside the kernel) voids all guarantees — sandboxing/credential brokering is a prerequisite.
- Stationary proposer is a modeling assumption: safety never relies on it; intrusiveness/termination results do.
- Least-intrusive supervisors can be non-unique; ties (Jmin(Mt) = Jmin(M)+1−ca) admit incomparable patterns — take the maximally permissive one.
- Terminal cost on abstention/escalation changes the refinement only beyond a computable threshold (release agent: g_a* ≈ 6.31).

Activation keywords: prompt injection, execution harness, supervisory control, Petri net, monitor place, consumable authorization, admission rule, least-intrusive supervisor, replanning loop, agent tool-call gating, runtime enforcement
