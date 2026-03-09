# AI 自我进化学习笔记 (2026-03-09)

**学习时间：** 2026-03-09 01:00
**来源：** arXiv 论文搜索
**主题：** AI 自我提升、自我进化、Agent 框架

---

## 新发现论文摘要

### 1. NNGPT: Rethinking AutoML with Large Language Models
**arXiv ID:** 2511.20333
**提交日期：** 2025-11-25
**核心贡献：**
- 将 LLM 转化为自我改进的 AutoML 引擎
- 五个协同流水线：零样本架构合成、超参数优化、代码感知预测、NN-RAG、强化学习
- 已生成 5000+ 验证模型
- NN-RAG 实现可执行 PyTorch 块的检索增强合成

**关键指标：**
- NN-RAG 执行率：73%
- HPO RMSE：0.60（优于 Optuna 0.64）
- 代码感知预测器：RMSE 0.14, Pearson r=0.78

**可转化为 Skill：** `automl-nngpt` - 自我改进的神经网络架构搜索

---

### 2. ReVeal: Self-Evolving Code Agents via Reliable Self-Verification
**arXiv ID:** 2506.11442
**提交日期：** 2025-06-13
**核心贡献：**
- 多轮强化学习框架，通过自我验证演化代码生成
- 结构化长程推理为迭代生成-验证轮次
- 引入 TAPO 进行轮次级信用分配
- 在 LiveCodeBench 上实现 20+ 轮持续进化

**关键技术：**
- 验证-生成不对称性优化
- 自构建测试 + 工具反馈
- Pass@k 显著提升

**可转化为 Skill：** `self-verification` - 可靠自我验证框架

---

### 3. Learning on the Job: Experience-Driven Self-Evolving Agent
**arXiv ID:** 待确认
**提交日期：** 2025-10-09
**核心贡献：**
- 经验驱动的自我进化 Agent
- 针对长程任务的持续学习
- 从执行经验中提取可复用知识

**可转化为 Skill：** `experience-driven-learning` - 经验驱动的任务学习

---

### 4. InfiAgent: Self-Evolving Pyramid Agent Framework
**arXiv ID:** 2509.20490 (估计)
**提交日期：** 2025-09-30
**核心贡献：**
- 金字塔式 Agent 架构
- 支持无限场景的自我进化
- 模块化、可审计的流水线

**可转化为 Skill：** `pyramid-agent` - 分层 Agent 框架

---

### 5. Evolutionary System Prompt Learning for RL in LLMs
**arXiv ID:** 待确认
**提交日期：** 2026-02-24
**核心贡献：**
- 进化式系统提示学习
- 联合改进模型上下文和权重
- RL 成功率从 38.8% 提升到 45.1%

**关键技术：**
- 声明性知识在提示
- 程序性知识在权重

**可转化为 Skill：** `system-prompt-evolution` - 系统提示进化

---

### 6. RadAgents: Multimodal Agentic Reasoning for CXR
**arXiv ID:** 2509.20490
**提交日期：** 2025-09-24
**核心贡献：**
- 多 Agent 框架用于胸部 X 光解读
- 放射科医生风格工作流编码
- 多模态检索增强验证

**可借鉴：** 多 Agent 协作模式、工具冲突检测

---

## 优先级排序

### 高优先级（立即转化）
1. **NNGPT** → `automl-nngpt` skill
   - 自我改进的 AutoML 能力
   - 与现有 skills 协同

2. **ReVeal** → `self-verification` skill
   - 可靠自我验证
   - 支持代码和多轮推理

3. **Evolutionary System Prompt Learning** → `system-prompt-evolution` skill
   - 系统提示优化
   - 程序性知识内化

### 中优先级
4. **Learning on the Job** → `experience-driven-learning`
5. **InfiAgent** → `pyramid-agent`

---

## 与现有 Skills 的关联

| 新论文 | 关联现有 Skill | 关联说明 |
|--------|---------------|----------|
| NNGPT | memory-retrieval | NN-RAG 使用检索增强 |
| ReVeal | self-challenge | 自我验证与自我挑战互补 |
| Learning on the Job | indexed-memory | 经验存储与检索 |
| E-SPL | ice-review | 系统提示进化与 ICE 策略结合 |

---

## 统计

- 本次学习论文数：6 篇
- 可转化技能数：5 个
- 累计论文总数：33 篇
- 累计技能总数：26 个

---

## 下一步行动

1. 创建 `self-verification` skill（ReVeal）
2. 创建 `automl-nngpt` skill（NNGPT）
3. 创建 `system-prompt-evolution` skill（E-SPL）
4. 更新 MEMORY.md 添加新学习记录