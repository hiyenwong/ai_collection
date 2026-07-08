---
name: llmoxie-agentic-scientific-software
description: "Institutional AI platform (LLMoxie) with three-tiered architecture supporting multi-cloud and on-premise inference, LiteLLM/MLflow control plane for authentication, budgeting, PII masking, and observability, and an application augmentation layer for AI coding agents in scientific software development. Activation: LLMoxie, scientific software, AI coding agent, LiteLLM, MLflow, multi-cloud, PII masking, institutional AI."
metadata:
  arxiv_id: "2607.02703"
  published: "2026-07-02"
  authors: "Landung Setiawan, Anant Mittal, Cordero Core, Anshul Tambay, Carlos Garcia Jurado Suarez, David A. C. Beck, Andrew J. Connolly, Vani Mandava"
  tags: [llmoxie, scientific-software, ai-coding-agent, litellm, mlflow, multi-cloud, pii-masking, institutional-ai]
---

# LLMoxie: Exploring Agentic AI for Scientific Software Development

## Overview

LLMoxie is an institutional AI platform whose three-tiered architecture supports multi-cloud and on-premise inference, a LiteLLM/MLflow control plane for authentication, budgeting, PII masking, and observability, and an application augmentation layer for AI coding agents. The platform is designed to support scientific software development in institutional research environments.

## Key Innovations

### Three-Tiered Architecture

1. **Inference Layer**: Multi-cloud and on-premise inference support
   - Enables organizations to use cloud APIs while keeping sensitive workloads on-premise
   - Supports multiple LLM providers through a unified interface

2. **Control Plane (LiteLLM/MLflow)**:
   - Authentication: Centralized access control for institutional users
   - Budgeting: Track and limit spending across users and projects
   - PII Masking: Automatically detect and redact PII before sending to cloud LLMs
   - Observability: Logging, monitoring, and audit trails for all LLM interactions

3. **Application Augmentation Layer**:
   - AI coding agents integrated into scientific software development workflows
   - Augmentation rather than replacement: enhances existing development practices
   - Domain-aware: understands scientific software patterns and conventions

### Scientific Software Focus
- Tailored for research institutions with specific needs (reproducibility, data sensitivity, grant compliance)
- Supports scientific codebases with domain-specific patterns
- Balances productivity gains with institutional governance requirements

## Methodology

1. **Platform Design**: Three-tier architecture separating inference, control, and application layers
2. **LiteLLM Integration**: Unified API for multiple LLM providers with fallback and load balancing
3. **MLflow Integration**: Experiment tracking, model management, and observability
4. **PII Masking Pipeline**: Pre-inference filtering of sensitive information
5. **Coding Agent Integration**: Agents for code generation, review, and documentation in scientific repos

## Implications

- Practical architecture for deploying agentic AI in institutional/research settings
- PII masking as a first-class concern enables cloud LLM use in regulated environments
- Multi-cloud + on-premise strategy addresses data sovereignty concerns
- Demonstrates real-world deployment of AI coding agents beyond commercial tech companies
- Governance (budgeting, authentication, observability) as essential infrastructure for institutional AI

## Pitfalls

- Institutional deployments have complex procurement and compliance requirements
- PII masking may introduce false positives that degrade LLM output quality
- Multi-cloud inference adds latency and operational complexity
- Scientific software patterns may not be well-represented in general LLM training data
- Budgeting mechanisms may be too rigid for exploratory research workflows

## Activation Keywords

LLMoxie, scientific software, AI coding agent, LiteLLM, MLflow, multi-cloud, PII masking, institutional AI, research computing, observability, budgeting, authentication

## Paper Reference

arXiv:2607.02703 - "LLMoxie: Exploring Agentic AI for Scientific Software Development" (Jul 2026)
