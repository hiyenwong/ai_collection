# SKILL.md - Leabra7 Biologically Realistic Neural Networks

## Activation Keywords

- Leabra7, LEABRA, biologically realistic neural networks
- AdEx model, emergent, recurrent neural networks
- local error-driven learning, biological neural simulation
- O'Reilly learning algorithm, biological RNN

## What It Does

Leabra7 is a Python package for simulating recurrent, biologically-realistic neural networks using the AdEx neural dynamics model and LEABRA (Local, Error-driven and Associative, Biologically Realistic Algorithm) learning algorithm. Provides quantitative equivalence with the Emergent simulation platform.

## When To Use

**Use this skill when:**
- Building biologically realistic neural network models
- Simulating recurrent neural circuits
- Implementing LEABRA learning algorithm
- Modeling cortical processing with biological constraints
- Comparing biological vs artificial neural networks

**Do NOT use for:**
- Standard deep learning (no biological realism needed)
- Simple feedforward networks (recurrence not required)
- Non-biological neural models (use PyTorch/TensorFlow)

## How To Use

### Step-by-Step Workflow

1. **Install Leabra7**
   ```bash
   pip install leabra7
   ```

2. **Define Network Architecture**
   - Specify layers (input, hidden, output)
   - Configure AdEx neuron parameters
   - Set up connectivity patterns

3. **Configure LEABRA Learning**
   - Local error-driven learning (XCAL)
   - Associative learning (Hebbian)
   - Balance between error-driven and associative

4. **Run Simulation**
   - Present input patterns
   - Run settling cycles
   - Apply learning rules
   - Collect outputs

5. **Analyze Results**
   - Compare with Emergent results
   - Validate biological plausibility
   - Test on cognitive tasks

### Key Components

| Component | Description | Parameters |
|-----------|-------------|------------|
| AdEx neuron | Adaptive exponential integrate-and-fire | τ_m, C_m, V_t, Δ_t |
| LEABRA learning | Local error + Hebbian | lrate, xcal_thresh |
| Inhibition | kWTA (k-winners-take-all) | k, g_bar_i |
| Settling | Iterative activation update | cycles, dt |

### AdEx Model Equations

**Membrane dynamics:**
```
C_m dV/dt = -g_L(V - E_L) + g_LΔ_t exp((V - V_t)/Δ_t) - w + I
τ_w dw/dt = a(V - E_L) - w
```

**Spike:**
```
if V > V_peak: V → V_reset, w → w + b
```

## Example Usage

### Basic Network Setup

```python
import leabra7 as lb

# Create network
net = lb.Network()

# Add layers
net.new_layer('input', size=10)
net.new_layer('hidden', size=20)
net.new_layer('output', size=5)

# Add connections
net.new_projn('input_to_hidden', 'input', 'hidden')
net.new_projn('hidden_to_output', 'hidden', 'output')

# Configure layers
net.configure_layer('hidden', 
    kwta_pct=0.25,  # 25% active
    g_bar_e=0.5,    # excitatory conductance
    g_bar_i=1.0)    # inhibitory conductance
```

### Training with LEABRA

```python
def train_leabra_network(net, inputs, targets, epochs=100):
    """
    Train network using LEABRA learning algorithm
    """
    for epoch in range(epochs):
        for inp, target in zip(inputs, targets):
            # Clamp input
            net.clamp_layer('input', inp)
            
            # Optionally clamp output for error-driven learning
            net.clamp_layer('output', target)
            
            # Settling phase
            net.settle(cycles=50)
            
            # Apply LEABRA learning
            net.learn()
            
            # Unclamp for testing
            net.unclamp_layer('output')
    
    return net
```

### Testing Pattern Completion

```python
def test_pattern_completion(net, partial_pattern):
    """
    Test network's ability to complete partial patterns
    """
    # Clamp partial input
    net.clamp_layer('input', partial_pattern)
    
    # Let network settle
    net.settle(cycles=100)
    
    # Read output
    output = net.get_output('output')
    
    return output
```

## LEABRA Algorithm Details

### Learning Rule

LEABRA combines:
1. **Error-driven learning** (XCAL - eXtended Contrastive Attenion Learning)
   - Compare minus (expectation) vs plus (outcome) phases
   - Error signal: δ = (w_plus - w_minus)

2. **Associative learning** (Hebbian)
   - Co-occurrence of pre and post activity
   - Strengthens frequently co-active connections

3. **Balance**: `Δw = err_weight * error + hebb_weight * hebbian`

### kWTA Inhibition

k-Winners-Take-All enforces sparse coding:
- Top k units remain active
- Others inhibited
- Creates competition, sparse representations

## Comparison with Standard Deep Learning

| Aspect | Leabra7 | Standard DL |
|--------|---------|-------------|
| Neuron model | AdEx (biological) | ReLU (abstract) |
| Learning | Local + Hebbian | Backprop (global) |
| Inhibition | kWTA (biological) | None or softmax |
| Recurrence | Native | RNN variants |
| Sparsity | Built-in | Requires regularization |

## Description
Framework from arXiv papers. See paper reference for details.
## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply leabra7-biological-neural-networks?

**Agent:** I'll help you understand and apply leabra7-biological-neural-networks...

### Example 2: Advanced Application

**User:** What are the key considerations for leabra7-biological-neural-networks?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **bio-neuron-snn-learning** - Biological neuron SNN learning
- **spiking-mode-neural-networks** - Spiking neural networks
- **decolle-snn-learning** - DECOLLE learning

## Source

- arXiv:1809.04166v2
- Title: Leabra7: a Python package for modeling recurrent, biologically-realistic neural networks
- Utility: 0.87
- Authors: Greenidge, Miller
- GitHub: https://github.com/PrincetonUniversity/leabra7
- Docs: https://leabra7.readthedocs.io

## Notes

- Python implementation of Emergent's LEABRA algorithm
- Targets quantitative equivalence with emergent71 branch
- Uses AdEx (Adaptive Exponential) neuron model
- Combines local error-driven and associative (Hebbian) learning
- Native recurrence and kWTA inhibition
- Good for cognitive modeling and biological simulation
- Alternative to backprop-based learning

---

_Created: 2026-04-01_