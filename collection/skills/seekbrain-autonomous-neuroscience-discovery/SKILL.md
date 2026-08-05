---
name: seekbrain-autonomous-neuroscience-discovery
description: "SeekBrain autonomous multi-agent framework for accelerating neuroscience discovery through domain-grounded hierarchical planning and cross-modal data analysis. Dynamically constructs analysis recipes from code-paper pairs and generates hypotheses and analytical pipelines on demand for integrating multi-scale, multimodal neuroscience datasets."
metadata:
  arxiv_id: "2607.29347"
  published: "2026-07-31"
  authors: "Jiamin Wu, Peishan Xiang, Jingyang Chen, Yuqing Zhu, Yuxi Li, Ling Luo, Qihao Zheng, Jialiang Zu, Yongchao Wu, Mindong Liu, Haitao Wu, Chaofan Hu, Yijie Sun, Yuqi Hang, Yu Zhu, Shuo Li, Yue Fan, Shiyang Feng, Wanghan Xu, Tianlei Zhang, Jie Zhang, Wenlong Zhang, Bo Zhang, Kai Wang, Lei Bai, Mianxin Liu, Wanli Ouyang, Jiulin Du, Chunfeng Song"
  tags: [autonomous-agents, neuroscience-discovery, multi-agent-systems, cross-modal-analysis, hypothesis-generation, brainarena-benchmark]
license: Complete terms in LICENSE.txt
---

# SeekBrain: Autonomous Multi-Agent System for Neuroscience Discovery

## Overview

SeekBrain is an autonomous multi-agent framework designed to accelerate neuroscience discovery by addressing the analytical challenges posed by highly heterogeneous, multi-scale, multimodal datasets and fragmented workflows. The framework combines domain-grounded hierarchical planning with cross-modal data analysis to scalably generate hypotheses and analytical pipelines on demand.

## Key Innovations

### 1. Analysis Recipe Construction
- **Code-Paper Pair Extraction**: Dynamically constructs a repertoire of analysis recipes by extracting patterns from code-paper pairs in neuroscience literature
- **Codified Expertise**: Transforms implicit methodological knowledge into explicit, executable analysis recipes
- **Scalable Repository**: Maintains a growing library of validated analytical approaches across neuroscience subdomains

### 2. Domain-Grounded Hierarchical Planning
- **Multi-Agent Architecture**: Employs specialized agents for different aspects of the discovery process (hypothesis generation, pipeline construction, execution, validation)
- **Hierarchical Decomposition**: Breaks complex discovery tasks into manageable subtasks with appropriate agent specialization
- **Cross-Modal Integration**: Seamlessly integrates behavioral, neural, anatomical, and other data modalities

### 3. On-Demand Pipeline Generation
- **Hypothesis Generation**: Automatically formulates testable hypotheses based on available data and existing knowledge
- **Pipeline Construction**: Assembles appropriate analytical methods from the recipe repository to test hypotheses
- **Execution and Validation**: Runs analyses and validates results against expected outcomes or benchmarks

## Performance Results

### BrainArena Benchmark Evaluation
- **Substantial Outperformance**: Significantly outperforms state-of-the-art agent baselines across various neuroscience analysis tasks
- **Expert-Annotated Benchmark**: Evaluated on BrainArena, a comprehensive benchmark curated by neuroscience experts
- **Task Diversity**: Demonstrates robust performance across diverse analytical challenges in modern neuroscience

### Real-World Research Applications
- **Larval Zebrafish Behavior**: Integrated behavioral, neural, and anatomical data to reveal structured, distributed neural representations
- **Mouse Decision-Making**: Discovered a shared axis of regional decoding strength across the brain in decision-making tasks
- **Practical Utility**: Established as a scalable and practical tool for accelerating data-driven discoveries

## Methodology Components

### Framework Architecture
1. **Knowledge Base**: Repository of analysis recipes extracted from code-paper pairs
2. **Planning Engine**: Hierarchical task decomposition and agent coordination system  
3. **Execution Engine**: Pipeline assembly and computational execution infrastructure
4. **Validation Module**: Result verification and quality assessment components
5. **Integration Layer**: Cross-modal data fusion and preprocessing capabilities

### Implementation Workflow
1. **Data Ingestion**: Load multi-scale, multimodal neuroscience datasets
2. **Task Specification**: Define research questions or discovery objectives
3. **Recipe Selection**: Identify relevant analysis recipes from knowledge base
4. **Pipeline Assembly**: Construct executable analytical pipeline
5. **Execution**: Run analyses on available computational resources
6. **Validation**: Assess results against benchmarks or expected patterns
7. **Knowledge Update**: Add successful pipelines to recipe repository

## Use Cases

Use SeekBrain when:
- Integrating heterogeneous neuroscience datasets (behavioral, neural, anatomical, molecular)
- Exploring large-scale, multi-modal datasets without predefined hypotheses
- Accelerating discovery cycles in systems neuroscience research
- Standardizing analytical approaches across research teams
- Reproducing and extending findings from published neuroscience studies
- Developing new analytical methods for emerging neuroscience data types

## Neuroscience Applications

### Systems Neuroscience
- **Cross-Species Integration**: Combine data from zebrafish, mice, primates, and humans
- **Multi-Modal Fusion**: Integrate electrophysiology, imaging, behavior, and anatomy
- **Network Analysis**: Discover functional and structural brain network properties

### Cognitive Neuroscience
- **Behavior-Brain Mapping**: Link complex behaviors to underlying neural mechanisms
- **Decision-Making Studies**: Analyze neural correlates of choice and preference
- **Learning and Memory**: Track neural plasticity during learning processes

### Computational Neuroscience
- **Model Validation**: Test computational models against empirical data
- **Algorithm Development**: Create new analytical methods for specific data challenges
- **Benchmark Creation**: Develop standardized evaluation frameworks

## Pitfalls and Considerations

### Data Quality and Preprocessing
- **Heterogeneous Formats**: Neuroscience data comes in diverse formats requiring careful preprocessing
- **Quality Control**: Automated pipelines must include robust quality assessment steps
- **Metadata Integration**: Proper metadata annotation is crucial for cross-modal integration

### Computational Resources
- **Scalability Requirements**: Large datasets require significant computational resources
- **Pipeline Optimization**: Efficient execution strategies needed for complex analytical workflows
- **Resource Management**: Dynamic allocation of computational resources based on task requirements

### Validation and Reproducibility
- **Ground Truth Availability**: Many neuroscience questions lack definitive ground truth answers
- **Statistical Rigor**: Automated analyses must maintain proper statistical standards
- **Reproducibility**: Pipelines should be version-controlled and documented for reproducibility

### Domain Expertise Integration
- **Expert Oversight**: Human expertise remains essential for interpreting results and guiding discovery
- **Knowledge Gaps**: Recipe repositories may lack coverage for emerging research areas
- **Bias Mitigation**: Careful attention needed to avoid perpetuating methodological biases

## References
- **Original Paper**: [arXiv:2607.29347](https://arxiv.org/abs/2607.29347)
- **BrainArena Benchmark**: Expert-annotated benchmark for evaluating neuroscience discovery systems
- **Related Work**: Multi-agent systems for scientific discovery, automated machine learning (AutoML), computational neuroscience frameworks

## Activation Keywords
- seekbrain
- autonomous neuroscience discovery
- multi-agent neuroscience
- cross-modal analysis neuroscience
- hypothesis generation neuroscience
- brainarena benchmark
- analysis recipe extraction
- domain-grounded planning
- neuroscience pipeline generation
- multi-scale neuroscience integration