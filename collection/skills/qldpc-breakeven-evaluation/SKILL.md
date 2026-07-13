---
name: qldpc-breakeven-evaluation
category: quantum-computing
description: Framework for evaluating quantum LDPC codes at breakeven point from arXiv:2606.06455. qLDPC codes achieve higher encoding rates than surface codes with demonstrated breakeven on real hardware.
source: "arXiv:2606.06455"
source_title: "Breakeven demonstration of quantum low-density parity-check codes"
source_author: "Unknown"
keywords:
  - quantum error correction
  - qLDPC codes
  - fault tolerance
  - breakeven
  - surface code
---

# qLDPC Code Breakeven Evaluation

## Overview

Quantum low-density parity-check (qLDPC) codes represent a leading candidate for fault-tolerant quantum computing, featuring higher encoding rates than planar surface codes.

**Trigger**: When evaluating quantum error correction codes, designing fault-tolerant architectures, or comparing qLDPC vs surface code approaches.

**arXiv**: 2606.06455

## Key Insights

- qLDPC codes achieve higher encoding rates than surface codes
- Breakeven demonstration validates practical viability
- Spacetime lifting framework enables low-overhead fault tolerance
- Coherent vs stochastic noise requires different handling strategies

## Evaluation Framework

1. Measure physical error rates on target hardware
2. Compute logical error rate for candidate qLDPC code
3. Compare against surface code baseline at same overhead
4. Verify breakeven: logical error < physical error

## Pitfalls

- Coherent noise behaves differently from stochastic noise under QEC
- Hardware-specific error channels may favor different code families
- Overhead comparison must account for both qubit count and circuit depth

## Verification Steps

1. Confirm logical error rate measurement methodology
2. Validate against independent simulation results
3. Check hardware error model matches experimental conditions
