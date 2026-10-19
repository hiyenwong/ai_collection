---
name: annotrace-a-workbench-for-step-level-annotation-of-agent-traces
description: 'Annotrace: A Workbench for Step-Level Annotation of Agent Traces (arXiv: 2610.23284v1). Utility: 0.85. Categories: cs.AI, cs.CL, cs.HC, cs.MA'
metadata:
  {
    "arxiv_id": "2610.23284v1",
    "utility": 0.85,
    "title": "Annotrace: A Workbench for Step-Level Annotation of Agent Traces",
    "authors": "Arun Josephraj Arokiaraj, Chenyi Huang, Sahan Bulathwela, Zekun Wu, Bin Wu",
    "url": "https://arxiv.org/abs/2610.23284v1",
    "categories": "cs.AI, cs.CL, cs.HC, cs.MA"
  }
---

# Annotrace: A Workbench for Step-Level Annotation of Agent Traces

**arXiv ID:** 2610.23284v1
**Authors:** Arun Josephraj Arokiaraj, Chenyi Huang, Sahan Bulathwela, Zekun Wu, Bin Wu
**URL:** https://arxiv.org/abs/2610.23284v1
**Utility Score:** 0.85
**Categories:** cs.AI, cs.CL, cs.HC, cs.MA

## Abstract

Every study of why LLM agents fail begins by labelling traces by hand, and every such study builds its own throwaway tool. Observability platforms record agent traces but offer no structured labelling; annotation tools label text but have no notion of a step, a delegation or a tool call, leaving it unclear what the smallest unit of execution to label should be. Annotrace reads six trace formats, including OpenTelemetry GenAI, LangSmith and Langfuse, and turns each run into an ordered, nested list of steps. The annotator writes their own labelling codebook; a frontier model proposes a starting set from a sample of their own traces, answers first, and is asked exactly the questions the human is asked, making annotation a joint human-AI process. Annotrace measures agreement between any two annotators, human or AI. On a multi-agent question-answering corpus it reproduces a previous manual effort's 235 annotation units exactly, and two models labelling the same traces agree 91% of the time at $κ= 0.82$.

## Key Concepts

- This paper addresses important questions in: cs.AI, cs.CL, cs.HC, cs.MA
- Published: 2026-10-16

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows and research tracking.

## References

- arXiv: https://arxiv.org/abs/2610.23284v1
