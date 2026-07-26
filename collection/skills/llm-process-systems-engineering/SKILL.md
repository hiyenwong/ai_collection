---
name: llm-process-systems-engineering
description: Large Language Models in Process Systems Engineering (PSE) - systematic survey of LLM applications across seven categories with capability assessment
trigger_words:
  - process systems engineering
  - PSE
  - LLM applications
  - chemical engineering
  - process design
  - molecular synthesis
  - process modeling
  - fault diagnosis
  - industrial AI
version: 1.0
paper_id: arxiv:2606.11589
authors: Bhushan Gopaluni, Vidya Kotamraju, Syon Bhushan
published: 2026-06-10
---

# Large Language Models in Process Systems Engineering

## Overview

Systematic survey of LLM applications in Process Systems Engineering (PSE), organizing literature into seven application categories with critical assessment of demonstrated capabilities versus aspirational claims.

## Seven Application Categories

### 1. Process Design and Engineering
- **Capabilities**: Natural language querying of documentation, design specification synthesis
- **Methods**: RAG systems, domain-specific fine-tuning
- **Challenges**: Physical constraint satisfaction, safety-critical requirements

### 2. Molecular Design and Synthesis
- **Capabilities**: Molecular property prediction, synthesis route suggestion
- **Methods**: Multi-modal models (structure + text), retrieval augmented generation
- **Challenges**: Chemical feasibility validation, reaction pathway optimization

### 3. Process Modeling and Simulation
- **Capabilities**: Equation discovery from data, model formulation assistance
- **Methods**: Symbolic regression, code generation for simulators
- **Challenges**: Physical consistency, numerical stability

### 4. Time-Series Forecasting
- **Capabilities**: Pattern recognition in operational data, anomaly precursor detection
- **Methods**: Foundation models for industrial time series, contextual reasoning
- **Challenges**: Real-time latency, prediction horizon limits

### 5. Optimization and Scheduling
- **Capabilities**: Problem formulation, constraint specification, heuristic suggestion
- **Methods**: LLM-guided optimization, scheduling constraint generation
- **Challenges**: Exact solution guarantee, computational efficiency

### 6. Process Control
- **Capabilities**: Control logic interpretation, tuning parameter suggestion
- **Methods**: Natural language control specification, PID tuning guidance
- **Challenges**: Formal stability guarantees, real-time execution

### 7. Fault Detection and Diagnosis
- **Capabilities**: Fault pattern recognition, diagnostic reasoning from logs
- **Methods**: Anomaly explanation, multi-modal sensor data interpretation
- **Challenges**: Novel fault detection, causal attribution

## Capability Assessment Framework

### Genuine Promise Areas
- Natural language documentation queries
- Unstructured knowledge synthesis
- Flexible human-machine interaction
- Design specification translation
- Fault scenario explanation

### Challenging Areas
- Real-time execution requirements
- Hard constraint satisfaction
- Formal safety guarantees
- Physical feasibility validation
- Numerical optimization exactness

## Methodological Patterns

### 1. RAG for Domain Knowledge
```python
# Conceptual PSE RAG architecture
class PSEKnowledgeRAG:
    def __init__(self, process_docs, equipment_specs):
        self.knowledge_base = VectorStore(process_docs)
        self.equipment_db = EquipmentDatabase(equipment_specs)
        
    def query_design_constraints(self, specification):
        retrieved_docs = self.knowledge_base.retrieve(specification)
        constraints = self.extract_constraints(retrieved_docs)
        return validated_constraints
```

### 2. Code Generation for Simulation
- Equation formulation from natural language
- Simulator code synthesis (Aspen, COMSOL, OpenModelica)
- Parameter initialization from specifications

### 3. Multi-Modal Molecular Design
- Structure-text alignment for property prediction
- Synthesis route retrieval + generation
- Feasibility scoring integration

### 4. Time-Series Foundation Models
- Pre-training on industrial operational data
- Contextual anomaly reasoning
- Multi-horizon forecasting with uncertainty

## Industrial Deployment Challenges

### Technical Barriers
- Latency constraints for real-time control
- Integration with legacy SCADA systems
- Model validation and verification
- Safety certification requirements

### Operational Barriers
- Data quality and standardization
- Domain expert trust calibration
- Maintenance and update cycles
- Regulatory compliance

## Open Problems

1. **Formal verification of LLM-generated control logic**
2. **Physical constraint embedding in generative models**
3. **Uncertainty quantification for safety-critical predictions**
4. **Domain adaptation for plant-specific variations**
5. **Multi-objective optimization with LLM guidance**

## Productive Research Directions

- Hybrid symbolic-neural approaches for constraint satisfaction
- Physics-informed LLM architectures for process modeling
- Foundation models pre-trained on PSE-specific corpora
- Interactive optimization interfaces with LLM reasoning
- Standardized benchmarks for PSE LLM evaluation

## Technical Requirements

- Domain-specific fine-tuning pipelines
- RAG infrastructure for technical documentation
- Multi-modal encoders for structure + text
- Integration frameworks for legacy systems

## References

- Paper: arXiv:2606.11589
- PSE application domains: chemical, pharmaceutical, energy
- Related surveys: AI in manufacturing, industrial foundation models