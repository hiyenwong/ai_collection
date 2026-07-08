---
name: amplitude-encoded-quantum-reservoir-protocol
description: Online quantum reservoir computing protocol with amplitude encoding using mid-circuit measurement and reset - enables scalable hardware implementations without input buffering
arxiv_id: "2606.18991"
authors: "Giacomo Franceschetto, Pere Mujal, Rodrigo Martínez-Peña"
published: "2026-06-17"
categories: "quant-ph"
trigger_words: ["amplitude encoding quantum reservoir", "mid-circuit measurement reset", "quantum reservoir online protocol", "partial-trace quantum dynamics", "indirect measurement quantum reservoir", "online quantum processing"]
created: "2026-07-06"
source: "cron-hourly-research"
---

# Amplitude-Encoded Quantum Reservoir Protocol

## Overview

Introduces a quantum reservoir computing online protocol that realizes amplitude encoding on quantum hardware using mid-circuit measurement and reset operations. Preserves online operation, avoids input buffering, and keeps runtime linear in time steps.

## Core Findings

1. **Mid-Circuit Measurement + Reset**: Combines these operations to implement partial-trace dynamics underlying amplitude encoding on real quantum hardware.

2. **Indirect Measurement Scheme**: Provides access to reservoir observables without interrupting temporal processing.

3. **Online Operation Preserved**: Unlike other approaches, this method avoids input buffering and maintains linear runtime in number of time steps.

4. **Dual Monitoring**: Reservoir dynamics can be monitored through both direct measurements of input qubits and indirect measurements of memory qubits — enabling full system observation while isolating internal reservoir evolution.

## Methodology

- Use mid-circuit measurement and reset for partial-trace dynamics
- Implement indirect measurement scheme for continuous monitoring
- Validate on standard benchmark tasks
- Evaluate on real quantum hardware

## Design Principles

1. Use mid-circuit measurement+reset instead of full circuit execution for amplitude encoding
2. Separate input qubit monitoring from memory qubit monitoring for isolation
3. Keep runtime linear in time steps by avoiding input buffering
4. Protocol provides practical route toward scalable hardware implementations

## Activation

Use when: amplitude encoding for quantum reservoir computing, mid-circuit measurement protocols, online quantum temporal processing, quantum reservoir hardware implementation, partial-trace quantum dynamics