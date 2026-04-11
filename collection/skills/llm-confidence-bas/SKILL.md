# SKILL.md - Behavioral Alignment Score (BAS) for LLM Confidence

## Paper Reference
- **arXiv:** 2604.03216
- **Title:** A Decision-Theoretic Approach to Evaluating Large Language Model Confidence
- **Utility Score:** 0.87
- **Authors:** Sean Wu et al.
- **Date:** April 2026

## Core Insights

### Key Problem
LLMs produce confident but incorrect answers when abstention would be safer.
Standard metrics (ECE, AURC) don't capture decision-level reliability.

### Solution: Behavioral Alignment Score (BAS)
- **Decision-theoretic metric** for abstention-aware decision making
- Derived from explicit answer-or-abstain utility model
- Aggregates realized utility across continuum of risk thresholds

### Key Properties
- Truthful confidence estimates uniquely maximize expected BAS
- Links calibration to decision-optimal behavior
- **Asymmetric penalty:** strongly prioritizes avoiding overconfident errors
- Unlike log loss (symmetric), BAS penalizes overconfidence more

### Findings
- Models with similar ECE/AURC can have very different BAS
- Frontier models remain prone to severe overconfidence
- Simple interventions improve confidence reliability

## Practical Applications

### Confidence Evaluation
```markdown
1. Compute BAS alongside ECE/AURC
2. Identify overconfident failure patterns
3. Apply top-k confidence elicitation
4. Post-hoc calibration improvements
```

### Decision Systems
- When to trust model output
- When to request abstention
- Risk-adjusted confidence thresholds

### Intervention Strategies
- Top-k confidence elicitation
- Post-hoc calibration
- Risk-aware prompting

## Key Takeaways
- BAS better captures decision-useful confidence
- Overconfidence errors are the critical risk
- Larger/accurate models ≠ better BAS
- Standard metrics miss overconfident failures

## Related Work
- Expected Calibration Error (ECE)
- Area Under Rejection Curve (AURC)
- Log loss / proper scoring rules

## Further Reading
- Full paper: https://arxiv.org/abs/2604.03216
- PDF: https://arxiv.org/pdf/2604.03216
- Benchmark across multiple LLMs/tasks
## Description

SKILL.md - Behavioral Alignment Score (BAS) for LLM Confidence

## Activation Keywords

- llm-confidence-bas
- llm-confidence-bas 技能
- llm-confidence-bas skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Understand the Request

### Step 2: Search for Information

### Step 3: Apply the Framework

### Step 4: Provide Results

### Step 5: Verify Accuracy

## Examples

### Example 1: Basic Application

**User:** I need to apply SKILL.md - Behavioral Alignment Score (BAS) for LLM Confidence to my analysis.

**Agent:** I'll help you apply llm-confidence-bas. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for llm-confidence-bas?

**Agent:** Let me search for the latest research and best practices...
