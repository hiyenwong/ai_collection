---
name: compress-distill-reasoning-trace-compression
description: Post-hoc compression of reasoning chain-of-thought traces before knowledge distillation for efficient training and inference
version: 1.0.0
category: ai_collection
tags: [deep-learning, distillation, efficiency, reasoning, knowledge-transfer]
arxiv: 2606.05988v1
paper_title: "Compress-Distill: Reasoning Trace Compression for Efficient Knowledge Distillation"
authors: ["Maxime Griot", "Paul Steven Scotti", "Tanishq Mathew Abraham"]
published: 2026-06-04
activation_keywords: [reasoning distillation, trace compression, knowledge distillation, CoT compression, efficient training, student model]
---

# Compress-Distill: Reasoning Trace Compression

## Core Insight

Reasoning trace compression offers accuracy-efficiency trade-off: students retain **96% accuracy** while gaining **18x higher per-token efficiency**.

## Methodology

### Compression Pipeline
1. **Generate teacher traces**: Qwen3.5-397B-A17B, gpt-oss-120B produce ~283k traces
2. **Compress with instruction-tuned models**: reduce to 8.6-21.0% of original length
3. **Distill compressed traces**: train student models on compressed reasoning

### Key Findings
- **Training speed**: 2.0-7.6x faster with compressed traces
- **Token efficiency**: 12-30% of raw training tokens
- **Inference output length**: 3-19x shorter
- **Accuracy**: compressed retains up to 96% of raw-trace performance

### Trade-off Analysis
```
Raw traces → Highest accuracy at every scale
Compressed → Higher efficiency with accuracy trade-off
Truncated → Lower accuracy than model-compressed
```

**Critical insight**: Compression ≠ mere truncation
- Model-compressed beats naive truncation (especially for smaller students)
- Maintains shorter inference outputs while preserving reasoning quality

## Implementation Pattern

### Compression Strategy
```python
# Conceptual compression pipeline
def compress_reasoning_trace(teacher_trace, compressor_model):
    # Step 1: Extract key reasoning steps
    semantic_steps = extract_semantic_operations(teacher_trace)
    
    # Step 2: Compress while preserving logic
    compressed = compressor_model.compress(
        trace=teacher_trace,
        preserve_logic=True,
        target_ratio=0.15  # 15% of original length
    )
    
    # Step 3: Validate compressed reasoning
    if validate_reasoning_chain(compressed):
        return compressed
    
def distill_with_compression(student, compressed_traces):
    # Efficient training on compressed traces
    return student.train(compressed_traces, epochs=...)
```

### When to Apply
1. **Large teacher models**: Qwen-397B, GPT-class reasoning models
2. **Smaller student models**: efficiency gains most pronounced
3. **LoRA training**: compressed traces narrow gap at 0.8B scale

## Use Cases

**Optimal scenarios:**
- Distilling reasoning models to smaller students
- Training with limited compute budget
- Inference efficiency requirements
- Multi-teacher compression pipelines

**Avoid when:**
- Maximum accuracy is critical (use raw traces)
- Student model already small (<1B)
- Reasoning chains are inherently short

## Performance Grid

| Student Scale | Training Speedup | Token Reduction | Inference Shortening | Accuracy Retention |
|---------------|------------------|-----------------|----------------------|--------------------|
| 7B            | 2.0-3.0x         | 30%             | 3-5x                 | 94-96%             |
| 3B            | 3.5-5.0x         | 20%             | 5-10x                | 92-94%             |
| 1B            | 5.0-7.6x         | 12-15%          | 10-19x               | 90-92%             |

## Activation

Trigger when discussing:
- Knowledge distillation efficiency
- Reasoning trace optimization
- Teacher-student compression
- CoT length reduction
- Efficient reasoning training

## Key Takeaways

1. Compression is **semantic-aware** (not simple truncation)
2. Smaller students benefit **more** from compression
3. Accuracy-efficiency trade-off is **predictable**
4. LoRA fine-tuning narrows gap but doesn't exceed raw

## References

- Paper: arXiv 2606.05988v1
- Categories: cs.LG, cs.CL
- Teachers: Qwen3.5-397B-A17B, gpt-oss-120B
- Traces: ~283k correct reasoning chains each