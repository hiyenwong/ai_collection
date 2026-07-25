---
name: eccentricity-constrained-cnn-visual-coding
description: "Eccentricity-constrained CNN training on egocentric video reveals adaptive, task-aligned information coding across the visual field, with fovea-preferred models advantaged for face and object tasks and periphery-preferred models favored in scene-selective cortex."
metadata:
  arxiv_id: "2607.19316"
  published: "2026-07-22"
  authors: ["Dylan M. Diaz", "Margaret M. Henderson"]
  tags: [neuroscience, computational-neuroscience, visual-cortex, eccentricity, fovea, periphery, cnn, self-supervised-learning, fmri-encoding, egocentric-vision]
license: Complete terms in LICENSE.txt
---

# Eccentricity-Constrained CNN Training for Visual Field Coding

A computational framework that trains ResNet-18 models on gaze-contingent egocentric video to test whether natural experience sculpts eccentricity-dependent visual representations aligned with human visual cortex.

## Core Idea

The primate visual system is organized around eccentricity: central/foveal regions prefer high-resolution, object/face-friendly information, while peripheral regions prefer lower-resolution, scene-layout information. This work asks whether such organization can emerge from natural egocentric experience by training CNNs on video frames that expose only the fovea, only the periphery, or a NeuroFovea-transformed periphery, then evaluating downstream task performance and neural predictivity against human fMRI (Natural Scenes Dataset).

## When to Use

- Building models of eccentricity-dependent visual coding.
- Linking egocentric video statistics to cortical representation.
- Evaluating self-supervised pretraining on naturalistic, gaze-contingent data.
- Comparing foveal vs. peripheral stream specialization in CNNs and brains.

## Key Findings

1. **Fovea-only models outperform periphery-only models** on face (VGGFace2) and scene (Places365) recognition, suggesting central-field information is more broadly useful for downstream tasks.
2. **VEDB-pretrained models approach ImageNet-100-level neural predictivity** in human visual cortex despite lower diversity and semantic content, showing natural egocentric experience is a strong organizational constraint.
3. **Scene-selective cortex (PPA, RSC) prefers periphery-only models**, consistent with the hypothesis that peripheral statistics are more informative for scene layout.
4. **Primary visual cortex (V1) favors fovea-gaze models**, while face-selective regions show no reliable fovea advantage in this dataset.

## Methodology

1. **Data**: Visual Experience Dataset (VEDB) egocentric video + eye-tracking.
2. **Preprocessing**: Create four training conditions:
   - **Baseline**: Full VEDB frames.
   - **Fovea-Gaze**: 112x112 crop centered on gaze position.
   - **Periph**: Complementary peripheral region.
   - **Periph-NF**: Periphery with NeuroFovea transform simulating peripheral information loss.
3. **Pretraining**: SimCLR self-supervised contrastive learning on ResNet-18 with tied weights across augmented views.
4. **Evaluation**:
   - Linear probes for in-domain VEDB categories, VGGFace2 (faces), and Places365 (scenes).
   - Voxel-wise encoding models on Natural Scenes Dataset (NSD) fMRI.
5. **Comparison**: VEDB-pretrained vs. ImageNet-100, STL-10, and ImageNet-1K pretrained backbones.

## Implementation Sketch

```python
# Gaze-contingent crop
fovea_crop = frame[gy-H:gy+H, gx-H:gx+H]  # center on gaze (gx, gy)
periph_mask = create_annular_mask(frame.shape, inner_radius=H)
periph_input = frame * periph_mask

# SimCLR pretraining (standard)
# encoder = ResNet18()
# projector = MLP()
# loss = NT-Xent(augmented_view1, augmented_view2)

# Downstream: linear probe + fMRI encoding model
```

## Interpretation

- Natural egocentric experience provides sufficient statistical structure to learn cortically aligned visual representations.
- The differential downstream utility of foveal vs. peripheral information supports a task-relevance account of eccentricity biases in visual cortex.
- Scene-selective regions' preference for peripheral models suggests adaptation to scene-layout statistics available in the visual periphery.

## Pitfalls

- VEDB has limited semantic diversity compared to curated datasets; task-specific fine-tuning may be needed for some benchmarks.
- NeuroFovea transform is an approximate model of peripheral information loss; real peripheral encoding may differ.
- fMRI noise ceilings and ROI definitions affect sensitivity to model differences in category-selective regions.

## Related Concepts

- Eccentricity bias in visual cortex
- Foveal vs. peripheral processing
- Egocentric vision
- Self-supervised learning (SimCLR)
- Neural encoding models
- Natural Scenes Dataset (NSD)
- Visual Experience Dataset (VEDB)
- Retinotopic organization
- Scene-selective cortex (PPA, RSC)

## Activation

eccentricity, visual field, fovea, periphery, egocentric video, SimCLR, visual cortex, neural encoding, retinotopy, scene-selective cortex, PPA, RSC, VEDB, NSD, computational neuroscience
