---
skill_name: llm-emotion-dynamics-decoding
description: LLM-enhanced multi-target regression framework for decoding continuous naturalistic emotion dynamics from brain fMRI signals using dynamic functional connectivity and graph-theoretical explainable AI, supporting psychological constructionist frameworks over locationist accounts
version: 1.0
last_updated: 2026-06-10
arxiv_id: 2606.07707v1
paper_title: "Decoding Naturalistic Emotion Dynamics from the Brain: An LLM-Enhanced Regression Framework"
paper_url: https://arxiv.org/abs/2606.07707
authors: Lemei Zhang, Peng Liu, Hans Dahle Kvadsheim, August Sætre Aasvær, Shuer Ye, Reza Bonyadi, Maryam Ziaei, Jon Atle Gulla
published: 2026-06-05
categories: [cs.LG]
activation_keywords: [emotion dynamics, LLM annotation, multi-target regression, dynamic functional connectivity, naturalistic neuroscience, graph-theoretical XAI, psychological constructionism, affective neuroscience, continuous emotion decoding, fMRI regression]
related_skills: [brain-foundation-model-inversion, llm-emotion-trajectory-fmri, eeg-foundation-model-adapters, neuroscience-of-transformers]
status: available
---

# LLM-Enhanced Emotion Dynamics Decoding Framework

## Overview

This framework reconceptualizes emotion decoding from discrete classification to **continuous multi-target regression**, leveraging LLM-automated annotation from naturalistic narratives to track emotional trajectories as continuous time series. It demonstrates that **Dynamic Functional Connectivity (DFC)** outperforms static ROI representations, providing evidence for psychological constructionist frameworks over locationist accounts.

## Core Innovation

### 1. Paradigm Shift: Classification → Regression

**Traditional Approach (Limitations)**:
- Discrete, single-label classification tasks
- Based on emotionally stable stimuli
- Oversimplifies continuous, fluid, co-occurring affect
- Misses temporal dynamics of emotional experience

**New Framework (Advantages)**:
- Multi-target regression for continuous trajectories
- Naturalistic, dynamic stimuli (Alice in Wonderland)
- Multiple overlapping emotional dimensions
- Time-varying emotional states

**Mathematical Formulation**:
```
Traditional: y ∈ {emotion_1, emotion_2, ..., emotion_k} (discrete)
New Framework: y(t) = [valence(t), arousal(t), dominance(t), ...] (continuous vector)

Regression targets:
├── Valence: positive ↔ negative continuum
├── Arousal: calm ↔ excited continuum  
├── Dominance: submissive ↔ dominant continuum
└── Additional dimensions (emotion-specific)
```

### 2. LLM-Automated Sentiment Annotation

**Innovation**: Use LLMs to extract fine-grained sentiment profiles from naturalistic narrative as proxies for subjective affect.

**Annotation Pipeline**:
```python
# Step 1: Segment narrative into temporal windows
segments = segment_narrative("Alice in Wonderland", window_size=10s)

# Step 2: LLM sentiment extraction for each segment
sentiment_profiles = []
for segment in segments:
    # LLM extracts continuous sentiment dimensions
    sentiment = llm_extract_sentiment(segment)
    sentiment_profiles.append({
        'valence': sentiment.valence,      # [-1, 1]
        'arousal': sentiment.arousal,      # [0, 1]
        'dominance': sentiment.dominance,  # [0, 1]
        'timestamp': segment.timestamp
    })

# Step 3: Use sentiment profiles as regression targets
targets = np.array([s['valence'], s['arousal'], s['dominance'] 
                    for s in sentiment_profiles])
```

**Key Advantages**:
- **Scalable**: No need for manual human annotation
- **Fine-grained**: Continuous sentiment dimensions
- **Temporal alignment**: Segment-by-segment extraction
- **Generalizable**: LLM robust semantic understanding

### 3. Dynamic Functional Connectivity (DFC) Features

**Innovation**: Use temporal snapshots of DFC instead of static ROI amplitude.

**DFC Construction**:
```python
# For each time window t:
# Compute functional connectivity matrix
FC_t = compute_functional_connectivity(fMRI_window_t)

# DFC features: temporal sequence of connectivity matrices
DFC_sequence = [FC_1, FC_2, ..., FC_T]

# Key insight: DFC captures network dynamics
# Static ROI only captures locationist regional activity
```

**Feature Extraction**:
```
DFC Features:
├── Sliding window connectivity matrices
├── Temporal dynamics of network interactions
├── Edge weights across time
└── Network reconfiguration patterns

Static ROI Features (Baseline):
├── Regional amplitude (BOLD signal)
├── No network dynamics
└── Locationist account (regional specificity)
```

**Comparison Results**:
- DFC significantly outperforms static ROI
- Captures continuous emotional trajectories
- Better alignment with rapidly fluctuating narrative

### 4. Graph-Theoretical Explainable AI (XAI)

**Innovation**: Implement graph-theoretical XAI to reveal emotion-specific topological configurations.

**XAI Pipeline**:
```python
# Step 1: Train regression model on DFC features
model = train_multi_target_regression(DFC_features, sentiment_targets)

# Step 2: Apply graph-theoretical XAI
def graph_xai(model, DFC_matrix):
    """
    Extract interpretable topological features
    
    Returns:
    - Important edges (connections)
    - Hub regions (central nodes)
    - Network motifs (subgraph patterns)
    - Community structure (emotion-specific modules)
    """
    # Feature attribution via graph importance
    edge_importance = compute_edge_importance(model, DFC_matrix)
    
    # Topological analysis
    topology = {
        'hubs': identify_hubs(edge_importance),
        'motifs': identify_network_motifs(DFC_matrix),
        'communities': detect_communities(DFC_matrix)
    }
    
    return topology
```

**Interpretable Features**:
- **Important edges**: Which connections predict specific emotions
- **Hub regions**: Central nodes in emotion networks
- **Network motifs**: Recurring subgraph patterns
- **Community structure**: Emotion-specific modular organization

### 5. Psychological Constructionist Evidence

**Key Finding**: Dynamic, distributed network interactions offer superior explanatory power over locationist accounts.

**Constructionist Framework**:
```
Emotion = Network Interaction Pattern (not brain region location)

Constructionist Account:
├── Emotions emerge from distributed network dynamics
├── Multiple brain regions interact continuously
├── Temporal reconfiguration of connectivity
└── Context-dependent network states

Locationist Account (Rejected):
├── Emotions localized in specific brain regions
├── Static regional activity
├── No network dynamics consideration
└── Limited explanatory power
```

**Evidence from Study**:
- DFC (network dynamics) outperforms static ROI (regional activity)
- Graph XAI reveals distributed network patterns
- Multiple overlapping emotional dimensions co-occur
- Rapidly fluctuating narrative requires dynamic features

## Methodology Details

### 1. Dataset and Stimuli

**Naturalistic Narrative**: Alice in Wonderland (auditory)

**fMRI Dataset**: Human subjects listening to narrative

**Temporal Segmentation**: Window-based analysis

**LLM Annotation**: Continuous sentiment extraction for each segment

### 2. Multi-Target Regression Models

**Regularized Regression**:
```python
# Ridge/Lasso regression with regularization
from sklearn.linear_model import Ridge, Lasso

ridge_model = Ridge(alpha=1.0)
ridge_model.fit(DFC_features, sentiment_targets)

# Kernel-based regression (non-linear)
from sklearn.kernel_ridge import KernelRidge

kernel_model = KernelRidge(kernel='rbf', alpha=0.1)
kernel_model.fit(DFC_features, sentiment_targets)
```

**Model Comparison**:
- Ridge regression: Linear with regularization
- Lasso regression: Sparse feature selection
- Kernel Ridge: Non-linear relationships
- SVR: Support vector regression

### 3. DFC Construction Pipeline

```python
def construct_DFC(fMRI_data, window_size=10, stride=5):
    """
    Construct dynamic functional connectivity sequence
    
    Parameters:
    - fMRI_data: [time, regions] BOLD signals
    - window_size: Temporal window (seconds)
    - stride: Window stride (seconds)
    
    Returns:
    - DFC_sequence: [windows, regions, regions] connectivity matrices
    """
    DFC_sequence = []
    
    for t in range(0, fMRI_data.shape[0] - window_size, stride):
        window_data = fMRI_data[t:t+window_size, :]
        
        # Compute correlation matrix for window
        FC_t = np.corrcoef(window_data.T)  # [regions, regions]
        
        DFC_sequence.append(FC_t)
    
    return np.array(DFC_sequence)

# Feature flattening for regression
DFC_features = flatten_DFC(DFC_sequence)  # [windows, regions²]
```

### 4. Graph-Theoretical XAI Implementation

```python
import networkx as nx

def graph_xai_analysis(DFC_matrix, threshold=0.5):
    """
    Extract interpretable graph-theoretical features
    
    Parameters:
    - DFC_matrix: Connectivity matrix for time window
    - threshold: Edge significance threshold
    
    Returns:
    - topology: Graph metrics and important features
    """
    # Create graph from connectivity matrix
    G = nx.Graph()
    
    # Add edges above threshold
    for i in range(DFC_matrix.shape[0]):
        for j in range(i+1, DFC_matrix.shape[1]):
            if abs(DFC_matrix[i,j]) > threshold:
                G.add_edge(i, j, weight=DFC_matrix[i,j])
    
    # Topological analysis
    topology = {
        'degree_centrality': nx.degree_centrality(G),
        'betweenness_centrality': nx.betweenness_centrality(G),
        'clustering_coefficient': nx.clustering(G),
        'modularity': community_detection(G),
        'motifs': detect_motifs(G)
    }
    
    return topology

def emotion_specific_topology(model, emotion_dim='valence'):
    """
    Extract topology specific to each emotion dimension
    
    Use feature attribution to identify:
    - Which edges predict valence
    - Which edges predict arousal
    - Which edges predict dominance
    """
    # Get feature importance for specific emotion
    importance = model.coef_[emotion_dim]
    
    # Map importance to edges
    edge_importance = map_to_edges(importance, brain_regions)
    
    # Identify top edges for this emotion
    top_edges = sort_edges_by_importance(edge_importance)
    
    return {
        'emotion': emotion_dim,
        'top_edges': top_edges,
        'hub_regions': identify_hubs(top_edges),
        'network_pattern': characterize_network(top_edges)
    }
```

## Key Findings

### Finding 1: DFC Superiority

**Result**: DFC significantly outperforms static ROI representations

**Evidence**:
- Higher regression accuracy (R²)
- Better temporal alignment with sentiment profiles
- Captures rapidly fluctuating narrative dynamics

**Statistical Validation**:
- Cross-validation: DFC vs Static ROI
- Significance testing: p < 0.01
- Correlation with continuous sentiment: r > 0.5

### Finding 2: LLM Annotation Effectiveness

**Result**: LLM-extracted sentiment profiles serve as reliable regression targets

**Evidence**:
- Fine-grained continuous dimensions
- Scalable automated annotation
- Strong correlation with human affective experience
- Robust generalization from narrative

### Finding 3: Emotion-Specific Topology

**Result**: Graph XAI reveals interpretable topological configurations for each emotion

**Evidence**:
- Valence-specific network patterns
- Arousal-specific hub regions
- Dominance-specific community structure
- Overlapping but distinct topologies

### Finding 4: Constructionist Evidence

**Result**: Network dynamics explain emotions better than regional localization

**Evidence**:
- DFC outperforms static ROI (network vs location)
- Multiple overlapping dimensions co-occur (constructionist)
- Temporal reconfiguration predicts emotion (dynamic)
- Distributed patterns (not isolated regions)

## Practical Implementation

### Full Pipeline

```python
import numpy as np
from transformers import pipeline

class LLMEmotionDecodingFramework:
    """
    Complete framework for LLM-enhanced emotion dynamics decoding
    """
    
    def __init__(self, llm_model='gpt-4', regression_type='kernel_ridge'):
        # LLM sentiment extractor
        self.llm_sentiment = pipeline('sentiment-analysis', model=llm_model)
        
        # Regression model
        if regression_type == 'kernel_ridge':
            self.regressor = KernelRidge(kernel='rbf')
        elif regression_type == 'ridge':
            self.regressor = Ridge()
        
    def extract_sentiment_from_narrative(self, narrative_segments):
        """
        Extract continuous sentiment profiles using LLM
        
        Returns: sentiment_targets [segments, dimensions]
        """
        sentiment_profiles = []
        
        for segment in narrative_segments:
            # LLM sentiment extraction
            sentiment = self.llm_sentiment(segment)
            
            # Extract continuous dimensions
            profile = {
                'valence': sentiment['valence_score'],
                'arousal': sentiment['arousal_score'],
                'dominance': sentiment['dominance_score']
            }
            sentiment_profiles.append(profile)
        
        return self.convert_to_targets(sentiment_profiles)
    
    def construct_DFC_features(self, fMRI_data, window_size=10):
        """
        Construct dynamic functional connectivity features
        """
        DFC_sequence = []
        
        for t in range(0, fMRI_data.shape[0], window_size):
            window = fMRI_data[t:t+window_size, :]
            FC = np.corrcoef(window.T)
            DFC_sequence.append(FC.flatten())
        
        return np.array(DFC_sequence)
    
    def train_regression(self, DFC_features, sentiment_targets):
        """
        Train multi-target regression model
        """
        self.regressor.fit(DFC_features, sentiment_targets)
        
    def predict_emotion_trajectory(self, new_DFC):
        """
        Predict continuous emotion trajectory from new DFC
        """
        predictions = self.regressor.predict(new_DFC)
        
        # Convert to emotion profiles
        trajectory = [{
            'valence': pred[0],
            'arousal': pred[1],
            'dominance': pred[2]
        } for pred in predictions]
        
        return trajectory
    
    def explain_predictions(self, DFC_matrix, brain_region_labels):
        """
        Graph-theoretical explainability
        """
        # Feature importance
        importance = self.regressor.coef_
        
        # Map to edges
        edge_importance = self.map_importance_to_edges(
            importance, brain_region_labels
        )
        
        # Topological analysis
        topology = self.graph_xai_analysis(DFC_matrix, edge_importance)
        
        return topology
```

### Usage Example

```python
# Initialize framework
framework = LLMEmotionDecodingFramework(
    llm_model='gpt-4',
    regression_type='kernel_ridge'
)

# Step 1: Extract sentiment from narrative
narrative_segments = segment_narrative("Alice in Wonderland")
sentiment_targets = framework.extract_sentiment_from_narrative(narrative_segments)

# Step 2: Construct DFC features from fMRI
fMRI_data = load_fMRI_data("subject_fMRI.npy")
DFC_features = framework.construct_DFC_features(fMRI_data, window_size=10)

# Step 3: Train regression model
framework.train_regression(DFC_features, sentiment_targets)

# Step 4: Predict emotion trajectory for new subject
new_fMRI = load_fMRI_data("new_subject.npy")
new_DFC = framework.construct_DFC_features(new_fMRI, window_size=10)
emotion_trajectory = framework.predict_emotion_trajectory(new_DFC)

# Step 5: Explain predictions with graph XAI
topology = framework.explain_predictions(new_DFC[0], brain_region_labels)

print("Predicted emotion trajectory:", emotion_trajectory)
print("Emotion-specific topology:", topology)
```

## Comparison with Traditional Approaches

### Traditional Emotion Classification

**Limitations**:
1. Discrete labels (no continuous dynamics)
2. Static stimuli (no naturalistic dynamics)
3. ROI-based (locationist, no network)
4. Single dimension (no overlapping emotions)

### LLM-Enhanced Regression Framework

**Advantages**:
1. Continuous trajectories (full temporal dynamics)
2. Naturalistic stimuli (real-world complexity)
3. DFC-based (network dynamics, constructionist)
4. Multi-target (overlapping emotional dimensions)
5. LLM annotation (scalable, fine-grained)
6. Graph XAI (interpretable topology)

## Applications

### 1. Affective Neuroscience Research

- **Emotion dynamics tracking**: Continuous trajectory analysis
- **Network-based emotion theory**: Constructionist evidence
- **Naturalistic paradigm**: Real-world emotional experience
- **Individual differences**: Subject-specific emotion networks

### 2. Clinical Applications

- **Mood disorder assessment**: Track emotional dynamics over time
- **Therapy monitoring**: Continuous affect measurement
- **Emotion regulation**: Network-level intervention targets
- **Personalized treatment**: Subject-specific topology

### 3. NeuroAI Architecture

- **Emotion-aware AI**: Incorporate emotional dynamics
- **Affective computing**: Naturalistic emotion modeling
- **Brain-inspired emotion**: Network-based architectures
- **LLM integration**: Automated affect annotation

### 4. Real-Time Applications

```python
# Real-time emotion monitoring
def realtime_emotion_monitor(fMRI_stream, narrative_stream):
    """
    Real-time continuous emotion decoding
    
    Use case: Therapy session monitoring
    """
    # Update DFC in real-time
    current_DFC = update_DFC(fMRI_stream.current_window)
    
    # Predict current emotion state
    current_emotion = framework.predict_emotion_trajectory(current_DFC)
    
    # Track emotion dynamics
    emotion_history.append(current_emotion)
    
    # Detect emotion changes
    if emotion_change_detected(emotion_history):
        trigger_intervention(current_emotion)
    
    return current_emotion
```

## Theoretical Implications

### Psychological Constructionist Framework

**Core Principle**: Emotions are **constructed** from distributed network interactions, not **localized** in specific brain regions.

**Evidence from Study**:
1. DFC outperforms ROI → Network > Location
2. Multiple overlapping dimensions → Construction
3. Temporal reconfiguration → Dynamic assembly
4. Distributed topology → No single "emotion center"

### Locationist Account (Rejected)

**Rejected Principle**: Each emotion has a dedicated brain region.

**Evidence Against**:
- Static ROI fails to capture dynamics
- Single regions insufficient for prediction
- Emotions co-occur (no clear separation)
- Network patterns more predictive

### Network Theory of Emotion

**Emerging Framework**:
```
Emotion = Network State (not regional activity)

Network state components:
├── Connectivity pattern (which regions connected)
├── Temporal dynamics (how connectivity changes)
├── Hub activation (central network nodes)
├── Community structure (emotion-specific modules)
└── Network reconfiguration (state transitions)
```

## Limitations and Future Directions

### Current Limitations

1. **Single narrative**: Only Alice in Wonderland tested
2. **LLM validation**: LLM sentiment proxies need human validation
3. **Temporal resolution**: Window-based (not instantaneous)
4. **Subject variability**: Individual differences in topology

### Future Extensions

1. **Multiple narratives**: Generalize across stimuli
2. **Human validation**: Compare LLM vs human sentiment ratings
3. **Instantaneous DFC**: Higher temporal resolution
4. **Individual topology**: Subject-specific network patterns
5. **Cross-modal integration**: EEG + fMRI emotion decoding
6. **Real-time deployment**: Clinical emotion monitoring

## Key Takeaways

1. **Paradigm shift**: Classification → Continuous regression
2. **LLM automation**: Scalable sentiment annotation
3. **DFC superiority**: Network dynamics > Regional activity
4. **Interpretable XAI**: Emotion-specific topology
5. **Constructionist evidence**: Distributed network theory
6. **Naturalistic validity**: Real-world emotional dynamics

## Summary

The LLM-enhanced emotion dynamics decoding framework provides a **constructionist, network-based approach** to emotion decoding that:
- **Tracks continuous trajectories** (not discrete labels)
- **Leverages LLM annotation** (scalable, fine-grained)
- **Uses DFC features** (network dynamics, not static ROI)
- **Reveals interpretable topology** (graph-theoretical XAI)
- **Supports constructionist theory** (network > location)
- **Validates naturalistic paradigm** (real-world emotion)

This methodology advances affective neuroscience by treating emotion as **continuous, dynamic network states** rather than **localized, discrete categories**, providing both theoretical insight and practical applications.

---

**Activation**: emotion dynamics, LLM annotation, multi-target regression, dynamic functional connectivity, naturalistic neuroscience, graph-theoretical XAI, psychological constructionism, affective neuroscience, continuous emotion decoding, fMRI regression, Alice in Wonderland, sentiment profiles, network topology, emotion-specific hubs, constructionist vs locationist