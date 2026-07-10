# Template: Causal SSM Implementation for Time-Series

Use this template when implementing causal state space models for inherently unidirectional temporal data.

## Applicability Check

Before using this template, verify the data exhibits:
- [ ] **Causal temporal structure**: Past → future dependencies only (no bidirectional influence)
- [ ] **Long-range dependencies**: Context from distant past influences current predictions
- [ ] **Streaming requirement**: Real-time or continuous inference needed
- [ ] **Variable-length sequences**: Cannot batch into fixed-size windows

Examples:
- EEG/EMG signals (brain/muscle activity)
- Physiological signals (ECG, respiration)
- Financial time series (market dynamics)
- Sensor streams (IoT, robotics)
- Speech/audio (real-time transcription)

## Architecture Components

### 1. Causal Backbone Selection

**Mamba variants**:
```python
# PyTorch implementation (conceptual)
from mamba_ssm import Mamba

class CausalMambaBackbone(nn.Module):
    def __init__(self, d_model, n_layer, d_state=16, d_conv=4, expand=2):
        super().__init__()
        self.layers = nn.ModuleList([
            Mamba(d_model=d_model, d_state=d_state, d_conv=d_conv, expand=expand)
            for _ in range(n_layer)
        ])
    
    def forward(self, x):  # x: (batch, seq_len, d_model)
        # Causal: processes from left to right only
        for layer in self.layers:
            x = layer(x)
        return x
```

**Key parameters**:
- `d_state`: Hidden state dimension (memory capacity)
- `d_conv`: Local convolution kernel size
- `expand`: Expansion factor (d_inner = d_model × expand)

### 2. Hidden State Training Objectives

Standard self-supervised objectives (reconstruction, contrastive) fail to train long-range memory. Use **multi-stage training**:

**Stage 1: Local dependency learning**
```python
# Short-range reconstruction
loss_local = F.mse_loss(model(x_short), x_short)
```

**Stage 2: Long-range dependency injection**
```python
# Predict distant future from current hidden state
h_current = model.get_hidden_state(x[:t])
prediction = model.predict_from_state(h_current, horizon=T)
loss_long = F.mse_loss(prediction, x[t:t+T])
```

**Stage 3: Memory retention verification**
```python
# Gap prediction: predict after long silent period
h_before_gap = model.get_hidden_state(x[:gap_start])
h_after_gap = model.process_gap(h_before_gap, gap_duration)
prediction = model.predict_from_state(h_after_gap, horizon)
loss_gap = F.mse_loss(prediction, x[gap_end:gap_end+horizon])
```

### 3. Streaming Inference Interface

```python
class StreamingInference:
    def __init__(self, model, buffer_size=1000):
        self.model = model
        self.buffer = []
        self.hidden_state = None
    
    def process_chunk(self, chunk):
        # Append to buffer
        self.buffer.append(chunk)
        
        # Process with current hidden state
        if self.hidden_state is None:
            output, self.hidden_state = self.model(chunk, return_state=True)
        else:
            output, self.hidden_state = self.model(
                chunk, 
                initial_state=self.hidden_state,
                return_state=True
            )
        
        return output
    
    def reset_state(self):
        self.hidden_state = None
        self.buffer.clear()
```

## Comparison vs Bidirectional

| Aspect | Bidirectional | Causal |
|--------|--------------|--------|
| Complexity | O(n) both ways | O(n) one way |
| Memory | Stores forward + backward | Forward only |
| Streaming | No (needs full sequence) | Yes |
| Training | Standard objectives work | Multi-stage needed |
| Suitability | Static data | Temporal streams |

**Cost savings**:
- Memory: 50% reduction (one direction)
- Computation: ~50% reduction for streaming
- Latency: Immediate (no buffering)

## Training Pipeline

```python
# Multi-stage training pattern
def train_causal_ssm(model, dataset, epochs_per_stage=10):
    
    # Stage 1: Local reconstruction
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
    for epoch in range(epochs_per_stage):
        for x in dataset:
            # x: (batch, short_seq_len, features)
            output = model(x)
            loss = F.mse_loss(output, x)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
    # Stage 2: Long-range prediction
    for epoch in range(epochs_per_stage):
        for x in dataset:
            t = x.shape[1] // 2  # split point
            h = model.encode(x[:t])  # get hidden state
            pred = model.decode(h, horizon=x[t:].shape[1])
            loss = F.mse_loss(pred, x[t:])
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
    # Stage 3: Gap handling (if applicable)
    for epoch in range(epochs_per_stage):
        for x_with_gap in dataset_with_gaps:
            # Process sequences with long silent periods
            loss = compute_gap_loss(model, x_with_gap)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
```

## Performance Benchmarks

**CaMBRAIN results** (EEG):
- Throughput: >10x vs bidirectional models
- Latency: <10ms per chunk (real-time capable)
- Accuracy: State-of-the-art on 3 EEG datasets
- Memory: Linear scaling with sequence length

**Expected benefits**:
- Real-time inference: Yes (streaming interface)
- Long-range context: Strong (multi-stage training)
- Variable length: Yes (no window constraints)

## Implementation Checklist

- [ ] Verify data exhibits causal temporal structure
- [ ] Select Mamba backbone with appropriate d_state
- [ ] Implement multi-stage training objectives
- [ ] Add streaming inference interface
- [ ] Test on long sequences (>1K timesteps)
- [ ] Benchmark vs bidirectional alternatives
- [ ] Profile memory and latency

## Pitfalls to Avoid

1. **Using bidirectional objectives**: Standard reconstruction fails for streaming
2. **Insufficient d_state**: Hidden state capacity limits long-range memory
3. **Fixed-length batching**: Prevents true streaming inference
4. **Ignoring gap handling**: Long silent periods break naive SSMs
5. **Skipping memory training**: Multi-stage objectives essential

## Code Resources

- Mamba official: https://github.com/state-spaces/mamba
- CaMBRAIN paper: arXiv 2605.28792
- Streaming patterns: See CaMBRAIN SKILL.md