---
name: cogeegagent-autonomous-cognitive-eeg-analysis
description: "CogEEGAgent methodology for autonomous cognitive EEG analysis with grounded execution and selection-aware verification. Uses MNE-Python framework with LLM agents for flexible language understanding while maintaining fail-closed control over inference and release. Provides auditable automation framework for cognitive-EEG workflows with participant-disjoint confirmation and capability hazard blocking."
metadata:
  arxiv_id: "2607.25045"
  published: "2026-07-27"
  authors: "Dengzhe Hou, Lingyu Jiang, Fangzhou Lin, Kazunori D Yamada"
  tags: [eeg, cognitive-neuroscience, llm-agents, mne-python, autonomous-analysis]
license: Complete terms in LICENSE.txt
---

# CogEEGAgent: Autonomous Cognitive EEG Analysis

## Overview

CogEEGAgent is a cognitive-EEG analysis agent that combines flexible language understanding with fail-closed control over inference and release. It provides an auditable automation framework for cognitive-EEG workflows using MNE-Python as the scientific foundation.

## Core Principles

### Grounded Execution
- **Semantic vs Scientific Authority**: Separates LLM's semantic interpretation from deterministic scientific validation
- **Typed Contracts**: Validates analysis choices against registered EEG-specific contracts
- **Evidence-Bound Release**: Authorizes only analyses supported by participant-disjoint confirmation

### Selection-Aware Verification
- **Adaptive Search Control**: Blocks uncorrected adaptive search that could lead to false positives
- **Capability Hazard Blocking**: Prevents prespecified dangerous operations and lifecycle-reuse requests
- **Policy Stress Testing**: Uses held-out confirmation to curb false positives

## Methodology

### System Architecture
1. **LLM Component**: Interprets natural language intent and proposes registered analyses
2. **Deterministic Components**: 
   - Validate typed contracts
   - Control confirmation access  
   - Authorize evidence-bound release
3. **Scientific Harness**: Grounds execution in MNE-Python framework

### Workflow Steps
1. **Intent Interpretation**: LLM translates natural language questions into analysis proposals
2. **Contract Validation**: System validates proposals against EEG-specific registered analyses
3. **Confirmation Access**: Controls access to participant-disjoint confirmation data
4. **Evidence Evaluation**: Evaluates whether analysis is supported by evidence
5. **Release Authorization**: Only releases supported analyses with proper verification

### Key Features
- **Bounded Autonomy**: Flexible language interface with constrained scientific execution
- **Auditable Framework**: Complete traceability of analysis decisions and verifications
- **Hazard Prevention**: Blocks capability hazards and lifecycle-reuse requests
- **Routing Accuracy**: Maps language to registered analyses more accurately than deterministic routers

## Implementation Guidelines

### Prerequisites
- MNE-Python installation
- EEG dataset with proper metadata
- Registered analysis protocols
- Confirmation dataset (participant-disjoint)

### Setup Steps
1. Initialize CogEEGAgent with MNE-Python environment
2. Load registered analysis contracts
3. Configure confirmation access controls
4. Set up hazard prevention policies
5. Establish release authorization rules

### Usage Patterns
- **Natural Language Queries**: Submit varied natural-language questions about EEG analysis
- **Analysis Proposals**: Review LLM-proposed registered analyses
- **Verification Reports**: Examine selection-aware verification results
- **Audit Trails**: Access complete execution and decision logs

## Pitfalls and Limitations

### Common Issues
- **Over-reliance on LLM fluency**: Fluent reports don't guarantee correct analysis selection
- **Adaptive search bias**: Uncorrected adaptive search can inflate false positives
- **Confirmation contamination**: Ensure participant-disjoint confirmation to maintain validity

### Mitigation Strategies
- **Preflight validation**: Use matched preflight to ensure system abstains when required
- **Policy stress testing**: Regularly test with held-out confirmation data
- **Hazard blocking**: Implement comprehensive capability hazard prevention

## Applications

### Cognitive Neuroscience
- Automated EEG analysis for cognitive studies
- Flexible interface for non-expert researchers
- Auditable workflow for reproducible research

### Clinical Applications
- Standardized EEG analysis protocols
- Evidence-based clinical decision support
- Regulatory-compliant analysis frameworks

### Research Automation
- High-throughput EEG analysis pipelines
- Multi-study meta-analysis frameworks
- Collaborative research platforms

## References
- Original Paper: arXiv:2607.25045 [cs.AI]
- MNE-Python Documentation: https://mne.tools/
- Related Work: Autonomous scientific agents, LLM-powered research automation

## Activation Keywords
- cogeegagent
- autonomous eeg analysis
- cognitive eeg agent
- grounded eeg execution
- selection-aware verification
- mne-python agent
- auditable eeg workflow
- participant-disjoint confirmation