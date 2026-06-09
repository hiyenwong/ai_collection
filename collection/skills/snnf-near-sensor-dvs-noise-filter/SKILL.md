---
name: snnf-near-sensor-dvs-noise-filter
description: >
  SNNF: SNN-based Near-Sensor Noise Filter for Dynamic Vision Sensors.
  Hardware-efficient BA noise filtering using compact EBBI representation,
  parallel memory architecture, and single-layer SNN classifier. Achieves
  AUC 0.89 with ~11% memory and ~40% logic of state-of-the-art filters.
  Ideal for resource-constrained edge DVS applications.
  Activation: SNNF, DVS noise filter, event-based binary image, background
  activity noise, near-sensor computing, dynamic vision sensor, EBBI,
  spatiotemporal filter, neuromorphic vision, 事件相机噪声过滤
---

# SNNF: SNN-based Near-Sensor Noise Filter for Dynamic Vision Sensors

Based on: Yang, Gopalakrishnan, Hong & Basu (2026), arXiv:2605.01937 [cs.NE]

## Core Problem

Dynamic Vision Sensors (DVS) produce spurious **Background Activity (BA) noise**
from intrinsic pixel circuitry imperfections (junction leakage, temporal noise).
BA noise increases computational overhead and energy consumption, especially under
low-light conditions. Near-sensor filtering is essential for edge applications.

## Key Innovation

SNNF combines three techniques for hardware-efficient noise filtering:
1. **Event-Based Binary Image (EBBI)**: 1-bit binary representation per pixel, eliminating timestamp storage
2. **Parallel Memory Bank Architecture**: Decouples memory size from sensor resolution
3. **Single-Layer SNN Classifier**: Replaces power-hungry multipliers with spike-based accumulation

## EBBI (Event-Based Binary Image) Representation

### Traditional Approaches vs EBBI

| Representation | Memory per Pixel | Temporal Info | Hardware Cost |
|---|---|---|---|
| SAE (Surface of Active Events) | nT bits (16-32) | Full timestamps | High |
| TS (Time Surface) | nT bits (16-32) | Normalized decay | High |
| **EBBI** | **1 bit** | Binary presence | **Very Low** |

### EBBI Construction

```python
# Accumulate events over a sliding window
ebbi = np.zeros((height, width), dtype=np.uint8)
for event in events_in_window:
    ebbi[event.y, event.x] = 1  # Mark pixel as active
# Reset cyclically for next window
```

EBBI sacrifices temporal precision for massive memory savings, but SNN compensates
by learning spatiotemporal patterns from accumulated binary frames.

## SNN Architecture

### Single-Layer SNN Classifier

```
Input: EBBI patches (spatial neighborhood)
    ↓
Hidden Layer: ~30 LIF neurons
    ↓
Output: Signal vs Noise classification
```

### LIF Neuron Dynamics

```
τm · dVm/dt = -Vm(t) + Rm · Isyn(t)
If Vm(t) ≥ Vth: s(t) = 1, Vm(t+) = Vreset
Else: s(t) = 0
```

- **Sparse Communication**: Only binary spikes transmitted
- **No Multipliers**: Simple accumulation logic replaces multiply-accumulate
- **Minimal Data Width**: Binary spikes minimize inter-neuron bandwidth

## Training Approach

1. Collect representative DVS data (signal + BA noise)
2. Train SNN using surrogate gradient methods
3. Optimize for AUC on signal vs noise classification
4. Quantize for hardware deployment

## Performance Results

| Metric | SNNF | MLPF [1] | STCF [21] |
|---|---|---|---|
| AUC | 0.89 | 0.89 | ~0.80 |
| Memory (FPGA) | ~11% of MLPF | 100% | Scales with resolution |
| Logic (FPGA) | ~40% of MLPF | 100% | Low |
| Throughput | 29 Meps | 25 Meps | Varies |
| ASIC Power | 1.48 mW | 40 mW | N/A |
| ASIC Area | ~13% of MLPF | 100% | N/A |

## Hardware Implementation

### FPGA
- Parallel memory banks for EBBI storage
- Cyclic reset mechanism avoids memory growth
- Low, deterministic latency (9 clock cycles)

### ASIC (65nm CMOS)
- 15 SRAM instances for parallel memory
- 0.5656 mm² total area
- 44.4 Meps throughput at 400 MHz
- Energy per event: ~1.47 nJ

## Comparison with Existing Filters

| Filter | Approach | Memory Scaling | Key Limitation |
|---|---|---|---|
| BAF [2] | STC principle, 1 support event | O(N) | High false positive rate |
| STCF [21] | STC, k support events | O(N) | Struggles with high-density noise |
| MLPF [1] | MLP on Time Surface | O(N) | Power-hungry, high memory |
| ONF [23] | O(N) space optimization | O(N) | Accuracy drops in dense scenes |
| Hashheat [29] | LSH + thermal values | Fixed | Suboptimal for dense patterns |
| **SNNF** | **SNN + EBBI** | **Fixed** | **Best accuracy-efficiency tradeoff** |

## Implementation Guidelines

### Step 1: EBBI Accumulation

```python
# Define accumulation window
window_size = 10  # ms
ebbi = np.zeros((H, W), dtype=np.uint8)

for event in event_stream:
    ebbi[event.y, event.x] = 1
    if time_elapsed(event, window_start) > window_size:
        # Process current EBBI
        result = classify_snn(ebbi)
        # Reset for next window
        ebbi.fill(0)
        window_start = event.timestamp
```

### Step 2: SNN Classification

```python
# Single-layer SNN with ~30 LIF neurons
class SNNFilter:
    def __init__(self, input_size, hidden_size=30):
        self.weights = initialize_weights(input_size, hidden_size)
        self.neurons = [LIFNeuron() for _ in range(hidden_size)]
    
    def classify(self, ebbi_patch):
        # Accumulate synaptic inputs
        for neuron in self.neurons:
            neuron.integrate(ebbi_patch @ self.weights[neuron.id])
            if neuron.fire():
                spike_count += 1
        return spike_count > threshold  # Signal vs Noise
```

### Step 3: Parallel Memory Architecture

```python
# Fixed number of memory banks, independent of resolution
NUM_BANKS = 15
memory_banks = [MemoryBank(size=BANK_SIZE) for _ in range(NUM_BANKS)]

# Hash-based bank selection
def get_bank(x, y):
    return hash_function(x, y) % NUM_BANKS
```

## Key Parameters

| Parameter | Description | Typical Value |
|---|---|---|
| Accumulation Window | EBBI temporal window | 5-20 ms |
| Hidden Neurons | SNN hidden layer size | ~30 |
| LIF Time Constant | Membrane decay rate | Task-dependent |
| Firing Threshold | Neuron spike threshold | Task-dependent |
| Memory Banks | Parallel bank count | 15 |

## When to Use SNNF

1. **Edge DVS Applications**: Resource-constrained devices with strict power budgets
2. **High-Resolution Sensors**: Where traditional filter memory scales prohibitively
3. **Always-On Systems**: Systems operating under tens of milliwatts power constraint
4. **Low-Light Conditions**: Where BA noise is most prominent

## Advantages

1. **Memory Efficiency**: 1-bit EBBI eliminates timestamp storage
2. **Hardware Simplicity**: SNN replaces multipliers with accumulators
3. **Scalability**: Parallel memory architecture decouples from sensor resolution
4. **Energy Efficiency**: Sparse spike-based computation minimizes energy
5. **High Throughput**: 29-44 Meps processing speed

## Pitfalls

1. **EBBI Temporal Loss**: Binary representation loses precise timing information
2. **Window Size Tuning**: Accumulation window must balance temporal context vs. latency
3. **Training Data**: SNN must be trained on representative DVS data for target environment
4. **Noise Density**: Performance may degrade under extremely high-density noise conditions
5. **Hardware Constraints**: SNN parameters must be quantized for target hardware platform

## Verification Steps

1. Verify AUC ≥ 0.89 on standard DVS datasets
2. Check memory usage scales independently of sensor resolution
3. Validate throughput meets application requirements (>29 Meps)
4. Confirm power consumption within edge application budget
5. Test filtering quality on target application scenarios

## Reference

Yang, Y., Gopalakrishnan, P. K., Hong, C. C., & Basu, A. (2026).
"SNNF: An SNN-based Near-Sensor Noise Filter for Dynamic Vision Sensors."
arXiv:2605.01937 [cs.NE].
