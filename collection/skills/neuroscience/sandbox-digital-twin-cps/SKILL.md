---
name: sandbox-digital-twin-cps
description: Sandbox-Enabled Digital Twin for Cyber-Physical Systems (CPS) - closed-loop validation framework that captures controller side-channels with simulated plant feedback
trigger_words:
  - digital twin
  - cyber-physical systems
  - CPS security
  - controller validation
  - side-channel analysis
  - sandbox testing
  - anomaly detection
  - OpenPLC
  - power system control
version: 1.0
paper_id: arxiv:2606.17001
authors: Meet Udeshi, Md Raz, Prashanth Krishnamurthy, Ramesh Karri, Farshad Khorrami
published: 2026-06-15
---

# Sandbox-Enabled Digital Twin for Cyber-Physical Systems

## Overview

Closed-loop digital twin framework for CPS controller validation that bridges the gap between traditional black-box I/O testing and open-loop side-channel analysis. Captures time-synchronized controller behavioral data alongside simulated plant conditions.

## Core Innovation

The SaMOSA Linux sandbox hosts an **unmodified controller binary** with I/O rerouted to an external plant simulator, enabling coupled capture of:
- Simulated plant conditions and events
- Controller behavioral side-channels (hardware performance counters, system calls, disk activity, network activity)
- Orchestrated repeatable runs with parameterized testing

## Methodology

### 1. Framework Architecture

```
Controller Binary → SaMOSA Sandbox → Plant Simulator
       ↓                    ↓                ↓
   Side-channels      I/O Rerouting    Plant State
       ↓                    ↓                ↓
   Time-synced Data Capture & Analysis
```

### 2. Four Captured Side-Channels

1. **Hardware Performance Counters**: CPU cycles, cache misses, branch mispredictions
2. **System Calls**: File operations, memory mappings, process control
3. **Disk Activity**: Read/write patterns, file access timestamps
4. **Network Activity**: Packet timing, protocol patterns, connection states

### 3. Closed-Loop Testing Protocol

```python
# Conceptual orchestration
class SaMOSADigitalTwin:
    def __init__(self, controller_binary, plant_model):
        self.sandbox = SaMOSASandbox(controller_binary)
        self.simulator = PlantSimulator(plant_model)
        
    def run_test_scenario(self, scenario_params):
        # 1. Initialize plant simulator with scenario
        # 2. Start sandboxed controller with I/O rerouting
        # 3. Capture synchronized side-channels + plant state
        # 4. Analyze behavioral correlation
        # 5. Detect anomalies or coverage gaps
        return time_synced_data
```

## Implementation Components

### SaMOSA Sandbox Features
- Linux-based execution environment
- I/O interception and rerouting
- Side-channel instrumentation hooks
- Orchestrated parameterized runs

### Plant Simulator Integration
- Modbus protocol support (IEEE 14-bus power system demonstrated)
- Real-time feedback injection
- Event injection capabilities
- State synchronization

## Demonstrated Applications

### Power System Control
- OpenPLC runtime executing Structured Text programs
- IEEE 14-bus power system model via Modbus
- Correlation of controller behavior with grid events

### Robotics Systems
- Extensible to robot controller validation
- Motor control anomaly detection
- Safety constraint verification

## Use Cases

1. **Pre-deployment Validation**: Test controllers under complex plant conditions
2. **Anomaly Detection**: Establish behavioral baselines for runtime monitoring
3. **Coverage Analysis**: Identify untested plant conditions
4. **Security Testing**: Detect fault/attack-induced behavioral deviations

## Key Advantages

- **Closed-loop observability**: Coupled plant + controller data
- **Unmodified binaries**: No instrumentation overhead
- **Side-channel diversity**: Four synchronized channels
- **Repeatability**: Parameterized orchestrated runs

## Limitations

- Requires Linux-based controllers
- Plant simulator fidelity affects validation accuracy
- Side-channel interpretation needs domain expertise
- Real-time performance constraints for production deployment

## Technical Requirements

- Linux sandboxing infrastructure
- Plant simulator with I/O protocol support (Modbus, ROS, etc.)
- Time-synchronization mechanisms
- Side-channel capture tools (perf, strace, syscall tracing)

## References

- Paper: arXiv:2606.17001
- SaMOSA sandbox architecture
- OpenPLC runtime environment
- IEEE 14-bus power system model