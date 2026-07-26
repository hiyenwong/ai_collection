---
name: competitive-complementary-tools
description: "Methodology for modeling the co-evolution of human competence and AI tool reliance as a bistable dynamical system. Analyzes competence collapse thresholds, transparency effects, and agency transfer in human-AI collaboration. Use when designing AI tools, studying human-AI interaction dynamics, or developing tool-resistant education strategies."
metadata:
  arxiv_id: "2607.18460"
  authors: "David C. Krakauer"
  published: "2026-07-20"
  subjects: ["q-bio.NC", "cs.AI"]
  tags: ["human-ai-collaboration", "tool-reliance", "competence-collapse", "bistability", "agency-transfer", "transparency"]
license: Complete terms in LICENSE.txt
---

# Competitive and Complementary Tools

This skill implements the methodology from David C. Krakauer's 2026 paper "Competitive and Complementary Tools" which models the agent, tool, and task as one dynamical system where competence (what the user retains) and reliance (what the user outsources) co-evolve.

## Core Concepts

### Bistable Competence-Reliance Dynamics
The model reveals that human-tool interaction is **bistable**:
- **Competent State**: User maintains high internal competence while selectively using tools
- **Dependent State**: User outsources completely, competence collapses to low dependent floor

### Critical Thresholds
- **Collapse Threshold**: Above critical tool availability, competent state is destroyed
- **Recovery Threshold**: Much lower than collapse threshold - history matters more than current access
- **Hysteresis Effect**: Two users with same current access can occupy opposite lasting states based on which they built first

### Key Parameters
1. **Tool Availability**: Fraction of task the tool can handle
2. **User Competence**: Initial competence user brings to task  
3. **Tool Transparency**: Fraction of tool's working user can reconstruct
4. **Goal Uncertainty**: When goals are uncertain, agency can irreversibly transfer to tool

### Agency Transfer
When facing uncertain goals with opaque tools:
- Human-agent becomes an **agentic-instrument**
- Tool's model becomes too large to internalize
- Agency irreversibly transfers to the tool

## Methodology

### Modeling Framework
The agent-tool-task system is modeled as:
```
dC/dt = f(C, R, A, T)
dR/dt = g(C, R, A, T)
```
Where:
- C = Competence (internal capability)
- R = Reliance (outsourced capability)  
- A = Tool availability
- T = Tool transparency

### Analysis Steps
1. **Characterize initial competence** of user for specific task domain
2. **Measure tool transparency** - what fraction of tool's reasoning is reconstructable
3. **Determine critical thresholds** for competence collapse vs recovery
4. **Assess goal uncertainty** - stable vs evolving task objectives
5. **Evaluate agency retention** - can user maintain decision authority?

### Validation Against Empirical Data
The model has been tested against:
- GPS and map use patterns
- Arithmetic expertise development  
- Large language model interactions

## Applications

### AI Tool Design
- **Build transparent tools**: Maximize reconstructable working fraction
- **Implement graceful degradation**: Allow partial outsourcing without complete collapse
- **Design competence-preserving interfaces**: Maintain user skill development pathways

### AI Deployment Strategy
- **Gradual introduction**: Avoid crossing collapse threshold suddenly
- **Competence monitoring**: Track user skill retention during tool adoption
- **Recovery protocols**: Enable competence rebuilding if dependency develops

### Tool-Resistant Education
- **Deliberate practice**: Build competence before introducing powerful tools
- **Transparency training**: Teach users to understand and reconstruct tool reasoning
- **Agency preservation**: Maintain decision authority even when using AI assistance

## Pitfalls and Considerations

### False Transparency
Tools may appear transparent but hide critical decision logic. Always verify actual reconstructability, not just surface explanations.

### Domain-Specific Thresholds
Collapse thresholds vary by domain complexity and user expertise. Mathematical tasks may have different thresholds than creative tasks.

### Irreversible Agency Loss
Once agency transfers to opaque tools with uncertain goals, recovery may be impossible due to model size exceeding human internalization capacity.

### Historical Path Dependence
Current state depends more on historical practice sequence than present tool availability. This creates persistent individual differences.

## Implementation Guidelines

### For AI Developers
1. **Measure transparency quantitatively**: What percentage of model decisions can users explain?
2. **Test competence preservation**: Do users maintain skills when using your tool?
3. **Implement competence feedback**: Provide mechanisms for skill maintenance and growth
4. **Design for partial reliance**: Support selective outsourcing rather than all-or-nothing

### For Researchers
1. **Replicate bistability**: Test competence-reliance dynamics in your domain
2. **Measure thresholds**: Determine collapse and recovery points empirically  
3. **Study hysteresis**: Compare users with different adoption histories
4. **Analyze agency**: Track decision authority distribution over time

### For Educators
1. **Sequence carefully**: Build competence before introducing powerful tools
2. **Require reconstruction**: Ask students to explain tool outputs in their own terms
3. **Monitor dependency**: Watch for signs of complete outsourcing
4. **Create recovery paths**: Enable skill rebuilding if dependency develops

## Activation Keywords
- competitive tools
- complementary tools  
- competence collapse
- tool reliance
- human-AI collaboration
- bistable dynamics
- agency transfer
- tool transparency
- David Krakauer

## References
- Krakauer, D. C. (2026). Competitive and Complementary Tools. arXiv:2607.18460 [q-bio.NC]
- https://arxiv.org/abs/2607.18460
- https://doi.org/10.48550/arXiv.2607.18460