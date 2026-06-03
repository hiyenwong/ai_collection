---
name: neuroscience-research-monitor
description: Automated neuroscience research monitoring from arXiv. Searches multiple categories (q-bio.NC, cs.NE, neuroscience-related keywords) for latest papers, extracts key information, and generates research summaries with skills.
---

# Neuroscience Research Monitor

## Purpose
Systematically monitor arXiv for the latest neuroscience, brain network, neural dynamics, spiking neural network, and computational neuroscience papers.

## Search Strategy

### ArXiv Categories
1. **q-bio.NC** - Neurons and Cognition
2. **cs.NE** - Neural and Evolutionary Computing
3. **Keyword queries** - "brain network", "neural dynamics", "spiking neural", "computational neuroscience"

### API Endpoint
```
http://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results=15
```

## Paper Selection Criteria

Papers are evaluated based on:
1. **Novelty** - Does it propose a new method, architecture, or framework?
2. **Relevance** - Direct connection to neuroscience, brain networks, neural dynamics, or SNNs
3. **Technical depth** - Substantive contribution vs. incremental improvements
4. **Applicability** - Potential for implementation or integration into existing work

## Recent Papers (April 2026)

### High-Value Papers

#### 1. Working Memory in Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
- **arXiv**: 2604.14096 (2026-04-15)
- **Authors**: Laurent U Perrinet
- **Key contribution**: Recurrent SNN with N neurons where each synapse has D=41 heterogeneous delays, enabling working memory for precise temporal pattern storage and recall
- **Relevance**: Addresses fundamental challenge in SNNs - working memory through heterogeneous delays rather than complex architectures
- **Skill connection**: `snn-working-memory-heterogeneous-delays`

#### 2. Modeling of Self-sustained Neuron Population without External Stimulus
- **arXiv**: 2604.13719 (2026-04-15)
- **Authors**: İhsan Ertuğrul Karakaş, Özden Özel, İlkay Ulusoy, Orhan Murat Koçak
- **Key contribution**: Studies conditions for self-sustained neural activity emergence in biophysically grounded network models without external input
- **Relevance**: Fundamental understanding of autonomous neural dynamics
- **Skill connection**: `self-sustained-neuron-population`

#### 3. From Brain Models to Executable Digital Twins: Execution Semantics and Neuro-Neuromorphic Systems
- **arXiv**: 2604.13574 (2026-04-15)
- **Authors**: Alexandre Muzy
- **Key contribution**: Framework bridging computational brain models to executable digital twins with proper execution semantics, enabling individualized brain representations
- **Relevance**: Important for clinical applications and personalized medicine
- **Skill connection**: `brain-digital-twins-execution-semantics`

#### 4. General aspects of internal noise in spiking neural networks
- **arXiv**: 2604.13612 (2026-04-15)
- **Authors**: I. D. Kolesnikov, D. A. Maksimov, V. M. Moskvitin, N. Semenova
- **Key contribution**: Examines additive and multiplicative noise impact on LIF neurons and trained SNNs across processing stages
- **Relevance**: Critical for understanding SNN robustness and hardware implementations
- **Skill connection**: `snn-internal-noise-analysis`

#### 5. Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining
- **arXiv**: 2604.12683 (2026-04-14)
- **Authors**: Junfeng Xia, Wenhao Ye, Xuanye Pan, Xinke Shen
- **Key contribution**: Universal fMRI foundation model supporting diverse brain states with metadata-conditioned pretraining, overcoming limited brain state range of current models
- **Relevance**: Major advance in fMRI foundation models for cross-state generalization
- **Skill connection**: `brain-dit-fmri-foundation-model`

#### 6. Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching
- **arXiv**: 2604.11178 (2026-04-13)
- **Authors**: Nicole Rogalla, Yuzhen Qin, Mario Senden, Ahmed El-Gazzar
- **Key contribution**: Generative forecasting framework for neural dynamics using autoregressive flow matching, enabling probabilistic prediction of brain activity
- **Relevance**: Novel approach for neural dynamics prediction with uncertainty quantification
- **Skill connection**: `autoregressive-flow-matching-neural`

#### 7. Astrocytic resource diffusion stabilizes persistent activity in neural fields
- **arXiv**: 2604.10036 (2026-04-11)
- **Authors**: Noah Palmer, Heather L. Cihak, Daniele Avitabile, Zachary P. Kilpatrick
- **Key contribution**: Introduces astrocyte network support into spatially extended neural circuit models, showing how astrocytic resource diffusion stabilizes working memory persistent activity
- **Relevance**: Bridges gap between metabolic support and neural circuit models
- **Skill connection**: `astrocyte-resource-diffusion-neural-fields`

#### 8. Attention to task structure for cognitive flexibility
- **arXiv**: 2604.13281 (2026-04-14)
- **Authors**: Xiaoyu K. Zhang, Mehdi Senoussi, Tom Verguts
- **Key contribution**: Neural network model of attention mechanisms enabling cognitive flexibility - retaining prior knowledge while transferring to new tasks
- **Relevance**: Important for understanding how brains and AI systems manage task switching
- **Skill connection**: `attention-task-structure-cognitive-flexibility`

#### 9. Relaxing in Warped Spaces: Generalized Hierarchical and Modular Dynamical Neural Network
- **arXiv**: 2604.10606 (2026-04-12)
- **Authors**: Kazuyoshi Tsutsumi, Ernst Niebur
- **Key contribution**: Dynamical neural network with hierarchical and modular structure derived from energy minimization with neurons of different time constants
- **Relevance**: Novel architecture for modular neural dynamics
- **Skill connection**: `warped-hierarchical-modular-neural-network`

## Automation Workflow

1. **Fetch** - Query arXiv API across multiple categories
2. **Parse** - Extract titles, authors, abstracts, dates
3. **Filter** - Remove duplicates, rank by relevance
4. **Analyze** - Select high-value papers for deeper study
5. **Generate** - Create/update skills for significant contributions
6. **Sync** - Update Obsidian wiki with structured notes

### Papers Added April 23, 2026 (Cron Job Round 2)

#### 10. Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching
- **arXiv**: 2604.11178 (2026-04-13)
- **Key contribution**: Generative forecasting for neural dynamics using autoregressive flow matching with uncertainty quantification
- **Skill created**: `autoregressive-flow-matching-neural-dynamics`

#### 11. Intrinsic Neuro-Synaptic Spiking Dynamics in Self-Organizing Memristive Networks
- **arXiv**: 2604.18015 (2026-04-17)
- **Key contribution**: Self-organizing memristive networks generating neuronal population dynamics without external control
- **Skill created**: `intrinsic-neurosynaptic-memristive-spiking`

#### 12. ODEBrain — Neural ODE latent dynamic forecasting for continuous-time EEG graph prediction
- **arXiv**: 2602.23285 (2026-02)
- **Key contribution**: Neural ODE-based framework for continuous-time EEG signal forecasting with graph structure
- **Skill created**: `odebrain-continuous-time-eeg-graph`

**Papers skipped (existing skills):**
- Adaptive Spiking Neuron (2604.12365) — ~10 existing ASN skills
- Working Memory SNN (2604.14096) — `snn-working-memory-heterogeneous-delays-v2` already covers

### Papers Added April 23, 2026 (Cron Job Round 3 — 15 Skills Batch)

**Search Statistics**: 56 unique papers from 5 keywords + 6 categories, top 15 selected.

| # | Paper | arXiv | Skill Created | Status |
|---|-------|-------|---------------|--------|
| 1 | NeuroAI Roadmap (NSF Workshop) | — | `neuroai-beyond-bridging-neuroscience-ai` | Updated v2.0 |
| 2 | EMBER: Autonomous Cognitive Behaviour | — | `ember-autonomous-cognitive-behaviour-learned-spiking` | Updated v2.0 |
| 3 | Brain-DiT Universal Multi-state fMRI | 2604.12683 | `brain-dit-fmri-foundation-model-v6` | Updated v2.0 |
| 4 | Adaptive Spiking Neuron (ASN) | 2604.12365 | `adaptive-spiking-neurons-asn` | Updated v2.0 |
| 5 | Dual-Timescale Memory (Neuron-Astrocyte) | — | `dual-timescale-neuron-astrocyte-memory` | Updated v2.0 |
| 6 | Brain-Inspired Capture (BI-Cap) | — | `brain-inspired-capture-visual-decoding` | New |
| 7 | Working Memory Heterogeneous Delays | 2604.14096 | `snn-working-memory-heterogeneous-delays-v3` | New |
| 8 | Autoregressive Flow Matching Neural | 2604.11178 | `autoregressive-flow-matching-neural-dynamics` | New |
| 9 | Quantization SNN Beyond Accuracy | — | `snn-quantization-beyond-accuracy` | New |
| 10 | Conv-Delay Learning Recurrent SNN | — | `conv-delay-learning-snn` | New |
| 11 | Neuromorphic Parameter Estimation | — | `neuromorphic-parameter-estimation-power-converter` | Kept English |
| 12 | TTA EEG Foundation Models | — | `tta-eeg-foundation-models` | Kept English |
| 13 | ISI-CV Gradient-Free Continual SNN | — | `isi-cv-gradient-free-continual-learning-snn` | Updated Chinese |
| 14 | Mind2Drive EEG Driver Intent | — | `mind2drive-eeg-driver-intention` | Kept English |
| 15 | DLink EEG Distillation | — | `dlink-eeg-distillation` | Updated Chinese |

**Research Trends Identified**:
1. **Brain Foundation Models** — Universal multi-modal models (fMRI/EEG/MEG) with metadata conditioning
2. **Hybrid SNN-LLM Architectures** — Combining spiking efficiency with LLM reasoning (EMBER)
3. **Astrocyte-Neuron Co-processing** — Glial cells as computational resources, not just support
4. **Energy-Efficient Neuromorphic** — Quantization, delay learning, low-precision SIMD
5. **Test-Time Adaptation for EEG** — Domain adaptation without retraining foundation models

**Operational Statistics**:
- 3 delegate_task batches (5 skills each), glm-5.1 model
- Total: ~2067s, ~1.94M input tokens, ~77K output tokens
- 25 skill_manage calls, 6 skill_view verifications

## Operational Pitfalls & Fallback Strategies

### 1. `web_search` Unreliability
`web_search` frequently returns errors during cron runs. **Fallback**: use `browser_navigate` to hit the arXiv API directly, then `browser_console` with a JS expression to extract and parse the XML:
```
browser_navigate → http://export.arxiv.org/api/query?search_query=...
browser_console → expression: "document.querySelector('feed').innerHTML"
```
This is more reliable than `web_search` or `web_extract` (which blocks arXiv API URLs as "private/internal network").

### 2. Obsidian Note Creation
**Never use shell `cat >` heredocs** for writing to the Obsidian vault — macOS sandbox permissions cause intermittent failures. **Always use `hermes_tools.write_file()`** from `execute_code`, which handles quoting and spaces in paths correctly.

### 3. Python Triple-Quoted Strings with YAML Frontmatter
When using `execute_code` to create Obsidian markdown files, **do NOT embed YAML frontmatter with date strings** (e.g. `2026-04-25`) inside Python triple-quoted strings — the `-` in dates gets parsed as subtraction, causing `SyntaxError`. Use `write_file()` from hermes_tools instead.

### 4. Skill Deduplication
Before creating a skill, always check with `skill_view()` — many neuroscience papers already have skills. When a new paper extends an existing one, create a versioned skill (e.g., `brain-dit-fmri-foundation-model-v7`) rather than overwriting.

### 5. delegate_task for Parallel Research
Use `delegate_task` with batch `tasks` (up to 3 concurrent) for:
- Paper search & collection (`["web", "browser"]`)
- Skill creation/audit (`["skills"]`)
- Obsidian note writing (`["browser"]` — needs file write via hermes_tools)

### Papers Added April 25, 2026 (Cron Job Round 4)

| # | Paper | arXiv | Skill Created | Status |
|---|-------|-------|---------------|--------|
| 1 | MILRO: Memory-Induced Long-Range Order | 2604.21071 | `milro-memory-induced-long-range-order-brain-criticality` | New |
| 2 | Working Memory SNN Delays | 2604.14096 | `snn-working-memory-heterogeneous-delays-v4` | Exists |
| 3 | Autoregressive Flow Matching Neural | 2604.11178 | `autoregressive-flow-matching-neural-dynamics` | Exists |
| 4 | ISI-CV Gradient-Free Continual SNN | 2604.16496 | `isi-cv-gradient-free-continual-learning-snn` | Exists |
| 5 | Brain-DiT v7 fMRI Foundation | 2604.12683 | `brain-dit-fmri-foundation-model-v7` | New (superseded v6) |

**Obsidian Notes Created**:
- `Neuroscience Research/MILRO - Memory-Induced Long-Range Order in Brain Criticality.md`
- `Neuroscience Research/Brain-DiT v7 - Universal Multi-state fMRI Foundation Model.md`
- `Neuroscience Research/2026-04-25 Research Monitor Summary.md` (weekly cross-linked summary)

**Emerging Themes (April 2026)**:
1. Beyond-criticality alternatives (MILRO challenges Griffiths phase)
2. fMRI foundation models with metadata conditioning (Brain-DiT)
3. Generative neural dynamics (flow matching, diffusion)
4. SNN efficiency via delay learning, quantization, gradient-free methods
5. Brain-inspired AI (neuromimetic pipelines, hippocampal memory for RAG)

## Update Schedule
Run weekly to capture new papers and update the knowledge base.