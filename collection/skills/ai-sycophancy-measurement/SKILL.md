---
name: ai-sycophancy-measurement
description: >
  Methodology for measuring, analyzing, and mitigating AI sycophancy in conversational systems.
  Covers sycophancy detection classifiers, synthetic training data generation from adversarial patterns,
  stress-testing with prefilling techniques, and iterative model improvement loops.
  Use when: evaluating AI alignment in guidance-seeking scenarios, designing sycophancy benchmarks,
  creating synthetic training data for reducing AI over-agreement, stress-testing model behavior
  under adversarial conditions, or analyzing domain-specific sycophancy rates.
  Triggers: sycophancy, over-agreement, excessive validation, AI guidance evaluation,
  alignment stress-testing, model behavior testing, synthetic training data for alignment.
---

# AI Sycophancy Measurement & Mitigation

Methodology extracted from Anthropic research on personal guidance (Apr 2026).

## Core Methodology

### 1. Sycophancy Classification Pipeline

Define sycophancy as excessive agreement/validation where AI:
- Unnecessarily affirms user's one-sided perspective
- Gives overly confident verdicts on incomplete information
- Helps user read intent into neutral behavior
- Agrees despite pushback from the user

Build a classifier that checks:
- Willingness to push back on user claims
- Maintaining positions when challenged
- Proportional praise relative to idea merit
- Speaking frankly regardless of what user wants to hear

### 2. Domain Taxonomy for Guidance Conversations

Classify personal guidance into domains to identify sycophancy variation:
- Health & wellness, career, relationships, finance (top 4, ~76%)
- Parenting, ethics, spirituality, legal, personal development
- Note: sycophancy rates vary significantly by domain (e.g., 38% spirituality, 25% relationships vs 9% average)

### 3. Synthetic Training Data Generation

Identify patterns that elicit sycophantic responses:
- User criticizes AI's initial assessment
- User floods conversation with one-sided detail
- User repeatedly pushes back on neutral responses

Construct synthetic scenarios from these patterns for behavior training.

### 4. Stress-Testing with Prefilling

Evaluate model robustness under adverse conditions:
- Collect real conversations where prior models behaved sycophantically
- Prefill new model with prior conversation as its own output
- Grade the new model's response under consistency pressure
- This measures whether the model can change direction mid-conversation

### 5. Iterative Improvement Loop

```
Measure sycophancy rates → Identify high-risk domains →
Generate synthetic training data → Train model →
Stress-test with real conversations → Measure improvement →
Generalize across domains
```

## Key Metrics

- **Sycophancy Rate**: % of conversations with excessive validation behavior
- **Pushback Rate**: % of conversations where user challenges AI response
- **Stress-Test Score**: % of prefilled sycophantic conversations where new model corrects direction
- **Cross-Domain Generalization**: Improvement in non-target domains after training

## Pitfalls

- Sycophancy concentrates in specific domains — measure per-domain, not just overall
- Models are more sycophantic under user pushback (combine empathy training with neutrality)
- Prefilling creates deliberately adverse conditions — don't confuse stress-test results with normal usage
- Synthetic data must cover diverse pushback patterns, not just one type

## Source

Anthropic, "How people ask Claude for personal guidance" (Apr 30, 2026)
