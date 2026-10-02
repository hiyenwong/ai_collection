---
name: arxiv-2610-00972-veriharness-scaling-agentic-verification
description: "Research paper: VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks. Introduces agentic verification framework that transforms LLMs into verifiers with workspaces, evidence tools, and reusable verification skills. Achieves highest selection scores across five long-horizon benchmarks with $100K+ rollout dataset released."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Research, Arxiv, Verification, Long-Horizon-Tasks, Agentic-Systems, LLM-Agents, Benchmark]
    related_skills: [ai-safety-eval, multi-agent-rl]
---

# VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks

**arXiv ID:** 2610.00972  
**Categories:** cs.AI, cs.MA  
**Utility Score:** 0.80 → Promoted (High)  
**PDF:** https://arxiv.org/pdf/2610.00972

## Abstract

As LLM agents undertake increasingly complex, long-horizon tasks, verifying their outputs becomes increasingly challenging. We study how verification capability can be strengthened with a fixed base model, without access to reference answers or grading rubrics at test time. Repeated sampling yields multiple rollouts that can contain complementary correct claims, but we need a reliable verification mechanism to determine which claims to trust. We first find that disagreement often exposes correct alternatives, while consensus can conceal errors. These observations motivate VeriHarness, which turns the underlying LLM a generator uses into an agentic verifier by giving it a workspace, evidence tools, and reusable verification skills. A disagreement resolver checks competing claims against environmental evidence, while a consensus challenger tests shared claims and searches for omitted requirements. Their findings guide the selection and revision of the final artifact. Across five long-horizon workspace benchmarks and two frontier models, VeriHarness achieves the highest selection scores among the evaluated baselines. Evidence-backed revision further improves average performance, bringing gains over a single rollout to 6.2 points with Gemini 3.5 Flash and 6.4 points with Claude Opus 4.8. We further show that verification skills can self-improve from failure feedback, demonstrating VeriHarness as a novel and critical approach for scaling long-horizon agentic verification. We release the full pool of approximately 26,000 rollouts across all five benchmarks and both models, produced at a cost of over $100,000, to support future research on agentic verification.

## Key Contributions

1. **Agentic Verifier Architecture**: Transforms base LLMs into verifiers with workspaces, evidence tools, and reusable verification skills
2. **Disagreement-Consensus Insight**: Disagreement exposes correct alternatives; consensus can conceal errors
3. **Dual Verification Mechanisms**:
   - Disagreement resolver: checks competing claims against environmental evidence
   - Consensus challenger: tests shared claims and searches for omitted requirements
4. **Self-Improving Verification Skills**: Verification skills evolve from failure feedback
5. **Large-Scale Dataset**: Releases ~26,000 rollouts ($100K+ cost) for future research

## Technical Approach

### Core Insight
- **Repeated Sampling**: Multiple rollouts contain complementary correct claims
- **Verification Challenge**: Need reliable mechanism to determine which claims to trust
- **Key Observation**: Disagreement ≠ error; consensus ≠ correctness

### VeriHarness Architecture
1. **Workspace**: Verifier has access to execution environment
2. **Evidence Tools**: Can query external sources, run tests, inspect artifacts
3. **Verification Skills**: Reusable procedures for checking specific claim types
4. **Disagreement Resolver**: When rollouts conflict, checks each against evidence
5. **Consensus Challenger**: When rollouts agree, searches for omitted requirements
6. **Evidence-Backed Revision**: Findings guide selection and revision of final artifact

### Self-Improvement Loop
- Verification skills learn from failure feedback
- Skills become more effective over time
- No retraining of base model required

## Experimental Results

### Benchmarks
Five long-horizon workspace benchmarks:
- Software engineering tasks
- Data analysis workflows
- Multi-step reasoning problems
- Complex document processing
- Integrated tool-use scenarios

### Performance
- **Highest selection scores** among evaluated baselines
- **Gemini 3.5 Flash**: +6.2 points over single rollout
- **Claude Opus 4.8**: +6.4 points over single rollout
- **Evidence-backed revision**: Further improves average performance

### Models Tested
- Gemini 3.5 Flash
- Claude Opus 4.8

## Implications for Agent Systems

- **Long-Horizon Verification**: Critical for complex multi-step agent workflows
- **No Reference Answers**: Works without ground truth or grading rubrics
- **Scalable Verification**: Reusable skills reduce per-task verification cost
- **Trust Calibration**: Helps distinguish genuine consensus from shared errors
- **Self-Evolution**: Verification capabilities improve over time

## Dataset Release

- **Size**: ~26,000 rollouts
- **Coverage**: 5 benchmarks × 2 models
- **Cost**: $100,000+ to produce
- **Purpose**: Support future research on agentic verification
- **Availability**: Released with paper

## Related Work

- Self-consistency methods (majority voting)
- Verification in theorem proving
- Reward models for RLHF
- Multi-agent debate and consensus
- Tool-use verification

## Code & Resources

- Paper: https://arxiv.org/abs/2610.00972
- PDF: https://arxiv.org/pdf/2610.00972
- Dataset: ~26,000 rollouts (released with paper)
