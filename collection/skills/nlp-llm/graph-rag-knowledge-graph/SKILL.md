---
name: graphrag-retrieval-augmented-generation-with-knowl
description: Skill for AI agent capabilities
---

# GraphRAG: Retrieval-Augmented Generation with Knowledge Graphs

## Description

GraphRAG enhances RAG by using knowledge graphs for retrieval instead of isolated text chunks. By leveraging graph structure with nodes connected by edges, GraphRAG captures heterogeneous and relational information, enabling better reasoning over complex query-knowledge relationships.

**Key Benefits:**
- Captures intrinsic relationships between chunks
- Enables reasoning over graph structure
- Supports general and underlying theme queries
- Works with heterogeneous knowledge bases

## Tools Used

- read: Load knowledge graph data
- write: Store graph structures
- exec: Run graph queries and retrieval
- browser: Access external knowledge sources
- memory_search: Query existing knowledge

## Instructions for Agents

### GraphRAG Pipeline

1. **Build Knowledge Graph** - Extract entities and relations from documents
2. **Index Graph** - Create graph embeddings and indexes
3. **Query Processing** - Parse query and identify relevant subgraphs
4. **Graph Retrieval** - Retrieve connected knowledge
5. **Generation** - Use retrieved graph context for LLM generation

### When to Use GraphRAG

- Complex relational queries
- Multi-hop reasoning required
- Domain knowledge with rich relationships
- Need to capture underlying themes

## Overview

**Source:** arXiv:2501.00309
**Utility:** 0.93
**GitHub:** https://github.com/Graph-RAG/GraphRAG

## Activation Keywords

- graph rag
- knowledge graph RAG
- graph retrieval augmented generation
- graph-based retrieval

---

## Architecture

### Standard RAG vs GraphRAG

| Aspect | Standard RAG | GraphRAG |
|--------|--------------|----------|
| Retrieval | Semantic similarity | Graph traversal |
| Context | Isolated chunks | Connected knowledge |
| Reasoning | Limited | Multi-hop capable |
| Relationships | Ignored | Explicitly captured |

### GraphRAG Pipeline

```
Documents → Entity Extraction → Knowledge Graph Construction
                                           ↓
Query → Entity Linking → Subgraph Retrieval → Context Assembly → LLM
```

---

## Implementation

### 1. Knowledge Graph Construction

```python
class KnowledgeGraphBuilder:
    def __init__(self, llm):
        self.llm = llm
    
    def extract_entities_and_relations(self, document):
        prompt = f"""
        Extract entities and their relationships from:
        {document}
        
        Format: (Entity1, RELATION, Entity2)
        """
        return self.llm.generate(prompt)
    
    def build_graph(self, documents):
        import networkx as nx
        graph = nx.DiGraph()
        
        for doc in documents:
            triples = self.extract_entities_and_relations(doc)
            for entity1, relation, entity2 in triples:
                graph.add_edge(entity1, entity2, relation=relation)
        
        return graph
```

### 2. Graph Indexing

```python
class GraphIndexer:
    def __init__(self, graph):
        self.graph = graph
        self.embeddings = {}
    
    def create_embeddings(self, embedding_model):
        for node in self.graph.nodes():
            # Node embedding from neighbors
            neighbor_text = self.get_neighbor_context(node)
            self.embeddings[node] = embedding_model.encode(neighbor_text)
    
    def get_neighbor_context(self, node, depth=2):
        context = [node]
        for neighbor in self.graph.neighbors(node):
            context.append(neighbor)
            relation = self.graph[node][neighbor].get('relation', '')
            context.append(relation)
        return ' '.join(context)
```

### 3. Graph Retrieval

```python
class GraphRetriever:
    def __init__(self, graph, embeddings):
        self.graph = graph
        self.embeddings = embeddings
    
    def retrieve_subgraph(self, query, k=5):
        # Find relevant entities
        query_embedding = self.embed_query(query)
        relevant_nodes = self.find_similar_nodes(query_embedding, k)
        
        # Expand to subgraph
        subgraph = self.expand_subgraph(relevant_nodes, depth=2)
        
        return subgraph
    
    def expand_subgraph(self, nodes, depth=2):
        import networkx as nx
        subgraph = nx.DiGraph()
        
        for node in nodes:
            for neighbor in nx.single_source_shortest_path(
                self.graph, node, cutoff=depth
            ):
                if self.graph.has_edge(node, neighbor):
                    subgraph.add_edge(
                        node, neighbor,
                        **self.graph[node][neighbor]
                    )
        
        return subgraph
```

### 4. Context Assembly

```python
class ContextAssembler:
    def subgraph_to_context(self, subgraph, query):
        context_parts = []
        
        # Extract paths relevant to query
        for u, v, data in subgraph.edges(data=True):
            relation = data.get('relation', 'related_to')
            context_parts.append(f"{u} {relation} {v}")
        
        # Format as natural language
        context = "\n".join(context_parts)
        return f"Knowledge Graph Context:\n{context}"
```

### 5. Complete GraphRAG Pipeline

```python
class GraphRAG:
    def __init__(self, llm, embedding_model):
        self.llm = llm
        self.embedding_model = embedding_model
        self.graph_builder = KnowledgeGraphBuilder(llm)
        self.indexer = None
        self.retriever = None
    
    def build_from_documents(self, documents):
        # Build knowledge graph
        self.graph = self.graph_builder.build_graph(documents)
        
        # Create embeddings
        self.indexer = GraphIndexer(self.graph)
        self.indexer.create_embeddings(self.embedding_model)
        
        # Initialize retriever
        self.retriever = GraphRetriever(
            self.graph, 
            self.indexer.embeddings
        )
    
    def query(self, query):
        # Retrieve relevant subgraph
        subgraph = self.retriever.retrieve_subgraph(query)
        
        # Assemble context
        context = ContextAssembler().subgraph_to_context(subgraph, query)
        
        # Generate answer
        prompt = f"""
        Context from Knowledge Graph:
        {context}
        
        Question: {query}
        
        Answer based on the graph context:
        """
        
        return self.llm.generate(prompt)
```

---

## Graph Foundation Models (GFM-RAG)

```python
class GFMRAG:
    """Graph Foundation Model for RAG - works on unseen datasets"""
    
    def __init__(self, gnn_model):
        self.gnn = gnn_model  # Pre-trained GNN
    
    def retrieve(self, query_graph, knowledge_graph):
        # GNN reasons over graph structure
        query_embedding = self.gnn.encode(query_graph)
        
        # No fine-tuning needed
        relevant_nodes = self.gnn.retrieve(
            query_embedding, 
            knowledge_graph
        )
        
        return relevant_nodes
```

---

## Applications

| Domain | Use Case | Benefit |
|--------|----------|---------|
| Medical | Disease-symptom-treatment chains | Safe reasoning paths |
| Legal | Case law relationships | Precedent chains |
| Scientific | Paper citation networks | Research lineage |
| Enterprise | Organizational knowledge | Process flows |

---

## Best Practices

1. **Quality graph construction** - Accurate entity/relation extraction
2. **Appropriate graph depth** - Balance context vs noise
3. **Efficient indexing** - Fast subgraph retrieval
4. **Context formatting** - Clear graph-to-text conversion
5. **Evaluation** - Measure retrieval and generation quality

---

## Comparison with Other Methods

| Method | Relationships | Multi-hop | General Themes |
|--------|--------------|-----------|----------------|
| Standard RAG | ❌ | ❌ | ❌ |
| HyDE | ❌ | ❌ | Partial |
| GraphRAG | ✅ | ✅ | ✅ |
| GFM-RAG | ✅ | ✅ | ✅ |

---

## Examples

### Example 1: Basic Application

**User:** I need to apply GraphRAG: Retrieval-Augmented Generation with Knowledge Graphs to my analysis.

**Agent:** I'll help you apply graph-rag-knowledge-graph. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for graph-rag-knowledge-graph?

**Agent:** Let me search for the latest research and best practices...

## References

- Paper: https://arxiv.org/abs/2501.00309
- GitHub: https://github.com/Graph-RAG/GraphRAG
- Related: Knowledge Graph construction, GNN for reasoning

---

**Created:** 2026-03-28
**Source:** arXiv:2501.00309 - "Retrieval-Augmented Generation with Graphs"