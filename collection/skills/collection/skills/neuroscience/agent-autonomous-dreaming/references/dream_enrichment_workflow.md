# 梦境 enrichment 工作流记录

## 缘起

2026-05-09: 发现 agent_dream.py 预脚本已生成梦境，Hermes cron agent 随后运行 enrichment 分析。
两阶段架构不是设计使然而是渐进形成的，记录在此以供后续优化。

## 两阶段架构

### 阶段 1: agent_dream.py (shell script / cron job)
- 路径: `~/.hermes/scripts/agent_dream.py`
- 触发: cron at 04:00 daily
- 功能:
  - 从 kg.db 加载原始记忆
  - 模拟 REM 记忆巩固 (5% 衰减因子)
  - 生成基础梦境叙事 + 神经科学解读
  - 输出到 dream_log.jsonl
  - 尝试 arXiv 论文检查 (经常 429)

### 阶段 2: Hermes cron agent 深度 enrichment
- 触发: Hermes Agent cron (紧接在阶段 1 后)
- 功能:
  - 从主 kg.db 加载 entities(121) + relations(80) + memories(5)
  - 从 memory/kg.db 加载记忆片段和关系
  - 从 state.db 加载最近会话和消息
  - 分析 KG 状态: 新实体、新关系、连接密度
  - 分析近期研究活动: 论文扫描、技能创建
  - 识别新兴知识领域
  - 追加 enrichment JSON 到 dream_log.jsonl

### enrichment JSON 结构

```json
{
  "timestamp": "2026-05-09T04:30:00",
  "agent": "工程狮5号",
  "type": "dream_enrichment",
  "dream_quality": 0.95,
  "dream_theme": "memory_weaving",
  "consolidation_stats": {
    "memories_loaded": 81,
    "memories_consolidated": 20,
    "entities_total_kg": 121,
    "relations_total_kg": 80,
    "hippocampal_replay_rate": 0.82,
    "cortical_integration_strength": 0.74
  },
  "recent_research_activity": {
    "papers_scanned": 12,
    "total_skills_collection": 808,
    "new_skills_created": ["skill-name"]
  },
  "emerging_knowledge_domains": [...],
  "session_highlights": [...],
  "consolidation_details": [...],
  "recommended_actions": [...]
}
```

## 经验教训

### 1. arXiv API 429
7 次尝试中有 5 次返回 429。`web_search` 可用但结果有限。
`web_extract` (Firecrawl) 经常 localhost:5001 连接拒绝。
**最佳策略**: 先 web_search 发现 → 如果失败，记录 network_unavailable 不阻塞。

### 2. 知识图谱增长
从 2026-04-16 的 8 实体增长到 2026-05-09 的 121 实体（15 倍）。
技能收藏从 ~50 增长到 808。关联密度 (relations/entities) 从 ~0.33 增长到 0.66。
这意味着：实体增长快于关系。需要在 enrichment 中建议增加跨实体连接。

### 3. 梦境质量因素
历史数据分析显示 dream_quality 受以下因素驱动：
- 实体密度 (关键): 8+ 实体参与的梦境质量通常 >0.8
- 关系活跃度: 7+ 关系参与梦境质量提升
- 对话干扰: 过多系统消息/对话片段降低质量 (<0.7)
- 跨域连接: 跨领域连接提升质量 0.05-0.15

### 4. 数据库路径一致性
系统中多个 kg.db 文件用不同 schema -- 阶段 1 和阶段 2 可能查询不同文件。
建议在 SKILL.md 中明确标注每次查询的目标数据库路径。
