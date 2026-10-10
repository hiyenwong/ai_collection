---
name: mem-motivated-emotional-mind-consciousness
description: Use when modeling consciousness, secondary perception, or allostatic affect. MEM theory of motivated mind.
category: ai_collection
---

# MEM: Motivated Emotional Mind — Motivational Account of Consciousness

**Paper**: "MEM as an Extension of Recurrent Processing Theory: Toward a Motivational Account of Consciousness" (arXiv: 2610.04057, Galus & Starzyk, Oct 2026)

## Core Thesis

MEM extends Lamme's Recurrent Processing Theory (RPT) from "recurrence is necessary for conscious vision" to a full embodied architecture: recurrence generates phenomenality **only when it reconstructs receptor-grounded sensory/interoceptive maps** ("secondary perception"). Not every feedback loop is conscious — purely regulatory recurrence without dominant sensory reconstruction stays unconscious.

## Central Mechanisms

### 1. Secondary Perception (the consciousness criterion)
- **Direct perception**: receptor activation → FFS → higher-layer matching.
- **Secondary perception**: active higher-order representation feeds back to reactivate lower-level sensory/interoceptive maps, reconstructing configurations learned during earlier receptor-mediated perception.
- Phenomenal content = reconstruction of modality-specific, receptor-grounded maps + interoceptive co-activation. "A report can describe content, but its qualitative character arises from activating the same maps originally formed through receptor activity."
- Perception–imagery–hallucination **continuum** controlled by reconstruction weight λ (Eq. 14): dreams/hallucinations = top-down content dominates over bottom-up input.
- Operational (testable) condition: χ_SP(t)=1 iff W(t)≠∅ ∧ ‖ĥ_sens‖≥Θ_rec ∧ ‖h_int^act‖≥Θ_int — thresholds are empirical, not algebraic.

### 2. Semblions (representational unit)
- Semi-hierarchical (heterohierarchical) distributed coalitions spanning modalities: lower components tied to receptor configurations, higher to concepts/emotions/action programs.
- S_m = (μ_m, ρ_m, v_m): sensory prototype + bodily/motivational context + valence.
- **Compression via convergence** (many lower fields → abstract pattern) gives memory capacity, generalization, cross-modal association.
- Matching score (Eq. 6): u_m(t) = α_s·sim(h_sens^ff, μ_m) + β_b·sim(b(t), ρ_m) + ξ_v·v_m — recognition is NOT purely stimulus-driven; context and valence co-determine it.
- **TopK → candidates C(t), NOT winners.** Soft competition within C(t): lateral associative priming q_m (Eq. 9a) modulates raw scores, softmax with temperature τ_c (Eq. 9b), then dominance threshold Θ defines winner set W(t) = {m: a_m(t) > Θ} (Eq. 12). Multiple compatible semblions may co-dominate; WTA is only the sharp limit.

### 3. Reconstruction Equations (13–14)
- ĥ_sens(t) = Σ_{m∈W(t)} a_m(t)·μ_m (winners reconstruct their prototypes)
- h_sens^eff = (1−λ)·h_sens^ff + λ·ĥ_sens, 0≤λ≤1 — λ is the signal-integration parameter fittable to neural/behavioral data.

### 4. Allostasis & Affect (embodied valuation)
- Distinguish raw interoception y(t), regulated allostatic variables n(t), integrated context b(t).
- One-sided violations: Δn_r⁻ = max(0, n_r^min − n_r), Δn_r⁺ = max(0, n_r − n_r^max) (Eq. 2). Tolerance limits are time/context-dependent — no fixed equilibrium.
- Global affect A(t) = tanh(w_A^T·d(t) + c_A) — a bounded regulatory signal, not an emotion name. Modulates attentional gain, learning rate, memory consolidation, valence, exploration/exploitation.
- Cost C(t) = Σ[α_r·Δn_r⁻ + β_r·Δn_r⁺] ≥ 0 (Eq. 4).
- Emotions = perceptual reading of allostasis (James/Lange/Prinz lineage); feeling during recollection = partial reinstatement of receptor-grounded fear pattern, not the label "I was afraid".

### 5. Deliberation & Action
- Activations compete for effector access. Blocked/inhibited action → activation circulates through successive recurrent cycles: simulate modified representations → reconstruct associated feelings → predict consequences → re-compete. **Deliberation = dynamic simulation, not a homunculus decision.**
- FFS→direct action ≈ System 1; multi-cycle deliberation ≈ System 2 (but not identical — System 2 needs repeated iterations).
- Decision value Q(Π|s_t) = −cost; procedural gap K(t)=1 when no known program meets threshold θ_Q → triggers candidate generation; new program = argmin J over candidates (Eq. 29).
- Dynamic semblions: transformation T converts temporal intervals between events into spatial relations among traces; T⁻¹ converts back during replay — neural substrate for CONTAINER / SOURCE-PATH-GOAL / FORCE image schemas (Lakoff/Johnson) and hence metaphor/analogy/inference.

### 6. Layered Dynamics (Eq. 1 vs 1R)
- Full: h_i^(ℓ)(t+Δt) = f(A^ff + A^lat + A^fb + A^int + A^ctx + θ) — five streams: feedforward, lateral, feedback, raw interoception, integrated context.
- **RPT is the restricted case**: set A^int = A^ctx = 0 → Eq. (1R) recovers the FFS/recurrence core. MEM ⊃ RPT by partial inclusion, not identity.

## Discriminating Predictions (vs minimal RPT)

1. Selectively disrupting feedback to early sensory maps impairs vividness/modality-specific quality of imagery, memory, dreams **more than** rapid unconscious recognition.
2. Allostatic manipulation (controlling stimulus/reward) alters semblion dominance, valence, vividness of affective recollection, exploration strategy — systematic influence on competition & learning, not just correlation.
3. Nonlinear competition between external activation and top-down content: intense stimulation suppresses subtle imagery; sustained internal attention suppresses irrelevant stimulus access while FFS is preserved.
4. Multi-cycle deliberation involves alternating reconstructions of outcomes + bodily states; blocking motor response without blocking reconstruction prolongs simulation.
5. Local recurrence WITHOUT receptor-grounded reconstruction → MEM predicts NO phenomenality (contradicts RPT sufficiency); strong reconstruction without global availability → phenomenality without access.
6. Fusion parameter λ is empirically fittable — links theory to data.

## Epistemic Status (honest assessment from the paper)

| Level | Status |
|---|---|
| Well-established | hierarchical feedback connections, FFS, figure-ground modulation, plasticity, interoception, top-down reactivation, competition |
| Integrative hypotheses | semblions as representational unit, dynamic semblions T/T⁻¹ |
| Strong constitutive claims | secondary perception = phenomenality; emotions = receptor-mediated allostatic reading; sensory grounding as qualia condition |
| Risks | overly broad explanandum, post-hoc fitting risk, tautological "sensory complex" danger, phenomenality measurement problem |

## Reuse Patterns for AI/Agent Design

1. **Grounding qualia-like content**: for generative agents/world models, make "experience" = reactivation of modality-specific encoder maps (not abstract tokens) — maps trained on receptor-equivalent (sensor) input.
2. **Affect as bounded control signal**: use A(t)=tanh(Σ violations) as a single global scalar modulating learning rate, exploration, and representation valence — cheap homeostatic modulation for long-horizon agents.
3. **Candidate/winner separation**: TopK candidates ≠ winners; lateral priming + softmax + dominance threshold gives soft, multi-winner selection for associative memory retrieval.
4. **λ-continuum control**: a single interpolation weight between feedforward evidence and top-down reconstruction gives a perception→imagery→hallucination dial for generative models (cf. classifier guidance strength).
5. **Deliberation as recurrent simulation**: when action is inhibited, run repeated cycles of (reconstruct → feel → predict → compete) instead of one-shot policy evaluation.

## Related Skills
- [[abstraction-fallacy-ai-consciousness]] — physicalist framework boundaries
- [[canonical-functionalism-consciousness]] — mathematical functionalism refinement
- [[thoughtseeds-dual-process-meditation]] — dual-process phenomenology

**Activation**: consciousness theory, secondary perception, semblion, allostasis, interoception, recurrent processing, phenomenal consciousness, motivated mind, embodied cognition
