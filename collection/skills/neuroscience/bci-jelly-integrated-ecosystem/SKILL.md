---
name: bci-jelly-integrated-ecosystem
description: "BCIJelly ecosystem for BCI research and deployment."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2608.13576"
  published: "2026-08-17"
  authors: "Liyuan Han, Xinrui Yang, Tianyu Zheng, Qizhi Yang, Yitao Qin, Liang Chen, Qinglai Wei, Binjie Hong, Xinhe Zhang, Rui Xiong, Yong Gu, Mu-ming Poo, Bo Xu, Chengyu Li, Tielin Zhang"
  tags: [bci, brain-computer-interface, neuroimaging, multimodal, decoder, neuromorphic]
---

# BCIJelly - Integrated Ecosystem for Brain-Computer Interface Research

## Overview

BCIJelly is a unified computational ecosystem that addresses the fragmentation in BCI research by integrating datasets, decoders, algorithmic modules, automated architecture search, and hardware-aware deployment within a single Python framework. Based on arXiv:2608.13576, it provides an end-to-end solution for BCI development from data to deployment.

## Core Components

### 1. Curated Datasets
- **18 curated BCI datasets** covering diverse paradigms
- **Multi-species support**: Human, macaque, and mouse recordings
- **Standardized formats**: Unified data loading interface
- **Paradigm coverage**: Motor, visual, speech, emotion, and auditory BCI tasks

### 2. Benchmark Decoders
- **15 benchmark decoders** implementing state-of-the-art algorithms
- **Modular design**: Plug-and-play decoder components
- **Performance validation**: Benchmarked across multiple datasets
- **Extensible architecture**: Easy integration of new decoder methods

### 3. Algorithmic Library
- **80 reusable modules** for BCI pipeline construction
- **Signal processing**: Filtering, feature extraction, artifact removal
- **Machine learning**: Classification, regression, deep learning components
- **Evaluation metrics**: Comprehensive performance assessment tools

### 4. Automated Architecture Search (AAS)
- **Task-specific decoder construction**: Automatically builds optimal architectures
- **LLM-guided closed-loop mode**: Uses large language models for search guidance
- **Multi-task support**: Simultaneous optimization for multiple objectives
- **Cross-species decoding**: Knowledge transfer across recording species

### 5. Hardware-Aware Deployment
- **toChip pipeline**: Compiles trained decoders for neuromorphic execution
- **Energy-efficient deployment**: Optimized for low-power BCI systems
- **Hardware abstraction**: Platform-independent compilation interface
- **Real-time execution**: Support for online BCI applications

### 6. Visualization Software
- **Graphical workflow interface**: No programming required for basic usage
- **Pipeline visualization**: Interactive display of BCI workflows
- **Results exploration**: Visual analysis of decoder performance
- **Parameter tuning**: Interactive hyperparameter optimization

## Usage Workflow

### Step 1: Dataset Selection and Loading
```python
from bcijelly import DatasetLoader
loader = DatasetLoader()
available_datasets = loader.list_datasets(paradigm="motor", species="human")
dataset = loader.load_dataset("motor_human_dataset_01")
```

### Step 2: Task Specification
Define your BCI task using natural language or structured format:
- **Single paradigm**: "Decode hand movement direction from motor cortex"
- **Multi-paradigm**: "Simultaneously decode visual category and emotional valence"
- **Cross-species**: "Transfer decoder from macaque to human motor imagery"

### Step 3: Automated Architecture Search
```python
from bcijelly import ArchitectureSearch
search = ArchitectureSearch(
    task_spec=task_description,
    dataset=dataset,
    search_space="comprehensive"  # or "lightweight" for resource-constrained scenarios
)
best_decoder = search.run(max_trials=100, validation_metric="accuracy")
```

### Step 4: Training and Validation
```python
from bcijelly import Trainer
trainer = Trainer(decoder=best_decoder)
results = trainer.train(
    train_data=dataset.train,
    val_data=dataset.val,
    epochs=100,
    early_stopping_patience=10
)
```

### Step 5: Hardware Deployment (Optional)
```python
from bcijelly import ChipCompiler
compiler = ChipCompiler(target_hardware="loihi2")  # or "spinnaker2", "dynap-se2"
compiled_model = compiler.compile(trained_model=results.model)
deployment_package = compiler.create_deployment_package(compiled_model)
```

### Step 6: Visualization and Analysis
```python
from bcijelly import Visualizer
viz = Visualizer(results=results, dataset=dataset)
viz.plot_performance_metrics()
viz.show_feature_importance()
viz.generate_report(output_format="html")
```

## Supported BCI Paradigms

### Motor BCI
- Movement intention decoding
- Kinematic parameter prediction
- Grasp type classification
- Force estimation

### Visual BCI
- Visual stimulus reconstruction
- Object category decoding
- Spatial attention tracking
- Visual working memory

### Speech BCI
- Phoneme decoding
- Word recognition
- Sentence reconstruction
- Prosody analysis

### Emotion BCI
- Emotional valence classification
- Arousal level prediction
- Discrete emotion recognition
- Mood state tracking

### Auditory BCI
- Sound source localization
- Music genre classification
- Speech vs. non-speech discrimination
- Auditory scene analysis

## Activation Keywords

Use this skill when working with:
- Brain-computer interface (BCI) research and development
- Neural decoder design and optimization
- Cross-species neural decoding
- Neuromorphic hardware deployment for BCI
- Automated neural network architecture search
- Multi-paradigm BCI systems (motor, visual, speech, emotion, auditory)
- BCI dataset integration and standardization

## Pitfalls and Best Practices

### Common Pitfalls
1. **Data leakage**: Ensure proper separation between training and test sets
2. **Overfitting**: Use regularization and cross-validation for small datasets
3. **Hardware mismatch**: Verify target neuromorphic platform capabilities
4. **Species differences**: Account for anatomical and physiological variations across species

### Best Practices
1. **Start simple**: Begin with single-paradigm, single-species tasks before scaling up
2. **Validate thoroughly**: Use multiple validation metrics beyond accuracy
3. **Monitor resources**: Track computational and energy requirements during search and deployment
4. **Document specifications**: Clear task descriptions improve LLM-guided search effectiveness

## References

- **Original Paper**: BCIJelly: An integrated ecosystem for brain-computer interface research (arXiv:2608.13576)
- **Datasets**: 18 curated BCI datasets covering 5 paradigms and 3 species
- **Decoders**: 15 benchmark decoder implementations with comprehensive evaluation
- **Modules**: 80 reusable algorithmic modules for flexible pipeline construction

## Verification Steps

After implementing a BCIJelly workflow:
1. Verify dataset loading and preprocessing completes successfully
2. Confirm architecture search finds valid architectures within time constraints
3. Validate decoder performance on held-out test set with appropriate metrics
4. Test hardware compilation and deployment if targeting neuromorphic platforms
5. Generate comprehensive reports documenting results and reproducible parameters