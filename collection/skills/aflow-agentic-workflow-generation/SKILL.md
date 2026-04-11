# AFlow: Automating Agentic Workflow Generation

## Description

AFlow automates the generation and optimization of agentic workflows using Monte Carlo Tree Search (MCTS). It reformulates workflow optimization as a search problem over code-represented workflows, enabling smaller models to outperform GPT-4o on specific tasks at 4.55% of its inference cost.

**Key Innovation:**
- Workflow optimization as code search
- MCTS-based exploration
- Iterative refinement via execution feedback
- 5.7% improvement over SOTA baselines

## Tools Used

- read: Load workflow definitions
- write: Generate workflow code
- exec: Execute workflows and collect feedback
- browser: Access external APIs
- memory_search: Retrieve workflow patterns

## Instructions for Agents

### Core Concept

Agentic workflows = LLM-invoking nodes connected by edges

AFlow automates:
1. Workflow generation
2. Workflow optimization
3. Cost-effective execution

### When to Use

- Complex multi-step tasks
- Cost optimization needed
- Workflow automation required
- Small models beating large models

## Overview

**Source:** arXiv:2410.10762v4 (ICLR 2025)
**Utility:** 0.94
**GitHub:** https://github.com/FoundationAgents/AFlow

## Activation Keywords

- aflow
- agentic workflow generation
- automated workflow optimization
- MCTS workflow
- workflow automation

---

## Architecture

### Workflow as Code

```python
# Workflow represented as code
class Workflow:
    def __init__(self):
        self.nodes = []  # LLM-invoking nodes
        self.edges = []  # Connections between nodes
    
    def add_node(self, node_type, prompt_template):
        node = Node(type=node_type, prompt=prompt_template)
        self.nodes.append(node)
        return node
    
    def add_edge(self, source, target, condition=None):
        edge = Edge(source, target, condition)
        self.edges.append(edge)
```

### MCTS Workflow Search

```python
class MCTSWorkflowSearch:
    def __init__(self, task, llm, budget=1000):
        self.task = task
        self.llm = llm
        self.budget = budget
        self.tree = SearchTree()
    
    def search(self):
        for _ in range(self.budget):
            # Selection
            node = self.select(self.tree.root)
            
            # Expansion
            child = self.expand(node)
            
            # Simulation
            reward = self.simulate(child)
            
            # Backpropagation
            self.backpropagate(child, reward)
        
        return self.best_workflow()
    
    def select(self, node):
        # UCB selection
        while node.children:
            node = max(node.children, key=lambda c: c.ucb_score())
        return node
    
    def expand(self, node):
        # Generate workflow modification
        modifications = self.generate_modifications(node.workflow)
        for mod in modifications:
            child = TreeNode(workflow=mod.apply(node.workflow))
            node.add_child(child)
        return node.children[0]
    
    def simulate(self, node):
        # Execute workflow and get reward
        result = node.workflow.execute(self.task)
        return self.evaluate(result)
```

---

## Workflow Optimization

### Code Modification

```python
class WorkflowModifier:
    def generate_modifications(self, workflow):
        modifications = []
        
        # Add node
        modifications.append(AddNodeMod(node_type='llm'))
        
        # Remove node
        if len(workflow.nodes) > 1:
            modifications.append(RemoveNodeMod(node_idx=random))
        
        # Modify prompt
        modifications.append(ModifyPromptMod(
            node_idx=random,
            new_prompt=self.llm.suggest_prompt()
        ))
        
        # Add edge
        modifications.append(AddEdgeMod(
            source=random,
            target=random
        ))
        
        return modifications
```

### Execution Feedback

```python
class ExecutionFeedback:
    def evaluate_workflow(self, workflow, task):
        # Run workflow on task
        result = workflow.run(task)
        
        # Calculate metrics
        metrics = {
            'accuracy': self.check_accuracy(result, task.ground_truth),
            'cost': self.calculate_cost(workflow),
            'latency': result.execution_time
        }
        
        return metrics
```

---

## Key Results

| Metric | Value |
|--------|-------|
| Average improvement | +5.7% over SOTA |
| Cost reduction | 4.55% of GPT-4o cost |
| Smaller model performance | Outperforms GPT-4o on specific tasks |

---

## Workflow Patterns

### Chain-of-Thought

```python
workflow = Workflow()
step1 = workflow.add_node('llm', "Think step by step about: {input}")
step2 = workflow.add_node('llm', "Based on {step1}, provide the answer")
workflow.add_edge(step1, step2)
```

### Self-Refine

```python
workflow = Workflow()
generate = workflow.add_node('llm', "Generate solution: {problem}")
critique = workflow.add_node('llm', "Critique: {generate}")
refine = workflow.add_node('llm', "Refine based on critique: {critique}")
workflow.add_edge(generate, critique)
workflow.add_edge(critique, refine)
```

### Ensemble

```python
workflow = Workflow()
solver1 = workflow.add_node('llm', "Solve: {problem}")
solver2 = workflow.add_node('llm', "Solve differently: {problem}")
aggregator = workflow.add_node('llm', "Combine solutions: {solver1}, {solver2}")
workflow.add_edge(solver1, aggregator)
workflow.add_edge(solver2, aggregator)
```

---

## Implementation

### Complete AFlow Pipeline

```python
class AFlow:
    def __init__(self, task_dataset, llm):
        self.dataset = task_dataset
        self.llm = llm
        self.mcts = MCTSWorkflowSearch(task_dataset, llm)
    
    def optimize(self, n_iterations=100):
        best_workflow = None
        best_score = 0
        
        for iteration in range(n_iterations):
            # Search for better workflow
            workflow = self.mcts.search(budget=100)
            
            # Evaluate on validation set
            score = self.evaluate(workflow, self.dataset.val)
            
            if score > best_score:
                best_score = score
                best_workflow = workflow
        
        return best_workflow
    
    def evaluate(self, workflow, dataset):
        correct = 0
        for task in dataset:
            result = workflow.run(task)
            if self.check_correctness(result, task.answer):
                correct += 1
        return correct / len(dataset)
```

---

## Cost Optimization

### Smaller Model Strategy

```python
class CostAwareWorkflow:
    def __init__(self, large_model, small_model):
        self.large = large_model
        self.small = small_model
    
    def run(self, task):
        # Try small model first
        result = self.small.run(task)
        confidence = self.estimate_confidence(result)
        
        if confidence > 0.9:
            return result
        
        # Fall back to large model
        return self.large.run(task)
```

---

## Benchmarks

| Benchmark | Task Type | Improvement |
|-----------|-----------|-------------|
| HumanEval | Code generation | +4.2% |
| MATH | Math reasoning | +6.8% |
| HotpotQA | Multi-hop QA | +5.1% |
| DROP | Discrete reasoning | +7.3% |

---

## Best Practices

1. **Start simple** - Begin with basic workflow patterns
2. **Iterate with feedback** - Use execution results to guide search
3. **Balance exploration** - Don't get stuck in local optima
4. **Consider cost** - Optimize for performance/cost trade-off
5. **Validate thoroughly** - Test on diverse task samples

---

## Applications

| Domain | Use Case |
|--------|----------|
| Code generation | Automated development workflows |
| Research | Literature review automation |
| Data analysis | Multi-step data processing |
| Content creation | Writing and editing pipelines |

---

## Examples

### Example 1: Basic Application

**User:** I need to apply AFlow: Automating Agentic Workflow Generation to my analysis.

**Agent:** I'll help you apply aflow-agentic-workflow-generation. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex multi-step tasks

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for aflow-agentic-workflow-generation?

**Agent:** Let me search for the latest research and best practices...

## References

- Paper: https://arxiv.org/abs/2410.10762
- GitHub: https://github.com/FoundationAgents/AFlow
- ICLR 2025

---

**Created:** 2026-03-28
**Source:** arXiv:2410.10762v4 - "AFlow: Automating Agentic Workflow Generation"