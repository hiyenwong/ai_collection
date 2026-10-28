---
name: oneshot-entanglement-petz-hypothesis-testing
description: "Use when bounding one-shot entanglement generation rates."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [quantum-information-theory, one-shot-coding, entanglement-generation, entanglement-distillation, petz-recovery, binary-hypothesis-testing, cheng-trace-inequality, hypothesis-testing-coherent-information, finite-blocklength, second-order-asymptotics, random-coding]
    related_skills: [entanglement-distillation-protocols, quantum-communication-capacity, private-capacity-superactivation]
trigger: one-shot entanglement bound, entanglement generation over noisy channel, one-way entanglement distillation, Petz decoder error analysis, binary hypothesis testing cost, Cheng trace inequality, hypothesis-testing coherent information, finite blocklength quantum communication, second-order Gaussian correction, random subspace second moment, code conversion generation to transmission, rank-deficient states, commuting hypotheses constant remainder
---

# One-Shot Entanglement via Petz Recovery and Binary Hypothesis Testing

**Source**: "One-shot entanglement generation and distillation via Petz recovery and binary hypothesis testing" — Matthew Can, Mark M. Wilde (Cornell), arXiv:2610.31501 (quant-ph, cs.IT, 22 Oct 2026). Relates how much entanglement two distant labs can share over a noisy channel to deciding which of two quantum hypotheses is present.

## When to Use

Use when deriving **finite-blocklength (one-shot) achievable rates** for entanglement generation, entanglement transmission, or one-way entanglement distillation; when you need an **explicit Petz-recovery decoder** with an error bound in terms of a binary testing cost; when analyzing random-code performance via Haar moments; when converting results between coding tasks at fixed error; when computing second-order asymptotics from a hypothesis-testing quantity.

## The Three Tasks (keep them distinct)

- **Entanglement generation**: Alice prepares a joint state ζ, keeps one system, sends the other through channel N; no prescribed input. Weakest resource assumptions, most flexible.
- **Entanglement transmission**: one share of a *prescribed* maximally entangled input Φ_m is encoded; reference share untouched.
- **One-way entanglement distillation**: an imperfect state ρ_AB is already shared; Alice's LOCC message selects Bob's decoder D_j.

All target Φ_m^{Lb} (m-dimensional maximally entangled, log₂ m ebits) under infidelity ≤ ε. At finite blocklength the distinctions matter; at n→∞ all coincide with coherent-information rates.

## The Testing Cost and the Main Bound

For PSD operators define the unnormalized binary testing cost:

e(X,Y) := min over effects 0 ≤ T ≤ I of Tr[(I−T)X] + Tr[TY]

(posterior-weighted Bayesian error after normalization; Y may be a sum of competing codeword states — its trace counts the competition size). Let d = dim A ≥ 2, m ∈ {2,…,d} the integer target dimension, ρ_B = Tr_A ρ_AB, and the **explicit alternative**:

B_{d,m} = (dm−1)/(d²−1) · (d I_A ⊗ ρ_B − ρ_AB)   (PSD, trace dm−1)

**Main theorem**: a one-way (m, ε) entanglement distillation protocol exists whenever

e_{d,m} · (1 − e_{d,m}/(dm)) ≤ ε,   where e_{d,m} = e(ρ_AB, B_{d,m})

Smaller testing cost ⇒ smaller achievable infidelity; the (1−e/(dm)) factor is a free improvement, and ε ≥ e_{d,m} alone already suffices. Coding guarantee reduces to distinguishing ρ_AB from ONE explicitly specified alternative — no optimization over codes appears in the final statement.

## Proof Architecture (the transferable part)

1. **Cheng's trace inequality**: bounds the infidelity of the **Petz decoder** (the coherent, superposition-preserving decoder from QEC) in terms of the binary testing cost e(X,Y). Separates the analysis test (free choice) from the physical decoding measurement.
2. **Apply the inequality BEFORE averaging over codes**: the inverse output-state operator in the Petz decoder changes with the selected code — averaging first breaks the analysis. Ordering the inequality before the random-coding average reduces the error analysis to computing a **single second moment of random subspaces** (one Haar moment), which evaluates in closed form — the B_{d,m} above IS that averaged alternative.
3. **Rank-deficient states treated explicitly**: no full-rank hand-waving; the proof covers every integer target dimension m.
4. **Remove inter-subspace coherence** via block structure (orthogonal blocks / cyclic windows) so the moment computation closes.

## Consequences

- **Hypothesis-testing coherent information**: achievable entanglement = testing-based coherent information with a **single logarithmic error slack and exact integer rounding** (no loose sandwiching).
- **Code conversion (generation → transmission)**: error-preserving; target dimension drops only by a CONSTANT factor at fixed error; decoder = original decoder + local processing. So arbitrary pure reference-input states give the same coherent-information rate and **second-order Gaussian correction at the original error tolerance** for both tasks.
- **Commuting testing hypotheses**: the logarithmic remainder improves to a constant.

## Method Template (for other one-shot coding problems)

1. Write the task's error criterion as fidelity to a target state.
2. Choose an explicit decoder family (Petz recovery for coherent tasks; pretty-good measurement for classical).
3. Bound decoder error via a binary testing cost (Cheng-type trace inequality).
4. Random-code: apply the inequality before averaging; compute the surviving moment (usually second) of the random code space in closed form → the explicit alternative operator.
5. Read off achievable rate: hypothesis-testing entropy + log slack + integer rounding.
6. Second-order: estimate the testing quantity for i.i.d. resources → Gaussian correction σ√n instead of AEP/de Finetti penalties.

## Pitfalls

- Averaging the Petz decoder's state-inverse over codes before bounding breaks the argument — bound first, average second.
- Do not assume normalized states: sub-normalized/rank-deficient cases carry the actual content of the finite-blocklength claim.
- One-shot bounds for classical capacity use hypothesis-testing relative entropy; the *coherent* tasks need the testing cost of ρ_AB against the m-scaled alternative — direct transplants lose the log-term tightness.
- The (m,ε) convention (integer dimension, infidelity criterion) is what makes the rounding exact — re-derive if your task uses trace distance or rate language.

## References

- arXiv:2610.31501 — Can & Wilde (this skill's source)
- Cheng — trace inequality for pretty-good measurement error via binary tests
- Beigi, Datta, Leditzky — Petz decoding + random code spaces for quantum communication
- Blahut — reliability/distinguishability program in classical IT; Tomamichel — second-order asymptotics
