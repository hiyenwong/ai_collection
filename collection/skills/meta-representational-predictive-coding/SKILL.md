---
name: meta-representational-predictive-coding
description: "Meta-Representational Predictive Coding (MPC) — encoder-only neuroscience-informed self-supervised learning within the free energy principle, using cross-stream latent prediction and active inference saccade planning instead of backpropagation (arXiv: 2503.21796v2)"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2503.21796"
  arxiv_version: "v2"
  published: "2025-03-22"
  updated: "2026-07-02"
  authors: "Alexander G. Ororbia, Karl Friston, Rajesh P. N. Rao"
  tags: [predictive-coding, self-supervised-learning, free-energy-principle, active-inference, NeuroSSL, brain-inspired, encoder-only, biological-plausibility]
---

# Meta-Representational Predictive Coding (MPC)

**arXiv**: 2503.21796v2 | **Updated**: 2026-07-02 | **Authors**: Ororbia (RIT), Friston (VERSES AI), Rao (UW)

## Core Concept

Meta-Representational Predictive Coding (MPC) inverts standard predictive coding: instead of learning a **generative decoder** that predicts raw sensory input (pixels), MPC learns an **encoder-only** model where latent representations predict each other across parallel neural streams. This creates biologically plausible self-supervised learning (NeuroSSL) without backpropagation.

**Key Insight**: Standard predictive coding (GPC) requires predicting high-dimensional sensory data. MPC sidesteps this by predicting *representations* across streams — foveal predicts parafoveal, parafoveal predicts peripheral, and vice versa — using local Hebbian plasticity.

## Architecture

### Multi-Stream Visual Structure

Inspired by central/peripheral vision functional anatomy:
- **Foveal streams**: High-resolution fine-grained features (stroke/arc components)
- **Parafoveal streams**: Medium-resolution object/part chunks
- **Peripheral streams**: Low-resolution global context

Each stream V processes sensory glimpses through L layers with:
```
mu^{l,v} = W^{l,v} · phi(z^{l-1,v}(t))    (intra-stream prediction)
```

### Inter-Stream Cross-Prediction

Stream v predicts stream q's latent activity:
```
mu_C^{l,v,q} = R^{l,v,q} · phi(z^{l,q}(t)) + A^{l,v,q} · a^{l,v}    (inter-stream + action-conditional)
```

Where:
- `R^{l,v,q}`: inter-stream predictive synapses
- `A^{l,v,q}`: action-conditional afferent synapses (glimpse position)
- `a^{l,v}`: action/coordinate vector

### Variational Free Energy Objective

```
F = sum_{v=1}^{V} [ sum_{l=1}^{L} gamma_{v,q} · N(z^{l,q}(t); mu_C^{l,v,q}, Sigma_C) + lambda_w · ||W^{l,v}||^2 ]
```

Inter-stream topology weighting: `gamma_{v,q} = alpha^{(q-v) mod V}` (power decay kernel)

## Learning Rules (Backprop-Free)

### Synaptic Plasticity (Local Hebbian)

**Intra-stream synapses** (Eq. 11):
```
tau_w · dW^{l,v}/dt = -lambda_w · W^{l,v} + e^{l,v} · (phi(z^{l-1,v}))^T
```

**Inter-stream synapses** (Eq. 12):
```
tau_w · dR^{l,v,q}/dt = -lambda_w · R^{l,v,q} + e_C^{l,v,q} · (phi(z^{l,v}))^T
```

**Action-conditional synapses** (Eq. 13):
```
tau_w · dA^{l,v,q}/dt = -lambda_w · A^{l,v,q} + e_C^{l,v,q} · (a^{l,v})^T
```

Where `e^{l,v}` and `e_C^{l,v,q}` are prediction errors (intra- and inter-stream).

### Inference Dynamics (E-step)

Neuronal state update via Euler integration (Eq. 10):
```
tau · dz^{l,v}/dt = -z^{l,v} + phi(z^{l,v}) + e^{l,v} + sum_q e_C^{l,v,q}
```

Scheduled as Expectation-Maximization: E-step (inference) then M-step (synaptic update).

## Active Inference: Epistemic Saccade Planning

MPC uses **active perception** to decide where to look next, driven by free energy minimization:

1. **Bottom-up focus landscape**: `S_BU(u,v) = G_BU(o_lgn)` — local feature energy from LGN-filtered image
2. **Top-down epistemic map**: accumulated prediction errors guide information foraging
3. **Focus map**: `A = S_BU + S_TD` balances reflexive and epistemic signals
4. **Next saccade**: `c_{k+1} = argmax(A)` (or stochastic Gumbel-Max sampling)

### Stochastic Foraging Temperature Schedule

Dual-phase sigmoidal decay (Eq. 38):
```
T(rho) = tau_min + (tau_max - tau_min) / (1 + exp(lambda * (rho - rho_0)))
```
- Phase 1 (exploration): High temperature for k < 0.35K
- Phase 2 (exploitation): Low temperature for k >= 0.35K
- Config: tau_max=0.012, tau_min=0.0012, rho_0=0.35, lambda=10.0

## Latent Glimpse Path Integration

Global code `z_K` built iteratively across K saccades, inspired by grid-cell spatial mapping:

**Content-Location Binding** (what-where):
- Content: stream activity magnitudes (z_k)
- Location: coordinate vector (c_k)

**Running moments** (Eq. 25-26):
```
Sigma_{f,k} = Sigma_{f,k-1} + f_k       (first-order)
Sigma_{f^2,k} = Sigma_{f^2,k-1} + f_k^2  (second-order)
```

Where `f_k = [z_k; c_k]` (concatenation of activity and coordinates).

## Key Results

### Downstream Classification (KNN probe)

| Dataset | MPC (proposed) | GPC-fov | I-JEPA | BP-CNN (supervised) |
|---------|---------------|---------|--------|---------------------|
| MNIST   | >98% (100 glimpses) | ~95% | ~97% | ~99% |
| K-MNIST | Competitive | Lower | Lower | ~95% |
| NORB    | >88% (80 glimpses) | Lower | N/A | ~92% |

### Key Findings
- MPC outperforms I-JEPA and GPC models in KNN discriminative performance
- Generalization improves with glimpse budget (more saccades = better representation)
- Epistemic saccade planner maintains 80.5% accuracy under maximal boundary, vs 61% for random saccades
- Zero-shot generalization demonstrated in v2 update

## Comparison: MPC vs Standard Predictive Coding (GPC)

| Feature | MPC (Encoder-only) | GPC (Generative decoder) |
|---------|-------------------|------------------------|
| Target | Latent representations | Raw sensory input |
| Architecture | Multi-stream encoder | Decoder-centric |
| Learning | Hebbian (local) | Hebbian (local) |
| Self-supervised | Yes (cross-stream) | No (unsupervised reconstruction) |
| Active sensing | Yes (saccade planning) | Optional |
| Biological plausibility | High (no backprop) | High (no backprop) |

## Implementation Notes

### Model Configuration
- Number of layers: L=3
- Stream types: foveal, parafoveal, peripheral (V total streams)
- Activation: element-wise nonlinearity phi()
- Synaptic decay: lambda_w (regularization)
- Time constant: tau_w (plasticity rate)

### Training Protocol
1. Extract multi-resolution glimpses from image
2. Run E-step: iterate neuronal dynamics to convergence
3. Run M-step: update synapses via Hebbian rules
4. Plan next saccade via epistemic focus map
5. Integrate latent code across saccade trajectory
6. Repeat for K glimpses per image

### Datasets Validated
- MNIST (28x28, 10 classes)
- Kuzushiji-MNIST (28x28, 10 classes)
- NYU NORB (96x96, 5 classes, stereo)
- ETH-80 (256x256, 8 classes)

## Limitations

1. **Biological fidelity**: MPC is loose inspiration, not faithful neuroanatomy
2. **Scale**: Validated on small datasets (MNIST, NORB), not large-scale vision
3. **Rate codes**: Uses rate-based neurons, not spikes
4. **Single modality**: Visual only, not extended to audio/language
5. **Temporal dynamics**: Static images, not video sequences

## Activation Keywords

`predictive coding`, `meta-representational`, `MPC`, `NeuroSSL`, `self-supervised learning`, `free energy principle`, `active inference`, `saccade planning`, `encoder-only`, `biological plausibility`, `Hebbian learning`, `backprop-free`, `cross-stream prediction`, `foveal`, `parafoveal`, `peripheral vision`, `free energy`, `Ororbia`, `Friston`, `Rao`, `joint-embedding`, `JEPA alternative`

## Related Skills

- `predictive-coding-light` — Simpler predictive coding framework for SNNs
- `predictive-coding-exponential-family` — Extended PC with exponential family
- `neocortex-error-driven-predictive-learning` — Neocortical learning via error-driven PC
- `online-generalised-predictive-coding` — Online generalized PC via dynamic expectations
- `closed-form-predictive-coding-hgf` — Closed-form PC via hierarchical Gaussian filtering

## References

1. Ororbia, A., Friston, K., & Rao, R.P.N. (2025/2026). Meta-Representational Predictive Coding: Neuroscience-Informed Self-Supervised Learning. arXiv:2503.21796v2.
2. Rao, R.P.N. & Ballard, D.H. (1999). Predictive coding in the visual cortex. Nature Neuroscience.
3. Friston, K. (2010). The free-energy principle: a unified brain theory? Nature Reviews Neuroscience.
4. Assran, M. et al. (2023). Self-supervised learning from images with a joint-embedding predictive architecture (I-JEPA). CVPR.

**Paper**: https://arxiv.org/abs/2503.21796
**HTML**: https://arxiv.org/html/2503.21796v2
