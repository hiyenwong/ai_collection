---
name: skillbrowser-selective-skill-exposure
description: "Selective Skill Exposure (SSE) methodology for LLM agents with large skill libraries. SkillBrowser = Meta-Skill-managed access: a fixed meta-skill lets the agent recognize emergent capability needs mid-reasoning, emit structured capability-oriented queries (capability description + task context + required attributes + type hints + positive/negative signals), and load skills on demand via SkillGrep hybrid retrieval (lexical + semantic over multi-view metadata expansion). Beats static retrieval and progressive disclosure across 6 SRA-Bench subsets × 5 LLMs (ToolQA 43-61% vs 17-39%); surpasses even gold-skill injection in 13/30 settings, showing unnecessary exposure actively disrupts solvable tasks. Use when scaling agent skill systems, designing skill retrieval, or diagnosing context pollution from skill metadata. Activation: selective skill exposure, meta-skill, skill retrieval, skill library scale, context pollution, capability-oriented query, SkillGrep, SRA-Bench, on-demand skill loading."
---

# SkillBrowser: Selective Skill Exposure for Scalable Skill-Using Agents

Methodology from arXiv:2610.23554 (Jiang, Ye, Guo — Nanjing University, Oct 2026; cs.AI). Solves the central scaling problem of skill-using agents: a repository of N skills (their benchmark: 26,262) cannot be naively exposed to the agent's context.

## Problem Formulation (SSE)

Repository S = {(m_j, f_j)}: metadata + full procedural content per skill. At potential exposure step i with solving context c_{i−1}, the ideal exposure is state-dependent: z_i* ∈ {0,1} decides whether ANY external skill content should enter context (no-exposure is a legitimate, common ideal — skills are not always needed, and injected instructions alter subsequent reasoning).

Two incumbent paradigms fail complementarily:
- **Progressive disclosure** (expose all metadata, load contents on demand): E^PD = {m_j} — metadata grows with the repository, consuming context budget and adding semantic noise BEFORE the needed skill is even found. At 26k skills the metadata list alone (capped at 20k tokens in their diagnostic) exhausts context and the agent never loads the gold skill. **Context pollution scales with N — this paradigm cannot scale.**
- **Static retrieval** (retrieve top-k from the initial task query, inject contents): E^SR = F(R(P,S,k)) — two failure modes: (a) **capability misalignment**: the capability need is obscured by a noisy request or only EMERGES during reasoning, so initial-query retrieval misses it; (b) **unnecessary injection**: retrieved contents enter context regardless of whether help is needed, disrupting tasks the agent would otherwise solve.

## SkillBrowser: Meta-Skill-Managed Access

The agent receives ONE fixed Meta-Skill s* alongside the user task. s* contains no task procedure — only HOW to access the repository:

- **No separate retrieve-or-not decision stage.** The agent proceeds with ordinary inference/interaction and invokes the search interface whenever an external capability need arises. E_i^SB = F(R(q_i,S,k)) if invoked, ∅ otherwise.
- **Capability-oriented structured query** q_i = Q_M(P, c_{i−1}; s*) — formulated from task P AND current solving context, not a repeat of the user request. Query schema fields: concise capability description · relevant task context · required/preferred capability attributes · type hints · positive AND negative retrieval signals · explicit constraints. Negative signals let the agent exclude lookalike-but-wrong skills.
- **Training-free** — no fine-tuning; the meta-skill is a reusable prompt artifact.
- **Under-invocation is the acknowledged failure mode**: the agent may fail to recognize a need it has (benefits are model-dependent; GLM-5.1/Qwen3-8B weakest at need recognition). Latency overhead per invocation is real but bounded (one retrieval round, not per-step).

## SkillGrep: Capability-Oriented Retrieval

- **Offline expansion**: each raw skill → multiple retrieval views (capability descriptions, usage conditions, representative queries, original instructions). Normalizes heterogeneous skills into a shared retrieval interface while preserving original contents.
- **Online hybrid matching**: lexical (precise terms/identifiers — catches exact API names, equation names) fused with semantic (paraphrased capability needs); returns top-k; contents flow back into the agent loop.
- Practical note: BM25-only backend retains most of the managed-access benefit (their component analysis: Meta-Skill+BM25 ≈ most of SkillBrowser's gain — the ACCESS POLICY matters more than the retriever).

## Key Results (6 SRA-Bench subsets × 5 LLMs: Qwen3-8B, Qwen3.6-Plus, GLM-5.1, GPT-5.4-mini, Gemini-3.1-Flash-Lite)

- vs **LLM selection** (SR-Agent baseline, pick from BM25 top-50): 21 wins / 4 ties / 5 losses.
- vs **static SkillGrep**: consistent gains across ALL 5 models on TheoremQA, MedCalcBench, ToolQA; LOSSES persist on CHAMP and LogicBench (tasks where the needed capability is hard to state as a query — retrieval, not exposure, is the bottleneck there).
- **ToolQA (multi-step tool use): 43–61% vs 17–39%** for static retrieval — the emergent-need setting is where managed access shines.
- **Gold Exposure is NOT an upper bound**: directly injecting the annotated gold skill LOSES to SkillBrowser in 13/30 settings — even a perfectly relevant skill disrupts an agent that would solve the task unaided. The no-exposure option has positive value.
- Avoiding unnecessary exposure (skill-unnecessary instances) is where Meta-Skill management most reduces degradation.

## Application to Real Agent Stacks

For Hermes-style agents (thousands of skills, system-prompt-bounded metadata lists):
- The default pattern — inject ALL skill descriptions into the system prompt — is progressive disclosure's context pollution at its worst; the 60-char description budgets used by skill registries are a mitigation, not a solution.
- The SkillBrowser fix maps to: keep the catalog external; expose only a small fixed "meta-skill" describing HOW to search (tool: search_skills/skill_view on demand); require capability-oriented structured queries (with negative signals) rather than raw task echo; hybrid lexical+semantic retrieval over multi-view metadata (name/description/triggers/keywords).
- Diagnose exposure failures in two axes: (a) recall of emergent needs (under-invocation → make the meta-skill's trigger conditions explicit and low-friction), (b) disruption from unnecessary loads (→ make no-exposure the default and retrieval strictly pull-based).
- Task-shape caveat: if the task's needed capability is not describable as a query (implicit tacit knowledge), managed access won't rescue retrieval — fix the retrieval index or the task decomposition instead.

## When to Use

- Designing or tuning skill/agent-instruction retrieval for repositories ≫ context budget.
- Diagnosing "agent got WORSE after we added more skills" — distinguish context pollution (progressive disclosure), capability misalignment (static retrieval), and disruption (unnecessary injection).
- Structuring meta-prompts for on-demand capability loading (query schema: capability + context + attributes + signals + constraints).
- Benchmarking skill systems: report skill-necessary vs skill-unnecessary instances separately; include a gold-exposure arm to detect disruption.
