---
name: automated-domain-model-extraction-llm
description: "Extract domain models from code using LLMs and heuristics."
metadata:
  arxiv_id: "2608.12228"
  published: "2026-08-12"
  authors: "Alessandra Mancas, Mounir Ammam, Hyacinth Ali, Kevin Delcourt, Houari Sahraoui"
  conference: "MODELS 2026"
  tags: [systems-engineering, model-driven-engineering, reverse-engineering, llm, domain-modeling]
license: Complete terms in LICENSE.txt
---

# Automated Domain Model Extraction using LLMs and Heuristics

This skill implements the methodology from arXiv:2608.12228 for automated domain model extraction from source code using lightweight, locally deployable LLMs combined with structural and semantic heuristics.

## Core Methodology

The approach addresses the challenge of reverse engineering domain models in privacy-sensitive industrial environments where proprietary LLMs cannot be used due to confidentiality constraints. It overcomes the context window limitations of compact open-source LLMs by:

1. **Progressive Analysis**: Iteratively analyzing ranked subsets of code elements rather than processing the entire codebase at once
2. **Structural Heuristics**: Using code structure (classes, methods, inheritance, dependencies) to identify candidate domain concepts
3. **Semantic Heuristics**: Leveraging naming conventions, documentation, and code patterns to refine domain boundaries
4. **Iterative LLM Reasoning**: Using the LLM to reason about domain concepts within manageable context windows

## Workflow Steps

### Step 1: Code Element Ranking and Selection
- Parse the source code to extract all relevant code elements (classes, interfaces, methods, fields)
- Rank elements based on structural importance (e.g., number of dependencies, inheritance depth, usage frequency)
- Select the top-ranked subset that fits within the LLM's context window

### Step 2: Initial Domain Concept Identification
- Feed the selected code subset to the LLM with a prompt asking to identify potential domain concepts
- Extract candidate domain entities, relationships, and attributes from the LLM response
- Store identified concepts in a working domain model

### Step 3: Boundary Refinement
- Use the current domain model to guide selection of the next code subset
- Focus on code elements that are related to or could refine existing domain concepts
- Apply semantic heuristics to validate and refine domain boundaries

### Step 4: Iterative Expansion
- Repeat steps 2-3 until all relevant code has been processed or convergence is reached
- Merge and deduplicate domain concepts across iterations
- Validate the final domain model against the complete codebase

### Step 5: Output Generation
- Generate the final domain model in standard formats (UML, JSON Schema, etc.)
- Include confidence scores and evidence traces for each domain concept
- Provide recommendations for manual validation

## Implementation Guidelines

### LLM Selection
- Use locally deployable LLMs with strong code understanding capabilities
- Prefer models optimized for software engineering tasks (e.g., CodeLlama, StarCoder variants)
- Ensure the model can run within available hardware constraints

### Heuristic Configuration
- **Structural Heuristics**: Configure weights for different structural features (inheritance = 0.3, dependencies = 0.4, usage = 0.3)
- **Semantic Heuristics**: Define patterns for domain-relevant naming conventions and documentation keywords
- **Ranking Algorithm**: Use weighted scoring combining structural and semantic factors

### Context Management
- Calculate optimal context window size based on LLM capabilities and code complexity
- Implement sliding window mechanism for overlapping code segments
- Maintain state between iterations to track progress and avoid redundancy

## Pitfalls and Mitigations

### Context Window Limitations
**Problem**: Even with progressive analysis, complex codebases may require too many iterations
**Mitigation**: Implement hierarchical analysis - first extract package/module-level concepts, then drill down

### False Positives in Domain Concepts
**Problem**: LLM may identify non-domain concepts as domain entities
**Mitigation**: Apply post-processing filters based on semantic heuristics and validation rules

### Privacy Constraints
**Problem**: Some industrial environments have strict data handling requirements
**Mitigation**: Ensure all processing happens locally with no external API calls or data transmission

### Performance Optimization
**Problem**: Processing large codebases can be time-consuming
**Mitigation**: Implement parallel processing for independent code modules and caching for repeated analyses

## Validation Metrics

The approach achieves high F1-scores on curated datasets of projects with known domain models. Key metrics include:
- **Precision**: Proportion of extracted concepts that are valid domain concepts
- **Recall**: Proportion of actual domain concepts that were successfully extracted  
- **F1-Score**: Harmonic mean of precision and recall
- **Boundary Accuracy**: Accuracy of domain concept boundaries and relationships

## Activation Keywords
- automated domain model extraction
- reverse engineering domain models
- LLM-based domain modeling
- privacy-sensitive domain extraction
- model-driven engineering reverse
- systems engineering domain models

## References
- Original paper: https://arxiv.org/abs/2608.12228
- MODELS 2026 conference proceedings
- Model-Driven Engineering Languages and Systems