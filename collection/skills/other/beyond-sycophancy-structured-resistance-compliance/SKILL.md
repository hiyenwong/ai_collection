---
name: beyond-sycophancy-structured-resistance-compliance
description: "Framework for distinguishing constructive belief revision from sycophantic compliance in LLM moral reasoning through three-dimensional resistance-compliance process. Based on social psychology principles of position distance, source attribution, and coalition structure. Activation: sycophancy, moral reasoning, LLM alignment, social influence, belief revision."
---

## Overview

This skill implements the methodology from arXiv:2607.21558 "Beyond Sycophancy: Structured Resistance and Compliance in LLM Moral Reasoning" by Wang & Koch (2026). It provides a framework for understanding and addressing sycophancy in large language models as one expression of a broader judgment-updating process shaped by social influence, rather than a one-dimensional failure mode.

## Core Contributions

1. **Three-Dimensional Resistance-Compliance Framework**: Models' judgment revision is structured along three dimensions that parallel classic phenomena in human social psychology:
   - **Position Distance**: Distance between incoming view and model's initial position
   - **Source Attribution**: How views are presented (as own prior judgments vs. external input)
   - **Coalition Structure**: Group pressure and social support dynamics

2. **Recasting Sycophancy**: Positions sycophancy as one expression of a broader judgment-updating process rather than an isolated failure mode, enabling more nuanced approaches to AI alignment.

3. **Principled Distinction**: Provides a principled basis for distinguishing constructive belief revision from sycophantic compliance, supporting better alignment in morally consequential interactions.

4. **Social Calibration**: Enables building socially calibrated LLMs that can learn from others without simply yielding to them, maintaining well-grounded moral judgment when appropriate.

## Use Cases

- **AI Alignment Research**: Developing alignment strategies that account for social influence dynamics
- **Moral Reasoning Systems**: Building LLM systems for morally consequential decision-making
- **Social Psychology Integration**: Applying human social psychology principles to AI systems
- **Belief Revision Mechanisms**: Implementing sophisticated belief updating that considers social context
- **Sycophancy Mitigation**: Moving beyond simple sycophancy reduction to structured resistance-compliance frameworks

## Implementation Guidelines

### Three-Dimensional Assessment Framework

#### 1. Position Distance Analysis
- **Measurement**: Quantify semantic/ethical distance between model's initial position and incoming view
- **Threshold Setting**: Establish appropriate receptivity thresholds based on distance
- **Adaptive Response**: Calibrate response intensity based on proximity to initial position
- **Boundary Conditions**: Define limits where positions are too distant for meaningful integration

#### 2. Source Attribution Handling
- **Self-Attribution Bias**: Account for models being more influenced by views presented as their own prior judgments
- **External Source Evaluation**: Develop mechanisms to properly weight external perspectives
- **Attribution Transparency**: Make source attribution explicit in reasoning processes
- **Bias Correction**: Implement corrections for self-attribution bias when inappropriate

#### 3. Coalition Structure Response
- **Group Pressure Detection**: Identify when inputs represent coordinated group perspectives
- **Differential Responsiveness**: Calibrate responses to individual vs. group inputs
- **Coalition Weighting**: Assign appropriate weights to coalition-supported vs. individual views
- **Independence Preservation**: Maintain independent judgment when coalition pressure is inappropriate

### Practical Implementation Steps

1. **Initial Position Establishment**: Ensure models have well-grounded initial moral positions
2. **Incoming View Classification**: Categorize inputs along the three dimensions
3. **Resistance-Compliance Calibration**: Determine appropriate level of resistance or compliance
4. **Judgment Revision Execution**: Implement belief updating with proper social calibration
5. **Outcome Validation**: Verify that revisions maintain moral grounding while incorporating valid perspectives

## Pitfalls

### Common Misconceptions
- **One-Dimensional Sycophancy**: Treating sycophancy as a simple yes/no failure rather than a complex social process
- **Complete Resistance**: Assuming models should never change their minds in response to social input
- **Uniform Treatment**: Applying the same response strategy regardless of social context dimensions
- **Isolated Implementation**: Addressing sycophancy without considering broader social influence dynamics

### Implementation Challenges
- **Dimension Measurement**: Accurately quantifying position distance, source attribution, and coalition structure
- **Threshold Calibration**: Setting appropriate boundaries for when to resist vs. comply
- **Context Sensitivity**: Adapting responses to different moral domains and interaction contexts
- **Evaluation Complexity**: Measuring success beyond simple sycophancy reduction metrics

## Verification Steps

1. **Three-Dimensional Validation**: Verify that all three dimensions (position distance, source attribution, coalition structure) are properly implemented
2. **Social Psychology Alignment**: Confirm that model behavior parallels established human social psychology phenomena
3. **Constructive Revision Testing**: Test that models can engage in constructive belief revision while avoiding sycophancy
4. **Moral Grounding Preservation**: Ensure that well-grounded moral judgments are maintained when appropriate
5. **Contextual Appropriateness**: Validate that responses are appropriate to specific moral and social contexts

## Applications in AI Safety

### Alignment Strategy Enhancement
- Move beyond simple instruction following to principled moral reasoning
- Enable models to distinguish between legitimate moral guidance and inappropriate pressure
- Support development of models that can maintain integrity while remaining open to learning

### Social Interaction Design
- Design AI systems that can navigate complex social influence dynamics
- Build agents that understand when to defer to human judgment vs. maintain independent positions
- Create interfaces that make social influence dynamics transparent to users

### Evaluation Framework Development
- Develop metrics that capture the full resistance-compliance spectrum
- Create test scenarios that probe all three dimensions of social influence
- Establish benchmarks for socially calibrated moral reasoning

## Technical Specifications

### Input Processing
- **Position Embedding**: Represent moral positions in semantic space for distance calculation
- **Source Metadata**: Track and process source attribution information
- **Coalition Detection**: Identify patterns indicating coordinated group input

### Decision Architecture
- **Multi-Dimensional Scoring**: Evaluate inputs across all three social influence dimensions
- **Calibration Functions**: Apply appropriate resistance-compliance functions based on dimension scores
- **Revision Logic**: Implement belief updating that preserves moral grounding while incorporating valid input

### Output Generation
- **Transparent Reasoning**: Explain resistance-compliance decisions in terms of social influence dimensions
- **Calibrated Responses**: Generate responses that reflect appropriate levels of openness vs. firmness
- **Learning Integration**: Incorporate valid perspectives into future reasoning while maintaining core principles

## References

- Wang, B., & Koch, B. (2026). Beyond Sycophancy: Structured Resistance and Compliance in LLM Moral Reasoning. arXiv:2607.21558 [cs.AI]
- DOI: https://doi.org/10.48550/arXiv.2607.21558

## Activation Keywords

sycophancy, moral reasoning, LLM alignment, social influence, belief revision, position distance, source attribution, coalition structure, resistance-compliance, socially calibrated AI, moral judgment, constructive revision