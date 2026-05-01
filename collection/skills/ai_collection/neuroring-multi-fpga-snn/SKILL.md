---
name: neuroring-multi-fpga-snn
title: "NeuroRing: Multi-FPGA Spiking Neural Network Accelerator"
category: neuroscience
source: arXiv:2604.28059
paper_title: "NeuroRing: Scaling Spiking Neural Networks via Multi-FPGA Bidirectional Ring Topologies and Stream-Dataflow Architectures"
authors:
  - Muhammad Ihsan Al Hafiz
  - Artur Podobas
date: 2026-04-30
acceptance: Euro-Par 2026
subjects:
  - cs.AR (Computer Architecture)
  - cs.DC (Distributed, Parallel, and Cluster Computing)
  - cs.NE (Neural and Evolutionary Computing)
description: >
  A modular and scalable SNN accelerator based on a stream-dataflow architecture
  and bidirectional ring topology, implemented in HLS on programmable FPGAs,
  with NEST simulator integration and multi-FPGA deployment support.
keywords:
  - spiking neural networks
  - SNN accelerator
  - FPGA
  - HLS
  - high-level synthesis
  - stream-dataflow architecture
  - bidirectional ring topology
  - multi-FPGA
  - NEST simulator
  - cortical microcircuit
  - neuromorphic computing
  - real-time factor
  - strong scaling
  - weak scaling
  - energy efficiency
  - constraint satisfaction
  - 脉冲神经网络
  - 现场可编程门阵列
  - 硬件加速
  - 神经形态计算
  - 数据流架构
  - 多FPGA部署
  - 脉冲神经元模型
activation_keywords:
  - neuroring
  - neuro-ring
  - neuro ring
  - multi-FPGA SNN
  - FPGA spiking network
  - SNN accelerator
  - stream-dataflow SNN
  - bidirectional ring SNN
  - HLS spiking neural network
  - 多FPGA脉冲网络
  - FPGA脉冲加速器
  - 神经环
---

# NeuroRing — Multi-FPGA SNN Accelerator

## Overview

**NeuroRing** is a hardware accelerator for **Spiking Neural Networks (SNNs)** that achieves scalable, faster-than-real-time simulation of large-scale SNN models. It combines a **stream-dataflow architecture** with a **bidirectional ring topology** to distribute synaptic event processing across multiple programmable FPGAs, while maintaining compatibility with the widely-used **NEST simulator** workflow.

- **arXiv**: [2604.28059](https://arxiv.org/abs/2604.28059)
- **Accepted**: Euro-Par 2026
- **Authors**: Muhammad Ihsan Al Hafiz, Artur Podobas

---

## Key Contributions

1. **Modular & Scalable SNN Accelerator** — Built on a stream-dataflow architecture with bidirectional ring topology for efficient event-driven SNN simulation.
2. **HLS Implementation** — Entire design is expressed in High-Level Synthesis, enabling rapid iteration and deployment on programmable FPGAs.
3. **Single- and Multi-FPGA Deployment** — Architecture scales modularly from a single FPGA to a ring of interconnected FPGAs.
4. **NEST Simulator Integration** — Compatible with existing SNN workflows; models built in NEST can be offloaded to NeuroRing hardware.
5. **Benchmark Evaluation** — Validated on:
   - Cortical microcircuit (Potjans & Diesmann, 2014) — 77,169 neurons, ~300M synapses
   - Sudoku constraint-satisfaction workload
6. **Biological Fidelity** — Preserves key activity statistics (mean firing rate, coefficient of variation) of the NEST reference model.
7. **Faster-than-Real-Time** — RTF = **0.83** for the full-scale cortical microcircuit.
8. **Meaningful Scaling** — Demonstrates both strong and weak scaling across multiple FPGAs.
9. **Competitive Energy Efficiency** — Evaluated across two programmable FPGAs.

---

## Architecture

### Stream-Dataflow Architecture

NeuroRing processes SNN events as streams flowing through pipelined compute blocks:

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Neuron      │───▶│  Synapse     │───▶│  Spike       │
│  Processing  │    │  Processing  │    │  Generator   │
│  Unit (NPU)  │    │  Unit (SPU)  │    │  Unit (SGU)  │
└──────────────┘    └──────────────┘    └──────────────┘
       ▲                                      │
       │          ┌──────────────┐            │
       └──────────│  Delay       │◀───────────┘
                  │  Line        │
                  │  Buffer      │
                  └──────────────┘
```

- **NPU (Neuron Processing Unit)**: Computes membrane potential updates and checks spike thresholds for each neuron model (e.g., leaky integrate-and-fire).
- **SPU (Synapse Processing Unit)**: Handles synaptic weight multiplication and event routing.
- **SGU (Spike Generator Unit)**: Produces spike events and routes them through the ring.
- **Delay Line Buffer**: Manages spike delivery delays, essential for biologically realistic simulations.

### Bidirectional Ring Topology

Multiple FPGA nodes are arranged in a ring with **bidirectional** communication links:

```
       ┌─────────┐
   ┌──▶│ FPGA N  │──┐
   │   └─────────┘  │
   │                ▼
┌──────┐        ┌─────────┐
│FPGA 1│───┬───▶│ FPGA 2  │
└──────┘   │    └─────────┘
   ▲       │
   │   ┌──────┐
   └───│FPGA 3│
       └──────┘
```

- **Bidirectional links** reduce latency by allowing spikes to travel in the shorter direction around the ring.
- **Stream-based communication** avoids buffering overhead — events flow continuously through the ring.
- **Scalable**: Add FPGAs to the ring to increase capacity linearly.
- **Partitioning**: Neurons are distributed across FPGAs; each FPGA handles a subset and routes inter-FPGA spikes via the ring.

### HLS Implementation

The entire accelerator is implemented using **High-Level Synthesis (HLS)**, which allows:
- Hardware design in C/C++ rather than HDL
- Rapid design space exploration via pragmas and directives
- Portability across FPGA vendors (Xilinx/AMD Vivado HLS, Intel HLS Compiler)

Key HLS design patterns:
- **Pipeline pragmas** for streaming throughput
- **Array partitioning** for parallel memory access
- **Dataflow pragmas** to overlap NPU, SPU, and SGU execution

---

## NEST Simulator Integration

NeuroRing integrates with NEST by:

1. **Model export**: NEST network definitions (neurons, synapses, topology) are serialized to a hardware-compatible format.
2. **Weight distribution**: Synaptic weights and connectivity are pre-processed and loaded into FPGA memory.
3. **Execution**: The FPGA runs the SNN simulation independently, producing spike trains.
4. **Result import**: Spike outputs are read back into NEST for analysis and comparison.

This allows researchers to build models in familiar NEST syntax and seamlessly offload computation to NeuroRing hardware.

### Python Setup Example

```python
#!/usr/bin/env python3
"""
NeuroRing — NEST Simulator Integration Example
Setup a cortical microcircuit model compatible with NeuroRing offloading.

Requires: nest-simulator, numpy
"""

import nest
import numpy as np

# ─── 1. Configure NEST ─────────────────────────────────────────────────────

nest.ResetKernel()
nest.SetKernelStatus({
    "resolution": 0.1,          # Simulation time step (ms)
    "simtime": 1000.0,          # Total simulation time (ms)
    "local_num_threads": 1,     # Single-threaded for export compatibility
})

# ─── 2. Build Cortical Microcircuit (Potjans-Diesmann, 2014) ───────────────

# Population sizes per cortical layer (L2/3, L4, L5, L6) × (E, I)
# Full-scale: 77,169 neurons
layer_scales = {
    "L23_E": 4205, "L23_I": 1051,
    "L4_E":  3500, "L4_I":  875,
    "L5_E":  1450, "L5_I":  371,
    "L6_E":  3750, "L6_I":  976,
}

populations = {}
for label, n_neurons in layer_scales.items():
    pop = nest.Create("iaf_psc_alpha", n_neurons)
    pop.record = ["spikes"]  # Record spikes for NeuroRing export
    populations[label] = pop

# ─── 3. Define Connectivity ────────────────────────────────────────────────
# In full implementation, use Potjans-Diesmann connectivity probabilities
# and synaptic weights. Here we sketch the pattern.

# Connection probabilities (subset for illustration)
# Full table: 4x4 (source × target) matrices for E→E, E→I, I→E, I→I

def connect_populations(src, tgt, prob, weight, delay=1.5):
    """Connect two populations with fixed probability and weight."""
    nest.Connect(
        src, tgt,
        {"rule": "pairwise_bernoulli", "p": prob},
        {"weight": weight, "delay": delay},
    )

# Example: L4 excitatory → L2/3 excitatory (strong feedforward)
connect_populations(
    populations["L4_E"], populations["L23_E"],
    prob=0.1009, weight=1.62,
)

# ─── 4. External Input (Poisson Drive) ─────────────────────────────────────

# Simulate thalamic / external input
for label, pop in populations.items():
    pg = nest.Create("poisson_generator", params={"rate": 8.0})
    nest.Connect(pg, pop, {"weight": 1.0, "delay": 1.5})

# ─── 5. Run Simulation ─────────────────────────────────────────────────────

nest.Simulate(1000.0)  # 1 second of biological time

# ─── 6. Export for NeuroRing ───────────────────────────────────────────────

# Extract spike data
spike_data = {}
for label, pop in populations.items():
    events = nest.GetStatus(pop, "events")[0]
    spike_data[label] = {
        "senders": events["senders"],
        "times": events["times"],
    }

# Save in NeuroRing-compatible format (CSV or binary)
import json
with open("neuroring_export.json", "w") as f:
    json.dump({
        "resolution": 0.1,
        "populations": {
            label: {"n_neurons": len(pop), "model": "iaf_psc_alpha"}
            for label, pop in populations.items()
        },
        "spike_data": {k: v for k, v in spike_data.items()},
    }, f)

print("✓ Exported model to neuroring_export.json")
print(f"✓ Total neurons: {sum(len(p) for p in populations.values())}")
```

### C++ HLS Kernel Skeleton

```cpp
// neuroring_npu.cpp
// NeuroRing — Neuron Processing Unit (HLS)
// Computes membrane potential updates for LIF neurons

#include <ap_int.h>
#include <hls_stream.h>
#include "neuroring_types.h"

// ─── Neuron State ───────────────────────────────────────────────────────────
struct NeuronState {
    float  v_mem;        // Membrane potential (mV)
    float  i_syn;        // Synaptic current (pA)
    bool   refractory;   // Refractory flag
    int    refractory_countdown;
};

// ─── NPU Core ───────────────────────────────────────────────────────────────
// Pipeline the neuron update loop for maximum throughput
// Each iteration processes one neuron; results streamed to SGU

void npu_kernel(
    hls::stream<SpikeEvent>& spike_in,       // Incoming spikes from ring
    hls::stream<SpikeEvent>& spike_out,       // Outgoing spikes to ring
    hls::stream<NeuronState>& state_in,       // Current neuron states
    hls::stream<NeuronState>& state_out,      // Updated neuron states
    const float  tau_m,                        // Membrane time constant (ms)
    const float  v_thresh,                     // Spike threshold (mV)
    const float  v_reset,                      // Reset potential (mV)
    const int    refractory_period,            // Refractory period (steps)
    const int    n_neurons                     // Number of neurons on this FPGA
) {
#pragma HLS PIPELINE II=1
#pragma HLS DATAFLOW

    // Process incoming spike events
    for (int i = 0; i < n_neurons; i++) {
#pragma HLS PIPELINE II=1

        NeuronState state = state_in.read();
        float synaptic_input = 0.0f;

        // Accumulate incoming spike contributions
        while (!spike_in.empty()) {
            SpikeEvent evt = spike_in.read();
            if (evt.target_neuron == i) {
                synaptic_input += evt.weight;
            }
        }

        // LIF membrane update
        if (!state.refractory) {
            state.i_syn = synaptic_input;
            // Euler integration: dV/dt = (-V + I_syn * R) / tau_m
            float dv = (-state.v_mem + state.i_syn * 1.0f) / tau_m;
            state.v_mem += dv * 0.1f;  // dt = 0.1ms

            // Check threshold
            if (state.v_mem >= v_thresh) {
                // Emit spike
                SpikeEvent out;
                out.source_neuron = i;
                out.timestamp = /* simulation_step */;
                spike_out.write(out);

                // Reset
                state.v_mem = v_reset;
                state.refractory = true;
                state.refractory_countdown = refractory_period;
            }
        } else {
            state.refractory_countdown--;
            if (state.refractory_countdown <= 0) {
                state.refractory = false;
            }
        }

        state_out.write(state);
    }
}
```

---

## Performance Metrics

| Metric | Value |
|--------|-------|
| **Real-Time Factor (RTF)** | **0.83** (cortical microcircuit, full-scale) |
| **Neuron count** (cortical microcircuit) | 77,169 |
| **Synapse count** (cortical microcircuit) | ~300 million |
| **Sudoku CSP neurons** | ~2,000 |
| **Scaling** | Strong & weak scaling demonstrated |
| **Fidelity** | Preserves NEST reference activity statistics (mean rate, CV) |
| **Energy efficiency** | Competitive across two programmable FPGAs |

### Real-Time Factor Interpretation

An RTF of **0.83** means NeuroRing simulates **1 second of biological time in 0.83 seconds of wall-clock time** — i.e., **faster than real-time** for the full-scale cortical microcircuit benchmark.

---

## When to Use This Skill

Use this skill when discussing or working with:

- **Hardware acceleration of SNNs** on FPGAs
- **Stream-dataflow architectures** for neuromorphic computing
- **Multi-FPGA system design** for large-scale neural simulation
- **NEST-to-hardware deployment** workflows
- **Scalable SNN simulation** with real-time or faster-than-real-time constraints
- **Neuromorphic benchmarking** (cortical microcircuits, constraint satisfaction)
- **HLS-based neural accelerator design**

---

## References

- **Paper**: M. I. A. Hafiz & A. Podobas, "NeuroRing: Scaling Spiking Neural Networks via Multi-FPGA Bidirectional Ring Topologies and Stream-Dataflow Architectures," arXiv:2604.28059, Apr. 2026. Accepted at Euro-Par 2026.
- **Potjans-Diesmann Model**: T. C. Potjans & M. Diesmann, "The cell-type specific cortical microcircuit: Relating structure and activity in a full-scale spiking network model," *Cerebral Cortex*, 24(3):785–806, 2014.
- **NEST Simulator**: M. O. Gewaltig & M. Diesmann, "NEST (NEural Simulation Tool)," *Scholarpedia*, 2(4):1430, 2007.
