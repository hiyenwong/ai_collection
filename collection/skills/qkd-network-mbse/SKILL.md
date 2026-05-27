---
name: qkd-network-mbse
description: "Model-Based Systems Engineering (MBSE) methodology for designing and evolving Quantum Key Distribution (QKD) network architectures. Use when: designing quantum communication networks, applying MBSE/SysML to quantum systems, integrating quantum devices into classical infrastructure, modeling QKD network evolution, creating modular quantum system architectures, managing variability in quantum network designs. Activation: MBSE, quantum network, QKD, SysML, quantum systems engineering, quantum key distribution, model-based design, quantum architecture."
---

# QKD Network MBSE

## Description
Methodology for designing and evolving Quantum Key Distribution (QKD) network architectures using Model-Based Systems Engineering (MBSE) approaches. Combines Orthogonal Variability Modelling (OVM) and Systems Modelling Language (SysML) to create traceable, modular quantum network architectures.

Source: arXiv:2508.15733v1 - "Exploration of Evolving Quantum Key Distribution Network Architecture Using Model-Based Systems Engineering" (ISSE 2025)

## Core Methodology

### 1. Variability-Driven Architecture Design
- Use Orthogonal Variability Modelling (OVM) to capture architecture variants
- Define variability points: QKD protocol type, network topology, trust model, hardware integration
- Create traceable links between stakeholder requirements and architecture variants

### 2. SysML-Based Modeling
- Model QKD network components: quantum channels, classical channels, key management systems
- Define interfaces between quantum devices and existing classical infrastructure
- Create structural diagrams showing modular, reusable architecture patterns

### 3. Architecture Evolution Framework
- Model existing QKD network proposals as baseline architectures
- Define evolution paths: point-to-point → trusted relay → quantum repeater → fully quantum
- Track how increasing stakeholder expectations drive architectural changes

### 4. Integration Strategy
- Map quantum device capabilities to classical infrastructure requirements
- Identify integration points: sensors, computing, timing, communication
- Design migration paths from classical to quantum-secure systems

## Key Patterns

### Pattern 1: Modular QKD Architecture
```
Stakeholder Requirements → OVM Variability Model → SysML Architecture → Traceable Artefacts
```

### Pattern 2: Evolution Modeling
```
Current State (QKD proposal) → Variability Analysis → Future State Architecture → Migration Path
```

### Pattern 3: Quantum-Classical Integration
```
Quantum Device Specs → Classical Infrastructure Map → Integration Points → System Architecture
```

## Application Steps

1. **Identify stakeholder expectations**: Security level, throughput, distance, cost constraints
2. **Model variability points**: Protocol variants (BB84, E91, CV-QKD), topology variants, trust models
3. **Create SysML diagrams**: Block diagrams, interface diagrams, sequence diagrams for QKD protocols
4. **Establish traceability**: Link requirements → variability → architecture → implementation
5. **Define evolution path**: Current → intermediate → target architecture with migration steps

## Related Patterns

- Distributed quantum computing (arXiv:2605.27027 - SQARL)
- Entanglement distillation (arXiv:2605.26757)
- Quantum control systems engineering
- Fault-tolerant quantum network design

## Verification
- Architecture models should be traceable from requirements to design
- Each variability point should have clear inclusion/exclusion criteria
- Evolution paths should be validated against stakeholder requirement changes
