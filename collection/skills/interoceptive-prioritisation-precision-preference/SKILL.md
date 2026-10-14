---
name: interoceptive-prioritisation-precision-preference
description: "Active inference双路径内感受优先级方法论：κ-routing（似然精度路由，改证据流）与dynamic-C（偏好重加权，改目标），二者经期望自由能作用于同一行为却产生可分离的感知/调节/学习效应。用内感受后验熵、最小裕量、访问状态熵、学习模型质量四类内部观测量区分机制，而非仅看生存率。Use when: modeling interoception/homeostatic control in active inference, dissociating attention-as-precision from motivation-as-preference, analyzing degeneracy of prioritisation mechanisms, or evaluating embodied agents beyond survival metrics."
---

# Two Routes to Interoceptive Prioritisation (κ-routing vs dynamic-C)

**Source**: Grimbly et al., "Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference" (arXiv:2610.18617, 13 Oct 2026, UCT Neuroscience Institute / Laureate Institute)

## Activation

active inference, interoception, likelihood precision, prior preferences, expected free energy, Dirichlet learning, homeostasis, 内感受, 精度路由, 偏好重加权, need prioritisation, AffectWorld, body model learning, attention as precision, motivational active inference, degeneracy

## Core Methodology

### 1. Two dissociable mechanisms acting through one policy score

An agent facing competing lethal needs can prioritise via two *distinct* mechanisms that both flow into expected free energy but enter the generative model at different loci:

| | κ-routing (likelihood precision) | dynamic-C (preference reweighting) |
|---|---|---|
| What changes | Diagonal precision κ of interoceptive likelihood A^(m) | Raw preference scores C rewritten from posterior deficits |
| Enters | State inference + policy evaluation + **Dirichlet learning update** | **Only the pragmatic (risk) term** of G(π) |
| Biological analog | Gain control on interoceptive afferents | Changes in regulated outcomes (motivational/homeostatic) |
| Total budget | Fixed K = M·κ̄ — prioritising one channel *necessarily* de-prioritises others | No shared budget; but oxygen (passive recovery) has no direct preference target |
| Side effect | Sharper evidence about the selected need | Changes **which states the agent visits** → indirectly changes what it learns |

Key structural fact: preferences never enter the likelihood update, yet they change learning by changing experience. This is the indirect coupling (Neacsu et al.) made operational.

### 2. Generative model (discrete active inference)

- POMDP: state factors = grid position + context + true need levels; agent infers only need levels (position observed exactly, resource cue 0.95 accuracy, ordinal interoceptive observations noisy)
- Likelihood P(o|s)=Cat(A) with per-channel factorisation A={A^(m)}, M=3 channels (hunger/thirst/oxygen)
- Expected free energy: G(π) = D_KL[Q(o|π)‖P_C(o)] (risk) + E_Q[ H[P(o|s)] ] (ambiguity); policies P(π)=σ(-γG(π))
- Up to normalisation, -G(π) = E_Q[C(o)] + I_Q(s;o|π) — C enters expected utility, A enters predicted outcomes and state information gain
- Online learning of A only (movement/body dynamics given): Dirichlet counts a^(m) += η(o^(m) ⊗ q(s^(m))), posterior-weighted outer product
- Task design principle: three needs in tension — drinking relieves thirst but lowers oxygen (water submerges agent); best priority is state-dependent

### 3. Four conditions, paired design

uniform baseline / κ-routing alone / dynamic-C alone / combined. Paired seeds × layouts across conditions; survival = fraction of 120-step episode completed. All conditions keep state information gain (no curiosity-driven model improvement) — conditions differ only in the experience their policies provide.

### 4. Internal observables (the actual contribution)

Survival alone cannot dissociate the mechanisms (degeneracy: both produce similar behaviour). Measure alongside survival:

1. **Posterior entropy** H̄ (sharpness of interoceptive beliefs) — precision signature
2. **Minimum headroom** b = ⟨min_m s^(m)/L_m⟩ (distance of most endangered need from lethal boundary, computed from TRUE body levels so perception cannot contaminate the measure) — regulation signature
3. **Visited-state entropy** H[p_visit] (breadth of body states occupied) — experience signature
4. **Learned-model quality** p*^(m) = probability learned likelihood assigns to true-model-favoured observation, reported **both across all levels and across visited levels** — the all-level vs visited-level split is what exposes "narrower experience" vs "poorer learning"

### 5. Key results

- Survival (11 layouts): κ-routing +0.27 (Holm p=.018), dynamic-C +0.11 (n.s., CI spans both signs), combined +0.38 (p=.018)
- 72 pre-registered additional layouts: precision +0.111, preference +0.080, **interaction +0.114 (p=.002)** — complementarity on the survival scale
- **Honest negative result**: the predicted preference benefit on difficult layouts was NOT established (primary test ≈0, p=.58); unadjusted tertile contrasts ran opposite (largest benefit on easiest layouts). The "overcommitment" account is retained for the original layouts only
- Precision lowers posterior entropy (-1.37×10⁻³ nats); preference raises headroom (+0.05, combined +0.11); both cut time-with-two-needs-near-death from ~2% to <0.1%
- **Preference changes the learned model**: lower quality averaged over ALL need levels, slightly HIGHER quality on visited levels, fewer levels visited — rarely-visited levels stay near the vague prior. Lower score = narrower experience, not poorer performance on encountered states
- Belief-only κ variant (uniform emission, routed inference/planning) improved survival +0.33 on 6/11 layouts — sharper emission is not required for benefit

## Implementation Guide

```python
# κ-routing: diagonal precision on interoceptive likelihood
def route_precision(A, channel_m, kappa_high, kappa_bar):
    """Total precision conserved: prioritising m de-prioritises others."""
    # A[m] diagonal mass = kappa for selected channel, others scale down
    # so that M * kappa_bar = K stays fixed
    ...

# dynamic-C: rewrite preference scores from posterior deficits
def reweight_preferences(C, q_deficit, threshold):
    """C_food   += f(q_hunger_deficit)
       C_water  += f(q_thirst_deficit)
       if deficit > threshold: penalty on alternative/empty tiles"""
    # enters ONLY the pragmatic term of G(pi) — never the Dirichlet update
    ...

# Dirichlet update (both conditions share this; only visited states differ)
# a[m] += eta * outer(o_onehot[m], q(s[m]))
```

Repo: https://github.com/sgrimbly/interoceptive-prioritisation-iwai2026-snapshot

## When to Apply

- Building active-inference agents with multiple homeostatic/interoceptive channels
- Deciding whether to implement attention as precision or motivation as preference
- Evaluating embodied agents: never report survival/accuracy alone — pair with posterior entropy, headroom (from ground truth), visited-state coverage, and visited-vs-all model quality
- Any setting with mechanism degeneracy: two agents with equal task success may have learned different bodies

## Pitfalls

- **Fixed total precision**: κ-routing under a conservation constraint trades off between channels — do not add precision without removing it elsewhere
- **All-level model quality is misleading**: an agent that overcommits to one need will look like a worse learner on the full likelihood while being fine on what it actually encounters; always split visited vs all
- **Passive channels break symmetry**: needs that recover without action (oxygen on land) cannot be reached by preference reweighting — they need precision routing or outcome-level preferences
- **Post-hoc difficulty splits don't replicate**: the difficulty-dependence of the preference benefit found post hoc on 11 layouts failed a pre-registered 72-layout test — treat post-hoc splits as hypotheses only
- **Headroom must be computed from true levels**, not inferred beliefs, or the measurement inherits the intervention

## Related Skills

- `belief-mop-active-inference-bellman` (POMDP belief-space EFE value iteration)
- `snn-dmn-self-consciousness` (default-mode interoceptive modelling)
- `mem-motivated-emotional-mind-consciousness` (affective/interoceptive hierarchy)
