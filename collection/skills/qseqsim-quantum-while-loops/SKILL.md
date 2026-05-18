---
name: qseqsim-quantum-while-loops
description: "QSeqSim: Qiskit-integrated symbolic backend for simulating while-loop quantum programs using sequential quantum circuits. Fills gap of no Qiskit-native support for iterative quantum programs."
category: quantum
tags: [qiskit, quantum-simulation, while-loops, sequential-circuits, symbolic-computation, QSeqSim]
arxiv_id: "2605.14881"
published: "2026-05-15"
---

# QSeqSim: Symbolic Simulation for Quantum While Loops

## Core Idea

QSeqSim is a **Qiskit-integrated symbolic backend** that enables simulation of **while-loop quantum programs** by converting them into **sequential quantum circuits**. It fills the gap of having no Qiskit-native support for iterative quantum programs.

## Problem

Standard quantum circuit simulators handle **static circuits** only. Many quantum algorithms require:

- Iterative amplitude amplification
- Adaptive measurement-based protocols
- Feedback-driven quantum control
- Repeat-until-success algorithms

These require **while-loops** which are not natively supported in Qiskit.

## Solution: Sequential Circuit Transformation

### How It Works

1. **Symbolic analysis** of the while-loop quantum program
2. **Unrolling** the loop into a sequential circuit with bounded iterations
3. **Qiskit integration** as a custom backend
4. **Efficient simulation** using symbolic state representation

### Key Features

- **Qiskit-native**: Integrates seamlessly with existing Qiskit workflows
- **Symbolic backend**: Uses symbolic representation for efficient state tracking
- **Bounded unrolling**: Converts while-loops to sequential circuits with iteration bounds
- **Measurement handling**: Properly handles mid-circuit measurements and conditional operations

## Usage Pattern

```python
from qseqsim import QSeqSimBackend

# Create the symbolic backend
backend = QSeqSimBackend(max_iterations=10)

# Run while-loop quantum programs
result = backend.run(quantum_program_with_while_loop)
```

## Applications

- Iterative quantum algorithms (amplitude amplification variants)
- Adaptive quantum protocols
- Repeat-until-success quantum computing
- Quantum error correction with adaptive decoding
- Variational quantum algorithms with dynamic circuits

## Methodology

### Step 1: Program Analysis

Parse the quantum while-loop program to identify:
- Loop conditions (typically based on measurement outcomes)
- Quantum operations within the loop body
- Classical control flow dependencies

### Step 2: Sequential Unrolling

Transform the while-loop into a sequential circuit:
- Bound the maximum number of iterations
- Create sequential circuit blocks for each iteration
- Wire measurement outcomes to control subsequent blocks

### Step 3: Symbolic Execution

Execute the sequential circuit using symbolic state representation:
- Track quantum state symbolically rather than numerically
- Exploit structure for efficient computation
- Handle probabilistic branching from measurements

## Related Work

- Qiskit dynamic circuits
- OpenQASM 3.0 control flow
- Quantum program verification

## Activation Keywords

QSeqSim, quantum while loops, sequential quantum circuits, Qiskit backend, symbolic simulation, iterative quantum algorithms, dynamic circuits, repeat-until-success

## Related Papers

- arXiv: 2605.14881 - "QSeqSim: A Symbolic Simulator for Qiskit While Loops Using Sequential Quantum Circuits" (2026-05-15)
