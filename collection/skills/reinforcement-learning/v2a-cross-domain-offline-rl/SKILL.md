---
name: v2a-cross-domain-offline-rl
description: V2A methodology — unifying Value Alignment, Assignment, and dynamics alignment for cross-domain offline RL with heterogeneous datasets from multiple source domains collected by diverse behavior policies.
---

# V2A: Value Alignment + Assignment for Cross-Domain Offline RL

**Paper**: Unifying Value Alignment and Assignment in Cross-Domain Offline Reinforcement Learning with Heterogeneous Datasets
**arXiv**: 2605.24862
**Authors**: Zhongjian Qiao, Jiafei Lyu, Chenjia Bai, Peisong Wang, Siyang Gao, Shuang Qiu
**Submitted**: 24 May 2026 (Accepted at ICML 2026)

## Core Idea

Cross-domain offline RL aims to learn a policy in a target domain with limited target data + source data that exhibits a dynamics shift. When source datasets come from **multiple source domains** collected by **diverse behavior policies**, a critical yet overlooked issue emerges: **value misassignment**. 

Value misassignment undermines value alignment, misleads data filtering toward selecting suboptimal samples, and loosens the suboptimality gap, degrading agent performance.

The proposed **V2A** framework integrates dynamics alignment, value alignment, and value assignment to address this.

## Key Contributions

1. **Identifies value misassignment** in heterogeneous cross-domain offline RL — first work to study this multi-source, multi-behavior-policy setting.
2. **V2A framework** with three components:
   - Dynamics alignment via temporally-consistent modality representation learning
   - Value alignment via modality-aware advantage learning
   - Value assignment via selective data filtering
3. **Empirical results**: Significantly outperforms strong baselines under general heterogeneous cross-domain offline RL settings.

## Method Details

### V2A Framework

1. **Dynamics Alignment**
   - Extract dynamics modalities from source datasets using temporally-consistent modality representation learning
   - Learn representations that capture the underlying dynamics of each source domain

2. **Value Alignment**
   - Modality-aware advantage learning to rectify value alignment across domains
   - Ensures value estimates are comparable across different source domains

3. **Value Assignment**
   - Data filtering paradigm to selectively share source data for policy learning
   - Filters out samples that would cause value misassignment

### Key Insight

Value misassignment arises when:
- Source datasets have different dynamics (multiple domains)
- Source datasets are collected by different behavior policies
- Standard value alignment methods fail to account for these differences

V2A addresses this by:
1. First identifying the dynamics modality of each source sample
2. Then learning modality-aware value estimates
3. Finally filtering data based on both dynamics alignment AND value alignment

## Implementation Considerations

- Use a dynamics encoder to extract temporal-consistent representations
- Modality-aware heads for advantage estimation per dynamics cluster
- Data filtering threshold based on combined dynamics + value alignment score
- Target domain policy initialized from filtered source data

## Activation Keywords

- cross-domain offline RL, heterogeneous offline RL, value misassignment, value alignment, dynamics alignment, V2A, multiple source domains, offline RL transfer, dynamics shift, modality-aware RL, offline policy transfer

## Related Work

- **Dynamics alignment**: Matching source/target dynamics via representation learning
- **Value alignment**: Ensuring value estimates are consistent across domains
- **Offline RL transfer**: Using source data to bootstrap target policy
