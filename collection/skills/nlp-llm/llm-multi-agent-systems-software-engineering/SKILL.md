---
name: llm-multi-agent-systems-software-engineering
description: "Select frameworks for LLM multi-agent systems."
metadata:
  arxiv_id: "2608.11965"
  published: "2026-08-12"
  authors: "Mariama Celi Serafim De Oliveira, Motunrayo Osatohanmen Ibiyo, Marco Gianrusso, Claudio Di Sipio, Davide Di Ruscio, Phuong T. Nguyen"
  conference: "Empirical Software Engineering journal"
  tags: [systems-engineering, multi-agent-systems, llm, software-engineering, framework-selection]
license: Complete terms in LICENSE.txt
---

# LLM-based Multi-Agent Systems in Software Engineering

This skill implements the methodology from arXiv:2608.11965 for selecting, evaluating, and implementing LLM-based multi-agent systems (MAS) in software engineering contexts.

## Core Methodology

The paper provides a comprehensive mixed-method approach combining quantitative analysis of MAS frameworks with qualitative empirical evaluation through a common use case (requirements file summarization). The methodology helps developers navigate the complex landscape of available MAS tools and frameworks.

## Framework Evaluation Criteria

### Quantitative Analysis Dimensions
1. **Documentation Quality**: Completeness, clarity, and examples
2. **Feature Coverage**: Support for fundamental MAS components (agent roles, communication protocols, coordination mechanisms)
3. **Developer Experience**: Ease of setup, configuration, and integration
4. **Advanced Capabilities**: Telemetry, monitoring, debugging support

### Qualitative Evaluation Approach
1. **Common Use Case Implementation**: Implement the same task across multiple frameworks
2. **Performance Metrics**: ROUGE scores for text generation tasks, response time, resource usage
3. **Maintainability Assessment**: Code complexity, extensibility, error handling
4. **Scalability Testing**: Performance under varying agent counts and task complexity

## Key Findings

### Framework Capabilities
- Most frameworks provide good coverage of fundamental MAS components
- Advanced features like agent telemetry are still missing in many frameworks
- No significant performance differences in basic tasks (e.g., ROUGE scores for summarization)

### Implementation Challenges
1. **Technology Selection**: Choosing appropriate LLM providers and agent frameworks
2. **Coordination Rules**: Designing effective communication and collaboration protocols
3. **Role Design**: Defining specific, non-overlapping agent responsibilities
4. **Error Handling**: Managing failures and inconsistencies in multi-agent workflows

## Practical Guidelines

### Framework Selection Process
1. **Define Requirements**: Identify specific needs (coordination complexity, scalability, monitoring)
2. **Shortlist Candidates**: Based on documentation quality and feature coverage
3. **Prototype Implementation**: Test with a representative use case
4. **Evaluate Trade-offs**: Balance between features, performance, and maintainability

### Implementation Best Practices
1. **Modular Architecture**: Separate agent logic from coordination logic
2. **Standardized Communication**: Use consistent message formats and protocols
3. **Comprehensive Logging**: Track agent interactions and decision processes
4. **Graceful Degradation**: Handle agent failures without system collapse

### Common Pitfalls and Mitigations

#### Over-Engineering
**Problem**: Creating overly complex agent architectures for simple tasks
**Mitigation**: Start with minimal viable agent systems and incrementally add complexity

#### Poor Coordination
**Problem**: Agents working at cross-purposes or duplicating effort
**Mitigation**: Implement clear role definitions and coordination protocols

#### Inadequate Monitoring
**Problem**: Difficulty debugging and understanding agent behavior
**Mitigation**: Implement comprehensive logging and visualization tools

#### Vendor Lock-in
**Problem**: Tight coupling to specific LLM providers or frameworks
**Mitigation**: Use abstraction layers and standardized interfaces

## Activation Keywords
- LLM multi-agent systems
- MAS framework selection
- software engineering agents
- multi-agent coordination
- LLM-based software development
- agent orchestration patterns

## References
- Original paper: https://arxiv.org/abs/2608.11965
- Empirical Software Engineering journal
- Requirements file summarization use case