---
name: orca-anchor-relative-object-centric-rl
description: "Use when object-centric RL agents relearn the same behavior at every location or collapse under scene shifts. ORCA anchor-relative coordinates plus ORBiT transformer give shift/rotation robustness and distractor generalization."
category: ai_collection
metadata:
  arxiv_id: "2610.28197"
---

# ORCA/ORBiT: Anchor-Relative Coordinates for Object-Centric RL

Source: arXiv:2610.28197 (Derstroff, Blüml, Moos, Girstl, Ye et al., Oct 2026). Object-centric RL agents typically receive each object's position in a **fixed global frame**, even though decisions depend on where objects are **relative to one another**. Consequences: the agent must relearn the same response at every location where a configuration occurs, and performance collapses when the scene is merely shifted.

## Method

1. **ORCA — Object-Relative Coordinates fixed to Anchor**: describe entities in a relative frame of reference anchored to one decision-relevant object (not the global origin).
2. **ORBiT — Object-Relative inductive-Bias Transformer**: transformer architecture for processing anchor-relative inputs in RL.
3. The anchor must be **decision-relevant** — gains disappear with an arbitrary anchor.

## Results

- Relative representations improve performance for **both MLP and transformer** agents — the coordinate frame matters independent of architecture.
- ORBiT beats the pixel-based PPO baseline: aggregate **HNS IQM greater than 1.0 over 13 Atari games**.
- Learns the game of **Foosball from scratch**, dominating all baselines.
- Controlled Tag environment: ORCA **extends to rotations**; ORBiT **generalizes to unseen numbers of distractors**.

## Reuse pattern

- Whenever entity-based state is built for RL/planning: re-express all entity positions **relative to an anchor the policy actually conditions on** (goal, held object, agent) instead of global coordinates — shift invariance by construction, not by data augmentation.
- Choose the anchor from the decision structure of the task; test anchor ablations.
- Relative frames also transfer to rotation if the anchor frame rotates with the scene.
- Complements (does not replace) equivariant-network approaches: ORCA is a cheap input-representation fix that works with plain MLPs and transformers.

Related: equivariant RL, object-centric world models, graph-based RL state encoders, symmetry-exploiting architectures.
