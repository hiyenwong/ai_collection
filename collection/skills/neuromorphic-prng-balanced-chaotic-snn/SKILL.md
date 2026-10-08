---
name: neuromorphic-prng-balanced-chaotic-snn
description: Chaotic balanced SNN as low-power pseudo-random number generator (NPRNG). Binarized/quantized LIF networks, spike-chaos vs rate-chaos regime selection, dynamic lookup-table bit transform, NIST/Dieharder validation, FPGA implementation at 3-5 mW.
category: ai_collection
version: "1.0.0"
source: arXiv:2610.00719
source_title: "Neuromorphic Pseudo-Random Number Generators with a Low Power Hardware Implementation"
authors: "Jafar Shamsi, Navid Akbari, Sonia Sennik, Aaron Gruber, Wilten Nicola (Hotchkiss Brain Institute, University of Calgary; CDL)"
published: 2026-09-30
categories: "cs.NE, nlin.CD"
trigger_words:
  - pseudo-random number generator
  - PRNG
  - neuromorphic PRNG
  - balanced network chaos
  - spike chaos
  - rate chaos
  - LIF network FPGA
  - NIST SP-800-22
  - entropy source hardware
  - stochastic computing
  - edge computing randomness
  - reservoir computing dual use
---

# Neuromorphic PRNG: Balanced Chaotic Spiking Networks as Randomness Engines

**arXiv**: 2610.00719 (30 Sep 2026) · Shamsi, Akbari, Sennik, Gruber & Nicola, U Calgary.
**Hardware**: Lattice iCE40UP5K FPGA, N=256 LIF neurons, 3.24 mW (FPGA only) / 5.45 mW (board measured), 120 kbps.

## Core Idea

Brain-inspired chaos is a cheap entropy source: a **balanced E/I spiking network** in the *spike-chaos* (Poisson-like irregular firing) regime produces statistically independent spike events; a tiny dynamic lookup table converts the spike-time sequence into a bitstream that passes the full NIST SP-800-22 battery at rates matching LCG, BBS and Mersenne Twister — with zero multipliers, weights stored as single bits, and reconfigurability of O(2^N²) unique generators.

## Network Model (hardware-friendly balanced state)

LIF neurons with double-exponential synapses:
```
τm·v̇i = −vi + Σj wij·rj(t) + I + wi·c(t)      (input c(t) used as streaming seed)
ṙj = −rj/τd + hj
ḣj = −hj/τr + Σ δ(t−t_jk)/(τr·τd)
```
Balanced regime: E(wij)=0, E(wij²)=g²/N. Hardware modifications that **do not** destroy the chaos:
- **Weight binarization**: wij = ±g/√N, each neuron receiving exactly N/2 positive and N/2 negative weights (moment conditions hold exactly per neuron).
- **Power-of-2 quantization**: all parameters of form ±2^k → all multiply operations become shift-and-add; multiplier-less datapath.
- Validation: ISI CV ≈ 0.99 (binarized, N=256) / 0.68 (quantized) — Poisson-like; single-spike deletion and single-weight flip both decorrelate the trajectory (chaos + parameter sensitivity).

## The Two Regimes — Select Spike-Chaos, Avoid Rate-Chaos

| Regime | coupling g | firing statistics | PRNG quality |
|---|---|---|---|
| **Rate chaos** | too large | long-timescale rate autocorrelation, bursts | POOR — serial correlations survive the transform |
| **Spike chaos (use this)** | large but < critical | isolated Poisson-like spikes, flat autocorrelation, weak cross-correlations | passes NIST; bitstreams ≈ independent Bernoulli(1/2) |

NIST pass count correlates strongly negatively with mean ISI CV (ρ = −0.8147): map the (g_q, τ_D) plane — g_q = 2^-j, τ_D = 2^-i grid — and stay in the low-CV Poisson-like region. N ≥ 128 required (N<64 admits stable non-chaotic attractors with sizable basins; verified by max-Lyapunov estimation).

## Bit Extraction: Dynamic Lookup Table Transform

**Naive transform fails**: emitting the k-bit binary index of each firing neuron (N=2^k) inherits each neuron's relative refractory period → NIST-detectable non-randomness.

**Working transform** (O(1) logic, history-accumulating):
```
y_n = mod(y_{n−1} + s_n, N)        # s_n = index of neuron firing n-th spike
b_n = L(y_n)                       # L: static N-bit table, N/2 zeros + N/2 ones, random permutation
```
The accumulator mixes network-wide spike history and destroys per-neuron refractory structure. (w, w_in, L) jointly define a generator instance.

## Validation Results
- Single weight matrix × 65,536 input seeds, 10^8 bits each: ~50% of seeds pass **all 15 NIST tests**, ~40% pass 14/15.
- 10^4 random weight matrices: ~half pass all 15; none below 10/15. But a "balanced" matrix with *correlated* weights can satisfy the moment conditions and still be poor — independence of wij is essential; NIST-screen instances in practice.
- Baseline comparison: quadratic congruential and mod-exp PRNGs fail everywhere; LCG, BBS, Mersenne Twister, quantized and non-quantized NPRNG all comparable.
- **Dieharder** initially flags short-range serial correlations (sts_serial, rgb_lagged_sum, sts_runs) in a subset of raw bitstreams — fix with XOR whitening: non-overlapping pairwise decimation b ← b_2i ⊕ b_2i+1. One pass insufficient, **two passes eliminate** systematic failures, three passes leave only chance-level flags. **TestU01 SmallCrush**: 100/100 configurations pass.
- Cycle risk (discretized chaos): 1.1 TB generated, no repetition found; birthday-bound estimate for N=256 @32-bit precision ≈ 2^12000 expected cycle time — negligible.

## Seeding & Reconfiguration
- **Seed options**: (a) N-bit seed → bit j sets neuron j super-threshold (1) or v_reset (0); (b) streaming input signal c(t) with binary input weights w_in=±1 (O(N) storage) — same constant initial state, different trajectories per input; long-enough shared c(t) also **synchronizes** two NPRNGs (stable-chaos property).
- **Reconfiguration**: disable neurons via inhibitory bias (I ≪ v_th) → different chaotic trajectory, statistics unchanged; NIST passes retained down to >128 active neurons.
- Uniqueness: O(2^(N²)) distinct generators from weight bits; same hardware block doubles as a **reservoir computing** accelerator (low-rank perturbation stabilizes dynamics).

## FPGA Microarchitecture (iCE40UP5K, 6 MHz)
- Synaptic multiply→MUX + add (spike event = multiplexer select, no DSP). Tree-adder spatial parallelism + 2/5/5-stage pipelines in h[n]/r[n]/v[n]. Resource-sharing time-multiplexes blocks (throughput ÷ N, compensated by pipelining, 1 neuron/clock).
- 32-bit fixed point (16.16), truncation rounding; constants exact powers of 2.
- 76% SLICEs for N=256; 25 BRAMs (weights 1 bit each via CONVERT block, LUT, states). Spike rate ≈ 1/50 per clock → 120 kbps @ 6 MHz; UART 5-bit chunks.
- Measured: 1.65 mA @ 3.3 V = 5.45 mW board; 3.24 mW FPGA-only (Lattice Radiant). Energy ≈ 27.16 nJ/bit (vs BBS 10.48 nJ/bit but BBS at 24.5 mW; LCG 0.13 nJ/bit at 36.8 mW — NPRNG wins on absolute power, not per-bit energy).
- Hardware bits → Monte-Carlo π estimate 3.1413 from 2.2M samples.

## Security Posture (honest framing)
Statistical randomness: proven (NIST/Dieharder/TestU01). Unpredictability: structural sensitivity to single-spike/single-weight perturbation. State secrecy: many-to-one output transform helps, but **no formal proof of cryptographic security, side-channel or fault-attack resistance** — positioned as a *statistical* RNG for stochastic computing / probabilistic inference / edge AI, not yet as a CSPRNG. Large key (O(N²) weight bits) and parallel localized integration raise side-channel difficulty vs AES-style secret-dependent serial computation. Natural next step: analog/memristive **NTRNG** (true randomness from device noise) and SNN-based PUFs.

## Implementation Checklist
1. N=256 LIF, τm=20 ms scale; weights ±g/√N binarized, exactly N/2 of each sign per neuron; quantize all constants to powers of 2.
2. Sweep (g_q, τ_D) on a power-of-2 grid; select the low-CV (µ_cv ≈ 0.7–1.0) Poisson-like region; verify max-Lyapunov > 0; reject N < 128.
3. Emit bits via accumulator + lookup table (never raw spike indices).
4. NIST SP-800-22 (100 × 10^6 bits) per instance; keep only instances passing 15/15.
5. Apply 2–3 passes of XOR pairwise decimation before Dieharder.
6. Seed via N-bit initial-condition vector or streamed input through binary w_in; reconfigure by inhibitory neuron disabling.
7. Budget: ~5 mW / 120 kbps on iCE40-class FPGA; expect 10-100× bandwidth gains in ASIC/neuromorphic-processor ports.

## Related Skills
- `predictable-mean-field-chaos-rnn` (balanced-chaos mean-field theory, stable chaos)
- `chaotic-topological-preictal-eeg` / `nca-deltarule-fast-memory-adaptation` (chaotic SNN regimes)
- `stochastic-computing-snn-accelerator` (stochastic computing consumer of the bitstream)
- `noise-assisted-rare-event-simulation` (deterministic chaos as internal randomness source)
