---
name: distributed-quantum-compiler-scheduling
description: "Compiler techniques for scheduling and optimizing distributed quantum computers (DQCs). Covers teleportation-aware scheduling, utility-driven lookahead scheduling, EPR-capacity-aware early scheduling, frequency allocation and transpilation co-design, and code surgery synthesis for stabilizer codes. Use when: designing DQC compilers, optimizing quantum circuit scheduling across multi-chip systems, minimizing teleportation overhead, implementing lookahead-aware quantum compilation, scheduling cross-chip CNOT operations, synthesizing code surgery for stabilizer codes, reducing latency in distributed quantum execution, or working with quantum error correction code surgery (arXiv: 2605.21795 ATHENA, 2605.21746 GeneCS)."
---

# Distributed Quantum Compiler Scheduling

Methodology for compiling and scheduling quantum circuits on distributed quantum computers (DQCs) with multi-chip architectures connected via photonic interconnects.

## Problem Statement

Non-local CNOTs between chips are 4.3-7.7x slower and 4x more error-prone than local CNOTs within a chip. Block-level scheduling (existing approach) lacks lookahead across blocks and introduces latency.

## ATHENA: Utility-Driven Lookahead + EPR-Capacity-Aware Scheduling

From arXiv:2605.21795 (Yun et al., UT Austin + Cisco Quantum Lab).

### Key Insight 1: UMS (Utility-driven Lookahead with Multi-Candidate Block Scheduling)

- Schedule current block considering only *useful* future blocks in lookahead window
- A future block has utility if it shares overlapping qubits with the current block
- Maintain multiple candidate schedules during compilation
- Defer commitment to globally sub-optimal schedules early in compilation

### Key Insight 2: EES (EPR-Capacity-Aware Early Scheduling)

- Schedule future operations and their relocations *early* when EPR resources are available
- Avoid waiting for preceding blocks to finish before scheduling teleportations
- Reduces latency by overlapping teleportation preparation with computation

### Results

- Reduces teleportations by 34% on average (up to 65%)
- Reduces latency by 2x on average (up to 2.9x)

## GeneCS: Code Surgery for Arbitrary Stabilizer Codes

From arXiv:2605.21746 (Zhou et al., UT Austin).

Resource-efficient compiler for synthesizing code surgery protocols for arbitrary quantum stabilizer codes:

- Structure-aware optimizations eliminate redundancy in graph construction
- Dynamically balance expansion and congestion
- Incorporate code degree constraints
- Reduces ancillary qubits and checks by 10x for single-code and cross-code operations
- Scales to codes with 1000+ qubits at ~1 second per instance

## Workflow

### Step 1: Identify DQC Architecture

- Map chip topology and interconnect bandwidth
- Determine EPR pair generation rate and fidelity
- Characterize local vs non-local gate costs

### Step 2: Decompose Circuit into Blocks

- Group CNOTs with overlapping qubits into blocks
- Identify cross-chip dependencies
- Build qubit-chip assignment graph

### Step 3: Apply UMS Scheduling

```
For each block B_i in topological order:
    1. Identify useful future blocks (shared qubits)
    2. Generate multiple candidate schedules
    3. Score each candidate by: teleportation cost + future impact
    4. Defer globally sub-optimal candidates
    5. Commit best schedule for B_i
```

### Step 4: Apply EES Early Scheduling

```
While EPR capacity available:
    1. Identify future teleportation needs
    2. Schedule teleportations ahead of computation
    3. Overlap EPR generation with ongoing computation
```

### Step 5: Code Surgery Synthesis (for FTQC)

For fault-tolerant operations on stabilizer codes:
1. Build measurement graph for logical operations
2. Apply structure-aware graph optimization
3. Balance expansion vs congestion
4. Enforce code degree constraints
5. Generate executable surgery protocol

## Pitfalls

- **Naive lookahead expansion**: Simply expanding the lookahead window to include all subsequent blocks does NOT solve the lookahead problem — must filter by *utility* (shared qubits)
- **EPR resource waste**: Schedule teleportations only when EPR pairs are actually available; otherwise wait and overlap with computation
- **Block ordering**: Topological order matters — schedule blocks with fewer cross-chip dependencies first
- **Code surgery overhead**: Theoretical constructions incur substantial ancilla overhead; use structure-aware optimization to eliminate redundancy

## Activation Keywords

ATHENA, DQC compiler, distributed quantum computer scheduling, teleportation optimization, utility-driven lookahead, EPR capacity, code surgery, stabilizer codes, GeneCS, cross-chip CNOT, quantum transpilation
