---
title: "AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack"
authors: "Justin Tan, Miao Li, Ding Zhao"
published: "2026-10-22"
arxiv_id: "2610.31404v1"
url: "https://arxiv.org/abs/2610.31404v1"
categories: ["cs.CR", "cs.AI"]
utility_score: 0.98
tags: [arxiv, paper, security-privacy]
---

# AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack

**Authors:** Justin Tan, Miao Li, Ding Zhao
**Published:** 2026-10-22
**arXiv:** [2610.31404v1](https://arxiv.org/abs/2610.31404v1)
**Categories:** cs.CR, cs.AI
**Utility Score:** 0.98

## Abstract

Computer-use agents increasingly handle private information and act on users' behalf across desktop and web applications, including email. Phishing therefore poses privacy and security risks that depend not only on whether agents recognize malicious messages, but also on how they respond. Existing phishing datasets were developed primarily for conventional detection, leaving agent susceptibility to persuasive malicious requests insufficiently characterized. To expose vulnerabilities that pre-existing datasets may miss, we introduce AgentPhishing, a benchmark for evaluating whether persuasive phishing attacks can evade detection and induce LLM email agents to comply with malicious requests. We develop PhishOpt, which optimizes reusable email-generation skills against individual agents under fixed benchmark constraints and a realism constraint. We analyze the generated emails using Cialdini's persuasion principles to identify strategies associated with agent failures and use these findings to construct a universal generation skill. Our evaluation shows that agents can handle pre-existing phishing emails safely yet remain susceptible to attacks adapted to agent behavior, while in an AgentPhishing evaluation of nine agents, four exhibit phishing-detection rates below $10\%$ and malicious-request compliance rates above $45\%$. These results highlight the limits of inferring agent safety from conventional phishing evaluations and the need to assess how agents respond to persuasive malicious requests.

## Key Contributions

- Research paper from arXiv, auto-processed by Hermes cron job
- Utility score >= 0.85 indicates high relevance for AI/ML research
- Category: security-privacy

## Related Skills

Check the `security-privacy` directory for related papers and tools.
