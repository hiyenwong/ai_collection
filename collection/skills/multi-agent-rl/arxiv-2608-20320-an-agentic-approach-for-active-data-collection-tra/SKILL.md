---
name: arxiv-2608-20320-an-agentic-approach-for-active-data-collection-tra
description: 'An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and Weather-Sensitive Demand Prediction (arXiv: 2608.20320)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and Weather-Sensitive Demand Prediction

**Authors:** Narges Ahmadi, Yubo Jiao, Jônatas Augusto Manzolli, Jiangbo Yu, Luis Miranda-Moreno
**arXiv:** 2608.20320
**Utility:** 1.00
**Published:** 2026-08-20T17:57:42Z
**Link:** http://arxiv.org/abs/2608.20320

## Abstract

Travel behavior research increasingly combines digital data collection with predictive modeling, yet these stages are often developed and evaluated separately. This study proposes a three-agent workflow integrating conversational data collection, structured data processing, and behavioral prediction. A chatbot-administered, image-augmented stated-preference survey collected mode choices from student commuters across five predefined weather scenarios, yielding 454 respondent-scenario observations. Weather-related associations were analyzed using a multinomial logit model, while logistic regression and random forest provided machine-learning benchmarks. Nine locally deployed large language models (LLMs), ranging from 2 to 35 billion parameters, were evaluated across four zero-shot prompt-and-context conditions and extended through persona, few-shot, and vision-based configurations. Random forest achieved 69.6% five-class accuracy, while the best text-only zero-shot LLM reached 69.9% without task-specific fitting. Habitual travel information produced the most consistent gains, Expert framing generally outperformed Role-Play, and persona information was most useful when habitual travel information was unavailable. Few-shot prompting improved prediction for several models, with gains stabilizing after a small number of examples. Using the same weather images shown to respondents, the best vision-based configuration reached 71.5% five-class accuracy, indicating that visual context may provide additional predictive information for selected models. Overall, the study shows how conversational surveys, structured data processing, conventional behavioral modeling, machine learning, and multimodal LLM prediction can be coordinated within an auditable multi-agent workflow.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and Weather-Sensitive Demand Prediction". 
The paper presents novel ideas in multi-agent-rl that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.20320
