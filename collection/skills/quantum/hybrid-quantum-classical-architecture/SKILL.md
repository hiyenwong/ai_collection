---
name: hybrid-quantum-classical-architecture
description: "Design and optimization of hybrid quantum-classical computing system architectures. Includes dataflow frameworks, fault-tolerant design, resource efficiency optimization, automated architecture search, and quantum ML application patterns. Use when: (1) designing quantum computing systems, (2) optimizing hybrid quantum-classical architectures, (3) implementing fault-tolerant quantum systems, (4) searching for optimal quantum architectures, (5) building hybrid quantum ML pipelines for medical/finance applications, or (6) working with quantum system engineering concepts."
---

# Hybrid Quantum-Classical Architecture

Design and optimize hybrid quantum-classical computing system architectures with focus on dataflow, fault tolerance, resource efficiency, automated architecture search, and quantum ML application patterns.

## Core Concepts

### 1. Hybrid Architecture Types

- **Dataflow Frameworks**: Quantum-classical data pipelines (e.g., Tierkreis)
- **Fault-Tolerant Systems**: Error correction with resource constraints (e.g., LSQCA)
- **Modular Hybrid Systems**: Spin-optical, photon-matter combinations
- **Automated Search**: ML-driven architecture optimization
- **Quantum ML Pipelines**: Hybrid quantum-classical models for diagnosis/classification

### 2. Key Design Patterns

**Pattern A: Dataflow-Centric**
```
Classical Preprocessing → Quantum Execution → Classical Postprocessing
                      ↓
                  Error Correction Layer
```

**Pattern B: Resource-Efficient FTQC**
```
Load/Store Architecture → Logical Operations → Memory Management
                      ↓
                  Qubit Connectivity Optimization
```

**Pattern C: Modular Hybrid**
```
Module 1 (Spin) + Module 2 (Optical) → Entangling Interface → Scalable Architecture
```

**Pattern D: Quantum ML Feature Fusion**
```
Classical Backbone (ResNet/CNN) → Feature Extract → Quantum Circuit (VQC) → Measurement → Classifier
```
- **SHF**: Static Hybrid Fusion — offline extraction, simple concatenation
- **DHF**: Dynamic Hybrid Fusion — end-to-end co-adaptation
- **TSHF**: Temperature-Scaled Hybrid Fusion — learnable scalar for gradient balance (best: 87.82% acc on BreastMNIST)
- **Constraint**: Qubit count must match latent dimension for stable training

**Pattern E: Tensor-Network Quantum Processing** (NISQ-constrained systems)
```
High-D Input → Tensor-Network Compression (TTN/MPS/MERA) → Compact Latent → Small-Qubit QC → Readout
```
- TTN+Quantum-Enhanced-Processor is the most balanced combination
- Serves dual role: enables small-qubit processing AND reduces communication overhead in federated settings

## Tools

### Knowledge Graph Integration

Use sqlite3 directly on kg.db (NOT kg_tool subcommands — they don't exist for pagerank/louvain):

```bash
# Query papers
sqlite3 kg.db "SELECT id, title FROM kg_entities WHERE category LIKE '%quant%'"

# Check relations
sqlite3 kg.db "SELECT source, target, type, weight FROM kg_relations LIMIT 10"
```

kg.db path: `/Users/hiyenwong/.openclaw/workspace/kg.db`

### ArXiv Search

Search for latest quantum architecture papers (HTTPS required — HTTP blocked by security scanner):

```bash
curl -s "https://export.arxiv.org/api/query?search_query=all:quantum+architecture&max_results=5" --proxy http://127.0.0.1:7890
```

## Workflow

### Step 1: Identify Architecture Requirements

Analyze the problem to determine:
- **Compute Model**: Quantum-only vs hybrid
- **Fault Tolerance Level**: Required error rates
- **Resource Constraints**: Qubit count, connectivity
- **Performance Goals**: Speedup targets, accuracy requirements

### Step 2: Survey Existing Architectures

Search knowledge graph for similar approaches, design patterns, and key papers.

### Step 3: Design Architecture

Choose appropriate pattern based on constraints:
- Dataflow for cloud/hybrid execution
- LSQCA for resource-constrained FTQC
- Modular for heterogeneous systems
- Pattern D (feature fusion) for quantum ML classification tasks
- Pattern E (tensor-network compression) for NISQ-constrained or federated settings

### Step 4: Evaluate Architecture

Metrics: resource efficiency (qubits per logical op), error rates, scalability, flexibility.

### Step 5: Iterate and Optimize

Use automated search: QAS, unsupervised representation learning, RL optimization.

## References

- **Dataflow**: See [references/tierkreis.md](references/tierkreis.md) for Tierkreis framework
- **Fault Tolerance**: See [references/lsqca.md](references/lsqca.md) for LSQCA architecture
- **Modular Systems**: See [references/spin-optical.md](references/spin-optical.md) for hybrid systems
- **Automated Search**: See [references/qas.md](references/qas.md) for architecture search methods
- **Quantum ML**: See [references/quantum-ml-patterns.md](references/quantum-ml-patterns.md) for hybrid ML architectures

## Examples

### Example 1: Design Cloud Quantum Platform

**User**: "Design a cloud-accessible quantum computing platform"

**Workflow**:
1. Requirements: Cloud access, multiple users, job scheduling
2. Survey: Tierkreis (dataflow), Tianyan (cloud platform)
3. Design: Dataflow architecture with classical job scheduler
4. Evaluate: User concurrency, job throughput, error rates
5. Iterate: Optimize scheduling with QAS

### Example 2: Hybrid Quantum ML for Medical Diagnosis

**User**: "Build a hybrid quantum-classical model for breast cancer classification"

**Workflow**:
1. Requirements: Medical image input, clinical-grade accuracy
2. Choose Pattern D (feature fusion) with TSHF strategy
3. Design: ResNet backbone → 4-qubit VQC → TSHF fusion → classifier
4. Evaluate: Accuracy, F1, AUC-ROC on BreastMNIST
5. If NISQ-constrained: Add Pattern E (TTN compression) before quantum circuit

## Related Skills

- `arxiv-search`: Find quantum architecture papers
- `quantum-ml-research`: Quantum ML research and paper analysis
- `skill-extractor`: Extract design patterns from papers

## Notes

- arxiv API requires HTTPS (HTTP blocked by security scanner)
- web_extract blocks arxiv URLs — use curl + XML parsing instead
- kg.db path: `/Users/hiyenwong/.openclaw/workspace/kg.db`
- No kg_tool subcommands for pagerank/louvain — implement in Python with sqlite3
