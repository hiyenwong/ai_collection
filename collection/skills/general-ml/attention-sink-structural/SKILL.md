---
name: attention-sink-structural
description: Mechanistic explanation of attention sink phenomenon. Variance discrepancy amplified by FFN super neurons. Head-wise RMSNorm fixes it. Based on arXiv 2605.06611.
category: transformer-attention
---

# Attention Sink: Structural Origin and Control

## Overview
Attention sinks (initial tokens monopolizing attention scores) emerge from a causal chain: value aggregation → variance discrepancy → FFN super neuron amplification → dimension disparity → sink formation.

## Causal Chain
1. **Value aggregation** in self-attention induces systematic variance discrepancy
2. **FFN super neurons** (channel-sparse down-projections) amplify this discrepancy
3. **Dimension disparity** of first-token representation emerges
4. **Attention sinks form** as structural anchors

## Key Interventions
- **Isolate aggregation**: Attention mask modifications replicate sinks at arbitrary positions
- **Amplify variance**: Targeted variance amplification creates sinks on demand
- **Head-wise RMSNorm**: Normalizes attention head outputs independently, restores statistical parity, accelerates convergence

## Key Findings
- Sinks are structural, not accidental
- Channel-sparse FFN down-projections are the amplification mechanism
- Can be created at arbitrary positions through controlled interventions
- Head-wise RMSNorm significantly accelerates pre-training

## Implementation Steps
1. Monitor per-token variance in value aggregation outputs
2. Identify FFN super neurons (channel-sparse high-activation units)
3. Apply head-wise RMSNorm to normalize attention head outputs
4. Verify statistical parity across token positions

## Applicable Use Cases
- Pre-training new LLM architectures
- Debugging attention sink-related instability
- Improving convergence in long-context models

## Triggers / Keywords
attention sink, variance discrepancy, super neurons, head-wise RMSNorm, transformer debugging, pre-training stability
