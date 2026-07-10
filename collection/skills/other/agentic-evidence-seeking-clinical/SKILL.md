---
name: agentic-evidence-seeking-clinical
category: deep-learning
description: ClinSeekAgent methodology for automated multimodal evidence seeking in clinical reasoning - shifting from passive evidence consumption to active evidence acquisition across heterogeneous medical data sources
trigger: ClinSeekAgent, clinical evidence seeking, agentic clinical reasoning, multimodal evidence, automated evidence acquisition, clinical agent, EHR navigation, medical tool invocation, evidence-seeking agent
---

# Agentic Evidence Seeking for Clinical Reasoning

Methodology for building clinical AI agents that actively seek, iteratively plan, and synthesize multimodal evidence from heterogeneous sources, rather than consuming pre-curated evidence.

## Core Problem

Existing clinical LLM systems assume evidence has already been curated and handed to the model. Real-world clinical workflows require agents to actively gather evidence from raw, heterogeneous sources.

## ClinSeekAgent Framework

### Three-Phase Evidence Seeking Cycle

**Phase 1: Evidence Gathering**
- Query medical knowledge bases (drug databases, guidelines, literature)
- Navigate raw EHRs (electronic health records) to extract relevant patient data
- Invoke medical imaging tools (CXR analysis, lab result interpretation)
- Access only raw data sources — no pre-curated evidence provided

**Phase 2: Hypothesis Refinement**
- Refine clinical hypotheses as new information emerges
- Dynamically adjust evidence-seeking strategy based on findings
- Iterative planning: decide what evidence to seek next

**Phase 3: Evidence Integration**
- Synthesize collected multimodal evidence
- Generate grounded clinical decisions
- Produce auditable reasoning traces

### Dual-Use Architecture

**Inference-Time Agent**
- Runs with frontier LLMs at inference time
- Dynamic evidence seeking for individual clinical queries
- +15.1 F1 improvement on multimodal tasks (Claude Opus 4.6: 47.5 → 62.6)

**Training-Time Pipeline**
- Distills high-quality agent trajectories into compact models
- ClinSeek-35B-A3B achieves +11.9 F1 over baseline on AgentEHR-Bench
- Approaches frontier LLM performance with 35B parameter model

## Implementation Pattern

```python
class ClinSeekAgent:
    def __init__(self, llm, data_sources):
        self.llm = llm
        self.data_sources = data_sources  # EHR, knowledge bases, imaging tools
        self.hypotheses = []
        self.evidence = []
    
    def seek_evidence(self, clinical_query):
        """Phase 1: Actively gather evidence from raw sources."""
        plan = self.llm.generate_evidence_plan(clinical_query)
        for source in plan.sources:
            evidence = self.data_sources[source].query(plan.queries[source])
            self.evidence.append(evidence)
    
    def refine_hypotheses(self):
        """Phase 2: Update hypotheses based on new evidence."""
        self.hypotheses = self.llm.update_hypotheses(
            self.hypotheses, self.evidence
        )
        # Decide if more evidence is needed
        if self.need_more_evidence():
            self.seek_evidence(next_queries)
    
    def integrate_and_decide(self):
        """Phase 3: Synthesize evidence into clinical decision."""
        return self.llm.clinical_decision(self.evidence, self.hypotheses)
```

## Benchmark: ClinSeek-Bench

- Pairs Curated Input reasoning with Automated Evidence-Seeking
- Evaluates both text-only EHR tasks and multimodal tasks
- Shows consistent improvement across 9 host models on risk prediction

## Performance

- Text-only: Claude Opus 4.6 from 60.0 → 63.2 F1; MiniMax M2.5 from 43.1 → 47.3
- Multimodal: Claude Opus 4.6 from 47.5 → 62.6 (+15.1)
- All evaluated models improve across CXR-related task groups
- Distilled model: +11.9 F1 over Qwen3.5-35B-A3B baseline

## When to Use

- Clinical decision support with raw, uncurated data sources
- Multimodal clinical reasoning (text + imaging + lab results)
- Building compact clinical models via trajectory distillation
- Any domain requiring active evidence acquisition from heterogeneous sources

## Activation

clinical evidence seeking, agentic clinical reasoning, multimodal evidence acquisition, ClinSeekAgent, EHR navigation agent, medical tool invocation, evidence-seeking pipeline, clinical trajectory distillation

## Reference

arXiv: 2605.20176v1 - "ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical Reasoning"
