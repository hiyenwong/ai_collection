---
name: simon-saliency-neural-decoding
description: "SIMON: Saliency-aware Integrative Multi-view Object-centric Neural Decoding for zero-shot EEG-to-image retrieval. Uses saliency-aware sampling and foveated views to overcome center-bias limitations. Trigger words: SIMON neural decoding, EEG-to-image retrieval, saliency-aware EEG, foveated neural decoding, zero-shot EEG image, object-centric neural decoding, multi-view EEG."
---

# SIMON: Saliency-aware Multi-view Neural Decoding

## Overview

SIMON addresses a critical limitation in EEG-to-image retrieval: most methods assume fixed, center-focused viewing, creating geometric-semantic dissociation between visual features and EEG responses. SIMON overcomes this with saliency-aware multi-view integration.

## Core Methodology

### Saliency-Aware Sampling (SAS)
1. Foreground segmentation: Isolate objects from background
2. Saliency prediction: Identify attention-worthy regions
3. Fixation center selection: Sample fixation points based on saliency map
4. Foveated view generation: Create multi-resolution views centered on salient regions

### Architecture
- Input: EEG signals + candidate images
- Multi-view encoder: Process foveated views at different scales
- EEG-brain encoder: Map neural responses to visual features
- Zero-shot retrieval: Match EEG embeddings to image embeddings without task-specific training

### Key Advantages
- Eliminates center-bias assumption
- Captures content-driven human attention patterns
- Works in both intra-subject and inter-subject settings
- Robust across sampling granularities and encoder backbones

## Performance

| Setting | Top-1 Accuracy |
|---------|---------------|
| Intra-subject | 69.7% |
| Inter-subject | 19.6% |

Consistently outperforms recent competitive baselines on THINGS-EEG dataset.

## Implementation Pattern

```python
class SIMON:
    def saliency_aware_sampling(self, image, n_fixations=5):
        saliency = self.saliency_model(image)
        fixations = sample_by_saliency(saliency, n_fixations)
        views = [create_foveated_view(image, f) for f in fixations]
        return views

    def encode(self, eeg, image):
        eeg_emb = self.eeg_encoder(eeg)
        views = self.saliency_aware_sampling(image)
        view_embs = [self.visual_encoder(v) for v in views]
        image_emb = aggregate_views(view_embs)
        return eeg_emb, image_emb

    def retrieve(self, query_eeg, candidate_images, top_k=1):
        q_emb = self.eeg_encoder(query_eeg)
        scores = []
        for img in candidate_images:
            views = self.saliency_aware_sampling(img)
            img_emb = aggregate_views([self.visual_encoder(v) for v in views])
            scores.append(cosine_similarity(q_emb, img_emb))
        return top_k_indices(scores, top_k)
```

## When to Use

- Zero-shot EEG-to-image retrieval tasks
- Brain-computer interface for visual content decoding
- Neural decoding where attention is not center-focused
- Cross-subject neural decoding with attention variability

## Paper Reference

- arXiv: 2605.00401v1 [cs.CV, q-bio.NC]
- Authors: YuSheng Lin, Ji-Hwa Tsai, Chun-Shu Wei
- Date: 2026-05-01
- Code: https://github.com/simonlink666/SIMON

## Related Skills

- eeg-visual-attention-decoding
- sgdm-eeg-visual-cognition
- eeg2vision-multimodal-eeg-framework-2d-visual
