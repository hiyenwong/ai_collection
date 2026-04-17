---
name: ember-hybrid-snn-llm-architecture
description: "EMBER (Experience-Modulated Biologically-inspired Emergent Reasoning) hybrid cognitive architecture combining LLM reasoning with spiking neural network memory and dynamics. Places SNN as the primary cognitive substrate with LLM for high-level reasoning. Activation: EMBER, hybrid SNN LLM, cognitive architecture, emergent reasoning, biologically-inspired AI."
---

# EMBER: Hybrid SNN-LLM Cognitive Architecture

## Description

EMBER (Experience-Modulated Biologically-inspired Emergent Reasoning) is a hybrid cognitive architecture that reorganizes the relationship between large language models (LLMs) and memory. Rather than augmenting an LLM with retrieval tools, EMBER places an LLM within a biologically-inspired spiking neural network (SNN) substrate that serves as the primary cognitive system, enabling autonomous cognitive behavior through learned SNN dynamics.

Based on research from arXiv:2604.12167v1 - "EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture" by William Savage.

## Activation Keywords

- EMBER
- hybrid SNN LLM
- cognitive architecture
- emergent reasoning
- biologically-inspired AI
- SNN substrate
- experience-modulated reasoning
- autonomous cognition
- spiking LLM hybrid
- 混合认知架构

## Tools Used

- `write`: Create EMBER architecture implementations
- `exec`: Run SNN simulations and LLM inference
- `read`: Load configuration and memory states
- `patch`: Update network weights and connections

## Core Architecture

### 1. SNN as Cognitive Substrate

The SNN serves as the primary cognitive system:
- **Neural population**: Distributed representation of concepts and experiences
- **Dynamic attractors**: Learned stable states representing memories
- **Online learning**: Continuous adaptation from experience
- **Emergent behavior**: Complex cognition from simple neuron dynamics

### 2. LLM Integration

LLM operates within the SNN substrate:
- **Query interface**: LLM queries SNN for context
- **Output modulation**: SNN dynamics modulate LLM generation
- **Experience injection**: SNN states inform LLM reasoning
- **Feedback loop**: LLM outputs update SNN connections

### 3. Experience Modulation

Learning and adaptation mechanisms:
- **Spike-timing dependent plasticity (STDP)**: Hebbian learning from experience
- **Neuromodulation**: Simulated dopamine/serotonin for reinforcement
- **Structural plasticity**: Dynamic synaptic rewiring
- **Homeostasis**: Activity regulation for stability

## Implementation

### Step 1: SNN Cognitive Substrate

```python
import torch
import torch.nn as nn
import numpy as np

class SNNCognitiveSubstrate(nn.Module):
    """
    Spiking Neural Network serving as cognitive substrate.
    
    Architecture:
    - Input layer: Encodes sensory/linguistic inputs
    - Associative layer: Distributed concept representations  
    - Memory layer: Long-term experience storage
    - Output layer: Action/decision generation
    """
    
    def __init__(self, input_dim=512, assoc_dim=2048, memory_dim=4096, output_dim=512):
        super().__init__()
        
        self.input_dim = input_dim
        self.assoc_dim = assoc_dim
        self.memory_dim = memory_dim
        self.output_dim = output_dim
        
        # Network structure
        self.W_input_assoc = nn.Parameter(torch.randn(input_dim, assoc_dim) * 0.1)
        self.W_assoc_memory = nn.Parameter(torch.randn(assoc_dim, memory_dim) * 0.1)
        self.W_memory_assoc = nn.Parameter(torch.randn(memory_dim, assoc_dim) * 0.1)
        self.W_assoc_output = nn.Parameter(torch.randn(assoc_dim, output_dim) * 0.1)
        
        # Recurrent connections for attractor dynamics
        self.W_assoc_rec = nn.Parameter(torch.randn(assoc_dim, assoc_dim) * 0.01)
        self.W_memory_rec = nn.Parameter(torch.randn(memory_dim, memory_dim) * 0.01)
        
        # Neuromodulatory signals
        self.dopamine = 0.0
        self.serotonin = 0.0
        
        # State variables
        self.assoc_spikes = None
        self.assoc_potential = None
        self.memory_spikes = None
        self.memory_potential = None
        
    def reset_states(self, batch_size=1):
        """Reset neuron states."""
        device = self.W_input_assoc.device
        self.assoc_potential = torch.zeros(batch_size, self.assoc_dim, device=device)
        self.assoc_spikes = torch.zeros(batch_size, self.assoc_dim, device=device)
        self.memory_potential = torch.zeros(batch_size, self.memory_dim, device=device)
        self.memory_spikes = torch.zeros(batch_size, self.memory_dim, device=device)
    
    def forward(self, input_pattern, steps=100, dt=1.0):
        """
        Run SNN dynamics with input pattern.
        
        Args:
            input_pattern: Input activation pattern (batch, input_dim)
            steps: Number of simulation steps
            dt: Time step
        
        Returns:
            output_pattern: Output activation (batch, output_dim)
            states: Record of network states
        """
        batch_size = input_pattern.shape[0]
        if self.assoc_potential is None:
            self.reset_states(batch_size)
        
        # Neuron parameters
        tau_m = 20.0
        v_thresh = 1.0
        v_rest = 0.0
        
        # Record states
        assoc_spikes_history = []
        memory_spikes_history = []
        
        for step in range(steps):
            # Input to associative layer
            input_current = torch.matmul(input_pattern, self.W_input_assoc)
            
            # Recurrent associative dynamics
            rec_current = torch.matmul(self.assoc_spikes, self.W_assoc_rec)
            
            # Memory feedback
            memory_feedback = torch.matmul(self.memory_spikes, self.W_memory_assoc.T)
            
            total_current = input_current + rec_current + memory_feedback
            
            # Update associative layer
            dv = (-(self.assoc_potential - v_rest) + total_current) * dt / tau_m
            self.assoc_potential = self.assoc_potential + dv
            
            # Spike generation
            self.assoc_spikes = (self.assoc_potential >= v_thresh).float()
            self.assoc_potential = self.assoc_potential * (1 - self.assoc_spikes) + v_rest * self.assoc_spikes
            
            # Associative to memory
            memory_input = torch.matmul(self.assoc_spikes, self.W_assoc_memory)
            mem_rec = torch.matmul(self.memory_spikes, self.W_memory_rec)
            
            # Update memory layer
            dv_mem = (-(self.memory_potential - v_rest) + memory_input + mem_rec) * dt / tau_m
            self.memory_potential = self.memory_potential + dv_mem
            
            self.memory_spikes = (self.memory_potential >= v_thresh).float()
            self.memory_potential = self.memory_potential * (1 - self.memory_spikes) + v_rest * self.memory_spikes
            
            # Record
            assoc_spikes_history.append(self.assoc_spikes.clone())
            memory_spikes_history.append(self.memory_spikes.clone())
        
        # Generate output from associative layer
        output_pattern = torch.matmul(self.assoc_spikes, self.W_assoc_output)
        
        states = {
            'assoc_spikes': torch.stack(assoc_spikes_history),
            'memory_spikes': torch.stack(memory_spikes_history),
            'final_assoc': self.assoc_spikes,
            'final_memory': self.memory_spikes
        }
        
        return output_pattern, states
    
    def stdp_update(self, pre_spikes, post_spikes, learning_rate=0.001):
        """
        Apply spike-timing dependent plasticity.
        
        Args:
            pre_spikes: Presynaptic spike train (time, batch, dim)
            post_spikes: Postsynaptic spike train (time, batch, dim)
            learning_rate: Learning rate
        """
        time_steps, batch_size, pre_dim = pre_spikes.shape
        _, _, post_dim = post_spikes.shape
        
        # Compute spike time differences
        weight_delta = torch.zeros(pre_dim, post_dim, device=pre_spikes.device)
        
        for t in range(time_steps):
            for t_pre in range(t):
                if torch.sum(pre_spikes[t_pre]) > 0 and torch.sum(post_spikes[t]) > 0:
                    dt = t - t_pre
                    # STDP window: potentiation for pre-before-post
                    delta = learning_rate * torch.exp(-dt / 20.0)
                    weight_delta += torch.matmul(
                        pre_spikes[t_pre].T, 
                        post_spikes[t]
                    ) * delta
        
        return weight_delta
    
    def apply_neuromodulation(self, reward, learning_rate=0.01):
        """
        Apply dopaminergic neuromodulation to learning.
        
        Args:
            reward: Reward signal (positive or negative)
            learning_rate: Base learning rate
        """
        # Update dopamine level
        self.dopamine = 0.9 * self.dopamine + 0.1 * reward
        
        # Modulate learning rate
        modulated_lr = learning_rate * (1 + self.dopamine)
        
        return modulated_lr


class ConceptRepresentation:
    """
    Distributed concept representation in SNN.
    """
    
    def __init__(self, substrate, concept_dim=256):
        self.substrate = substrate
        self.concept_dim = concept_dim
        self.concepts = {}
    
    def encode_concept(self, concept_name, initial_pattern):
        """
        Create distributed representation for a concept.
        
        Args:
            concept_name: Name of the concept
            initial_pattern: Initial activation pattern
        
        Returns:
            concept_id: ID for the learned concept
        """
        # Run network to stable attractor
        _, states = self.substrate(initial_pattern, steps=500)
        
        # Store final attractor state
        attractor_state = states['final_assoc'].mean(dim=0)
        
        self.concepts[concept_name] = {
            'attractor': attractor_state,
            'activation_pattern': states['final_assoc']
        }
        
        return concept_name
    
    def retrieve_concept(self, concept_name):
        """Retrieve concept representation."""
        if concept_name in self.concepts:
            return self.concepts[concept_name]['attractor']
        return None
```

### Step 2: LLM Integration Layer

```python
class LLMIntegrationLayer:
    """
    Interface between LLM and SNN substrate.
    """
    
    def __init__(self, llm_model, snn_substrate):
        self.llm = llm_model
        self.snn = snn_substrate
        
        # Token-to-pattern encoder
        self.token_encoder = TokenToPatternEncoder()
        
        # Pattern-to-token decoder
        self.pattern_decoder = PatternToTokenDecoder()
    
    def snn_guided_generation(self, prompt, max_tokens=100, temperature=0.7):
        """
        Generate text with SNN-guided context.
        
        Args:
            prompt: Input text prompt
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
        
        Returns:
            generated_text: Generated text
            snn_context: SNN activation context
        """
        # Encode prompt to SNN input
        prompt_pattern = self.token_encoder.encode(prompt)
        
        # Run SNN to get context
        output_pattern, states = self.snn(prompt_pattern, steps=200)
        
        # Extract relevant memories and concepts
        context_vector = self.extract_context(states)
        
        # Augment prompt with SNN context
        augmented_prompt = self.augment_prompt(prompt, context_vector)
        
        # Generate with LLM
        generated = self.llm.generate(
            augmented_prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        # Update SNN with generated output
        generated_pattern = self.token_encoder.encode(generated)
        self.update_snn_from_output(generated_pattern, states)
        
        return generated, states
    
    def extract_context(self, snn_states):
        """Extract meaningful context from SNN states."""
        # Pool spikes over time and neurons
        assoc_activity = snn_states['assoc_spikes'].mean(dim=(0, 1))  # Average over time and batch
        memory_activity = snn_states['memory_spikes'].mean(dim=(0, 1))
        
        # Identify active concepts (high-activity neurons)
        active_concepts = torch.where(assoc_activity > assoc_activity.mean() + assoc_activity.std())[0]
        
        context = {
            'active_concepts': active_concepts,
            'assoc_activity': assoc_activity,
            'memory_activity': memory_activity
        }
        
        return context
    
    def augment_prompt(self, prompt, context):
        """Augment prompt with SNN context."""
        # Convert active concepts to text descriptions
        concept_descriptions = []
        for concept_id in context['active_concepts'][:5]:  # Top 5 concepts
            desc = f"[Concept {concept_id}: active]"
            concept_descriptions.append(desc)
        
        # Insert into prompt
        context_str = "Relevant context: " + ", ".join(concept_descriptions) + "\n\n"
        augmented = context_str + prompt
        
        return augmented
    
    def update_snn_from_output(self, output_pattern, previous_states):
        """
        Update SNN weights based on LLM output.
        Uses STDP between input and output patterns.
        """
        # Get pre and post spike patterns
        pre_spikes = previous_states['assoc_spikes']
        post_spikes = output_pattern.unsqueeze(0).expand(pre_spikes.shape[0], -1, -1)
        
        # Apply STDP
        weight_delta = self.snn.stdp_update(pre_spikes, post_spikes)
        
        # Update weights
        with torch.no_grad():
            self.snn.W_assoc_output.data += weight_delta.T * 0.001


class TokenToPatternEncoder:
    """Encode text tokens to SNN input patterns."""
    
    def __init__(self, vocab_size=50000, pattern_dim=512):
        self.vocab_size = vocab_size
        self.pattern_dim = pattern_dim
        
        # Learnable embedding
        self.embedding = nn.Embedding(vocab_size, pattern_dim)
    
    def encode(self, text):
        """Encode text to activation pattern."""
        # Tokenize (simplified - use actual tokenizer in practice)
        tokens = self.tokenize(text)
        
        # Get embeddings
        embeddings = self.embedding(tokens)
        
        # Average pooling
        pattern = embeddings.mean(dim=0)
        
        # Normalize
        pattern = pattern / (pattern.norm() + 1e-8)
        
        return pattern.unsqueeze(0)  # Add batch dimension
    
    def tokenize(self, text):
        # Simplified tokenization - use actual tokenizer
        tokens = torch.tensor([hash(word) % self.vocab_size for word in text.split()])
        return tokens


class PatternToTokenDecoder:
    """Decode SNN patterns to text tokens."""
    
    def __init__(self, pattern_dim=512, vocab_size=50000):
        self.pattern_dim = pattern_dim
        self.vocab_size = vocab_size
        
        self.decoder = nn.Linear(pattern_dim, vocab_size)
    
    def decode(self, pattern):
        """Decode pattern to token probabilities."""
        logits = self.decoder(pattern)
        probs = torch.softmax(logits, dim=-1)
        return probs
```

### Step 3: Experience Learning

```python
class ExperienceLearning:
    """
    Online learning from experience with neuromodulation.
    """
    
    def __init__(self, substrate):
        self.substrate = substrate
        self.experience_buffer = []
        
    def store_experience(self, input_pattern, output_pattern, reward):
        """
        Store experience for later learning.
        
        Args:
            input_pattern: Input activation
            output_pattern: Output activation
            reward: Reward signal
        """
        experience = {
            'input': input_pattern.detach(),
            'output': output_pattern.detach(),
            'reward': reward
        }
        self.experience_buffer.append(experience)
        
        # Keep buffer size manageable
        if len(self.experience_buffer) > 1000:
            self.experience_buffer.pop(0)
    
    def learn_from_experience(self, batch_size=32):
        """
        Perform learning updates from stored experiences.
        """
        if len(self.experience_buffer) < batch_size:
            return
        
        # Sample experiences
        batch = np.random.choice(self.experience_buffer, batch_size, replace=False)
        
        for exp in batch:
            # Run network forward
            _, states = self.substrate(exp['input'], steps=100)
            
            # Compute reward prediction error
            predicted_reward = self.predict_reward(states['final_assoc'])
            reward_error = exp['reward'] - predicted_reward
            
            # Apply neuromodulation
            modulated_lr = self.substrate.apply_neuromodulation(reward_error)
            
            # Update weights based on reward
            if reward_error > 0:  # Positive surprise
                self.potentiate_connections(exp['input'], states, modulated_lr)
            else:
                self.depress_connections(exp['input'], states, modulated_lr)
    
    def predict_reward(self, state):
        """Predict expected reward from state."""
        # Simple reward prediction - can be learned
        return torch.mean(state)
    
    def potentiate_connections(self, input_pattern, states, learning_rate):
        """Strengthen relevant connections."""
        # STDP-based potentiation
        pass
    
    def depress_connections(self, input_pattern, states, learning_rate):
        """Weaken irrelevant connections."""
        # STDP-based depression
        pass
```

### Step 4: Complete EMBER System

```python
class EMBERSystem:
    """
    Complete EMBER cognitive architecture.
    """
    
    def __init__(self, llm_model, config=None):
        # Initialize SNN substrate
        self.substrate = SNNCognitiveSubstrate(
            input_dim=config.get('input_dim', 512),
            assoc_dim=config.get('assoc_dim', 2048),
            memory_dim=config.get('memory_dim', 4096),
            output_dim=config.get('output_dim', 512)
        )
        
        # Initialize LLM integration
        self.llm_layer = LLMIntegrationLayer(llm_model, self.substrate)
        
        # Initialize experience learning
        self.learner = ExperienceLearning(self.substrate)
        
        # Concept memory
        self.concepts = ConceptRepresentation(self.substrate)
        
    def process(self, input_text, mode='reasoning'):
        """
        Process input through EMBER system.
        
        Args:
            input_text: Input text
            mode: 'reasoning', 'memory', or 'creative'
        
        Returns:
            response: System output
            internal_states: Internal processing states
        """
        if mode == 'reasoning':
            response, states = self.llm_layer.snn_guided_generation(input_text)
        elif mode == 'memory':
            response, states = self.memory_retrieval(input_text)
        elif mode == 'creative':
            response, states = self.creative_generation(input_text)
        
        # Learn from experience
        reward = self.compute_intrinsic_reward(states)
        input_pattern = self.llm_layer.token_encoder.encode(input_text)
        output_pattern = self.llm_layer.token_encoder.encode(response)
        self.learner.store_experience(input_pattern, output_pattern, reward)
        
        return response, states
    
    def memory_retrieval(self, query):
        """Retrieve relevant memories."""
        # Encode query
        query_pattern = self.llm_layer.token_encoder.encode(query)
        
        # Run SNN to activate related memories
        _, states = self.substrate(query_pattern, steps=300)
        
        # Extract memory content
        memory_activity = states['memory_spikes']
        
        # Decode to text
        response = "Retrieved memory patterns..."
        
        return response, states
    
    def creative_generation(self, prompt):
        """Generate creative output with SNN exploration."""
        # Encode prompt
        prompt_pattern = self.llm_layer.token_encoder.encode(prompt)
        
        # Run with higher temperature (more exploration)
        _, states = self.substrate(prompt_pattern, steps=200)
        
        # Generate with LLM using creative context
        response, _ = self.llm_layer.snn_guided_generation(
            prompt, 
            temperature=0.9
        )
        
        return response, states
    
    def compute_intrinsic_reward(self, states):
        """Compute intrinsic reward for learning."""
        # Novelty-based reward
        activity = states['assoc_spikes'].mean()
        
        # Higher activity = more novel/interesting
        reward = activity.item() - 0.5  # Center around 0
        
        return reward
```

## Usage Patterns

### Pattern 1: Autonomous Reasoning

```python
# Initialize EMBER
ember = EMBERSystem(llm_model)

# Process query with autonomous reasoning
response, states = ember.process(
    "Explain the concept of emergence in complex systems",
    mode='reasoning'
)

# System automatically updates from experience
ember.learner.learn_from_experience(batch_size=32)
```

### Pattern 2: Memory-Augmented Conversation

```python
# Multi-turn conversation with memory
conversation_history = []

for turn in conversation:
    # Process with memory context
    response, states = ember.process(turn['input'])
    
    # Store in conversation memory
    conversation_history.append({
        'input': turn['input'],
        'response': response,
        'states': states
    })
    
    # Periodic consolidation
    if len(conversation_history) % 10 == 0:
        ember.consolidate_memories()
```

### Pattern 3: Concept Learning

```python
# Learn new concepts
ember.concepts.encode_concept(
    "neural plasticity",
    initial_pattern=ember.llm_layer.token_encoder.encode(
        "Neural plasticity is the ability of neural circuits to change..."
    )
)

# Retrieve concept
plasticity_concept = ember.concepts.retrieve_concept("neural plasticity")
```

## Error Handling

### SNN Instability

If SNN dynamics become unstable:
1. Check recurrent connection weights (should be small)
2. Verify homeostatic mechanisms are active
3. Reduce time step
4. Increase membrane time constants

### LLM Misalignment

If LLM output doesn't match SNN context:
1. Verify token encoder/decoder alignment
2. Check context augmentation format
3. Ensure SNN has sufficient simulation steps
4. Validate pattern dimensions

### Learning Failures

If learning doesn't improve performance:
1. Check reward signal quality
2. Verify STDP parameters
3. Ensure sufficient experience samples
4. Review neuromodulation levels

## References

- Savage, W. (2026). EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture. arXiv:2604.12167v1.
- Maass, W. (1997). Networks of spiking neurons: the third generation of neural network models. Neural Networks.
- Zenke, F., & Ganguli, S. (2018). Superspike: Supervised learning in multi-layer spiking neural networks. Neural Computation.

## Related Skills

- `brain-digital-twins-execution-semantics`: Execution semantics framework
- `adaptive-spiking-neurons-vision`: Adaptive spiking neurons
- `agent-memory-framework`: Memory-augmented agent design


## Paper Reference (Updated 2026-04-17)
- **Title**: EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture
- **arXiv ID**: 2604.12167
- **Date**: 2026-04-14
- **Authors**: William Savage
- **Categories**: cs.AI, cs.NE
