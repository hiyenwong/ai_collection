---
name: s2-sensorimotor-alignment
description: "Use when ranking VLA/robot models without closed-loop eval."
category: ai_collection
version: 1.0
author: neuro-cron-2026-10-26
license: MIT
metadata:
  hermes:
    tags: [platonic-representation-hypothesis, embodied-ai, model-selection, offline-proxy, nearest-neighbor-overlap, dtw, vla, world-action-models, representation-alignment]
    related_skills: [platonic-representations-brain, vlm-lam-brain-alignment, mllm-tom-valence-brain-alignment, eeg-based-lm-evaluation]
  arxiv_id: "2610.31670"
  paper_title: "Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success"
  paper_authors: "Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei"
  published: "2026-10-22"
---

# S²: Sensorimotor Alignment as an Offline Capability Proxy

A **training-free offline metric** — mutual k-NN overlap between a model's sensory embeddings and recorded **end-effector trajectories** — predicts downstream robot task success across VLAs, raw VLM backbones, world action models, and real-robot policies, while VQA and video-quality metrics do not. Extends the Platonic Representation Hypothesis (PRH) to a new modality pair: **action is another projection of reality**. arXiv 2610.31670 (Rice / NVIDIA).

## When to Use

Use when: choosing between robot/embodied/VLA/WAM checkpoints and closed-loop rollouts are too expensive to run for all candidates; **screening VLM backbones BEFORE fine-tuning into VLAs**; diagnosing WHY an embodied model succeeds/fails at the representation level (modality dominance, frozen encoders, denoising steps, layer choice); you need a cheap capability proxy for policies trained by behavior cloning or visual-reward learning; auditing whether a passive-perception benchmark actually predicts action performance.

## Problem

Closed-loop rollout is the only trusted evaluation of robot policies but is slow, noisy, and benchmark-dependent. Existing offline proxies (VQA scores, FID/SSIM/PSNR video quality) measure passive perception or pixel plausibility — two scenes may look alike yet demand different motions. None of them reference the motor structure the policy must produce.

## Core Method

### 1. Two representations per episode

- **Sensory** z_i = f(x_i): vision+text encoders of the candidate model applied to one sampled image frame + task instruction, mean-pooled to a single vector.
- **Motor** τ_i ∈ R^{h×7}: end-effector state over next h steps — position (R³), orientation (roll/pitch/yaw as SO(3) rotations so distances respect geometry), gripper coordinate.

### 2. Distances matched to each space

    d_sensory(i,j) = 1 − cos(z_i, z_j)
    d_motor(i,j)   = DTW(τ_i, τ_j)   # speed/warp-invariant trajectory distance

### 3. Mutual nearest-neighbor overlap (CKNNA)

    S² = mNN = (1/Nk) Σ_i |N_sensory(i) ∩ N_motor(i)|

k=10, centered/normalized CKNNA variant (per Huh et al. PRH). Reference datasets: DROID (Franka), BridgeDataV2 (WidowX), ALOHA (bimanual). Sample N episodes; one random frame per episode; repeat over sampled frames.

### 4. Validation ladder (how to trust a proxy)

1. **Correlation across families**: 12 VLAs vs SimplerEnv success r=+0.717 (p=.004); 8 raw VLMs vs success of VLAs fine-tuned FROM them r=+0.681; 6 WAMs vs RoboTwin 2.0 r=+0.718; 5 real-robot policies (MolmoBot, shared protocol) r=+0.831.
2. **Beat alternative proxies on the same models**: VQA r=−0.154 (nothing); SSIM r=+0.558, PSNR r=+0.468, FID runs BACKWARDS (lower quality ↔ higher success, r=+0.680) vs S² r=+0.999 on the 3 video-generating WAMs.
3. **Robustness**: transfers across reference datasets (DROID 0.717 / BridgeDataV2 0.699), horizons (r>0.5 through h=220), and 8 implementation settings.
4. **Negative control (mandatory)**: embodiment mismatch — score bimanual WAMs on single-arm reference data — collapses correlation r=+0.999 → +0.246. A sound alignment metric must respond to embodiment mismatch.

## Representation-Level Diagnostics (decompose the score)

- **Modality dominance**: after VLA fine-tuning, success tracks VISION-only S² (r=+0.694) not TEXT-only S² (r=+0.237, n.s.) — fine-tuned VLAs act on what they see, explaining observed instruction-ignoring.
- **Frozen encoders**: freezing the vision encoder during fine-tuning blocks the S² gain — performance comes from pulling sensory representations toward motor structure.
- **Iterative denoising**: WAM features reach near-max S² at the earliest denoising step and stay flat — explains why skipping video denoising barely hurts success.
- **Layer choice**: schedule-averaged S² peaks at Block 14 (mid-depth) of the 30-block video backbone in all 3 WAMs — the layers carrying semantic reasoning are the ones aligned with motion.

## Implementation Recipe

1. Pick a reference dataset paired with your embodiment (mismatched embodiment invalidates the metric).
2. Sample N episodes × one random frame each; encode sensory (vision+text pooled) with the CANDIDATE model's own encoders.
3. Build motor features: next-h-step end-effector state, rotations as SO(3), DTW distance.
4. Compute centered/normalized CKNNA (k=10) between the two neighbor structures; average over sampled frames.
5. Rank models; validate once against whatever ground-truth success data exists; keep closed-loop eval as the final arbiter for the shortlist.
6. For diagnosis: recompute S² per modality (vision-only / text-only), per layer, per denoising step.

## Generalizable Patterns

- **Action as a modality**: trajectories are a projection of reality like images/text; a capable model's representation neighborhoods should agree with action-space neighborhoods. Generalizes PRH from passive modalities to interaction.
- **k-NN overlap as universal alignment probe**: works between an embedding space and any structured object space once you choose a proper metric there (DTW for sequences, SO(3) for rotations). No training, no probes, no labels.
- **Screen before you spend**: compute the cheap alignment proxy on RAW backbones before expensive fine-tuning — it predicts post-fine-tuning success better than capability benchmarks do.
- **Passive metrics don't predict action**: perception/generation quality is orthogonal to whether representations are organized for the motions required.
- **Negative control for metrics**: deliberately break a required condition (embodiment mismatch) and demand the metric collapse — otherwise it is measuring something else.

## Honest Limitations (from the paper)
- The S²–success link is CORRELATIONAL across tested models; not yet shown useful as a direct training objective.
- Models with similar S² can have different success rates — use for screening/prioritization only; closed-loop evaluation remains the final step.
- Evidence base is thin per cell: limited families and recipes, few models per comparison (5–12), one real-robot setting; broader generalization untested.

## Related Skills

- [[platonic-representations-brain]] — PRH in human fMRI representations
- [[vlm-lam-brain-alignment]] — aligning VLM/large-action-model representations with brain data
- [[mllm-tom-valence-brain-alignment]] — scoring multimodal model ToM/valence against fMRI
- [[eeg-based-lm-evaluation]] — neural signals as evaluation substrate
