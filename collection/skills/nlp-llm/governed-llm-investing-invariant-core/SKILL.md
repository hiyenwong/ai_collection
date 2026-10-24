---
name: governed-llm-investing-invariant-core
description: Use when agent self-evolution must not weaken safeguards.
category: economics
trigger: self-evolving LLM agent, autonomous investing agent, prompt self-edit governance, agent guardrail erosion, LLM trading system, replay verification of agent changes
arxiv_id: "2610.30557"
---

# Governed Self-Evolution for Autonomous Investing (Steward)

Methodology from "Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core" (arXiv:2610.30557, Feng, Dai, Pan, Lau, Xu, Liu — NTU/UCL, Oct 2026). A nine-agent LLM system traded live 102 days; the reusable contribution is a **type-system boundary** that lets an agent rewrite its own prompts while making safeguard erosion structurally impossible.

Open system: github.com/yebof/quant-agent

## The core problem: four failure modes of self-improving agents

A self-improving loop (act → grade → reflect → edit own policy π → act) fails silently in four ways:

- **F1 Self-grading**: the evolution signal is the agent's own optimistic assessment ĝ_t, not the outcome y_t.
- **F2 Discipline erosion**: π′ weakens the risk rules, because nothing separates what the loop may change from what it must not.
- **F3 Unauditable change**: no record ties π′ to the evidence that produced it — an erroneous edit can be neither found nor reverted.
- **F4 Undetected inertness**: an edit passes every check yet changes no decision; the loop reports progress it did not make.

## The five governance requirements (R1–R5)

| Req | Rule | Kills |
|---|---|---|
| R1 Typed record | Every decision d_t is a machine-checkable object stored WITH its input x_t; code can grade, read, replay the whole trace | F1, F3 |
| R2 Outcome grading | Every signal fed back into decisions/reflection is computed from outcomes y_t by deterministic code, never by the LLM | F1 |
| R3 Typed proposals | Every proposed change is a typed object whose justification must cite a number from the graded record | F3 |
| R4 Gated application | Deterministic code applies proposals under invariants, logs accept/reject, reverts in one step, and cannot reach the invariant core π₀ | F2, F3 |
| R5 Verification by replay | A proposal's effect is measured by re-running recorded inputs through π′ and structurally diffing outputs | F4 |

**Key idea**: draw the boundary of self-evolution **in the type system, not in a prompt**. The proposal type cannot name the core; discipline agents are absent from the proposal schema's Literal target list. An agent can rewrite itself but cannot weaken its own safeguards — no instruction has to be trusted.

## Invariant core π₀ (untouchable) vs evolvable periphery

**Core** (no self-edit can reach):
- Order arithmetic: a deterministic constructor turns PM intent into orders (target weight ≤20%, stop = PM/TA value or 2·ATR below entry, widened if <1 ATR; size = min(target weight, 0.5% equity risk budget at stop); skip entry >5% from market; skip trade with R/R <1.2 after execution moves prices).
- Blocking risk engine running BEFORE any LLM audit: no negative cash, position ≤20% equity, sector ≤40%, net exposure ≤90%, no entry without stop, no buy after −3% day. LLM Risk Manager may reject/modify/scale but can never approve what the engine blocked; it **fails closed** (schema/call failure ⇒ reject).
- Discipline-agent prompts (Risk Manager, Position Reviewer).
- Circuit breaker: no LLM, every 30 min; on −3% daily loss cancel entries and liquidate.

**Periphery** (gate may append to): 7-layer shared memory (rewritten daily by code) + Learnings sections of the 6 editable agent prompts (4 analysts, PM, Evening Analyst).

## Nine agents, six sessions

- Morning (only session that may open positions): 4 analysts → typed reports → PM (7-step CoT → TargetPosition) → constructor → hard rules → Risk Manager → executor (sells first as limits, wait for fills, re-check daily loss before buys, record order before submission, GTC stop immediately after each buy fills).
- Midday/close: sell-only Position Reviewer (SELL/REDUCE/TRAIL_STOP/HOLD).
- Evening: code grades every trade/forecast, Evening Analyst 7-step CoT assigns correct/premature/wrong + one of 9 root causes for wrong buys.
- Quarterly: Meta Reflector proposes ≤3 PromptLearning objects.
- Agents: News Intelligence (3-layer typed report), Earnings (10-Q/10-K), Macro (regime classification from FRED), Technical (5-level rating with entry/stop/falsifier), PM, Risk Manager, Position Reviewer, Evening Analyst, Meta Reflector. Orchestration: session lock, 20-min kill, 7 retries with backoff, vendor failover; every other failure removes an action rather than adding one.

## Seven-layer shared memory (assembled by code, never by an agent)

L1 today's typed signals · L2 position context + last 7 technical ratings · L3 narrative/regime/active state changes · L4 **45-day calibration by entry size** (FIFO buy-exit matching: win rate, mean return, hold time for <$5k/$5–10k/>$10k) · L5 last 5 Risk Manager verdicts · L6 own last 3 decisions (reversals visible) · L7 projected book flagging sectors near caps.

> Every number an agent can cite comes from code, not from another agent's prose.

## Schema-enforced reasoning

Each agent's output is a Pydantic object embedding its CoT: every reasoning step is a required `str = Field(min_length=1)`, enums are `Literal` types, cross-field validators encode domain invariants (actionable rating must carry entry+stop on the protective side; wrong grade must name a root cause; proposal must cite a number). Malformed list items are dropped and logged individually instead of invalidating the report.

## Quarterly gate invariants (deterministic, two layers)

Proposal schema first (malformed → rejected before staging); then PromptEditor invariants: append-only into marked section; tag with quarter + content hash (human text never modified); allow-list targets; **word-boundary tripwire** rejecting absolutes (never/always/override) that would conflict with hard rules; **Jaccard ≥0.6 rejects paraphrases**; FIFO cap 10 entries/agent; ≤3 agents change per cycle; every accept/reject logged with reason; one cycle = one version-control commit → `git revert` undoes a quarter of evolution in one step.

Reflector input is a deterministic 90-day digest (alpha vs SPY, calibration by size, themes caught/missed, root causes, per-agent signal activity) + all editable prompts + previous reflection. Its 7-step CoT ends with a prompt audit: "does a rule for each gap already exist?" (prevents overcorrection — in deployment the reflector declined to re-add a rule it had already applied, citing that risk).

## Verification by replay (R5) — the anti-inertness instrument

Every LLM call is stored with full input/response/model/cost. The replay harness re-runs recorded inputs through the prompt before/after a learning, diffs structurally (symbols added/dropped/resized; evening grades/bias changes), and — crucially — **re-runs the UNCHANGED prompt to measure the model's own variance**, against which the learning's effect is read. Cost: tens of dollars per experiment ($16–19 here). Replay caught what the gate's invariants could not: an applied learning whose trigger presupposed a count absent from the input (recurring misses unchanged 25/64 → 26/64), while confirming the targeted behavior appeared in 5/20 trigger replays vs 0/20 base and never on controls.

## Field-study findings (102 live trading days, $100k, 1,632 calls, $455)

- **Individual analyst signals are weak; the synthesis carries the value**: technical-rating rank IC −0.004/0.019/0.031 (5/10/20d), news sentiment uncorrelated; yet PM synthesis of the weak signals returned +12.2% (Sharpe 2.33) vs SPY +12.4%, analyst-following +1.3%.
- **Single-agent-on-raw-data is a different, worse trader**: 5.8 names/morning vs 3.7, 41% new intent vs 19%, reverses itself 2.5×, re-buys just-closed names, books lose −1.35±0.44pp (5d) vs market; joint design indistinguishable from zero. Removing the memory changes little per-morning — the memory's value is longitudinal (calibration, continuity, feedback).
- **Drawdown containment**: portfolio −0.3% through a window where the semiconductor ETF fell 24.6% (QQQ −10.3%, SPY −2.0%). Core alone (LLM-free entries, 2015–2026) lowered max drawdown under all 50 random entry policies (median 37%→28%) at unchanged Sharpe — the core bounds what judgement can lose.
- **Adaptation runs through graded memory, not stated intent**: realized exposure co-moves with trailing forecast hit rate (ρ=0.34, p=0.01) while the PM's declared sizing does not (|ρ|≤0.14).
- **Outcome grading exposes what self-grading hides**: the Evening Analyst graded 134/163 sells "correct", but outcome-scored opportunity cost showed stops (n=132) gave up only $0.7k post-exit while agent exits (n=306) gave up $19.9k.
- **Injection resistance without prompt-only defense**: 3 adversarial payloads (direct override; plausible headline "300% upside, stops disabled"; discipline suspension) inserted into 10 recorded mornings — followed in 0/30 replays; News agent excluded+flagged the item in all 20; in 23/30 the PM named it and cited the stop/cash conflict. Untrusted raw text reaches only the two reader agents; code drops news state changes whose keywords/symbols appear in neither input nor prior state; PM never sees a headline.
- **A strict gate costs nothing here**: the Q2 learning withheld on a length invariant (282>200 chars) was shown by replay to be inert anyway.

## Transferable checklist (any consequential-decision LLM agent)

1. Enumerate the four failure modes; map each to R1–R5.
2. Split policy into invariant core π₀ vs evolvable periphery; enforce the split in the **proposal type**, not instructions.
3. Put every quantitative feedback signal in code computed from outcomes; LLMs may categorize, never score.
4. Fail closed on LLM/schema failure; run hard deterministic rules before any LLM audit.
5. Keep untrusted content upstream of decision agents (typed intermediaries + code-level consistency checks).
6. Make every cycle a single reversible commit; log accept/reject with reasons; tripwire absolutes; dedupe paraphrases (Jaccard).
7. Verify by replay against measured model variance before claiming any progress; budget tens of dollars per experiment.

## Pitfalls

- Prompt-only guardrails are rewritable by the very loop they constrain — the boundary must be structural (type system).
- Self-graded evolution reports progress that replay shows is inert (F4) — never announce a learning without replay.
- Backtests of LLM agents cannot exclude pre-training leakage; record decisions before outcomes exist and evaluate forward.
- Execution realism dominates: live returned +5.0% vs intent +12.2% at 56% vs 79% realized exposure (180/492 orders unfilled) — always decompose policy layers (intent → executed → benchmark).

## Related topics

- governed-self-evolution-anytime-referee (frozen-referee variant of the governance problem)
- athena-distributed-quantum-compiler · web-agent prompt-injection defenses (raised-prompt-injection-self-distillation)
- LLM-agent serving with execution-state checkpoints (reversible evolution commits)
- lvr-transaction-cost-amm (companion DeFi cost model)
