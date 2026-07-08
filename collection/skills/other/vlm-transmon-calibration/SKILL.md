---
name: vlm-transmon-calibration
description: "Self-specializing Vision-Language Model agent for physics-grounded transmon chip calibration. Uses zero-weight-update online adaptation via human-readable device notes, gradient-free strategy refinement with paired-snapshot accept gate, and physics-grounded simulation with realistic drift/wall-time/leakage. Activation: transmon calibration, quantum chip tuning, VLM calibration agent, gradient-free online adaptation, superconducting qubit calibration, 量子芯片校准"
metadata:
  arxiv_id: "2607.03193"
  published: "2607-07-03"
  authors: "VLM transmon calibration authors"
  tags: [quantum, calibration, vlm, transmon, gradient-free, online-adaptation]
---

# VLM Transmon Chip Calibration

## Core Methodology

**Problem**: Superconducting transmon chip calibration is a sequential decision problem under noise, drift, and finite budget. Experts must choose experiments, read plots, judge fits, and revise beliefs as chips drift.

**Solution**: VLM agent closes the calibration loop end-to-end via 3 co-designed artifacts:

1. **Physics-grounded simulation environment**
   - Calibration observables from circuit-quantized parameters (scqubits)
   - Realistic flux-line distortion, wall-time-scaled drift, gate leakage
   - Each tool call advances modeled clock — drift accrues by wall time, not call count

2. **Vision-Language Agent loop**
   - Calls tools, reads plots, maintains structured notebook
   - Submits parameters without hidden truth access
   - Scored against hidden parameters and measured gate fidelities

3. **Gradient-free online adaptation**
   - Reflector reads truth-free anomaly signatures from past attempts
   - Grows small human-readable device note appended to prompt
   - Paired-snapshot accept gate isolates strategy improvement from drift

**Results**: On hard-tier chip, 6 iterations raised worst-case CZ fidelity from 0.678→0.787. Single accepted note raised CZ from 0.678→0.913 on paired snapshot.

## Key Design Patterns

### Pattern 1: Physics-Grounded Simulation
When simulating quantum hardware for agent training:
- Derive observables from actual circuit parameters (scqubits)
- Include realistic noise: flux-line distortion, wall-time drift, gate leakage
- Advance simulation clock per action — drift is time-based, not step-based

### Pattern 2: Gradient-Free Online Adaptation
When adapting an agent without weight updates:
- Maintain structured notebook of past attempts
- Extract anomaly signatures (patterns of failure without truth access)
- Append concise device notes to prompt
- Use paired-snapshot accept gate: compare strategy on frozen snapshot before/after

### Pattern 3: Planted-Fault Diagnosis
When testing calibration agent capabilities:
- Plant known hardware faults in simulation
- Verify agent diagnoses faults truth-free
- Measure: does the device note causally improve fidelity?

## Activation Keywords
- transmon chip calibration
- quantum chip tuning agent
- VLM calibration
- gradient-free online adaptation
- superconducting qubit calibration
- physics-grounded quantum simulation
- 量子芯片校准
- 超导量子比特标定

## Related Skills
- `hardware-safety-gated-llm-quantum-control` — LLM-written quantum control
- `rl-ion-shuttling` — RL for trapped-ion control
- `model-based-rl-quantum-control` — RL for robust quantum control
- `vibe-calibration-autonomous-quantum` — autonomous quantum calibration
