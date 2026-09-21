---
name: llm-apr-cps-limitations
description: "LLM integration limitations in CPS automated program repair."
---

## Use when

You need to integrate Large Language Models (LLMs) into search-based Automated Program Repair (APR) systems for Cyber-Physical Systems (CPS) modeled in Simulink/Stateflow, or when evaluating the effectiveness of LLM-based mutation operators in APR workflows.

## Core Methodology

### Problem Context
Search-based APR techniques traditionally rely on carefully designed mutation operators to explore the space of candidate fixes. Recent advances suggest LLMs could replace these operators by dynamically proposing repairs, but naive integration can substantially degrade performance.

### Key Findings from Controlled Evaluation
- **Performance degradation**: LLM-based mutation substantially degraded repair performance under the same experimental setup as traditional approaches
- **Reduced success rates**: LLM variants produced plausible patches for only 4-6 models and valid patches for 4 models, compared to 18 and 16 respectively with the original approach
- **Root causes identified**:
  1. LLMs struggle with precise symbolic edits required for CPS models
  2. Lack of behavioral feedback during patch generation
  3. Noisy search space that hinders effective exploration

### Recommended Hybrid Approach
Rather than replacing mutation operators entirely, combine structured mutation with generative guidance:
1. **Preserve core structured operators**: Keep domain-specific mutation operators that understand CPS semantics
2. **Use LLMs for augmentation**: Employ LLMs to suggest high-level repair strategies or generate diverse initial candidates
3. **Implement feedback loops**: Integrate behavioral validation feedback into the LLM prompting process
4. **Constrained generation**: Apply syntactic and semantic constraints to LLM outputs to reduce noise

### Experimental Setup Guidelines
- Use controlled comparison under identical wall-clock budgets
- Evaluate on real-world faulty Stateflow models across multiple CPS domains
- Measure both plausible patches (syntactically correct) and valid patches (behaviorally correct)
- Include the same benchmark suite as FlowRepair for reproducibility

## Implementation Steps

1. **Baseline establishment**: Implement or use existing FlowRepair-like APR system as baseline
2. **LLM integration points**: Identify specific mutation operators to replace or augment with LLMs
3. **Constraint definition**: Define syntactic and semantic constraints for LLM-generated patches
4. **Feedback mechanism**: Implement behavioral validation feedback loop
5. **Evaluation protocol**: Use identical experimental setup with controlled wall-clock budget
6. **Metrics collection**: Track plausible vs. valid patch generation rates

## Pitfalls to Avoid

- **Naive replacement**: Don't simply replace all mutation operators with LLM calls
- **Ignoring domain semantics**: CPS models have specific structural requirements that generic LLMs may not understand
- **Lack of validation**: Always validate LLM-generated patches behaviorally, not just syntactically
- **Unconstrained generation**: Without constraints, LLMs generate too much noise in the search space

## Verification Steps

1. Reproduce baseline FlowRepair results on the same benchmark
2. Implement LLM integration with proper constraints
3. Run controlled experiment with identical wall-clock budget
4. Compare plausible and valid patch generation rates
5. Analyze failure cases to identify improvement opportunities

## References

- Original paper: "Hype Meets Reality: Large Language Models as Mutators in Search-based Automated Program Repair of Simulink-Stateflow Models" (arXiv:2608.19347)
- FlowRepair methodology: State-of-the-art APR approach for Simulink/Stateflow models
- Benchmark: 19 real-world faulty Stateflow models across four CPS domains

## Activation Keywords

LLM APR, CPS repair, FlowRepair, Simulink Stateflow, automated program repair, cyber-physical systems, mutation operators, hybrid repair, LLM limitations