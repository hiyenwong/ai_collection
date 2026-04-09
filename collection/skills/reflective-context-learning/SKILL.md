# SKILL.md - Reflective Context Learning (RCL)

## Paper Reference
- **arXiv:** 2604.03189
- **Title:** Reflective Context Learning: Studying the Optimization Primitives of Context Space
- **Utility Score:** 0.87
- **Authors:** Shikib Mehri, Nikita Vassilyev et al.
- **Date:** April 2026 (Under review at COLM)

## Core Insights

### Key Problem
Learning challenges (credit assignment, overfitting, forgetting, local optima, high variance) persist in context space, but remain fragmented and ad hoc.

### Solution: Unified Framework
**Reflective Context Learning (RCL):**
1. **Reflection:** Converts trajectories + context → directional update signal (analogous to gradients)
2. **Mutation:** Applies signal to improve future behavior in context space

### Optimization Primitives
- **Batching:** Aggregate multiple experiences
- **Improved credit-assignment signal**
- **Auxiliary losses**
- **Failure replay**
- **Grouped rollouts** for variance reduction

### Benchmark Results
- AppWorld, BrowseComp+, RewardBench2
- Primitives improve over strong baselines
- Relative importance shifts across task regimes

## Practical Applications

### Agent Learning Pattern
```markdown
1. Execute task → collect trajectory
2. Reflect on behavior/failures
3. Generate context update signal
4. Apply mutation to context
5. Iterate with optimization primitives
```

### Design Choices
- Robustness to initialization
- Batch size effects
- Sampling/curriculum strategy
- Optimizer-state variants
- Model allocation (strong vs. weak for different components)

## Key Takeaways
- Context learning is an optimization problem
- Classical ML primitives transfer to context space
- Different primitives matter for different task types
- Stronger/weaker model allocation affects performance

## Open Resources
- GitHub: https://github.com/nvassilyev/RCL

## Related Work
- Context optimization approaches
- In-context learning
- Agent memory systems

## Further Reading
- Full paper: https://arxiv.org/abs/2604.03189
- PDF: https://arxiv.org/pdf/2604.03189
## Description
Framework from arXiv papers. See paper reference for details.
## Activation Keywords

- reflective-context-learning
- reflective-context-learning 技能
- reflective-context-learning skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply reflective-context-learning?

**Agent:** I'll help you understand and apply reflective-context-learning...

### Example 2: Advanced Application

**User:** What are the key considerations for reflective-context-learning?

**Agent:** Let me search for the latest research and best practices...
