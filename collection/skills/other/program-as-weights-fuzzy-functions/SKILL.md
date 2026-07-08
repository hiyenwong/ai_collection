---
name: program-as-weights-fuzzy-functions
description: Program-as-Weights (PAW) paradigm for fuzzy function programming. Compile natural-language specifications into compact, locally-executable neural artifacts using parameter-efficient adapters for frozen interpreters. Achieves 32B-level performance at 1/50 inference memory.
trigger: program as weights, fuzzy functions, PAW, neural artifact compilation, parameter efficient adapters, tool builder pattern
category: ai_collection/collection/skills
---

# Program-as-Weights: Fuzzy Function Programming

## Overview
Many programming tasks resist clean rule-based implementation (alerting on log lines, repairing malformed JSON, ranking search results by intent). PAW reframes the foundation model from a per-input problem solver into a **tool builder**: invoked once per function definition, it produces a small reusable artifact.

## Architecture
1. **Compiler** (4B model): Trained on FuzzyBench (10M examples), emits parameter-efficient adapters
2. **Interpreter** (0.6B frozen model): Executes PAW programs locally
3. **FuzzyBench**: 10M-example dataset for compiler training

## Performance
- 0.6B Qwen3 interpreter executing PAW programs matches direct prompting of Qwen3-32B
- Uses ~1/50 of inference memory
- Runs at 30 tokens/s on MacBook M3
- Subsequent calls per function application are cheap and offline

## Usage Pattern
```
# Step 1: Define function in natural language (once)
# "Alert on important log lines" → Compiler emits adapter

# Step 2: Execute adapter locally (many times, offline)
# Cheap inference with small interpreter
```

## Benefits
- **Locality**: No API calls needed after compilation
- **Reproducibility**: Deterministic local execution
- **Cost efficiency**: 1/50 memory, 30 tok/s on consumer hardware
- **Offline**: No network dependency after compilation

## Activation Keywords
program as weights, PAW, fuzzy functions, neural compilation, parameter efficient, tool builder, FuzzyBench

## Source
arXiv: 2607.02512 (2026-07-02)
