---
name: ft-primitive-bench
description: "FTPrimitiveBench methodology for fault-tolerant quantum computing benchmarking. Provides systematic approach for evaluating QEC protocols under hardware-motivated noise models including Pauli bias, measurement bias, and spatio-temporal non-uniformity. Use when: (1) analyzing fault-tolerant quantum computing performance, (2) benchmarking QEC codes under realistic noise, (3) comparing decoders for surface code, (4) studying logical primitive operations (memory, lattice surgery, Hadamard, phase gate), (5) hardware-aware quantum architecture co-design, (6) noisy stabilizer simulation workflows."
---

# FTPrimitiveBench - Fault-Tolerant Primitive Benchmarking

Systematic benchmarking methodology for studying how logical primitives interact with hardware-motivated noise in fault-tolerant quantum computing.

## Core Concept

FTPrimitiveBench standardizes the link between noise-model specification and logical primitive construction. It extends memory-only benchmarks to **active logical computation**, where the interaction between noise structure and primitive implementation matters.

**Key Insight**: Structured noise (Pauli bias, measurement bias, spatial non-uniformity) affects logical primitives in qualitatively distinct ways, shaped by the interplay between noise model, primitive type, and decoder choice.

## Noise Model Families

### 1. Pauli Bias
- Asymmetric rates for X, Y, Z errors
- Common in superconducting qubits (dephasing dominant)
- Can be exploited by biased-noise codes (XZZX surface code)

### 2. Measurement Bias
- Different error rates for measurement vs gate operations
- Critical for syndrome extraction fidelity
- Affects lattice surgery and flag-qubit protocols

### 3. Spatial/Spatio-temporal Non-uniformity
- Position-dependent error rates across qubit array
- Time-correlated errors (drift, crosstalk)
- Captures real device heterogeneity

## Logical Primitives

| Primitive | Description | Key Sensitivity |
|-----------|-------------|-----------------|
| Logical Memory | Idling code for duration T | Noise correlations, decoder thresholds |
| Lattice Surgery | Merge/split logical qubits | Measurement errors, boundary noise |
| Transversal Hadamard | Logical H via transversal gates | Pauli bias asymmetry |
| Logical Phase (S) | Phase gate via lattice surgery | Combined gate + measurement errors |

## Workflow

### Step 1: Define Noise Model
Specify hardware-motivated noise parameters:
- Pauli error rates (pX, pY, pZ)
- Measurement error rate (pM)
- Spatial variation function f(x,y)
- Temporal correlation model

### Step 2: Select Primitives
Choose logical primitives to benchmark based on target architecture:
- Memory-only: baseline code performance
- Active computation: include lattice surgery, logical gates

### Step 3: Choose Decoder
Select decoder appropriate for noise structure:
- MWPM (minimum-weight perfect matching)
- Union-Find decoder
- Neural network decoder
- Custom decoder exploiting noise bias

### Step 4: Run Simulation
Execute noisy stabilizer simulation at HPC scale:
- Vary code distance d
- Measure logical error rate pL
- Track error propagation through primitives

### Step 5: Analyze Results
Compare logical error rates across:
- Different noise models
- Different primitives
- Different decoders
- Code distances and depths

## Hardware-Aware Co-Design Principles

1. **Noise-adapted codes**: Choose codes matching hardware bias (e.g., XZZX for dephasing-dominant devices)
2. **Decoder selection**: Match decoder to noise structure (biased-noise decoders for biased channels)
3. **Primitive scheduling**: Order operations to minimize exposure to dominant noise
4. **Threshold estimation**: Compute thresholds under realistic noise, not uniform depolarizing

## Key Findings from Paper

- Structured noise affects primitives in **qualitatively distinct** ways
- Uniform depolarizing model fails to capture real device behavior
- Noise-primitive-decoder interaction determines logical error rate
- Results extend beyond memory benchmarks to active computation

## Code Reference

Official implementation: https://github.com/kan-shuwen/FTPrimitiveBench (verify URL from paper)

## Activation Keywords
- ft-primitive-bench
- fault-tolerant benchmarking
- QEC benchmarking
- logical primitive analysis
- hardware-motivated noise
- noisy stabilizer simulation
- surface code benchmark
- lattice surgery benchmark
- quantum error correction evaluation
- 容错量子计算基准测试
- 量子纠错码评估
