---
name: mbse-quantum-network-architecture
category: quantum-systems
description: Model-Based Systems Engineering (MBSE) methodology for evolving quantum network architectures. Uses Orthogonal Variability Modeling (OVM) and SysML for traceable, modular quantum system design.
created: 2026-06-04
source: arXiv:2508.15733
tags: [quantum, MBSE, systems-engineering, network-architecture, QKD, SysML]
---

# MBSE for Quantum Network Architecture

## Background
Engineering quantum systems (sensors, computing, timing, communication) requires integrating quantum devices into existing classical infrastructure. Model-Based Systems Engineering (MBSE) addresses the growing complexity of quantum-secure telecommunications and quantum network evolution.

## Key Methodology

### Orthogonal Variability Modeling (OVM)
- Separate core architecture from variable features
- Model mandatory vs optional components independently
- Track variability decisions through the system lifecycle
- Enable modular reuse across different quantum network proposals

### SysML Integration
- Use Systems Modeling Language for structural and behavioral modeling
- Create traceable artifacts linking requirements to design
- Model interfaces between quantum and classical subsystems
- Support simulation and validation of architecture choices

### Variability-Driven Framework
1. **Identify Stakeholder Expectations** — Performance, security, cost, scalability
2. **Model Core Architecture** — Essential components common to all QKD network variants
3. **Define Variability Points** — Where architectures diverge (protocol, topology, hardware)
4. **Create Traceable Variants** — Each variant is a composition of core + selected options
5. **Evolve with Expectations** — Update models as stakeholder needs change

## Application Steps
1. Start with OVM to identify mandatory and optional features of your quantum system
2. Model the system architecture in SysML with clear quantum/classical boundaries
3. Create variability models for each architectural decision point
4. Maintain traceability from requirements → architecture → implementation
5. Use models to evaluate integration challenges before building

## Pitfalls
- Treating quantum and classical subsystems as monolithic blocks — model interfaces explicitly
- Ignoring variability management — architectures evolve rapidly in quantum field
- Building without traceable requirements — leads to rework when specifications change
- Not modeling stakeholder expectations as first-class artifacts

## Verification
- All architectural decisions should be traceable to stakeholder requirements
- Each variant should be derivable from the core + variability model
- Interface specifications between quantum/classical components must be complete
- Model should support answering "what-if" questions about architecture changes

## Activation
MBSE, quantum network, QKD, systems modeling, SysML, OVM, variability modeling, quantum architecture, traceability, stakeholder requirements