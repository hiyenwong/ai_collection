---
name: convex-tokenization
description: "ConvexTok methodology — formulating tokenizer construction as a convex optimization (linear program) instead of greedy BPE/Unigram. Use when: (1) Designing tokenizers for new languages or domains, (2) Improving bits-per-byte (BpB) efficiency of LLM tokenizers, (3) Evaluating tokenizer quality beyond greedy heuristics, (4) Tokenizer research comparing BPE/Unigram vs. globally optimal approaches."
arxiv_id: "2605.22821"
date: "2026-05-21"
authors: "Unknown"
tags: ["information-science", "tokenization", "nlp", "convex-optimization", "llm-preprocessing"]
---

# ConvexTok: Tokenization via Convex Relaxations

## Description

Current tokenizer algorithms (BPE, Unigram) are greedy — they make locally optimal decisions without considering the vocabulary as a whole. ConvexTok formulates tokenizer construction as a linear program and solves it using convex optimization tools, yielding globally better tokenizers.

## Core Insight

**Problem**: BPE/Unigram make greedy merge/split decisions → suboptimal vocabulary.

**Solution**: Formulate as LP with constraints on vocabulary size, coverage, and compression → solve globally.

## Mathematical Framework

The tokenization problem is formulated as:

```
min Σ_i c_i · x_i
subject to:
  Σ_i A_ij · x_i ≥ 1  (coverage constraint)
  Σ_i x_i ≤ V          (vocabulary size constraint)
  x_i ∈ {0, 1}         (selection variable)
```

Where:
- `x_i` = whether subword i is in vocabulary
- `c_i` = cost (frequency-weighted length) of subword i
- `A_ij` = coverage matrix (subword i covers position j)
- `V` = target vocabulary size

Relax to `x_i ∈ [0, 1]` for convex solution, then round.

## Key Advantages

1. **Global optimization**: Considers full vocabulary, not greedy merges
2. **Intrinsic metrics**: Consistently improves BpB (bits-per-byte)
3. **Flexible constraints**: Can add domain-specific constraints
4. **Theoretical guarantees**: Convex relaxation provides optimality bounds

## Usage Patterns

### Pattern 1: Tokenizer Design for New Domain

When building a tokenizer for a specialized domain (medical, legal, code):

1. Collect domain corpus
2. Build candidate subword inventory (all n-grams up to max length)
3. Formulate LP with domain-specific costs
4. Solve with convex optimizer (CVX, scipy.optimize)
5. Round solution to integer vocabulary
6. Validate BpB on held-out data

### Pattern 2: Tokenizer Evaluation

Compare existing tokenizers against ConvexTok upper bound:

1. Run ConvexTok on same corpus as BPE/Unigram
2. Compare BpB: ConvexTok provides theoretical upper bound
3. Gap analysis: large gap → greedy tokenizer is far from optimal

### Pattern 3: Hybrid Approach

Use ConvexTok to initialize vocabulary, then fine-tune:

1. Run ConvexTok to get globally optimal initial vocabulary
2. Use as starting point for further BPE merges
3. Achieve better final tokenizer than pure BPE

## Implementation Guidance

### LP Solver Selection

- **Small vocabularies** (<100K candidates): `scipy.optimize.linprog`
- **Medium** (100K-1M): `cvxpy` with ECOS or SCS solver
- **Large** (>1M): Column generation + specialized solver

### Rounding Strategy

After solving LP relaxation:
1. **Threshold rounding**: x_i > 0.5 → include
2. **Greedy rounding**: Select highest fractional values until budget
3. **Pipage rounding**: Preserves LP objective bounds

## Error Handling

### LP Infeasible
- Check vocabulary size constraint V is feasible
- Verify coverage constraints aren't contradictory
- Relax constraints iteratively

### Slow Solve Time
- Use column generation: start with small candidate set
- Add promising subwords iteratively
- Warm-start from BPE vocabulary

## Resources

- **arXiv**: [2605.22821](https://arxiv.org/abs/2605.22821)
- **Related**: BPE, Unigram, SentencePiece, convex optimization
