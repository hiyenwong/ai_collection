---
name: gaussian-fisher-superadditivity
description: Use when measuring multiple Gaussian quantum modes jointly.
category: ai_collection
trigger_words: [quantum Fisher information, Gaussian measurement, Bell homodyne, heterodyne, superadditivity, quantum metrology, thermal sensing, collective readout]
---

# Gaussian Fisher Information Is Superadditive — Joint Readout of Independent Modes

**Source**: "Gaussian Fisher Information Is Superadditive" — Liu, Wang, Ma (arXiv:2610.02625, Oct 2026)

## Core Insight

Quantum Fisher information (QFI) **adds** over independent probes — for unrestricted measurements, one parameter is best estimated probe-by-probe. But **Gaussian measurements break this rule**: two independent modes are better measured **jointly**.

Mechanism: a linear (homodyne) detector sees only **half of phase space** (one quadrature). For two modes, the *choice of which half* becomes a resource:
- **Heterodyne**: splits one mode on a beam splitter, reads both quadratures, pays **1 unit vacuum noise** for the empty port.
- **Bell homodyne**: balanced beam splitter + two homodyne detectors — **fills the empty port with the second mode**, converting that vacuum noise into signal.

## Proven Bounds

| Setting | Result |
|---------|--------|
| Gain bound (any width-carried parameter) | < (√2−1)² = 17.157% |
| Thermal modes, same temperature | gain conjectured impossible — DISPROVEN: any frequency difference opens a temperature window |
| Peak thermal gain | 12.699% at frequency ratio 3.318 (Bell homodyne optimal there) |

Bell homodyne wins when the two modes **differ in quadrature width** and in **how the width responds to the parameter**.

## Implementation Recipe

1. When estimating a parameter encoded in mode widths (temperature, loss, squeezing) over ≥2 modes, do NOT default to per-mode homodyne + classical averaging.
2. Interleave the modes on a **50:50 beam splitter** (or equivalent microwave coupler), then homodyne both outputs.
3. Reconstruct the parameter from the joint quadrature pair; the Fisher information of the joint Gaussian measurement exceeds the sum of separate readouts.
4. Hardware already supports this: (a) two coupled resonators + two homodyne detectors; (b) a phase-preserving amplifier whose **idler band is fed by the same thermal source** (the idler port becomes the "second mode" — no extra hardware).

## Key Design Rules
- Requires **mode mismatch** (different quadrature widths / different parameter sensitivity) — identical modes give no gain.
- For thermal thermometry: pick frequency ratio near 3.318 for near-optimal gain.
- Gain is bounded at 17.157% — meaningful for precision-limited budgets (e.g., microwave thermometry, axion searches, dark-matter detectors), not a scaling shortcut.
- This is a **Gaussian-measurement-only** effect; unrestricted measurement still obeys additivity — do not over-generalize.

## Relation to Prior Skills
- Distinct from `qrc-task-resolved-fisher-spectroscopy` (QRC Fisher spectra) — this skill is about measurement architecture selection, not learning dynamics.
- Generalizes `optimal-shadow-estimation`-style metrology thinking: choose the measurement *partition*, not just the estimator.

## Activation

Use this skill when: designing readout for multi-mode Gaussian states (thermal, squeezed, displaced) in optical or microwave setups, when two homodyne detectors are available but modes are read separately, when estimating shared parameters (temperature, loss) across resonators, or when phase-preserving amplifier idler ports sit idle (can be fed with signal instead of vacuum).
