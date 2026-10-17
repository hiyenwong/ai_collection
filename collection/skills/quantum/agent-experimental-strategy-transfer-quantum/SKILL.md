---
name: agent-experimental-strategy-transfer-quantum
description: "Transfer agent-run quantum experiments across processors."
category: ai_collection
---

# Agent-Assisted Experimental Strategy Transfer Across Quantum Processors

Methodology from arXiv:2610.21047 (Hou, Wu, Zhang, Feng, Li, Xiang, 2026): an LLM agent (Codex/GPT-5) develops an experimental strategy under supervision on one 3-qubit NMR processor (Q0), then sequentially deploys and refines it on four others (Q1→Q2→Q4→Q3), each time rebuilding the local model and realizing the same 3-qubit Grover task (marked-state population ideal 121/128 ≈ 0.945; achieved 0.910–0.959, deviations <3.8%). Use when designing agent-driven experiment automation that must survive device change/drift, when porting calibration/control workflows across quantum hardware, or when defining what an agent may/may not carry between devices.

## T2T / T2E Split

- **T2T (target-to-task)**: scientific target → hardware-independent task package (target state/observable, logical circuit, evaluation criterion). Context only in this paper (LM systems already address code/blueprint generation).
- **T2E (task-to-experiment)**: realize the task package on physical hardware — the evaluated contribution. Agent invokes deterministic tools, assesses evidence, selects next actions; operators keep instrument prep, physical intervention, safety, authorization.

## Separation Principle

Transferable: model CLASS (three-spin), generic procedures, quality criteria, acquisition budgets, stopping rules, deterministic tools, decision policy.
Excluded from transfer: device-specific numbers, spectra, response matrices, reference shapes, waveforms from the source device. Q0's parameters must be re-derived locally on every new device.

## Decision Cycle (recorded policy)

Each step: assess observations & data quality → identify missing information → select an allowed action → evaluate resulting evidence → continue / request intervention / stop. Mandatory records: observations, candidate actions, selected action + rationale, tool outputs, hardware results, updated assessment, acquisition cost, operator involvement.

Allowed action set: hard-pulse X/Y-phase spectroscopy, selective reference measurements, relaxation measurements, tomography, GRAPE pulse optimization, repeated acquisition.

## Transfer Incidents → Adaptation Patterns

| Device | Incident | Agent response |
|---|---|---|
| Q1 | legacy fitter used Q0 settings (violated the no-parameter-transfer rule) | REJECTED the fit; refit X and Y spectra separately after operator readjustment |
| Q2 | reference checks alternated pass/fail | required TWO CONSECUTIVE passing readiness checks + updated references before pulse compilation |
| Q4 | overlapping inner transitions — original 3-resolved-quartets fitter unsuitable | adapted line-assignment (infer couplings from 2 resolved quartets + outer lines of third multiplet as constraints); 0/9 X/Y pairs passed initially → STOPPED acquisition, requested operator adjustment |
| Q3 | same overlapping pattern | REUSED the adapted method; combined 5 qualified X/Y pairs |
| Q3-R1 | server interruption | resumed, retained historical FAIL verdict, proposed separate Q3-R2 (operator-authorized) |

Key: adaptations made on one device (Q4's fitter) became part of the transferable strategy for the next (Q3) — refinement accumulates through deployment sequence P0→P1→P2→P3.

## Evidence-Based Stopping Rules

- Spectral fit quality gates (line assignments must resolve; if not, adapt method, don't force through)
- Two-consecutive-pass readiness checks for unstable references
- Validation gate: complete tomography repeats before declaring success
- Independent cross-checks (e.g., separate X and Y fits → parameter consistency <2 Hz)
- Keep FAIL verdicts; never overwrite historical results; run auxiliary sessions instead

## Pipeline Per Device

1. Local Hamiltonian estimation: fit resonance lines from x/y-phase excitation spectra (4 lines/spin; Q0 RMS error 1.186 Hz)
2. Response-matrix construction: 8 basis inputs → 8×8 empirical preparation/measurement matrix; correct reconstructed populations by constrained inversion (nonnegativity + unit sum)
3. Task pulse: GRAPE-optimize 11-ms / 440-segment pulse against local model, robustified over detuning (−40..40 Hz in 20-Hz steps) × RF-amplitude scale (0.95/1.0/1.05) ensemble
4. Execute + tomography → response-corrected populations; evaluate against task criterion

## Results
- Q1/Q2/Q4/Q3 dominant-eigenstate marked populations: 0.929 / 0.959 / 0.936 / 0.910; TV distance from ideal 0.020–0.047
- Robustness ensemble minimum simulated populations 0.887–0.934
- Repeat sessions: 15 complete tomography repeats across 5 sessions (Q2-R1, Q4-R1/R2/R3, Q3-R1/R2); repeatability varied (Q4-R2 range 0.894–0.940 judged unsatisfactory vs Q2-R1 0.960–0.970 satisfactory) — honest reporting of variation

## Related Work Positioning
- vs fixed-rule feedback controllers: agent adapts the PROCEDURE, not just control variables
- vs Vibe Calibration (single-qubit characterization at scale, chip-transfer fine-tune test): this work transfers the STRATEGY for a multiqubit task with local model+control rebuild
- vs autonomous-lab closed loops: agent coordinates at decision level above deterministic tools

## Reuse Checklist

1. Define task package (T2T) separately from any device realization
2. Whitelist transferable context (model class, procedures, criteria, tools); blacklist device numbers
3. Enforce local re-derivation; reject fits that inherit foreign parameters
4. Record every decision + rationale + cost; keep historical verdicts immutable
5. Gate acquisition on readiness checks (two consecutive passes when unstable)
6. Adapt methods to observed spectral structure; carry adaptations forward as strategy upgrades
7. Robustify control pulses over detuning × amplitude ensembles before deployment
8. Operators authorize revisions, reruns, and physical interventions — agent never assumes that role

## Related
- [[vibe-calibration-autonomous-quantum]] — skill distillation for calibration portability
- [[llm-guided-quantum-code-discovery]] — LLM-driven quantum automation
