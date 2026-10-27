---
description: Use when an LLM agent must map a quantum phase diagram.
name: agentic-phase-diagram-mapping
category: ai_collection
version: 1.0
author: cs-cron-2026-10-27
license: MIT
metadata:
  hermes:
    tags: [autonomous-agent, quantum-many-body, phase-diagram, dmrg, exact-diagonalization, long-horizon-planning, persistent-plan, physics-critic, skills-library, reAct, context-compaction, finite-size-scaling]
    source: arXiv:2610.32001
    related_skills: [agentic-scientific-workflow, agentic-fusion-materials, eval-harness-retained-reasoning-compaction, multiagent-systemic-failure-taxonomy, automated-alignment-researchers]
---

# Agentic Phase-Diagram Mapping (QuantumMatterExplorer)

Methodology from arXiv:2610.32001 — "QuantumMatterExplorer: An Autonomous Agent for the Discovery of Quantum Many-Body Phases of Matter" (Nys, Jreissaty & Carrasquilla, ETH Zürich; quant-ph, 22 Oct 2026).

## One-Line Summary

A single LLM "deep agent" with a persistent written plan, a small expert-skills library, and a validation-gated 4-stage protocol (survey → refine → identify → scale) autonomously maps quantum phase diagrams from DMRG simulations cross-checked against exact diagonalization — reproducing known transitions and identifying Néel/Haldane/dimerized phases of an undocumented spin-1 chain within an 8-hour budget.

## When to Use / Activation

- Building an autonomous agent that drives expensive numerical simulators over multi-hour horizons (physics, chemistry, materials, any domain with an expert computational protocol).
- Deciding single deep agent vs. multi-agent state machine for scientific exploration.
- Structuring long-horizon agentic runs so constraints survive context compaction.
- Injecting niche-library expertise (ITensor/DMRG-style tools) into an LLM without fine-tuning.
- Designing validation gates that keep an agent from compounding an early unverified assumption.

## Architecture Decisions (with reasons)

1. **Single deep agent, not a wired state machine.** Multi-agent arrangements lose/distort information between agents, lose advantages at matched token budgets, and can cost ~10× a plain chain-of-thought baseline. Observed failure modes of partitioned orchestrators: over-looping, redundant file rewrites, re-exploring the same parameter region, decisions on partial information. One central reasoner holds the whole trajectory.
2. **Subagents = context offloading, not division of authority.** Three types: (a) general-purpose for bounded subtasks; (b) **data-analyst** that reads/summarizes large data files and runs post-processing so bulk data never enters the main context; (c) **physics-critic** — an independent skeptical reviewer in an isolated context (so it cannot be biased by the main agent's reasoning), combining LLM-as-judge with tool-based validation; called early to review the plan and again at the end of analysis phases.
3. **Persistent written plan (`plan.md`) that survives compaction.** Counters the two dominant long-horizon failure modes: loss of earlier constraints after context compression, and compounding of an early unverified assumption. A separate lab-notebook document tracks every simulation run; an internal to-do list strengthens plan adherence (re-presenting the plan during execution measurably improves adherence).
4. **Skills as training-free expert-knowledge injection.** A deliberately small skill library (below the size where skill selection degrades): (a) protocol guidance for each exploration stage, (b) compressed pitfall knowledge for niche libraries (ITensor/ITensorMPS/XDiag). Ablation: adding the `itensor-dmrg` skill sharply cuts Julia error rate and failed calls (Gemma 4 backend); note gpt-oss-120b still failed to build a working DMRG pipeline even with the skill — skills help but cannot rescue a backend without the coding capability.
5. **Loop discipline:** plan → execute → analyse → replan, with context forced below ~20% of the window via fixed-budget compaction (two compressions in the 8 h flagship run; 653 tool calls, 453 model calls).

## The 4-Stage Exploration Protocol (the transferable core)

- **Stage 0 — Validation gate (before any result is trusted):** reproduce a known limit of the Hamiltonian and cross-check the implementation against an independent method (exact diagonalization). Never let the agent interpret physics from an unvalidated Hamiltonian implementation.
- **Stage 1 — Survey:** coarse grid over the FULL parameter range at the smallest system size. Localizes candidate boundaries cheaply so expensive large-L compute is spent only in boundary windows, not uniformly.
- **Stage 2 — Refine:** denser sampling near candidate boundaries, larger L.
- **Stage 3 — Identify:** assign phases from order parameters, correlators, entanglement (e.g., structure-factor peak m²zz, bond-alternation proxy, mid-chain entanglement entropy S_mid; incommensurate correlations via the maximizing wavevector q*).
- **Stage 4 — Scale:** finite-size extrapolation of order parameters and boundary locations to L→∞. **Revisit a region** when a boundary shifts with L or a label disagrees with the extrapolation — the flow is result-dependent, not a fixed pipeline.

## Evaluation Discipline

- **Ground-truth ladder:** first validate on known-phase Hamiltonians (anisotropic XY chain: exact free-fermion h_c = 1; frustrated J1–J2 chain: Majumdar–Ghosh solvable point, numerically known BKT α_c ≈ 0.2411), THEN challenge with a phase diagram published only after the models' training cutoff (frustrated bilinear-biquadratic spin-1 J1–J2 chain with single-ion anisotropy D, published April 2026) so the agent cannot be reciting memorized results.
- BKT transitions are the hardest to localize — expect degraded accuracy there vs. sharp order-disorder transitions.
- **Honesty requirements:** the agent states uncertainties in its research note; assigns phases only to a subset of computed points; unresolved regions are reported as unresolved. Interpolated phase-region sketches are drawn by human authors from the agent's point assignments + boundary brackets, not silently claimed by the agent.

## Empirical Findings (for calibration)

- Backend-agnostic (needs only tool calling): **Qwen3.6-27B performed best** despite being small and open (strong coding + exploration); Gemma 4-31B workable with the DMRG skill; gpt-oss-120b failed DMRG pipeline construction.
- Input tokens ≫ output tokens; all backbones similar input budgets, Qwen3.6 most verbose.
- The agent anticipates the wall-clock budget (finished 7.7 h of an 8 h limit).
- On the undocumented spin-1 chain it found candidate Néel, Haldane and dimerized phases in broad agreement with the reference, detected incommensurate correlations (q* drifting from π toward 2π/3), and inferred frustration-dependent boundary geometry.

## Pitfalls

- **Symmetry-broken phases at finite N:** the true ground state is a symmetric superposition (cat state), so ⟨order parameter⟩ ≈ 0 — use ⟨M²⟩-type probes (structure-factor peaks, m²zz), and remember the "excitation gap" w₁−w₀ is the exponentially small ferromagnetic doublet splitting in the ordered phase, NOT the physical gap (a gap-minimum boundary locator is biased into the ordered phase by this doublet). Correct finite-size criticality locator: crossing of the size-scaled observable (m²·L^{2β/ν}).
- Open boundaries induce Friedel-like oscillations in local observables — flag as finite-size artifacts, don't over-interpret.
- Limit checks must carry the right correction order: E₀(h→∞) = −hN holds only up to 2nd-order corrections ~(N−1)J/h; a zero-tolerance gate on a large-h limit fails spuriously.
- State-machine multi-agent orchestration re-explores the same region and decides on partial information.
- LLM training data under-represents niche scientific libraries — without a skill, error rates on DMRG code are high and a run can burn its whole budget on failed coding attempts.
- Context compaction without a persistent external plan = silent constraint loss.

## Deliverables an Agent Should Produce

1. `plan.md` (human-readable, editable; critic-reviewed before execution)
2. Lab-notebook file of every simulation (parameters, L, outcome)
3. Data files + analysis scripts (reproducible)
4. Research note with phase assignments, boundary brackets (finite-size), stated uncertainties, and unresolved regions

## Connection Map
- Long-horizon harness design → eval-harness-retained-reasoning-compaction, execution-state-capsules-serving.
- Critic pattern → self-verification, hallucination-resistant-evals.
- Skills-as-knowledge-injection → skill-rag-indexer, socratic-swe-self-evolving-coding-agents.
- Same-question independent replication → privacy-preserving-external-research-pilot (Anthropic), agentic-evidence-seeking-clinical.
