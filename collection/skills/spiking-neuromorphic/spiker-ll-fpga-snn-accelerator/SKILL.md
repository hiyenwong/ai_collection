---
name: spiker-ll-fpga-snn-accelerator
description: >
  Spiker-LL methodology — FPGA-based SNN accelerator enabling adaptive local learning
  at the edge. Extends the open-source Spiker+ inference architecture with efficient
  support for the Spiking Time Sparse Feedback (STSF) local learning rule.
  Achieves up to 93% accuracy (MNIST/F-MNIST/DIGITS), sub-millisecond latency,
  and <0.1 mJ per inference, remaining DSP-free and highly scalable for edge-FPGA deployments.
  Use when: designing edge SNN hardware accelerators, implementing on-device learning,
  building FPGA-based neuromorphic systems, optimizing STSF/local learning rule hardware,
  comparing SNN accelerator architectures.
  Activation: Spiker-LL, FPGA SNN accelerator, edge learning, on-device training, STSF,
  local learning rule hardware, Spiker+ extension, neuromorphic FPGA, event-driven accelerator.
  Based on arXiv:2605.18003 (May 2026).
---

# Spiker-LL: FPGA Accelerator for Adaptive Local Learning in SNNs

## Core Concept

Spiker-LL extends the open-source Spiker+ inference architecture with targeted
microarchitectural extensions enabling on-device learning via the Spiking Time Sparse
Feedback (STSF) local learning rule. The design adds training support through minimal
modifications at synaptic-state access points while reusing existing datapaths, memory
banks, and control logic.

**Key Achievement**: Unified inference + training accelerator that remains DSP-free,
scales from <5k LUTs to larger networks, and maintains real-time operation.

## Paper Details (arXiv:2605.18003)

- **Authors**: Alessio Caviglia, Filippo Marostica, Alessandro Savino, Stefano Di Carlo
- **Categories**: cs.NE (Neural and Evolutionary Computing), cs.AI (Artificial Intelligence)
- **Submitted**: 18 May 2026
- **License**: CC BY-NC-SA 4.0

## Technical Architecture

### Spiker+ Base Architecture

- Open-source Spiker framework as inference foundation
- Discrete-time Leaky Integrate and Fire (LIF) neuron model
- Event-driven, temporally sparse computation
- Binary spike communication instead of dense vector operations

### STSF Local Learning Rule

- Spiking Time Sparse Feedback (STSF) enables supervised learning without full BPTT cost
- Computes updates where and when data is generated, reducing computation and memory
- Key advantage: avoids the memory overhead of storing spike traces required by BPTT

### Microarchitectural Extensions

1. **Synaptic-state access modifications**: Minimal changes at memory access points
2. **Datapath reuse**: Existing datapaths, memory banks, control logic preserved
3. **DSP-free design**: No digital signal processing blocks required
4. **Scalable**: From <5k LUTs (ultra-compact) to larger configurations

## Performance Results

| Dataset | Accuracy | Latency | Energy/Inference |
|---------|----------|---------|------------------|
| MNIST   | ~93%     | <1ms    | <0.1 mJ          |
| F-MNIST | ~92%     | <1ms    | <0.1 mJ          |
| DIGITS  | ~92%     | <1ms    | <0.1 mJ          |

## Key Design Decisions

1. **FPGA over ASIC/ASIC**: FPGAs combine low deployment cost with reconfigurability
2. **Local learning over BPTT**: BPTT is infeasible on resource-constrained edge devices
3. **Minimal extensions**: Training added without compromising inference efficiency
4. **DSP-free**: Avoids dedicated DSP blocks, reduces resource usage

## Implementation Considerations

- Input encoding: rate, temporal, or latency coding for spike trains
- Neuromorphic sensor compatibility for real-time event streams
- Timing closure preserved through reuse of existing control logic
- Memory bandwidth optimization for concurrent inference + training

## Activation Keywords

- Spiker-LL
- FPGA SNN accelerator
- edge learning
- on-device training
- STSF
- Spiking Time Sparse Feedback
- local learning rule hardware
- Spiker+ extension
- neuromorphic FPGA
- event-driven accelerator
- SNN inference training
- DSP-free SNN
- LIF FPGA implementation

## Related Skills

- spiking-neural-network-analysis
- snn-learning-survey
- snn-fpga-hardware-software-codesign
- spiking-computational-neuroscience-survey
- edgespike-edge-iot-snn

## References

- Paper: arXiv:2605.18003 (May 2026)
- Spiker+ architecture: https://github.com/polito-Make-it/spiker
- STSF local learning rule: Reference [9] in paper
