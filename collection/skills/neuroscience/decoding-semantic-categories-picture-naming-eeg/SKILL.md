# Decoding Semantic Categories from Picture-Naming EEG

---
created: 2026-06-16
arxiv_id: 2606.14614
authors: Wei Hu, Binbin Xu
categories: q-bio.NC, eess.SP
published: 2026-06-12
activation: EEG decoding, semantic categories, picture naming, neural decoding, lexical-semantic processing, language production, deep learning, multilingual embeddings
---

## Summary

This study demonstrates that semantic-category information is recoverable from high-density EEG during overt picture naming. Using a pre-trained single-channel EEG encoder and multilingual text-embedding model, researchers achieved **78.4% Macro-F1** in nine-class semantic-category decoding, showing that early and naming-related temporal windows provide complementary information for lexical-semantic processing.

## Key Findings

### Decoding Performance
- **Balanced accuracy**: 0.562 (early window) → 0.610 (naming-related) → **0.781 (combined)** 
- **Maximum Macro-F1**: **0.784** when combining both temporal windows
- Class-level F1 scores: **consistent gains across all semantic categories**
- Sensor-level maps: **spatially distributed category information**

### Temporal Dynamics
- **Early post-stimulus window**: 0-500ms (perceptual processing)
- **Naming-related window**: 500-1200ms (lexical-semantic processing)
- **Combined representation**: Complementary information extraction

### Semantic Category Structure
- **Multilingual text-embedding model** (line drawings → labels → embeddings)
- **Nine interpretable semantic categories** (data-driven semantic target space)
- Categories recoverable without music-theoretic input

## Technical Framework

### EEG Representation
```
Pipeline:
1. High-density EEG (64+ channels)
2. Single-channel encoder (pre-trained)
3. Channel-wise representation extraction
4. Temporal window selection (early + naming-related)
5. Combined feature fusion
```

### Semantic Target Space
```
Construction:
Picture labels → Multilingual text-embedding model → 
Semantic embedding space → Nine interpretable categories

Categories:
- Natural objects (animals, plants)
- Man-made objects (tools, vehicles)
- Abstract concepts
- Actions
- etc.
```

### Decoding Architecture
```
Model Components:
- Pre-trained EEG encoder (single-channel)
- Temporal window selector
- Feature fusion layer
- Nine-class classifier

Performance:
Input: EEG activity → 
Encoder → Channel representations → 
Temporal fusion → 
Semantic category prediction
```

## Experimental Setup

### Participants
- **16 native French-speaking participants**
- Picture-naming task with line drawings
- Overt naming (spoken responses)

### EEG Acquisition
- High-density EEG setup
- Overt picture naming task
- Multilingual semantic target space

### Evaluation Metrics
- Balanced accuracy
- Macro-F1 score
- Class-level F1 scores
- Sensor-level decoding maps

## Implications

### For Language Production Research
1. **Semantic-category structure reflected in EEG** during overt picture naming
2. **Early and naming-related windows** provide complementary information
3. **Modern neural decoding** viable tool for lexical-semantic processing

### For BCI Applications
1. **Semantic-category decoding** from EEG possible
2. **Overt speech production** EEG decoding achievable
3. **Multilingual embeddings** enhance semantic target space

### For Neurolinguistics
1. **Perceptual → Semantic → Lexical → Articulatory** pathway observable
2. **Temporal dynamics** of semantic processing measurable
3. **Cross-language semantic embeddings** transferable

## Implementation Guidelines

### EEG Semantic Decoder
```python
# Core pipeline:
class EEGSemanticDecoder:
    def __init__(self, n_channels, n_categories):
        self.encoder = PretrainedEEGEncoder()
        self.temporal_selector = TemporalWindowSelector(
            early_window=(0, 500),  # ms
            naming_window=(500, 1200)  # ms
        )
        self.fusion = FeatureFusionLayer()
        self.classifier = NineClassClassifier(n_categories)
    
    def encode_channel_wise(self, eeg_data):
        # Single-channel encoder per channel
        channel_repr = []
        for ch in range(eeg_data.shape[1]):
            repr = self.encoder(eeg_data[:, ch])
            channel_repr.append(repr)
        return np.stack(channel_repr)
    
    def extract_temporal_windows(self, channel_repr):
        early = self.temporal_selector.extract_early(channel_repr)
        naming = self.temporal_selector.extract_naming(channel_repr)
        return early, naming
    
    def fuse_and_classify(self, early, naming):
        fused = self.fusion(early, naming)
        return self.classifier(fused)
```

### Semantic Target Space Construction
```python
# Build semantic category space:
def build_semantic_space(labels, embedding_model):
    # Multilingual text embeddings
    embeddings = embedding_model.encode(labels)
    
    # Cluster into nine categories
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=9)
    categories = kmeans.fit_predict(embeddings)
    
    return categories, embeddings
```

## Related Research

### EEG Decoding
- Schirrmeister et al. (2017) - Deep learning for EEG decoding
- Lawhern et al. (2018) - EEGNet architecture

### Semantic Processing
- Indefrey & Levelt (2004) - Time course of language production
- Huth et al. (2016) - Semantic representations in brain

### Picture Naming
- Glaser (1992) - Picture naming paradigm
- Levelt et al. (1999) - Lexical access in speech production

## Applications

### Speech BCI
- **Semantic intent decoding** before articulation
- **Vocabulary prediction** from neural signals
- **Communication aid** for speech disorders

### Neurolinguistic Research
- **Temporal dynamics** of semantic processing
- **Cross-language comparison** of semantic representations
- **Semantic category evolution** in development

### Clinical Assessment
- **Semantic processing deficits** detection
- **Language disorder diagnosis**
- **Cognitive impairment screening**

## Future Directions

1. **Expand category count** beyond nine
2. **Cross-subject generalization** improvement
3. **Multilingual participants** inclusion
4. **Real-time decoding** implementation
5. **Integration with articulation** prediction

## Key References

- Hu & Xu (2026) - This paper
- Schirrmeister et al. (2017) - Deep EEG decoding
- Indefrey & Levelt (2004) - Language production timeline
- Levelt et al. (1999) - Lexical access model