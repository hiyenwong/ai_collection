---
name: llm-sysml-alignment
description: "LLM-assisted semantic alignment methodology for SysML v2 model integration in collaborative MBSE. Use when working with cross-organizational system model integration, SysML v2 semantic alignment, or LLM-based MBSE workflows. Keywords: SysML, MBSE, LLM, semantic alignment, model integration, SysML v2."
---

# LLM-SysML Alignment

LLM-assisted methodology for semantic alignment and integration of SysML v2 models in collaborative Model-Based Systems Engineering (MBSE).

## Problem Statement

Cross-organizational collaboration in MBSE faces challenges in achieving semantic alignment across independently developed system models. Different organizations use different naming conventions, model structures, and domain-specific terminology, making integration difficult.

## Solution Approach

Structured, prompt-driven approach leveraging:
- **SysML v2 constructs**: alias, import, metadata extensions
- **LLM capabilities**: semantic matching, syntax verification, traceability
- **Iterative process**: model extraction → semantic matching → verification

## Core Methodology

### Step 1: Model Extraction

Extract semantic information from SysML v2 models:

```python
# Key elements to extract:
- Element names and aliases
- Relationships and dependencies
- Domain-specific terminology
- Metadata and annotations
```

### Step 2: Semantic Matching

Use LLM for semantic alignment:

```markdown
Prompt structure:
1. Identify equivalent elements across models
2. Detect semantic similarities despite naming differences
3. Generate alignment mappings
4. Create traceability links
```

### Step 3: Verification and Integration

Verify alignment consistency:

```python
Verification checks:
- Syntax correctness (SysML v2 compliant)
- Semantic consistency (equivalent meanings)
- Traceability (alignment rationale documented)
- Completeness (all elements covered)
```

## SysML v2 Constructs Used

### Alias
```sysml
alias ModelA.Part as ModelB.Component;
```

### Import
```sysml
import ModelA::*;
import ModelB::*;
```

### Metadata Extensions
```sysml
metadata alignmentSource = "ModelA";
metadata alignmentConfidence = 0.95;
```

## Workflow Example

**Scenario**: Two companies developing subsystem models for a larger system.

```markdown
Model A (Company 1):
- EngineSubsystem
- FuelSystem
- PowerControl

Model B (Company 2):
- PropulsionModule
- FuelManagement
- EnergyRegulator

Alignment Process:
1. LLM identifies semantic equivalents
2. Creates alias mappings
3. Generates import statements
4. Adds metadata for traceability
```

## LLM Prompt Patterns

### Semantic Extraction Prompt
```markdown
Extract semantic information from SysML v2 model [MODEL]:
1. Identify core concepts and their domain
2. List element relationships
3. Document naming conventions used
4. Extract domain-specific terminology
```

### Alignment Matching Prompt
```markdown
Match elements between Model A and Model B:
1. Identify equivalent elements by semantics (not names)
2. Generate alias mappings
3. Document alignment rationale
4. Flag ambiguous matches for human review
```

### Verification Prompt
```markdown
Verify alignment correctness:
1. Check SysML v2 syntax compliance
2. Verify semantic equivalence
3. Ensure traceability completeness
4. Identify missing alignments
```

## Best Practices

1. **Iterative refinement**: LLM alignment may need multiple iterations
2. **Human verification**: Flag ambiguous matches for review
3. **Metadata traceability**: Always document alignment rationale
4. **Soft alignment**: Use aliases instead of renaming
5. **Domain context**: Provide domain-specific context to LLM

## Key Findings (from Research)

- LLMs effectively assist in semantic alignment across engineering models
- SysML v2 provides robust framework for model integration
- Structured prompts improve alignment accuracy
- Traceability essential for maintaining alignment over time
- Soft alignment (aliases) preferred over hard renaming

## Applications

- Cross-company system integration
- Legacy model modernization
- Domain-specific model translation
- Multi-team collaborative MBSE
- System of systems integration

## Related Skills

- **arxiv-search**: Search for latest MBSE papers
- **kg-research-workflow**: Import papers to knowledge graph
- **skill-creator**: Create new skills from research

## Source Paper

**LLM-Assisted Semantic Alignment and Integration in Collaborative Model-Based Systems Engineering**
- arxiv ID: 2508.16181
- Authors: Li, Zirui et al.
- Published: 2026

## Notes

- Requires SysML v2 knowledge
- LLM prompts should be domain-specific
- Alignment confidence varies by domain complexity
- Human review essential for safety-critical systems