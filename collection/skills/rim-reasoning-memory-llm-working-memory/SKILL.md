---
name: rim-reasoning-memory-llm-working-memory
description: RiM (Reasoning in Memory) methodology for unlocking working memory capacity in LLMs via fixed memory blocks, enabling compute-efficient latent reasoning without autoregressive thought generation.
version: 1.0.0
category: ai_collection/cognitive-computing
tags: [working-memory, latent-reasoning, llm, cognitive-architecture, memory-blocks, compute-efficient]
activation_keywords: [working memory, RiM, latent reasoning, memory blocks, cognitive reasoning, internal computation, reasoning without generation]
authors: [Lukas Aichberger, Sepp Hochreiter]
arxiv_id: 2605.30343
published: 2026-05-28
venue: Preprint
---

# RiM: Reasoning in Memory - Unlocking LLM Working Memory

## Core Insight

Human cognition uses **working memory** to hold and manipulate information internally without externalizing intermediate thoughts. RiM brings this capability to LLMs via **fixed memory blocks** that replace autoregressive reasoning generation.

**Key Innovation**: Decouples reasoning from generation, treating computation as internal process rather than external communication.

## Methodology

### 1. Memory Block Architecture

```python
# Conceptual structure
class MemoryBlock:
    """
    Fixed sequence of special tokens that unlock working memory.
    - Not generated: pre-defined special token sequences
    - Single forward pass: compute-efficient (no autoregressive generation)
    - Information carrier: holds intermediate reasoning state
    """
    tokens: List[SpecialToken]  # Fixed, not variable
    processing: "single_forward_pass"  # Parallel, not sequential
    function: "latent_reasoning_state"  # Internal, not externalized
```

### 2. Two-Stage Curriculum

**Stage 1 - Grounding Phase**:
- Predict explicit reasoning steps after each memory block
- Supervise intermediate reasoning process
- Establish memory block semantics

**Stage 2 - Refinement Phase**:
- Discard step-level supervision
- Iteratively refine final answer after memory blocks
- Enable pure latent reasoning without generation

### 3. Computational Advantage

| Method | Reasoning Steps | Compute Cost | Externalization |
|--------|-----------------|--------------|-----------------|
| Chain-of-Thought | Generated autoregressively | O(k × n) tokens | Yes (external) |
| RiM Memory Blocks | Fixed special tokens | O(k) forward passes | No (internal) |

**Key**: Memory blocks are **fixed**, enabling single forward pass per block instead of sequential token generation.

## Implementation Guidance

### Memory Block Design

```python
# Example: RiM training configuration
class RiMConfig:
    memory_block_length: int = 64  # Fixed length special tokens
    num_memory_blocks: int = 4     # Number of reasoning cycles
    grounding_epochs: int = 1000   # Stage 1: explicit supervision
    refinement_epochs: int = 2000  # Stage 2: answer refinement
    
    # Curriculum stages
    stage_1: "predict_explicit_steps"  # Grounding
    stage_2: "refine_answer_only"      # Pure latent reasoning
```

### Training Protocol

1. **Initialize**: Define fixed memory block token sequences
2. **Grounding Stage**: 
   - Insert memory blocks in input
   - Supervise: predict reasoning steps after each block
   - Train model to associate blocks with reasoning semantics
3. **Refinement Stage**:
   - Remove explicit reasoning supervision
   - Supervise: final answer after all memory blocks
   - Enable iterative refinement through blocks

## Experimental Results

### Performance Comparison

- **Matches/exceeds** existing latent reasoning methods
- **Compute-efficient**: no autoregressive thought generation overhead
- **Cross-model**: works across different LLM families and sizes
- **Reasoning benchmarks**: validated on standard reasoning tasks

### Key Findings

1. LLMs can be trained to use **working memory** effectively
2. Fixed memory blocks enable **internal computation** without externalization
3. **Two-stage curriculum** crucial for grounding then refining
4. Single forward pass processing maintains **efficiency**

## Cognitive Science Connection

### Working Memory Theory Alignment

- **Human working memory**: holds/manipulates info without externalizing
- **RiM memory blocks**: analogous mechanism in LLMs
- **Latent reasoning**: internal computation, not communicative output
- **Cognitive load**: distributed across fixed blocks, not generated tokens

### Neuroscience Implications

```yaml
Human Working Memory:
  capacity: "7 ± 2 items (Miller's law)"
  function: "manipulate without externalize"
  process: "internal cognitive operations"

RiM Memory Blocks:
  capacity: "num_blocks × block_length"
  function: "parallel latent reasoning"
  process: "internal forward-pass computation"
```

## Use Cases

### When to Apply RiM

1. **Reasoning tasks** requiring intermediate computation
2. **Compute-constrained scenarios** (avoid autoregressive overhead)
3. **Latent reasoning** applications (internal, not communicative)
4. **Working memory analogues** in neural architectures

### Integration Patterns

```python
# Pattern 1: Enhance existing LLMs
class RiMEnhancedLLM:
    base_model: PreTrainedLLM
    memory_blocks: FixedTokenSequences
    reasoning_mode: "latent"  # vs. "autoregressive_chain_of_thought"
    
# Pattern 2: Hybrid reasoning
class HybridReasoning:
    simple_tasks: "autoregressive"  # Fast, no blocks
    complex_tasks: "RiM_blocks"    # Compute-efficient deep reasoning
```

## Technical Details

### Memory Block Token Design

- **Special tokens**: `[MEM_START]`, `[MEM_BLOCK_1]`, ..., `[MEM_END]`
- **Fixed sequences**: Pre-defined, not variable per task
- **Position encoding**: Maintains block identity across tasks
- **Semantic grounding**: Learned during Stage 1 curriculum

### Architecture Considerations

```yaml
Model Requirements:
  - Attention mechanism: processes memory blocks in context
  - Hidden states: carry reasoning information across blocks
  - Token vocabulary: includes special memory block tokens
  
Training Requirements:
  - Stage 1: reasoning step supervision data
  - Stage 2: final answer supervision data
  - Curriculum: gradual transition from grounding to refinement
```

## Limitations & Considerations

1. **Fixed block design**: Less flexible than generated reasoning chains
2. **Training overhead**: Two-stage curriculum required
3. **Semantic grounding**: Depends on Stage 1 supervision quality
4. **Block length**: Trade-off between capacity and efficiency

## Future Directions

1. **Dynamic block sizing**: Adaptive memory block lengths
2. **Multi-modal RiM**: Extend to vision-language reasoning
3. **Hierarchical blocks**: Nested memory structures
4. **Neuroscience validation**: Compare with human working memory fMRI

## References

- **Paper**: "Unlocking the Working Memory of Large Language Models for Latent Reasoning" (arXiv:2605.30343)
- **Authors**: Lukas Aichberger, Sepp Hochreiter
- **Key concepts**: Working memory theory (Baddeley), latent reasoning, memory blocks

## Related Skills

- `working-memory-heterogeneous-delays`: Working memory in SNNs
- `neuroai-beyond-bridging-neuroscience-ai`: NeuroAI integration
- `llm-concept-neurons-control`: LLM internal representations
- `attention-task-structure-cognitive-flexibility`: Cognitive attention mechanisms