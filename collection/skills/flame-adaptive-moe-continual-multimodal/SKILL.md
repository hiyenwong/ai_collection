---
name: flame-adaptive-moe-continual-multimodal
description: "FLAME: Adaptive Mixture-of-Experts for continual multimodal multi-task learning. Handles both co-available multi-task pretraining and sequential continual adaptation. Activation triggers: FLAME MoE, continual multimodal learning, adaptive mixture of experts, multi-task continual learning, sequential task adaptation"
---

# FLAME: Adaptive Mixture-of-Experts for Continual Multimodal Multi-Task Learning

> An adaptive MoE framework for multimodal models operating under two complementary regimes: (1) multi-task pretraining with co-available tasks, and (2) continual adaptation with sequential task arrival.

## Metadata
- **Source**: arXiv:2605.09355
- **Authors**: Xing Han, Shravan Chaudhari, Tanvi Ranade, Rama Chellappa, Suchi Saria
- **Published**: 2026-05-10

## Core Problem

**Two Regimes of Multimodal Learning**:
1. **Multi-task pretraining**: Multiple tasks available simultaneously at design time, allowing cross-task knowledge transfer
2. **Continual adaptation**: New tasks arrive sequentially over time, requiring adaptation without forgetting

Real-world deployment must handle both regimes effectively.

## FLAME Architecture

### Adaptive Mixture-of-Experts Design
- **Shared experts**: Capture knowledge common across all tasks/modalities
- **Task-specific experts**: Specialize for individual tasks
- **Adaptive routing**: Dynamically assign inputs to appropriate experts based on task context

### Two-Regime Handling
1. **Pretraining Phase**: All tasks available → learn comprehensive expert specialization and routing policies
2. **Continual Phase**: New tasks arrive → add new task experts while preserving shared knowledge, adapt routing without retraining everything

### Key Innovations
1. **Expert specialization**: Different experts learn different aspects of multimodal representations
2. **Routing stability**: Routing mechanism adapts to new tasks without completely rewiring
3. **Memory efficiency**: Only new task experts need training during continual phase

## Methodology

### MoE Routing
- Router network assigns weights to experts based on input features
- Top-K expert selection for computational efficiency
- Load balancing to prevent expert collapse

### Continual Adaptation
- Freeze shared experts and most of the router
- Add new task-specific experts
- Fine-tune routing for new task while preserving old routing patterns
- Optional: minor updates to shared experts with regularization

### Training Objectives
- Task-specific losses for each modality/task combination
- Load balancing loss for routing stability
- Regularization terms to prevent catastrophic forgetting

## Applications
- Medical AI systems learning new imaging modalities over time
- Autonomous systems adapting to new sensor types
- Multi-modal assistants learning new capabilities
- Industrial inspection with new product lines

## Pitfalls
- **Expert collapse**: Without proper load balancing, some experts may dominate
- **Routing interference**: New task routing may conflict with old task routing
- **Scalability**: Adding many task experts increases model size
- **Modality imbalance**: Some modalities may dominate the learning signal

## Related Skills
- continual-learning-methods
- mixture-of-experts-routing
- multimodal-learning
