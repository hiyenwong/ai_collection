---
name: spiker-ll-fpga-snn-accelerator
description: "Spiker-LL methodology: FPGA-based SNN accelerator enabling on-device adaptive local learning via STSF (Spiking Time Sparse Feedback) rule. Extends open-source Spiker+ inference architecture with hardware-adapted three-factor learning. Achieves 92-93% accuracy, sub-ms latency, <0.1mJ per inference, DSP-free. Use when: designing SNN hardware accelerators, implementing on-device learning, edge neuromorphic computing, STSF learning rule, FPGA SNN deployment, hardware-algorithm co-design, local learning rules vs BPTT, energy-efficient edge AI."
---

# Spiker-LL: FPGA SNN Accelerator with On-Device Learning

## Core Contribution

Spiker-LL extends the open-source Spiker+ inference architecture with efficient **on-device supervised learning** using the STSF (Spiking Time Sparse Feedback) local learning rule. Enables real-time inference AND training on low-cost edge FPGAs.

## Key Results

| Dataset | Architecture | Accuracy | Latency | Energy/Inference |
|---------|-------------|----------|---------|-----------------|
| MNIST | 784-200-10 | 92% | <1ms | <0.1 mJ |
| F-MNIST | 784-200-10 | 88% | <1ms | <0.1 mJ |
| DIGITS | 64-20-10 | 93% | <1ms | <0.1 mJ |

- **Platform**: Pynq Z2 (Xilinx Zynq-7020)
- **DSP-free**: Uses only LUTs and BRAMs, no DSP slices
- **Scalable**: From <5k LUTs (compact) to larger configurations
- **16-bit fixed-point**: 8 fractional bits for weights and membrane potentials

## STSF Learning Rule

STSF is a **three-factor local learning rule** that avoids BPTT's O(NT) memory and O(ET) compute costs.

### Weight Update

For each synapse, combines three quantities available in hardware:
1. **Pre-synaptic spike**: s_pre(t)
2. **Post-synaptic membrane potential**: V_post(t)
3. **Global error signal**: δ(t) from temporal gating

ΔW_ij ∝ s_pre(t) · V_post(t) · δ(t)

### Key Design Choices

- **Coincidence-based updates without traces**: Avoids memory bottlenecks of eligibility trace methods
- **Temporal gating**: Only 5 timesteps used for weight updates (out of 10 total), reducing compute
- **Single-sample adaptation**: Fixed-point updates preserve learning dynamics with marginal accuracy loss
- **No BPTT required**: Eliminates temporal unrolling and long-range dependencies

## Hardware Architecture

### Baseline (Spiker+)
- Fully parameterizable LIF neuron layers
- Multiplier-free discrete-time LIF model
- Per-layer BRAM weight storage
- Sequential input streaming, parallel neuron computation
- Local controllers per layer + global controller

### Extensions for Learning (Spiker-LL)
1. **Weight Updater Module**: Ultra-lightweight, tightly coupled to each LIF neuron
   - Implements STSF three-factor rule in datapath
   - Modular — deployable across different network configs
2. **Error Signal Distribution**: Global error signal routed to all synaptic access points
3. **Temporal Gating Controller**: Selects which timesteps contribute to weight updates
4. **State Memory**: Minimal additional BRAM for post-synaptic state accumulation

### LIF Neuron Model

```
I_syn[n] = Σ_j W_j · s_in,j[n]
V_m[n] = β·V_m[n-1] + I_syn[n] - V_th·s_out[n-1]
s_out[n] = 1 if V_m[n] ≥ V_th, else 0
```

Reset mechanism configurable (subtractive or zeroing).

## Comparison with Prior SNN Accelerators

| Work | Year | Rule | Accuracy | Platform |
|------|------|------|----------|----------|
| Spiker-LL (this) | 2026 | STSF | 92% | Pynq Z2 |
| [15] Integer E-Prop | 2025 | E-Prop | 97.55% | Zynq-7010 |
| [16] Optimized AL | 2025 | AL | 97.3% | Zynq-7045 |
| [18] PLR | 2020 | PLR | 96.2% | Zynq-7045 |
| [21] STDP | 2023 | STDP | 91.5% | Virtex-6 |

Spiker-LL trades some accuracy for **full on-device training** capability with minimal energy.

## Design Principles

1. **Hardware-adapted algorithm**: STSF chosen specifically for hardware compatibility (coincidence detection, no traces)
2. **Reuse existing datapaths**: Training modifications at synaptic-state access points only
3. **Preserve timing closure**: No impact on inference path critical timing
4. **Fixed-point arithmetic**: 16-bit with 8 fractional bits — balances precision and resource usage

## Future Extensions

- Incremental updates for online adaptation
- Runtime feedback loops for continuous learning
- Richer neuron models beyond LIF
- Stability analysis under quantization and gating

## Related Skills

- `snn-fpga-hardware-software-codesign` — FPGA SNN co-design patterns
- `edgespike-edge-iot-snn` — Edge SNN deployment
- `spiking-neural-network-analysis` — SNN paper analysis
- `snn-learning-survey` — SNN learning paradigms

## arXiv Reference

- **Paper**: "Spiker-LL: An Energy-Efficient FPGA Accelerator Enabling Adaptive Local Learning in Spiking Neural Networks" (Caviglia et al., 2026)
- **ID**: arXiv:2605.18003
- **URL**: https://arxiv.org/abs/2605.18003
