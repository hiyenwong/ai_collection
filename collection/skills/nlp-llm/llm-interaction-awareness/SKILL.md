---
name: llm-interaction-awareness
description: 'Probe and measure interaction awareness in language models using user-turn generation. Use when evaluating LLM conversation quality beyond task accuracy, measuring whether models encode awareness of what follows their responses, or designing collaboration-oriented post-training. Based on arXiv:2604.02315 - User Turn Generation as a Probe of Interaction Awareness in Language Models.'
---

# LLM Interaction Awareness

Measure whether LLMs encode awareness of conversation flow beyond task accuracy.

## Core Concept

Standard benchmarks evaluate **assistant turns** only. This leaves unmeasured whether LLMs encode awareness of what follows their responses.

**User-turn generation probe**: Given conversation context (user query + assistant response), let model generate under user role. If model has interaction awareness, generated user turn will be grounded follow-up reacting to preceding context.

## Key Findings

From experiments across 11 LLMs (Qwen3.5, gpt-oss, GLM) and 5 datasets:

1. **Interaction awareness ≠ task accuracy**: GSM8K accuracy scales from 41% (0.8B) to 96.8% (397B), yet genuine follow-up rates near zero under deterministic generation
2. **Latent awareness**: Higher temperature sampling reveals interaction awareness with follow-up rates reaching 22%
3. **Decoupled dimensions**: Task accuracy and interaction awareness are independent properties

## Probe Methodology

To measure interaction awareness:

```python
# Given: user_query, assistant_response (conversation context)
# Generate: next_user_turn under user role

prompt = f"""
User: {user_query}
Assistant: {assistant_response}
User: [GENERATE NEXT TURN AS USER]
"""

# Measure: Is generated turn a grounded follow-up?
# - Reacts to preceding context?
# - Makes sense as conversation continuation?
# - Not generic/hallucinated?
```

## Follow-Up Rate Metrics

- **Genuine follow-up**: Generated turn is grounded, contextually relevant
- **Follow-up rate**: Percentage of generations that are genuine follow-ups
- **Temperature sensitivity**: Follow-up rates increase with temperature sampling

## Post-Training for Interaction Awareness

Collaboration-oriented post-training on Qwen3.5-2B demonstrated:
- Increased follow-up rates
- Improved interaction awareness
- Better conversation grounding

## When to Apply

- Evaluating LLMs for conversational agents
- Benchmarking beyond task accuracy
- Designing post-training for dialogue models
- Measuring latent model capabilities
- Building multi-turn reasoning systems

## Implications

- Current assistant-only benchmarks miss critical dimension of LLM behavior
- Task accuracy alone insufficient for conversational quality
- Temperature affects interaction awareness emergence
- Post-training can specifically target interaction awareness

## Paper Reference

arXiv:2604.02315 - "User Turn Generation as a Probe of Interaction Awareness in Language Models" (Apr 2026)
## Activation Keywords

- llm-interaction-awareness
- llm-interaction-awareness 技能
- llm-interaction-awareness skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Interaction awareness ≠ task accuracy

### Step 2: Latent awareness

### Step 3: Decoupled dimensions

### Step 4: Understand the Request

### Step 5: Search for Information

## Examples

### Example 1: Basic Application

**User:** I need to apply LLM Interaction Awareness to my analysis.

**Agent:** I'll help you apply llm-interaction-awareness. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for llm-interaction-awareness?

**Agent:** Let me search for the latest research and best practices...
