# Reference: In-Context Brain Decoding

## Paper Details

**Title:** Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding

**Authors:** 
- Mu Nan, Muquan Yu, Weijian Mai, Jacob S. Prince, Hossein Adeli
- Rui Zhang, Jiahang Cao, Benjamin Becker, John A. Pyles
- Margaret M. Henderson, Chunfeng Song, Nikolaus Kriegeskorte
- Michael J. Tarr, Xiaoqing Hu, Andrew F. Luo

**Venue:** CVPR 2026 (Accepted)

**arXiv:** 2604.08537

**Code:** https://github.com/ezacngm/brainCodec

## Abstract

Visual decoding from brain signals is a key challenge at the intersection of computer vision and neuroscience, requiring methods that bridge neural representations and computational models of vision. A field-wide goal is to achieve generalizable, cross-subject models. A major obstacle towards this goal is the substantial variability in neural representations across individuals, which has so far required training bespoke models or fine-tuning separately for each subject.

To address this challenge, we introduce a meta-optimized approach for semantic visual decoding from fMRI that generalizes to novel subjects without any fine-tuning. By simply conditioning on a small set of image-brain activation examples from the new individual, our model rapidly infers their unique neural encoding patterns to facilitate robust and efficient visual decoding. Our approach is explicitly optimized for in-context learning of the new subject's encoding model and performs decoding by hierarchical inference, inverting the encoder. First, for multiple brain regions, we estimate the per-voxel visual response encoder parameters by constructing a context over multiple stimuli and responses. Second, we construct a context consisting of encoder parameters and response values over multiple voxels to perform aggregated functional inversion. We demonstrate strong cross-subject and cross-scanner generalization across diverse visual backbones without retraining or fine-tuning. Moreover, our approach requires neither anatomical alignment nor stimulus overlap. This work is a critical step towards a generalizable foundation model for non-invasive brain decoding.

## Key Contributions

1. **Training-Free Cross-Subject Generalization**
   - First approach to achieve zero-shot generalization without fine-tuning
   - Eliminates need for subject-specific model training
   - Reduces calibration data requirements dramatically

2. **Hierarchical Inference Framework**
   - Two-level context construction
   - Level 1: Stimulus-response context for encoding estimation
   - Level 2: Encoder-voxel context for functional inversion

3. **Practical Advantages**
   - No anatomical alignment required
   - No stimulus overlap needed
   - Cross-scanner generalization
   - Compatible with diverse visual backbones

## Technical Details

### Problem Formulation

Given:
- A new subject with minimal calibration data
- fMRI responses to visual stimuli
- Goal: Decode visual representations from brain signals

Traditional approach:
```
Train subject-specific model → Fine-tune on new subject → Decode
```

Proposed approach:
```
Meta-trained model → In-context learning → Direct decoding
```

### Meta-Learning Framework

**Inner Loop (Subject Adaptation):**
```
Given: Context pairs {(x₁, y₁), ..., (xₙ, yₙ)}
Estimate: Subject-specific encoding model f_θ
Objective: Minimize prediction error on context
```

**Outer Loop (Meta-Training):**
```
Across: Multiple subjects
Optimize: Meta-parameters φ
Objective: Minimize decoding error after adaptation
```

### Encoding Model

The encoding model maps visual features to predicted brain responses:

```
r = f_θ(v) + ε

where:
- v: Visual feature vector
- r: Brain response (fMRI BOLD)
- θ: Subject-specific parameters
- ε: Noise
```

### Functional Inversion

Decoding is formulated as inverse problem:

```
v̂ = argmin_v ||r - f_θ(v)||² + λΩ(v)

where:
- v̂: Decoded visual features
- r: Observed brain response
- θ: Estimated encoding parameters
- Ω: Regularization term
```

## Experimental Results

### Datasets
- Natural Scene Dataset (NSD)
- Generic Object Decoding (GOD)
- Brain/Cloud dataset

### Evaluation Metrics
- Identification accuracy
- Correlation between predicted and actual features
- Semantic similarity

### Key Findings

1. **Cross-Subject Performance**
   - Comparable to subject-specific trained models
   - Significantly outperforms anatomical alignment baselines
   - Generalizes across different visual regions

2. **Cross-Scanner Robustness**
   - Maintains performance across different MRI scanners
   - Handles different acquisition protocols
   - Robust to scanner-specific artifacts

3. **Efficiency**
   - Requires only 5-10 example pairs for new subject
   - Inference time: <1 second per decoding
   - No retraining needed

## Implementation Notes

### Visual Feature Extraction
- CLIP ViT-L/14 recommended
- Other backbones: ResNet, EfficientNet, Swin Transformer
- Features extracted from penultimate layer

### fMRI Preprocessing
- Standard preprocessing (motion correction, slice-timing, etc.)
- z-scoring within each run
- Nuisance regression (motion parameters, drift)
- Region-of-interest selection (early visual cortex, ventral stream)

### Context Construction
- Random sampling of diverse stimuli
- Balanced coverage of visual space
- Quality control for motion artifacts

### Hyperparameters
- Context size: 5-10 examples
- Learning rate: 1e-4 (meta-training)
- Batch size: 4-8 subjects
- Training epochs: 100-200

## Comparison with Related Work

| Method | Fine-tuning | Anatomical Alignment | Stimulus Overlap | Cross-scanner |
|--------|-------------|---------------------|------------------|---------------|
| Subject-specific CNN | Required | No | Yes | Limited |
| Anatomical alignment | Not required | Required | No | Limited |
| Functional alignment | Required | No | Required | Moderate |
| **Meta-learning (Ours)** | **Not required** | **Not required** | **Not required** | **Strong** |

## Limitations and Future Work

**Current Limitations:**
- Requires some context examples (not fully zero-shot)
- Focused on visual cortex (not whole brain)
- Performance degrades with very few examples (<5)

**Future Directions:**
- Extend to other brain regions
- Incorporate anatomical priors optionally
- Develop active learning for context selection
- Apply to other modalities (MEG, EEG)

## Citation

```bibtex
@inproceedings{nan2026meta,
  title={Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding},
  author={Nan, Mu and Yu, Muquan and Mai, Weijian and Prince, Jacob S. and Adeli, Hossein and Zhang, Rui and Cao, Jiahang and Becker, Benjamin and Pyles, John A. and Henderson, Margaret M. and Song, Chunfeng and Kriegeskorte, Nikolaus and Tarr, Michael J. and Hu, Xiaoqing and Luo, Andrew F.},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2026}
}
```

## Related Papers

1. **Brain Decoding:**
   - "Toward a realistic model of speech processing in the brain" (Nature, 2023)
   - "Reconstructing dynamic mental models in the brain" (Nature Neuroscience, 2024)

2. **Meta-Learning:**
   - "Model-Agnostic Meta-Learning" (ICML 2017)
   - "Learning to Learn: A Brief Review" (NeurIPS 2019)

3. **In-Context Learning:**
   - "Language Models are Few-Shot Learners" (NeurIPS 2020)
   - "In-context Learning and Induction Heads" (Transformer Circuits, 2022)

4. **Cross-Subject fMRI:**
   - "Hyperalignment" (NeuroImage, 2011)
   - "Shared and subject-specific representation spaces" (Nature Communications, 2020)
