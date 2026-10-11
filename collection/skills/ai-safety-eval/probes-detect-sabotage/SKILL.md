---
name: probes-detect-sabotage
description: "White-box deception detection via probes scaled to frontier monitoring settings. Novel probe architecture aggregating across layers and tokens for detecting sabotage and unverbalized deception in LLM agents."
tags: [deception-detection, probes, monitoring, sabotage, ai-safety, white-box, frontier-models]
source: "arXiv:2610.12445"
utility_score: 0.95
---

# Caught in the Act: Probes Detect Sabotage and Unverbalized Deception

## Paper Metadata

- **arXiv ID**: 2610.12445
- **Title**: Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception
- **Authors**: Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba, Adam Gleave, Chris Cundy
- **Published**: 2026-10-08
- **Categories**: cs.LG, cs.AI
- **Link**: https://arxiv.org/abs/2610.12445

## Abstract Summary

Recent incidents have highlighted the challenge of monitoring LLM agents and the danger of models deceiving people. This work shows that white-box deception detection via probes can be scaled up to frontier monitoring settings by collecting the largest deception dataset to date for training probes and introducing a novel probe architecture which can aggregate information across many layers and tokens. The probes achieve 98.8% AUC in SHADE-Arena, surpassing an Opus 5.5 text-monitoring baseline, and show improved efficacy as the underlying model is scaled up. In cases of introspective deception (where ground truth cannot be determined from context alone), probes can distinguish transcripts containing a model's true hidden goal from other goals with an AUC of up to 99.7%.

## Key Contributions

1. **Largest deception dataset** to date for training probes (FIBS dataset released)
2. **Novel probe architecture** that aggregates information across many layers and tokens
3. **Frontier-scale validation**: 98.8% AUC in SHADE-Arena, surpassing text-monitoring baselines
4. **Introspective deception detection**: Up to 99.7% AUC in distinguishing true hidden goals
5. **Open-weight model testing**: Probes readily detect deception in models that lie about politically sensitive topics

## Research Implications

- **Deployment Safety**: Enables white-box monitoring for high-stakes agent deployments
- **Early Detection**: Can detect agent sabotage before it manifests in outputs
- **Layered Security**: Supports building safety systems combining output and internal-state monitoring
- **Scalability**: Probe efficacy improves with model scale, suggesting viability for frontier models
- **Community Resource**: Released FIBS dataset enables further research on deception detection

## Practical Applications

- Deploy white-box monitoring systems for production LLM agents
- Build layered safety architectures combining behavioral and internal-state monitoring
- Develop red-teaming protocols that test for unverbalized deception
- Create monitoring dashboards that track probe confidence scores in real-time

## Related Work

- Probes for internal state analysis
- Mechanistic interpretability
- AI safety and alignment
- Agent monitoring and oversight
