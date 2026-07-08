---
name: llm-as-a-verifier
description: "General-purpose verification framework using probabilistic logit expectation for continuous scoring, enabling multi-dimensional scaling of verification along granularity, repeated evaluation, and criteria decomposition."
---

# LLM-as-a-Verifier: Probabilistic Verification Framework

## Description
A general-purpose verification framework that treats verification as a new scaling axis for LLM capabilities. Instead of discrete LM judges producing ordinal scores, LLM-as-a-Verifier computes the expectation over scoring token logits to generate continuous scores, enabling verification to scale along three dimensions: score granularity, repeated evaluation, and criteria decomposition. Achieves SOTA on Terminal-Bench V2 (86.5%), SWE-Bench Verified (78.2%), RoboRewardBench (87.4%), and MedAgentBench (73.3%).

## Activation Keywords
- LLM-as-a-verifier
- verification framework
- probabilistic scoring
- logit expectation scoring
- verification scaling
- continuous verification scores
- verifier-based ranking
- llm verifier
- 验证框架
- 概率评分
- 连续验证分数
- 验证缩放

## Tools Used
- terminal: Run LLM API calls to compute scoring token logit expectations
- execute_code: Implement the probabilistic scoring computation
- read: Parse task outputs and verification criteria

## Core Concepts

### Probabilistic Scoring
Standard LM judges prompt LLMs to produce discrete scores (e.g., "Score: 1-5"). LLM-as-a-Verifier instead:
1. Defines a set of scoring tokens (e.g., "0", "1", "2", ..., "100")
2. Computes the logit probabilities for each scoring token
3. Takes the expectation: `E[score] = Σ(token_value × P(token))`
4. Returns a continuous, fine-grained score

This probabilistic formulation enables three scaling dimensions:

### Scaling Dimension 1: Score Granularity
- Finer score bins (e.g., 0-100 vs 1-5) → better separation between positive/negative solutions
- More calibrated comparisons between candidate solutions
- Soft transitions instead of hard cutoffs

### Scaling Dimension 2: Repeated Evaluation
- Evaluate the same solution multiple times with the verifier
- Average scores to reduce variance
- Higher repeated evaluations → higher verification accuracy

### Scaling Dimension 3: Criteria Decomposition
- Break complex verification into sub-criteria
- Score each criterion independently
- Aggregate sub-scores with weighted combination
- Reduces complexity of individual verification judgments

## Usage Patterns

### Pattern 1: Continuous Verification Scoring
Use when you need to rank or compare multiple candidate solutions with fine-grained discrimination.

```
Given N candidate solutions for a task:
1. For each solution, prompt the verifier with the task + solution
2. Extract logits for scoring tokens (e.g., "0" through "10")
3. Compute expected score: E = Σ(i × P("i"))
4. Rank solutions by continuous score
```

### Pattern 2: Criteria Decomposition for Complex Tasks
Use for tasks with multiple evaluation dimensions (e.g., code quality, correctness, efficiency).

```
For complex agentic tasks:
1. Decompose verification into criteria: [correctness, completeness, efficiency, readability]
2. For each criterion, run the verifier separately
3. Compute continuous score for each criterion
4. Aggregate: weighted_sum(criteria_scores) or product(criteria_scores)
5. Use decomposition scores to guide targeted improvements
```

### Pattern 3: Repeated Evaluation for Variance Reduction
Use when single-pass verification has high variance (e.g., creative tasks, ambiguous solutions).

```
For noisy verification tasks:
1. Run verifier N times on the same solution
2. Collect N continuous scores
3. Compute mean and confidence interval
4. Use mean score for ranking, CI for uncertainty estimation
```

### Pattern 4: Cost-Efficient Candidate Ranking
Use when you need to select the best solution from many candidates efficiently.

```
Two-stage ranking:
1. Stage 1: Quick single-pass verification on all candidates → top-K filter
2. Stage 2: Multi-criteria, repeated evaluation on top-K only
3. Select best from Stage 2 ranking
```

### Pattern 5: Dense RL Feedback Signal
Use the verifier's continuous scores as reward signals for reinforcement learning.

```
For RL fine-tuning (SAC, GRPO, etc.):
1. Generate N candidate responses
2. Score each with LLM-as-a-Verifier (continuous)
3. Use scores as dense reward signal instead of sparse binary pass/fail
4. Improves sample efficiency over sparse-reward RL
```

## Instructions for Agents

### Step 1: Define Scoring Tokens
- Choose a granularity appropriate for the task (e.g., 0-10 for quick checks, 0-100 for fine-grained ranking)
- Scoring tokens should be: ["0", "1", "2", ..., "N"]
- Ensure the LLM can reliably produce these as scoring tokens

### Step 2: Construct Verification Prompt
```
Task: {task_description}
Solution: {candidate_solution}

Please evaluate the correctness and quality of this solution.
Score from 0 (completely incorrect) to {max_score} (perfect):
```

### Step 3: Compute Expected Score
```python
# Pseudocode for expected score computation
scoring_tokens = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
logits = get_logits_for_tokens(verifier_response, scoring_tokens)
probabilities = softmax(logits)
expected_score = sum(int(t) * p for t, p in zip(scoring_tokens, probabilities))
```

### Step 4: Apply Scaling
- **Granularity**: Increase max_score for more discrimination
- **Repeated**: Run N times, average results
- **Decomposition**: Split into sub-criteria, aggregate

### Step 5: Interpret Results
- Scores > threshold → accept solution
- Scores near decision boundary → request repeated evaluation
- Low scores across all candidates → regenerate candidates

## Error Handling

### Logit Extraction Failure
If the LLM doesn't produce clean scoring token logits:
1. Use a forced-decoding approach: constrain the model to output only scoring tokens
2. Fallback to discrete LM judge with multiple evaluations
3. Use regex parsing of the model's text output as a last resort

### Calibration Issues
If scores don't correlate well with ground truth:
1. Increase score granularity (more bins)
2. Add criteria decomposition
3. Use few-shot examples in the verification prompt
4. Increase repeated evaluations

### Token Cost Management
For large-scale verification:
1. Use smaller/faster models for initial filtering
2. Reserve larger models for final ranking of top candidates
3. Cache verification results for repeated solutions

## Performance Benchmarks (from arXiv:2607.05391)
- Terminal-Bench V2: 86.5% (SOTA)
- SWE-Bench Verified: 78.2% (SOTA)
- RoboRewardBench: 87.4% (SOTA)
- MedAgentBench: 73.3% (SOTA)

## Examples

### Example 1: Code Solution Verification
```
Task: Implement a binary search in Python
Candidate: def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

Verification prompt: "Evaluate this binary search implementation.
Score 0-10 based on: correctness, edge case handling, code clarity."

Expected output: continuous score like 8.73 (from logit expectation)
```

### Example 2: Multi-Criteria Decomposition
```
Task: Build a web scraper
Criteria: [functionality, robustness, efficiency, code quality]

Verification scores:
- Functionality: 9.1
- Robustness: 6.8 (fails on malformed HTML)
- Efficiency: 8.5
- Code quality: 9.0

Aggregated: weighted_mean([9.1, 6.8, 8.5, 9.0], weights=[0.3, 0.3, 0.2, 0.2]) = 8.45

Action: Target robustness improvement for this candidate
```

## Related Skills
- `self-verification` — Multi-round generate-verify iteration for code and reasoning
- `validation-driven-llm-workflow` — Verification-driven LLM workflow pattern
- `opencode` — For skills involving code generation
- `agent-integration-testing` — Integration testing patterns for autonomous agents

## Resources
- Paper: arXiv:2607.05391 — "LLM-as-a-Verifier: A General-Purpose Verification Framework"
- Code: https://github.com/llm-as-a-verifier/llm-as-a-verifier
- Website: https://llm-as-a-verifier.com
