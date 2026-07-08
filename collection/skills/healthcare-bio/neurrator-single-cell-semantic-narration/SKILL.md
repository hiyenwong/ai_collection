---
name: neurrator-single-cell-semantic-narration
description: NEURRATOR - Semantic narration of vision at single-cell resolution. Maps spiking activity to natural-language descriptions via CLIP-LLaVA embedding space, enabling functional probing of cell types and brain regions.
version: 1.0.0
category: neuroscience
arxiv_id: 2606.18667
authors: Arnau Marin-Llobet, Richard Hakim, Sara Matias, Venkatesh N. Murthy, Na Li, Demba Ba
institution: Harvard University (Kempner Institute, Center for Brain Science)
published: 2026-06-17
activation_words:
  - neurrator
  - semantic narration
  - single-cell decoding
  - neuron language
  - CLIP neural decoding
  - spike-to-text
  - cell-type functional probe
  - visual cortex narration
  - Neuropixel decoding
  - neural semantic
related_skills:
  - spike-image-decoder
  - brain-cause-causal-visual-representation
  - neural-code-speak
  - neurrate-single-cell-semantic-narration
  - llm-eeg-graph-refinement
---

# NEURRATOR: Semantic Narration of Vision at Single-Cell Resolution

## Core Innovation

NEURRATOR 是首个将**单神经元脉冲活动**直接映射到**自然语言叙述**的框架，实现从视觉皮层神经元活动到语义描述的端到端解码。

**突破性贡献**:
1. **语义级解码器**: 从单细胞脉冲活动生成连贯的自然语言描述
2. **区域/细胞类型作为功能探针**: 输入端使用细胞身份，输出端返回功能描述
3. **概念级分解**: 结合稀疏自编码器(SAE)将细胞贡献分解为可解释的视觉概念特征

## Methodology

### Architecture

```
Spike Trains → [Neurrator Encoder] → CLIP Patch Embeddings → [Frozen LLaVA] → Natural Language
```

**核心组件**:
1. **Neurrator Encoder**: 
   - Multi-scale 1D-CNN spike-train frontend
   - Transformer temporal encoder
   - Attention-weighted temporal pooling
   - 576 learned patch queries (24×24 grid, 1024-d)
   
2. **PatchInjector Hook**: Runtime bypass of LLaVA vision tower

3. **Frozen LLaVA-1.5-7B**: Multimodal projector + LLaMA-2-7B decoder (no training)

### Training Objective

```python
L = 0.5 * MSE(P̂_t, P_f(t)) + 0.5 * (1 - cos(P̂_t, P_f(t)))
```

Dual loss: MSE + cosine similarity on predicted vs. true CLIP patch tensors.

### Natural Language Decoding

- Greedy decoding with fixed one-sentence prompt
- No language-side training
- Patch tensor is the only modality bridge

## Key Results

### Decoding Fidelity Scaling

| Population | Semantic Accuracy | Generalization |
|------------|-------------------|----------------|
| 1000s neurons | High | Across held-out frames |
| Single region | Moderate | Across movies |
| Single neuron | Low but interpretable | N/A |

### Region-Level Findings

- **Higher visual cortex**: Better semantic fidelity
- **Primary visual cortex**: Lower but still functional
- **Cell-type signatures**: Distinct concept profiles

### Concept-Level Decomposition

Using CLIP SAE:
- PV interneurons → "small rounded objects"
- Excitatory cells → broader semantic concepts
- Each cell type has interpretable concept dictionary

## Implementation Details

### Input Processing

```python
# Spike preprocessing
spike_counts = bin_and_zscore(raw_spikes, 
                             training_stats_only=True)

# Encoder architecture
encoder = nn.Sequential(
    MultiScaleConv1D(spike_window),  # Multi-scale temporal
    TransformerEncoder(window_length),
    AttentionPool(),
    PatchQueryCrossAttention(576 patches)
)
```

### PatchInjector Hook

```python
class PatchInjector:
    def __call__(self, module, input, output):
        # Replace LLaVA vision tower output
        return predicted_patch_tensor
```

### SAE Concept Decomposition

```python
# Sparse autoencoder on CLIP space
sae = pretrained_CLIP_SAE()
concept_profile = sae.encode(neural_patch_prediction)
# Returns sparse activation over named concepts
```

## Experimental Validation

### Dataset
- **Neuropixels recordings**: Mouse visual cortex
- **Natural movie viewing**: Video stimuli
- **Molecular cell types**: Optotagged populations

### Evaluation Metrics
1. **Semantic accuracy**: Human evaluation of caption quality
2. **Cross-movie generalization**: Held-out stimulus
3. **Concept-axis validation**: Bootstrap + orthogonal CLIP-text
4. **Size-matched controls**: Random population comparison

## Biological Insights

### Cell-Type as Functional Probe

Traditional approach: Cell-type as **classification output**
NEURRATOR approach: Cell-type as **functional input probe**

```python
# Functional probing
for cell_type in [PV, SST, VIP, Excitatory]:
    activity = get_spikes(cell_type)
    narration = neurrator(activity)
    concepts = sae.decode(activity)
    # Returns: what this cell type encodes
```

### Mushroom Body Dominance

Leading adjoint modes concentrated in mushroom body:
- Insect learning center shapes recurrent dynamics
- Sparse input routing confined to olfactory pathway
- Random networks flood activity everywhere

## Applications

### Research Applications
1. **Single-neuron characterization**: What does each cell encode?
2. **Population scaling laws**: How many neurons needed for semantic fidelity?
3. **Circuit functional probing**: What does each region contribute?
4. **Cell-type concept signatures**: Genetic identity → function

### Clinical Potential
- Neural prosthetics with semantic feedback
- BCI with natural-language output
- Cell-type-specific therapeutic targeting

## Technical Requirements

### Dependencies
- PyTorch
- transformers (LLaVA, CLIP)
- sparse_autoencoder library
- Neuropixels data processing

### Hardware
- GPU training: Encoder fitting
- CPU inference: Frozen LLaVA decoding

## Limitations & Future Directions

### Current Limitations
1. **Fixed dynamical regime**: No physiological tuning
2. **Frozen language model**: No neural-data language training
3. **Mouse visual cortex**: Generalization to other species?

### Extensions
- Multi-modal stimuli (audio, olfaction)
- Behavioral state integration
- Temporal narrative coherence
- Human cortical application

## Code & Resources

- **GitHub**: https://github.com/arnaumarin/neurrator
- **Data**: Allen Institute Neuropixels
- **Models**: CLIP ViT-L/14, LLaVA-1.5-7B

## Citation

```bibtex
@article{marin2026neurrator,
  title={Can neurons speak? Semantic narration of vision at single-cell resolution},
  author={Marin-Llobet, Arnau and Hakim, Richard and Matias, Sara and Murthy, Venkatesh N. and Li, Na and Ba, Demba},
  journal={arXiv preprint arXiv:2606.18667},
  year={2026}
}
```

## Key Takeaways

1. **Bridge to language**: Spikes → CLIP embeddings → Natural language
2. **Uniform decoder**: Same model for arbitrary subpopulations
3. **Concept decomposition**: SAE exposes cell-type-specific features
4. **Functional probes**: Cell identity as input, not output
5. **No language training**: Frozen multimodal model

---

**Activation**: Use when analyzing spike-to-language decoding, cell-type functional characterization, semantic neural decoding, or CLIP-based neural embedding approaches.