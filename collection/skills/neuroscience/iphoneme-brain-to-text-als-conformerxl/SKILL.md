---
name: iphoneme-brain-to-text-als-conformerxl
description: "iPhoneme brain-to-text communication system for ALS using ConformerXL phoneme decoder with gaze-assisted interface. Achieves 92.14% phoneme accuracy (7.86% PER) and 73.39% word accuracy on T15 intracranial EEG dataset. 180ms latency on CPU. Activation: brain-to-text, speech BCI, phoneme decoding, Conformer, ALS, intracranial EEG, iEEG."
---

# iPhoneme: Brain-to-Text Communication for ALS Using ConformerXL Decoding

**arXiv:** [2604.16441](https://arxiv.org/abs/2604.16441)  
**Published:** 2026-04-07  
**Authors:** Yoonmin Cha, Dawit Chun, Sung Park  
**Categories:** cs.SD, cs.AI, cs.CL

## Problem

Speech BCIs for ALS face two critical challenges:
1. **Neural decoding accuracy** limits practical deployment
2. **Input interface design** suffers from Midas touch problem (unintended selections in eye-tracking)

Despite transformative potential for 173,000-232,500 ALS patients worldwide, high-performance speech BCIs demonstrated in only 22-31 patients globally.

## Core System: iPhoneme

### Component 1: ConformerXL Phoneme Decoder (192.9M parameters)

#### Architecture
- **Temporal Prenet:** Multi-scale dilated convolutions + bidirectional GRU
  - Handles neural jitter correction across temporal scales
  - Dilated convolutions capture long-range temporal dependencies
- **Temporal Subsampling:** Reduces sequence length for CTC training stability
- **12 Encoder Blocks** with Pre-RMSNorm stabilization
  - Conformer architecture combining CNN + self-attention
  - Pre-RMSNorm instead of Post-LayerNorm for training stability

#### Training
- **Optimizer:** AdamW with cosine scheduling
- **Loss:** CTC (Connectionist Temporal Classification) for alignment-free phoneme prediction
- **6-gram phoneme language model** trained on 3.1M sequences
- **WFST beam search** (beam=128) for decoding

### Component 2: Gaze-Assisted Phoneme Input Interface

#### Chorded Gaze-Plus-Silent-Speech Paradigm
- Replaces traditional dwell-time selection
- **Chorded input:** Combines gaze direction with silent speech attempt
- Mitigates Midas touch problem through multi-modal verification
- Enables more efficient phoneme input rate

## Key Results

### T15 Dataset (256-channel intracranial EEG)
| Metric | Score |
|--------|-------|
| Phoneme Accuracy | **92.14%** |
| Phoneme Error Rate (PER) | **7.86%** |
| Word Accuracy | **73.39%** |
| Word Error Rate (WER) | **26.61%** |
| Inference Latency | **180 ms** (CPU) |

- ~3% above prior state-of-the-art
- Real-time operation on standard CPU hardware

## Technical Details

### Data
- **T15 dataset:** 45 sessions, 8,071 trials
- **256-channel intracranial EEG** from speech motor cortex regions
- Intracranial (iEEG/ECoG) signals — higher SNR than scalp EEG

### Phoneme Language Model
- 6-gram model trained on 3.1M phoneme sequences
- Integrated via Weighted Finite-State Transducer (WFST)
- Beam search with beam width = 128 for efficient decoding

### Neural Jitter Correction
- Temporal prenet with multi-scale dilated convolutions handles timing variability
- Bidirectional GRU captures forward/backward temporal context
- Critical for handling non-deterministic neural response timing

## Reusable Methodology

### 1. ConformerXL for Neural Signal Decoding
```
# Architecture pattern
Input → TemporalPrenet(dilated_conv + BiGRU) 
     → Subsampling 
     → 12x ConformerBlock(Pre-RMSNorm)
     → CTC Loss
```

### 2. Gaze-Assisted Interface Design
- Chorded paradigm: gaze_direction + silent_speech → phoneme selection
- Dual verification prevents unintended inputs
- Applicable to other BCI modalities

### 3. Phoneme-Level Brain-to-Text Pipeline
1. Record iEEG from speech motor cortex
2. Temporal preprocessing with jitter correction
3. ConformerXL phoneme prediction
4. WFST beam search with language model
5. Phoneme-to-text conversion

## Applications

- **ALS communication:** Primary target for speech restoration
- **Locked-in syndrome:** Brain-to-text for completely paralyzed patients
- **Speech neuroprosthetics:** General speech BCI applications
- **Real-time BCI:** 180ms latency enables conversational use

## Datasets

- **T15:** 256-channel intracranial EEG
  - 45 recording sessions
  - 8,071 trials total
  - Speech motor cortex coverage

## Key Innovations

1. **ConformerXL adaptation** for neural signal phoneme decoding (192.9M params)
2. **Multi-scale temporal prenet** for neural jitter correction
3. **Chorded gaze-plus-silent-speech** interface replacing dwell-time
4. **CPU real-time** operation at 180ms latency
5. State-of-the-art phoneme (92.14%) and word (73.39%) accuracy

## Limitations

- Requires intracranial EEG (invasive) — not applicable to non-invasive BCI
- Performance on limited patient population
- Language model trained on English phonemes only
- 192.9M parameters — large model size

## Related Skills

- `brain-to-speech-prosody-feature-engineering`: Brain-to-speech synthesis
- `brain-to-speech-transformer-reconstruction`: Speech reconstruction from brain signals
- `eeg-foundation-model-adapters`: EEG foundation models with adaptation
- `neural-population-decoding`: Neural population decoding methods
