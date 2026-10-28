---
name: sota-strategy-selection-option-agents
description: "Use when post-training LLM agents for option/multi-instrument trading. Strategy-level abstraction."
category: economics
trigger: "option trading agent, strategy-level action space, LLM trading post-training, GRPO portfolio, frontier distillation, agentic trading, resolver pattern, news ablation"
---

# SOTA: Strategy-Level Action Abstraction for LLM Option-Trading Agents

**Source**: Xie & Liu, "SOTA: Stock Options Trading Agents Guided by Option-Implied Return Distributions" (arXiv:2610.10407, CMU + Amazon, 2026-10-07). Qwen3.8-27B post-trained via SFT→GRPO; +18.32% OOS return, Sharpe 1.60, MDD 8.96% over 6 months on SPY + 9 large-caps while every rule-based and ML baseline was negative.

## When to Use

- Training an LLM agent to trade options, or any market where the raw action space is combinatorially explosive (thousands of instruments × expiry × type) and changes over time.
- Designing a post-training pipeline that mixes expert-distillation (SFT) with outcome-based RL (GRPO).
- Deciding whether textual features (news/filings) belong in the RL information set — they often do NOT (asymmetric information role).

## Core Pattern 1 — Strategy-Level Action Abstraction + Deterministic Resolvers

**Problem**: contract-level choice = thousands of contracts per underlying, dynamically listed/delisted; direct token-level decisions are time-sensitive and context-blowing.

**Solution — three-layer separation**:

1. **Policy layer (LLM)**: selects `(underlying u, family f, orientation ω, tenor θ, delta κ)` from 9 economically meaningful strategy families spanning 4 exposure classes:
   - Directional (outright, debit/credit vertical, defined-risk reversal) — net delta view
   - Volatility long-gamma (long straddle, long strangle) — movement view
   - Volatility short-gamma (iron butterfly, iron condor) — range view
   - Curvature (butterfly) — central vs extreme strike pricing view
2. **Resolver layer (deterministic code)**: contract resolver picks expiry nearest tenor anchor {5,14,45,120}d and strike with Δ closest to requested Δ*; size resolver equalizes risk via second-order Taylor (R = |Δ|σ̂ + Γ(Sσ̂)²/2 + |ν|σκ + |Θ|); hedge resolver applies Whalley–Wilmott no-hedge band H = (3kSΓ²/2λ)^(1/3) e^{-r(T-t)}.
3. **Environment layer**: midpoint execution, fees/commissions, expiring contracts settle; portfolio state (open positions, exposures, NAV) feeds back into the next state.

**Action verbs**: open / close / roll / hold — rolling keeps positions alive across expiries rather than flatten+reopen.

**Two-stage candidate proposal**: the agent first proposes up to 6 candidate strategies per underlying; only those get priced. Price-aware selection without stuffing the full chain into context.

**Key discipline**: the resolver returns the *realized* coordinate on the receipt line — request ≠ fill is never silently assumed.

## Core Pattern 2 — SFT-from-Frontier then GRPO Post-Training

**Stage A (SFT)**: generate trajectories with a frontier model on point-in-time states; **anonymize first** (mask stock identity, absolute price levels, calendar time) to prevent temporal/identity leakage; filter retained trajectories by annualized Sharpe; SFT the 27B student (414 episodes, lr 1e-5, 3 epochs).

**Stage B (GRPO)**: group size 8, actor lr 5e-7, KL coef 0.01, PPO clip 0.2; reward = change in log portfolio value net of transaction costs (trajectory-level). Checkpoint every 10 steps, evaluated on test window; report the honest checkpoint (they use step 20, not step 40 — check both).

**Chronological splits are sacred**: SFT 2024-09→11, RL 2024-12→2025-02, test 2025-03→08. No overlap.

## Core Pattern 3 — Asymmetric Information Role (the honest negative result)

| Variant | TR | ASR | MDD |
|---|---|---|---|
| Full (RL, no news) | **+18.32%** | **1.60** | **8.96%** |
| RL WITH news retained | −2.72% | −0.16 | 31.69% |
| SFT only, no RL | −10.19% | −1.25 | 15.56% |

- News **helps the frontier teacher** produce better SFT trajectories.
- News **hurts during RL**: retaining it collapses OOS return from +18.3% to −2.7% and triples drawdown.
- RL genuinely improves the SFT policy (−10.2% → −2.7% with same info set), but the full +18.3% **additionally requires stripping news from the RL state**.
- Generalized lesson: *information useful for constructing expert supervision need not remain useful during downstream policy optimization.* Ablate the RL information set separately from the SFT corpus.

## Baselines (all negative — the bar the paper clears)

Equal-weighted −5.22%, GARCH −49.24%, threshold −28.46%, GBDT −49.78%, logistic −55.45%. All share the same execution model, costs, constraints and resolvers — differences are purely strategy selection.

## Implementation Checklist

- [ ] Reduce raw instrument space to ≤ ~10 strategy families + small parameter grids (tenor buckets, delta grid)
- [ ] Write contract/size/hedge resolvers as deterministic code — never let the LLM output contract IDs or sizes
- [ ] Anonymize teacher-trajectory states (identity/price/calendar) before SFT
- [ ] Filter teacher trajectories by risk-adjusted performance before SFT
- [ ] GRPO reward = log NAV change net of costs; trajectory-level discounting only
- [ ] Run news-on/news-off ablation on the RL state independently of the SFT corpus decision
- [ ] Report the checkpoint honestly (eval multiple, don't cherry-pick)
- [ ] Compare against rule-based + supervised ML baselines under identical execution

## Pitfalls

- Putting the full option chain in context — use candidate-proposal staging instead.
- Letting request≠fill discrepancies pass silently — always return realized coordinates.
- Assuming RL inherits SFT's optimal information set — ablate independently.
- Mixing SFT/RL/test windows — keep chronological splits strictly disjoint.
- Qwen training numbers: max seq 33,280 (32,768 content + template tokens); episodes over budget are dropped, not truncated.

## Cross-references

- `wrap-adversarial-deep-hedging` (arXiv:2610.07162) — robust option hedging line, same market family
- `heterogeneous-llm-collusion-bertrand` (arXiv:2610.11256) — agentic market interaction line
- GRPO reference: Shao et al., 2024
