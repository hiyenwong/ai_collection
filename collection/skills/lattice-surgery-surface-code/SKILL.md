---
name: lattice-surgery-surface-code
description: "Lattice surgery methodology for fault-tolerant logical operations between distance-three surface-code logical qubits on planar superconducting processors. Enables deterministic Bell state preparation, two-qubit Deutsch-Jozsa at logical level, and magic-state injection for non-Clifford gates."
category: quantum
---

# Lattice Surgery Surface Code

## Description
Lattice surgery methodology from arXiv:2606.06598 (June 2026). Experimental realization of lattice-surgery operations between distance-three surface-code logical qubits on planar superconducting processor. Key results: per-cycle error rates of 0.0365 and 0.0282, logical Bell state fidelity confirmation, two-qubit Deutsch-Jozsa algorithm at logical level, and magic-state injection achieving logical R_X(π/4) gate fidelity of 0.943 conditioned on no detected errors. Establishes lattice surgery as practical paradigm for logical computation in near-term surface-code architectures.

## Activation Keywords
- lattice surgery surface code
- surface code logical operations
- distance-three logical qubits
- magic state injection
- logical gate fidelity
- 格手术表面码
- 逻辑量子比特

## Tools Used
- terminal: Run quantum circuit simulations, surface code decoders
- read_file: Read error correction code specifications
- search_files: Search for QEC implementations

## Core Concepts

### Surface Code Basics
- **Planar surface code**: 2D array of physical qubits with stabilizer measurements
- **Distance-d code**: Can correct up to ⌊(d-1)/2⌋ errors; distance-3 corrects 1 error
- **Logical qubits**: Encoded in surface code using stabilizer formalism

### Lattice Surgery Operations
1. **Merge**: Two logical patches are merged by measuring joint stabilizers across boundary
2. **Split**: A logical patch is split by measuring new stabilizers within the patch
3. **Joint initialization**: Preparing entangled states between patches
4. **Lattice splitting**: Deterministically separating entangled patches

### Key Achievements (arXiv:2606.06598)
- **Per-cycle error rates**: 0.0365(2) and 0.0282(1) after leakage rejection
- **Logical Bell state**: Prepared via joint initialization + lattice splitting
- **Bipartite entanglement**: Confirmed via error-corrected logical state fidelity
- **Deutsch-Jozsa at logical level**: Demonstrated algorithmic utility in FT framework
- **Magic-state injection**: Achieved logical R_X(π/4) with fidelity 0.943_{-9}^{+10}
- **Continuous non-Clifford rotations**: Via gate teleportation from magic states

## Usage Patterns

### Pattern 1: Fault-Tolerant Two-Qubit Gate
When implementing logical two-qubit gates:
1. Use lattice surgery merge/split instead of transversal gates
2. Prepare logical Bell state via joint initialization
3. Apply lattice splitting to distribute entanglement
4. Verify via error-corrected state tomography

### Pattern 2: Magic-State Injection Pipeline
For universal gate set:
1. Prepare magic state in dedicated patch
2. Inject via gate teleportation to target logical qubit
3. Apply non-Clifford rotation (e.g., R_X(π/4))
4. Condition fidelity on syndrome detection

### Pattern 3: Surface Code Error Budget Analysis
For assessing logical qubit quality:
1. Measure per-cycle logical error rate
2. Track leakage event rate separately
3. Compute error-corrected fidelity (conditioned on no detection)
4. Compare against break-even threshold

## Instructions for Agents

### Step 1: Architecture Assessment
- Identify if target hardware supports planar surface code
- Determine available qubit connectivity for distance-3 encoding
- Assess syndrome extraction fidelity

### Step 2: Lattice Surgery Design
- Plan merge/split sequence for target logical operation
- Design boundary stabilizer measurement pattern
- Account for time overhead of surgery operations

### Step 3: Magic-State Preparation
- Design magic-state factory circuit
- Optimize injection protocol for target gate
- Budget for magic-state distillation if needed

### Step 4: Verification
- Implement error-corrected state tomography
- Track leakage events during syndrome extraction
- Report both raw and post-selected fidelities

## Error Handling
- **High per-cycle error rate**: If > 0.05, increase code distance or improve hardware
- **Leakage events**: Track and reject; consider leakage reduction units (LRUs)
- **Magic-state fidelity too low**: Implement distillation or improve preparation circuit

## Resources
- arXiv:2606.06598 - Superconducting surface-code processor with lattice-surgery logical operations
- Related: Surface codes, lattice surgery, magic-state distillation

## Related Skills
- quantum-fault-tolerance-benchmark - Benchmarking quantum error-correcting codes
- distributed-quantum-error-correction - Distributed QEC patterns
- fpga-quantum-error-decoder - FPGA-based QEC decoding
