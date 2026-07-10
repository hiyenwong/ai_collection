---
name: coset-ensemble-decoder-qec
description: "Coset Ensemble Decoder for Quantum Error Correction with Algorithm-Hardware Co-Design methodology. Ensemble forest exploration exploiting logically equivalent cosets to improve Union-Find decoding, with domain-specific FPGA architecture reducing LUT consumption 8.2x. Use when: (1) designing QEC decoders for fault-tolerant quantum computing, (2) optimizing accuracy-latency trade-offs in real-time syndrome decoding, (3) implementing hardware-efficient QEC decoders on FPGA, (4) ensemble decoding approaches for surface codes. Activation: coset ensemble decoding, QEC decoder, Union-Find decoder, syndrome decoding, quantum error correction, FPGA decoder, algorithm-hardware co-design, fault-tolerant decoding, surface code decoder, real-time QEC, min-weight perfect matching, coset-level maximum-likelihood"
metadata:
  arxiv_id: "2606.11076"
  published: "2026-06-09"
  authors: "IM Seon et al."
---

## Context

Fault-tolerant quantum computation requires real-time QEC decoding that simultaneously delivers high logical accuracy and ultra-low latency. Traditional decoders (MWPM, Union-Find) face an accuracy-latency trade-off. This paper introduces coset ensemble decoding — an algorithm-hardware co-design that improves UF decoding by exploiting logically equivalent cosets, with an FPGA architecture that reduces resource consumption 8.2x.

## Core Methodology

### 1. Coset Ensemble Decoding (Algorithm)

- **Coset Exploitation**: Multiple logically equivalent cosets produce the same syndrome — enumerate candidates across cosets rather than selecting single minimum-weight matching
- **Ensemble Forest Exploration**: Generate multiple coset-consistent UF forest candidates, aggregate to approximate coset-level maximum-likelihood decoding
- **Reverse-Order Elimination**: Reduce computational complexity by processing elimination in reverse order
- **Lossless Graph Compression**: Compress syndrome graph without accuracy loss to reduce memory footprint

### 2. Domain-Specific FPGA Architecture (Hardware)

- **Temporal Resource Reuse**: Avoids code-distance-proportional resource growth via time-multiplexed processing units
- **Multi-Bank Memory Hashing**: Mitigates pipeline stalls under concurrent syndrome access patterns
- **Hierarchical ID Mapping**: Resolves memory conflicts in highly concurrent syndrome extraction

### 3. Accuracy-Latency Trade-Off

- Tunable candidate number parameter: users adjust decoding performance vs. latency based on workload requirements
- Under circuit-level depolarizing noise: better accuracy-latency than MWPM and UF baselines
- 8.2x reduction in FPGA LUT consumption vs. reported UF-based decoder resources

## Implementation Steps

1. Implement Union-Find decoder as base algorithm
2. Extend to enumerate logically equivalent cosets for each syndrome
3. Build ensemble forest exploration: generate N coset-consistent candidates
4. Implement aggregation mechanism for coset-level ML approximation
5. Apply reverse-order elimination for computational efficiency
6. Apply lossless graph compression for memory reduction
7. Design FPGA architecture with temporal resource reuse
8. Implement multi-bank memory hashing and hierarchical ID mapping
9. Benchmark under circuit-level depolarizing noise model
10. Tune candidate number parameter for target accuracy-latency point

## Key Results (arXiv:2606.11076)

- **LUT reduction**: 8.2x vs. prior UF-based FPGA decoder resources
- **Accuracy**: Better than MWPM and UF baselines under circuit-level noise
- **Tunability**: Candidate number provides flexible performance knob
- **Availability**: Implementation at github.com/IMSeonL/coset-ensemble-decoder
- **Noise model**: Circuit-level depolarizing noise

## Pitfalls

- **Candidate Number Scaling**: Increasing candidate count improves accuracy but increases latency — the trade-off must be calibrated for target fault-tolerant workload
- **Code Distance Scaling**: Temporal resource reuse may become bottleneck at very large code distances (d > 20) where sequential processing dominates
- **Noise Model Specificity**: Results demonstrated under circuit-level depolarizing noise — verify for biased noise, leakage, or crosstalk models
- **Hardware-Specific Optimizations**: Multi-bank memory hashing and hierarchical ID mapping are FPGA-specific — ASIC or GPU implementations require different approaches
- **Coset Enumeration Completeness**: The ensemble approach approximates coset-level ML; full enumeration may be intractable for large codes

## Verification

1. Implement coset ensemble decoder in Python/C++ for simulation
2. Compare logical error rate vs. standard UF decoder at same code distance
3. Verify accuracy improvement under circuit-level depolarizing noise
4. Synthesize FPGA design and measure LUT/BRAM/DSP utilization
5. Confirm 8.2x LUT reduction vs. baseline UF decoder
6. Measure decoding latency vs. candidate number parameter
7. Validate tunable accuracy-latency trade-off curve

## Code Reference

Implementation available at: https://github.com/IMSeonL/coset-ensemble-decoder
