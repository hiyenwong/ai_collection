---
name: snn-microcontroller-simulation
description: "Full-feature Spiking Neural Network simulation on microcontrollers (RP2350) using IEEE 16-bit floating point. Demonstrates Synfire4 benchmark (1200 neurons) at 97.5% accuracy with 20mW power consumption. Enables neuromorphic edge computing with 5x better energy efficiency than ARM Cortex-A53. Triggers: SNN microcontroller, CARLsim MCU, 16-bit SNN, neuromorphic edge"
---

# Full-Feature SNN Simulation on Microcontrollers for Neuromorphic Edge Computing

> First demonstration of full-feature SNN simulator (CARLsim) running on resource-constrained microcontrollers (RP2350 with 8MB memory), achieving 97.5% accuracy on Synfire4 benchmark with only 20mW power consumption—5x more efficient than ARM application-class processors.

## Metadata
- **Source**: arXiv:2604.16474
- **Authors**: L. Niedermeier, J. L. Krichmar
- **Published**: 2026-04-11
- **Category**: Neuromorphic Computing, Edge AI

## Core Methodology

### Key Innovation
This work demonstrates that full-feature SNN simulations (previously requiring GPU workstations or specialized hardware like Intel Loihi) can run on low-power microcontrollers (MCUs). The breakthrough uses **IEEE 16-bit floating point (fp16)** to reduce memory requirements without loss of function, enabling neuromorphic applications at the edge with unprecedented SWaP (Size, Weight, and Power) efficiency.

### Technical Framework

#### 1. IEEE 16-bit Floating Point Optimization
- **Challenge**: SNN simulators typically require 32-bit floating point
- **Solution**: Implement IEEE 754 half-precision (16-bit) floating point
- **Memory Reduction**: 50% reduction in memory footprint
- **Accuracy**: 97.5% compared to single-precision baseline
- **Benefit**: Enables SNN simulation on 8MB MCU memory

#### 2. CARLsim Port to Microcontroller
- **Platform**: RP2350 microcontroller (Raspberry Pi Pico 2)
- **Memory**: 8MB external PSRAM
- **Features**: Full CARLsim feature set including:
  - Spike-timing dependent plasticity (STDP)
  - Synaptic weight updates
  - Neuron dynamics (LIF, Izhikevich)
  - Network topology management

#### 3. Real-time SNN Execution
- **Benchmark**: Synfire4 (186 neurons, scaled-down)
- **Performance**: Real-time execution
- **Power Consumption**: Only 20mW
- **Comparison**: 5x more energy efficient than ARM Cortex-A53
- **System Comparison**: 10x better than complete SoC (CPU + Board)

#### 4. Scalability Demonstration
- **Maximum Scale**: 1200 neurons (Synfire4 benchmark)
- **Accuracy**: 97.5% match to single-precision simulation
- **Capability**: Proves MCU-based neuromorphic computing is viable

## Implementation Guide

### Prerequisites
- Raspberry Pi Pico 2 (RP2350)
- 8MB external PSRAM
- CARLsim MCU port
- ARM GCC toolchain

### Step-by-Step Implementation

#### Step 1: Setup Development Environment
```bash
# Install ARM GCC toolchain
sudo apt-get install gcc-arm-none-eabi

# Clone CARLsim MCU port
git clone https://github.com/carlsim-snn/carlsim-mcu.git
cd carlsim-mcu

# Setup build environment
mkdir build && cd build
cmake -DCMAKE_TOOLCHAIN_FILE=../cmake/arm-none-eabi.cmake ..
```

#### Step 2: Configure 16-bit Floating Point
```cpp
// carlsim_mcu_config.h
#ifndef CARLSIM_MCU_CONFIG_H
#define CARLSIM_MCU_CONFIG_H

// Enable IEEE 754 half-precision (16-bit) floating point
#define USE_FP16 1

// Memory allocation settings
#define MAX_NEURONS 1200
#define MAX_SYNAPSES 50000
#define HEAP_SIZE (8 * 1024 * 1024)  // 8MB PSRAM

// Precision configuration
#ifdef USE_FP16
    typedef __fp16 float_t;  // ARM half-precision float
    #define FLOAT_EPSILON 9.77e-04f  // 2^-10
#else
    typedef float float_t;
    #define FLOAT_EPSILON 1.19e-07f  // 2^-23
#endif

#endif
```

#### Step 3: Implement FP16 Neuron Dynamics
```cpp
// lif_neuron_fp16.h
#ifndef LIF_NEURON_FP16_H
#define LIF_NEURON_FP16_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

// LIF neuron state in FP16
typedef struct {
    __fp16 v_mem;        // Membrane potential
    __fp16 v_rest;       // Resting potential
    __fp16 v_thresh;     // Threshold potential
    __fp16 v_reset;      // Reset potential
    __fp16 tau_m;        // Membrane time constant
    __fp16 tau_ref;      // Refractory period
    uint32_t ref_count;  // Refractory counter
    uint8_t fired;       // Spike flag
} LIFNeuronFP16;

// Update neuron state with FP16 precision
static inline void lif_update_fp16(LIFNeuronFP16* neuron, __fp16 input_current) {
    if (neuron->ref_count > 0) {
        neuron->ref_count--;
        neuron->v_mem = neuron->v_rest;
        neuron->fired = 0;
        return;
    }
    
    // LIF dynamics: dv/dt = -(v - v_rest)/tau_m + I
    __fp16 dv = -(neuron->v_mem - neuron->v_rest) / neuron->tau_m + input_current;
    neuron->v_mem += dv;
    
    // Check for spike
    if (neuron->v_mem >= neuron->v_thresh) {
        neuron->fired = 1;
        neuron->v_mem = neuron->v_reset;
        neuron->ref_count = (uint32_t)(neuron->tau_ref);
    } else {
        neuron->fired = 0;
    }
}

#ifdef __cplusplus
}
#endif

#endif
```

#### Step 4: Synaptic Weight Update (STDP)
```cpp
// stdp_fp16.h
#ifndef STDP_FP16_H
#define STDP_FP16_H

#include <stdint.h>
#include "carlsim_mcu_config.h"

// STDP learning rule with FP16 precision
typedef struct {
    __fp16 A_plus;    // LTP amplitude
    __fp16 A_minus;   // LTD amplitude
    __fp16 tau_plus;  // LTP time constant
    __fp16 tau_minus; // LTD time constant
    __fp16 w_max;     // Maximum weight
    __fp16 w_min;     // Minimum weight
} STDPParamsFP16;

// Compute weight update using STDP
static inline __fp16 stdp_update_fp16(
    STDPParamsFP16* params,
    __fp16 current_weight,
    int32_t delta_t  // Pre-post timing difference
) {
    __fp16 dw = 0.0f;
    
    if (delta_t > 0) {
        // Pre before Post: LTP
        dw = params->A_plus * exp(-((__fp16)delta_t) / params->tau_plus);
    } else if (delta_t < 0) {
        // Post before Pre: LTD
        dw = -params->A_minus * exp(((__fp16)(-delta_t)) / params->tau_minus);
    }
    
    __fp16 new_weight = current_weight + dw;
    
    // Clamp to bounds
    if (new_weight > params->w_max) new_weight = params->w_max;
    if (new_weight < params->w_min) new_weight = params->w_min;
    
    return new_weight;
}

#endif
```

#### Step 5: Synfire4 Benchmark Implementation
```cpp
// synfire4_benchmark.c
#include "carlsim_mcu.h"
#include "lif_neuron_fp16.h"
#include "stdp_fp16.h"

#define SYNFIRE4_NEURONS 186  // Scaled for MCU
#define SYNFIRE4_LAYERS 4
#define NEURONS_PER_LAYER 40

// Create Synfire4 chain network
void create_synfire4_chain(CARLsimMCUNet* net) {
    // Layer configuration
    int neurons_per_layer = SYNFIRE4_NEURONS / SYNFIRE4_LAYERS;
    
    // Create excitatory neuron groups
    int g0 = createGroup(net, "layer0", neurons_per_layer, EXCITATORY_NEURON);
    int g1 = createGroup(net, "layer1", neurons_per_layer, EXCITATORY_NEURON);
    int g2 = createGroup(net, "layer2", neurons_per_layer, EXCITATORY_NEURON);
    int g3 = createGroup(net, "layer3", neurons_per_layer, EXCITATORY_NEURON);
    
    // Set LIF parameters
    LIFNeuronFP16 lif_params = {
        .v_rest = 0.0f,
        .v_thresh = 1.0f,
        .v_reset = 0.0f,
        .tau_m = 10.0f,
        .tau_ref = 2.0f
    };
    
    setNeuronParameters(net, g0, &lif_params);
    setNeuronParameters(net, g1, &lif_params);
    setNeuronParameters(net, g2, &lif_params);
    setNeuronParameters(net, g3, &lif_params);
    
    // Feed-forward connections with STDP
    STDPParamsFP16 stdp_params = {
        .A_plus = 0.1f,
        .A_minus = 0.1f,
        .tau_plus = 20.0f,
        .tau_minus = 20.0f,
        .w_max = 1.0f,
        .w_min = 0.0f
    };
    
    // Connect layers
    connect(net, g0, g1, "full", 0.5f, &stdp_params);
    connect(net, g1, g2, "full", 0.5f, &stdp_params);
    connect(net, g2, g3, "full", 0.5f, &stdp_params);
    
    // Input stimulation
    int input_group = createGroup(net, "input", 10, INPUT_NEURON);
    connect(net, input_group, g0, "random", 0.8f, NULL);
}

// Run benchmark
int main() {
    CARLsimMCUNet net;
    initNetwork(&net);
    
    create_synfire4_chain(&net);
    setupNetwork(&net);
    
    // Run simulation
    for (int t = 0; t < 1000; t++) {
        // Stimulate first layer periodically
        if (t % 50 == 0) {
            spikeInput(&net, "input");
        }
        
        runNetwork(&net, 1);
    }
    
    // Measure accuracy (synchronization)
    float accuracy = computeSynchronization(&net);
    printf("Synfire4 Accuracy: %.1f%%\n", accuracy * 100);
    
    return 0;
}
```

#### Step 6: Memory Management
```cpp
// memory_manager_mcu.c
#include <stdlib.h>
#include <string.h>
#include "carlsim_mcu_config.h"

// Custom memory allocator for PSRAM
static uint8_t* heap_base = NULL;
static size_t heap_offset = 0;

void init_memory_manager() {
    // Initialize PSRAM heap
    heap_base = (uint8_t*)psram_malloc(HEAP_SIZE);
    heap_offset = 0;
}

void* mcu_malloc(size_t size) {
    // Align to 4 bytes
    size = (size + 3) & ~3;
    
    if (heap_offset + size > HEAP_SIZE) {
        return NULL;  // Out of memory
    }
    
    void* ptr = heap_base + heap_offset;
    heap_offset += size;
    
    return ptr;
}

void mcu_free(void* ptr) {
    // Simple allocator - no individual free
    // Use reset for full deallocation
}

void mcu_reset_heap() {
    heap_offset = 0;
}

// Allocate neuron array with FP16 precision
LIFNeuronFP16* allocate_neurons_fp16(uint32_t count) {
    size_t size = count * sizeof(LIFNeuronFP16);
    return (LIFNeuronFP16*)mcu_malloc(size);
}

// Allocate synapse matrix with FP16 precision
__fp16* allocate_synapse_matrix_fp16(uint32_t pre_count, uint32_t post_count) {
    size_t size = pre_count * post_count * sizeof(__fp16);
    return (__fp16*)mcu_malloc(size);
}
```

#### Step 7: Power Measurement
```cpp
// power_measurement.c
#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/adc.h"

// Measure current consumption
float measure_power_mw() {
    // Configure ADC for current sense
    adc_init();
    adc_gpio_init(26);
    adc_select_input(0);
    
    // Read voltage (current sense resistor)
    const float conversion_factor = 3.3f / (1 << 12);
    uint16_t raw = adc_read();
    float voltage = raw * conversion_factor;
    
    // Convert to current (assuming 0.1 ohm sense resistor)
    float current = voltage / 0.1f;  // Amps
    
    // Power = V * I (3.3V rail)
    float power = 3.3f * current * 1000.0f;  // mW
    
    return power;
}

// Benchmark execution
void run_power_benchmark() {
    float power_samples[100];
    
    for (int i = 0; i < 100; i++) {
        power_samples[i] = measure_power_mw();
        sleep_ms(10);
    }
    
    // Compute average power
    float avg_power = 0.0f;
    for (int i = 0; i < 100; i++) {
        avg_power += power_samples[i];
    }
    avg_power /= 100.0f;
    
    printf("Average Power Consumption: %.1f mW\n", avg_power);
}
```

## Applications
- **Edge Neuromorphic Computing**: Real-time SNN processing on low-power devices
- **IoT Sensor Networks**: Distributed spiking neural processing
- **Wearable AI**: Always-on pattern recognition with minimal power
- **Robotic Control**: Low-latency sensorimotor loops
- **Brain-Computer Interfaces**: Portable SNN-based signal processing

## Pitfalls
- **Numerical Precision**: FP16 has limited range (~5.96e-8 to 65504); watch for overflow
- **Memory Fragmentation**: Simple allocator has no individual free—use full reset
- **PSRAM Latency**: External memory is slower than internal SRAM
- **Timing Variability**: Real-time execution requires careful timing calibration
- **Hardware Variability**: Different MCUs may have different fp16 support

## Related Skills
- spikingjelly-framework
- snn-fpga-hardware-software-codesign
- neuromorphic-continual-nuclear-ics

## Key Insights
1. **16-bit floating point** enables full-feature SNNs on 8MB microcontrollers
2. **97.5% accuracy** maintained vs single-precision simulation
3. **20mW power consumption** vs 100mW+ for ARM application-class processors
4. **RP2350** proves viable for real-time neuromorphic edge computing
5. **CARLsim MCU port** makes sophisticated SNNs accessible to edge developers

## Performance Comparison
| Platform | Power | Neurons | Efficiency |
|----------|-------|---------|------------|
| RP2350 MCU | 20mW | 186-1200 | **Baseline** |
| ARM Cortex-A53 | 100mW+ | 1200 | 5x less efficient |
| Intel Loihi | 1W | 100K+ | Specialized hardware |
| GPU Workstation | 200W+ | 1M+ | Not edge-deployable |
