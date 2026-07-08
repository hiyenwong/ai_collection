---
name: ntt-accelerator-pqc
category: post-quantum-cryptography
description: High-performance NTT accelerator design for post-quantum cryptography (PQC). Novel redundant number representation eliminates conditional corrections for Montgomery modulo multiplication and combined subtract-multiply operations.
trigger_words: NTT accelerator, post-quantum cryptography, Montgomery multiplication, redundant arithmetic, FPGA PQC, polynomial arithmetic hardware, ML-KEM, ML-DSA, CRYSTALS-Kyber, CRYSTALS-Dilithium
arxiv_id: 2607.00621
authors: George Alexakis, Dimitrios Schoinianakis, Giorgos Dimitrakopoulos
---

# High-Performance NTT Accelerators for PQC

## Overview

Post-quantum cryptography (PQC) schemes like ML-KEM (CRYSTALS-Kyber) and ML-DSA (CRYSTALS-Dilithium) rely heavily on large-degree polynomial arithmetic, making the Number Theoretic Transform (NTT) a key computational primitive. This skill covers optimized NTT/INTT accelerator design with novel arithmetic techniques.

## Core Innovations

### 1. Unified Redundant Number Representation
- Eliminates conditional corrections for Montgomery modulo multiplication
- Eliminates conditional corrections for combined subtract-multiply operations
- Reduces branching overhead and enables fully pipelined execution

### 2. Inverse-Transform Scaling Integration
- Integrates inverse-transform scaling into existing arithmetic hardware
- Avoids dedicated scaling units, reducing hardware cost
- Reuses Montgomery multiplier resources for both NTT and INTT

### 3. Hierarchical Montgomery Multipliers
- Maps efficiently onto FPGA DSP resources
- Reduces hardware cost while enabling high operating frequencies
- Supports both NTT and INTT with unified butterfly units

## Design Patterns

### Pattern 1: Unified Butterfly Unit
- Single hardware unit handles both forward (NTT) and inverse (INTT) transforms
- Uses redundant arithmetic to eliminate conditional branches
- Achieves higher clock frequencies through reduced critical path

### Pattern 2: Parallel Iterative Architecture
- Iterative NTT/INTT with parallel processing elements
- Exploits data parallelism at each stage of the Cooley-Tukey decomposition
- Balances resource utilization and throughput for FPGA implementation

### Pattern 3: DSP-Resource Mapping
- Hierarchical Montgomery multipliers aligned with FPGA DSP block structure
- Minimizes LUT/FF usage while maximizing DSP utilization
- Enables operation at higher frequencies than conventional implementations

## When to Use
- Designing hardware accelerators for post-quantum cryptography
- Implementing ML-KEM or ML-DSA on FPGA/ASIC platforms
- Optimizing polynomial multiplication in lattice-based cryptography
- Building privacy-preserving cryptographic hardware

## Performance Benefits
- Higher clock frequencies through reduced critical path
- Reduced execution times through parallelism and pipelining
- Competitive resource utilization (fewer DSP blocks, LUTs)
- Suitable for both embedded and high-throughput applications

## References
- arXiv: 2607.00621 - "High-Performance NTT Accelerators for PQC leveraging Unified Redundant Arithmetic and Fine-Tuned Microarchitecture"
