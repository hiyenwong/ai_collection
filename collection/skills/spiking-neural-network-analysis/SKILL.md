---
name: spiking-neural-network-analysis
version: v1.0.0
last_updated: 2026-04-06
description: Analyze Spiking Neural Network (SNN) papers, extract technical patterns from knowledge graph, and identify reusable research methodologies for neuromorphic computing.
---

# Spiking Neural Network Analysis

Analyze SNN research papers from knowledge graph and extract reusable technical patterns.

## Activation Keywords

- spiking neural network
- SNN analysis
- 脉冲神经网络分析
- spiking neuron
- neuromorphic computing
- SNN papers

## Tools Used

- `exec` - Run kg_tool and sqlite3 commands
- `read` - Read skill docs and paper content
- `write` - Save analysis reports

## Workflow Decision Tree

```
User Request → Identify Task Type
├── Search Papers → Search kg.db for SNN papers
├── Analyze Patterns → Extract technical patterns
├── Knowledge Graph → Run PageRank/Louvain/Similarity
└── Generate Report → Create analysis summary
```

## Core Commands

### Step 1: Search SNN Entities

```bash
# Search knowledge graph
sqlite3 /Users/hiyenwong/wiki/kg.db \
  "SELECT id, name FROM kg_entities WHERE name LIKE '%spiking%' OR name LIKE '%neuromorphic%'"
```

### Step 2: Get Paper Details

```bash
# Get paper properties (keywords, topics, category)
sqlite3 /Users/hiyenwong/wiki/kg.db \
  "SELECT id, name, properties FROM kg_entities WHERE entity_type='paper' AND name LIKE '%spiking%'"
```

### Step 3: Knowledge Graph Analysis

```bash
# PageRank
/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool pagerank --limit 10

# Community detection
/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool communities --limit 10

# Search
/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool search --query "spiking neural" --limit 10
```

### Step 4: Extract Technical Patterns

Common SNN patterns:
- **energy-efficient** - Energy optimization
- **brain-inspired** - Biological inspiration
- **forward-forward** - Biologically plausible learning
- **backpropagation-free** - No backpropagation
- **temporal dynamics** - Time-series processing
- **low-latency** - Fast inference

## Usage Examples

### Example 1: Basic Analysis

```
User: "分析 SNN 论文"

Execute:
1. Search "spiking neural" papers
2. Get Top 5 paper properties
3. Run pagerank
4. Extract patterns
5. Generate report
```

### Example 2: Pattern Extraction

```
User: "从 SNN 论文中提取技术模式"

Execute:
1. List all SNN papers
2. Parse keywords from properties
3. Identify common patterns
4. Create pattern summary
```

### Example 3: Cross-domain Analysis

```
User: "找出与 SNN 相关的量子计算论文"

Execute:
1. Search "spiking" AND "quantum"
2. Find intersection entities
3. Analyze hybrid approaches
```

### Key Findings from Analysis

#### Top SNN Papers in KG

| Paper | Category | Pattern |
|-------|----------|---------|
| Energy-Efficient SNN | Medical AI | energy-efficient |
| Brain-Inspired Computing | Neuromorphic | brain-inspired |
| PSPM (Pre-Synaptic Pool) | Supervised Learning | forward-forward |

#### D2E Transfer (Direct-to-Event SNN Transfer)

**arXiv: 2605.07207** — Luu et al. (2026), IEEE Signal Processing Letters

A critical SNN deployment pattern: converting direct-coded SNNs (floating-point inputs) to event-based representations (TTFS) for neuromorphic hardware.

**Core approach**: Self-Knowledge Distillation (SKD) — use the pretrained direct-coded SNN as its own teacher to guide event-based finetuning via KL-divergence regularization.

**Key theorem**: Cross-domain accuracy gap bounded by KL divergence between teacher/student output distributions + TV distance between input distributions.

**Performance**: SKD recovers 45-51pp on CIFAR-10 (vs naive TSF's 30-49pp), consistently outperforms across 9 architectures.

**Theoretical limits**: ~60% of input entropy is lost in TTFS encoding — even optimal transfer cannot match direct-coded teacher. Expect 15-20pp ceiling gap.

**Pitfalls**:
- Deep architectures suffer exponential spike rate collapse across layers
- Temperature scaling is critical for KL distillation effectiveness
- DVS sensor encoding gap is even larger than TTFS

#### SNN-Quantum Intersection

- Hybrid spiking-quantum CNN
- Quantum memristor for brain computing
- Neural operator quantum states
- **Qutrit entropy estimation via CNN** (arXiv: 2606.20504) — Classical CNN estimates von Neumann entropy in multi-qutrit systems using only 12.5% of full tomography measurements. See `qutrit-entropy-neural-estimation` skill.

## Key Recent Findings (2026-06-22)

### Hybrid ANN-SNN Pipeline with Local Plasticity (arXiv: 2606.20151)

**Core innovation**: Couples pretrained EfficientNet encoder with CoLaNET spiking classifier via rate-coding. Trains SNN using local biologically-inspired learning rules, bypassing end-to-end backpropagation.

**Performance**: 99.09% on 64-class ImageNet benchmark — on par with conventional deep networks.

**Why it matters**: Demonstrates that pretrained ANN features + local plasticity can replace full backpropagation, enabling biologically-plausible yet high-performance SNNs.

**Pattern**: `Pretrained Encoder → Rate Coding → Local Learning SNN` — modular, energy-efficient, no gradient transport.

### Biological Plausibility Assessment Framework (arXiv: 2606.17853)

**Core innovation**: Automated black-box assessment of spiking neuron models using Izhikevich firing pattern classification. Encodes 20 canonical patterns as objective functions for optimization.

**Implementation**: Python/PyTorch/Norse compatible. Treats neuron models as black boxes — no analytical modeling required.

**Why it matters**: Provides empirical, systematic way to quantify "how biological" a neuron model is. Useful for comparing neuromorphic hardware designs.

**Pattern**: `Model → Pattern Encoding → Black-Box Optimization → Plausibility Score`

## Cross-domain extensions

### Quantum-SNN Fusion
SNNs can be augmented with quantum computing for energy-efficient high-performance tasks:
- **QDS-SNN**: Quantum deep supervision + TSA-LIF neurons (arXiv: 2606.07657)
- **QACM**: Quantum-Assisted Classifier Modules using superposition/entanglement
- See `quantum-neuromorphic-computing` skill for the full methodology

## Related Skills

- `brain-connectivity-analysis` - Brain network analysis
- `quantum-neural-hybrid` - Quantum-classical NN
- `quantized-snn-hardware-optimization` - Hardware acceleration

## Limitations

- Requires kg.db with SNN papers
- Vector embeddings needed for similarity search
- Manual pattern interpretation

## Resources

- **Knowledge Graph**: `/Users/hiyenwong/wiki/kg.db`
- **KG Tool**: `/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool`
- **Daily Research**: `memory/2026-04-06.md`
- **Reference Files**:
  - `references/functional-ensembles-1fc-groups.md` - 1FC (First-order Functional Connectivity) groups framework from arXiv 2606.00073. Documents computational units in deep SNNs through inter-layer functional connectivity analysis, including methodology, experimental findings, and applications for network debugging, architecture optimization, and transfer learning.