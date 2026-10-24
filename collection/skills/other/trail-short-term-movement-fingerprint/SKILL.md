---
name: trail-short-term-movement-fingerprint
description: "Short-term movement as identity and learning fingerprint."
version: 1.0.0
author: "Zhang, Nguyen, Lei et al. (arXiv 2610.27140) via neuro-cron 2026-10-24"
license: MIT
category: ai_collection
metadata:
  hermes:
    tags: [behavioral-representation, self-supervised, movement-trajectories, animal-identity, learning-progress, contrastive-learning, pose-estimation, conditional-generation]
    arxiv_id: "2610.27140"
---

# TRAIL: Short-Term Movement as Identity + Learning Fingerprint

Methodology from "Representing short-term movement to reveal animal identity and learning progress" (Zhang, Nguyen, Lei, Shridhar, ... Chao; BU/OSU/UChicago, arXiv:2610.27140, cs.LG/q-bio.NC, 35 pp, code github.com/pizhn/TRAIL). Self-supervised representations learned from 1-3 second keypoint trajectories predict individual identity and learning progress WITHOUT predefined behavioral states or kinematic features — temporal proximity is the only supervision.

## When to Use

- Extracting behavioral fingerprints (identity, learning stage, proficiency) from short pose/movement clips of freely behaving animals
- Choosing a self-supervised objective for LONGITUDINAL behavioral data spanning days of learning
- Designing behavioral probes: deciding WHERE (maze regions), WHEN (days), and WHICH motifs carry identity vs learning signal before collecting more data
- Interpreting what a learned behavioral representation encodes, via representation-conditioned generation

## Core Hypothesis and Objective

Hypothesis: movements vary rapidly, but behavioral characteristics tied to IDENTITY and LEARNING are stable over NEARBY time intervals. Therefore use temporal proximity as supervision:
- Positives: trajectory segments from the SAME session within a window (default 10% of recording partition)
- Negatives: temporally distant segments of the same session, or segments from other sessions
- Balanced InfoNCE + auxiliary trajectory reconstruction (reconstruction matters: identity 81.1 -> 84.0 with it)

KEY REGULARITY: widening the positive window toward recording-wide hurts learning readouts in ALL animals — learning-related behavioral state is LOCAL in time. Identity is insensitive to window size.

## Pipeline (Wayformer-style encoder)

1. Input: X in R^{T x K x 2} keypoint trajectory (default T = 3 s x 11 Hz = 33 frames, K = nose/neck/body) + maze waypoints M (environment context)
2. Anchor: center body point and vertically align body-neck vector at the FINAL frame; apply the same rigid transform to all frames and maze coords
3. NeRF-style multi-frequency encoding (L=10 frequencies) of every 2D coordinate -> linear projection to 64 dims; learnable keypoint embedding (shared across frames) + temporal embedding (shared across keypoints); separate additive embedding for maze tokens
4. Q-Former encoder (4 layers, 8 learned queries) attends to (KT + N) tokens; q0 -> 16-dim latent h (8-dim also works)
5. Loss: contrastive on h + reconstruction from [projected q0; remaining tokens]

## Reference-Frame Dissociation (main scientific finding)

- Local Pose (egocentric: per-frame centered + heading-aligned posture dynamics) -> predicts IDENTITY (77.1)
- Global Trajectory (allocentric: body position + heading over time) -> predicts LEARNING readouts (Day MSE 1.47, Proficiency .017)
- Full Movement (both) -> best on everything (identity 84.0, Day 1.26, Proficiency .016): posture dynamics and spatial navigation carry COMPLEMENTARY information

## Where/When Signals Live

- Maze junction >> arms (identity 88.7 vs 81.7; proficiency .014 vs .021): signals concentrate at DECISION points
- Days 4-5 > Days 1-3 (proficiency .012-.013 vs .016-.019): signals sharpen with experience
- Turning motif is the strongest carrier (identity 98.0, proficiency .008); remaining still still informative (87.1); scanning weakest
- One-second trajectories are already competitive with 3 s — brief movements suffice, especially for identity

## Conditional Generation for Interpretation

Train diffusion generator G(u, h) conditioned on frozen-encoder representation h. Given observed trajectory x0 with representation h0: approximate DDIM inversion to get latent u0; FIX u0 and model, vary h along an interpretable direction:

    d = |(h_ref - h0)^T v| v   (v = leading PC of daily centers within an animal, or of animal centers on the same day)
    h(tau) = h0 + tau * d;  x_hat(tau) = G(u0, h(tau))

Fixing u0 preserves the broad motion structure (travel direction) while pace, turning rhythm (cross-day) or body-ratio extension = nose-neck / neck-body distance (cross-individual) morph toward the reference — making representation axes VISIBLE as movement changes.

## Benchmark Anchors (Y-maze spatial learning, 6 alternation + 8 probabilistic rats, 275 sessions, 44.9 h)

- Identity acc: TRAIL 84.0 > Supervised-all-targets 78.4 > TCN 65.4 > VAME 62.5 > Chronos-2-LoRA 46.8 > TimesFM-3-LoRA 44.4 > AR-HMM 44.1 — beats fine-tuned time-series foundation models and direct supervision
- Day MSE 1.26, Proficiency .016, Reward 0.61 all best; Success Rate ~tied (0.13)
- MABe22 Mouse Triplets: best Identity (73.65 at 2 s), frame-level F1 77.39 (2 s) / 79.08 (45 s); sequence tasks competitive
- Proficiency ground truth: Smith et al. (2004) state-space model per trial

## Pitfalls / Discipline

- Reconstruction loss is not optional: contrastive-only drops identity by ~3 points
- Local temporal windows for learning signals; recording-wide positives blur day/proficiency information
- Identity survives cross-session contrasting during training — the fingerprint is not an artifact of session idiosyncrasies, but DO check per-session probes when transferring
- Coarse readouts (success rate under alternation) may not separate methods — choose sensitive continuous readouts (proficiency, reward MSE) for representation comparisons
- 1 s clips: identity robust, learning readouts weaker — match clip length to the target

## Key References

- Shridhar et al. (2026) — Y-maze spatial learning dataset (alternation + probabilistic reward cohorts)
- CEBRA (Schneider et al. 2023) — temporal/auxiliary-guided contrastive alternative
- BAMS, hBehaveMAE — multi-timescale behavioral SSL baselines
- Smith et al. (2004) — state-space proficiency estimation from binary trial outcomes
