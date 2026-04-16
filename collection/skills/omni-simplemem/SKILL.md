---
name: omni-simplemem
description: Omni-SimpleMem - Autoresearch-guided multimodal agent memory framework with selective ingestion, progressive retrieval, and knowledge graph augmentation. Use when building lifelong multimodal memory systems for AI agents.
---

# Omni-SimpleMem

**Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory**

A unified multimodal memory framework discovered through autonomous research pipeline (AutoResearch Claw), achieving SOTA on LoCoMo and Mem-Gallery benchmarks.

## Paper Information

- **arXiv**: 2604.01007
- **Authors**: Jiaqi Liu et al. (UNC-Chapel Hill, UPenn, UCSC, Berkeley, Cisco)
- **Code**: https://github.com/aiming-lab/SimpleMem

## Problem Statement

AI agents operating over extended time horizons face critical bottlenecks in:
- Retaining multimodal experiences (text, images, audio, video)
- Organizing heterogeneous memory streams
- Recalling relevant past experiences efficiently

**Design Space Challenge**: Manual exploration cannot navigate the vast interconnected space of architecture, retrieval strategies, prompt engineering, and data pipelines.

## Key Results

Starting from naive baseline (F1 = 0.117 on LoCoMo):

| Benchmark | Initial | Final | Improvement |
|-----------|---------|-------|-------------|
| **LoCoMo** | 0.117 | 0.598 | **+411%** |
| **Mem-Gallery** | 0.254 | 0.797 | **+214%** |

**Critical Finding**: Highest-impact discoveries are NOT hyperparameter adjustments:
- Bug fixes: **+175%**
- Architectural changes: **+44%**
- Prompt engineering: **+188%** (on specific categories)

These exceed cumulative contribution of all hyperparameter tuning - demonstrating capabilities beyond traditional AutoML.

## Three Core Architectural Principles

### 1. Selective Ingestion

**Novelty-Based Filtering**: Before storage, lightweight perceptual encoders assess novelty and discard redundant content:
- **Vision**: CLIP embeddings detect scene changes across frames
- **Audio**: VAD speech probability gates retention
- **Text**: Jaccard overlap filters near-duplicates

**Multimodal Atomic Units (MAUs)**: Unified representation decoupling metadata from raw content:
```
M = ⟨s, e, p, τ, m, ℓ⟩
```
- `s`: text summary
- `e`: embedding
- `p`: pointer to raw content (cold storage)
- `τ`: timestamp
- `m`: modality
- `ℓ`: structural links

**Two-Tier Storage**:
- **Hot storage**: summaries, embeddings, metadata (fast retrieval)
- **Cold storage**: large assets (images, audio, video) - lazy access

### 2. Progressive Retrieval with Hybrid Search

**Hybrid Dense-Sparse Search**:
- **Dense**: FAISS for semantic similarity
- **Sparse**: BM25 for keyword matching
- **Key Discovery**: Set-union merging (not score-based re-ranking)
  ```
  R(q) = D(q) ∪ K(q) \ D(q)
  ```

**Pyramid Retrieval** (3-level progressive expansion):
1. **Level 1**: Summaries only (~10 tokens) for top-k candidates
2. **Level 2**: Full text/captions for candidates above threshold θ
3. **Level 3**: Raw content under token budget B (greedy expansion by similarity-per-token)

All transitions use deterministic rules (not LLM judgment) to avoid latency.

### 3. Knowledge Graph-Augmented Retrieval

**Graph Structure**: G = (V, E)
- 7 entity types: Person, Location, Event, Concept, Time, Organization, Object
- Entity resolution via hybrid similarity (cosine + Jaro-Winkler)

**Retrieval Process**:
1. Identify seed entities Vq from query
2. Bounded neighborhood expansion within h hops
3. Distance-decayed relevance scoring: rG(v) = β^d(v,Vq) · conf(v)
4. Merge with hybrid search results

## Autonomous Discovery Process

**Pipeline**: AutoResearch Claw (23-stage)

**Inputs**:
1. SimpleMem codebase (unimodal text-only baseline)
2. Benchmark evaluation harnesses (LoCoMo, Mem-Gallery)
3. LLM API access

**Iterative Loop** (50 experiments):
1. Analyze prior results
2. Generate hypothesis
3. Implement code change
4. Evaluate on benchmark
5. Decision:
   - **Proceed**: metric improved ≥ 0.5%
   - **Iterate**: ambiguous result, refine hypothesis
   - **Pivot**: 2 consecutive degradations, revert and try new direction

**Discovery Taxonomy** (6 types):
1. Bug fixes (+175%)
2. Architectural changes (+44%)
3. Prompt engineering (+188%)
4. Hyperparameter tuning
5. Data pipeline modifications
6. Evaluation alignment

## Why Multimodal Memory Suits Autoresearch

Four key properties:
1. **Immediate scalar metrics**: Tight optimization loops
2. **Modular architecture**: Isolated component modification
3. **Fast iteration**: 1-2 hours per experiment
4. **Version control**: Clean reversion of failed experiments

## Implementation Guidelines

### For Building Multimodal Memory Systems:

1. **Start with novelty filtering** - reduces storage without losing semantics
2. **Use MAU representation** - decouple searchable metadata from heavy content
3. **Implement hybrid search with set-union** - avoids re-ranking degradation
4. **Apply pyramid retrieval** - adapt context depth to query complexity
5. **Build knowledge graph** - enable multi-hop reasoning
6. **Use deterministic transitions** - avoid LLM latency in retrieval path

### For Applying Autoresearch:

1. Ensure well-defined quantitative evaluation signals
2. Design modular architecture for isolated modifications
3. Maintain fast iteration cycles (hours, not days)
4. Use version control for clean experiment management

## When to Apply

- Building lifelong multimodal agent memory
- Optimizing complex multi-component AI systems
- Exploring large design spaces beyond manual capability
- Need SOTA retrieval performance on memory benchmarks

## Related Work

- **SimpleMem**: Unimodal text-only baseline (Liu et al., 2026a)
- **AutoResearch Claw**: 23-stage autonomous research pipeline (Liu et al., 2026b)
- **MemGPT**: OS-inspired memory hierarchies (Packer et al., 2023)
- **A-Mem**: LLM-directed memory reorganization (Xu et al., 2025a)
- **MemVerse**: Episodic-semantic with multimodal knowledge graphs (Liu et al., 2025)
