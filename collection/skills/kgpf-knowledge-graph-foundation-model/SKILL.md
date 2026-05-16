---
name: kgpf-knowledge-graph-foundation-model
description: >
  Knowledge Graph Foundation Model using Prior-data Fitted Network (PFN) for in-context
  learning. Unifies transferable relational regularities with inference-time context from
  structured neighborhoods. Use when: building KG reasoning systems, cross-graph transfer
  learning, in-context KG completion, multi-graph pretraining, or zero/few-shot adaptation
  to unseen knowledge graphs. Triggers: knowledge graph foundation model, in-context KG
  reasoning, PFN for graphs, cross-graph transfer, NBFNet neighborhood encoding.
---

# KGPFN: Knowledge Graph Foundation Model via In-Context Learning

## Overview

KGPFN (arXiv:2605.14907) combines two pillars of foundation models for knowledge graphs:
1. **Transferable relational regularities** - learned via multi-graph pretraining
2. **In-context learning at inference time** - conditioning on structured context

## Architecture

### Three-Level Context Encoding

| Level | Component | Purpose |
|-------|-----------|---------|
| **Relation** | Message passing on relation graphs | Cross-graph relational invariances |
| **Local** | Multi-layer NBFNet | Entity neighborhood structure |
| **Global** | PFN with feature + sample attention | Relation-specific global context from retrieved instances |

### Key Design Decisions

**Local Context (NBFNet):**
- Encode query entity neighborhoods via multi-layer NBFNet
- Captures local graph topology around target entities
- Multiple layers = larger receptive field

**Global Context (PFN):**
- Retrieve large set of instances of the query relation + their local neighborhoods
- Aggregate within Prior-data Fitted Network framework
- Combines feature-level and sample-level attention
- Learns when to instantiate reusable patterns vs override with contextual evidence

**Multi-Graph Pretraining:**
- Train on diverse KGs simultaneously
- Model learns transferable relational regularities
- At inference: adapts to unseen graphs via ICL alone

## Implementation Pattern

```python
# 1. Relation Graph Message Passing
# Build relation graphs where nodes = relation types
# edges = co-occurrence patterns across entities
def encode_relations(kg):
    rel_graph = build_relation_cooccurrence(kg)
    rel_embeddings = message_passing(rel_graph)
    return rel_embeddings

# 2. Local Neighborhood Encoding (NBFNet)
def encode_local_context(kg, query_entity, num_hops=3):
    subgraph = extract_k_hop_neighborhood(kg, query_entity, k=num_hops)
    return nbfnet_encode(subgraph, query_entity)

# 3. Global Context Construction (PFN)
def build_global_context(kg, query_relation, k=100):
    instances = retrieve_relation_instances(kg, query_relation, top_k=k)
    local_contexts = [encode_local_context(kg, inst.entity) for inst in instances]
    return pfn_aggregate(local_contexts)  # feature + sample attention

# 4. Inference: Combine all levels
def predict(kg, query):
    rel_emb = encode_relations(kg)
    local_ctx = encode_local_context(kg, query.entity)
    global_ctx = build_global_context(kg, query.relation)
    return combine_and_predict(rel_emb, local_ctx, global_ctx)
```

## When to Use

- **Zero-shot KG completion** on unseen graphs - ICL alone achieves strong results
- **Multi-domain KG reasoning** - pretrain once, adapt via context
- **Few-shot relation learning** - retrieve similar instances as context
- **Cross-graph transfer** - no fine-tuning needed, just context retrieval

## Benchmarks

Tested on 57 KG benchmarks, consistently outperforming competitive fine-tuned KG foundation models through in-context learning alone.

## Resources

- Paper: https://arxiv.org/abs/2605.14907
- Code: https://github.com/HKUST-KnowComp/KGPFN
