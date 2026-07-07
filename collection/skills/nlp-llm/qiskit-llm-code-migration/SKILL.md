---
name: qiskit-llm-code-migration
description: "LLM+RAG methodology for automated Qiskit code migration across versions. Uses taxonomy-based RAG to reduce hallucinations and improve code reliability in Quantum Software Engineering (QSE). Activation: qiskit migration, quantum code migration, QDK version upgrade, quantum API refactoring, quantum software engineering, quantum development kit, quantum code maintenance, LLM quantum code, RAG quantum migration, Qiskit version, quantum technical debt"
metadata:
  arxiv_id: "2606.20173"
  published: "2026-06-18"
  authors: "Jose Manuel Suarez, Luis Mariano Bibbo, Joaquin Bogado, Alenandro Fernandez"
  category: cs.SE
  tags: [quantum, software-engineering, LLM, RAG, code-migration, qiskit]
---

# Qiskit Code Migration with LLMs

## Problem

Quantum Development Kits (QDKs) evolve rapidly, introducing technical debt that compromises code maintainability and hinders software reuse. In Quantum Software Engineering (QSE), this is intensified by:
- Scarcity of high-quality training data
- High volatility of emerging frameworks
- General-purpose LLMs producing unreliable/hallucinated results

## Methodology

### Hybrid LLM+RAG Architecture

1. **Automated Taxonomy Generation**: Create version-specific taxonomy of migration scenarios as structured knowledge source
2. **RAG with Retrieval Schemes**:
   - **Unconstrained**: Broad retrieval for exploratory migration analysis
   - **Restrictive**: Narrow retrieval for precise migration suggestions (recommended for production)
3. **LLM Evaluation**: Test multiple models (e.g., Gemini Flash-2.5, GPT-oss) under different retrieval schemes

### Key Findings

- Taxonomy-based RAG significantly reduces hallucinations
- Restrictive retrieval scheme outperforms unconstrained for complex refactoring
- Gemini Flash-2.5 shows superior performance in detecting complex refactoring scenarios
- The approach ensures long-term availability of quantum algorithms within rapidly shifting ecosystems

## Implementation Pattern

```
Migration Workflow:
1. Parse source Qiskit code → identify API calls
2. Query taxonomy with current version + target version
3. Retrieve version-specific migration rules via RAG
4. LLM generates migration suggestions guided by retrieved context
5. Validate suggestions against target API documentation
6. Apply migrations and run test suite
```

## Pitfalls

- **General-purpose LLM hallucination**: Without RAG grounding, LLMs fabricate API calls that don't exist in target version
- **Taxonomy completeness**: Migration taxonomy must be automatically generated and kept current with each QDK release
- **Complex refactoring detection**: Simple regex-based migration misses multi-step API changes; LLM+RAG is essential for complex cases

## When to Use

- Migrating Qiskit code between major versions (e.g., 0.x → 1.x)
- Updating quantum code to new QDK APIs
- Maintaining quantum codebases across framework updates
- Building quantum code analysis tools

## Core Contribution

First systematic methodology applying taxonomy-based RAG to quantum software engineering, demonstrating that data-centric approaches can mitigate API obsolescence and flatten the learning curve in QSE.
