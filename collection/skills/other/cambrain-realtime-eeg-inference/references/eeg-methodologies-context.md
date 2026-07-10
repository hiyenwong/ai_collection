# Related EEG Methodologies & Foundation Models

## State Space Models in Neuroscience

### Mamba Architecture
- **Core concept**: Selective state space model with input-dependent dynamics
- **Key innovation**: Linear O(n) complexity for sequence modeling
- **Applications**: Long-range dependency capture without quadratic attention cost
- **Reference**: Gu & Dao, 2023

### S4 (Structured State Space)
- **Earlier SSM variant**: Structured state space for long sequences
- **Limitation**: Less efficient than Mamba for streaming
- **Use case**: Static sequence processing

### EEG-Specific SSM Applications
- **CaMBRAIN**: First causal Mamba for real-time EEG (2605.28792)
- **Streaming EEG**: Linear-time inference for continuous signals
- **Hidden state training**: Multi-stage objectives for memory retention

## EEG Foundation Models

### LaBraM
- **Approach**: Large-scale pre-training on EEG data
- **Limitation**: Fixed-length window processing
- **Architecture**: Transformer-based

### NeuroBERT
- **Approach**: BERT-style pre-training for EEG
- **Limitation**: Bidirectional (overkill for causal EEG)
- **Use case**: Offline EEG classification

### NeuroSTORM
- **Approach**: Foundation model for multi-state fMRI
- **Related**: Cross-modal neuroimaging
- **Reference**: arXiv 2604.xxxxx

### Recent Developments (May 2026)
- **CaMBRAIN**: Causal SSM for real-time EEG (2605.28792)
- **JET**: Flow matching for generative EEG (2605.22xxx)
- **Laya**: LeJEPA approach for EEG foundation (2605.22xxx)

## EEG Signal Characteristics

### Temporal Dynamics
- **Extreme variability**: Events range from milliseconds to minutes
- **Causal structure**: Past → future dependencies only
- **Non-stationary**: Brain state changes over time

### Processing Challenges
1. **Length**: Clinical recordings span hours
2. **Real-time**: Clinical monitoring needs immediate inference
3. **Memory**: Long-range context retention critical
4. **Events**: Brief salient events in long recordings

## Comparison Matrix

| Model | Complexity | Streaming | Causal | EEG Suitability |
|-------|------------|-----------|--------|-----------------|
| Transformer | O(n²) | No | No | Poor (overkill) |
| Bidirectional SSM | O(n) | No | No | Overkill |
| **CaMBRAIN** | O(n) | Yes | Yes | Optimal |
| Sliding-window CNN | O(n×w) | No | Partial | Limited |

## Integration Patterns

### CaMBRAIN + Foundation Models
1. Pre-train foundation model on large EEG corpus
2. Transfer learned representations to CaMBRAIN backbone
3. Fine-tune streaming inference on task-specific data

### CaMBRAIN + Event Detection
1. Run continuous CaMBRAIN inference
2. Monitor hidden state dynamics
3. Detect state transitions as events
4. Trigger downstream analysis on events

### CaMBRAIN + Clinical Systems
1. Deploy streaming inference pipeline
2. Connect to ICU EEG monitors
3. Real-time anomaly detection
4. Alert system for critical patterns

## Key Research Questions

1. **Memory retention**: How to train SSM hidden states for long-range EEG context?
2. **Event detection**: Can hidden state dynamics detect brief salient events?
3. **Multi-modal**: Integration with fMRI/MEG foundation models?
4. **Transfer learning**: Pre-training strategies for EEG SSMs?

## Future Directions

- Multi-modal neuroimaging SSMs (EEG + fMRI)
- Real-time BCI integration
- Clinical deployment pipelines
- Large-scale EEG pre-training for SSMs