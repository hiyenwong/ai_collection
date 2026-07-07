---
name: paving-way-agents-biology
description: Methodology from Anthropic research (Jun 2026) on making biological data infrastructure agent-friendly. Case study shows that adding deterministic retrieval layers (like gget virus) to scientific research agents improves accuracy from inconsistent results to nearly 100% for dataset construction tasks.
version: 1.0.0
author: Anthropic Research (Laura Luebbert)
date: 2026-06-08
source: https://www.anthropic.com/research/agents-in-biology
arxiv: https://arxiv.org/pdf/2606.06749
category: ai_collection
tags: [biology, agents, deterministic-retrieval, scientific-discovery, data-infrastructure]
activation_keywords: [biology agents, scientific data, deterministic retrieval, agent-friendly infrastructure, NCBI Virus, gget virus]
---

# Paving the Way for Agents in Biology

## Core Problem

AI agents navigating biological data infrastructure face a "click tax" problem similar to driving through an old city designed before cars:
- **Idiosyncratic file formats** scattered across heterogeneous databases
- **One-off retrieval scripts** requiring domain-specific knowledge
- **Implicit conventions** humans understand but agents struggle with
- **Brittle, process-dependent infrastructure** lacking structured digital workflows

## Key Insight

**Deterministic retrieval layers are crucial** for making scientific agent workflows reliable. Pure reasoning agents (Claude, GPT, Biomni OSS) did not consistently achieve accuracy required for reliable dataset construction. But accuracy rose to nearly 100% once a deterministic retrieval layer (gget virus) was added.

## Methodology: Deterministic Retrieval Layer Integration

### 1. Identify Infrastructure Bottlenecks
- Map existing human-click workflows for scientific tasks
- Identify points where agents fail due to implicit conventions
- Catalog metadata inconsistencies, format variations, naming conventions

### 2. Create Deterministic Execution Layers
- Build API wrappers for browser-based databases
- Standardize metadata fields across retrieval paths
- Implement explicit validation checks (genome builds, RefSeq/GenBank consistency)

### 3. Layer Architecture Pattern
```
Agent Intent Layer → Deterministic Retrieval Layer → Biological Database
      (reasoning)           (deterministic API)         (raw data)
```

### 4. Validation Protocol
For biological workflows, even small errors invalidate downstream interpretation:
- Genome build coordinate consistency
- RefSeq vs GenBank record separation
- Partial vs complete genome detection
- Segment name consistency for segmented viruses
- Metadata field standardization

## Case Study: NCBI Virus Retrieval

**Problem**: Virologists use NCBI Virus for surveillance and diagnostic assay development. Agents struggled to reliably retrieve sequence data.

**Solution**: Add `gget virus` as deterministic retrieval layer

**Result**: Accuracy jumped from inconsistent agent performance to nearly 100% for dataset construction

## Design Principles for Agent-Friendly Scientific Infrastructure

1. **API-first, browser-secondary**: Replace "go to URL, click dropdown" workflows with documented API endpoints
2. **Explicit metadata**: Make implicit conventions explicit in schema
3. **Version control for data**: Track genome builds, database versions
4. **Package manager integration**: Tools like Biopython, BioPerl, BioJulia, gget move data out of browsers
5. **Testable outputs**: Provide verification signals like software (passing tests = correct behavior)

## Broader Implications

- **Karpathy's "vibe coding" problem**: Same friction occurs in software when dashboards replace APIs
- **Scientific discovery bottleneck**: Not reasoning capability, but infrastructure accessibility
- **Scale requirement**: Biological databases must treat agents as scaled users

## Activation Triggers

Use when:
- Building scientific research agents for biology/chemistry domains
- Integrating agents with biological databases (NCBI, GenBank, RefSeq)
- Designing agent-friendly data infrastructure for scientific domains
- Creating deterministic wrappers for browser-based scientific tools

## Key References

- Original paper: https://arxiv.org/pdf/2606.06749
- gget package: https://github.com/pachterlab/gget
- NCBI Virus: https://www.ncbi.nlm.nih.gov/labs/virus
- Karpathy talk reference: Software in the era of AI

## Pitfalls

- **Assuming agents can infer conventions**: Biology has domain-specific implicit knowledge
- **Mixing database sources without validation**: RefSeq/GenBank mixing invalidates interpretations
- **Treating partial as complete genomes**: Critical for viral surveillance
- **Ignoring genome build versions**: Coordinate systems must match

## Implementation Notes

The deterministic layer pattern applies beyond biology to any domain where:
- Data lives in browser-based interfaces
- Human workflows depend on implicit knowledge
- Small errors invalidate downstream work
- Testable verification signals are absent