---
name: intrinsic-goals-drosophila-autonomy
description: Use when intrinsic motivation must explain animal autonomy.
category: ai_collection
---

# Intrinsic Goals for Autonomous Agents: Hierarchical Exploration Matches Drosophila Volitional Action

**Source**: Kutscher, Keller, Kirsch, Pei & Nayebi (UMD/CMU), "Intrinsic Goals for Autonomous Agents: Hierarchical Exploration Captures Future Volitional Action in Drosophila", arXiv:2610.34638 (Oct 2026). Project: neuroagents-lab.github.io/autonomous_drosophila

Reverse-engineers animal autonomy by training **20 intrinsic-drive methods (IDM)** — no external reward — on a biomechanical Drosophila digital twin, then scoring each against whole-brain recordings of spontaneously exploring flies (Brezovec et al. 2023). Winner: **DIAYN operating hierarchically over ethological motor primitives**.

## Biological ground truth (the evaluation target)

- Head-fixed flies on a spherical treadmill in darkness; whole-brain imaging.
- Interhemispheric activity difference in the Inferior Posterior Slope (IPS) predicts future turn direction **~15–8 s before a turn** (neural prospective coding 66.5 ± 1.4% BA).
- Sum rule: bilateral summed activity ↔ forward velocity (r = 0.429); difference rule: interhemispheric difference ↔ angular velocity (r = 0.191).
- Behavior alone predicts turn direction at 60.5 ± 0.9% BA; flies show wide inter-individual turning-bias variability (handedness).

## Agent architecture (the hypothesis space)

- **Embodiment**: NeuroMechFly v2 in FlyGym/MuJoCo (1e-4 s timestep); compound-eye vision (pale/yellow ommatidia), bilateral olfaction, proprioception (joint angles/velocities, body kinematics). 310-dim fused features → actor & critic LSTMs (256 units) → MLP heads.
- **Hierarchy**: every 100 ms the policy picks one of **7 motor primitives** — forward, left, hard-left, right, hard-right, stop, groom. Locomotor primitives drive a CPG whose phase indexes real walking-fly step trajectories; grooming = kinematic replay. Intrinsic objectives act on ethological syllables, not joint torques.
- **Training**: Recurrent PPO, 2048 parallel envs, procedural arenas (3 odor sources, 12–50 obstacles), 50M policy decisions, identical budget for all 20 IDMs + random-init and extrinsic controls.

## DIAYN objective (winning hypothesis)

r(θ) = I(S; Z) + H(A|S,Z) = H(Z) − H(Z|S) + H(A|S,Z), per-step intrinsic reward:

rₜ = log q_θ(z|φₜ) − log π(aₜ|φₜ, z)

(q = skill discriminator, φ = encoded sensory state, z = skill sampled uniformly). −H(Z|S) makes skills induce **distinguishable states**; H(A|S,Z) keeps within-skill action entropy high. Each skill = a persistent exploratory strategy (one skill held per 30-min evaluation rollout, paralleling one fly).

## Key results

1. **Prospective coding emerges from intrinsic motivation alone**: DIAYN 82.1±0.9%, NGU 65.4±1.8% neural BA vs fly 66.5±1.4%. 9/20 IDMs never turn or turn one direction only (immediate behavioral mismatch).
2. **The ratio matters**: an agent matches the fly only if BOTH neural and behavioral predictability land on the fly's neural:behavioral ratio line. DIAYN is the only IDM that does (NGU exceeds neural but breaks the ratio); MAX has 92% behavioral but wrong ratio — highly predictable behavior ≠ fly-like.
3. **Population variability captured**: DIAYN's skill library spans the same wide turning-bias range as 9 individual flies (state-space coverage); same-schedule controls (CSF, Random-DIAYN) stay narrow → spread comes from the learned objective, not the sampling scheme.
4. **Sum-difference rule recovered**: PCA on DIAYN actor-LSTM activity finds component pairs whose difference ↔ ω (r=0.153) and sum ↔ v (r=0.413), close to fly IPS (0.191/0.429); absent in random-init control (0.021/0.113).
5. **Interpretation**: individual flies may each commit to one strategy (limited-capacity brain) while the POPULATION realizes diversity that maximizes sensory state-space coverage — evolution optimizes the repertoire, handedness is an individual sample from it.

## Evaluation protocol (reusable as a benchmark recipe)

1. Freeze policy; evaluate in a tethered-ball assay (head-fixed 9 mm air-supported ball, vision+odor zeroed), 9×30-min rollouts.
2. Match biological preprocessing exactly: 500 ms Savitzky-Golay smoothing; turns = |angular velocity| peaks > 200°/s; turning bias = log(N_R/N_L).
3. Decode future turn direction from the −15..−8 s window (elastic-net logistic regression, 5-fold stratified CV, balanced accuracy); decode from both internal activity (best layer among actor/critic LSTM, MLP heads, concatenations) and behavior alone (mean ω, v).
4. Accept an intrinsic objective only if it matches: (a) behavioral prospective coding, (b) neural prospective coding, (c) the neural:behavioral ratio, (d) population-level bias spread, (e) low-dim sum/difference structure vs ω/v.

## How to apply

- **Designing autonomous agents**: hierarchical skill discovery over behavior primitives (not raw torques) + competency objectives (state-distinguishability) is the strongest known intrinsic drive for animal-like autonomy; curiosity/entropy families underperform or collapse to no-turn/single-turn pathologies.
- **Choosing intrinsic rewards**: evaluate against biology (behavioral variability + internal predictivity), not only downstream task performance — predictable behavior and matched mean statistics are insufficient evidence.
- **NeuroAI model selection**: the joint neural+behavioral matching protocol generalizes to any whole-brain/whole-body dataset with spontaneous behavior; use the ratio constraint to reject superficially matching baselines.
- **Population-level coverage hypothesis**: when explaining individual behavioral idiosyncrasy (handedness), test whether the POPULATION distribution optimizes state-space coverage; a DIAYN skill library gives a mechanistic model of that distribution.

## Related skills
- `untrained-connectome-sensorimotor-banc` — connectome-based fly behavior (wiring-first vs objective-first contrast)
- `beast3d-animal-behavioral-neural-encoding` — 3D behavioral + neural encoding analysis
- `multi-plasticity-snn-training` — complementary biologically motivated learning
