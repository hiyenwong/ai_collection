---
name: availability-contract-earnings-nlp
description: Use when auditing label-clock validity in event NLP benchmarks.
category: ai_collection
---

# Availability Contract for Event-Window NLP Benchmarks

**Paper**: "When Does \"Post-Call\" Begin? An Availability Contract for Earnings-Call NLP Benchmarks" — Ma, Koa, Liu, Huang (NUS/AIDF), ICAIF '26, arXiv:2610.21659 (submitted 15 Oct 2026).

## Core Problem: Within-Event Timing Mismatch

A financial NLP benchmark predicts returns from event inputs (earnings calls: prepared remarks + Q&A, often ~1 hour). The prediction target (return window) frequently begins BEFORE the declared input could be complete — the call is still ongoing. Chronological train-test splits do NOT fix this: the leakage lives INSIDE individual events (between the representation boundary and the label start), not between samples. What is measured then is an event-window ASSOCIATION, not post-input prediction. The estimand must be declared, not defaulted.

## The Availability Contract (9 fields)

Any event-based benchmark must state:
1. **Permitted claim q** — which rung of the claim ladder (below) the timing evidence supports
2. **Input boundary B** — what information the representation includes (e.g. complete spoken Q&A)
3. **Source-to-completion-proxy rule G** — evidence + rule for when input completion is proxied (e.g. t_audio = source_start + max(MP3 duration, alignment endpoint))
4. **Allowance l** — stipulated processing margin (e.g. +15 min; audit a 0-120 min grid)
5. **Checkpoint record K** — model identity, knowledge boundary, point-in-time availability
6. **Inference-completion evidence M** — how long scoring actually takes
7. **Price-anchor rule A** — mapping from completion time to a market price (bar-close, NOT execution price)
8. **Endpoint E** — the common outcome endpoint
9. **Sample rule S** — joins, attrition, complete-case definition

Label start = A(G(B) + l) on the stated market calendar.

## Claim Ladder (what the timing evidence permits)

| Claim | Permitted interpretation |
|---|---|
| Event-window association | Return may span the event; interpretation is association, NOT post-input attribution |
| Proxy-aligned association | A stated completion proxy precedes label start; interpretation is conditional on the proxy |
| Verified post-input | Observed input completion (or defensible upper bound) precedes label start |
| Deployability | Point-in-time input, model, order, AND execution clocks observed/bounded; costs modeled |

Do not describe a rung-1 design as post-input prediction. A rung-4 claim additionally requires the checkpoint's knowledge boundary to precede the forecast (point-in-time model state, not just data state).

## Paired Three-Clock Audit (the diagnostic instrument)

Fix the sample AND endpoint; vary only the starting price. Three clocks:
- **L (legacy)**: preceding-session close — event-spanning window
- **S (source-start)**: close of first regular-session 5-min bar starting strictly after the documentary source-start timestamp
- **A (ready proxy)**: same rule after reconstructed audio end + allowance l

Because LOG returns over adjacent intervals add exactly (r_L = d_LS + r_A), and OLS is linear in the outcome, the same-design OLS identity holds: **beta_L - beta_S = beta_LS, beta_S - beta_A = beta_SA**. Each coefficient contrast is localized to precisely the return interval the clock change removes — rows, representation, controls, fixed effects, estimator all held fixed. This converts "where did the association go?" into an additive decomposition.

Separately from label start, hold A fixed and vary elapsed time (exact 390-trading-minute endpoint) to distinguish label-start sensitivity from holding-period sensitivity.

## Headline Empirical Findings (552 calls, 24 firms, 2018-2024)

- S->A alone (15-min allowance): **9.4% of raw-return signs flip**, 28.3% change fixed-A quintile, 30.1% change relative quintile. Spearman rho(S,A) = 0.900 — highly correlated targets, yet 1-in-10 labels reverse.
- L->S (event dating): rho = 0.506, 32.1% sign flips, 64.3% quintile reassignment — the bigger effect, but the S->A increment is the novel part.
- Association localization (Qwen answer-valence): beta_L = +1.122, beta_S = -0.135, beta_A = -0.233 pp/SD. The full L->A shift (+1.355) decomposes as +1.256 over L->S and only +0.098 over S->A — most association lives BEFORE the source-start anchor.
- External check (DEC benchmark, frozen predictions, 1,710 events): shifting 1,191 before-market targets forward one session raises 3-day MSE by **18.1-21.4%** across four prediction streams — while **point rankings are unchanged** (Kendall tau = 1 at every horizon). Stable leaderboard does NOT mean robust targets or losses.
- Attrition is selective and must be reported: usable source clock keeps only 26.4% of the parent panel (2,094 -> 552), shifting toward later years, larger firms (~1 pooled SD in log market cap).

## Methodological Rules to Reuse

1. **Declare the estimand before the clock**: an L-window is legitimate for event-response research; an A-window is required for post-input evaluation claims. Both can be reported; neither is universal.
2. **Log returns, not simple returns**: adjacent intervals must add exactly so the OLS decomposition identity holds (simple returns compound).
3. **Bar-close anchors, never instant prices**: each anchor is the close of a bar starting strictly after its proxy — this makes timestamp->price mapping reproducible and mechanically checkable (after-close calls: S and A collapse to the same next-session bar, rho = 1, zero change — a built-in falsification check).
4. **Report allowance sensitivity as an envelope**: across the 0-120 min grid, sign-flip rates span 6.5-15.0% — a single allowance number hides this.
5. **Freeze representations and score retrospectively**: fix model checkpoint, decoding, truncation; all representation-level inference is exploratory (multiple-testing adjusted via Holm/BH within declared families).
6. **Common-anchor vs own-boundary comparisons**: comparing an early-partial-transcript model and a complete-Q&A model from one shared later anchor measures relative content; comparing each from its own declared boundary compares two different forecasting TASKS. Do not conflate them.
7. **Ranking stability is not target stability**: always rescore frozen predictions under the perturbed clock before claiming a benchmark is timing-robust.
8. **Attrition accounting**: report retained-at-each-stage percentages relative to both previous stage and parent panel; a selective clock join can silently re-weight the firm/year distribution.

## Generalization Beyond Earnings Calls

Any sequential-disclosure benchmark has the same structure: press conferences, product launches, court rulings, central-bank pressers, medical announcements, sports lineups. The contract transfers: state the input boundary, the completion proxy, the allowance, the anchor rule, the endpoint, and the permitted claim. The paired-clock audit transfers whenever the outcome is a market (or any additive-in-time) measurement anchored to a calendar.

## Limitations Noted by the Authors

- Transcript/model inference completion is UNOBSERVED — only audio duration + allowance is available; hence "proxy-aligned association" is the strongest claim this evidence supports for their own audit.
- Representations were inspected before family freezing (Qwen construct marked exploratory).
- Price data vendor semantics (timezone, adjustment) not independently certified.

## Related Skills

- [[backtest-live-parity-defects]] — implementation-level backtest drift (six defects); complementary: that skill covers code/data drift, this covers estimand/clock validity.
- [[hawkes-common-signal-spurious-excitation]] — identification audits in financial point processes.
- [[ts-validation-impossible-trinity]] — time-series validation trade-offs; the contract is the event-study instance of declaring what is validated.
