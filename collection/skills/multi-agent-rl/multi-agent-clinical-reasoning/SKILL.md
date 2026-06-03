---
name: multi-agent-clinical-reasoning
description: "Multi-agent framework for clinical reasoning and radiology AI. Use when designing multi-agent systems for medical diagnosis, radiology report generation, clinical decision support, or multi-modal medical reasoning. Triggers: multi-agent radiology, clinical reasoning agents, multi-agent medical AI, radiology report generation, clinical decision support agents."
---

# Multi-Agent Clinical Reasoning

Designs and analyzes multi-agent frameworks for clinical reasoning, radiology AI, and medical diagnosis support.

## Core Concept

Multi-agent clinical reasoning uses multiple specialized AI agents collaborating to analyze medical data, generate reports, and support clinical decisions. Each agent handles a specific aspect (imaging analysis, clinical context, report generation, quality assurance).

## Agent Roles

| Agent Type | Responsibility | Tools |
|------------|---------------|-------|
| **Imaging Agent** | Analyze radiology images | CNN, Vision Transformers |
| **Context Agent** | Process clinical history | LLM, Medical knowledge bases |
| **Report Agent** | Generate structured reports | LLM, Template systems |
| **QA Agent** | Validate consistency | Cross-checking, uncertainty estimation |
| **Coordinator** | Orchestrate collaboration | Reinforcement learning, consensus protocols |

## Framework Patterns

### Pattern 1: Consensus-Based Diagnosis
Multiple agents analyze independently → Vote/consensus mechanism → Final diagnosis

```python
agents = [imaging_agent, context_agent, report_agent]
votes = [agent.analyze(patient_data) for agent in agents]
diagnosis = consensus_protocol(votes, weights)
```

### Pattern 2: Pipeline Orchestration
Sequential agent pipeline → Each agent enriches previous output

```
Image → Imaging Agent → Findings → Context Agent → Enriched Findings → Report Agent → Final Report
```

### Pattern 3: Reinforcement Learning Optimization
Agents learn optimal collaboration through RL rewards

```
State: Patient data + Agent outputs
Action: Next agent task assignment
Reward: Diagnostic accuracy + Report quality
```

## Key Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **Diagnostic Accuracy** | F1 score on diagnosis | >0.90 |
| **Report Coherence** | BLEU/ROUGE for report quality | High human similarity |
| **Agent Consensus** | Agreement rate between agents | >0.85 |
| **Efficiency** | Time to complete analysis | <5 minutes |

## Design Workflow

1. **Define Agent Roles** - Identify specialized tasks for each agent
2. **Select Coordination Protocol** - Consensus, pipeline, or RL-based
3. **Implement Communication** - Define agent message passing
4. **Validate Performance** - Benchmark on medical datasets
5. **Iterate** - Optimize agent collaboration weights

## Clinical Safety

- **Uncertainty Quantification**: Each agent reports confidence scores
- **Human Override**: Allow clinician to intervene at any stage
- **Audit Trail**: Log all agent decisions for review
- **Bias Detection**: Monitor for demographic biases in agent outputs

## Example Use Case

**Radiology Report Generation:**
- Imaging Agent detects abnormalities in chest X-ray
- Context Agent retrieves patient history and relevant guidelines
- Report Agent synthesizes findings into structured report
- QA Agent checks for consistency and completeness
- Coordinator ensures all agents contribute appropriately

## Related Skills

- **quantum-medical-imaging** - Quantum-enhanced imaging analysis
- **agent-collaboration-protocol** - General agent collaboration patterns
- **arxiv-search** - Find multi-agent medical AI papers

## References

- arXiv:2509.17353 - Medical AI Consensus: Multi-Agent Framework for Radiology
- Multi-agent reinforcement learning in clinical settings
- LLM-based radiology report generation systems

## Notes

- Multi-agent systems improve reliability through redundancy
- Clinical validation is essential before deployment
- Balance agent specialization vs coordination overhead
- Consider regulatory requirements for medical AI