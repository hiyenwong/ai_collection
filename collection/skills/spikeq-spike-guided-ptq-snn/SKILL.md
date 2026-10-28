---
name: spikeq-spike-guided-ptq-snn
description: Use when PTQ-ing SNNs; pick levels by flipped spikes.
trigger: SNN post-training quantization, neuromorphic chip deployment, membrane potential quantization, low-bit SNN, spike error minimization, PTQ4SNN, SpikeQ
category: ai_collection
---

# SpikeQ — Spike-Guided Post-Training Quantization for SNNs

Source: arXiv:2610.23046 (Sun, Duan, Yan, Zhang, Huang, Kuhlmann — Monash/NEU/NUS, announced Oct 2026). PTQ framework that quantizes BOTH synaptic weights and membrane potentials of a pretrained SNN without retraining, guided by the spikes an error flips rather than by MSE.

## Core Empirical Law (why MSE fails)

Accuracy loss tracks the **fraction of flipped spikes**, not error magnitude. Injecting equal-MSE errors into a full-precision SNN (PreAct-ResNet18/CIFAR-100, T=4):

- Constant input-current error +0.2θ at every step keeps pushing the membrane up → flips spikes → large accuracy loss. Zero-sum ±0.2θ error has the SAME MSE but cancels over time → almost no loss.
- Reversing a membrane error's sign whenever it would cross θ keeps MSE unchanged but removes the accuracy drop.
- Plotted against flipped-spike fraction, all curves merge: Spearman(flips, accuracy) = −0.99 vs Spearman(MSE, accuracy) = −0.77.

**Rule: an SNN quantization objective must minimize the spikes it changes.** An error far from θ flips nothing; a tiny error near θ flips a spike that propagates to later steps and layers.

## Setup

LIF: `Vt = (1−1/τ)·Ut−1 + It/τ`, `St = 1[Vt ≥ θ]`; hard reset `Ut = Vt(1−St)`, soft reset `Ut = Vt − θ·St`. Benchmarks use T=4 steps; SEW-ResNet-18 uses IF neurons, others LIF.

## Stage 1 — Weight Quantization (spike-count objective)

For layer ℓ, compare each downstream neuron's quantized spike count N̂ᵢ against TWO references:

- `N_i^FP`: count from the original full-precision network (global correctness)
- `N_i^loc`: count from full-precision weights W^ℓ applied to the ALREADY-QUANTIZED input spikes S^ℓ−1 (accumulated-error realism)

Loss = **count + margin + population** terms:

1. `Lcount = ρ·Σᵢ|N̂ᵢ−N_i^FP| + (1−ρ)·Σᵢ|N̂ᵢ−N_i^loc|` — blend global and local references; ρ=0.5 at W2, ρ=0.25 at W3/W4.
2. `Lmargin = ρ·M^FP + (1−ρ)·M^loc`, where `M = Σ_{wrong spikes} |V̂ᵢ,ₜ − θ|` — distance of each wrong spike from being corrected. Tie-breaker when a one-level move changes no count; removing it costs up to 5.29 pts on complex tasks.
3. `Lpop = Σᵢ(N̂ᵢ − N̄ᵢ)`, `N̄ᵢ = ρN_i^FP+(1−ρ)N_i^loc` — extra vs missed spikes give identical |·| errors; this keeps the layer's TOTAL spike output balanced. Critical for segmentation (−3.2 mIoU if removed); irrelevant on CIFAR-10.

`L = Lcount + λ·Lmargin + µ·Lpop`, λ=1, µ adapted per sweep: `µ ← clip(µ + 0.5·Lpop/(Lcount+λ·Lmargin), −0.9, 0.9)`. Keep |µ|<1 so population balancing never outweighs fixing one neuron's spike.

### Discrete search (no gradient through spikes)

- **Phase 1**: decide weights one input at a time (all neurons at once), LARGEST input current first. Each weight picks among its FOUR nearest levels `{⌊q̄⌋−1, ⌊q̄⌋, ⌈q̄⌉, ⌈q̄⌉+1}` (q̄=w/Δw) — the spike-optimal level often lies beyond the two nearest. Undecided weights are modeled as uniform rounding noise ε∈[−Δw/2, Δw/2], 4 draws, score by mean loss.
- **Phase 2**: ≤6 sweeps of ±1-level moves kept only if they lower L. 25% of calibration images held out; any channel whose held-out loss rises after a sweep is restored and frozen (anti-overfit).
- Per-output-channel grids. Clipping searched by min-L2.4 weight error (shared with BRECQ/PTQ4SNN). Non-spiking layers (classifier head) fall back to output error `Lout = Σₜ ∥(W−Ŵ)·Sₜ∥²`. On COCO, keep first layer + detection head at 8-bit RTN.
- Calibration: 1024 unlabeled images (weights), 256 (membrane); segmentation samples 16,384 neurons/image/layer. Seed-stable: 90.52±0.19 on CIFAR-10 W2.

## Stage 2 — Membrane Quantization (pre-fire, threshold-anchored)

**Key hardware mismatch**: neuromorphic chips (Loihi, Speck) store the membrane potential at fixed bit width and compare the STORED value with θ — quantization happens BEFORE the firing decision. Most prior methods quantize the post-reset state, so firing still sees full precision. Under pre-fire quantization their grids collapse at V2 on all seven benchmarks (0.05–27% vs full precision).

### Threshold anchoring (the load-bearing component)

Place θ EXACTLY midway between two adjacent levels → θ is a rounding boundary:

`gⱼ = θ + (j − n + ½)·Δv`, j = 0..K−1, with n of the K levels below θ.

Then `1[Qv(V) ≥ θ] = 1[V ≥ θ]` for ANY Δv and n — **rounding can never flip the current spike**. Without anchoring (a level AT θ), potentials within half a step below θ round UP to θ and fire spuriously: −8 to −51 pts, total collapse on every hard-reset benchmark. Ablation: anchoring is what prevents the collapse, nothing else.

### Reset-aware step rule (post-reset state stays on grid)

- **Hard reset** (U=0 after spike): make 0 a level; keep exactly ONE level above θ (n=K−1); `Δv = θ/(m+½)` with m levels in [0,θ). Calibration keeping one level above θ loses nothing vs free choice.
- **Soft reset** (U=V−θ): the above-θ excess carries forward, so keep several levels above θ and make θ a whole number m of steps: `Δv = θ/m` → subtracting θ maps level gⱼ → gⱼ₋ₘ, which is again a level. No second rounding on the stored state.

### Grid calibration by spike mismatch, never membrane MSE

Enumerate all (m,n); record each layer's input currents with earlier layers already quantized; simulate every neuron full-precision vs candidate grid; keep the grid minimizing `Lv = Σᵢ,ₜ |Ŝᵢ,ₜ − Sᵢ,ₜ|`.

Why not MSE: under hard reset the membrane MSE is dominated by negative potentials far from θ, whose rounding flips nothing → MSE picks a coarse step that rounds just-below-θ potentials to zero → their neurons MISS spikes at the next step. Replacing Lv by MSE among the same candidates costs up to 40.22 pts.

**Per-channel caution (SpikeQ†)**: per-channel grids win up to +0.90 mIoU on segmentation but FAIL on SEW-ResNet-18 V2 — some first-layer channels chose grids with NO level between 0 and θ, so sub-threshold potentials round to 0 and can never accumulate (−73% spikes in those channels). Rule: early/first layers need at least one level in (0,θ); layer-wise grids are the safe default.

## Results (7 benchmarks, T=4)

Classification (CIFAR-10/100 PreAct-R18; ImageNet SEW-R18 + Spike-driven Transformer), segmentation (SDT-V2 + spiking FPN, VOC/ADE20K), detection (EMS-YOLO R34, COCO).

- **W4**: within 0.28 pts of the best method on every benchmark. **W2**: best on 6/7; on SDT more than doubles the strongest baseline (45.76 vs 22.21).
- **V2 pre-fire**: every existing grid collapses (MinMax/MSE/SQUAT/FlowQ-M/PTQ4SNN-M); SpikeQ retains most of FP (e.g., SDT-V2 VOC 69.71 vs FP 70.86). Mechanism: in un-anchored grids the band between θ and the nearest level (up to half a step wide) flips spikes in every layer and time step at 2 bits.
- **W4V4**: ≤2.59 pts from full precision everywhere, footprint 7.8–7.9×, energy 6.4–6.9× lower. **W2V2**: 15.1–15.7× footprint but complex tasks collapse (SEW 15.85 vs 62.89) — at 2 bits both stages still flip spikes and errors compound.
- Energy model `EC = Ecompute + Ememory + Eneuron`: weight READS dominate FP energy, so energy gains come almost entirely from weight quantization; membrane bit width only enters the small neuron term.

## Design Rules (transferable)

1. Optimize SNN quantization by flipped-spike count against dual references (full network + local recompute on quantized inputs); MSE/current-error objectives are proxies that fail at ≤2 bits where the step is coarse and WHERE the error lands is all that matters.
2. Anchor the firing threshold on a rounding boundary whenever a stored value decides the spike — this makes rounding spike-safe by construction, independent of step size.
3. Match the grid to the reset rule so the stored post-reset state needs no second rounding.
4. Gains grow with task complexity (coarse-class CIFAR-10 tolerates flips: top-4 methods within 0.19 pts at W2; fine-grained ImageNet/ADE20K benefit most). 2-bit only pays off on simple tasks under tight memory; complex tasks need 4 bits.
5. Always keep levels in (0,θ) so sub-threshold membrane potentials can accumulate.

## Activation

spikeq, SNN PTQ, flipped spikes, membrane quantization, pre-fire quantization, threshold anchoring, neuromorphic deployment, low-bit SNN, spike-count objective
