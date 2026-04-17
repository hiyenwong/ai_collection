# EMBER: Hybrid SNN-LLM Architecture — Implementation Patterns

## 1. SNN Core Setup

```python
# Four-layer hierarchical SNN with E/I balance
class EMBERSNN:
    """
    220,000-neuron SNN with hierarchical organization.
    
    Layers:
    - Sensory: Input encoding layer
    - Concept: Feature abstraction layer
    - Category: Semantic grouping layer
    - Meta-pattern: Cross-concept association layer
    """
    def __init__(self, n_neurons=220_000):
        self.layers = {
            'sensory': int(n_neurons * 0.40),    # ~88,000
            'concept': int(n_neurons * 0.30),     # ~66,000
            'category': int(n_neurons * 0.20),    # ~44,000
            'meta_pattern': int(n_neurons * 0.10) # ~22,000
        }
        # E/I balance: ~80% excitatory, ~20% inhibitory
        self.ei_ratio = 0.8
        # STDP parameters
        self.stdp_tau_plus = 20.0   # ms
        self.stdp_tau_minus = 20.0  # ms
        self.stdp_eta = 0.01        # learning rate
```

## 2. Z-Score Standardized Top-K Population Encoding

```python
import numpy as np

def zscore_topk_encode(embedding: np.ndarray, k: int = 10, n_neurons: int = 1000) -> np.ndarray:
    """
    Dimension-independent population encoding of text embeddings.
    Achieves 82.2% discrimination retention across embedding dimensionalities.
    
    Args:
        embedding: Input text embedding vector (any dimensionality)
        k: Number of top neurons to activate
        n_neurons: Size of population code
        
    Returns:
        Spike pattern vector of length n_neurons
    """
    # Z-score standardize the embedding
    z_scores = (embedding - embedding.mean()) / (embedding.std() + 1e-8)
    
    # Project to neuron population via random projection
    projection = np.random.randn(len(z_scores), n_neurons)
    activation = z_scores @ projection
    
    # Z-score again on the projected space
    activation = (activation - activation.mean()) / (activation.std() + 1e-8)
    
    # Top-k activation
    spike_pattern = np.zeros(n_neurons)
    top_indices = np.argsort(activation)[-k:]
    spike_pattern[top_indices] = 1.0
    
    return spike_pattern
```

## 3. STDP with Reward Modulation

```python
def stdp_update(weights, pre_spikes, post_spikes, reward=0.0,
                tau_plus=20.0, tau_minus=20.0, eta=0.01):
    """
    Spike-timing-dependent plasticity with reward modulation.
    
    Potentiation: pre before post → strengthen
    Depression: post before pre → weaken
    Reward scales the magnitude of updates.
    """
    # Pre-synaptic trace
    pre_trace = np.exp(-np.abs(np.arange(len(pre_spikes))) / tau_plus)
    post_trace = np.exp(-np.abs(np.arange(len(post_spikes))) / tau_minus)
    
    # Hebbian update
    delta_w = eta * (np.outer(post_spikes, pre_trace) - 
                     np.outer(post_trace, pre_spikes))
    
    # Reward modulation
    delta_w *= (1.0 + reward)
    
    return weights + delta_w
```

## 4. Idle-Period Lateral Propagation and LLM Triggering

```python
class EmberController:
    """Manages SNN idle operation and LLM triggering."""
    
    def __init__(self, snn, llm, action_threshold=0.7):
        self.snn = snn
        self.llm = llm
        self.action_threshold = action_threshold
        self.association_buffer = []
    
    def run_idle_period(self, duration_hours=8.0):
        """
        Run SNN during idle period. STDP lateral propagation
        can trigger and shape LLM actions without external prompting.
        """
        steps = int(duration_hours * 3600 * 1000)  # ms
        for t in range(steps):
            self.snn.step()  # SNN dynamics with STDP
            
            # Check for lateral propagation patterns
            association_strength = self.snn.get_lateral_association()
            self.association_buffer.append(association_strength)
            
            if association_strength > self.action_threshold:
                return self._trigger_llm()
        
        return None
    
    def _trigger_llm(self):
        """Surface SNN associations to LLM for action selection."""
        associations = self.snn.get_active_associations()
        # LLM selects action type and generates content
        action = self.llm.generate(
            context=associations,
            prompt="Based on these associations, what action should be taken?"
        )
        return action
```

## 5. Training Loop

```python
def train_ember(snn, conversations, n_exchanges=7):
    """
    Train EMBER from cold start.
    First SNN-triggered action occurs after ~7 conversational exchanges (14 messages).
    """
    exchange_count = 0
    for msg in conversations:
        # Encode message into SNN
        pattern = zscore_topk_encode(msg.embedding, n_neurons=1000)
        snn.inject(pattern)
        
        # Run SNN dynamics with STDP
        snn.step()
        
        exchange_count += 1
        
        if exchange_count >= n_exchanges:
            # Check for autonomous action trigger
            action = snn.check_action_threshold()
            if action:
                print(f"SNN triggered action after {exchange_count} exchanges")
                return action
```

## References

- Paper: EMBER (2604.12167v1)
- STDP: Bi and Poo (2001), "Synaptic Modification by Correlated Activity"
- Population coding: Georgopoulos et al. (1986), "Neuronal Population Coding of Movement Direction"
