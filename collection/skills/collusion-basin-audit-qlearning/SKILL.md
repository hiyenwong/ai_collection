---
name: collusion-basin-audit-qlearning
description: Use when auditing collusion claims in RL pricing agents.
category: ai_collection
---

# Auditing Algorithmic Collusion Claims in Q-Learning Pricing Agents

**Paper**: "Algorithmic Collusion Without Deterrence: Auditing the Punishment Mechanism in Q-Learning Pricing Agents" — Lopes de Moraes & De Losso (USP), ICAIF '26, arXiv:2610.21867 (submitted 15 Oct 2026).

## Core Claim (What It Refutes)

The seminal Calvano et al. (2020) impulse-response exhibit (deviation → rival price drop → both prices return to pre-deviation level) is read as a learned "reward-punishment scheme" — the mechanism that turns high prices into a regulatory-target cartel. This paper replicates the pattern (98.2% return rate, 1,006/1,024 pairs) and then shows the mechanism reading fails a five-part audit on frozen policies (learning off). What co-training actually builds is a **dyad-specific basin of attraction** — fast, blind to what perturbed it, and worthless outside the pair that carved it. Deterrence is a property an agent has; the basin is a property only the pair has.

## The Five-Part Audit Protocol (run jointly on the same frozen policies)

1. **Directional information test**: shock the price UP (toward monopoly) as well as down. A trigger rule may legitimately punish any departure, but the response form matters: the same drop-and-return fires after cooperative hikes (960/1,024 pairs) — the response encodes no direction, payoff relevance, or identity of the perturbation. Consistent with basin relaxation, not with a rule whose function is deterring defection.
2. **Opponent-model test (the valid design)**: initialize the joint state AT the cooperative price so a grim-trigger punisher starts untriggered; compare play against grim-trigger vs constant-Nash. CAUTION: from a random state, grim reads the initial price as a defection and the two opponents are behaviorally identical — the naive comparison proves nothing. Result: 77% of trained agents (1,577/2,048) undercut the cooperative punisher within 4 periods and destroy the arrangement — an agent carrying a retaliation model would not.
3. **Off-path best-response structure**: slice the 225-entry lookup table at the on-path price to extract the reaction function. Trained reaction functions vs the static best-response curve: mean Spearman ρ = 0.18, range −0.70 to 0.84 — salt-and-pepper everywhere except the attractor itself. No threat structure off-path.
4. **Over-determination test (pivotal)**: two fixed greedy policies on the state = previous joint action define a deterministic map on 225 states; every orbit is eventually periodic (pigeonhole). Enumerate the FULL state space: 89.3% of pairs (914/1,024) have exactly ONE attractor whose basin is all 225 states (dominant-basin share 99.3%). With one global attractor, the return after a defection and the return after a cooperative shock CANNOT differ — the exhibit would follow any perturbation. **Null model**: random Q-tables on the same value range fragment the space (3.39 attractors, 77.5% dominant basin, Fisher p < 10⁻²⁸⁶) — the global basin is training-built, not state-space-built. What training adds is speed (5.14 vs 14.08 steps, Mann-Whitney p < 10⁻³⁰⁰) and placement (94.2% of returns at CI > 0.3 vs 68.2%) — calibration, not selectivity.
5. **Capacity control**: hand-build reactive (forgiving trigger) and grim (own-price-as-phase-flag) policies in the IDENTICAL 225×15 matrix — both behave as punishment rules should (threshold bands in the heatmap vs salt-and-pepper learned policies). The architecture could express punishment; learning did not use it.

## Positive Findings

- **Cross-pairing protocol** (turn Calvano's rematching into an evaluation with learning OFF): CI collapses 0.669 → 0.134 (−80%) across 2,000 random matchings; 7.4% price BELOW Nash. Pairs converged to the SAME price collapse just as far (0.138) — what fails to transfer is the off-path return structure, not the price level. The pair has overfit to itself: OOD failure of each policy to the state distribution a new partner generates.
- **Exact best-response (DP against frozen partner, δ=0.95)**: the optimal deviation profits +17.5% on average (median 16.2%, max 93.7%) vs converged play — while the one-period undercut Calvano tests is unprofitable in 92% of pairs. The scheme deters only the deviation no optimizer would choose. Collusion survives because deviation is never tried, not because it would not pay.
- **Visitation funnel mechanism**: ε-decay concentrates visitation on a narrow trajectory neighborhood; off-path Q-entries stay at initialization. The funnel both builds the basin and seals it (removes the experience that would test it). **Comparative statics prediction verified**: refining the price grid 15 → 50 → 100 → 200 points (2M steps held) drops mean CI monotonically 0.64 → 0.33 → 0.24 → 0.23 while cross-pair dispersion collapses (s.d. 0.13 → <0.003).
- Theoretical name for the converged object: **self-confirming equilibrium** (Fudenberg-Levine) — beliefs correct on the realized path, never tested off it.

## Reusable Audit Patterns (Generalization)

1. **Frozen-policy audit**: separate learning phase from measurement phase; evaluate greedy (no learning, no exploration). Mechanism claims about learned agents must survive learning-off evaluation.
2. **Over-determination vs selectivity**: before reading a return-to-baseline as evidence of a rule, enumerate the full state space of the deterministic induced map — if one attractor's basin covers everything, the pattern is forced and uninformative.
3. **Random-policy null**: same trial count, same value range — locates which parts of the behavior the architecture forces vs training adds.
4. **Capacity control by construction**: hand-build the claimed mechanism in the same representational matrix to rule out "the architecture can't express it."
5. **Stranger treatment as test**: re-match converged agents from independent runs with learning off — pair-specific conventions collapse; individually-held strategies transfer. Distinguishes joint objects from agent properties.
6. **Exact DP best-response sizing**: compute the optimal deviation value (not the one-period probe) to size the wedge the converged profile leaves on the table.

## Environment & Reproducibility

- Bertrand-logit duopoly: q_i = e^{(a_i−p_i)/μ} / Σ_j e^{(a_j−p_j)/μ} + e^{a₀/μ}, π_i = (p_i − c)q_i, a=2, c=1, μ=0.25, a₀=0; 15-point price grid 1.43–1.97; static Nash p^NE ≈ 1.473, monopoly p^M ≈ 1.925. State = previous joint action (225 states), 2M co-training steps, 1,024 pairs + 5-pair faithful-protocol control + 10M-step reference (CI = 0.6421).
- Collusion Index: CI = 0 at Nash, 1 at monopoly; mean 0.668 at 2M steps.
- Code/Q-tables: https://github.com/kauelopes/algorithmic-collusion-without-deterrence

## Policy Implications

What the standard test establishes changes: impulse-response shows basin stability, not enforcement. Pairing-disruption remedies (forced rematching of pricing algorithms) are MORE powerful than the deterrence reading implies (80% collapse with learning off, nothing carried across) — but re-learning partially restores coordination, so remedies must prevent re-pairing, not just interrupt it.

**Activation**: algorithmic collusion, Q-learning pricing agents, punishment mechanism, basin of attraction, frozen policy audit, self-confirming equilibrium, impulse response, antitrust, multi-agent RL, joint policy overfitting, stranger treatment, cross-pairing test