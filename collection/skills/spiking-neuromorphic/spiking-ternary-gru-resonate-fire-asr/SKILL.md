---
name: spiking-ternary-gru-resonate-fire-asr
description: Ternary MLGRU with resonate-and-fire spikes for ASR.
category: ai_collection
arxiv_id: "2610.29720"
trigger: spiking speech recognition, matrix-free SNN, ternary recurrent network, resonate-and-fire neuron, event-driven ASR, neuromorphic speech
---

# Spiking Ternary GRU (stGRU): Parallel Resonate-and-Fire + Ternary Recurrent Networks for ASR

Source: Poulos, Sadorf, Stafylakis & Anastassiou, "Bio-Inspired Auditory Processing: Coupling Parallel Resonate-and-Fire Dynamics with Ternary Recurrent Networks for Speech Recognition", arXiv:2610.29720 (cs.SD/q-bio.NC, 21 Oct 2026).

## Thesis

SNN ASR is bottlenecked by LIF neurons: membrane decay erases context across pauses and phonetic boundaries, and hard resets force sequential BPTT. stGRU separates WHAT the network stores (ternary weights) from WHAT it communicates (binary spikes from Resonate-and-Fire neurons), making the activation constraint a NATIVE TRAINING constraint rather than a deployment-time quantization. First matrix-MAC-free SNN without a learned ANN sequence decoder to reach single-digit WER on LibriSpeech.

## When to use

- Building energy-efficient speech/audio models for edge or neuromorphic hardware (avoid dense FP matrix MACs)
- You need event-driven communication trained end-to-end (spike constraint inside optimization, not bolted on)
- Studying how biological motifs (gated dendritic filtering before somatic spike generation, cortical hierarchical processing) map onto sequence models

## Architecture (per block, C channels, residual stream Z)

1. Ternary projections everywhere: T(V, W_f, gamma) with W_f in {-1,0,+1}^d and deferred-scaling per-tensor scale gamma. Depthwise ternary 1D convs (kernel up to K=63) + pointwise ternary mixing.
2. Ternary MLGRU gates (adapted from Zhu et al. 2024): C_t = SiLU(T_c(X_t)), F_t = sigma(T_f(X_t)), G_t = RMSNorm(T_g(X_t)); state update H_t = F_t ⊙ H_{t-1} + C_t ⊙ (1 − F_t) — strictly element-wise (NO dense W·h products), so associative parallel scan over sequence length replaces BPTT. Output O_t = T_o(G_t ⊙ SiLU(H_t)).
3. Channel mixing: ternary SwiGLU — U_t = SiLU(T_gate(O_t) ⊙ T_up(O_t)); Z_t = X_t + alpha ⊙ T_down(U_t) with learnable ReZero vectors alpha.
4. Residual stream: Z^(l)_t = RMSNorm(Z^(l-1)_t) + alpha ⊙ RMSNorm(Z'_t) (variance stabilization across depth).
5. PRF spike neuron (below) converts the stabilized residual Z into the binary input of block l+1.

## Parallel Resonate-and-Fire (PRF) neuron

The key trick: fold the spike RESET into a complex-valued decay, so membrane integration becomes spike-independent and globally parallelizable.
- Complex decay rate: gamma_tilde = −1/tau + i·theta (damped oscillator; tau = membrane time constant, theta = subthreshold oscillation frequency).
- Discrete update (Euler, step Delta): U_t = A · U_{t-1} + Delta·Z_t, with A = exp(Delta·gamma_tilde) = e^{−Delta/tau}(cos(Delta·theta) + i·sin(Delta·theta)).
- Spike emission: strictly on the REAL component, S_t = H(Re{U_t} − V_th). (No reset subtraction: LIF's Vth·S_{t-1} term is what breaks parallelism; RF keeps it inside the rotating decay.)
- Global FFT evaluation over the whole sequence: U_{1:T} = F^{-1}(F(Z_{1:T}) ⊙ F(K_{1:T})), decay kernel K_t = Delta·A^t. O(T log T) instead of O(T²) BPTT. (pdftotext garbles eq. 11's exponent placement; the form above is re-derived from the paper's own A = exp(Delta·gamma_tilde) definition.)
- Training: Multi-Gaussian surrogate gradients (Yin et al. 2021) on the Heaviside interface; the next block is optimized on the SAME discrete spike stream used at inference.

Why RF over LIF for speech: LIF decay erases information across silences/phonetic boundaries; RF's subthreshold oscillation retains phase-locked information and provides a band-pass temporal filter matched to speech dynamics (cf. cortical separation of nonlinear dendritic filtering and somatic integration, Gidon 2020, Hausser & Mel 2003).

## Train-time dual discretization

- Weights: ternary {-1,0,+1} (+scale) — discretize storage, remove dense FP MACs (7.4-10.8x memory cut; FP32->ternary costs 5.83->6.49% WER but modeled energy 33.48->4.10 mJ/s).
- Activations: RF binary spikes — discretize communication, learned during optimization (not a post-hoc activation quantization step as in MLGRU/Loihi-2 deployments).
- Discrete PRF spikes BEAT continuous ternary ReLU activations on both WER and energy at Large scale (6.14% @ 3.42 mJ/s vs 6.49% @ 4.10 mJ/s; FP32 ReLU: 33.48 mJ/s).

## Recipe (reproducible pipeline)

- Input: 80-dim log-Mel filterbanks @ 50 Hz -> ternary 2D CNN frontend (512/1024 ch) with 4x temporal subsampling -> MLGRU + PRF pre-encoder emitting spikes at 12.5 Hz -> stGRU backbone (depthwise K<=63 across 1024 channels) -> CTC loss with Semi-Resonant Cosine Annealing. SpeechBrain toolkit, 8x AMD MI250X (LUMI).
- Sizing: Small / Medium / Large.

## Results (standalone acoustic model, no external LM)

| Model | test-clean WER | Energy | Memory |
|---|---|---|---|
| stGRU Small | 8.09% | 1.95 mJ/s | (INT2 ternary) |
| stGRU Medium | 7.04% | — | — |
| stGRU Large | 6.44 ± 0.17% (6-seed) | 3.42 mJ/s | 122.22 MB (LibriSpeech) / 167.84 MB (Aishell-1) |
| + optional 4-gram LM (CPU hash, non-neural) | 5.95 ± 0.16% | excluded from neural profiling | — |
| Streaming variant (320 ms look-ahead) | 9.11% | 3.51 mJ/s | — |
| Aishell-1 (Mandarin, from scratch) | 10.88% test CER / 9.28% dev | — | — |

References: Transformer 112M 8.80 mJ/s, Conformer 136M 11.28 mJ/s, hybrid IML-Spikeformer 17.18 mJ/s. Energy model: 45 nm CMOS constants — 4.6 pJ/FP-MAC, 0.9 pJ/sparse-AC, 17.5 pJ/PRF-update (Horowitz 2014; Huang et al. 2024).
Training speed: 3.1-3.4x faster than parameter-matched LIF variants (associative scan + FFT vs sequential BPTT).

## Emergent cortical-like internal dynamics

- Depth-graded hierarchy: shallow layers = fast acoustic filters; deep layers = slower semantic integrators. Latents progressively disentangle into part-of-speech manifolds (verbs/nouns/pronouns) and word-level spike events (Rastermap-sorted superneuron heatmaps + UMAP).
- Firing rates: lognormal distributions with a depth-wise sparsity gradient, mirroring human cortex in vivo.
- Layer L11 autonomously develops ACC-like error monitoring: incorrect words trigger elevated firing, peak sparsity 0.83, heavy-tailed lognormal rates (Delta R^2 = +0.091 over Gaussian).
- Layer L14 inverts into PFC-like commitment: high-confidence correct words elicit peak firing, sparsity drops, distributions shift Gaussian — an autonomous ACC->PFC-like functional handoff inside ONE sequence model.
- Ablation: removing MLGRU gating collapses deep-layer outcome selectivity by 95.5% (vs 8.1% full model, empty-emission controlled) — gating, not spiking per se, carries the semantic outcome coding.

## Pitfalls

- The ternary GRU backbone retains CONTINUOUS activations internally; only the inter-block pathway is binary (that is the design — storage vs communication split).
- CTC head is FP32 ("ternary SNN + FP32 CTC") — the output layer is not part of the matrix-MAC-free claim.
- Single-digit WER claim is vs matrix-MAC-free SNNs WITHOUT learned ANN sequence decoders; dense ANN models (Conformer etc.) are still better in absolute WER.
- Energy numbers are MODELED arithmetic costs from CMOS constants, not measured hardware draws.
- Cross-lingual transfer shown on Mandarin (Aishell-1) but below the strongest dense/hybrid systems there.
