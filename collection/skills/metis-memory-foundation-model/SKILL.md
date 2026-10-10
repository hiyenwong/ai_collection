---
name: metis-memory-foundation-model
description: "Metis Memory Foundation Model framework for native memory capabilities in foundation models. Introduces persistent dynamically evolving memory state within backbone and native memory procedures for autonomous information storage/utilization. Use when building AI agents with internalized memory, gradient-free online memory maintenance, or frozen-weight inference with dynamic memory states."
metadata:
  arxiv_id: "2607.26760"
  published: "2026-07-29"
  authors: "Zeyu Zhang, Ziliang Guo, Yihang Sun, Xichong Zhang, Xixuan Hao, Zehao Lin, Yang Zhang, Xiaoyan Zhao, Tong Shen, Bo Tang, Zhi-Qin John Xu, Junchi Yan, Haofen Wang, Xu Chen, Feiyu Xiong, Zhiyu Li, Tat-Seng Chua"
  tags: [memory-foundation-models, ai-agents, native-memory, gradient-free-memory, frozen-weight-inference]
license: Complete terms in LICENSE.txt
---

# Metis: Memory Foundation Model

## Overview

Metis introduces the first prototype of memory foundation models, which empower foundation models with native memory capabilities. Instead of relying on external memory modules, Metis internalizes memory functionality directly into the model architecture.

## Core Framework

### Native Memory Definition

Native memory is formalized from two perspectives:

1. **Persistent and dynamically evolving memory state** within the backbone
2. **Native memory procedures** that autonomously store and utilize information through model computation

### Architectural Innovation

- **Memory state integration**: Historical information compressed into the model
- **Memory attention**: Access to compressed historical information through attention mechanisms
- **Frozen weights**: All learned model weights remain frozen during inference
- **Dynamic transformation**: Native memory states autonomously transformed through standard forward computation

## Key Advantages

### Architecture Benefits

- **End-to-end optimization**: Memory capabilities learned during training
- **Efficiency**: Online memory maintenance requires only forward pass
- **Gradient-free updates**: No backpropagation needed for memory maintenance
- **Native integration**: Memory is part of the model, not external module

### Operational Characteristics

- **Online memory maintenance**: Gradient-free, forward-pass only
- **Frozen inference**: Model weights never updated during deployment
- **Autonomous transformation**: Memory states evolve through standard computation
- **Scalable training**: Large-scale memory-specific training data with multiple optimization objectives

## Implementation Details

### Training Methodology

- **Memory-specific data**: Constructed large-scale training datasets focused on memory tasks
- **Multiple objectives**: Introduced optimization objectives to acquire native memory procedures through mid-training
- **Mid-training approach**: Memory capabilities acquired during intermediate training phase
- **End-to-end learning**: Full integration of memory procedures into model training

### Inference Workflow

1. **Input processing**: Standard forward pass through model backbone
2. **Memory interaction**: Memory attention mechanisms access stored information
3. **State transformation**: Memory states autonomously updated through computation
4. **Output generation**: Final output incorporates both current input and memory state

## Practical Applications

### AI Agent Development

- **Internalized memory**: Eliminates need for external memory modules
- **Autonomous operation**: Agents maintain and use memory without external intervention
- **Efficient deployment**: Frozen weights enable efficient inference
- **Scalable memory**: Memory capacity scales with model architecture

### Long-Context Processing

- **Compressed history**: Historical information efficiently stored in memory state
- **Dynamic retrieval**: Memory attention enables selective access to relevant history
- **Context continuity**: Maintains context across long sequences without external storage
- **Efficient scaling**: Avoids quadratic attention costs of traditional long-context models

## Usage Guidelines

### When to Use Metis Framework

- **AI agent memory**: Building agents with internalized memory capabilities
- **Frozen-weight deployment**: Scenarios requiring fixed model weights during inference
- **Gradient-free memory**: Applications needing memory updates without backpropagation
- **Native memory research**: Exploring foundation models with built-in memory

### Implementation Considerations

1. **Architecture design**: Integrate memory state into model backbone
2. **Training data**: Create memory-specific training datasets
3. **Optimization objectives**: Design objectives for acquiring memory procedures
4. **Memory attention**: Implement mechanisms for accessing stored information
5. **Evaluation metrics**: Develop metrics for native memory capability assessment

## Strengths and Limitations

### Demonstrated Strengths

- **Native memory capabilities**: Exhibits genuine memory functionality
- **Efficient inference**: Forward-pass only memory maintenance
- **Frozen weights**: Stable deployment with fixed parameters
- **Autonomous operation**: Self-contained memory management

### Potential Limitations

- **Memory capacity**: Limited by model architecture and training data
- **Training complexity**: Requires specialized memory-specific training
- **Task specificity**: Memory procedures may be task-dependent
- **Scalability**: Memory state size may impact computational requirements

## Research Impact

### Paradigm Shift

- **Foundation model evolution**: Extends foundation models beyond perception/reasoning to include memory
- **Agent internalization**: Moves memory from external modules to native capabilities
- **New research direction**: Opens exploration of other native agent capabilities

### Future Directions

- **Extended capabilities**: Other native agent functions (planning, tool use, etc.)
- **Architecture variants**: Different memory state representations and access mechanisms
- **Cross-modal memory**: Memory integration across multiple modalities
- **Lifelong learning**: Combining native memory with continual learning

## Code and Resources

- **Project Repository**: Available upon request (mentioned in paper)
- **Model Checkpoints**: Released to facilitate future research
- **Paper**: https://arxiv.org/abs/2607.26760
- **HTML Version**: https://arxiv.org/html/2607.26760v1

## Activation Keywords

- Metis memory foundation model
- native memory capabilities
- frozen-weight memory inference
- gradient-free memory maintenance
- memory attention mechanisms
- autonomous memory transformation
- internalized agent memory
- memory state compression
- foundation model memory
- AI agent native memory

## Related Skills

- llm-sleep-memory-consolidation
- worldkv-world-memory
- self-evolving-memory
- indexed-memory
- memory-retrieval
- llm-serving-system-adaptive-architecture
- agentic-fast-slow-planning