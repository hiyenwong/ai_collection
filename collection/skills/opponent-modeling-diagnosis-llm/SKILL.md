---
name: opponent-modeling-diagnosis-llm
description: Audit LLM opponent modeling claims beyond payoff alone.
category: ai_collection
trigger: LLM theory of mind evaluation, opponent modeling audit, mentalizing benchmark, agent evaluation rigor, repeated games LLM
---

# Opponent Modeling Diagnosis in LLMs (arXiv:2610.17310)

Use when auditing claims that an LLM exhibits theory of mind (ToM/mentalizing), social adaptation, or opponent modeling in interactive settings. Source: Xie, Zhao & Wilson (Georgia Tech / Sussex), "Beyond Successful Play: Diagnosing Opponent Modeling in Large Language Models", arXiv:2610.17310 (Oct 2026).

## Core thesis
Better play is evidence of adaptation, NOT of theory of mind. In a binary game, every forecast on the same side of 0.5 yields the same best response — payoff can improve while the opponent probability estimate stays inaccurate. ToM claims require separating three abilities that payoff conflates:
1. **Adaptive play** (live payoff)
2. **Action prediction** (forecasting q_t = P(opponent takes action 1))
3. **Belief tracking** (recovering the opponent's belief about YOU, b_t)

## The evaluation chain
h_t → q̂_t → BR_role(q̂_t) → a_self_t → r_t
- h_t: history of both players' actions + own payoff
- q̂_t: forecast of the simulator's next-action probability
- BR_role: role-conditioned best response (seeker matches the likely action; hider avoids it)
- Score each link separately: payoff (sum of 50 round rewards), forecast MSE vs simulator q_t, belief MSE vs simulator b_t, Brier score vs the sampled action.

## Benchmark design (reusable pattern)
- Repeated two-action hide-and-seek: seeker gets +1 for matching, hider +1 for differing. The minimal action space isolates opponent-modeling from action-search confounds.
- Algorithmic opponents with KNOWN update rules (tomsup library): Bayesian k-ToM (k = recursion order), plus behavioral controls — biased random, Q-learning, win-stay/lose-shift. Ground-truth beliefs and action probabilities exist by construction.
- Three evaluation modes:
  1. **Live interaction** — actions change future histories (measures payoff under adaptation)
  2. **Fixed-history** — score forecasts on shared recorded trajectories (isolates prediction from action selection)
  3. **Information interventions** — supply/hide the opponent specification (type, parameters, state schema, initialization) and simulator beliefs
- Controls: constant-0.5 predictor, past-action-frequency predictor; 95% CIs by resampling complete matches (keep within-match decisions together).

## Key empirical findings
- **Payoff ≠ modeling**: Qwen2.5-7B behavioral SFT flips payoff from −13.5 to +2.3 (seeker) yet belief reports stay worse than a constant baseline.
- **Use vs inference gap**: probability-only SFT reaches forecast MSE 0.00990 WITH the opponent specification supplied; removing it degrades performance more than 4-fold (0.01206 → 0.05182). GPT-5.4 given true simulator beliefs: best-action agreement 66.7% → 96.3%, expected regret −0.187; its OWN belief reports remain worse than constant (MSE 0.02717 vs 0.01258). Using belief information is easier than inferring it — even for frontier models.
- **Mixed-exposure repair**: training on examples that omit the specification half the time cuts history-only MSE by 31.65% (0.04926 → 0.03367) vs a specification-only continuation; improves ToM1/2 in both roles but WORSENS ToM0 (transfer is opponent-dependent).
- **RL trap**: GRPO action-chain RL earns +38.3/+33.4 vs WSLS (simple heuristic) but +1.0/+0.5 vs ToM2 and −8.6/−17.5 vs GPT-5.4 — it overfits simple opponents; a 120-update probability-reward run reached >99% output-field consistency while forecast MSE EXCEEDED the constant baseline on fresh histories (distribution shift from buffer reuse is the candidate bottleneck).
- **Field sensitivity ≠ content benefit**: true vs shuffled beliefs changed 10.3% of final actions, but the forecast-MSE advantage of true beliefs remained statistically uncertain — the two must be tested separately.
- Scale non-monotonicity: Qwen2.5 payoff vs ToM2 is non-monotonic in size (3B: −4.9/−11.1; 72B: −13.0/−16.1, seeker/hider); higher requested reasoning effort shows no consistent gain.

## Audit checklist (apply to any "our agent has ToM" claim)
1. Can a reactive/behavioral control (win-stay-lose-shift, frequency matching) reproduce the headline payoff?
2. Are forecasts scored against a ground-truth generative model, or only against observed actions?
3. Is the claimed gain measured when opponent information must be INFERRED from history, not supplied?
4. Do true vs shuffled belief interventions change choices (field sensitivity), AND does correct content specifically help (content benefit)? Both must hold.
5. Does the task make belief-based and reactive strategies DIVERGE after diagnostic feedback? In binary tasks they can coincide — design tasks where they separate.
6. Are prediction gains tested LIVE (own actions shape observations), not only fixed-history? Distribution shift from training-buffer reuse is a known failure mode.
7. Check report depth: deeper belief elicitation (L1/L2/L3) and self-generated memory did NOT reliably improve forecasts — report depth is not opponent order.

## Pitfalls
- Structured output (forcing the model to write predictions before acting) helps GPT-5.4 hiders (+9.0) but HURTS Qwen2.5 vs WSLS (−26.8/−31.9) — format interventions are model- and opponent-specific.
- A reported prediction conditioning later text does not prove the prediction CAUSED the choice.
- In binary games, distinct beliefs and reactive heuristics yield identical choices and payoff — null results are uninformative without divergence design.
- Simulator states are exact targets for the algorithmic opponents, not validated human mental states — external validity is a separate question.
- Live-play gains after SFT did not transfer robustly: action-only SFT earned +1.9 as seeker but −14.7 as hider against GPT-5.4 as a live opponent (role sensitivity).

## Transferable patterns
- **Ground-truth-by-construction**: evaluate social inference against algorithmic agents with known beliefs rather than human labels.
- **Use-vs-inference intervention**: any capability claim (planning, world models, ToM) should be tested both with information supplied and with information withheld-but-inferable; the gap between the two is the real capability frontier.
- **Match-bootstrap CI**: resample whole episodes, never individual decisions (within-episode dependence).
- **Known-rule positive control first**: verify the model can EXECUTE the generative rules when handed them (GPT-5.4: 96.3% of scheduled predictions within 0.001 of reference) before testing whether it can INFER them from history.

## Key numbers
| Measurement | Value |
|---|---|
| Qwen2.5-7B prob-only SFT MSE (with spec) | 0.08119 → 0.00990 (constant 0.05874) |
| Same, spec removed | 0.01206 → 0.05182 (×4.3) |
| Mixed-exposure history-only MSE | −31.65% (paired diff −0.01559, CI [−0.02054, −0.01071]) |
| GPT-5.4 true-belief supply | agreement 66.7% → 96.3%, regret −0.18676 (CI [−0.26968, −0.10510]) |
| GPT-5.4 autonomous belief MSE | 0.02717 vs constant 0.01258 (WORSE) |
| GRPO RL vs WSLS / ToM2 / GPT-5.4 | +38.3+33.4 / +1.0+0.5 / −8.6−17.5 (seeker/hider) |
| True vs shuffled belief prefix | actions differ on 10.3% of decisions; MSE advantage uncertain |

**Activation**: theory of mind evaluation, LLM mentalizing audit, opponent modeling, repeated games, belief tracking, k-ToM, tomsup, agent evaluation rigor, use vs inference, ground-truth opponents, hide and seek benchmark, adaptive play vs ToM
