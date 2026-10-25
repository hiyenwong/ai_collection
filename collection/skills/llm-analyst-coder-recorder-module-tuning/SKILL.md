---
name: llm-analyst-coder-recorder-module-tuning
description: Use when tuning fixed blocks of neural models via multi-agent LLM. Analyst-Coder-Recorder loop with experiment log.
category: ai_collection
---

# LLM Analyst-Coder-Recorder Module Tuning (arXiv 2610.13663)

**Paper**: "A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models" — Moloshnikov, Kunitsyn, Sboev, Skorokhodov, Rybka, Liu (Kurchatov Institute / MEPhI / MIPT / HIT), 9 Oct 2026.

## Core Idea

Specialized neural models (SNN decoders, PINN input/output transforms) are **two-level**: an expert picks the method class, then key components (encoder, decoder, loss terms, coordinate transforms) are hand-tuned. This framework automates component tuning **without redesigning the network**: the agent generates code only for one specified functional block, keeping the rest of the pipeline frozen.

## Framework Architecture (5 components)

1. **LLM Analyst** — reads task prompt + experiment log, proposes ONE hypothesis per iteration as a structured technical specification. Optionally assigns it to a method class from a researcher-defined taxonomy.
2. **LLM Coder** — translates the specification into Python under a fixed **software contract**: allowed dependencies, class names, call signatures, input/output shapes, trainable parameters.
3. **Sandboxed execution (Docker)** — inserts the generated module into the frozen pipeline; runs a short functional test first, then full evaluation. Runtime errors loop back to the Coder (≤10 attempts, then "With error" status, hypothesis discarded, budget NOT consumed).
4. **LLM Recorder** — summarizes spec + validated code + metric + fitted hyperparameters into a JSON log record.
5. **Experiment log** — external memory (table of JSON records). Failed records stay stored but are **filtered out of the Analyst's view**; only baseline + OK records are visible. Run budget counts only OK records (250 for SNN, 50 for PINN).

**Key design contrast vs MLE-Bench/AI-Scientist systems**: this is NOT full-script optimization or NAS over a discrete space. It is an *open but semantically narrow* search — the Analyst can propose arbitrary method ideas in natural language, but code must land inside the fixed software contract.

## Detailed Prompt Mode (the transferable trick)

Standard prompt = role + problem + metric + constraints + spec format + full log.
**Detailed prompt adds**:
- **Method-class taxonomy** (12 decoder classes for the SNN task) — classes are exploration areas, not fixed algorithms.
- **Structured Chain-of-Thought** procedure for coverage/failure analysis.
- **Coverage map** — dynamically generated from the log: per class → number of evaluated hypotheses, best metric, status ("not explored" / "limited data" / "explored"). Included in every next Analyst prompt, which prioritizes under-covered classes and revisits explored ones only with substantially different hypotheses.

The coverage map is the mechanism that lets *weak* LLMs search systematically instead of re-proposing similar variants.

## Verified Results

| Task | Baseline | Best agent | Gain |
|------|----------|------------|------|
| SNN CCN decoder, MNIST (acc) | 79.88% (argmax) | 92.83% | +13 pp |
| SNN CCN decoder, Digits (acc) | 90.83% | 96.67% | +6 pp |
| PINN GNLSE single soliton (Rel_h) | 5.51e-2 | 2.21e-5 | 2491× |
| PINN GNLSE soliton+Gaussian (Rel_i) | 1.28e-1 | 6.61e-4 | 325× (103–116× over 10 retrainings) |
| PINN Kuramoto–Sivashinsky (mass drift) | 9.31e-2 | 6.56e-3 | 14× |

**Model-dependent prompt effect (MNIST, 10 paired runs, Wilcoxon + Holm, all significant at α=0.05):**
- Claude Opus 4.6: simple 91.13% → detailed 92.15% (coverage map removal costs only 1.14 pp — strong models don't need it).
- Perplexity Sonar: simple = baseline 79.88% in ALL 10 runs → detailed 91.76% (0/10 → 10/10 crossing 90%). Detailed prompt closed the model gap entirely.
- Qwen3-30B-A3B: simple = baseline → detailed 85.88 ± 2.42% (best 89.16%, never crosses 90% — prompt helps but doesn't fully compensate).
- **Coverage-map ablation**: removing the map drops Sonar by 9.42 pp (all runs below threshold) and Qwen by 5.70 pp (back to baseline). For weak analysts the coverage map is THE key component.

**Cost analysis (250 evaluated decoders/run)**: Claude $97.99/run but reaches best decoder at k_min=2–43, so cost-to-best ≈ $0.37; Sonar $0.21; Qwen $5.85 (managed rate). Random catalog sampling (no CoT, no debugging) is 40–84× cheaper in tokens but caps at 89.93% vs agent 90.93–92.83%. Framework is preferable to catalog sampling only when the Analyst model is strong enough.

## What the Agents Actually Discovered (method patterns)

- **SNN decoder (CCN)**: class-conditional spike-rate statistics decoders — the winning direction was fitting richer readouts on frozen STDP-trained LIF activity, not touching the network.
- **PINN single soliton**: all three winning configs embedded the analytical soliton structure into F_I/F_O (normalized traveling-wave coordinate, amplitude/phase corrections) — with a known solution, the agent "hints" the representation.
- **PINN soliton+Gaussian (no closed form)**: winning config `SPM_XPM_CorrWidth_SplitScale_HighP` — self-phase/cross-phase modulation features with split scaling; improves BOTH residual (2.08e-5) and conservation error simultaneously. Only Claude configs improved both criteria; Sonar/Qwen improved one and worsened the other.
- **Kuramoto–Sivashinsky**: multiplicative-additive decomposition û = u(x,0)·e^(-αt(1+t)γ_m·N1 + t·W(x)·(γ1N2+γ2N3)) — embeds the exact initial condition at t=0, vanishes at boundaries via window W(x), supplies co-moving coordinate ξ=x−t, sech² pulse profile, and collision-phase marker sin(πt/6). The mass-drift winner only differs by bounding N1 with tanh — small change, order-of-magnitude better conserved quantity.

## Reusable Patterns

1. **Software contract as search-space definition**: express "what may vary" as an interface (deps, class name, signatures, shapes) — the LLM gets an open idea space, the sandbox gets a checkable contract.
2. **Filtered experiment log as external memory**: show the analyst only successful records; archive failures separately to avoid re-proposal loops.
3. **Coverage map over a method taxonomy** to force systematic exploration — the single highest-leverage addition for weaker models.
4. **Error budget decoupled from run budget**: failed code-gen attempts (≤10) don't consume experiment budget, so weak coders don't starve the search.
5. **Task transfer = replace 4 things**: prompt, software contract, editable block, metric. Agent roles and loop stay unchanged — validated across 5 tasks of completely different nature (spiking classification ↔ nonlinear PDE).
6. **Multidimensional metrics need explicit priority**: rank by primary (Res_bvp), report secondary (Rel_i / mass drift) as independent diagnostics — the two are NOT interchangeable (tanh-bound example).
7. **Paired-run statistics**: same trained SNN + same spike data for each prompt-variant pair, exact Wilcoxon on 10 matched pairs, Holm correction over 6 tests.

## Limitations (from the paper)

- Search restricted to the editable-block catalogue (no auxiliary networks, no paradigm changes).
- Flat chronological log, no hypothesis DAG → limited multi-step reasoning depth.
- Bounded iterations (250/50) → reported results are lower bounds.
- Single-seed for the most expensive PINN configs.
- No head-to-head vs LLM-based NAS baselines.

## References

- arXiv: 2610.13663 (cs.AI, cs.CL, cs.LG, cs.MA, cs.NE)
- Related: MLE-STAR (closest agent system: logged memory + sandbox), LangPINN (builds PINN from text, not block tuning), Voyager (skill library ≈ logged hypotheses), AI-Scientist / Agent Laboratory (full-cycle systems without domain knowledge).
- Energy model constants used in companion paper: E_MAC = 4.6 pJ, E_AC = 0.9 pJ (Horowitz ISSCC 2014).
