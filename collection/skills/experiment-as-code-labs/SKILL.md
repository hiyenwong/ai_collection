---
name: experiment-as-code-labs
description: >
  Experiment-as-Code (EaC) Labs — a declarative stack for AI-driven scientific discovery.
  Encodes experiments as declarative configurations compiled to device-level APIs, with three-layer
  architecture: specification (standardization/reproducibility), execution (safety/reliability),
  and orchestration (scalability/efficiency). Inspired by Infrastructure-as-Code (IaC) for cloud
  computing, adapted for physical lab automation. Use when designing autonomous lab systems,
  AI-scientist physical execution stacks, declarative experiment specifications, lab automation
  frameworks, instrument orchestration, or reproducible scientific workflows.
  Activation: experiment-as-code, EaC lab, autonomous lab, declarative experiment, lab automation,
  AI scientist physical execution, infrastructure-as-code lab, instrument orchestration,
  scientific workflow reproducibility, autonomous battery lab
---

# Experiment-as-Code (EaC) Labs

Based on: Yang et al. (2026) "Experiment-as-Code Labs: A Declarative Stack for AI-Driven Scientific Discovery" — arXiv:2605.04375

## Core Problem

AI scientists reason in digital environments but cannot execute physical experiments. Autonomous labs exist but use ad-hoc, non-portable, imperative scripts. The gap: no systems abstraction for managing heterogeneous, stateful, safety-constrained physical instruments.

## Three-Layer Stack

### 1. Specification Layer (Standardization + Reproducibility)

Encodes experimental intent as **declarative configurations** (EaC programs), not imperative scripts.

- Hides vendor-specific APIs behind unified abstractions
- Makes resources, parameters, dependencies, and execution semantics explicit
- Experiments are portable across labs and version-controllable
- Shim layer enables onboarding heterogeneous instruments via EaC schema

**Key insight**: Analogous to Infrastructure-as-Code (Terraform, etc.) for cloud computing.

### 2. Execution Layer (Safety + Reliability)

Validates and enforces constraints during physical operation.

- **Static checks**: Validate specs against device capabilities before execution
- **Safety checks**: Prevent unsafe operations based on validated constraints
- **Calibration checks**: Detect instrument drift
- **Runtime checks**: Monitor device faults and state violations during execution
- **Provenance tracking**: Record experimental intent and execution context

### 3. Orchestration Layer (Scalability + Efficiency)

Compiles validated specs into executable workflow DAGs and schedules over shared resources.

- **Resource assignment**: Manages contention for shared, stateful instruments
- **State-aware batching**: Groups compatible operations
- **Job scheduling**: Produces execution plans consulting live lab state
- **Fault handling**: Maintains data validity despite instrument faults

## Architecture Flow

```
Scientists/AI Agents
    │
    ▼ (1) EaC configs
Compiler
    │
    ├── (2) Static checks ← Query lab state
    │
    ▼ (3) Workflow DAGs
Scheduler
    │
    ├── (4) Query lab state → (5) State-aware execution plan
    │
    ▼
Execution Engine
    │
    ├── (6) Runtime checks ← Query live state
    ├── (7) Send device commands
    │
    ▼
Device Interface
    ├── (8) Send device-specific APIs (vendor translation)
    └── (9) Record telemetry → (10) Refresh lab state
```

## Key Design Patterns

### Declarative Experiment Specification

Experiments are written as ensembles of declarative configs (e.g., parameter sweeping) rather than device-specific imperative scripts. Benefits:
- **Reproducibility**: Version-controlled experiment definitions
- **Portability**: Run same EaC config across different lab setups
- **Safety**: Static validation catches errors before execution
- **AI Integration**: Well-defined digital interface for AI agents

### Centralized Lab State

A continuously maintained state model tracks all instruments:
```
pump_0:
  status: IN_USE
  flow_rate: 0.00028
  direction: CLOCKWISE
```
- Device telemetry updates state in real-time
- Compiler and scheduler query state for validation
- Enables closed-loop iteration between design and execution

### Shim Layer for Instrument Onboarding

New instruments are integrated via a shim layer that:
1. Encodes instrument capabilities in EaC schema
2. Maps unified operations to vendor-specific APIs
3. Provides state translation and API translation

## Comparison with Existing Approaches

| Approach | Portability | Static Checks | Composability | AI Integration |
|----------|------------|---------------|---------------|----------------|
| GUI workflows | ✗ | ✗ | ✗ | ✗ |
| Vendor scripts | ✗ | ✗ | ✗ | Partial |
| LIMS/ELN | Limited | Limited | Limited | Limited |
| **EaC** | **✓** | **✓** | **✓** | **✓** |

## Implementation Pattern

### Step 1: Define EaC Schema
Create declarative configuration format describing:
- Required resources (instruments, reagents)
- Parameters and their valid ranges
- Dependencies between operations
- Safety constraints

### Step 2: Build Compiler
- Parse EaC configs
- Static validation against lab state and device capabilities
- Lower to workflow DAGs with explicit dependencies

### Step 3: Implement Execution Engine
- Runtime state checks before each operation
- Fault detection and handling
- Telemetry collection and state refresh

### Step 4: Design Orchestration
- State-aware batching of compatible operations
- Resource contention management
- Priority-based scheduling

## Common Pitfalls

1. **Stateful instruments**: Unlike cloud resources, lab instruments maintain state between operations and are not cleanly time-sliceable.
2. **Irreversible actions**: Consumed reagents, contaminated wells cannot be "rolled back" like cloud provisioning.
3. **Calibration drift**: Instrument performance degrades over time; must detect and compensate.
4. **Physical safety**: Unlike cloud, unsafe operations can cause physical damage or injury.
5. **Multi-tenant contention**: Shared instruments require careful scheduling to avoid conflicts.

## Application Domains

- Battery research (cycling, characterization)
- Materials discovery
- Biological assays
- Chemical synthesis
- Any field requiring automated physical experimentation
