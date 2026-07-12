---
name: reasonstl-nl-to-stl
description: Tool-augmented process-rewarded learning for Natural Language to Signal Temporal Logic (STL) translation in cyber-physical systems (CPS) specification. Use when: (1) translating natural language CPS requirements into STL formulas, (2) building NL-to-formal-specification pipelines for autonomous systems, robotics, or CPS verification, (3) designing tool-augmented LLM frameworks for formal methods, (4) implementing process-rewarded training for structured output generation, (5) creating benchmarks for computation-aware formal specification translation. Activation keywords: NL-to-STL, signal temporal logic, cyber-physical systems specification, formal methods translation, tool-augmented LLM, process-rewarded learning, STL benchmark, CPS requirements, autonomous systems specification
---

# ReasonSTL: NL-to-STL via Tool-Augmented Process-Rewarded Learning

## Overview

Methodology for translating natural language descriptions of cyber-physical system requirements into Signal Temporal Logic (STL) formulas using tool-augmented open-source LLMs with process-rewarded training. Provides a transparent, low-cost, privacy-preserving alternative to prompting commercial LLM APIs for formal specification drafting.

Source: arXiv:2605.06483 — Ye et al., Shanghai Jiao Tong University + Alibaba Group (2026)

## STL Primer

STL extends temporal logic to continuous, real-valued signals. Key constructs:

```
STL Formula φ ::= p           | atomic predicate (μ > 0)
                | ¬φ         | negation
                | φ₁ ∧ φ₂    | conjunction
                | ◻_[a,b] φ  | always (within time interval)
                | ◇_[a,b] φ  | eventually (within time interval)
                | φ₁ U_[a,b] φ₂ | until (within time interval)
```

Atomic predicates: `μ(s(t)) > 0` where μ is a linear function over signal values.
Example: `◻_[0,10] (distance > 5)` — "always maintain distance > 5m for next 10 seconds"

## Core Methodology: Three-Stage Pipeline

### Stage 1: Explicit Reasoning Decomposition

Decompose NL requirement into structured reasoning steps before formula construction:

1. **Entity Identification**: Extract physical quantities, signals, and entities
2. **Temporal Scope Detection**: Identify time intervals and temporal operators needed
3. **Predicate Construction**: Map natural language conditions to atomic predicates
4. **Formula Assembly**: Combine predicates with temporal operators into STL

### Stage 2: Deterministic Tool Calls

LLM calls external tools at reasoning checkpoints:

- **Signal Registry Tool**: Validate identified signals against known system vocabulary
- **Temporal Interval Tool**: Verify time bounds are physically meaningful
- **Syntax Checker Tool**: Validate partial STL formula syntax in real-time
- **Semantic Validator Tool**: Check formula matches original NL intent

Tool calls are deterministic — they execute known validation functions, not additional LLM calls.

### Stage 3: Structured Formula Construction

Output STL formula in structured JSON following a defined schema:

```json
{
  "formula": "always(0, 10, greater_than(distance, 5))",
  "ast": {
    "op": "always",
    "interval": [0, 10],
    "child": {
      "op": "greater_than",
      "signal": "distance",
      "threshold": 5
    }
  },
  "natural_language": "always maintain distance greater than 5 meters for 10 seconds"
}
```

## Process-Rewarded Training

Train local open-source models using process supervision:

### Training Pipeline

1. **Data Collection**: Gather NL-STL pairs from STL-Bench or domain-specific corpus
2. **Process Annotation**: Annotate intermediate reasoning steps and tool-use trajectories
3. **Reward Model**: Train reward model on both process quality and formula correctness
4. **Fine-tuning**: Apply process-rewarded optimization (e.g., GRPO/DPO) to base model

### Reward Design

Two-level reward signal:
- **Process Reward**: Correct tool usage, valid reasoning chain, appropriate decomposition
- **Outcome Reward**: Final STL formula correctness (syntax + semantic match)

### Model Selection

- ReasonSTL shows 4B parameter models can achieve SOTA with process-rewarded training
- Local deployment enables privacy preservation for industrial CPS requirements
- Avoids token costs and data exposure of commercial LLM APIs

## STL-Bench Benchmark

When building evaluation benchmarks for NL-to-STL translation:

### Key Dimensions

1. **Computation-Aware**: Include computational complexity metadata (number of operators, nesting depth)
2. **Bilingual**: Support both English and Chinese requirements
3. **Grounded in Real Signals**: Use actual CPS signal data, not synthetic predicates
4. **Diverse Domains**: Cover autonomous driving, UAV, robotics, electronics

### Evaluation Metrics

- **Exact Match**: Formula string equality (after normalization)
- **AST Match**: Abstract syntax tree structural equivalence
- **Robustness Score**: Performance under paraphrased inputs
- **Computation Cost**: Inference time and memory usage

## Implementation Patterns

### Pattern 1: Direct Pipeline (Simple)

```
NL Input → Reasoning Prompt → STL Formula → Validation → Output
```

Suitable for single-shot translation with known signal vocabulary.

### Pattern 2: Tool-Augmented (Recommended)

```
NL Input → Reason → Tool Call (validate) → Reason → Tool Call (check) → STL → Output
```

Adds verification at each step; catches errors before formula construction completes.

### Pattern 3: Process-Rewarded Fine-tuned (Production)

```
NL Input → Fine-tuned Model (with tool-use capability) → STL → Validation → Output
```

Deploy locally after process-rewarded training; lowest latency, highest privacy.

## Pitfalls

- **Signal Ambiguity**: NL descriptions may reference signals not in the registry — implement fallback to request clarification
- **Interval Ambiguity**: "soon" or "quickly" need domain-specific mapping to concrete time bounds
- **Nested Temporal Operators**: Deep nesting (>3 levels) causes exponential complexity — limit nesting depth or use hierarchical decomposition
- **Predicate Grounding**: Abstract predicates ("safe distance") require domain-specific threshold mapping
- **Training Data Quality**: Process-rewarded training requires annotated reasoning traces — quality matters more than quantity

## When to Use

- CPS requirement engineering from natural language specifications
- Autonomous system safety constraint specification
- Robotics mission planning with temporal logic constraints
- Verification/synthesis pipeline input generation
- Educational tools for teaching STL to engineers without formal methods background
