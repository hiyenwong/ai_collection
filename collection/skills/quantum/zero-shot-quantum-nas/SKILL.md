---
name: zero-shot-quantum-nas
description: "Zero-shot Quantum Neural Architecture Search methodology for VQA circuit optimization without classical search loop. Use when: (1) designing variational quantum circuits, (2) optimizing quantum architecture without expensive search, (3) reducing classical overhead in VQA, (4) NISQ-era algorithm design, (5) quantum machine learning circuit selection."
---

# Zero-shot Quantum Neural Architecture Search

## Core Idea

Replace classical architecture search loops with a zero-shot approach that evaluates quantum circuit expressibility and trainability analytically, eliminating the need for costly iterative evaluation on quantum hardware.

## Methodology

### Step 1: Expressibility-Trainability Analysis

Evaluate candidate VQA circuits using:
- **Gradient variance** as trainability proxy (low variance = barren plateau)
- **State space coverage** as expressibility measure
- **Fisher information** for parameter sensitivity

### Step 2: Analytical Circuit Ranking

Rank architectures without execution:
1. Compute expressibility via Haar measure distance
2. Estimate trainability via gradient norm distribution  
3. Filter out circuits in barren plateau regime
4. Select Pareto-optimal expressibility-trainability tradeoff

### Step 3: Hardware-Aware Selection

Match selected architecture to target hardware:
- Gate depth vs. coherence time
- Connectivity requirements vs. hardware topology
- Native gate set compatibility

## Activation Keywords
- zero-shot quantum architecture search
- quantum NAS
- VQA circuit design
- variational circuit optimization
- quantum architecture without search
- 零样本量子架构搜索
- 量子神经架构搜索

## Error Handling
- If gradient estimation fails: use parameter-shift rule instead of finite difference
- If hardware constraints reject architecture: fall back to next Pareto-optimal candidate

## References
- arXiv:2605.27410 - Zero-shot Quantum Neural Architecture Search
