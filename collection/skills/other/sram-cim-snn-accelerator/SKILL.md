---
name: sram-cim-snn-accelerator
version: v1.0.0
last_updated: 2026-04-21
description: "SRAM-Based Compute-in-Memory Accelerator for Linear-decay Spiking Neural Networks. Leverages in-memory computing to eliminate the von Neumann bottleneck for SNN inference using linear-decay neuron models compatible with CIM crossbar arrays for ultra-low power edge inference. Activation: SRAM CIM SNN, compute-in-memory spiking network, linear-decay SNN accelerator, CIM crossbar SNN, in-memory computing spiking neural network."
---

# SRAM CIM SNN Accelerator

Skill for designing and utilizing SRAM-based compute-in-memory (CIM) accelerator architectures for linear-decay spiking neural networks (SNNs).

**Source:** arXiv:2603.12739 — "SRAM-Based Compute-in-Memory Accelerator for Linear-decay Spiking Neural Networks"

## Core Concepts

### Compute-in-Memory (CIM) Architecture

CIM eliminates the von Neumann bottleneck by performing computation directly within memory arrays, avoiding costly data movement between memory and processing units:

- **Crossbar Array**: SRAM cells organized in a matrix where rows = inputs, columns = outputs
- **In-Memory MAC**: Multiply-accumulate operations happen in-place within the memory array
- **Analog/Digital Hybrid**: Analog computation in the array + digital peripheral circuits
- **Massive Parallelism**: All cells compute simultaneously during a single access cycle

### Linear-Decay Neuron Model

The linear-decay neuron model is specifically designed for CIM compatibility:

- **Linear Membrane Decay**: Instead of exponential decay, uses a linear approximation
- **CIM-Friendly**: Simplifies the computation to additions/subtractions, eliminating multiplications
- **Hardware Efficient**: Requires only adders and comparators, no multipliers
- **SNN Compatible**: Preserves the essential spiking dynamics of LIF neurons

The membrane update equation:

```
V[t+1] = V[t] - decay_step + Σ(w_i × s_i[t])
```

Where:
- `V[t]` = membrane potential at time t
- `decay_step` = fixed linear decay value (not proportional to V)
- `w_i` = synaptic weight
- `s_i[t]` = input spike (0 or 1)

### SRAM Cell as Computing Element

Standard 6T SRAM cells are repurposed for computation:

```
SRAM CIM Cell Operation:
  ┌─────────────────────────────────────────────┐
  │  Weight stored as cell state (W or ~W)       │
  │  Input spike applied to wordline (WL)        │
  │  Bitline current ∝ weight × spike            │
  │  Sense amplifier converts analog → digital   │
  └─────────────────────────────────────────────┘
```

## Architecture Design

### Crossbar Array Organization

```
                 Input Spikes (s_1 ... s_N)
                      │   │       │
                      ▼   ▼       ▼
              ┌─────┬─────┬───┬─────┐
        W_11  │  ●  │  ●  │...│  ●  │ ← Neuron 1 (Column 1)
        W_21  │  ●  │  ●  │...│  ●  │ ← Neuron 2 (Column 2)
        W_31  │  ●  │  ●  │...│  ●  │ ← Neuron 3 (Column 3)
              └─────┴─────┴───┴─────┘
                │       │       │
                ▼       ▼       ▼
            Σ+ADC   Σ+ADC   Σ+ADC   ← Column-wise accumulation
                │       │       │
                ▼       ▼       ▼
            Neuron 1 Neuron 2 Neuron 3  ← Linear-decay update + threshold
```

### Hardware Components

| Component | Function | Design Considerations |
|-----------|----------|----------------------|
| **SRAM Crossbar** | Store weights, compute MAC in-place | 6T standard cells, row=inputs, columns=neurons |
| **Sense Amplifiers** | Convert bitline current to digital | Column-parallel, low-offset design |
| **ADC/DAC** | Analog-digital conversion for column sums | SAR ADC for power efficiency |
| **Neuron Circuits** | Linear-decay update + threshold check | Adder + comparator, no multiplier needed |
| **Spike Router** | Route output spikes to next layer | Digital logic, configurable connectivity |
| **Controller** | Sequence operations across time steps | FSM for time-stepped SNN execution |

### Linear-Decay Neuron Circuit

```verilog
module linear_decay_neuron (
    input wire clk,
    input wire reset,
    input wire signed [15:0] synaptic_input,  // From crossbar
    output reg spike_out,
    output reg signed [15:0] V_mem            // For debugging/monitoring
);
    reg signed [15:0] V_mem_reg;
    parameter V_THRESHOLD = 16'sh4000;  // Fixed threshold
    parameter V_RESET = 16'sh0000;
    parameter DECAY_STEP = 16'sh0400;   // Fixed linear decay
    
    always @(posedge clk) begin
        if (reset) begin
            V_mem_reg <= V_RESET;
            spike_out <= 0;
        end else begin
            // Linear decay: subtract fixed amount (no multiplication!)
            // Then add synaptic input from crossbar
            V_mem_reg <= V_mem_reg - DECAY_STEP + synaptic_input;
            
            // Threshold check
            if (V_mem_reg >= V_THRESHOLD) begin
                V_mem_reg <= V_RESET;
                spike_out <= 1;
            end else begin
                spike_out <= 0;
            end
        end
    end
    
    assign V_mem = V_mem_reg;
endmodule
```

## Advantages of Linear-Decay Model for CIM

### 1. Eliminates Multiplication in Neuron Update

Standard LIF requires:
```
V[t+1] = α × V[t] + Σ(w_i × s_i[t])    // Needs multiplication α × V[t]
```

Linear-decay requires:
```
V[t+1] = V[t] - δ + Σ(w_i × s_i[t])   // Only addition/subtraction!
```

The multiplications `w_i × s_i[t]` are handled by the SRAM crossbar. The neuron circuit itself needs only adders.

### 2. Simplified Peripheral Circuitry

| Operation | Standard LIF | Linear-Decay |
|-----------|-------------|--------------|
| Membrane decay | Multiplication | Subtraction (fixed value) |
| Threshold check | Comparator | Comparator (same) |
| Reset | Register write | Register write (same) |
| Hardware cost | Multiplier + adder | Adder only |

### 3. Power Efficiency

- **No neuron multipliers**: Removes power-hungry multiplication units
- **Sparse spike activity**: Only active neurons consume power
- **In-memory MAC**: Eliminates data movement energy
- **Linear scaling**: Power scales with spike activity, not network size

## Energy Efficiency Analysis

### Energy Breakdown (per inference step)

| Component | Standard Architecture | CIM Architecture |
|-----------|---------------------|------------------|
| Weight fetch from memory | ~10 pJ per weight | ~0 pJ (in-place) |
| MAC computation | ~1 pJ per MAC | ~0.1 pJ per MAC |
| Data movement | ~5 pJ per activation | ~0 pJ |
| Neuron update | ~2 pJ (with multiplier) | ~0.5 pJ (adder only) |
| **Total per step** | **~18 pJ** | **~0.6 pJ** |

**Estimated speedup: 30× lower energy per inference step**

### Comparison with Other Platforms

| Platform | Energy/Inference | Latency | Flexibility |
|----------|-----------------|----------|-------------|
| GPU (digital) | ~100 mJ | ms | High |
| CPU (digital) | ~10 mJ | ms | Highest |
| Neuromorphic ASIC (Loihi) | ~20 μJ | μs | Medium |
| **SRAM CIM SNN** | **~1 μJ** | **μs** | **Low** |

## Design Methodology

### Step 1: Network Specification

Define SNN architecture:
- Number of layers and neurons per layer
- Connection topology (sparse or dense)
- Weight precision requirements
- Time steps per inference

### Step 2: Linear-Decay Parameter Selection

Choose decay parameters to match desired temporal dynamics:

```python
def calibrate_linear_decay(target_tau, dt, V_thresh):
    """
    Calibrate linear decay step to approximate 
    exponential decay with time constant tau.
    
    Args:
        target_tau: Desired membrane time constant (ms)
        dt: Simulation time step (ms)
        V_thresh: Firing threshold
    Returns:
        decay_step: Fixed linear decay value
    """
    # Match average decay behavior
    # For LIF: dV/dt = -V/tau → V(t) = V0 * exp(-t/tau)
    # For linear: V(t) = V0 - (decay_step/dt) * t
    # Equate at half-life: V(t_half) = V0/2
    t_half = target_tau * np.log(2)
    decay_step = (V_thresh * dt) / (2 * t_half)
    return decay_step
```

### Step 3: Crossbar Mapping

Map weights to SRAM cells:

```python
def map_weights_to_crossbar(weights, num_rows, num_cols, bits_per_cell):
    """
    Map SNN weight matrix to SRAM crossbar array.
    
    Args:
        weights: Weight matrix [num_inputs x num_neurons]
        num_rows: Crossbar rows (input lines)
        num_cols: Crossbar columns (neurons)
        bits_per_cell: Precision per SRAM cell
    Returns:
        cell_values: Mapped values for each SRAM cell
    """
    # Quantize weights to crossbar precision
    q_weights = quantize_to_fixed(weights, bits_per_cell)
    
    # Handle sign: split into positive and negative arrays
    pos_weights = np.maximum(q_weights, 0)
    neg_weights = np.maximum(-q_weights, 0)
    
    # Map to differential pairs (if supported)
    return pos_weights, neg_weights
```

### Step 4: Peripheral Circuit Design

Design supporting circuits:
- Sense amplifiers for column readout
- ADC for analog-to-digital conversion
- Linear-decay neuron circuits
- Spike routing logic

### Step 5: System Integration

Combine components into complete accelerator:
- Controller FSM for time-stepped execution
- Input/output interfaces
- Configuration registers
- Test and debug interfaces

## When to Use

- Ultra-low power edge inference (<1mW budget)
- Always-on sensing applications (visual, auditory)
- Battery-powered IoT devices requiring SNN inference
- Wearable devices with strict energy constraints
- Applications where von Neumann bottleneck dominates energy

## Design Trade-offs

### Precision vs. Energy

| Weight Bits | Accuracy | Energy/Step | Crossbar Area |
|-------------|----------|-------------|---------------|
| 8-bit | Baseline | 1× | 1× |
| 4-bit | ~2-5% drop | 0.4× | 0.5× |
| 2-bit | ~5-15% drop | 0.2× | 0.25× |
| 1-bit (binary) | ~10-25% drop | 0.1× | 0.125× |

### Network Size vs. Performance

| Network Size | Feasible on CIM | Notes |
|-------------|-----------------|-------|
| < 1K neurons | Yes (single array) | Ideal for CIM |
| 1K-10K neurons | Yes (multi-array) | Requires tiling |
| 10K-100K neurons | Challenging | Inter-array communication overhead |
| > 100K neurons | Not recommended | Use neuromorphic chip instead |

## Related Skills

- **quantized-snn-hardware-optimization**: SNN quantization for hardware
- **snn-microcontroller-simulation**: SNN deployment on MCUs
- **analog-neuromorphic-plasticity**: Analog neuromorphic computing
- **spiking-neural-network-analysis**: SNN performance analysis

## Key References

- "SRAM-Based Compute-in-Memory Accelerator for Linear-decay Spiking Neural Networks." arXiv:2603.12739 (2026)
- Ambrogio et al. (2018) "Equivalent-accuracy accelerated neural-network training using analogue memory"
- Chen et al. (2020) "A fully-integrated 64Kb compute-in-memory SRAM macro"

---

**Integration Pattern**: Use this skill for designing ultra-low-power SNN inference accelerators. Combine with `quantized-snn-hardware-optimization` for weight compression, and with `snn-microcontroller-simulation` for hybrid MCU+CIM deployments where a microcontroller handles control and CIM handles MAC operations.

## Activation Keywords

- "sram-cim-snn-accelerator"
- "sram cim snn accelerator"
- "use sram cim snn accelerator"
- "sram cim snn accelerator help"
- "compute-in-memory spiking network"
- "linear-decay SNN hardware"
- "CIM crossbar SNN"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's CIM accelerator requirements (power budget, network size, precision)
2. Gather necessary context (target application, accuracy requirements)
3. Apply the linear-decay neuron model with SRAM crossbar architecture
4. Provide design recommendations and implementation guidance

## Examples

### Basic SRAM CIM SNN Accelerator usage
```
User: "Help me design a low-power SNN accelerator for edge inference"
→ Understand requirements → Propose CIM architecture with linear-decay neurons → Provide design → Follow up
```

### Advanced usage
```
User: "I need a sub-1mW SNN inference chip for always-on audio processing"
→ Analyze power budget → Select crossbar configuration → Calibrate linear-decay parameters → Design peripheral circuits → Provide complete architecture
```
