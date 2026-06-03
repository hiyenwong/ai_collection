---
name: tea-nets-cognitive-network
description: "TEA Nets (Target-Event-Agent Networks) — computational framework combining AI and cognitive network science to extract subjects (Agents), verbs (Events), and objects (Targets) from text. Enables interpretable emotion detection, semantic frame analysis, and linguistic inquiry. Activation: TEA Nets, cognitive network science, semantic network extraction, agent-event-target, text network analysis."
category: ai_collection
source:
  paper: "The TEA Nets framework combines AI and cognitive network science to model targets, events and actors in text"
  authors:
    - "Sebastiano Franchini"
    - "Alexis Carrillo"
    - "Edoardo Sebastiano De Duro"
    - "Riccardo Improta"
    - "Ali Aghazadeh Ardebili"
    - "Massimo Stella"
  arxiv: "2604.27673"
  date: "2026-04-30"
  fields:
    - cs.CL
    - cs.AI
activation_keywords:
  en:
    - TEA Nets
    - cognitive network science
    - semantic network extraction
    - agent event target
    - text network analysis
    - semantic frame analysis
    - emotion detection network
    - linguistic network
    - knowledge graph extraction
    - NLP network science
  zh:
    - TEA网络
    - 认知网络科学
    - 语义网络提取
    - 代理事件目标
    - 文本网络分析
    - 语义框架分析
    - 情感检测网络
    - 语言网络
version: "1.0.0"
---

# TEA Nets: Target-Event-Agent Networks for Text Analysis

> **Reference:** Franchini, S. et al. *The TEA Nets framework combines AI and cognitive network science to model targets, events and actors in text.* arXiv:2604.27673 [cs.CL] (2026).

## Overview

TEA Nets (Target-Event-Agent Networks) is a computational framework that extracts **semantic triplets** (Agents → Events → Targets) from text and represents them as **cognitive networks**. Grounded in cognitive network science and AI, TEA Nets enables interpretable analysis of text through network-theoretic measures.

## Core Concepts

### TEA Triplet Structure

Every extracted semantic unit follows the pattern:

```
[Agent] --(Event)--> [Target]
```

- **Agent**: The subject/actor performing the action (noun, pronoun)
- **Event**: The action/verb/operation connecting Agent to Target
- **Target**: The object/entity affected by the action (noun, noun phrase)

### Network Representation

TEA Nets constructs a **multilayer network** where:
- **Nodes** = Agents and Targets (entities)
- **Edges** = Events (directed, labeled with verb type)
- **Edge weights** = frequency or strength of association
- **Node attributes** = sentiment, emotion, frequency, centrality

---

## Extraction Pipeline

### Step 1: Dependency Parsing

```python
import spacy
from collections import defaultdict

class TEAExtractor:
    """Extract Target-Event-Agent triplets from text."""
    
    def __init__(self, model="en_core_web_trf"):
        self.nlp = spacy.load(model)
        self.triplets = []
        
    def extract_triplets(self, text):
        """Extract TEA triplets using dependency parsing."""
        doc = self.nlp(text)
        triplets = []
        
        for sent in doc.sents:
            for token in sent:
                # Find verbs (Events)
                if token.pos_ == "VERB":
                    event = token.lemma_
                    
                    # Find subject (Agent)
                    agent = self._find_subject(token)
                    # Find object (Target)  
                    target = self._find_object(token)
                    
                    if agent and target:
                        triplets.append({
                            'agent': agent.text.lower(),
                            'event': event,
                            'target': target.text.lower(),
                            'sentence': sent.text
                        })
        
        return triplets
    
    def _find_subject(self, verb):
        """Find the grammatical subject of a verb."""
        for child in verb.children:
            if child.dep_ in ('nsubj', 'nsubjpass'):
                return child
            # Handle compound subjects
            if child.dep_ == 'conj':
                for sub_child in child.children:
                    if sub_child.dep_ in ('nsubj',):
                        return sub_child
        return None
    
    def _find_object(self, verb):
        """Find the grammatical object of a verb."""
        for child in verb.children:
            if child.dep_ in ('dobj', 'pobj', 'attr'):
                return child
            # Handle prepositional objects
            if child.dep_ == 'prep':
                for sub_child in child.children:
                    if sub_child.dep_ == 'pobj':
                        return sub_child
        return None
```

### Step 2: Network Construction

```python
import networkx as nx
import numpy as np

class TEANetwork:
    """Construct and analyze TEA network from extracted triplets."""
    
    def __init__(self):
        self.G = nx.DiGraph()
        self.edge_events = defaultdict(list)  # edge -> list of events
        self.node_emotions = {}
        
    def add_triplets(self, triplets):
        """Add TEA triplets to the network."""
        for t in triplets:
            agent = t['agent']
            event = t['event']
            target = t['target']
            
            # Add nodes
            if agent not in self.G:
                self.G.add_node(agent, node_type='agent')
            if target not in self.G:
                self.G.add_node(target, node_type='target')
            
            # Add directed edge
            if self.G.has_edge(agent, target):
                self.G[agent][target]['weight'] += 1
            else:
                self.G.add_edge(agent, target, weight=1)
            
            self.edge_events[(agent, target)].append(event)
    
    def get_network_summary(self):
        """Compute network-level statistics."""
        summary = {
            'n_nodes': self.G.number_of_nodes(),
            'n_edges': self.G.number_of_edges(),
            'density': nx.density(self.G),
            'avg_clustering': nx.average_clustering(self.G.to_undirected()),
            'avg_path_length': nx.average_shortest_path_length(
                self.G.to_undirected()
            ) if nx.is_connected(self.G.to_undirected()) else None,
            'assortativity': nx.degree_assortativity_coefficient(
                self.G.to_undirected()
            ),
        }
        return summary
    
    def get_node_centrality(self):
        """Compute various centrality measures."""
        return {
            'degree': dict(nx.degree_centrality(self.G)),
            'betweenness': dict(nx.betweenness_centrality(self.G)),
            'pagerank': dict(nx.pagerank(self.G)),
            'hub': dict(nx.hits(self.G)[0]),  # hub scores
            'authority': dict(nx.hits(self.G)[1]),  # authority scores
        }
```

---

## Application Cases

### Case 1: Emotion Detection

```python
def detect_emotions_tea(network, sentiment_lexicon):
    """Detect emotions in text through TEA network analysis."""
    emotions = {}
    
    for node in network.G.nodes():
        # Get all events connected to this entity
        events_in = [e for _, _, events in network.G.in_edges(node, data=True) 
                     for e in network.edge_events.get((_, node), [])]
        events_out = [e for _, _, events in network.G.out_edges(node, data=True) 
                      for e in network.edge_events.get((node, _), [])]
        
        all_events = events_in + events_out
        
        # Map events to emotions using lexicon
        node_emotions = []
        for event in all_events:
            if event in sentiment_lexicon:
                node_emotions.append(sentiment_lexicon[event])
        
        if node_emotions:
            # Most frequent emotion
            emotions[node] = max(set(node_emotions), key=node_emotions.count)
    
    return emotions
```

### Case 2: Semantic Frame Analysis

```python
def analyze_semantic_frames(network):
    """Analyze semantic frames through network community detection."""
    # Detect communities (semantic frames/topics)
    communities = nx.community.louvain_communities(network.G.to_undirected())
    
    frames = []
    for i, community in enumerate(communities):
        subgraph = network.G.subgraph(community)
        
        # Extract key entities and events
        central_nodes = sorted(
            subgraph.nodes(), 
            key=lambda n: subgraph.degree(n), 
            reverse=True
        )[:5]
        
        frame_events = set()
        for u, v in subgraph.edges():
            frame_events.update(network.edge_events.get((u, v), []))
        
        frames.append({
            'frame_id': i,
            'central_entities': central_nodes,
            'events': list(frame_events),
            'size': len(community),
            'density': nx.density(subgraph),
        })
    
    return frames
```

### Case 3: Narrative Structure Analysis

```python
def analyze_narrative_structure(network):
    """Analyze narrative arc through TEA network properties."""
    # Find main protagonist (highest out-degree)
    out_degrees = dict(network.G.out_degree())
    protagonist = max(out_degrees, key=out_degrees.get)
    
    # Find main antagonist (connected to protagonist via negative events)
    # (requires sentiment labeling of events)
    
    # Narrative complexity
    complexity = {
        'protagonist': protagonist,
        'n_characters': network.G.number_of_nodes(),
        'n_interactions': network.G.number_of_edges(),
        'avg_interactions_per_character': np.mean(list(out_degrees.values())),
        'max_interactions': max(out_degrees.values()),
        'network_diameter': nx.diameter(network.G.to_undirected()) 
            if nx.is_connected(network.G.to_undirected()) else None,
    }
    
    return complexity
```

---

## Cognitive Network Science Measures

### Key Network Metrics for Text Analysis

| Metric | Interpretation in TEA Nets |
|---|---|
| **Degree Centrality** | How central an entity is in the narrative |
| **Betweenness Centrality** | Entities that bridge different semantic frames |
| **Clustering Coefficient** | Tendency for entities to form cohesive semantic groups |
| **Assortativity** | Whether central entities connect to other central entities |
| **Community Structure** | Distinct topics/themes in the text |
| **Rich-Club Coefficient** | Whether high-degree entities preferentially connect to each other |

### Semantic Proximity

```python
def semantic_distance(G, node1, node2):
    """Compute semantic distance between two entities in TEA network."""
    try:
        return nx.shortest_path_length(G, node1, node2)
    except nx.NetworkXNoPath:
        return float('inf')

def semantic_similarity(G, node1, node2):
    """Compute semantic similarity via common neighbors."""
    neighbors1 = set(G.neighbors(node1))
    neighbors2 = set(G.neighbors(node2))
    
    # Jaccard similarity
    intersection = neighbors1 & neighbors2
    union = neighbors1 | neighbors2
    
    if not union:
        return 0.0
    return len(intersection) / len(union)
```

---

## Integration with LLMs

### LLM-Assisted TEA Extraction

```python
def llm_tea_extraction(text, llm_client):
    """Use LLM to extract TEA triplets with higher accuracy."""
    prompt = f"""
    Extract all Target-Event-Agent (TEA) triplets from the following text.
    Format each triplet as: AGENT | EVENT | TARGET
    
    Text: {text}
    
    Return only the triplets, one per line.
    """
    
    response = llm_client.complete(prompt)
    triplets = []
    
    for line in response.strip().split('\n'):
        parts = line.split('|')
        if len(parts) == 3:
            triplets.append({
                'agent': parts[0].strip().lower(),
                'event': parts[1].strip().lower(),
                'target': parts[2].strip().lower(),
            })
    
    return triplets
```

---

## Best Practices

1. **Use transformer-based parsers** (en_core_web_trf) for higher accuracy than rule-based
2. **Lemmatize events** to consolidate verb forms (running → run)
3. **Filter stop words** from agents and targets
4. **Merge coreferent entities** (he → John) for cleaner networks
5. **Weight edges by context** — nearby triplets have stronger relationships
6. **Use multilayer networks** for texts with multiple dimensions (time, emotion, etc.)
7. **Validate extraction quality** — sample and manually verify triplets
8. **Combine with sentiment analysis** for richer emotional TEA networks
9. **Track temporal evolution** — build TEA networks for text segments over time
10. **Use community detection** to identify semantic frames and topics

## References

- Franchini, S. et al. (2026). *The TEA Nets framework combines AI and cognitive network science to model targets, events and actors in text.* arXiv:2604.27673 [cs.CL].
- Related: brain-connectivity-analysis, interdisciplinary-discovery