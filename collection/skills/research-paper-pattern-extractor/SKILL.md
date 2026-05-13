---
name: research-paper-pattern-extractor
description: "Extract reusable research skill patterns from knowledge graph paper analysis. Uses PageRank, Louvain, and vector search to identify important papers and research clusters, then distills patterns into new skills. Activation: extract research pattern, research skill extractor, 研究模式提炼, paper pattern analysis."
---

# Research Paper Pattern Extractor

## Description
从知识图谱研究论文分析中提炼可复用的技能模式。使用 PageRank、Louvain 社区检测和向量相似度搜索识别重要论文和研究聚类，然后将研究模式提炼为新的技能。

## Activation Keywords
- extract research pattern
- research skill extractor
- 研究模式提炼
- paper pattern analysis
- 论文模式分析
- knowledge graph pattern extraction
- KG pattern mining
- research skill creator
- 学术技能提炼

## Tools Used
- **kg_tool**: 知识图谱分析工具（PageRank、Louvain、搜索）
- **sqlite3**: 直接查询 kg.db 数据库
- **read**: 读取现有技能模板和相关论文
- **write**: 创建新的 SKILL.md 文件
- **exec**: 运行 Python 脚本和命令

## Workflow

### Step 1: Analyze Knowledge Graph

使用知识图谱工具分析论文：

```bash
# 1. 检查统计信息
kg_tool stats kg.db

# 2. 运行 PageRank 找重要论文
kg_tool pagerank kg.db

# 3. 运行 Louvain 找研究聚类
kg_tool louvain kg.db

# 4. 搜索特定主题论文
kg_tool search kg.db "quantum"
kg_tool search kg.db "medical"

# 5. 向量相似度搜索（如果有向量）
kg_tool similar kg.db [entity_id]
```

### Step 2: Extract Key Papers

从 PageRank 结果中获取最重要的实体：

```bash
# 查询 Top 10 实体详情
sqlite3 kg.db "SELECT id, entity_type, name FROM kg_entities WHERE id IN (top_ids);"
```

### Step 3: Identify Research Patterns

分析论文标题和摘要，识别模式：

1. **主题聚类**: Louvain 社区检测显示的研究方向
2. **方法论**: 重复出现的算法、技术、方法
3. **应用领域**: 医学、量子计算、金融等
4. **工具链**: Python、神经网络、模拟器等

### Step 4: Distill Skill Patterns

从论文模式提炼技能：

| Pattern Type | Skill Example |
|--------------|---------------|
| Algorithm Focus | `quantum-algorithm-optimizer` |
| Application Domain | `medical-imaging-analyzer` |
| Tool Integration | `simulation-framework` |
| Methodology | `statistical-analysis-tool` |

### Step 5: Create New Skill

生成新技能文件：

```bash
# 创建技能目录
mkdir -p skills/{skill-name}/{scripts,references}

# 创建 SKILL.md
write skills/{skill-name}/SKILL.md
```

## Skill Creation Template

```markdown
---
name: {skill-name}
description: "{功能描述}. Activation: {触发关键词}."
---

# {Skill Name}

## Description
{详细描述}

## Activation Keywords
- {keyword1}
- {keyword2}
- {keyword3}

## Tools Used
- {tool1}: {用途}
- {tool2}: {用途}

## Workflow
### Step 1: {动作}
{指令}

### Step 2: {动作}
{指令}

## Examples
### Example 1: {场景}
{示例}
```

## Research Patterns Detected

### Pattern 1: Quantum Algorithm Research
**Detection Signals:**
- PageRank 显示 "Quantum Algorithms" 为最重要主题
- 多篇量子计算、量子门、量子纠缠论文
- Louvain 社区检测显示量子聚类

**Distilled Skill:**
- `quantum-algorithm-analyzer`
- 功能：分析量子算法论文，评估复杂度和可行性
- 关键词：quantum algorithm analysis, 量子算法分析

### Pattern 2: Medical AI Application
**Detection Signals:**
- 医学影像、生物医学分析论文
- AI 在医疗诊断中的应用
- PageRank 显示医学相关实体重要性

**Distilled Skill:**
- `medical-ai-research`
- 功能：医学 AI 应用研究分析
- 关键词：medical AI, 医学人工智能

### Pattern 3: Knowledge Graph Analysis
**Detection Signals:**
- 使用 PageRank、Louvain、向量搜索
- 识别重要论文和研究聚类
- 提炼研究模式

**Distilled Skill:**
- `research-pattern-extractor` (本技能)

## Key Metrics

分析知识图谱时关注：

- **Entity Count**: 论文总数
- **Relation Count**: 关系总数
- **Avg Degree**: 平均连接度
- **PageRank Score**: 论文重要性
- **Community ID**: 研究聚类归属

## Best Practices

### 1. 多维度分析
结合 PageRank + Louvain + 向量搜索，全面理解研究结构

### 2. 跨领域发现
寻找跨学科研究（量子 + 医学、AI + 金融等）

### 3. 技能验证
创建新技能后测试其实用性

### 4. 持续更新
定期分析新论文，更新技能库

## Limitations

- 需要 kg.db 有足够数据（>100 论文）
- PageRank/Louvain 需要关系数据
- 向量搜索需要预先生成嵌入
- 技能提炼需要人工判断和验证

## Related Skills

- **quantum-knowledge-graph**: 量子知识图谱
- **skill-extractor**: 技能提炼元技能
- **skill-creator**: 技能创建指南
- **arxiv-search**: arXiv 论文搜索

## Resources

- **kg.db**: 本地知识图谱数据库
- **kg_tool**: 知识图谱分析工具
- **scripts/weekly_topics.py**: 每周主题配置

## Example Usage

### Example 1: 量子研究分析

```
User: "分析知识图谱中的量子研究模式"

Agent Process:
1. kg_tool pagerank kg.db → 发现 "Quantum Algorithms" 最重要
2. kg_tool search kg.db "quantum" → 找到 20+ 量子论文
3. kg_tool louvain kg.db → 发现量子研究聚类
4. 分析论文标题和摘要
5. 提炼 quantum-algorithm-analyzer 技能
6. 创建 SKILL.md 文件
```

### Example 2: 医学 AI 研究

```
User: "提炼医学 AI 研究技能"

Agent Process:
1. kg_tool search kg.db "medical" → 找医学论文
2. 分析论文标题（medical imaging, clinical diagnosis）
3. 识别医学 AI 应用模式
4. 创建 medical-ai-research 技能
```

---

_Last updated: 2026-04-08_