---
name: elsa-snn-elastic-inference
description: "ELSA — ELastic SNN Inference Architecture for efficient neuromorphic computing, featuring near-SRAM spine/token-wise dataflow pipeline, bundled AER protocol for NoC, and mini-batch spiking Gustavson-product for exploiting SNN sparsity. ISCA 2026. 3.4× speedup and 13.6× energy efficiency vs SOTA. arXiv:2605.20802"
tags: [snn, neuromorphic-hardware, accelerator, elastic-inference, dataflow-architecture, sparse-computation, event-driven, isca-2026]
arxiv_id: "2605.20802"
date: "2026-05-20"
---

# ELSA: An ELastic SNN Inference Architecture for Efficient Neuromorphic Computing

## Paper Reference

**Title:** ELSA: An ELastic SNN Inference Architecture for Efficient Neuromorphic Computing
**Authors:** Kang You, Chen Nie, Lee Jun Yan, Ziling Wei, Cheng Zou, Zekai Xu, Yu Feng, Honglan Jiang, Zhezhi He
**arXiv:** 2605.20802 (May 20, 2026)
**Category:** cs.AR (Hardware Architecture) — **Accepted ISCA 2026**

## Abstract Summary

SNNs exploit event-driven and addition-only computation for efficiency. A key SNN property — **elastic inference** — allows outputs to emerge progressively. However, existing SNN accelerators use layer-by-layer or time-step-by-time-step designs that cannot capitalize on this. ELSA is a near-SRAM dataflow architecture realizing true elastic inference through fine-grained **spine/token-wise pipeline** and hardware optimizations tailored to SNNs.

## Core Innovations

### 1. Fine-Grained Spine/Token-Wise Pipeline

Traditional SNN accelerator vs. ELSA:

```
Traditional (layer-wise):
  [Layer1 all] → [Layer2 all] → [Layer3 all] → Output
  
Traditional (time-step-wise):
  [t=0: all layers] → [t=1: all layers] → [t=2: all layers]
  
ELSA (spine/token-wise):
  [spine1 → spine2 → spine3 → ...] continuous streaming
   ↑ Each spike token forwarded immediately upon production
```

- Each spine/token forwarded immediately upon production
- **Continuous streaming pipeline** minimizes latency to first response
- Enables early exit for salient inputs (truly elastic)

### 2. Bundled Address Event Representation (AER) Protocol

- Custom protocol for network-on-chip (NoC) communication
- Bundles spike events efficiently
- Reduces communication traffic between processing elements

### 3. Mini-Batch Spiking Gustavson-Product

A novel sparse computation primitive:
- Exploits inherent SNN sparsity
- Reduces memory access by processing only active spikes
- Mini-batch grouping for efficient hardware utilization

## Architecture Overview

```
┌──────────────────────────────────────────────────┐
│                 ELSA Architecture                  │
│                                                    │
│  Input ──► Spike Encoder ──► Near-SRAM PE Array    │
│                                    │               │
│                            ┌───────┴───────┐      │
│                            │  Spine/Token   │      │
│                            │  Stream Buffer │      │
│                            └───────┬───────┘      │
│                                    │               │
│                            ┌───────┴───────┐      │
│                            │ Bundled AER   │      │
│                            │ NoC Router    │      │
│                            └───────┬───────┘      │
│                                    │               │
│                            ┌───────┴───────┐      │
│                            │ Spike          │      │
│                            │ Accumulation   │      │
│                            └───────┬───────┘      │
│                                    │               │
│  Output ◄──── Continuous Stream ◄──┘               │
└──────────────────────────────────────────────────┘
```

## Key Results

### Performance Comparison (4-bit ResNet-50)

| Metric | vs SOTA QANN Accel (ANT) | vs SOTA SNN Accel (PAICORE) |
|--------|:------------------------:|:--------------------------:|
| **Speedup** | **3.4×** | **2.9×** |
| **Energy efficiency** | **13.6×** | **22.1×** |
| Accuracy | On-par | On-par |

### Benefits of Elastic Inference

- **Salient inputs**: Early response in as little as 1/3 of full inference time
- **Progressive refinement**: Output quality improves over time
- **Latency-accuracy trade-off**: Configurable for real-time constraints
- **Batch processing**: Efficient handling of mixed-sallience inputs

## Technical Details

### Bundled AER Protocol

```
Standard AER:  [addr_1][addr_2]...[addr_n]  (individual packets)
Bundled AER:   [n] [addr_1, addr_2, ..., addr_n]  (batched)
```

- Reduces header overhead for dense spike bursts
- Compatible with mesh/torus NoC topologies
- Support for multicast and broadcast

### Mini-Batch Gustavson-Product

Standard sparse matrix multiply:
```
C = A × B  →  process non-zeros of A one at a time
```

Mini-batch version:
```
C = A × B  →  group non-zeros into mini-batches
               process batch with SIMD-style execution
```

- Better utilization of near-SRAM compute units
- Exploits temporal locality of spike patterns
- Reduces load/store operations

### Near-SRAM Dataflow

Processing elements placed close to SRAM banks:
- Minimal wire delay for spike data
- Local accumulation for membrane potentials
- Distributed spike identification and routing

## Comparison with Existing SNN Accelerators

| Feature | PAICORE | ELSA |
|---------|:------:|:----:|
| Pipeline granularity | Layer-wise | Spine/token-wise |
| Elastic inference | No | Yes |
| NoC protocol | Standard AER | Bundled AER |
| Sparsity exploitation | Post-processing | Gustavson-product |
| First-spike latency | Full network | Progressive |
| Energy efficiency | Baseline | **22.1×** |

## Applications

1. **Real-time SNN inference**: Autonomous driving, robotics
2. **Edge neuromorphic computing**: Low-power IoT devices
3. **Event-based vision**: DVS camera processing
4. **Continuous monitoring**: Always-on sensory processing
5. **Sparse spike processing**: Any SNN workload

## Pitfalls & Considerations

- Designed specifically for SNNs, not ANNs
- Performance depends on spike sparsity (very sparse inputs benefit most)
- Near-SRAM placement limits total SRAM capacity
- Elastic inference requires algorithm-level support (e.g., early-exit classifiers)
- Bundled AER may hurt latency for very sparse spike patterns

## Activation Keywords

- ELSA SNN accelerator
- elastic SNN inference
- spine-wise pipeline neuromorphic
- bundled AER protocol SNN
- spiking Gustavson product
- near-SRAM SNN architecture
- fine-grained SNN dataflow
- ISCA 2026 SNN
- progressive SNN inference
- arXiv:2605.20802

## Related Skills

- quantized-snn-hardware-optimization
- spiker-ll-snn-accelerator
- edgespike-edge-iot-snn
- snn-fpga-hardware-software-codesign

## References

- arXiv:2605.20802 — "ELSA: An ELastic SNN Inference Architecture" (You et al., ISCA 2026)
- PAICORE — prior SOTA SNN accelerator
- ANT — prior SOTA QANN accelerator
- Gustavson's algorithm for sparse matrix multiply
- Address Event Representation (AER) protocol
