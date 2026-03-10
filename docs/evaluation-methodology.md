# Agent & Skill 评测方法论

## 目的

每日凌晨 03:00 自动评测所有 agents 和 skills，确保质量和实用性。

## 评测流程

### 1. 能力评估 (Capability Assessment)

**评估内容：**
- 核心能力是否完整定义
- 能力是否与角色定位匹配
- 能力是否有实际价值

**评分标准：**
| 等级 | 标准 |
|------|------|
| ⭐⭐⭐⭐⭐ | 能力完整、清晰、有深度 |
| ⭐⭐⭐⭐ | 能力完整、清晰 |
| ⭐⭐⭐ | 能力基本完整 |
| ⭐⭐ | 能力不完整或有遗漏 |
| ⭐ | 能力定义模糊或缺失 |

### 2. 实用性测试 (Practicality Test)

**测试内容：**
- Agent 是否能完成典型任务
- Skill 是否能正确激活和执行
- 输出质量是否符合预期

**测试方法：**
```python
# 测试用例模板
test_cases = [
    {
        "agent": "ml-engineer",
        "task": "Train a classification model on customer churn data",
        "expected": ["数据预处理", "模型训练", "评估报告"],
        "timeout": 300
    },
    {
        "skill": "prompt-optimization",
        "trigger": "优化这个 prompt",
        "expected": ["分析问题", "提供改进建议", "优化后 prompt"],
    }
]
```

### 3. 代码质量 (Code Quality)

**检查项目：**
- [ ] 文档完整性（AGENT.md/SKILL.md）
- [ ] 配置正确性（.yaml 文件）
- [ ] 灵魂定义（SOUL.md）
- [ ] 示例代码质量
- [ ] 测试覆盖率

**质量检查脚本：**
```bash
# 运行验证
python scripts/validate_skill.py

# 代码风格
ruff check collection/
ruff format collection/
```

### 4. 用户反馈 (User Feedback)

**收集方式：**
- 任务成功率统计
- 用户满意度评分
- 错误日志分析
- 改进建议收集

**反馈处理：**
- 高优先级问题：立即修复
- 中优先级问题：纳入下一迭代
- 低优先级问题：记录备查

### 5. 版本更新 (Version Updates)

**检查内容：**
- 依赖工具版本
- 模型版本
- API 变更
- 最佳实践更新

## 评测报告格式

```markdown
# Agent/Skill 评测报告

**日期：** YYYY-MM-DD 03:00
**评测人：** Claude Code

## 评测摘要

| Agent/Skill | 能力 | 实用性 | 代码质量 | 总分 |
|-------------|------|--------|----------|------|
| ml-engineer | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 4.7 |
| security-engineer | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 4.0 |

## 详细发现

### ml-engineer
- ✅ 能力定义完整
- ✅ 文档清晰
- ⚠️ 缺少测试用例

### security-engineer
- ✅ 安全审计能力全面
- ✅ 代码示例实用
- 🔧 建议增加更多渗透测试示例

## 改进建议

1. **ml-engineer**: 添加模型部署测试用例
2. **security-engineer**: 增加 OWASP Top 10 实战示例

## 下一步行动

- [ ] 为 ml-engineer 添加测试用例
- [ ] 更新 security-engineer 的渗透测试示例
```

## 自动化执行

### Cron 配置

```bash
# 每天凌晨 03:00 执行评测
0 3 * * * cd /Users/hiyenwong/projects/ai_projects/ai_collection && claude --print "执行 Agent & Skill 评测" --permission-mode bypassPermissions
```

### 执行脚本

```bash
#!/bin/bash
# evaluate_agents.sh

PROJECT_DIR="/Users/hiyenwong/projects/ai_projects/ai_collection"
REPORT_DIR="$PROJECT_DIR/knowledge/daily"
DATE=$(date +%Y-%m-%d)

# 运行评测
cd $PROJECT_DIR

# 生成评测报告
claude --print "
## 任务：评测所有 Agents 和 Skills

请执行以下评测：

1. 遍历 collection/agents/ 目录下的所有 agents
2. 遍历 collection/skills/ 目录下的所有 skills
3. 对每个 agent/skill 进行：
   - 能力评估
   - 实用性测试
   - 代码质量检查
4. 生成评测报告到 knowledge/daily/$DATE-evaluation.md
5. 提出改进建议

评测标准参考 docs/evaluation-methodology.md
" --permission-mode bypassPermissions

echo "评测完成：$REPORT_DIR/$DATE-evaluation.md"
```

## Review 流程

每次评测后进行 Review：

1. **自动 Review** - Claude Code 自我审查评测报告
2. **手动 Review** - 用户查看报告并确认
3. **改进执行** - 根据建议实施改进
4. **验证闭环** - 确认改进效果

---

**创建时间：** 2026-03-10
**创建者：** Aerial (main agent)