---
name: temporal-representation-degree-neural-networks
description: Time as explicit computational variable defines a 0-4 degree taxonomy of networks.
trigger: degree of temporal representation, temporal vs spatial gradient, delay neural network, DeNN, TTFS coding, synaptic delay learning, event-based dataset, spiking vs ANN comparison
category: neuroscience
---

# Degree of Temporal Representation in Neural Networks (arXiv 2610.19730)

**Paper**: "Design and Analysis of Temporal Representations in Neural Networks" — Alban Colas-Gattepaille (Université Côte d'Azur, I3S), Alexandre Muzy (ILLS McGill/MILA), submitted 14 Oct 2026, cs.NE.

**One-line**: 提出以"网络函数是否显式操纵时间作为计算变量"定义的**时间表示度（0–4）分类学**：把网络的四类函数（编码/激活/解码/学习）逐一判定 temporal 与否——关键洞察是**SNN 的二值脉冲激活本身是非时间性的**（spike 是布尔事件，不携带时刻），ANN 与 SNN 可以同度；在固定架构上单调提升时间度 → GSC 性能与能效单调提升，DeNN（度4）达 SOTA 98.94%（35类，175K参数）超过 AST transformer。

## The Taxonomy: function-level temporal audit

A function is **temporal iff time explicitly appears as a computational variable** in it. Audit four function slots:

| Slot | Temporal example | Non-temporal example |
|------|-----------------|---------------------|
| Encoding | DeNN: average inter-spike interval per neuron | ANN/SNN: brightness levels, event counts |
| Activation | DeNN: spike-time-delayed o_j[t] = Σ sgn(ds_ij)·(e^{−(z_i[t]+d_ij)} − e^{−(z_i[t]+c)}) | ANN weighted-sum; SNN IF/LIF/adLIF membrane updates (binary spike = boolean, NOT a timestamp) |
| Decoding | DeNN: temporal softmin over spike times (faster = bigger weight) | time-aggregated softmax (ANN); softmax over spike counts (SNN) |
| Learning | DeNN: ∂L/∂ds_ij ∝ Σ_t e^{−(z_i[t]+d_ij)} — gradient depends on arrival-time history | BPTT: spatial components dominate (Meng et al. 2023); boxcar surrogate |

**Degrees measured in the paper**: DeNN=4, exponential ANN=2, adLIF=1, LIF=0. (ANN here gets temporal encoding + decoding; SNNs get temporal encoding only.)
- Core definitional move: a network "processing signals over time" (recurrent membrane dynamics) ≠ representing time. Temporal dependence typically arises only through learning dynamics unless time is an explicit variable.

## DeNN mechanics (Delay Neural Network)

- **Synaptic delays replace weights as the learned quantity**: real sign-delays d_sij ∈ ℝ, physical delay d_ij = c·exp(−d_sij) > 0 (c=1). Sign of d_sij = excitatory/inhibitory; distance to zero = strength (smaller delay = stronger).
- Forward pass uses **arrival time** t_i + d_ij, not coefficient multiplication: o_j[t] = Σ_i sgn(d_sij)[κ(z_i[t]+d_ij) − κ(z_i[t]+c)], κ = e^{−x}; then LayerNorm-standardize → z_j[t].
- **Long-term memory** (ν timesteps): m_j^h[t] = sign(δ)·(e^{−|δ|}−1) with δ = z_j[t]−z_j[t−h]; z_e = z + Σ_h α·m. α learnable → multi-timescale memory without recurrence.
- **Encoding**: event2time algorithm scans events in temporal order, emits T arrays each holding proportion-p of active pixels; DeNN input = average ISI; SNN input = event count; ANN input = negated DeNN input (for controlled comparison).

## Theory: same function family ≠ same learning system

- **Lemma 3.1 / Thm 3.2**: initialize ANN weights w_ij = −sgn(d_sij)(e^{−d_ij}−e^{−c}) so both nets start at IDENTICAL outputs (z_ANN[t] = −z_DeNN[t] ∀t). After standardization the difference stays bounded (Υ ≤ z_ANN + z_DeNN ≤ Ψ) but NON-ZERO — trajectories diverge monotonically (Frobenius norm of δ-matrix grows then stabilizes; lower bound Υ→1.0092±0.0082, upper Ψ→0.7428±0.4292).
- **Lemma 3.3**: only at the FIRST gradient step is ∂L/∂w_ij = −(1/β_ij)·∂L/∂d_sij (proportional). After that they learn in different dimensions: DeNN gradient is temporal (short-term spike-arrival dynamics), ANN gradient is spatial.
- **IF-mapping (Eq 13-14)**: with F_j[Is] = ReLU(Σ w_ij e^{F_i}/θ − n_j θ), a DeNN trained on periods (1/frequency) converts to a frequency-domain IF network with **zero-loss conversion** (avg accuracy diff −0.00375±0.0014, N-MNIST). Conversion direction DeNN→IF works; training the IF model directly with surrogate gradients on temporal data does NOT (42–74% vs 91.9%).
- **Gradient split (Eq 16-17)**: delay parameters d_sij learn from SHORT-term dynamics (cosine similarity of the short-term proxy gradient with true gradient is high, Fig 3); memory parameters α learn from LONG-term dynamics (∝ Σ m_j^h[t], t>h). Timescales dissociate across parameter types.

## Benchmark Results

- **GSC 10-class subset** (temporal audio, speech2spikes encoding): accuracy strictly increases with degree — DeNN 91.90% > ANN(ν=100) 90.26% > adLIF 63.66% (74.47% w/ BN+dropout) > LIF 42.34%. DeNN reaches good performance from EPOCH 1; ANN needs several; SNNs far behind on purely temporal data.
- **Caveat the paper concedes**: adLIF's published benchmark is higher — because it uses mel-spectrogram input, not the purely-temporal event representation used here. Data representation choice confounds neuron-model comparisons.
- **GSC 35-class full SOTA**: DeNN 98.94% (175K params) > AST 98.11% (5.6M) > KWT-3 97.51% (610K) > SpikCommander 96.92% (2.13M spiking transformer) > d-cAdLIF 95.69%. Temporal feed-forward beats transformers and spiking transformers with ~30× fewer params than AST.
- **N-MNIST (spatial-ish)**: ANN ≈ DeNN — temporal degree pays off only when the dataset is genuinely temporal.
- **Efficiency**: DeNN more resilient to synapse pruning (reaches benchmark with fewer active synapses); better accuracy/cycles ratio on Intel and SpiNNaker; better accuracy/Joule on GPU.

## Reusable Patterns

1. **Function-slot temporal audit**: before claiming a model "uses time", check each of {encoding, activation, decoding, learning} for time as an explicit variable. Most "temporal" models fail at activation/learning (spatial gradients dominate BPTT).
2. **Identical-initialization trajectory comparison**: initialize two architectures to produce identical outputs, then measure divergence (Δ, Frobenius norm) — proves "mappable function families" ≠ "equivalent learning systems". Port to any architecture-pair comparison.
3. **Delay-as-parameter reparameterization**: d = c·exp(−d_s) keeps delays positive & differentiable; sign(d_s) encodes synapse type; |d_s| encodes strength. Replaces weight multiplication with arrival-time arithmetic.
4. **Train-in-time, convert-to-frequency**: train where gradients flow through temporal variables (DeNN), then convert to the deployable substrate (IF network) losslessly — instead of training the deployable substrate directly with surrogate gradients on temporal data.
5. **Parameter-type ↔ timescale dissociation**: check which parameter classes carry short- vs long-term learning signals (cosine-similarity of proxy gradients); design multi-timescale learning by assigning timescales to parameter types, not by adding recurrence.
6. **Degree-monotonicity benchmark design**: fix the architecture, vary ONLY the temporal degree of each function slot → clean causal read of "what does explicit time buy" (performance AND energy).

## Honest Limitations
- The "degree" is a coarse count (0–4), not weighted by slot importance; ANN=2 vs DeNN=4 hides that both share temporal encoding/decoding — the performance gap is attributable to activation+learning slots.
- DeNN activation is feed-forward with explicit delays; comparison to adLIF uses a deliberately hard (purely temporal) encoding where spiking models are known to be weak — the paper flags the mel-spectrogram confound itself.
- Energy analysis uses cycle/Joule models of chips (analytical), not hardware measurements.
- Single-seed-10 shallow-network theory; deep-architecture generalization argued by proxy ("if different on shallow, likely different on deep").

## Cross-links
- Related skills: [[controlling-the-latency-in-temporal-coded-spiking-models]] (DeNN latency control, same lineage), [[stdp-synaptic-delay-learning]], [[spora-binary-temporal-spiking-attention]] (UBS/BBS binary temporal codes), [[mdtf-temporal-fusion-local-snn]] (TTFS local learning), [[temporal-coding-thousand-brains-spiking]], [[spiking-sequence-machines-transformers]]
- Lineage: Maass 1997 (delays as computational resource) → SpikeProp/tempotron → TTFS closed-form (Mostafa/Comsa/Göltz) → DCLS (Hammouamri 2023, delays as dilated-conv kernel positions) → this paper's function-level taxonomy.

**Activation**: degree of temporal representation, temporal vs spatial gradient, delay neural network, DeNN, synaptic delay learning, TTFS coding, event-based dataset, spiking vs ANN taxonomy, softmin spike-time decoding, zero-loss SNN conversion, 时间表示度, 延迟神经网络
