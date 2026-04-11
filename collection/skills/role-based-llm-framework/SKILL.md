---
name: role-based-llm-framework
description: 'Implement role-based multi-agent LLM frameworks for complex domain tasks. Use when extracting structured information from diverse documents, building domain-specific agent teams, or reducing hallucinations through role specialization. Based on arXiv:2604.01529 - A Role-Based LLM Framework for Structured Information Extraction from Healthy Food Policies.'
---

# Role-Based LLM Framework

Assign specialized roles to LLMs for complex domain tasks, reducing hallucinations and improving accuracy.

## Problem

Standard LLM approaches for domain-specific tasks face:
- Hallucinations from structural diversity
- Misclassifications from inconsistent formats
- Omissions from missing domain knowledge

## Role-Based Framework

Assign specialized roles mimicking expert analysis workflows:

### Role Types

| Role | Responsibility | Domain Knowledge |
|------|----------------|------------------|
| Analyst | Metadata & classification | Domain structure, terminology |
| Specialist | Complex approach identification | Sub-domain expertise |
| Expert | Categorization | Domain-specific taxonomies |

### Example: Policy Analysis

```python
roles = {
    "policy_analyst": {
        "task": "metadata and mechanism classification",
        "knowledge": "policy structure, legal mechanisms"
    },
    "legal_specialist": {
        "task": "identify complex legal approaches",
        "knowledge": "legal strategy patterns, case law"
    },
    "food_system_expert": {
        "task": "categorize food system stages",
        "knowledge": "food supply chain taxonomy"
    }
}
```

## Implementation

### 1. Role-Specific Prompts

Embed domain knowledge into role prompts:
```python
analyst_prompt = """
Role: Policy Analyst
Knowledge: {explicit_definitions, classification_criteria}
Task: Extract metadata and classify mechanisms

Document: {input}
Output: {structured_fields}
"""
```

### 2. Structured Domain Knowledge

Include in prompts:
- Explicit definitions of key concepts
- Classification criteria
- Domain taxonomies
- Common patterns and exceptions

### 3. Workflow

```python
# Sequential role application
metadata = analyst.extract(document)
legal_approaches = specialist.identify(document, metadata)
categories = expert.categorize(document, metadata, legal_approaches)

# Combine outputs
final_extraction = aggregate(metadata, legal_approaches, categories)
```

## Evaluation

Tested against baselines (zero-shot, few-shot, CoT) using Llama-3.3-70B:
- Superior performance on complex reasoning tasks
- Reduced hallucinations
- More reliable extraction
- Transparent methodology (role assignments explainable)

## When to Apply

- Domain-specific information extraction
- Tasks requiring multiple expert perspectives
- Documents with structural diversity
- Reducing hallucinations in specialized tasks
- Building explainable LLM workflows

## Key Benefits

1. **Specialization**: Each role focuses on narrow task
2. **Domain knowledge**: Explicit definitions in prompts
3. **Workflow mimicry**: Follows expert analysis patterns
4. **Transparency**: Role assignments explain outputs
5. **Reduced hallucinations**: Domain constraints prevent generic outputs

## Paper Reference

arXiv:2604.01529 - "A Role-Based LLM Framework for Structured Information Extraction from Healthy Food Policies" (Apr 2026)
## Activation Keywords

- role-based-llm-framework
- role-based-llm-framework 技能
- role-based-llm-framework skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Specialization

### Step 2: Domain knowledge

### Step 3: Workflow mimicry

### Step 4: Transparency

### Step 5: Reduced hallucinations

## Examples

### Example 1: Basic Application

**User:** I need to apply Role-Based LLM Framework to my analysis.

**Agent:** I'll help you apply role-based-llm-framework. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for role-based-llm-framework?

**Agent:** Let me search for the latest research and best practices...
