# SWE-CI: CI-Based Code Maintenance Evaluation

**Source:** arXiv:2603.03823
**Utility:** 0.95
**Created:** 2026-03-25

## Activation Keywords

- SWE-CI
- code maintenance evaluation
- CI benchmark agents
- long-term code evolution
- repository-level benchmark
- agent maintainability evaluation

## Description

The first repository-level benchmark built on the Continuous Integration loop, evaluating LLM agents on dynamic, long-term code maintainability rather than static one-shot fixes.

## Core Methodology

### 1. Problem: Static vs Dynamic Evaluation

**Limitation of SWE-bench:**
- Static, one-shot bug fixes
- Short-term functional correctness
- Doesn't capture real-world development

**Real-world software development:**
- Complex requirement changes
- Long-term feature iterations
- Continuous Integration cycles

### 2. SWE-CI Benchmark

**Key Features:**
- 100 tasks from real repositories
- Average evolution: 233 days, 71 commits
- Dozens of rounds of analysis and coding
- CI-based evaluation loop

**Evaluation Paradigm Shift:**
- From: Static, short-term functional correctness
- To: Dynamic, long-term maintainability

### 3. Task Structure

Each task includes:
- Evolution history spanning months
- Consecutive commits to analyze
- Requirement changes over time
- Multiple iterations to resolve

### 4. Agent Capabilities Tested

- **Code understanding** - Analyze codebase evolution
- **Requirement interpretation** - Handle changing requirements
- **Iterative coding** - Multiple rounds of modifications
- **Quality maintenance** - Sustain code quality over time

## Implementation Framework

```python
# Conceptual SWE-CI evaluation framework
class SWECIBenchmark:
    """
    Benchmark for evaluating agent code maintenance capabilities
    """
    
    def __init__(self, repository, task):
        self.repo = repository
        self.task = task
        self.evolution_history = self.load_evolution_history()
    
    def load_evolution_history(self):
        """Load commit history and requirement changes"""
        return {
            'commits': [],  # List of commits
            'requirements': [],  # Changing requirements
            'tests': [],  # CI test results
        }
    
    def evaluate_agent(self, agent):
        """
        Evaluate agent on code maintenance task
        
        Returns:
            - Functional correctness
            - Code quality metrics
            - Maintainability score
        """
        results = {
            'rounds': 0,
            'success': False,
            'quality_metrics': {},
            'iterations': []
        }
        
        # Run agent through CI loop
        for round_num in range(self.task.max_rounds):
            # Agent analyzes and modifies code
            changes = agent.analyze_and_fix(
                self.repo,
                self.task.current_requirement
            )
            
            # Run CI tests
            test_results = self.run_ci_tests(changes)
            
            results['iterations'].append({
                'round': round_num,
                'changes': changes,
                'tests': test_results
            })
            
            if test_results['all_passed']:
                results['success'] = True
                break
        
        return results
    
    def run_ci_tests(self, changes):
        """Run CI pipeline on changes"""
        pass

class AgentEvaluator:
    """Evaluate agent maintainability over long-term evolution"""
    
    def __init__(self, benchmark):
        self.benchmark = benchmark
    
    def evaluate_maintainability(self, agent_results):
        """
        Assess code maintainability metrics
        
        Metrics:
        - Code quality trends
        - Technical debt accumulation
        - Test coverage stability
        - Refactoring effectiveness
        """
        pass
```

## Benchmark Statistics

| Metric | Value |
|--------|-------|
| Tasks | 100 |
| Avg evolution period | 233 days |
| Avg commits per task | 71 |
| Avg rounds needed | Dozens |

## Applications

### 1. Agent Development
- Test code maintenance capabilities
- Identify weaknesses in iterative coding
- Improve long-term code quality

### 2. CI/CD Research
- Understand code evolution patterns
- Develop better CI practices
- Automate maintenance tasks

### 3. Software Engineering
- Evaluate code generation tools
- Study maintainability metrics
- Design better development workflows

## Key Insights

SWE-CI reveals how well agents can:
1. **Understand evolving requirements** - Track changes over time
2. **Maintain code quality** - Sustain quality through iterations
3. **Handle complexity** - Manage long-term evolution
4. **Iterate effectively** - Improve through multiple rounds

## When to Use

- Evaluating LLM agents on code maintenance
- Benchmarking code generation tools
- Research on software evolution
- CI/CD automation development

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

**User:** How can I apply swe-ci-benchmark?

**Agent:** I'll help you understand and apply swe-ci-benchmark...

### Example 2: Advanced Application

**User:** What are the key considerations for swe-ci-benchmark?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `claude-code` - Claude Code agent
- `coding-agent` - Generic coding agents
- `self-verification` - Code verification

## References

- Chen, J., et al. "SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration." arXiv:2603.03823 (2026)
- SWE-bench benchmark
- Continuous Integration practices