---
name: commuting-pauli-parallelization
description: >
  Methodology for optimizing parallel execution of commuting Pauli Product Rotations
  in fault-tolerant quantum computation. Use when: (1) compiling quantum programs to
  Pauli Product Measurements (PPMs), (2) reducing circuit depth in surface code
  architectures with lattice surgery, (3) scheduling commuting quantum operations
  under hardware port constraints, (4) optimizing logical-layer quantum compilation.
  Keywords: Pauli Product Rotation, commuting groups, lattice surgery, surface code,
  circuit depth optimization, fault-tolerant compilation, clique reshuffling, generator
  restructuring, QASMBench.
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Commuting Pauli Product Parallelization

Methodology from arXiv:2605.23738 (Sethi, Nambisan, Baker, May 2026).

## Core Problem

Fault-Tolerant Quantum Computation (FTQC) permits parallel execution of mutually commuting
Pauli Product Rotations (PPRs). However, per-qubit access point/port limits (e.g., two X and
two Z edges on the surface code) force commuting groups that exceed the budget to be split,
inflating circuit depth.

## Key Insight

Even when PPRs mutually commute (theoretically parallelizable), **hardware port constraints**
create an additional bottleneck. Each logical qubit tile has limited X and Z edges for
lattice surgery operations. When a commuting group requires more simultaneous operations
on a qubit than available ports, the group must be serialized.

## Two-Heuristic Optimization Framework

### 1. Clique Reshuffling

**What it does:** Permute commuting products within a commuting group and re-form
port-constrained subgroups.

**How it works:**
- Given a maximal commuting clique of PPRs
- Find alternative permutations of how products are grouped
- Each permutation distributes per-qubit port usage differently
- Select the permutation that minimizes the number of serial subgroups

**Algorithm:**
1. Identify maximal commuting cliques from the PPR sequence
2. For each clique, enumerate valid subgroupings respecting port budget
3. Find the grouping that minimizes total depth (number of subgroups)
4. Reshuffle products across groups to balance port usage

### 2. Generator Restructuring

**What it does:** Rewrite each commuting group as an equivalent generating set
with reduced per-qubit port pressure.

**How it works:**
- A set of commuting Paulis can be represented by a smaller generating set
- Different generating sets have different per-qubit Pauli weight distributions
- Find a generating set that minimizes max per-qubit port usage
- Execute the generators in parallel, then reconstruct the original products

**Algorithm:**
1. Convert commuting group to binary symplectic representation
2. Perform Gaussian elimination to find alternative generating sets
3. Select generating set with minimized per-qubit port pressure
4. Execute generators, classically compute original Pauli values

## Combined Approach

Apply clique reshuffling first, then generator restructuring on the resulting groups.

**Results (QASMBench benchmark):**
- Average hardware-limited depth reduction: **15-35%** over non-reordering baseline
- Up to **35%** maximum reduction on specific circuits
- Gains scale with per-qubit port budget
- Performance saturates near **20 ports** per qubit

## When to Use

- **Surface code with lattice surgery**: Primary target architecture
- **Logical compilation**: After programs are compiled to PPM sequences
- **Port-constrained hardware**: Any architecture with limited simultaneous
  operation capacity per qubit
- **Large commuting groups**: When theoretical parallelism exceeds hardware limits

## Implementation Notes

1. **Port budget varies**: Surface code typically has 2 X + 2 Z edges per tile
2. **Ancilla qubits**: Additional ancilla can increase effective port budget
3. **Trade-off**: Generator restructuring may increase total gate count while
   reducing depth — acceptable when depth is the bottleneck
4. **Scalability**: Heuristics remain relevant as hardware exposes more ports
5. **Integration**: Can be integrated into existing compilation pipelines as
   a post-processing optimization pass

## Related Patterns

- Qubit mapping and routing for physical-layer optimization
- Magic state distillation scheduling
- Time-optimal quantum computation with ancilla-assisted parallelism
- Pauli-based computation (PBC) optimization

## Activation

commuting pauli parallelization, pauli product rotation, PPR optimization,
lattice surgery compilation, surface code scheduling, clique reshuffling,
generator restructuring, quantum circuit depth reduction, fault-tolerant compilation
