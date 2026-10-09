---
name: design-time-conformance-pulse-quantum-control
description: Use when checking pulse programs against device limits pre-run. Evidence-cited descriptor + exact arithmetic checker.
category: ai_collection
---

# Design-Time Conformance Checking for Pulse-Level Quantum Control

**Paper**: arXiv:2610.10427 — Rylan Malarchick (Embry-Riddle Aeronautical University, 2026)
**Artifact**: https://github.com/rylanmalarchick/qconform (Apache-2.0, C99, 4488 lines, zero deps)

## Problem
Pulse-level quantum control toolchains (QICK, Qblox, QubiC, Qibolab) accept programs that exceed hardware limits and **silently mutate them**: aliased frequencies folded ~860 MHz away, gains past full scale wrapped in registers, envelopes truncated at board load, amplitudes rounded to zero making play instructions disappear. The experiment runs, produces data, and **nothing in the data says the program was altered**. Vendor limits live in prose documentation that drifts from the toolchain enforcing them.

## Core Methodology: Treat Device Limits as a Machine-Checkable Contract

### 1. Evidence-Cited Capability Descriptor (anti-drift)
- Device limits live in a **versioned, machine-readable JSON descriptor** pinned to (firmware config, library version)
- **Every constraint carries an `evidence` list pointing into a black-box probing survey catalog** — a gate script refuses descriptors whose citations do not resolve
- Evidence entries name the probe axis, outcome (accept/reject), and a note fragment to match survey rows
- Accept/reject behavior is a function of the (firmware, library) pair — pin both

```json
{"id": "frequency_range", "shape": "range_resolution", "severity": "fatal",
 "post_mixer": true,
 "min": {"num": -860160000, "den": 1},
 "max": {"num": 28185722866875, "den": 32768},
 "evidence": [{"axis": "freq", "outcome": "reject", "note_contains": "just under lower edge"}]}
```

### 2. Exact Arithmetic — No Floating Point
- Durations are **integer counts of a rational time base** (chosen so both the generator fabric clock 599.04 MHz and the timing clock 430.08 MHz are whole multiples)
- Frequencies, phases, amplitudes are **exact rationals** (`{"num": ..., "den": ...}`)
- Why: vendor toolchains subtract mixers in double precision — a request at exactly the upper band edge becomes 860.1600000000001 MHz and is refused. An exact grid test is immune to this artifact.
- **Dual time-base**: one channel can have TWO grids (fabric clock vs processor tick) — a single grid field misstates the device

### 3. Verdicts: Pass / Fail / Pass-with-Repairs / Tool-Error
- **A repair is a verdict of its own** — each rejection is `fatal` or `vendor-repairable`; a repairable rejection names what the toolchain will silently change (amplitude clamp at 32767/32768, half-to-even readout rounding, frequency folding to Nyquist image)
- The user sees the silent mutation **before** the program runs

### 4. Coverage Manifest (anti-vacuous-pass)
- Every report classifies **all 26 coverage classes** as `checked | not-applicable | unchecked | indeterminate`
- A channel that a descriptor declares but does not constrain reports `unchecked` — separates a vacuous pass from a verified one
- "A pass states its own scope"

### 5. Version-Pinned Soundness Claim
- The checker makes ONE claim: *if it returns pass or pass-with-repairs, the **pinned** vendor toolchain compiles the program*
- Verdicts do NOT transfer across toolchain releases — the oldest QICK release gives **90 unsound passes** against the pinned descriptor; Qblox older releases give 10/10/8
- Deliberately conservative: refuses programs the toolchain accepts but hardware cannot honor (aliased freq, overfull-scale gain, oversized envelopes), and unused frequency/phase updates

## Differential Testing Evaluation

### Black-box probing survey (build the descriptor)
- Drive the toolchain **with no hardware present** (QICK against captured board configs; Qblox dummy cluster) — 605 QICK probes + 193 Qblox probes, 4 outcomes per probe: accept-unchanged / accept-mutated / refuse-typed / fail-unnamed
- Each probe varies one parameter around a limit the configuration implies → catalog records where each limit sits and on which side the toolchain refuses, repairs, or stays silent

### Corpus design
- **Boundary ladders**: each declared limit at far-below / just-below / exactly-at / just-above / far-above
- **Budget ladders**: exactly the limit + one element past (program-memory cost model: 4097/4096 words)
- **Spacing ladders**: two operations one unit either side of minimum spacing
- **Resolution rungs**: odd multiple of the step (on declared lattice, off 2× coarser lattice)
- **Randomized programs**: compose elements near limits; only seed-dependent part; verify across 10 seeds

### 9-way triage dispositions (only one counts against soundness)
`agree | unsound (checker accepts, vendor refuses — THE claim) | missed-repair | over-predicted | vendor-lenient | conservative | unobserved | harness | open`
- **Harness self-attribution**: vendor interfaces take doubles; every conversion records request/passed/same-grid-cell — rows where the value didn't survive the double are attributed to the harness, excluded from soundness count
- Channel-class reduction: two channels in one class only when every descriptor value is identical (27 channels → 8 classes)

**Result: 1263 runs / 969 programs / 4 configurations / 0 unsound passes.**

## Defect Patterns Found (highly reusable)

1. **"Parsed but never enforced"** (recurred 3×): descriptor field read by the parser but never consulted by the checker logic (post_mixer flag, mux tone count, instruction cost model)
   → **Fix: build-time tripwire requiring the checker to read EVERY descriptor field the parser fills** — on first run it found 3 more latent instances
2. **Evidence gate that resolves citations but never asks the model to predict them**: the Qblox instruction cost model cited rows showing 2 instructions/output while charging 1
   → **Fix: gate requires each cost model to predict the accept/refuse outcome of every row its evidence cites**
3. **Harness artifacts masquerading as unsound passes**: lowering defining a new pulse per play (exhausts waveform table), non-deterministic corpus seed from unsalted string hash (120/286 programs differed between runs)
4. **Fault injection**: 742 single-change defects planted in descriptors/checker; 6 survived for lack of a test program on a probed channel — coverage metric: a class counts as covered only when it has BOTH a firing program and a checked-and-holds program

## Reusable Design Principles (beyond quantum)

1. **Prose contracts drift; evidence-cited machine contracts don't** — applicable to any hardware/software interface where limits are documented informally (robotics drivers, FPGA toolchains, GPU kernels)
2. **Exact arithmetic for grid/range checks** — whenever a vendor interface takes doubles, decide on rationals and convert at the boundary, recording conversion fidelity
3. **Make silent mutations first-class verdicts** — any system that "accepts and repairs" (compilers, serializers, quantizers) should surface the repair before execution
4. **A pass must state its own scope** — coverage manifest with checked/unchecked distinction prevents vacuous assurance
5. **Pin the oracle version** — soundness claims are relative to a (toolchain, library) pair; re-verify on version change
6. **Differential corpus = ladders (boundary/budget/spacing/resolution) + randomized composition** — systematic limit-walking beats pure fuzzing for interface conformance
7. **Tripwire unused-field detection** — static guarantee that every parsed contract field is consulted by the decision procedure

## Key Numbers
| Item | Value |
|------|-------|
| Checker | 4488 lines C99, zero dependencies |
| Survey | 605 (QICK) + 193 (Qblox) probes |
| Corpus | 1263 runs, 969 programs, 4 configs, 10 seeds |
| Unsound passes | 0 (pinned) / up to 90 (oldest release) |
| Coverage classes | 26 total, 23 exercised |
| Defects found | 10 checker/descriptor + 18 harness + 5 evidence |
| Compile time | ~1.9 ms (QICK) / ~11 ms (Qblox) |

## Related Skills
- [[pulse-level-quantum-computing]] — pulse-level design/optimization (this skill checks realizability)
- [[validation-driven-llm-workflow]] — verification-first workflow pattern
- [[automated-cps-testing-act]] — ACT differential testing for CPS
- [[safety-liveness-control-contracts]] — contract-based layered control

## Sources
- arXiv:2610.10427 (quant-ph, cs.SE cross-list)
- Companion: control-plane openness rubric applied to 13 vendor stacks
- Related: QDiff (quantum software differential testing), MorphQ (Qiskit metamorphic), OpenPulse backend specs, QDMI device interface
