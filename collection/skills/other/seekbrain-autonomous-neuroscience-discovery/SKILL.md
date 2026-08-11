---
name: seekbrain-autonomous-neuroscience-discovery
description: SeekBrain autonomous multi-agent framework for accelerating neuroscience discovery using domain-grounded hierarchical planning and cross-modal data analysis. Use when building AI systems for neuroscience research automation.
trigger_words:
  - seekbrain
  - autonomous neuroscience
  - multi-agent neuroscience
  - brainarena benchmark
---

# SeekBrain: Autonomous Multi-Agent Framework for Neuroscience Discovery

## Overview
SeekBrain is an autonomous multi-agent framework designed to accelerate neuroscience discovery through domain-grounded hierarchical planning and cross-modal data analysis. It addresses the analytical challenges posed by highly heterogeneous neuroscience data and fragmented workflows by dynamically constructing analysis recipes from code-paper pairs and coupling this codified expertise with agentic planning and execution engines.

## Key Components

### 1. Domain-Grounded Hierarchical Planning
- Extracts analysis recipes from code-paper pairs in neuroscience literature
- Constructs hierarchical task decomposition based on domain knowledge
- Dynamically adapts planning based on data characteristics and research goals

### 2. Cross-Modal Data Analysis
- Integrates behavioral, neural, and anatomical data modalities
- Handles multi-scale, multimodal neuroscience datasets
- Generates hypotheses and analytical pipelines on demand

### 3. BrainArena Benchmark
- Expert-annotated benchmark for evaluating neuroscience discovery agents
- Demonstrates substantial outperformance over state-of-the-art agent baselines
- Validates real-world research deployment capabilities

## Implementation Guidelines

### Setting up SeekBrain Framework
```python
# Core components structure
class SeekBrainFramework:
    def __init__(self):
        self.recipe_extractor = CodePaperRecipeExtractor()
        self.hierarchical_planner = DomainGroundedPlanner()
        self.execution_engine = MultiModalExecutionEngine()
        self.evaluation_module = BrainArenaEvaluator()
    
    def analyze_dataset(self, dataset_path, research_question):
        # Extract relevant recipes from literature
        recipes = self.recipe_extractor.extract_relevant_recipes(research_question)
        
        # Generate hierarchical plan
        plan = self.hierarchical_planner.create_plan(recipes, dataset_path)
        
        # Execute analysis pipeline
        results = self.execution_engine.execute_plan(plan)
        
        return results
```

### Recipe Extraction from Code-Paper Pairs
1. Parse neuroscience papers and associated code repositories
2. Identify methodological patterns and analysis workflows
3. Codify expertise into reusable analysis recipes
4. Store recipes in structured format for retrieval

### Hierarchical Planning Process
1. Decompose research question into subtasks
2. Match subtasks to available analysis recipes
3. Construct execution graph with dependencies
4. Validate plan feasibility against dataset constraints

## Real-World Applications

### Zebrafish Behavior Analysis
- Integrated behavioral, neural, and anatomical data
- Revealed structured, distributed neural representations of larval zebrafish behavior
- Discovered shared axis of regional decorrelation in neural activity

### Hypothesis Generation
- Automatically generates testable hypotheses from multi-modal data
- Suggests novel analytical approaches based on literature patterns
- Accelerates discovery cycle from data to insight

## Evaluation Metrics

### BrainArena Benchmark Tasks
- Dataset characterization and metadata extraction
- Cross-modal alignment and integration
- Hypothesis generation and validation
- Pipeline reproducibility and documentation

### Performance Indicators
- Task completion accuracy
- Hypothesis quality (expert evaluation)
- Computational efficiency
- Reproducibility score

## Best Practices

### Data Preparation
- Ensure proper metadata annotation in standard formats (NWB, HDF5)
- Include cross-modal alignment information where available
- Document experimental protocols and preprocessing steps

### Recipe Curation
- Regularly update recipe database with new literature
- Validate recipes against ground truth datasets
- Maintain version control for reproducibility

### Deployment Considerations
- Start with well-defined, narrow research questions
- Gradually expand to more complex multi-modal analyses
- Maintain human-in-the-loop for hypothesis validation

## References
- **Paper**: SeekBrain: An Autonomous Multi-Agent System for Accelerating Neuroscience Discovery (arXiv:2607.29347v1)
- **Authors**: Jiamin Wu, Peishan Xiang, Jingyang Chen, et al.
- **Affiliations**: Shanghai Artificial Intelligence Laboratory, Chinese Academy of Sciences, The Chinese University of Hong Kong
- **Benchmark**: BrainArena - expert-annotated evaluation framework for neuroscience discovery agents

## Activation Keywords
- seekbrain
- autonomous neuroscience discovery
- multi-agent neuroscience framework
- brainarena benchmark
- cross-modal neural analysis
- hierarchical planning neuroscience
- code-paper recipe extraction
- zebrafish behavior analysis