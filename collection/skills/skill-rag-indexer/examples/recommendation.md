# 推荐功能示例

## 基础推荐

```bash
# 为任务推荐技能
skill-rag recommend "我想创建一个新的 OpenClaw agent"
skill-rag recommend "需要分析股票数据"
skill-rag recommend "构建一个全栈 Web 应用"
```

## 带限制的推荐

```bash
# 限制推荐数量
skill-rag recommend "编程" --limit 3

# 只包含特定技能
skill-rag recommend "coding" --include opencode,claude-code

# 排除特定技能
skill-rag recommend "分析" --exclude stock-analysis
```

## 输出格式示例

```
=== Skill Recommendations for Task ===
Task: "创建一个新的 agent"

1. ⭐ tech-cofounder [88.5%]
   ID: tech-cofounder
   Reason: 高度语义匹配
   技术联合创始人，提供创业项目的技术战略和执行指导...

2. 👍 fullstack-engineer [82.3%]
   ID: fullstack-engineer
   Reason: 良好语义匹配
   高级全栈工程师，专注于现代Web开发...
```
