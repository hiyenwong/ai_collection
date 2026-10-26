---
name: neuroml2loihi-celegans-loihi2
description: Use when porting NeuroML models to Loihi 2 neuromorphic hardware.
category: neuroscience
---

# NeuroML2Loihi — Standards-Based Neural Simulation on Loihi 2

**Paper**: "Small-scale neural simulation of Caenorhabditis elegans on Loihi-2 using NeuroML2Loihi" — Danny Rosen, Ramashish Gaurav, Yang Yi (Virginia Tech), arXiv:2610.25424 (18 Oct 2026, cs.NE). Code: github.com/DRosen766/NeuroML2Loihi (Zenodo DOI 10.5281/zenodo.21431945).

## When to Use
- Porting NeuroML/LEMS model descriptions to Intel Loihi 2 via Lava without rewriting models in hardware-oriented abstractions
- Benchmarking neuromorphic vs conventional (NEURON/CoreNEURON) simulation: latency, power, energy, on-chip memory
- Cross-platform fidelity assessment of spiking simulations (spike-train + voltage-trace metrics with Poisson baselines)
- Connectome-scale simulation of small organisms: first full 302-neuron C. elegans deployment on a single neuromorphic chip (contrast: Drosophila FlyWire ~140K neurons on 12 Loihi 2 chips, Wang et al. 2025)

## N2L Pipeline Architecture
1. **NMLParser**: .nml (neurons, synapses, stimuli, params) → `Network` (NetworkX graph: labeled neurons, weighted edges)
2. **LEMSParser**: LEMS .xml (duration, timestep, recorded neurons) → `Config`
3. **Mapping layer**: dict resolving NeuroML tag → Lava process (iafCell→LIF, expTwoSynapse→Dense); extensible via `register_mapping()` — separates parsing from Lava-specific choices
4. **Experiment**: SpikeBuffer input processes; recording via Monitor (simulator) or Dense routing-matrix→Receiver→StateProbe (hardware); voltage via StateProbe on the neuron process's `v` property
5. **Backend**: Loihi 2 hardware (NxCore, Kapoho Point single-chip board) OR LoihiSim CPU simulator — hardware NOT required to develop/run
6. **Analysis**: output .dat files mirror c302/OpenWorm format for direct cross-backend comparison; Van Rossum + Victor–Purpura spike distances; voltage cross-correlation (Elephant-based implementations)

## Deployment Facts
- **Vectorization**: ALL N neurons in ONE LIF process + ONE recurrent Dense synaptic process (adjacency matrix W from graph edge weights) — never one process per neuron
- Lava discrete-time LIF: u[t]=(1−du)u[t−1]+I[t]; v[t]=(1−dv)v[t−1]+u[t]+b; s[t]=H(v[t]−vth); reset v←0 on spike
- Grid-searched params: du=49, dv=8, vth=131071 (Loihi max → maximal subthreshold granularity), recurrent scale=320, input scale=4
- C. elegans model: c302 Parameter Set A; muscles excluded; PLML/PLMR (posterior touch receptor neurons) stimulated; 300 ms bio-time, dt=0.02 ms → 15,000 timesteps; weights = anatomical connection counts (integers)
- Three connectome scales: **Full** (302 neurons / 3119 synapses incl. gap junctions), **Active** (18/125, nonzero-voltage subset), **Minimal** (2 PLM neurons only)

## Fidelity Methodology (reusable)
- **Victor–Purpura distance** (q∈{1,50} s⁻¹; shift cost q|Δt|; q=50 ≈ PLM ISI ~16 ms at 63 Hz), **van Rossum distance** (causal exp kernel, τ=20 ms, normalized L2)
- **Poisson calibration**: score against rate-matched (63 Hz) homogeneous Poisson train; report ratio D(vs NEURON)/D(vs Poisson) — below 1 = better than chance
- Verified results: VP@1 ratio 0.2862 (1.0914 vs 3.8133), VP@50 ratio 0.4563 (5.5700 vs 12.2079), VR ratio 0.7252 (3.4194 vs 4.7154), |Δspikes|/neuron 1.0 vs 3.5
- ⚠️ pdftotext extracts this table COLUMN-MAJOR: 12 values = 4 rows × 3 cols read transposed; verify by division (each ratio = col1/col2 exactly) before trusting any transcription
- **Voltage affine mapping** (Eq 6) before comparison — platforms use different scales (Loihi integer vs NEURON mV): ṽ = g_rest + (v_HW − h_rest)·(g_θ−g_rest)/(h_θ−h_rest), anchored on rest/threshold pairs; then Pearson r (scale-invariant), MAE, RMSE
- Voltage fidelity < spike fidelity: PLM-only r=−0.1441 (oscillation phase offset), Active/Full r=0.4334; RMSE 8.83/3.94/0.235 mV. Spike-level behavior preserved; subthreshold differs because Lava LIF/Dense approximates NeuroML IAF/expTwoSynapse

## Benchmarking Methodology (reusable)
- **Latency**: on-chip execution window (power profiler) vs simulation-loop wall-clock (NEURON, excluding one-off generation+compile); normalize to Real-Time Factor RTF = T_wall/T_bio (RTF<1 = faster than biological real time)
- **Energy**: trapezoidal integration of sampled power rails over the execution window. Loihi: total chip power INCLUDING static draw. NEURON on Jetson AGX Orin (15 W mode, INA3221 rails ~50 Hz): dynamic only (30 s idle baseline subtracted) → **comparison deliberately conservative toward Loihi; reported advantage is a lower bound**
- **Memory**: Loihi2Memory profiler; per-core occupancy r_c = (1/5)r_small + (4/5)r_large of 192 KB neurocore; networks statically compiled → fixed footprint
- Protocol: 25 seeds × 3 scales, mean±std, 95% CI

## Headline Results (single Loihi 2 chip)
- Latency speedup vs NEURON/Jetson: **514× (Minimal) → 768× (Active) → 1211× (Full)**; N2L latency nearly scale-invariant (0.0243→0.0258 s) while NEURON grows (12.47→31.19 s) → advantage GROWS with scale
- Energy: N2L 0.0122–0.0131 J vs 11.65–28.52 J → 0.105%→0.0458% of reference (≈2183× at Full scale)
- Power: only 1.8–1.9× lower (0.505 W vs 0.92–0.98 W) — **energy advantage is latency-dominated, not power-dominated** (E = P̄·T with T collapsing)
- Memory (Full): 9 cores, 0.6571 MB, 38.94% occupancy; Active→Full: neurons ×16.8 but SRAM ×121 → **synaptic connectivity, not neuron count, is the scalability constraint** for biologically derived networks

## Pitfalls / Lessons
- Behavioral match across substrates REQUIRES per-model tuning (input scale, recurrent scale, du/dv) — no automatic derivation from NeuroML/LEMS yet; budget a tuning phase for every new model
- Never compare raw traces across integer/mV platforms: scale via input/weight scaling at deployment + affine voltage mapping at analysis
- Full-model RMSE can LOOK better because most neurons sit quiescent — segment metrics by active neurons before concluding fidelity
- Prior art gap filled: Loihi 1 C. elegans klinokinesis was a reduced circuit (not a full neuron set); PyNN/NIR/SNN-MLIR lack a direct NeuroML→Loihi 2 path; Brian2Lava lacks standards-based model deployment

## Related Skills
- [[snn-mlir-neuromorphic-compilation]] — NIR→bare-metal compilation (complementary IR-level approach)
- [[unifying-von-neumann-hpc-neuromorphic-ebbrains]] — transparent cross-platform SNN execution
- [[neuromorphic-satellite-snn-energy-model]] — SNN energy modeling on edge hardware
- [[quantization-snn-beyond-accuracy]] — quantized SNN evaluation methodology
