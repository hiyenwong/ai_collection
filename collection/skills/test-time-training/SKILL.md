---
name: test-time-training
description: Framework for implementing Test-Time Training (TTT) - updating model weights during inference to adapt to continuous information streams. Use when designing adaptive AI systems, online learning for LLMs, breaking static train-deploy paradigm, or handling real-world tasks with evolving data.
---

# Test-Time Training (TTT)

## Overview

Test-Time Training (TTT) breaks the static "train then deploy" paradigm by updating model parameters (fast weights) during inference time, enabling dynamic adaptation to continuous streams of new information inherent in real-world tasks.

**Core Innovation**: Move from static deployment to dynamic adaptation at inference time.

## Core Capabilities

### 1. Fast vs. Slow Weights

**Concept**: Separate model parameters into two types.

| Weight Type | Purpose | Update Timing |
|-------------|---------|---------------|
| **Slow Weights** | General knowledge | Pre-training phase |
| **Fast Weights** | Task-specific adaptation | Inference (TTT) |

**Implementation**:
```python
class TTModel:
    def __init__(self, base_model):
        self.slow_weights = base_model.parameters()  # Frozen
        self.fast_weights = initialize_fast_weights()  # Updated at inference
    
    def forward(self, input, update_fast=True):
        # Combine slow + fast weights
        combined = combine_weights(self.slow_weights, self.fast_weights)
        output = model_forward(combined, input)
        
        if update_fast:
            # Update fast weights at inference
            self.fast_weights = ttt_update(self.fast_weights, input, output)
        
        return output
```

### 2. In-Place Training

**Key Challenge**: TTT traditionally requires architectural modifications and computational overhead.

**Solution**: In-place training - update weights directly without auxiliary architecture.

**Benefits**:
- Architectural compatibility with existing models
- Computational efficiency
- Minimal deployment overhead

### 3. Real-World Adaptation

**Use Case**: Handle continuous information streams.

**Scenarios**:
- Real-time data processing
- Evolving user preferences
- Dynamic task requirements
- Streaming information

**Workflow**:
1. Receive new input at inference
2. Update fast weights with TTT
3. Generate adapted output
4. Continue adaptation cycle

## Workflow

### Step 1: Design TTT Architecture

When implementing TTT:

```python
# 1. Identify slow vs. fast weight separation
slow_params = identify_general_knowledge_params(model)
fast_params = identify_adaptive_params(model)

# 2. Design update mechanism
update_fn = design_fast_weight_update(fast_params)

# 3. Ensure architectural compatibility
verify_compatibility(model, update_fn)
```

### Step 2: Implement Inference Update

Update weights at inference:

```python
def ttt_inference(model, input_stream):
    outputs = []
    
    for input in input_stream:
        # Generate output with current weights
        output = model(input)
        
        # Update fast weights in-place
        model.fast_weights = in_place_update(
            model.fast_weights,
            input,
            output,
            loss_fn=self_adaptation_loss
        )
        
        outputs.append(output)
    
    return outputs
```

### Step 3: Handle Computational Constraints

Address efficiency challenges:

1. **Memory**: Limit fast weight size
2. **Computation**: Efficient update algorithms
3. **Latency**: Real-time update constraints

**Solution Patterns**:
- Sparse updates (update subset of weights)
- Low-rank adaptations (LoRA-style)
- Memory-efficient gradients

## Applications

### Application 1: LLM Online Learning

**Use Case**: LLMs adapting to new information at inference.

**Benefits**:
- No retraining for new knowledge
- Continuous learning
- Real-time adaptation to user context

**Implementation**:
```python
class TTLLM:
    def generate(self, prompt, context_stream):
        # Update fast weights with context
        for context in context_stream:
            self.fast_weights = update_with_context(self.fast_weights, context)
        
        # Generate with adapted weights
        return self.model.generate(prompt, self.fast_weights)
```

### Application 2: Dynamic Task Adaptation

**Use Case**: Model adapting to changing task requirements.

**Benefits**:
- Task-specific optimization without fine-tuning
- Multi-task handling with single model
- Efficient resource usage

### Application 3: Streaming Data Processing

**Use Case**: Real-time processing of continuous data streams.

**Benefits**:
- No batch processing delays
- Immediate adaptation to data patterns
- Continuous performance improvement

## Key Concepts

### Static vs. Dynamic Paradigm

| Paradigm | Training | Deployment | Adaptation |
|----------|----------|------------|------------|
| **Static** | Pre-train | Deploy frozen | No adaptation |
| **TTT** | Pre-train slow weights | Deploy + update fast weights | Continuous at inference |

### In-Place Training Benefits

| Challenge | Traditional TTT | In-Place TTT |
|-----------|-----------------|--------------|
| **Architecture** | Requires modifications | Compatible with existing |
| **Computation** | Auxiliary overhead | Efficient direct update |
| **Deployment** | Complex setup | Minimal overhead |

## Related Skills

- **online-learning**: General online learning frameworks
- **lora-adaptation**: Low-rank adaptation methods
- **meta-learning**: Learning to learn patterns

## Resources

### references/

- `ttt_theory.md`: Test-Time Training theory and foundations
- `fast_slow_weights.md`: Fast/slow weight separation strategies

## Key Papers

1. **In-Place Test-Time Training** (arxiv:2604.06169v1)
   - Authors: Guhao Feng, Shengjie Luo, Kai Hua, et al.
   - Date: 2026-04-07
   - Key innovation: In-place training for architectural compatibility

2. **Related Works**: Test-Time Training, online learning, adaptive inference

## Usage Examples

### Example 1: Implement TTT for LLM

**Request**: "Add test-time training to a language model for online learning"

**Response**:
1. Separate slow (frozen) and fast (adaptive) weights
2. Design in-place update mechanism
3. Implement inference-time adaptation loop
4. Test with streaming data

### Example 2: Handle Streaming Data

**Request**: "Process continuous data stream with adaptive model"

**Response**:
1. Initialize model with TTT capability
2. Design fast weight update for data stream
3. Implement real-time adaptation loop
4. Monitor performance over stream