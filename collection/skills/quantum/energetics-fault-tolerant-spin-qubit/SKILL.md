---
name: energetics-fault-tolerant-spin-qubit
description: "Energy-budget methodology for Loss-DiVincenzo spin-qubit FTQC (Si, ~1 K): baseline power model (cryostat 5-10 kW constant, instrumentation ∝ qubits, magnet), QFT-vs-FFT benchmark with energy crossover ~45 qubits preceding time crossover ~57 (gate/FLOP ratios 10^9 energy vs 10^12 time), single-cryostat thermal limit 10^4-10^5 qubits at 1 K (700 mW cooling), control demultiplexing ratio 1:500 cutting energy ~2 orders of magnitude, ~100 kW at 10^6 physical qubits. Use when estimating FTQC power draw, energy-vs-speedup crossovers, or cryo scaling limits. Activation: spin qubit energy budget, FTQC energetics, QFT vs FFT crossover, cryogenic cooling power, demultiplexing ratio, thermal budget, resource estimation power."
---

# Energetics of Fault-Tolerant Spin-Qubit Quantum Computation

Methodology from arXiv:2610.22199 (Santos, Nath, Pezzutto, Savin, Meunier & Omar; Oct 2026). Complete power/energy model of a Loss-DiVincenzo semiconductor spin-qubit quantum computer (isotopically purified silicon, operated near 1 K), benchmarked via QFT vs classical FFT with surface-code QEC overheads included. Headline: **quantum computing can become energetically competitive before it becomes faster**.

## Energy Budget Components

| Component | Scaling | Reference values |
|---|---|---|
| Cryostat cooling | constant | 5-10 kW input power; dominant baseline pre-QEC |
| Static magnet | constant | baseline contribution |
| Room-temp instrumentation | ∝ # RF outputs (≈ gate electrodes) | ≈15 MW at 10^6 qubits without demux |
| Gate execution | ∝ # gates | ≈10^-2 J/gate incl. baseline; ESR R_x most expensive |
| QEC cycles + gate synthesis | ∝ # physical qubits × cycles | surface code d=13/25 at scale |
| Decoding (CPU) | ∝ # physical qubits | ~100 kW order at 10^6 qubits (AMD EPYC 7763, 280 W; decoder-dependent) |

## Energy Crossover Before Time Crossover

Benchmark: QFT (1024 shots) vs full FFT on TOP500 references — El Capitan (1742 PFLOP/s) for time; KAIROS (46 kW, 3.1 PFLOP/s, 1.37×10^-11 J/FLOP) for energy.

- Per-op cost ratios: energy 1 gate (≈10^-2 J) / 1 FLOP (1.37×10^-11 J) ≈ 10^9; time 1 gate (10^-6 s) / 1 FLOP (5.74×10^-19 s) ≈ 10^12.
- Since the time ratio ≫ energy ratio while scaling exponents match, the **energy crossover precedes the time crossover** whenever the quantum workload (state prep + shot sampling) stays polynomially bounded.
- Analytic crossover equation: Q·q² = C·q·2^q → energy crossover ≈45 qubits vs time ≈57 qubits (explicit simulation: <50 vs ~60).
- Practical meaning: energy crossover at 45 qubits needs only ~2×10^15 classical ops (~990 quantum gates) vs 8×10^18 at the 57-qubit time crossover — a 10^3 reduction in classical resources burned before quantum wins on energy.

## QEC Effects

- Surface code d=9: running time grows by 4 orders of magnitude; crossovers shift to 69 (energy) vs 75 (time) logical qubits — beyond what one cryostat can host (~20 logical / ~3×10^4 physical qubits), so cryo-electronics + demultiplexing are prerequisites for even reaching the analysis regime.
- At 10^6-qubit scale, instrumentation + decoding dominate the budget; cryogenic cooling constrains scalability.

## Cryostat Thermal Budget (the hard wall)

At ~1 K, cooling capacity ≈ 700 mW (Bluefors XLD-class). Each qubit needs ≥3 DC (≈200 nW static each) + 3 RF (≈15 nW) cables at the mixing chamber → **max ~2-3×10^4 physical qubits per cryostat** (order-of-magnitude bound 10^4-10^5). Brute-force wiring of 10^6 qubits is thermally impossible: demultiplexing is a scalability requirement, not merely an optimization.

## Control-Signal Demultiplexing

- Demux ratio m = # RF outputs without demux / # with demux; demuxer power itself negligible.
- Instrumentation power scales down by m; 1:500 ratio in the benchmark system.
- Rebalancing cooling + instrumentation + decoding: **≈2 orders of magnitude total energy reduction**.

## Reference Estimate

10^6 physical qubits, surface code d = 13 and 25 (within target error thresholds), demux 1:500, within a single-cryostat thermal budget → **total system power ≈ 100 kW**, at least one order of magnitude below today's highest-performance classical systems.

## Workflow: Build Your Own Energy Model

1. Enumerate baseline power (cryo, magnet — constant), per-gate energy, instrumentation cost per RF output, decoder FLOPs → CPU count → watts.
2. Express time and energy as (per-op cost) × (op count) for both the quantum algorithm and classical benchmark; keep sampling overheads explicit.
3. Solve the crossover equation Q·q^a = C·q·2^{aq} for energy and time. Energy crossover comes first iff (gate/FLOP energy ratio) < (gate/FLOP time ratio).
4. Add QEC: physical qubits per logical patch, cycle times, gate synthesis, decoder throughput; recompute crossovers in logical qubits.
5. Check cryostat thermal budget: sum static cable loads at the mixing chamber vs cooling capacity; if exceeded, introduce demux ratio m and rescale instrumentation.
6. Report crossover sizes, per-component power at target scale, and the demux ratio used.

## Caveats

- QFT (sampling-based estimates) vs full FFT is a benchmark, not an equivalent-task comparison — crossovers are indicative, not proof of quantum advantage.
- Decoding estimate is decoder-dependent (neural-network decoders would change the ~100 kW figure).
- Operating at 1 K vs lower temperatures trades coherence/fidelity against power.

## Related Skills

- ft-resource-estimation-uncertainty-propagation — report FT resource estimates as intervals
- hardware-tailored-qec-resource-estimation — hardware-specific resource estimation
- energetic-efficiency-quantum-computation — energetic efficiency analysis framework
- wattlytics-hpc-optimization — classical HPC energy/TCO co-optimization (benchmark side)
