---
name: hpc-vqpu-architecture
version: v1.0.0
last_updated: 2026-05-30
description: "Service-export architecture for hosting virtual quantum processing units (vQPUs) on batch-scheduled HPC systems. Enables secure supercomputers to expose interactive, backend-oriented quantum interfaces while preserving topology, native-gate, and calibration semantics across queue delays and system scaling."
---

# HPC-vQPU Architecture

## Description

HPC-vQPU is a service-export architecture that bridges the gap between HPC batch-scheduled execution environments and the interactive, backend-oriented interfaces expected by quantum software stacks. It enables device-aware quantum simulation on HPC-scale accelerators while preserving quantum hardware semantics across queue delays, scaling, and calibration drift.

**arXiv**: 2605.28845
**Title**: HPC-vQPU: A Service-Export Architecture for Virtual QPUs on Batch-Scheduled HPC Systems
**Categories**: quant-ph, cs.DC

## Core Problem

Secure supercomputers expose batch-scheduled execution environments, but quantum software frameworks (Qiskit, Cirq, etc.) expect interactive, backend-oriented interfaces. The key obstacle is not just remote job submission — a vQPU must preserve:
- **Topology** — qubit connectivity maps
- **Native-gate semantics** — hardware-specific gate sets
- **Calibration semantics** — device calibration parameters that drift over time

These must be preserved across queue delays, batch scheduling, and heterogeneous system scaling.

## Architecture Components

### 1. Service-Export Layer
- Exposes quantum backend interfaces (REST/gRPC) compatible with standard quantum SDKs
- Translates interactive API calls into batch job specifications
- Maintains stateful session management across asynchronous execution

### 2. Virtual QPU Abstraction
- Virtualizes physical QPU properties (topology, noise model, gate set)
- Supports multiple backend types: real hardware, simulators, emulators
- Maintains calibration databases with timestamp-aware retrieval

### 3. Batch Integration Layer
- Maps quantum circuits to HPC batch scheduler formats (SLURM, PBS)
- Handles resource allocation for quantum simulation workloads
- Manages queue-aware scheduling with priority and preemption

### 4. Semantic Preservation
- **Topology preservation**: Maintains qubit connectivity across virtualization
- **Native-gate fidelity**: Ensures gate decomposition respects hardware constraints
- **Calibration awareness**: Tracks calibration timestamps and applies corrections

## Workflow for HPC Quantum Access

### Step 1: vQPU Registration
- Register physical/simulated QPU with HPC system
- Define topology, gate set, noise model, calibration schedule
- Create virtual endpoint accessible via standard quantum SDKs

### Step 2: Job Submission via SDK
- User submits quantum circuit via standard SDK (Qiskit, Cirq, etc.)
- SDK call routed to vQPU service endpoint
- vQPU validates circuit against topology and gate constraints

### Step 3: Batch Scheduling
- Validated circuit converted to batch job specification
- Job submitted to HPC scheduler with resource requirements
- Queue position tracked, estimated completion time communicated

### Step 4: Execution & Results
- Job executed on HPC accelerator (GPU/CPU quantum simulator)
- Results collected and returned via vQPU service
- User receives results asynchronously via callback or polling

## Implementation Considerations

### Queue Delay Management
- Calibration parameters may become stale during queue wait
- Implement calibration validity windows with automatic refresh
- Support speculative execution with calibration-aware post-processing

### Scaling Strategies
- Horizontal scaling: distribute circuits across multiple simulator instances
- Vertical scaling: leverage GPU/CPU acceleration for larger circuits
- Hybrid: mix real hardware access with simulation for hybrid algorithms

### Security
- Multi-tenant isolation on shared HPC infrastructure
- Secure credential management for quantum hardware access
- Audit logging for all quantum job submissions and results

## Integration with Quantum Workflows

This architecture enables:
- **Quantum-classical hybrid algorithms** on HPC systems
- **Large-scale quantum simulation** beyond desktop capabilities
- **Device-aware compilation** with accurate hardware models
- **Reproducible research** with preserved calibration snapshots

## Activation Keywords
- hpc quantum computing
- virtual qpu
- batch scheduled quantum
- quantum simulation hpc
- quantum service export
- quantum hpc architecture
- 虚拟量子处理器
- 高性能计算量子

## Resources
- Paper: https://arxiv.org/abs/2605.28845
- Related: quantum-systems-engineering, distributed-quantum-computing
