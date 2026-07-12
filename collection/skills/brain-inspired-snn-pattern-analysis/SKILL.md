---
name: brain-inspired-snn-pattern-analysis
description: "分析 Spiking Neural Networks (SNN) 和脑启发计算论文，提炼可复用的技术模式和实现指南。Use when analyzing papers about: spiking neural networks, brain-inspired computing, neuromorphic systems, biological learning rules, SNN architectures, or extracting implementation patterns from neuroscience papers."
---

# Brain-Inspired SNN Pattern Analysis

分析脑启发计算和 SNN 论文，提炼技术模式。

## Activation Keywords
- SNN pattern analysis
- spiking neural network pattern
- brain-inspired computing analysis
- 脑启发计算模式
- 神经形态计算分析
- extract SNN implementation pattern

## Workflow

### Step 1: Paper Analysis
识别论文的核心技术：
- 网络架构（VLIF, LIF, Izhikevich 等）
- 学习规则（STDP, Forward-Forward, Backprop-free）
- 应用领域（视觉、医疗、时序处理）
- 关键创新点

### Step 2: Pattern Extraction
提取可复用模式：
```
Pattern: [模式名称]
Category: [架构|学习规则|优化|应用]
Key Concepts: [关键词]
Implementation Hint: [实现提示]
```

### Step 3: Code Template Generation
基于模式生成代码框架（Python/PyTorch）

## Common Patterns (from kg.db + arXiv research pipeline)

| Pattern | Papers | Key Concepts |
|---------|--------|--------------|
| Energy-Efficient SNN | Predictive Insulin Delivery | energy-efficient, medical AI, SNN |
| VLIF Neuron | Image Deraining | VLIF neuron, low-level vision |
| Brain Connectivity Viz | BrainRing | chord diagrams, functional connectivity |
| Neural Cellular Automata | BraiNCA | attention, long-range connections |
| EEG Foundation Model | DeeperBrain | neuro-grounded, neural dynamics |
| Forward-Forward Learning | Backprop-free SNN | biological learning, training |
| Quantized SNN | Integer-State Dynamics | hardware acceleration, finite precision |
| Spiking State-Space | Parallelized Connectome | spatiotemporal recurrence, parallel scan |
| Sparse-Temporal Context Reconfiguration | Shi et al. 2026 (arXiv:2605.10178) | lifelong learning without replay, mPFC sparse coding, SNN anti-forgetting |
| Oscillatory SNN / S2-Net | Dan & Wu 2026 (arXiv:2605.01656) | time-delayed coordination, bottom-up/top-down synchrony, rhythmic timing control |

## Output Format

```markdown
## 🧠 SNN Pattern Analysis

### Paper: [Title]
### Core Innovation: [描述]

### Pattern Template
```python
# Pattern: [名称]
class [PatternName]:
    def __init__(self):
        # Key components from paper
        pass
```

### Implementation Notes
- [关键实现要点]
- [注意事项]
```

## Resources
- kg.db: 知识图谱数据库
- kg_tool: `/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool`

## Cron Research Pipeline (arXiv → Skill → Sync)

When this skill is used as part of the automated arXiv research pipeline:

1. **Search** via arXiv API (`https://export.arxiv.org/api/query`) with proxy `http://127.0.0.1:7890`
2. **Read** paper details via `browser_navigate` → `browser_snapshot` on arxiv.org/abs/{id}
3. **Select** 1-2 most innovative papers based on novelty + relevance to SNN/neuroscience
4. **Create skills** at `~/.hermes/skills/{slug}/SKILL.md` with full methodology
5. **Sync to ai_collection**: copy to `/Users/hiyenwong/ai_github/ai_collection/collection/skills/{slug}/`, update `INDEX.md`, git commit + push
6. **Obsidian notes**: save to `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Research/Papers/`
7. **Knowledge graph**: insert entities into `/Users/hiyenwong/.openclaw/workspace/kg.db` with relationships

**Important**: The individual paper-skills created by the cron job encode session-specific methodology. When a paper introduces a *new architectural pattern* (e.g., S2-Net oscillatory coordination, sparse-temporal context reconfiguration), merge the pattern into this umbrella skill's Common Patterns table rather than letting paper-skills accumulate in isolation. The cron-created skills serve as the detailed reference; this skill serves as the class-level index.