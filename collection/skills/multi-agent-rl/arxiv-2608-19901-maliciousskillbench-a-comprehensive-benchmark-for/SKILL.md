---
name: arxiv-2608-19901-maliciousskillbench-a-comprehensive-benchmark-for
description: 'MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection (arXiv: 2608.19901)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection

**Authors:** Yue Wang, Yi Liu, Gelei Deng, Ying Zhang, Yuekang Li, Zhenyu Chen, Leo Zhang
**arXiv:** 2608.19901
**Utility:** 1.00
**Published:** 2026-08-20T11:13:00Z
**Link:** http://arxiv.org/abs/2608.19901

## Abstract

Agent Skills extend LLM agents with reusable instruction packages that may also include scripts, resources, and service configuration. This creates a direct distribution channel for malicious behavior, yet existing malicious-Skill datasets are fragmented across sources, artifact formats, evidence regimes, and benign coverage; duplicated and structurally related content further complicates direct aggregation and evaluation. We present MaliciousSkillBench, a comprehensive benchmark for malicious Agent Skill detection. We consolidate 13 public sources, 11 of which contribute Core malicious artifacts, and reduce 8,414 raw malicious records to 7,539 normalized-unique identities in 4,588 operational structural families. After conservative cross-label conflict exclusion, the primary benchmark contains 9,740 Skills: 7,505 malicious and 2,235 benign. To characterize its coverage, we harmonize 11 attack categories for 4,983 malicious identities with supported source-native mappings and find substantial differences in threat composition across sources. We then evaluate three learned text detectors and three off-the-shelf Skill scanners. Learned detectors achieve 0.882-0.932 Random Macro-F1 but only 0.653-0.665 under Source-Disjoint evaluation; the strongest word TF-IDF SVM scores 0.932/0.916/0.665 on Random/structural-disjoint/Source-Disjoint while retaining 95.6% malicious recall but producing 62.4% benign FPR on held-out sources. Off-the-shelf scanners occupy different but also unsatisfactory operating regimes, reducing false positives only at the cost of sharply lower malicious recall. Together, these results show that reliable malicious-Skill detection requires both broader cross-source benchmark coverage and evaluation that jointly measures attack detection and benign over-flagging.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection". 
The paper presents novel ideas in multi-agent-rl that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.19901
