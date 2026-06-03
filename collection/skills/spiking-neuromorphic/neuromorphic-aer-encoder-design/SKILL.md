---
name: neuromorphic-aer-encoder-design
description: "Ultra-low-power synthesizable asynchronous AER encoder design for neuromorphic edge devices. Tree-based architecture with bundled-data protocol and cross-coupled NAND random-priority arbiter for event collision resolution. Activation: neuromorphic encoder, AER design, asynchronous circuit, spiking neural network hardware, edge device neuromorphic, low-power SNN."
---

# Neuromorphic AER Encoder Design

Fully synthesizable tree-based Address-Event Representation (AER) encoder for scalable neuromorphic computing systems with ultra-low power consumption.

## Description

This skill provides methodology for designing and implementing ultra-low-power asynchronous AER encoders for neuromorphic edge devices. The design uses standard digital cells, enabling full synthesis and place-and-route with commercial EDA tools.

**Key Features:**
- Fully synthesizable (no custom cells required)
- Tree-based architecture for scalability
- Bundled-data protocol in semi-decoupled micropipeline
- Cross-coupled NAND random-priority arbiter
- 435 fJ per encoded event energy efficiency

## Activation Keywords
- neuromorphic encoder
- AER design
- asynchronous circuit
- spiking neural network hardware
- edge device neuromorphic
- low-power SNN
- event-based encoding

## Research Foundation

**Paper:** An Ultra-Low-Power Synthesizable Asynchronous AER Encoder for Neuromorphic Edge Devices  
**arXiv:** 2604.05313v1 (2026)  
**Authors:** Yihui Wang, Sheng-Yu Peng, Sahil Shah

## Architecture Overview

### Tree-Based Structure

```
        Root Encoder
       /     |     \
    Node1   Node2   Node3
    /  \    /  \    /  \
  Leaf Leaf Leaf Leaf Leaf
  (Event Sources)
```

### Key Components

1. **Semi-Decoupled Micropipeline**
   - Bundled-data protocol for timing
   - Edge-triggered flip-flops (standard cells)
   - No transparent latches

2. **Random-Priority Arbiter**
   - Cross-coupled NAND structure
   - Fair event collision resolution
   - Deterministic latency

3. **Tree Encoder**
   - Hierarchical event aggregation
   - Scalable to N events
   - 33 MEvent/s throughput

## Implementation Specifications

### Fabrication Results (65nm CMOS)

| Metric | Value |
|--------|-------|
| Technology | 65nm CMOS |
| Event Capacity | 8 events |
| Peak Throughput | 33 MEvent/s |
| Average Latency | 50 ns |
| Delay per Event-Bit | 17 ns |
| Energy per Event | 435 fJ |
| Design Flow | Pure digital standard-cell |

### Design Flow

```
RTL Description → Logic Synthesis → Place & Route → Sign-off
     ↑                                              ↓
  Verilog/VHDL                                  GDSII
```

## Circuit Design Details

### Bundled-Data Protocol

```verilog
// Request-Acknowledge handshake
module bundled_data_channel (
    input req_in,
    input ack_out,
    output req_out,
    output ack_in,
    input [DATA_WIDTH-1:0] data_in,
    output [DATA_WIDTH-1:0] data_out
);
    // Delay line matched to combinational logic
    wire delay_out;
    delay_line #(.DELAY(COMB_DELAY)) dl (.in(req_in), .out(delay_out));
    
    // Output registration
    assign req_out = delay_out;
    assign ack_in = ack_out;
endmodule
```

### Cross-Coupled NAND Arbiter

```verilog
module nand_arbiter (
    input req_a,
    input req_b,
    output grant_a,
    output grant_b
);
    wire q_a, q_b;
    
    // Cross-coupled NAND gates
    nand n1(q_a, req_a, q_b);
    nand n2(q_b, req_b, q_a);
    
    assign grant_a = q_a;
    assign grant_b = q_b;
endmodule
```

### Tree Encoder Node

```verilog
module tree_encoder_node (
    input [N-1:0] event_in,
    input [N-1:0] addr_in,
    output event_out,
    output [ADDR_WIDTH-1:0] addr_out
);
    // Priority encoding with arbiter
    wire [N-1:0] grants;
    round_robin_arbiter arb (.requests(event_in), .grants(grants));
    
    // Address selection
    priority_encoder enc (.in(grants & addr_in), .out(addr_out));
    assign event_out = |event_in;
endmodule
```

## Design Workflow

### Step 1: Event Source Interface

Define event source characteristics:
- Event rate (events/second)
- Address width
- Timing requirements

### Step 2: Tree Sizing

Determine tree depth and fanout:
```python
tree_depth = ceil(log2(num_events))
fanout = 2  # binary tree
```

### Step 3: Timing Closure

Match delay lines to combinational paths:
```tcl
# SDC constraints
set_max_delay -from [get_pins req_in] -to [get_pins req_out] 2.0
set_min_delay -from [get_pins req_in] -to [get_pins req_out] 1.5
```

### Step 4: Power Optimization

- Clock gating for inactive branches
- Multi-Vt cell usage
- Voltage island partitioning

## Performance Comparison

| Design | Throughput | Energy/Event | Synthesizable |
|--------|-----------|--------------|---------------|
| This Work | 33 MEvent/s | 435 fJ | Yes |
| Traditional AER | ~10 MEvent/s | ~1 pJ | Partial |
| Custom Cell | 50 MEvent/s | 200 fJ | No |

## Integration with SNN Systems

### Interface to Spiking Neurons

```
Spiking Neuron Array → AER Encoder → Communication Channel
      (events)            (address)      (serialized)
```

### Event Format

```
[Timestamp] [Address] [Polarity]
   16-bit     8-bit      1-bit
```

## Tools and Resources

- **Synthesis**: Cadence Genus, Synopsys Design Compiler
- **Place & Route**: Cadence Innovus, Synopsys ICC2
- **Verification**: Custom UVM testbench
- **Timing**: PrimeTime, Tempus

## Future Enhancements

- Multi-level arbitration for fairness
- Dynamic power management
- 3D stacking for higher density
- Integration with memristive synapses

## References

- Paper: arXiv:2604.05313v1
- 65nm CMOS process parameters
- AER protocol specifications

_Last updated: 2026-04-13_
