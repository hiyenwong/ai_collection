---
name: arxiv-2608-19938-from-noise-to-signal-improving-security-log-anomal
description: 'From Noise to Signal: Improving Security Log Anomaly Detection Using LLMs with Endpoint-Specific Logs (arXiv: 2608.19938)'
category: nlp-llm
version: "1.0"
date: 2026-08-22
---

# From Noise to Signal: Improving Security Log Anomaly Detection Using LLMs with Endpoint-Specific Logs

**Authors:** Christopher Henshaw, Gour Karmakar
**arXiv:** 2608.19938
**Utility:** 1.00
**Published:** 2026-08-20T11:54:56Z
**Link:** http://arxiv.org/abs/2608.19938

## Abstract

Existing approaches to anomalous behaviour log detection, such as Wazuh rely primarily on predefined detection rules, while statistical anomaly detection approaches such as OpenSearch identify deviations from previously observed behavioural patterns. Recent research has investigated LLMs for log anomaly detection because of their ability to interpret semantic and contextual information. However, LLM-based approaches can be affected by prompt construction, noisy log data, and reliance on generic datasets that may lack endpoint-specific authentication behaviours. To address these limitations, this study develops a standardised instruction-based LLM classification framework for detecting anomalous authentication behaviours, including borderline cases. A controlled cybersecurity testbed was developed to generate endpoint-specific authentication data, producing a curated dataset comprising normal, borderline, and anomalous behavioural scenarios. Three instruction-tuned LLMs, Meta Llama 3.1 8B Instruct, Qwen 2.5 7B Instruct, and GPT-OSS 20B, were evaluated against Wazuh rule-based detection and OpenSearch Anomaly Detection using a common ground-truth severity framework. Meta Llama 3.1 8B Instruct achieved the strongest overall end-to-end detection performance, with an accuracy of 89.3%, recall of 88.2%, F1-score of 91.8%, and false negative rate of 11.8%. In comparison, Wazuh achieved an accuracy of 52.0% and false negative rate of 68.6%, while OpenSearch achieved an accuracy of 49.3% and false negative rate of 74.5%. Meta Llama also detected 80% of the borderline anomalous scenarios, compared with 20% for Wazuh and 15% for OpenSearch. Qwen achieved lower overall detection performance than Meta Llama but recorded the lowest average inference latency and 100% structured-response validity. GPT-OSS demonstrated strong classification performance when valid responses were produced.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "From Noise to Signal: Improving Security Log Anomaly Detection Using LLMs with Endpoint-Specific Logs". 
The paper presents novel ideas in nlp-llm that can be applied to agent systems.

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

- arXiv:2608.19938
