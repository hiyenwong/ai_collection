---
name: cog-eeg-agent-autonomous-analysis
title: CogEEGAgent Autonomous EEG Analysis Framework
description: LLM-powered EEG analysis agent grounded in MNE-Python that separates semantic interpretation from scientific validation using deterministic contracts and confirmation controls to prevent false positives.
trigger_words:
  - cogeegagent
  - autonomous eeg analysis
  - llm eeg agent
  - grounded eeg analysis
  - scientific validation eeg
---

# CogEEGAgent Autonomous EEG Analysis Framework

## Overview
CogEEGAgent is an autonomous EEG analysis framework that leverages large language models (LLMs) while maintaining scientific rigor through deterministic grounding in MNE-Python. The key innovation is the separation of semantic interpretation (handled by LLM) from scientific validation (handled by deterministic code), preventing false positives through participant-disjoint confirmation controls.

## Key Components

### 1. Grounded Execution Architecture
- **MNE-Python Integration**: All EEG operations are grounded in the established MNE-Python library
- **Deterministic Contracts**: Scientific validation steps use deterministic, reproducible code
- **Semantic Interpretation**: LLM handles natural language intent and high-level reasoning
- **Execution Separation**: Clear boundary between LLM interpretation and scientific execution

### 2. Confirmation Control Framework
- **Participant-Disjoint Confirmation**: Held-out participant data used to validate findings
- **Adaptive Search Prevention**: Confirmation controls curb adaptive search errors during policy stress testing
- **False Positive Blocking**: Systematic validation prevents spurious correlations
- **Reproducibility Guarantee**: All scientific claims are backed by deterministic validation

### 3. Policy Stress Testing Results
- **Without Confirmation**: Adaptive search leads to inflated performance metrics
- **With Confirmation**: Performance aligns with ground truth, preventing overfitting
- **Robustness**: Framework maintains accuracy across diverse EEG analysis tasks
- **Scalability**: Architecture supports complex multi-step EEG analysis workflows

## Implementation Guidelines

### When to Use This Skill
Use when:
- Building autonomous EEG analysis systems
- Integrating LLMs with scientific computing workflows
- Needing to prevent false positives in data-driven discovery
- Designing reproducible neuroscientific analysis pipelines

### Architecture Design Principles

1. **Grounding Layer**:
   - Integrate with established scientific libraries (MNE-Python for EEG)
   - Ensure all operations are deterministic and reproducible
   - Provide clear API boundaries between LLM and scientific code

2. **Semantic Layer**:
   - Use LLM for natural language understanding and intent parsing
   - Handle high-level reasoning and workflow orchestration
   - Maintain separation from scientific validation logic

3. **Validation Layer**:
   - Implement participant-disjoint confirmation controls
   - Use held-out data for systematic validation
   - Block false positives through rigorous statistical testing

### Best Practices

- **Reproducibility**: Always maintain deterministic scientific validation paths
- **Transparency**: Clearly document the boundary between LLM interpretation and scientific execution
- **Validation**: Implement systematic confirmation controls for all discoveries
- **Integration**: Leverage existing scientific computing ecosystems rather than reinventing

## Applications

### EEG Analysis Workflows
- **Automated Pipeline Construction**: LLM interprets analysis goals, deterministic code executes
- **Hypothesis Testing**: Natural language hypotheses validated through systematic testing
- **Data Exploration**: Guided exploration with built-in validation to prevent false discoveries
- **Reproducible Research**: End-to-end reproducible analysis from natural language to results

### Scientific Computing Integration
- **Domain-Specific Agents**: Extend to other domains (fMRI, MEG, behavioral data)
- **Multi-Modal Analysis**: Combine multiple data modalities with unified validation
- **Collaborative Analysis**: Support team-based analysis with shared validation standards

## References
- **Paper**: "CogEEGAgent: Toward Autonomous Cognitive EEG Analysis"
- **Authors**: [Authors from arXiv:2607.25045]
- **arXiv**: 2607.25045 [q-bio.NC]  
- **Date**: July 29, 2026
- **Key Insight**: Separation of semantic interpretation from scientific validation prevents false positives in LLM-driven scientific discovery

## Related Skills
- `llm-agent-externalization`
- `validation-driven-llm-workflow`
- `tool-integrated-reasoning-recipe`