---
name: arxiv-2610-01756-sok-decentralized-agent-economic-infrastructure
description: "Research paper: SoK: Decentralized Agent Economic Infrastructure. Systematizes security and economic requirements across the full lifecycle of agent tasks, introducing 'guarantee closure' criterion for end-to-end verification. Examines 12 systems, 5 mechanism families, and exposes recurring failures between verification and settlement in decentralized agent economies."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Research, Arxiv, Multi-Agent, Decentralized-Systems, Security, Economics, Verification, Blockchain]
    related_skills: [multi-agent-rl, security-privacy]
---

# SoK: Decentralized Agent Economic Infrastructure

**arXiv ID:** 2610.01756  
**Categories:** cs.CR, cs.AI, cs.MA  
**Utility Score:** 0.80 → Promoted (High)  
**PDF:** https://arxiv.org/pdf/2610.01756

## Abstract

Decentralized agent economies increasingly build a single task from protocols that were designed and secured separately. This creates a simple problem: a workflow can look correct at each step and still produce the wrong outcome. For example, a correct escrow may release payment on an authorized approval that provides little evidence that the delivered work actually satisfied the task. We systematize this problem across the full lifecycle of an agent task. Our study organizes security and economic requirements into 17 property families over six stages, with receipt soundness and completeness assessed separately. We examine 12 systems and standards, five reusable mechanism families, and four classical baselines. We introduce guarantee closure, a task-relative criterion for determining whether guarantees established at one stage remain available and constrain the later decisions that depend on them. We apply the criterion to controlled and native workflows, covering 840 matched executions and an exhaustive 11,648-case check over a finite objective-task domain. Our results expose recurring failures between verification and settlement, where conforming work can remain unaccepted or valid evidence can be ignored. Public records and model judgments further distinguish recorded approval from evidence of task conformance, while economic analysis identifies the report, penalty, and shared-error assumptions behind these guarantees. These findings show where end-to-end guarantees fail and what must be repaired to preserve them across the workflow.

## Key Contributions

1. **Lifecycle Systematization**: First comprehensive analysis of security/economic requirements across all 6 stages of agent task execution
2. **17 Property Families**: Organizes requirements into verifiable categories with receipt soundness and completeness
3. **Guarantee Closure Criterion**: Novel concept for tracking whether stage-level guarantees constrain later decisions
4. **Empirical Validation**: 840 matched executions + 11,648-case exhaustive check
5. **Failure Mode Catalog**: Identifies recurring gaps between verification and settlement phases

## Technical Framework

### Six-Stage Lifecycle
1. **Task Specification** → 2. **Agent Selection** → 3. **Execution** → 4. **Verification** → 5. **Settlement** → 6. **Dispute Resolution**

### Guarantee Closure
- **Definition**: Whether guarantees from stage N remain available and enforceable at stage N+k
- **Failure Modes**:
  - Verification succeeds but settlement ignores evidence
  - Conforming work remains unaccepted due to protocol gaps
  - Escrow releases on authorization without task conformance proof

### Mechanism Families Analyzed
- Escrow protocols
- Reputation systems
- Staking/slashing
- Oracle networks
- Zero-knowledge proofs

## Experimental Results

- **840 matched executions** across controlled workflows
- **11,648-case exhaustive check** over finite objective-task domain
- **Key Finding**: Public records ≠ evidence of task conformance
- **Economic Analysis**: Identifies report, penalty, and shared-error assumptions

## Implications for Agent Systems

- **Decentralized Economies**: Critical for understanding trust assumptions in agent marketplaces
- **Protocol Design**: Reveals where end-to-end guarantees break down
- **Verification Gaps**: Shows that step-wise correctness ≠ workflow correctness
- **Repair Strategies**: Identifies what must be fixed to preserve guarantees across stages

## Systems Examined

12 systems and standards including:
- Blockchain-based agent platforms
- Decentralized autonomous organizations (DAOs)
- Multi-agent marketplaces
- Smart contract frameworks
- Reputation systems

## Related Work

- Mechanism design for multi-agent systems
- Smart contract verification
- Decentralized trust mechanisms
- Agent economics and incentive compatibility

## Code & Resources

- Paper: https://arxiv.org/abs/2610.01756
- PDF: https://arxiv.org/pdf/2610.01756
