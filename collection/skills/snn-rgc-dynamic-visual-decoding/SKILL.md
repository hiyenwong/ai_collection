---
name: snn-rgc-dynamic-visual-decoding
description: Use when decoding spikes to video/tracking or SNN energy.
---

# Spike-Native Dynamic Visual Decoding from Retinal Ganglion Cell Populations

Methodology from arXiv:2610.17154 (Zhang & Nurmikko, Brown University, 12 Oct 2026, cs.ET/cs.LG/eess.SP): the first end-to-end spiking neural network that reconstructs **dynamic, moving visual scenes** and simultaneously tracks target position, entirely in the spike domain, from ex vivo mouse retinal ganglion cell (RGC) populations (up to 1836 cells on HD-MEA). Compact (~5.4M params) and ~70x lower compute energy than the ANN-equivalent.

## When to use

- Decoding neural population spikes (MEA/probe recordings) into time-varying stimulus estimates — especially moving targets, where single-frame decoders fail
- Joint "what + where" (reconstruction + tracking) from one shared encoder
- Energy-budgeted decoder design for implantable/wearable interfaces (visual prostheses, BCI front-ends)
- SynOps-based energy accounting and SNN-vs-ANN decoder benchmarking

## Core methodology

1. **Input rasterization (Gaussian splatting)**: place each cell's firing rate at its measured receptive-field center, spread with an isotropic 2D Gaussian (sigma = 0.5 grid px, unit mass per neuron), SUM where RFs overlap; channels = response polarity (ON / OFF / ON-OFF) -> input tensor [T x 3 x 32 x 32]. Sub-pixel RF positions are preserved; hard-snapping to the nearest grid pixel loses them. Polarity separation contributes more to quality than raw cell count (ON cells dominate decoding).
2. **Shared spiking encoder**: SEW-ResNet spiking U-Net (LIF/IF neurons, surrogate-gradient training, SpikingJelly). Three downsamples 32->16->8->4, widths 48/96/192/384. Optional MA-SNN attention front-end re-weighting channel/spatial/temporal axes. In depth a feedforward hierarchy, in time a stateful integrator (membranes carry across bins; same weights each step).
3. **Reconstruction readout**: a single high-threshold (Vth=5000) **non-firing** analog-membrane output neuron; image = sigmoid(V[t]); **temporal-fusion readout** learns a softmax weighting over per-timestep membranes (zero-init bias reproduces last-timestep readout, then redistributes weight to informative moments) — this is what carries dynamic reconstruction past the last-timestep baseline.
4. **Tracking readout**: spike-count (leaky) centroid + bounded learned regression offset s*tanh(g(F)), s=0.5, g zero-initialized -> starts as the exact centroid and learns only a correction. LIF pre-integration (tau=6 bins) suppresses frame-to-frame jitter ~10x. Train against the TRUE trajectory shifted +250 ms (retinal response latency), masked to valid bins.
5. **Loss**: L = L_BCE + L_SSIM + L_IoU (equal weights; SSIM window 3 for small targets, 11 for 512-px images); AdamW lr 1e-3, wd 1e-4, fp16 autocast. Firing-rate penalty lambda*r̄ exposes energy as a trainable knob: L = L_recon + lambda_track*L_track + lambda*r̄.
6. **Energy accounting**: SynOps = Sum_l f_l * Sum_t ||S_l[t]||_0 (layer fan-out x spike counts; silent units cost nothing). 45 nm convention: MAC 4.6 pJ vs AC 0.9 pJ. ~70x = 13.6x (spike sparsity at 14.2% mean firing) x 5.1x (AC vs MAC). Report compute-only; memory movement excluded.

## Key results (sanity anchors)

- Flashed images (1836 cells, up to 512 px): masked-SSIM 0.81 natural / 0.88 synthetic
- Moving bars SSIM 0.93; drifting gratings 0.80 (faithful <=4 Hz, fails at 15 Hz); randomly moving digits 0.80 +/- 0.07
- Reconstruction sharpens over the clip as membranes integrate evidence (SSIM ~0 -> 0.80 over the 1.6 s motion phase) — temporal evidence accumulation, not one informative frame
- Tracking: 1.33 px mean error (32-grid) vs calibrated COM baseline 2.91 px vs chance 9.10 px — learned spiking readout roughly halves the classical readout's error
- Fidelity SATURATES across 18 architectures (masked-SSIM 0.80–0.82 over 5.9M–1.7B params): data-limited regime, not capacity-limited — stop scaling the decoder, get richer data
- 5.4M params vs spiking transformers QKFormer 33M / Meta-SpikeFormer 59.8M at equal fidelity
- lambda=0.1 firing penalty: -21% SynOps (70x -> 88x) at SSIM 0.80 -> 0.73; the penalty lowers firing where fan-out is largest (decoder) and may raise it in small heads — **the spike count, not the mean rate, is the relevant knob**

## Pitfalls / lessons

- Adaptive-threshold (SFA) neurons did NOT improve over plain LIF/IF — at this data limit the neuron model is not the bottleneck
- Coupling the two tasks (soft Gaussian gate / warp re-registration) gave no gain; keep readouts independent on a shared encoder
- Single-frame decoders fundamentally cannot handle randomly moving targets — the capability comes from the stateful membranes' temporal memory, not preprocessing
- Use masked-SSIM when the background dominates; match SSIM window to target size
- Energy claims: decompose the sparsity term (process-node-independent, conservative) from the per-op term (node-dependent); never claim wall-plug power from SynOps alone
- Read reconstruction from accumulated membrane potential, not spike counts — binary spikes cannot carry graded intensity by amplitude

## Related

- [[spike-image-decoder]] — ANN predecessor (static frames, dense compute)
- Event-camera SNN reconstruction/tracking work (robotic vision) — this paper's substrate is living retina with trial-to-trial variability
- Code: github.com/nzhang1218/snn_rgc_decoding
