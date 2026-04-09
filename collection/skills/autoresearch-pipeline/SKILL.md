# Autoresearch Pipeline for AI Safety Research

## Overview

**Source:** arXiv:2603.24511v1 (Claudini)
**Utility:** 0.95
**Topic:** LLM agent autonomous research for discovering new algorithms
**Key Contribution:** Autoresearch pipeline achieves SOTA results in adversarial attack discovery

## Activation Keywords

- autoresearch pipeline
- LLM agent autonomous research
- automated AI safety research
- iterative algorithm discovery
- Claude Code research automation

## Core Innovation

### Problem
- AI safety research often manual and slow
- Existing methods provide good starting points but optimization needed
- Dense quantitative feedback available but not leveraged

### Solution
**Autoresearch Pipeline:**
1. **Start from existing implementations** - Strong baseline (e.g., GCG)
2. **LLM agent iteration** - Claude Code explores modifications
3. **Quantitative evaluation** - Attack success rate (ASR) feedback
4. **Discover new algorithms** - SOTA results achieved

### Key Results

| Target Model | New Algorithm | Best Baseline | Improvement |
|--------------|---------------|---------------|-------------|
| GPT-OSS-Safeguard-20B | 40% ASR | ≤10% ASR | +30% |
| Meta-SecAlign-70B | 100% ASR | 56% ASR | +44% |

## Pipeline Architecture

```
Existing Methods → LLM Agent Exploration → Iterative Refinement → Evaluation → New Discovery
      ↓                    ↓                      ↓                ↓           ↓
   Baseline          Code Modification      Algorithm Changes    ASR Test    SOTA Results
```

### Implementation Framework

```python
class AutoresearchPipeline:
    def __init__(self, baseline_method, evaluation_fn, agent):
        self.baseline = baseline_method
        self.evaluate = evaluation_fn
        self.agent = agent  # Claude Code-like agent
    
    def run(self, n_iterations=100):
        current_algorithm = self.baseline
        
        for i in range(n_iterations):
            # Agent explores modifications
            modifications = self.agent.suggest_modifications(current_algorithm)
            
            # Try each modification
            for mod in modifications:
                new_algorithm = apply_modification(current_algorithm, mod)
                score = self.evaluate(new_algorithm)
                
                if score > best_score:
                    current_algorithm = new_algorithm
                    best_score = score
                    log_discovery(mod, score)
        
        return current_algorithm, best_score
```

## Key Principles

### 1. Strong Starting Points
- Existing methods provide foundation
- Don't start from scratch
- Leverage prior research

### 2. Dense Quantitative Feedback
- Clear optimization objective
- Measurable outcomes (ASR, accuracy, etc.)
- Direct feedback drives improvement

### 3. Agent Capabilities
- Code generation/modification
- Literature understanding
- Creative exploration

### 4. Iterative Refinement
- Many small modifications
- Gradual improvement accumulation
- Exploration vs exploitation balance

## Application Domains

| Domain | Starting Point | Objective | Suitability |
|--------|----------------|-----------|-------------|
| Adversarial Attacks | GCG, AutoPrompt | ASR maximization | ✅ Excellent |
| Prompt Optimization | Base prompts | Task performance | ✅ Good |
| Architecture Search | Known architectures | Accuracy | ✅ Good |
| Hyperparameter Tuning | Default configs | Validation score | ✅ Good |
| Algorithm Discovery | Existing algorithms | Benchmark scores | ✅ Excellent |

## Safety Considerations

⚠️ **Important**: This pipeline can be used for both defensive and offensive research.

### Defensive Applications
- Discover robust defense mechanisms
- Identify vulnerabilities before attackers
- Stress-test safety systems

### Offensive Applications
- Create new attack algorithms
- Jailbreak safety measures
- Prompt injection optimization

### Recommended Use
- **Prioritize defensive research**
- Use for authorized security testing only
- Follow ethical guidelines
- Report findings responsibly

## Relation to Self-Evolution

| Self-Evolution Concept | Autoresearch Pipeline |
|------------------------|----------------------|
| Learn → Apply → Reflect → Improve | Baseline → Modify → Evaluate → Discover |
| Delegation to Specialists | Agent handles code exploration |
| Dense Feedback | Quantitative ASR metrics |
| Ship or It Doesn't Count | Published SOTA algorithms |

## Implementation for OpenClaw

### Potential Applications

1. **Skill Optimization**
   - Start from existing skills
   - Agent modifies instructions
   - Evaluate on task performance

2. **Agent Improvement**
   - Optimize agent behaviors
   - Discover new workflows
   - Quantitative success metrics

3. **Workflow Discovery**
   - Find better processes
   - Optimize existing workflows
   - Task completion metrics

### Example: Skill Autoresearch

```python
class SkillAutoresearch:
    def optimize_skill(self, base_skill, evaluation_tasks):
        current_skill = base_skill
        
        for iteration in range(n_iterations):
            # Agent suggests skill modifications
            suggestions = self.agent.analyze_skill(current_skill)
            
            for suggestion in suggestions:
                modified_skill = apply_suggestion(current_skill, suggestion)
                
                # Evaluate on tasks
                performance = evaluate_skill(modified_skill, evaluation_tasks)
                
                if performance > best_performance:
                    current_skill = modified_skill
                    best_performance = performance
        
        return current_skill
```

## Best Practices

1. **Define Clear Objectives** - Measurable success metrics
2. **Set Constraints** - Safety boundaries, computational limits
3. **Document Discoveries** - Track all improvements
4. **Validate Transfers** - Test generalization to other contexts
5. **Report Responsibly** - Ethical disclosure for security findings

## Description
Framework from arXiv papers. See paper reference for details.
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

**User:** How can I apply autoresearch-pipeline?

**Agent:** I'll help you understand and apply autoresearch-pipeline...

### Example 2: Advanced Application

**User:** What are the key considerations for autoresearch-pipeline?

**Agent:** Let me search for the latest research and best practices...

## References

- Paper: https://arxiv.org/abs/2603.24511
- GitHub: https://github.com/romovpa/claudini
- Related: `self-evolving-agents-survey`

---

**Created:** 2026-03-28
**Source:** arXiv:2603.24511v1 - "Claudini: Autoresearch Discovers SOTA Adversarial Attack Algorithms"

⚠️ **Note**: Focus on research methodology, not attack details. Use for defensive research only.