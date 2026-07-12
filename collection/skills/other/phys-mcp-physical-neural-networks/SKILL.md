---
name: phys-mcp-physical-neural-networks
description: >
  phys-MCP: substrate-aware control plane architecture for heterogeneous Physical
  Neural Networks (PNNs) spanning molecular, chemical, biological, photonic,
  memristive, and mechanical substrates. Provides capability models, lifecycle
  semantics, telemetry interfaces, and digital-twin bindings. Includes wetware-facing
  API via Cortical Labs adapter. Use when: orchestrating physical neural networks,
  edge-cloud PNN integration, wetware computing, substrate-aware orchestration,
  neuromorphic hardware management, or biological neural network APIs.
  Activation: phys-MCP, physical neural network, PNN orchestration, wetware API,
  Cortical Labs, substrate-aware control, neuromorphic edge computing, digital twin
  neural network, heterogeneous neural substrates, biological computing control plane
---

# phys-MCP: Control Plane for Heterogeneous Physical Neural Networks

Based on: Fischer, Hariri & Otte (2026), arXiv:2605.04256

## Problem

Physical Neural Networks (PNNs) embed computation in material dynamics
(molecular, chemical, biological, photonic, memristive, mechanical). Each substrate
exposes distinct interfaces, timing behavior, observability limits, and lifecycle
requirements, making integration into edge-cloud software stacks difficult.

## Solution: phys-MCP Architecture

A substrate-aware orchestration architecture that exposes physical neural substrates
as discoverable and invocable resources for edge, fog, and cloud workflows.

### Core Components

1. **Capability Model**: Describes substrate properties (latency, resetability,
   plasticity, I/O modality) in a unified descriptor format
2. **Lifecycle Semantics**: Standardized states (init, calibrate, run, reset, teardown)
   adapted per substrate
3. **Telemetry Interfaces**: Substrate-specific observability with unified access
4. **Digital-Twin Bindings**: Twin-backed backends for simulation-verified execution
5. **Wetware-Facing API**: Cortical Labs adapter exposing biological neural substrates
   through the same control model

### Architecture Layers

```
┌──────────────────────────────────────┐
│  Workflow Orchestrator (edge/fog/cloud) │
├──────────────────────────────────────┤
│         phys-MCP Control Plane         │
│  ┌──────────┬──────────┬──────────┐   │
│  │Discovery │Capability│Lifecycle  │   │
│  │  Model   │  Model   │  Manager  │   │
│  └──────────┴──────────┴──────────┘   │
│  ┌──────────┬──────────┬──────────┐   │
│  │Telemetry │ Digital  │ Resource  │   │
│  │Collector │ Twin Mgr │  Matcher  │   │
│  └──────────┴──────────┴──────────┘   │
├──────────────────────────────────────┤
│  HTTP-backed │ Photonic │ Wetware    │
│  Execution   │ Backend  │ (Cortical) │
└──────────────────────────────────────┘
```

### Substrate Properties Captured

| Property | Description | Examples |
|----------|-------------|----------|
| Latency | Inference time range | Photonic: ns, Biological: ms |
| Resetability | Can state be cleared? | Memristive: partial, Chemical: full |
| Plasticity | Does substrate learn online? | Biological: yes, Photonic: no |
| I/O Modality | Input/output interface | Electrical, optical, chemical |
| Energy | Power consumption profile | Varies by orders of magnitude |

### Resource Matching

Runtime-aware matching improves over simple baselines by considering:
- Substrate capability fit for task requirements
- Current load and latency SLA
- Digital twin verification before execution
- Telemetry-based fault recovery

## Evaluation Results

- Descriptor-portable integration across heterogeneous backends
- Improved runtime-aware matching vs. simpler baselines
- Telemetry-aware recovery under representative faults
- Successful execution against API-backed wetware path
- Small local control-path overhead

## Implementation Considerations

### Integration Pattern
```python
# Register a new substrate
register_substrate(
    backend_type="photonic",
    capabilities={"latency_ms": 0.001, "plasticity": False},
    telemetry_endpoint="http://photonic-node:8080/telemetry",
    twin_model="twin_photonic_v1"
)

# Execute through control plane
result = execute(
    substrate="photonic",
    input_data=encoded_signal,
    verify_with_twin=True
)
```

### Key Pitfalls
- **Heterogeneous timing**: Different substrates have vastly different response times;
  async execution is essential
- **State management**: Some substrates (memristive) have persistent state between runs;
  reset semantics vary
- **Wetware constraints**: Biological substrates have limited lifespan and
  environmental requirements
- **Digital twin fidelity**: Twin accuracy determines pre-execution verification quality

## Related Skills
- `neural-digital-twins-bci` - Neural digital twin framework for BCI
- `equation-free-digital-twins` - Equation-free digital twins using Koopman operators
- `multi-agent-active-inference-digital-twins` - Multi-agent digital twin framework
- `snn-fpga-hardware-software-codesign` - SNN hardware-software co-design
