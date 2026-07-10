# KG Research Workflow Examples

## Example 1: Full Research Pipeline

**User Request:**
```
执行 KG 研究流程：搜索最近 SNN 论文，导入知识图谱，生成嵌入，运行算法
```

**Agent Response:**
Following kg-research-workflow:

1. **Paper Search**: Using web_search for arxiv SNN papers
2. **KG Import**: Imported 8 papers with keywords
3. **Embeddings**: Generated 256-dim vectors for 46 entities
4. **PageRank**: Top papers identified:
   - Entity 11: Taming the Exponential (score: 0.069)
   - Entity 12: TensorPool (score: 0.068)
5. **Vector Search**: Found relevant SNN papers and keywords
6. **Pattern Extraction**: Identified VLIF neuron pattern

---

## Example 2: Paper Import Only

**User Request:**
```
导入这些论文到 KG：
- 2603.27589: Energy-Efficient SNN Architecture
- 2601.06134: DeeperBrain EEG Foundation Model
```

**Agent Response:**
```python
# Create import script
papers = [
    {"arxiv_id": "2603.27589", ...},
    {"arxiv_id": "2601.06134", ...}
]

# Import to kg_entities, create keyword relations
# Result: 2 papers + 12 keyword entities added
```

---

## Example 3: KG Analysis Only

**User Request:**
```
分析知识图谱：找最重要的论文，搜索 SNN 相关论文
```

**Agent Response:**
```bash
kg_tool pagerank kg.db
# Top: Entity 11 (0.069), Entity 12 (0.068)

python3 scripts/vector_search.py "spiking neural network"
# Results: VLIF neuron, SNN keyword, TensorPool paper
```

---

## Example 4: Skill Extraction from KG

**User Request:**
```
从知识图谱论文中提取技能模式，创建新技能
```

**Agent Response:**
Analysis of top papers reveals pattern:
- **VLIF neuron**: Specialized LIF for visual tasks
- **Forward-forward**: Alternative training without backprop
- **Energy-efficient design**: Low-power SNN architectures

Creating skill: `snn-design-patterns`