---
name: graphidyom-musical-expectation-modeling
title: "GraphIDyOM: A graph-native Python reimplementation of IDyOM for musical expectation modelling"
description: "Graph-native Python reimplementation of the Information Dynamics of Music (IDyOM) model that represents predictive memories as explicit graph objects for musical expectation modeling and network analysis."
authors: ["Lluc Bono Rosselló"]
arxiv_id: "2607.25787"
date: "2026-07-28"
categories: ["q-bio.NC", "cs.SD", "computational-neuroscience", "music-cognition", "graph-neural-networks"]
trigger_words: ["graphidyom", "musical expectation", "IDyOM", "information dynamics music", "graph-native music modeling", "predictive memory graphs"]
---

# GraphIDyOM: Graph-Native Musical Expectation Modeling

## Overview
GraphIDyOM is a graph-native Python reimplementation of the Information Dynamics of Music (IDyOM) model, which provides event-by-event estimates of uncertainty and surprise from symbolic musical sequences. The original Lisp implementation was difficult to integrate with contemporary Python workflows and had inaccessible internal memory structures. GraphIDyOM solves these issues by representing long-term and short-term predictive memories as explicit graph objects while preserving IDyOM's variable-order, multiple-viewpoint architecture.

## Core Features

### 1. Graph-Native Memory Representation
- **Long-term memory**: Explicit graph objects representing learned musical patterns
- **Short-term memory**: Graph structures for recent context and recency-sensitive retrieval
- **Variable-order architecture**: Preserves IDyOM's ability to learn patterns of varying lengths
- **Multiple-viewpoint support**: Handles different musical feature dimensions simultaneously

### 2. Enhanced Accessibility and Integration
- **Python-native**: Integrates seamlessly with modern Python data science workflows
- **Memory export**: Internal memory structures can be analyzed and exported for research
- **Local server support**: Provides programmatic access through HTTP endpoints
- **Event-wise outputs**: Returns information content and entropy for each musical event

### 3. Validation and Performance
- **Faithful reimplementation**: Validated against original Lisp IDyOM across configurations
- **Benchmarked performance**: Outperforms recent reimplementations in coverage and speed
- **Configuration support**: Works with single, projected, and multiple-viewpoint setups

## Implementation Guidelines

### Basic Usage
```python
from graphidyom import GraphIDyOM

# Initialize model with musical viewpoints
model = GraphIDyOM(viewpoints=['pitch', 'duration', 'onset'])

# Train on symbolic music sequences
training_sequences = load_midi_sequences('dataset/')
model.train(training_sequences)

# Get expectation values for new sequence
test_sequence = load_midi_sequence('test.mid')
info_content, entropy = model.predict(test_sequence)

# Access internal memory graphs
long_term_graph = model.get_long_term_memory()
short_term_graph = model.get_short_term_memory()
```

### Network Analysis Applications
```python
# Analyze learned memory as network
import networkx as nx

memory_graph = model.get_long_term_memory()
centrality_measures = nx.betweenness_centrality(memory_graph)
clustering_coefficients = nx.clustering(memory_graph)

# Project expectation values onto musical networks
expectation_projection = model.project_expectations(
    sequence=test_sequence,
    graph=external_music_network
)

# Recency-sensitive memory retrieval
recent_patterns = model.retrieve_recent_patterns(
    context_window=16,  # last 16 events
    similarity_threshold=0.8
)
```

### Interactive Applications
```python
# Start local server for interactive use
model.start_server(port=8080)

# Now accessible via HTTP API:
# GET /predict?sequence=[...]
# GET /memory/long_term
# GET /memory/short_term  
# POST /train with JSON sequences
```

## Applications in Neuroscience and Music Cognition

### 1. Musical Expectation Research
- **Uncertainty quantification**: Measure information-theoretic surprise in musical sequences
- **Cross-cultural comparison**: Train models on different musical traditions
- **Developmental studies**: Track how musical expectations evolve with exposure

### 2. Brain-Music Interface Studies
- **Neural alignment**: Correlate model predictions with EEG/MEG responses to musical violations
- **Predictive coding**: Test hierarchical predictive processing theories in music perception
- **Individual differences**: Model personalized musical expectations based on listening history

### 3. Computational Musicology
- **Style analysis**: Extract characteristic patterns from different composers or genres
- **Creative applications**: Generate music that balances predictability and surprise
- **Music recommendation**: Use expectation models to suggest pieces matching listener preferences

## Key Advantages Over Original IDyOM

1. **Accessibility**: Python integration enables use with standard scientific computing libraries
2. **Transparency**: Explicit memory representation allows inspection and modification
3. **Extensibility**: Graph-based architecture supports custom network analysis techniques
4. **Interactivity**: Local server enables real-time applications and web integration
5. **Reproducibility**: Open-source implementation facilitates research replication

## Practical Workflow Example

### Step 1: Data Preparation
```python
# Convert MIDI files to symbolic sequences
from music21 import converter
import numpy as np

def midi_to_symbolic(midi_path):
    score = converter.parse(midi_path)
    # Extract pitch, duration, onset features
    pitches = [note.pitch.midi for note in score.flat.notes]
    durations = [note.duration.quarterLength for note in score.flat.notes] 
    onsets = [note.offset for note in score.flat.notes]
    return list(zip(pitches, durations, onsets))
```

### Step 2: Model Training and Prediction
```python
# Train GraphIDyOM model
sequences = [midi_to_symbolic(f) for f in training_files]
model = GraphIDyOM(viewpoints=['pitch', 'duration'])
model.train(sequences)

# Predict on test sequence
test_seq = midi_to_symbolic('beethoven_sonata.mid')
ic, entropy = model.predict(test_seq)

# Find surprising events (high information content)
surprising_events = np.where(ic > np.percentile(ic, 90))[0]
```

### Step 3: Network Analysis
```python
# Analyze memory structure
memory_graph = model.get_long_term_memory()
print(f"Memory contains {len(memory_graph.nodes)} patterns")
print(f"Average clustering coefficient: {nx.average_clustering(memory_graph):.3f}")

# Visualize expectation projection
projection = model.project_expectations(test_seq, external_network)
plot_network_with_expectations(external_network, projection)
```

## Pitfalls to Avoid

- **Overfitting**: Ensure sufficient training data for complex viewpoint combinations
- **Computational complexity**: Graph operations can become expensive with large memories
- **Viewpoint selection**: Choose musically meaningful features rather than exhaustive combinations
- **Validation**: Always compare against original IDyOM for critical applications

## Verification Steps

1. **Reproduce original results**: Validate predictions match original IDyOM on benchmark datasets
2. **Memory consistency**: Verify graph structure preserves sequential relationships
3. **Performance benchmarking**: Confirm computational efficiency meets requirements
4. **Integration testing**: Test with downstream neuroscience analysis pipelines

## References

- Bono Rosselló, L. (2026). GraphIDyOM: A graph-native Python reimplementation of IDyOM for musical expectation modelling. arXiv:2607.25787 [cs.SD, q-bio.NC]
- Pearce, M. T. (2005). The construction and evaluation of statistical models of melodic structure in music perception and composition. PhD thesis, City University London.
- Conklin, D., & Witten, I. H. (1995). Multiple viewpoint systems for music prediction. Journal of New Music Research, 24(1), 51-73.