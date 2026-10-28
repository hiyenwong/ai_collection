---
name: neuromorphic-satellite-snn-energy-model
description: Satellite and edge SNN energy model with bounded STDP.
trigger: neuromorphic satellite, SNN energy budget, onboard inference, event-driven attitude estimation, telemetry anomaly detection SNN, EAL trade-off surface, radiation-aware neuromorphic architecture
---

# Neuromorphic Satellite Intelligence Framework (arXiv 2610.12471)

Formal framework for event-driven spiking computation under satellite constraints: fixed power/mass/radiation budgets vs monotonically growing mission intelligence needs. Reusable for ANY edge deployment with hard energy ceilings (drones, IoT, implants), not just satellites.

## 1. Closed-Form Energy Model

E_total = N·r·T·F·(ε_SOP + ε_read) + P_leak·T

- N neurons, F avg fan-out, r mean firing rate (spikes/s), T inference window
- ε_SOP: energy per synaptic op; ε_read: per-weight SRAM read energy
- Scales as **O(α·N·F)** where α = activity fraction (T·r/T_max)

Key insight: energy is proportional to **total spike count rT**, not to model size. Satellite workloads have r ≈ 2–5 spikes/s/neuron vs 50–200 Hz in active cortex — sparsity α is the primary efficiency lever.

Worked example (α=0.02, N=64k, F=50, ε_SOP=12pJ@180nm-rad-hard, ε_read=8pJ, T=1ms): E_total ≈ 1.54 µJ per inference.

Radiation overhead: N_SEU = λ_SEU·B·T corrupted bits per window (LEO 600km, 2mm Al: λ_SEU≈10⁻⁸/bit/day). TMR fault-tolerant energy: E_FT = E_total + 3·N_SEU·ε_TMR·B. Negligible for short windows; material over 5+ year missions.

## 2. Radiation-Aware Architecture Taxonomy (4 classes)

| Class | Rad strategy | Hybridization | Learning | Target |
|-------|-------------|---------------|----------|--------|
| Rad-Neu | TMR + rad-hard SRAM, majority-vote spike aggregation (Δt_sync≈50ns) | pure SNN | offline only | deep space |
| NeuHybrid | partial TMR + SEFI scrubbing | SNN + FPGA/Rad-hard RISC-V | supervised fine-tune | LEO/MEO |
| DEC-Node | redundant spike paths | SNN + comms ASIC | federated STDP | constellations |
| NeuroSoC | process-level hardening | SNN + DSP + RISC-V SoC | full on-orbit STDP | GEO |

NeuHybrid runtime partition rule: assign(task) = SNN if s(task) > θ_s (=0.15 empirically) ∧ ℓ(task) < t_hard, else CPU. Preserves deterministic timing for control loops on conventional hardware.

DEC-Node: encode observations as temporal-contrast spike events, transmit only significant events; distributed spike-majority consensus in O(log N_sat) rounds → 15–40× inter-satellite link reduction.

## 3. Three Event-Driven Algorithms

### SKCF — Spiking Kalman-Complementary Filter (attitude estimation)
Replaces continuous KF with event-driven updates triggered only when |ω(t)−ω̂(t)| > δ_ω (gyro) or quaternion change > δ_q (star tracker). Recurrent membrane state holds q̂; on each spike: quaternion propagation + covariance propagation; on star-tracker spike: 4×4 Kalman gain correction with complementary gain λ. Amortized cost O(64·r_ev)≈O(32) flops/s in quiescent mode vs O(6400) for 10ms-period KF → **~200× compute reduction** nominal.

### TCAD — Temporal Contrast Anomaly Detector (health monitoring)
Telemetry channel i spikes when |x_i(t)−x_i(t−Δt)|/σ_i > θ_TC. Two-layer SNN (offline-trained on nominal telemetry) updates ONLY on spike arrival; zero dynamic energy when quiescent (no spikes ⇒ no computation ⇒ no energy). False-spike analysis: θ_TC=3.5, 256 channels, Gaussian noise → p_false=2(1−Φ(3.5))≈4.7×10⁻⁴/channel/sample.

### SAMC — Spike-Based Adaptive Modulation & Coding (cognitive links)
512-neuron echo-state reservoir (ρ(W_R)=0.9) over sparse channel events (phase/SNR/Doppler spikes); softmax readout → MCS index. **Hold-last-valid** on no-spike intervals (valid because channel coherence >100ms ≫ max inter-spike interval). GEO case study: +6.4% throughput vs static MCS, +2.1% vs conventional AMC, 58.3% energy saving vs DSP-based AMC.

## 4. Constrained STDP (bounded drift, safety-critical)

Δw_ij = +A⁺·exp(−|Δt|/τ⁺)·(w_max−w_ij)/w_max   if Δt>0
Δw_ij = −A⁻·exp(−|Δt|/τ⁻)·w_ij/w_max            if Δt≤0

Multiplicative saturation factors ⇒ drift bound: E[|dw_ij/dt|] ≤ (A⁺τ⁺ + A⁻τ⁻)·r_pre·r_post. With A±=0.01, τ±=20ms, r=10Hz: ≤4×10⁻³ w_max/s. Supervisory gate halts STDP during critical maneuvers or battery SoC <30%.

## 5. EAL Trade-off Surface
Pareto-optimal (Energy, Accuracy, Latency) points by sweeping N, r, encoding precision B_enc. Observations: accuracy sub-linear in N above ≈4k neurons; energy linear in r (controlled by event threshold δ_ω); latency minimized at intermediate N (propagation depth vs parallelism).

Balanced design point (N=16k, r=2Hz): 97.8% accuracy, 18.3 µJ, 4.1ms latency.

⚠️ **Quality caveat (honest reporting)**: the paper's headline multipliers are internally inconsistent — abstract claims 8–47× over GPU, Table II shows ~3700–4000×, text says 7751×. The energy formula and architecture are sound; the multipliers are not. Re-derive from the energy formula with your own ε_SOP/ε_read for your process node before citing any speedup.

## 6. Case Study Patterns
- **12U CubeSat EO (2W budget)**: event imager → 2.1×10⁵ spikes/scene vs 3.1×10⁷ pixels (148× compression); TCAD at 10Hz = 12.8µJ/inf = 0.023% daily budget; spike-based tile filtering cuts downlink 91% (14.2→1.27 GB/orbit).
- **Deep-space probe (RTG 220W, 10yr)**: SKCF event-driven correction latency 18ms vs 100ms polled-KF → 41cm positional accuracy gain at 5m/s terminal descent.

## When to Use
1. Sizing an edge/SNN deployment against a hard joule budget → start from E_total formula, pick α/r/F targets.
2. Deciding hybrid partition (what goes to SNN vs CPU) → sparsity-threshold rule.
3. Event-driven control/monitoring design → SKCF/TCAD templates (update-on-spike, hold-last-valid, zero-quiescent-energy).
4. On-device continual learning with safety constraints → drift-bounded multiplicative STDP + supervisory gate.

## References
- Suresh Kumar TP, Vikas Agnihotri. "Neuromorphic Satellite Intelligence: A Formal Framework..." arXiv:2610.12471 (2026).
- Baselines: Loihi 2 (~0.9 pJ/SOP, Intel 4), SpiNNaker 2 (~3.5 pJ/SOP, 22nm FD-SOI), DYNAP-SE2 (0.003 pJ analog, 65nm).