---
name: convex-tokenisation
description: "Tokeniser construction via convex relaxation - reformulating tokenisation as a linear program solved with convex optimisation tools"
category: information-science
---

# Convex Tokenisation (ConvexTok)

## Description
Methodology for constructing tokenisers using convex relaxation techniques. Reformulates tokeniser construction as a linear program instead of using greedy algorithms (BPE, Unigram), enabling globally optimal vocabulary construction that considers the vocabulary as a whole.

## Activation Keywords
- convex tokenisation
- ConvexTok
- tokeniser construction
- 凸松弛分词
- linear program tokeniser
- convex optimization NLP
- BPE alternative

## Tools Used
- exec: Run convex optimization solvers
- write: Create tokeniser implementations
- search_files: Find related NLP code

## Core Concepts

### Tokenisation Problem
Tokenisation maps continuous text into discrete tokens for NLP models. Traditional methods (BPE, Unigram) make locally optimal decisions greedily without considering global vocabulary quality.

### Convex Relaxation Approach
Instead of greedy merge/split decisions, formulate tokeniser construction as:
$$\min_v \mathcal{L}(v) \quad \text{s.t.} \quad v \in \mathcal{V}$$
where $v$ represents the vocabulary and $\mathcal{V}$ is the feasible set of valid tokenisations.

### Linear Programming Formulation
The tokeniser construction problem is relaxed into a linear program that can be solved optimally, yielding globally optimal vocabulary assignments.

## Mathematical Framework

### Objective Function
Minimize encoding loss over corpus while constraining vocabulary size:
$$\min_{x} \sum_{w \in \mathcal{C}} c(w) \cdot \ell(w, x)$$
subject to:
$$\sum_{t \in \mathcal{T}} x_t \leq K$$
$$x_t \in \{0, 1\} \quad \forall t \in \mathcal{T}$$

### Convex Relaxation
Relax binary constraints to $x_t \in [0, 1]$ for tractable optimization.

## Usage Patterns

### Pattern 1: Vocabulary Construction
1. Collect training corpus statistics
2. Define candidate token set
3. Formulate linear program
4. Solve with convex optimizer (CVX, scipy)
5. Extract vocabulary from solution

### Pattern 2: Tokenisation Quality Evaluation
1. Apply ConvexTok vocabulary to test corpus
2. Measure encoding efficiency (tokens per character)
3. Compare with BPE/Unigram baselines
4. Evaluate downstream task performance

## Instructions for Agents

### Step 1: Collect Corpus Statistics
Count subword frequencies from training data. Build suffix tree/array for candidate token enumeration.

### Step 2: Define Candidate Set
Generate all possible subwords up to maximum length. Filter by minimum frequency threshold.

### Step 3: Formulate LP
Construct the linear program:
- Variables: binary selection for each candidate token
- Objective: minimize total encoding cost
- Constraints: vocabulary size budget, valid tokenisation

### Step 4: Solve and Extract
Solve the relaxed LP. Round solution to binary. Extract selected tokens as vocabulary.

### Step 5: Build Tokeniser
Construct encoding/decoding functions from vocabulary.

## Error Handling

### LP Infeasibility
If LP is infeasible:
- Relax vocabulary size constraint
- Add more candidate tokens
- Check constraint consistency

### Large-Scale Optimization
For very large vocabularies:
- Use column generation
- Apply cutting plane methods
- Consider distributed solvers

## Resources
- arXiv: 2605.22821 - "Tokenisation via Convex Relaxations"
- CVXPY Python library for convex optimization
- BPE (Sennrich et al., 2016) and Unigram (Kudo, 2018) for baselines

## Related Skills
- ai-math-discovery
- prompt-optimization
- skill-creator