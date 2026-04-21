---
name: snn-microcontroller-simulation
version: v1.0.0
last_updated: 2026-04-21
description: "Full Feature Spiking Neural Network Simulation on Micro-Controller via Neuromorphic State Machine Framework. Enables complete SNN execution on resource-constrained MCUs using state machine abstraction for neuron dynamics, synapse updates, and spike routing. Activation: SNN microcontroller, MCU spiking network, neuromorphic state machine, edge SNN simulation, spiking neural network on microcontroller."
---

# SNN Microcontroller Simulation

Skill for deploying full-featured spiking neural network (SNN) simulation on resource-constrained microcontrollers using a neuromorphic state machine framework.

**Source:** arXiv:2604.16474 — "Full Feature Spiking Neural Network Simulation on Micro-Controller via Neuromorphic State Machine Framework"

## Core Concepts

### Neuromorphic State Machine Framework

The key insight is abstracting SNN components into state machines that can be efficiently executed on standard MCUs without specialized neuromorphic hardware:

- **Neuron State Machine**: Encodes LIF (Leaky Integrate-and-Fire) or other neuron dynamics as state transitions
- **Synapse State Machine**: Manages synaptic weight updates, plasticity rules, and spike-triggered postsynaptic currents
- **Spike Router State Machine**: Handles event-driven spike propagation between neurons with minimal memory overhead

### State Machine Abstraction

Each SNN component is decomposed into discrete states and transitions:

```
Neuron States:
  IDLE → INTEGRATING → SPIKING → REFRACTORY → IDLE

Synapse States:
  REST → SPIKE_RECEIVED → UPDATE_WEIGHTS → DECAY → REST

Spike Router States:
  IDLE → FETCH_SPIKE → ROUTE_TO_TARGET → QUEUE_UPDATE → IDLE
```

### Resource-Constrained Execution

Designed for deployment on MCUs with limited RAM/Flash (e.g., ARM Cortex-M, RISC-V):

- **Memory Efficiency**: State machine representation minimizes RAM footprint
- **Event-Driven**: Only active neurons/synapses consume compute cycles
- **Fixed-Point Arithmetic**: Avoids floating-point unit (FPU) dependency
- **Static Memory Allocation**: No dynamic allocation during inference

## Implementation Framework

### 1. Neuron State Machine (LIF)

```c
typedef enum {
    NEURON_IDLE,
    NEURON_INTEGRATING,
    NEURON_SPIKING,
    NEURON_REFRACTORY
} NeuronState;

typedef struct {
    int16_t V_mem;          // Membrane potential (fixed-point)
    int16_t V_thresh;       // Firing threshold
    int16_t V_reset;        // Reset potential
    int16_t tau_m;          // Membrane time constant
    int16_t refractory_cnt; // Refractory counter
    NeuronState state;
    uint8_t spike_flag;     // Output spike indicator
} NeuronSM;

void neuron_step(NeuronSM* n, int16_t input_current) {
    switch (n->state) {
        case NEURON_REFRACTORY:
            n->refractory_cnt--;
            if (n->refractory_cnt == 0) {
                n->state = NEURON_INTEGRATING;
            }
            n->spike_flag = 0;
            break;

        case NEURON_INTEGRATING:
            // LIF dynamics: dV/dt = -(V - V_rest) / tau + I
            n->V_mem = n->V_mem - (n->V_mem >> n->tau_m) + input_current;
            if (n->V_mem >= n->V_thresh) {
                n->state = NEURON_SPIKING;
                n->spike_flag = 1;
            }
            break;

        case NEURON_SPIKING:
            n->V_mem = n->V_reset;
            n->refractory_cnt = n->tau_m;
            n->state = NEURON_REFRACTORY;
            break;

        default:
            n->spike_flag = 0;
            break;
    }
}
```

### 2. Synapse State Machine

```c
typedef struct {
    int16_t weight;         // Synaptic weight (fixed-point)
    int16_t psc;            // Postsynaptic current
    int16_t tau_syn;        // Synaptic time constant
    uint16_t delay;         // Axonal delay (time steps)
    uint16_t delay_cnt;     // Delay counter
    uint8_t spike_pending;  // Spike in transit
} SynapseSM;

void synapse_step(SynapseSM* s) {
    // Exponential decay of PSC
    s->psc = s->psc - (s->psc >> s->tau_syn);

    if (s->spike_pending) {
        s->delay_cnt++;
        if (s->delay_cnt >= s->delay) {
            s->spike_pending = 0;
            s->delay_cnt = 0;
        }
    }
}

void synapse_trigger_spike(SynapseSM* s) {
    s->spike_pending = 1;
    s->delay_cnt = 0;
    s->psc += s->weight;
}

int16_t synapse_get_output(SynapseSM* s) {
    return s->psc;
}
```

### 3. Spike Router

```c
typedef struct {
    uint16_t src_id;
    uint16_t dst_id;
    uint16_t syn_idx;
} SpikeRoute;

// Circular spike queue for event-driven processing
#define SPIKE_QUEUE_SIZE 64
typedef struct {
    uint16_t buffer[SPIKE_QUEUE_SIZE];
    uint8_t head;
    uint8_t tail;
    uint8_t count;
} SpikeQueue;

void spike_queue_push(SpikeQueue* q, uint16_t neuron_id) {
    if (q->count < SPIKE_QUEUE_SIZE) {
        q->buffer[q->tail] = neuron_id;
        q->tail = (q->tail + 1) % SPIKE_QUEUE_SIZE;
        q->count++;
    }
}

uint16_t spike_queue_pop(SpikeQueue* q) {
    if (q->count == 0) return 0xFFFF;
    uint16_t val = q->buffer[q->head];
    q->head = (q->head + 1) % SPIKE_QUEUE_SIZE;
    q->count--;
    return val;
}

void process_spikes(SpikeQueue* q, NeuronSM* neurons, 
                    SynapseSM** synapses, SpikeRoute* routes,
                    uint16_t num_routes) {
    while (q->count > 0) {
        uint16_t src = spike_queue_pop(q);
        if (src == 0xFFFF) break;

        // Route spike to all downstream synapses
        for (uint16_t i = 0; i < num_routes; i++) {
            if (routes[i].src_id == src) {
                synapse_trigger_spike(
                    &synapses[routes[i].dst_id][routes[i].syn_idx]
                );
            }
        }
    }
}
```

### 4. Full SNN Simulation Loop

```c
void snn_simulate(NeuronSM* neurons, SynapseSM** synapses,
                  SpikeRoute* routes, SpikeQueue* spike_q,
                  uint16_t num_neurons, uint16_t num_routes,
                  uint16_t num_timesteps) {
    for (uint16_t t = 0; t < num_timesteps; t++) {
        // Phase 1: Update all neurons
        for (uint16_t i = 0; i < num_neurons; i++) {
            int16_t total_input = 0;
            // Sum synaptic inputs
            for (uint16_t j = 0; j < num_routes; j++) {
                if (routes[j].dst_id == i) {
                    total_input += synapse_get_output(
                        &synapses[i][routes[j].syn_idx]
                    );
                }
            }
            neuron_step(&neurons[i], total_input);

            // Queue spike if fired
            if (neurons[i].spike_flag) {
                spike_queue_push(spike_q, i);
            }
        }

        // Phase 2: Route spikes (event-driven)
        process_spikes(spike_q, neurons, synapses, routes, num_routes);

        // Phase 3: Update synapses
        for (uint16_t i = 0; i < num_neurons; i++) {
            for (uint16_t j = 0; j < /* fan_in */; j++) {
                synapse_step(&synapses[i][j]);
            }
        }
    }
}
```

## MCU Optimization Techniques

### Memory Management

| Component | Strategy | Savings |
|-----------|----------|---------|
| Neuron states | Struct-of-arrays (SoA) layout | Better cache utilization |
| Synapse weights | Sparse CSR format | Eliminates zero-weight storage |
| Spike queues | Circular buffer, fixed size | No dynamic allocation |
| Routing table | Compressed adjacency list | Minimal RAM footprint |

### Fixed-Point Arithmetic

- Use Q15 or Q7.8 fixed-point format for membrane potentials
- Replace floating-point multiplies with bit-shifts where possible
- Scale thresholds and weights to integer range

### Energy Optimization

- **Sleep-mode integration**: Use MCU low-power timers between simulation steps
- **Sparse wake-up**: Only wake neurons with pending spikes
- **DMA-assisted routing**: Offload spike buffer transfers to DMA

## Deployment Considerations

### Target MCUs

| Platform | Typical Use | SNN Capacity |
|----------|-------------|--------------|
| STM32L4 | Ultra-low-power sensor node | ~500 neurons |
| ESP32-C3 | IoT edge inference | ~1000 neurons |
| nRF52840 | BLE wearable | ~300 neurons |
| RISC-V (CH32V) | Open-source edge AI | ~500 neurons |

### Model Conversion Workflow

1. **Train SNN** in framework of choice (SpikingJelly, Nengo, Brian2)
2. **Quantize weights** to fixed-point representation
3. **Export network topology** (connectivity, delays, neuron params)
4. **Generate C code** from state machine templates
5. **Compile for target MCU** with size optimization flags

## When to Use

- Deploying SNNs on battery-powered edge devices
- No access to specialized neuromorphic hardware (Loihi, TrueNorth)
- Real-time inference with strict power budget (<10mW)
- Sensor data processing on microcontroller-class hardware
- Prototyping neuromorphic algorithms before custom ASIC

## Advantages Over Specialized Hardware

- **No specialized hardware required**: Runs on any standard MCU
- **Full feature support**: All SNN components (neuron, synapse, routing)
- **Portable**: Cross-platform C implementation
- **Cost-effective**: Uses commodity microcontrollers
- **Development-friendly**: Standard toolchains (GCC, clang, Arduino)

## Limitations

- Slower than dedicated neuromorphic chips for large networks
- Limited by MCU memory for very large networks
- Real-time constraints for complex topologies

## Related Skills

- **quantized-snn-hardware-optimization**: SNN quantization techniques
- **spikingjelly-framework**: PyTorch-based SNN training
- **bio-neuron-snn-learning**: Biological learning rules for SNNs
- **snn-performance-analysis**: SNN performance evaluation

## Key References

- "Full Feature Spiking Neural Network Simulation on Micro-Controller via Neuromorphic State Machine Framework." arXiv:2604.16474 (2026)

---

**Integration Pattern**: Use this skill for deploying pre-trained SNNs on edge MCUs. Combine with `quantized-snn-hardware-optimization` for further energy reduction, and with `spikingjelly-framework` for the training pipeline.

## Activation Keywords

- "snn-microcontroller-simulation"
- "snn microcontroller simulation"
- "use snn microcontroller simulation"
- "snn microcontroller simulation help"
- "snn on MCU"
- "spiking network microcontroller"
- "neuromorphic state machine MCU"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific MCU deployment requirements
2. Gather necessary context (target MCU, network size, power budget)
3. Apply the neuromorphic state machine framework with appropriate optimizations
4. Provide implementation code and suggest next steps

## Examples

### Basic SNN Microcontroller Simulation usage
```
User: "Help me deploy an SNN on an STM32 microcontroller"
→ Understand MCU specs and network size → Apply state machine framework → Generate C code → Provide results
```

### Advanced usage
```
User: "I need a full-featured SNN simulation on an ESP32 with fixed-point arithmetic"
→ Clarify network topology → Quantize parameters → Generate optimized state machine code → Follow up
```
