---
name: covert-bosonic-sequential-detection
description: "Covert communication over bosonic channels using blockwise sequential detection — receiver-centric framework exploiting linear vs quadratic information growth asymmetry between Bob and Willie for optimal signaling design. Use for covert quantum communication, bosonic channel analysis, sequential detection systems."
metadata:
  arxiv_id: "2606.18666"
  published: "2026-06-17"
  authors: "Qipeng Qian, Yuntao Qian"
---

# Covert Blockwise Coding with Sequential Detection

## Core Methodology

### Key Information-Theoretic Asymmetry
- **Bob's post-change information growth**: Linear in small-signal regime
- **Willie's detectability**: Quadratic quantum relative entropy law
- This asymmetry enables covertness: Bob detects signals Willie cannot distinguish from noise

### Design Principles
- Each block = binary super-symbol (active/inactive)
- **Minimum detection-segment length**: Enables Bob detection before block end while staying covert to Willie
- **Asymptotically optimal signaling**: Uniform across detection segment under per-block covertness budget
- Single-pass CUSUM detector crosses threshold within block with exponentially high probability

### Framework Components
1. **Block structure**: Detection segment + payload segment per block
2. **Receiver design**: General-dyne measurement (physically realizable)
3. **Sequential detection**: CUSUM-based change-point detection within each block
4. **Covertness budget**: Per-block constraint on Willie's detection probability

## Activation Keywords
- Covert quantum communication, bosonic channels
- Sequential detection, CUSUM detection
- Quantum covertness, quantum relative entropy
- 隐蔽量子通信，顺序检测

## Usage Patterns

### Pattern 1: Covert Quantum Link Design
Design covert communication links over thermal-loss bosonic channels by exploiting the linear/quadratic information growth asymmetry between legitimate receiver and eavesdropper.

### Pattern 2: Sequential Detection in Quantum Systems
Apply CUSUM-based sequential detection within finite transmission horizons where detection must complete before block ends.

### Pattern 3: Covertness Budget Allocation
Under per-block covertness constraints, use uniform signaling strategy across detection segment — proven asymptotically optimal.

## Pitfalls
- Framework assumes fixed physically realizable general-dyne receiver — optimal receiver design not addressed
- Analysis asymptotic — finite-block-length corrections needed for practical systems
- Quadratic Willie detectability law applies only to small-signal regime
- Single-pass CUSUM optimality assumes known pre/post-change distributions
