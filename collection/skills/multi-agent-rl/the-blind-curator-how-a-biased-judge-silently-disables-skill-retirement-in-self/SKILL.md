---
name: the-blind-curator-how-a-biased-judge-silently-disables-skill-retirement-in-self
description: 'A self-evolving agent retires its bad skills by watching them fail, so what happens when the judge cannot see the failures? Skill retirement is the structural constraint that keeps a growing library f. Based on arXiv:2607.07436.'
---

# The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents

**arXiv**: 2607.07436 | **Authors**: Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu et al. | **Utility**: 0.92

## Overview

A self-evolving agent retires its bad skills by watching them fail, so what happens when the judge cannot see the failures? Skill retirement is the structural constraint that keeps a growing library from drifting below the no-skill baseline, but its guarantee assumes an unbiased reward, which is false for the LLM judges that reference-free tasks force upon us. We show that a biased judge does not merely add noise; it \emph{silently switches off the curator}. We make this precise with a corrupted-reward analysis and, isolating the causal channel by injecting corruption on top of a deterministic reward, a behavioral study on a reference-free report-writing testbed with a code-generation cross-check. Symmetric noise leaves retirement intact, but \emph{false-pass} bias (failures slipping through as passes) disables contribution-based retirement past a sharp threshold that no amount of data can cross. Separating genuine retirement from cap-eviction churn shows this \emph{mechanism} failure is universal, holding across domains and failure rates and sparing only near-zero-false-pass, verifier-like graders. The downstream \emph{outcome}, though, is regime-dependent: eval quality degrades only where the same corruption also starves skill synthesis, and otherwise holds steady, so the disabled curator is \emph{silent}, surfacing in no aggregate metric. The contribution is a behavioral safety result, not a performance one. A cheap defect-injection audit then tells an operator, before deployment, which side of the threshold their judge occupies.

## Key Contributions

1. A self-evolving agent retires its bad skills by watching them fail, so what happens when the judge cannot see the failures? Skill retirement is the structural constraint that keeps a growing library from drifting below the no-skill baseline, but its guarantee assumes an unbiased reward, which is false for the LLM judges that reference-free tasks force upon us.
2. We show that a biased judge does not merely add noise; it \emph{silently switches off the curator}.
3. We make this precise with a corrupted-reward analysis and, isolating the causal channel by injecting corruption on top of a deterministic reward, a behavioral study on a reference-free report-writing testbed with a code-generation cross-check.
4. Symmetric noise leaves retirement intact, but \emph{false-pass} bias (failures slipping through as passes) disables contribution-based retirement past a sharp threshold that no amount of data can cross.

## Implementation Notes

- **Keywords**: llm, skill-library, self-evolving
- **Categories**: cs.AI, cs.CL, cs.CR
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: llm, skill-library, self-evolving.
