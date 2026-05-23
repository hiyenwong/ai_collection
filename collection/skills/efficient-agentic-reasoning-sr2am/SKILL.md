---
name: efficient-agentic-reasoning-sr2am
description: "SR²AM (Self-Regulated Simulative Reasoning Agentic LLM) methodology from arXiv:2605.22138 (May 2026). Three-system framework decomposing agent reasoning: System II (simulative planning via world model), System III (self-regulation deciding when/how to plan), and System I (reactive execution). Use when working on: agent reasoning architectures, adaptive computation for LLM agents, self-regulated planning, token-efficient reasoning, or world-model-based planning."
---

# SR²AM: Self-Regulated Simulative Reasoning Agentic LLM

**Paper:** arXiv:2605.22138 (May 2026) — "Efficient Agentic Reasoning Through Self-Regulated Simulative Planning"

**Core Insight:** SR²AM introduces a three-system cognitive architecture (Systems I/II/III) for LLM agents that decouples *what* to predict (future states) from *when/how much* to plan (self-regulation). By framing both simulative reasoning and self-regulation as distinct stages within a single LLM chain-of-thought, SR²AM achieves more efficient deliberation — the LLM serves double duty as both the world model for simulation and the self-regulator that decides planning depth.

---

## 1. Three-System Framework

### System I — Reactive Execution
- **Role:** Handles fine-grained action execution in the environment.
- **Behavior:** Direct, reflex-like responses (similar to standard LLM generation without explicit planning).
- **Triggered when:** System III determines that no simulative planning is needed — the current state is simple, familiar, or low-stakes.
- **Efficiency:** Zero overhead from simulation; fast token generation.

### System II — Simulative Reasoning
- **Role:** Grounds deliberation in future-state prediction via a world model.
- **Behavior:** The LLM acts as a **world model** — it simulates possible future trajectories (rollouts) from the current state, evaluating outcomes before committing to an action.
- **Key Mechanism:** Simulative planning within chain-of-thought: the LLM generates candidate action sequences, predicts resulting world states, and selects the trajectory with highest expected utility.
- **Planning Horizon:** Controlled by System III — can range from shallow (1-2 steps) to deep (5+ steps) simulation.

### System III — Self-Regulation (Configurator)
- **Role:** Decides *whether* to plan, *how deeply* to plan, and *when to stop* planning and act.
- **Behavior:** A learned "configurator" module that observes the current state and context, then outputs a planning budget (e.g., number of simulation steps, search width, temperature for rollouts).
- **Key Mechanism:** The configurator learns a policy over planning depth — it balances deliberation cost against expected accuracy gains.
- **Training:** Optimized via reinforcement learning with a reward that trades off task success vs. computational cost (token usage).
- **Output:** Control signals injected into System II's chain-of-thought (e.g., "simulate 3 steps" or "act immediately").

---

## 2. Methodology

### World-Model-as-LLM
SR²AM reuses the same LLM for both world-model simulation and action policy — there is no separate trained world model. During System II, the LLM is prompted to:
1. Propose a candidate action.
2. Predict the resulting world state given that action.
3. Score the desirability of that predicted state.
4. Repeat for additional candidates (within the budget set by System III).
5. Select the action with the best expected outcome.

### Self-Regulation as CoT Stage
System III's configurator is implemented as an additional chain-of-thought stage that precedes System II. This stage:
- Analyzes the current observation and task context.
- Estimates the value of planning (e.g., "this is a high-stakes decision with long-term consequences; deeper planning needed" vs. "this is a simple next-step; no simulation required").
- Outputs structured control tokens that influence System II's simulation budget.

### Chain-of-Thought Flow
```
Observation → [System III: Configurator] → planning_budget → [System II: Simulative Reasoning] → selected_action → [System I: Execution]
```
If System III outputs `budget=0`, the system skips System II entirely and goes directly to System I execution.

---

## 3. RL Fine-Tuning for Planning

### Training Setup
- **Base model:** An instruction-tuned LLM (e.g., LLaMA-3 or equivalent).
- **Two-stage fine-tuning:**
  1. **Simulation fine-tuning:** Train the LLM to produce high-quality rollouts (accurate world-state predictions and action evaluations) via supervised learning on demonstration traces.
  2. **Self-regulation fine-tuning:** Freeze System II capabilities; train System III's configurator via RL (PPO) to optimize:
     - **Task success reward:** Positive reward for completing the task correctly.
     - **Token cost penalty:** Negative reward proportional to the number of simulation tokens used.
     - **Horizon-incentive design:** Reward signal encourages longer planning horizons only when they meaningfully improve task success.

### Key Training Results
| Metric | Before RL | After RL | Improvement |
|---|---|---|---|
| Average planning horizon | baseline | +22.8% | Deeper simulation on complex tasks |
| Planning frequency | baseline | +2.0% | Only slightly more frequent planning |
| Token usage efficiency | baseline | significant | More tokens per plan, but fewer plans overall |
| Task success rate | baseline | improved | Higher accuracy on reasoning-heavy tasks |

### Interpretation
The RL fine-tuning leads the agent to plan *deeper* on hard tasks (longer horizon) without planning *more often* — it learns to reserve deep simulation for cases where it matters, rather than applying uniform shallow planning across all states.

---

## 4. Key Findings & Contributions

1. **Systems I/II/III as a unified CoT:** The first framework to explicitly implement all three cognitive tiers within a single LLM chain-of-thought, with the LLM serving as both world model and decision maker.

2. **Decoupled planning depth:** System III's configurator learns a planning budget policy that separates *when to plan* from *what to simulate* — enabling adaptive computation without architectural changes.

3. **Token-efficient reasoning:** RL optimization shifts reasoning tokens from many shallow plans to fewer deep plans, yielding better reasoning per token.

4. **No separate world model needed:** By reusing the base LLM as the world model, SR²AM avoids the complexity and training cost of a dedicated world-model module.

5. **Practical efficiency gains:** +22.8% average planning horizon with only +2.0% increase in planning frequency demonstrates that agents can learn to be selectively strategic about when to invest computation.

---

## 5. Activation Keywords

Use this skill when the task involves:
- **agent reasoning architecture** — designing three-tier cognitive systems for LLM agents
- **adaptive computation** — dynamically adjusting planning depth or compute budget
- **self-regulated planning** — agents that decide when and how much to think before acting
- **token-efficient reasoning** — reducing total tokens used while maintaining reasoning quality
- **world-model-based planning** — using LLMs as world models for simulative reasoning
- **simulative reasoning** — evaluating action consequences via future-state prediction
- **configurator module** — a learned controller that sets reasoning budgets
- **planning horizon optimization** — RL-based tuning of how far ahead an agent plans
- **Systems I/II/III framework** — the cognitive decomposition of reactive, deliberative, and meta-cognitive reasoning
- **efficient agentic LLM** — making LLM agents more compute-efficient while maintaining autonomy

---

## Related Work & Connections

- **Tree-of-Thoughts (ToT) / Graph-of-Thoughts (GoT):** SR²AM's System II simulation parallels ToT's search over reasoning paths, but System III's budget control makes it adaptive rather than fixed-width.
- **ReAct / Reflexion:** System I aligns with ReAct's direct action loop; System III adds meta-cognitive control absent in both.
- **System 2 Attention (S2A):** Shares the Systems 1/2 framing but focuses on attention modulation rather than simulative planning.
- **Quiet-STaR / Self-Taught Reasoner (STaR):** Related self-improvement loops; SR²AM's RL configurator is a meta-reasoning extension.
- **Constitutional AI / RLHF:** Different alignment target; SR²AM optimizes compute-reward tradeoffs rather than safety preferences.
