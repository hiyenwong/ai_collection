---
name: qcnn-small-data-generalization
description: Use when evaluating quantum CNN generalization in small-data regimes — encoding bottleneck analysis (amplitude vs angle), parameter-matched comparisons, mid-circuit measurement QCNN design.
category: ai_collection
trigger_words: [quantum convolutional neural network, QCNN, small-data regime, generalization, Caro bounds, amplitude encoding, angle encoding, encoding bottleneck, mid-circuit measurement, classical feed-forward, parameter efficiency, BreastMNIST, sample efficiency, quantum ML experiment]
arxiv: 2609.24666
---

# QCNN Generalization in the Small-Data Regime (Experimental Evidence)

**Source**: arXiv:2609.24666 (Anthony, Burov, Piro, Dal Peraro, Javerzac — EPFL; 2026-09-21), quant-ph.
Paper: https://arxiv.org/abs/2609.24666

## Core Idea

Experimental test of the claim behind QCNN sample efficiency: Caro et al. (2022)
generalization bounds say quantum model error scales with **trainable parameter count**,
not Hilbert-space dimension — placing QCNNs in a potentially sample-efficient regime for
medical imaging / clinical trials / rare diseases where data is the bottleneck.

The authors build a **hardware-compatible QCNN with mid-circuit measurement and classical
feed-forward** (MCM+FF: measure qubits mid-circuit, feed results forward as classical
conditioning — reduces circuit width at the cost of mid-circuit measurement support).

## Key Results

1. **10 training samples suffice** for strong test performance on a binary
   handwritten-digit task; generalization error decreases as training set grows.
2. At matched **45-parameter budget**, the QCNN learns where an equally small classical
   CNN stays at chance.
3. **Honest negative**: an *unconstrained* classical baseline (~25k params) remains
   strongest when data is plentiful. On BreastMNIST, the QCNN does **not** surpass it —
   but learns consistently above chance with **orders of magnitude fewer parameters**.
4. The **real bottleneck is data encoding, not optimization**:
   - **Amplitude encoding**: qubit-efficient (log₂N qubits) but circuit depth explodes
     with resolution (2×2 → 512×512 becomes extremely deep).
   - **Angle encoding**: stays shallow but becomes **qubit-prohibitive** (one qubit per
     feature/pixel).
   - The two encodings cross over; neither scales cleanly to realistic image data.

## Reusable Patterns

### Pattern 1 — Encoding-scaling transpile audit
- Transpile the same model across input resolutions (2×2 → 512×512) under both encodings;
  plot depth & qubit count vs resolution.
- Decision rule: pick encoding by which resource (width vs depth) your hardware has more
  of. This audit exposes the bottleneck before any training run.

### Pattern 2 — Parameter-matched vs unconstrained double baseline
- Always run BOTH: (a) parameter-matched classical model (tests inductive bias), and
  (b) unconstrained classical model (tests practical relevance).
- Report the honest triangle: quantum wins (a), loses (b), and characterize the crossover
  data size where (b) takes over.

### Pattern 3 — MCM+FF width-depth tradeoff
- Mid-circuit measurement + classical feed-forward shrinks effective circuit width during
  execution; requires hardware with MCM support (IBMQ etc.).
- Use for QCNN pooling layers: measure a qubit subset, classically condition remaining
  layers — mimics classical pooling without ancilla overhead.

### Pattern 4 — Minimum-viable-sample curve
- Train from n=10 samples upward; if test accuracy climbs smoothly with n, the model
  generalizes rather than memorizes. A model at chance for n<100 is NOT in the
  sample-efficient regime regardless of theory.

## Activation

Use when: designing QCNNs for medical imaging with scarce data; choosing amplitude vs
angle encoding for image inputs; validating "quantum sample efficiency" claims
experimentally; building hardware-executable QCNNs with mid-circuit measurement.

## Pitfalls

- Do not claim quantum advantage from parameter-matched comparisons alone — the
  unconstrained classical baseline is the practically relevant competitor.
- Amplitude encoding's qubit efficiency is deceptive: depth, not width, kills you.
- MCM+FF requires mid-circuit measurement hardware support; simulators hide this cost.
- BreastMNIST-scale tasks are still toy-scale for imaging; scaling constraints (encoding
  + hardware execution) dominate beyond this regime.
