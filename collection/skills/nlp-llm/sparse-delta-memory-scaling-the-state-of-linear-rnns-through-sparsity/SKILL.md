---
name: sparse-delta-memory-scaling-the-state-of-linear-rnns-through-sparsity
description: 'Linear attention models allow a fixed state size and a fixed amount of compute per token. However, due to their limited state size, linear attention models fall behind in long-context recall compared. Based on arXiv:2607.07386.'
---

# Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity

**arXiv**: 2607.07386 | **Authors**: Loïc Cabannes, Pierre-Emmanuel Mazaré, Gergely Szilvasy, Matthijs Douze, Maria Lomeli et al. | **Utility**: 0.85

## Overview

Linear attention models allow a fixed state size and a fixed amount of compute per token. However, due to their limited state size, linear attention models fall behind in long-context recall compared to softmax-attention-based transformer architectures. Increasing the state size of linear attention improves recall performance but at the cost of higher FLOPs. In this work, we introduce Sparse Delta Memory (SDM), an architecture that scales the hidden state of gated linear RNNs to orders of magnitude higher capacity using a sparse addressing scheme. SDM extends the Gated DeltaNet architecture by replacing the dense key-value outer product with sparse reads and writes to a large explicit memory. We show that, under an isoFLOP constraint and with an identical number of parameters, a higher state memory capacity significantly improves performance on in-context learning and long-context retrieval tasks. Moreover, by learning the initial state of the SDM memory and therefore using it as a parametric memory, we show that the model further improves on a wide range of common-knowledge and reasoning tasks.

## Key Contributions

1. Linear attention models allow a fixed state size and a fixed amount of compute per token.
2. However, due to their limited state size, linear attention models fall behind in long-context recall compared to softmax-attention-based transformer architectures.
3. Increasing the state size of linear attention improves recall performance but at the cost of higher FLOPs.
4. In this work, we introduce Sparse Delta Memory (SDM), an architecture that scales the hidden state of gated linear RNNs to orders of magnitude higher capacity using a sparse addressing scheme.

## Implementation Notes

- **Keywords**: transformer, agent-memory
- **Categories**: cs.LG
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: transformer, agent-memory.
