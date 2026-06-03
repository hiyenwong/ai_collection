---
name: shia-sysml-hardware-interface
description: "SysML-Hardware Interface Architecture (SHIA) for model-centric verification. Keeps executable SysML models directly in the hardware verification loop without intermediate transformations. Use when: designing model-to-hardware interfaces, implementing hardware-in-the-loop (HiL) verification with MBSE/SysML, building digital threads between system models and physical hardware, or integrating SysML models with embedded systems for V&V. Keywords: SHIA, SysML, MBSE, hardware-in-the-loop, HiL, model-centric verification, digital thread, IBM Rhapsody, model-governed verification."
---

# SHIA: SysML-Hardware Interface Architecture for Model-Centric Verification

Based on: Lewis, Elsokary & Ji (2026). "SHIA: A Direct SysML-Hardware Interface Architecture for Model-Centric Verification." arXiv:2605.11248. Published in *Advanced Engineering Informatics*.

## Problem

In MBSE workflows, SysML models become authoritative references for system architecture, but once verification moves to hardware, the model is left behind. Domain-specific simulators, model transformations (M2M/M2T), and bespoke tool integrations take over, causing the model to drift out of sync with the physical implementation it was meant to govern.

## Core Innovation

SHIA keeps the executable SysML model **directly inside the verification loop**, exchanging messages with physical hardware without:
- Intermediate transformation chains (M2M, M2T)
- Co-simulation platforms (FMI-based)
- Broker-mediated plugins

## Architecture

### Two-Server Bidirectional Link

```
┌─────────────────┐         ┌─────────────────┐
│  SysML Server    │◄───────►│  Hardware Server │
│  (IBM Rhapsody   │  Socket │  (Raspberry Pi)  │
│   Embedded C++)  │  Link   │  + Sensors/Actua │
└─────────────────┘         └─────────────────┘
       │                            │
  SysML Statecharts             Physical I/O
  Behavioural Models            Hardware Logic
```

### Key Design Decisions

1. **SysML side server**: Embedded C++ within IBM Rhapsody
   - Implements message protocol for bidirectional communication
   - Executes behavioral statecharts as live controllers
   - Maintains model as authoritative reference during verification

2. **Hardware side server**: Runs on Raspberry Pi
   - Interfaces with physical sensors and actuators
   - Translates hardware signals to/from model-compatible messages
   - Operates as Hardware-in-the-Loop (HiL) node

3. **Direct socket connection**: No middleware, no brokers
   - Eliminates transformation overhead
   - Reduces model-to-hardware latency
   - Preserves semantic fidelity of the model

## Implementation Pattern

### Step 1: Model Construction
- Build SysML model with Internal Block Diagrams (IBDs)
- Define behavioral statecharts for system logic
- Specify input/output ports for hardware interface

### Step 2: SysML Server Implementation
- Write embedded C++ code within Rhapsody environment
- Implement message serialization/deserialization
- Connect statechart execution to message I/O

### Step 3: Hardware Server Implementation
- Deploy server on embedded platform (e.g., Raspberry Pi)
- Implement hardware abstraction layer for I/O
- Connect to SysML server via socket

### Step 4: Staged Verification
- Verify SysML server in isolation (Model Only Mode)
- Verify hardware server in isolation
- Integrate and verify bidirectional communication
- Validate model outputs against hardware outputs (e.g., Karnaugh map comparison)

## Operating Modes

- **MOM (Model Only Mode)**: SysML server runs standalone for simulation
- **MRM (Model Replacement Mode)**: Hardware server substitutes model behavior

## Verification Methodology

1. Build SysML model of target system
2. Assemble physical prototype
3. Design test harness for both sides
4. Verify SysML server behavior in MOM
5. Verify hardware server independently
6. Integrate and test bidirectional messaging
7. Compare model-generated vs hardware-generated outputs (zero discrepancy expected)

## Benefits

- **Model governance**: SysML remains authoritative throughout V&V lifecycle
- **Shorter digital thread**: Direct link between architecture and implementation
- **No transformation drift**: Model stays in sync with hardware behavior
- **Actionable verification**: Model can stimulate, observe, and verify hardware directly
- **Traceability**: Every hardware behavior traceable to model element

## Pitfalls

- Requires IBM Rhapsody with embedded C++ capability
- Initial setup complexity for server implementation
- Network/socket reliability must be ensured for real-time verification
- Case study demonstrated with logic gates; scaling to complex systems requires additional validation

## Activation

- SHIA architecture
- SysML hardware interface
- Model-centric verification
- MBSE HiL integration
- SysML-to-hardware connection
- Model-governed verification
