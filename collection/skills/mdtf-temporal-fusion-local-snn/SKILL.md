---
name: mdtf-temporal-fusion-local-snn
description: Use when building deep SNNs trained with local STDP and temporal fusion.
category: ai_collection
---

# Multi-Depth Temporal Fusion (MDTF): Feedforward, Locally Trained Spiking Neural Networks

**Source**: arXiv:2609.37047 (Attar, Cicciarella, Rossi — University of Padua, 29 Sep 2026)
**Code**: https://github.com/aidinattar/multi-depth-temporal-fusion-snn

## Core Question

How much can deep convolutional SNNs achieve when learning stays **fully local** (no backprop, no global error signals)? Under local plasticity, any feature suppressed by an intermediate layer is *permanently lost* — later layers cannot recover it via gradients. So depth becomes a problem of **temporal evidence routing**, not just adding stages.

## Architecture (4 components)

### 1. Label-free early-vision latency front end (deterministic, no learning)
Pipeline: local decorrelation → signed-context gate → polarity split → response calibration → polarity balancing → latency encode.
- Local decorrelation: patch whitening `W = (Σ + εI)^{-1/2}` estimated once from train split, frozen
- Polarity split: positive/negative contrasts → separate ON/OFF latency maps (2 maps grayscale, 6 maps RGB; 1 per polarity-time channel for events)
- Latency coding: `L_j(u) = max(ℓmax − (ℓmax−ℓmin)·ã⋆_j(u), ∞)` on [0,1] — stronger response ⇒ earlier spike; below `θsilent` ⇒ silent (∞)
- **Ablation proof it matters**: simple latency coding gives 9.8% on MNIST (chance); full front end 96.7% — the front end IS the representation for local learning

### 2. Four-layer conv backbone S1–S4, layerwise unsupervised STDP
- General local update: `Δw_ij = λ_j·[A⁺F⁺(w) if t_i≤t_j else −A⁻F⁻(w)]`
- Conv layers use soft-bounded weights: `F⁺=e^{-βw}`, `F⁻=e^{β(w-1)}` (potentiation decays near upper bound)
- λ_j from local winner selection + layer-specific LR schedule; layers trained one at a time then **frozen** (cached representations)
- C1/C2: deterministic min-latency pooling, export latency representations

### 3. MDTF — the key contribution (deterministic, no parameters to train)
Three representations: **P** = preserved shallow H⁽¹⁾, **I** = intermediate H⁽²⁾, **D** = deep H⁽⁴⁾.
Fused code: `H = [P, Δres, Δagree]`
- **Residual principle**: `Δres = TopK_kres(I)` — temporal top-k: keep the k *earliest* finite events of I, suppress the rest. Deep processing enriches but never replaces P.
- **Agreement gating**: `Δagree(i) = min{I(i),D(i)}` iff both finite AND `|I(i)−D(i)| ≤ m_agree`, else silence; then `TopK_kagree(Δagree)`. Isolated/temporally-inconsistent deep events are suppressed — deep evidence survives only when it confirms the intermediate code in time.

### 4. Multi-prototype R-STDP readout (only task-driven part)
- Population coding: each class = small set of prototype neurons; class latency `τ_c = min over prototypes`; predict `ŷ = argmin_c τ_c`
- Temporal corridor: `τ̄ = mean of finite class latencies`; target must fire before `τ̄ − m/2`, non-targets after `τ̄ + m/2`
- Reward (target prototypes): `λ⁺_j = clip([τ_j − τ*_{y}]⁺/β⁺, 0, λmax)/τmax` — late-firing targets get stronger updates; already-early neurons get none
- **Sparse punishment**: only the K classes with largest margin violations get anti-STDP (hard negatives P_hn) — avoids destabilizing non-competing classes
- Additive update (F⁺=F⁻=1) + weight clipping + fixed per-neuron ℓ1 normalization for stability; silent-state guards
- Correctly-classified samples keep margin updates at reduced scale

## Results

| Dataset | Accuracy | vs local STDP/R-STDP baseline [14] |
|---|---|---|
| MNIST | 96.6±0.6 | −0.3 (ns) |
| Fashion-MNIST | 86.3±0.7 | **+18.2 pp** |
| CIFAR-10 | 62.5±0.4 | **+29.2 pp** |
| N-MNIST (events) | 95.1±0.6 | **+73.0 pp** (baseline lacks event front end) |

- Baseline collapse on N-MNIST (22%) shows event→latency front end is mandatory for event streams
- Code sparsity: 5.7–12.6% active density (994–3100 events/sample) — high data efficiency
- **Spike-budget Pareto**: retrain readout on top-X% earliest spikes only — gradual graceful degradation; early/strong events carry concentrated value; budgets tune accuracy-vs-activity tradeoff
- Front-end ablations (MNIST): simple latency 9.80 → w/o signed context 95.41 → w/o polarity balance 95.02 → full 96.68

## Reusable Patterns

1. **Evidence routing under local learning**: when no gradient can recover lost features, preserve shallow codes by default (residual) and admit deep features only via temporal consensus — analogous to gated skip connections, but consensus-based and timing-native
2. **Temporal top-k sparsification**: rank events by latency (earlier=stronger), keep top-k — a general purpose tool for event-code compression
3. **Agreement tolerance m_agree**: cross-depth temporal consistency as a trust gate — filters noise/hallucinated deep events without labels
4. **Corridor-based margin reward**: continuous reward from margin violation, not binary reward — replaces sparse RL signal with differentiable-ish temporal objective
5. **Sparse hard-negative anti-STDP**: punish only the top-K competing classes — stability trick transferable to any competitive learning readout
6. **Frozen-cache layerwise training**: train layer → freeze → cache representations → train next. Standard for local learning pipelines

## Limitations

- CIFAR-10 62.5% — local learning ceiling remains far below gradient methods; gains are architectural, not a solution to local-plasticity limits
- MDTF hyperparams (k_res, k_agree, m_agree) fixed per dataset, no adaptation rule given
- Static-image latency coding requires dataset-level statistics (not event-native)

**Activation**: spiking neural network, local learning, STDP, reward-modulated STDP, time-to-first-spike, TTFS latency coding, temporal fusion, residual routing, event-based vision, neuromorphic, layerwise training, population coding, spike sparsity, activity budget
