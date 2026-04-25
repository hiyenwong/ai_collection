---
name: context-selective-multimodal-memory
description: "Human-inspired context-selective multimodal memory architecture for embodied agents and social robots. Features hippocampal-inspired indexing for efficient retrieval and cortical consolidation for long-term storage. Captures both textual context and non-verbal behavioral cues for personalized, context-aware interactions. Activation: multimodal memory, context-selective, hippocampal indexing, cortical consolidation, social robots, embodied ai memory."
---

# Context-Selective Multimodal Memory for Embodied Agents

## Overview

This memory architecture draws inspiration from **cognitive neuroscience** to create a **context-selective, multimodal memory** for social robots and embodied agents. Unlike traditional text-based memory systems, it captures and retrieves both **textual context** and **non-verbal behavioral cues**, enabling personalized, context-aware interactions.

**Core Innovation**: Biologically-grounded memory hierarchy combining hippocampal-inspired fast indexing with cortical-inspired stable consolidation.

## Key Features

### 1. Hippocampal-Inspired Indexing
- **Fast Encoding**: Rapid storage of new experiences
- **Pattern Separation**: Distinguish similar contexts
- **Episodic Memory**: Event-specific memories with temporal context

### 2. Cortical Consolidation
- **Stable Storage**: Long-term memory formation
- **Semantic Extraction**: Generalize from specific instances
- **System Integration**: Connect with existing knowledge

### 3. Multimodal Representation
- **Text**: Conversational content, semantic meaning
- **Visual**: Facial expressions, gestures, environment
- **Audio**: Tone, prosody, emotional content
- **Temporal**: Timing, duration, sequence

### 4. Context-Selective Retrieval
- **Context Matching**: Find memories relevant to current situation
- **Selective Attention**: Filter out irrelevant information
- **Adaptive Weighting**: Prioritize by relevance and recency

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│         Context-Selective Multimodal Memory                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Input Modalities                                               │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │   Text   │ │  Visual  │ │  Audio   │ │ Temporal │          │
│  │(utterance)│ │ (faces)  │ │  (tone)  │ │  (time)  │          │
│  └─────┬────┘ └─────┬────┘ └─────┬────┘ └─────┬────┘          │
│        │            │            │            │                │
│        └────────────┴────────────┴────────────┘                │
│                     │                                           │
│                     ▼                                           │
│        ┌──────────────────────┐                                │
│        │  Multimodal          │                                │
│        │  Encoder             │                                │
│        │  (CLIP-style fusion) │                                │
│        └──────────┬───────────┘                                │
│                   │                                             │
│                   ▼                                             │
│        ┌──────────────────────┐                                │
│        │  Hierarchical        │                                │
│        │  Memory System       │                                │
│        ├──────────────────────┤                                │
│        │                      │                                │
│        │  ┌────────────────┐  │                                │
│        │  │   Hippocampal  │  │  ← Fast, Episodic             │
│        │  │   Index        │  │  ← Pattern separation         │
│        │  │                │  │  ← Context binding            │
│        │  └────────────────┘  │                                │
│        │           │          │                                │
│        │           ▼          │                                │
│        │  ┌────────────────┐  │                                │
│        │  │   Consolidation│  │  ← Sleep/replay               │
│        │  │   (Sleep-like) │  │  ← Replay sequences           │
│        │  └────────────────┘  │                                │
│        │           │          │                                │
│        │           ▼          │                                │
│        │  ┌────────────────┐  │                                │
│        │  │   Cortical     │  │  ← Stable, Semantic           │
│        │  │   Memory       │  │  ← Generalized knowledge      │
│        │  │                │  │  ← Long-term storage          │
│        │  └────────────────┘  │                                │
│        │                      │                                │
│        └──────────────────────┘                                │
│                   │                                             │
│                   ▼                                             │
│        ┌──────────────────────┐                                │
│        │  Context-Selective   │                                │
│        │  Retrieval           │                                │
│        │  - Query encoding    │                                │
│        │  - Similarity search │                                │
│        │  - Attention weight  │                                │
│        └──────────┬───────────┘                                │
│                   │                                             │
│                   ▼                                             │
│        ┌──────────────────────┐                                │
│        │  Retrieved Memory    │                                │
│        └──────────────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Memory Formation Process

### Step 1: Multimodal Encoding

```python
from multimodal_memory import MultimodalEncoder

# Initialize encoder
encoder = MultimodalEncoder(
    text_model='sentence-transformers/all-MiniLM-L6-v2',
    visual_model='clip-vit-base-patch32',
    audio_model='wav2vec2-base',
    fusion_dim=512
)

# Encode an interaction
interaction = {
    'text': "User seemed happy about the recommendation",
    'visual': load_image('user_expression.jpg'),  # Smiling face
    'audio': load_audio('user_response.wav'),     # Cheerful tone
    'timestamp': datetime.now(),
    'context': {'location': 'kitchen', 'activity': 'cooking'}
}

# Create multimodal embedding
multimodal_embedding = encoder.encode(interaction)
print(f"Memory embedding shape: {multimodal_embedding.shape}")
# Output: (512,) - fused representation
```

### Step 2: Hippocampal Indexing

```python
from multimodal_memory import HippocampalIndex

# Initialize hippocampal index
hippocampus = HippocampalIndex(
    index_dim=512,
    pattern_separation=0.3,  # Higher = more distinct memories
    capacity=10000
)

# Store in episodic memory
memory_id = hippocampus.store(
    embedding=multimodal_embedding,
    episode=interaction,
    context_tags=['positive', 'recommendation', 'kitchen']
)

print(f"Memory stored with ID: {memory_id}")
```

### Step 3: Context Binding

```python
# Bind memory to contextual cues
hippocampus.bind_context(
    memory_id=memory_id,
    contexts={
        'spatial': 'kitchen',
        'temporal': 'evening',
        'emotional': 'positive',
        'social': 'friendly_interaction'
    }
)
```

### Step 4: Consolidation (Sleep-like)

```python
from multimodal_memory import CorticalConsolidation

# Initialize cortical memory
cortex = CorticalConsolidation(
    semantic_dim=512,
    knowledge_graph=True
)

# Trigger consolidation (periodically)
# This mimics sleep-dependent memory consolidation
def consolidate_memories():
    # Get recent episodic memories
    recent_memories = hippocampus.get_recent(hours=24)
    
    # Replay and consolidate
    for memory in recent_memories:
        # Extract semantic content
        semantic_memory = cortex.extract_semantics(memory)
        
        # Integrate with existing knowledge
        cortex.integrate(semantic_memory)
        
        # Strengthen hippocampal-cortical connections
        hippocampus.strengthen(memory['id'])

# Run consolidation nightly
consolidate_memories()
```

## Context-Selective Retrieval

### Step 1: Query Encoding

```python
# Current situation
current_context = {
    'text': "User is asking about dinner recommendations",
    'visual': load_image('current_scene.jpg'),
    'context': {'location': 'kitchen', 'time': 'evening'}
}

# Encode query
query_embedding = encoder.encode(current_context)
```

### Step 2: Similarity Search

```python
# Search hippocampal index
candidates = hippocampus.retrieve(
    query=query_embedding,
    context_filter={'location': 'kitchen'},  # Context constraint
    k=10  # Top-10 candidates
)

print(f"Retrieved {len(candidates)} candidate memories")
```

### Step 3: Context Matching

```python
# Score by context relevance
def score_context_relevance(memory, current_context):
    scores = []
    
    # Spatial match
    if memory['context']['location'] == current_context['context']['location']:
        scores.append(1.0)
    else:
        scores.append(0.0)
    
    # Temporal match
    if memory['context']['time'] == current_context['context']['time']:
        scores.append(1.0)
    else:
        scores.append(0.5)
    
    # Emotional match
    text_similarity = cosine_similarity(
        memory['embedding'],
        current_context['embedding']
    )
    scores.append(text_similarity)
    
    return np.mean(scores)

# Score candidates
scored_candidates = [
    (memory, score_context_relevance(memory, current_context))
    for memory in candidates
]

# Sort by relevance
scored_candidates.sort(key=lambda x: x[1], reverse=True)
```

### Step 4: Selective Attention

```python
# Apply selective attention (softmax over scores)
scores = torch.tensor([s[1] for s in scored_candidates])
attention_weights = F.softmax(scores / temperature, dim=0)

# Retrieve most relevant memories
retrieved_memories = []
for i, ((memory, score), weight) in enumerate(zip(scored_candidates, attention_weights)):
    if weight > threshold:  # Only keep significant memories
        memory['attention_weight'] = weight.item()
        memory['relevance_score'] = score
        retrieved_memories.append(memory)

print(f"Selected {len(retrieved_memories)} relevant memories")
for m in retrieved_memories:
    print(f"  - Relevance: {m['relevance_score']:.2f}, Weight: {m['attention_weight']:.3f}")
```

## Using Retrieved Memories

```python
from multimodal_memory import MemoryIntegrator

# Integrate memories into response
integrator = MemoryIntegrator()

# Generate context-aware response
response = integrator.generate_response(
    query=current_context['text'],
    retrieved_memories=retrieved_memories,
    policy='balanced'  # balanced, conservative, or liberal
)

print(f"Agent: {response}")
# Output might include:
# "Based on your previous positive reaction to recommendations in the kitchen,
#  you might enjoy trying the pasta recipe I suggested before."
```

## Implementation Details

### Hippocampal Pattern Separation

```python
class HippocampalIndex:
    """Hippocampal-inspired fast indexing with pattern separation."""
    
    def __init__(self, index_dim, pattern_separation=0.3):
        self.index_dim = index_dim
        self.separation = pattern_separation
        self.memories = {}
        self.index = faiss.IndexFlatIP(index_dim)  # Inner product index
        
    def store(self, embedding, episode, context_tags):
        # Apply pattern separation (Dentate Gyrus-like)
        separated = self.separate_patterns(embedding)
        
        memory_id = len(self.memories)
        self.memories[memory_id] = {
            'embedding': separated,
            'episode': episode,
            'context_tags': context_tags,
            'timestamp': datetime.now()
        }
        
        # Add to index
        self.index.add(separated.unsqueeze(0).numpy())
        
        return memory_id
    
    def separate_patterns(self, embedding):
        """Pattern separation: make similar patterns more distinct."""
        # Add orthogonal noise proportional to separation parameter
        noise = torch.randn_like(embedding) * self.separation
        noise = noise - (noise @ embedding) * embedding  # Orthogonalize
        return F.normalize(embedding + noise, dim=-1)
    
    def retrieve(self, query, context_filter=None, k=10):
        """Retrieve similar memories with optional context filtering."""
        # Search in index
        D, I = self.index.search(query.unsqueeze(0).numpy(), k * 2)
        
        # Filter by context if specified
        candidates = []
        for idx, distance in zip(I[0], D[0]):
            memory = self.memories[idx]
            if context_filter:
                if all(memory['context_tags'].get(k) == v 
                       for k, v in context_filter.items()):
                    candidates.append(memory)
            else:
                candidates.append(memory)
            
            if len(candidates) >= k:
                break
        
        return candidates
```

### Cortical Consolidation

```python
class CorticalConsolidation:
    """Cortical-inspired stable memory with semantic extraction."""
    
    def __init__(self, semantic_dim, knowledge_graph=True):
        self.semantic_dim = semantic_dim
        self.semantic_memory = {}
        self.knowledge_graph = KnowledgeGraph() if knowledge_graph else None
        
    def extract_semantics(self, episodic_memory):
        """Extract semantic knowledge from episodic memory."""
        # Summarize the episode
        episode = episodic_memory['episode']
        
        semantic = {
            'type': self.infer_type(episode),
            'participants': self.extract_participants(episode),
            'location': episode['context']['location'],
            'outcome': self.infer_outcome(episode),
            'embedding': self.summarize_embedding(episodic_memory['embedding'])
        }
        
        return semantic
    
    def integrate(self, semantic_memory):
        """Integrate with existing knowledge."""
        # Check for similar existing memories
        similar = self.find_similar(semantic_memory)
        
        if similar:
            # Update existing schema
            self.update_schema(similar, semantic_memory)
        else:
            # Create new schema
            self.create_schema(semantic_memory)
        
        # Update knowledge graph
        if self.knowledge_graph:
            self.knowledge_graph.add_node(semantic_memory)
    
    def find_similar(self, semantic):
        """Find similar semantic memories."""
        for mem_id, mem in self.semantic_memory.items():
            if self.similarity(mem, semantic) > 0.8:
                return mem_id
        return None
```

## Use Cases

1. **Social Robots**: Remember user preferences and past interactions
2. **Personal Assistants**: Context-aware conversation
3. **Healthcare Companions**: Track patient history and emotional states
4. **Educational Agents**: Adapt to student learning patterns
5. **Therapeutic Agents**: Maintain therapeutic context across sessions

## Research Paper Reference

**Title**: Human-Inspired Context-Selective Multimodal Memory for Social Robots  
**Authors**: Hangyeol Kang, Slava Voloshynovskiy, Nadia Magnenat Thalmann  
**arXiv**: 2604.12081v1  
**Published**: 2026-04-13  
**Categories**: cs.AI

**Key Contributions**:
1. Biologically-inspired memory hierarchy (hippocampal + cortical)
2. Context-selective retrieval mechanism
3. Multimodal representation learning
4. Integration with social robot architecture

## References

- See [references/paper-details.md](references/paper-details.md) for full paper analysis
- See [references/hippocampal-memory.md](references/hippocampal-memory.md) for neuroscience background
