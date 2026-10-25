---
name: fvqkd-rocq-qkd-formal-verification
description: "Use when verifying QKD security proofs in Rocq (BB84)."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [quantum-key-distribution, formal-verification, rocq, coq, BB84, composable-security, finite-key-analysis, smooth-entropy, entropic-uncertainty, leftover-hash-lemma, serfling-bound, proof-engineering, quantum-cryptography]
    related_skills: [post-quantum-crypto-analysis, quantum-protocol-designer, verified-commissioning]
trigger: QKD formal verification, machine-checked security proof, BB84 security, composable security, finite-key key length formula, smooth min-entropy, entropic uncertainty relation, quantum leftover hash lemma, Serfling sampling, purified distance smoothing, Rocq Coq proof assistant, admit-free proof, missing proof branch, convention reconciliation, two-factor assurance
---

# FVQKD: Formal Verification of QKD Security Proofs in Rocq

**Source**: "FVQKD: A Formal Verification of Quantum Key Distribution Security in Rocq" — Ruixuan Deng, Zhengfeng Ji, Jiayu Zhang (Tsinghua/Zhongguancun Lab), Li Zhou (CAS Software Institute), arXiv:2610.30645 (quant-ph, cs.CR, cs.LO, 22 Oct 2026). First end-to-end machine-checked composable finite-key security proof for BB84.

## When to Use

Use when **verifying or mechanizing a QKD/quantum-cryptography security proof**; when a pen-and-paper information-theoretic argument needs kernel-checked guarantees; when auditing security proofs for hidden side conditions, missing proof branches, or convention mismatches; when building reusable proof infrastructure for quantum information theory (smooth entropies, EUR, QLHL, SDP duality); when formally modeling quantum protocols with explicit execution semantics.

## The Two-Factor Assurance Idea

QKD security already comes from physics (information-theoretic, against unbounded quantum adversaries). Formal verification adds the second factor: **machine-checked proofs against reasoning errors**. Important QIT results have contained serious gaps years after publication; decoy-state BB84 surveys found gaps in published proofs. The mathematical chain (smooth entropy → EUR → QLHL → sampling) is too delicate for hand-checking alone at the rigor level standardization demands.

## The Security Chain (what gets mechanized)

1. **Entropic Uncertainty Relation (EUR)**: H^ε_min(X|E) + H^ε_max(Z|B) ≥ n·q, where q = −log₂ max_{x,z}|⟨ψ_x|ψ_z⟩|² is preparation quality (q=1 ideal BB84). POVM-general form.
2. **Serfling sampling bound**: H^ε_max(Z|Z′) ≤ n·h(Q_tol + μ), with μ = √((n+k)(k+1)/(nk²))·ln(2/ε_s) the finite-sample correction (the ONLY finite-size loss ~1/√k), h = truncated binary entropy (clamp h(x)=1 for x>1/2 so more errors never yield more key).
3. **Data processing**: H^ε_max(Z|B) ≤ H^ε_max(Z|Z′).
4. **Quantum Leftover Hash Lemma**: converts the H^ε_min lower bound into secrecy of the hashed key.
5. **Chain rule**: charges leak_EC bits + ⌈log₂(1/ε_c)⌉ verification bits.

**Key-length bound**: ℓ ≤ n[q − h(Q_tol+μ)] − leak_EC − log₂(2/(ε_s²ε_c)), with ε_c-correctness (verification hash collision) and ε_s-secrecy. Protocol Φ(n,k,ℓ,Q_tol,ε_c,leak_EC).

## The Missing Proof Branch (the audit catch)

Smooth entropies H^ε_min/H^ε_max are defined by optimizing over states within purified distance ε of ρ — **well-defined only for ε < √Tr ρ** (ε < 1 for normalized states). The BB84 proof applies EUR **after conditioning on parameter-estimation pass**, which renormalizes the state and rescales the smoothing parameter to ε′ = ε/√p_pass. The published analysis stated "ε′ ≥ 0" without the upper bound. An **active adversary forcing frequent aborts** can push p_pass ≤ 10⁻¹², making ε′ = ε/√p_pass ≫ 1 — the EUR invoked outside its domain.

**Resolution pattern**: introduce an explicit domain predicate; split the secrecy proof into two branches: (a) EUR-domain satisfied → normal chain; (b) high abort probability → the (1−p_abort) prefactor already trivially bounds secrecy. Security is not compromised, but the theorem was invoked in a regime where its hypotheses fail. Formalization catches this because **every side condition must be discharged before the kernel accepts the proof**.

## Convention Reconciliation (the integration tax)

The BB84 chain imports theorems from six treatments with incompatible definitional choices:
- **Smoothing-ball metric**: 5/6 use purified distance; Renner uses trace-distance balls on sub-normalized operators. The exact duality H^ε_max(A|B) = −H^ε_min(A|C) (ρ_ABC pure) **requires** purified-distance balls (purification lifting) — Eve's uncertainty ↔ Bob's error rate link breaks otherwise.
- **Witness domain**: conditional min-entropy is sensitive to whether the SDP witness σ_B is normalized or sub-normalized. Value is the same (optimum attained at normalized witness) but a lemma proved for one domain does not directly apply to the other.

**Pattern**: fix one definition per concept; bridge differences with coercion lemmas at theorem boundaries; never silently mix conventions.

## Reusable Infrastructure (protocol-agnostic core)

Uhlmann fidelity theorem, generalized (sub-normalized) fidelity, purified distance as metric monotone under CPTN maps, smooth conditional min/max-entropy calculus (duality + classical chain rules), POVM-general EUR, Quantum LHL, Serfling bound, **SDP strong duality proved from first principles** (primal direction of Tomamichel Thm 2.6). New protocols (decoy-state, MDI, entanglement-based) on the same smooth-entropy route reuse the core and add a new top layer. Admit-free; TCB = Rocq kernel + 3 MATHCOMP-ANALYSIS axioms; built on MATHCOMP, MATHCOMP-ANALYSIS, COQQ.

## Protocol Model Layer

A small quantum programming language (quantum/classical variable sets, registers) with formal semantics connects the entropy proof to executable protocol structure; the final theorem quantifies over every initial state and transcript-dependent adversary channel. Explicit **source and measurement obligations** expose device-model parameters (q, Q_tol) as theorem parameters — device-level attacks (detector blinding, PNS, Trojan-horse) are out of scope until a device model discharges them.

## Lessons for Proof Engineering

- Mechanization is a **proof audit tool**, not just verification: it found a missing branch and unstated side conditions in a decade-old standard analysis that later finite-key proofs build on.
- Conditioning events rescale smoothing parameters (ε → ε/√p_pass) — always re-check domain constraints after every conditioning step.
- Literature theorem-chains are convention minefields: one fixed definition + coercion lemmas beats per-paper reinterpretation.
- Ground information-theoretic bounds in formal execution semantics, or the proof certifies a state the protocol never produces.

## Scope and Extensions

Out of scope: device vulnerabilities, implementation side channels, entropy accumulation (needs Rényi chain-rule library), numerical security frameworks (needs verified convex optimization — FVQKD's SDP duality is a core ingredient), continuous-variable QKD (infinite-dimensional Hilbert spaces).

## References

- arXiv:2610.30645 — FVQKD (this skill's source; development built on Rocq/MATHCOMP/MATHCOMP-ANALYSIS/COQQ)
- Tomamichel, Lim, Gisin, Renner — tight finite-key BB84 analysis (the formalized bound)
- Renner — smooth-entropy framework; Tomamichel — quantum information theory monograph (convention consolidation)
- Shor–Preskill — QKD-via-QEC reduction lineage
