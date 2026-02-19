# Tech Co-Founder Agent - Configuration Summary

## ✅ 配置完成

### 已配置的工具

| 工具 | 配置状态 | 配置文件 |
|------|---------|---------|
| **OpenClaw** | ✅ 已配置 | `.openclaw-skill.md` |
| **Claude Code** | ✅ Agent Teams 已启用 | UI 配置 |
| **Codex** | ✅ Skills 已添加 | `.codex-skill.md` |
| **OpenCode** | ⏳ 待配置 | - |

---

## 🚀 使用方式

### 1. OpenClaw

```python
sessions_spawn(
    task="Build a customer support chatbot platform",
    agentId="tech-cofounder",
    model="claude-sonnet-4.5",
    thinking="high",
    runTimeoutSeconds=600,
    cleanup="keep"
)
```

**或使用技能触发**：

```
在消息中包含关键词：
- "build a"
- "create"
- "implement"
- "turn this into working code"
```

### 2. Claude Code

1. 在 Claude Code UI 中，进入 **Settings → Agent Teams**
2. 创建新的 Team：`tech-cofounder-team`
3. 添加 agents：
   - **Product Owner** (你)
   - **Tech Co-Founder Builder** (tech-cofounder)
4. 使用 **kickoff.md** 模板提供工作订单

**工作流程**：

```
你 (Product Owner) → [提供 kickoff.md 工作订单]
                      ↓
Tech Co-Founder (Builder) → [Phase A: Plan]
                           → [等待批准]
                           → [Phase B: Build]
                           → [Phase C: Polish]
                           → [Phase D: Handoff]
                           → [返回完整交付物]
```

### 3. Codex

1. 打开 Codex 应用
2. 在 Skills 中启用 `tech-cofounder`
3. 在对话中自然地使用：

```
User: "Build a note-taking CLI tool"

Codex (with tech-cofounder skill):
Phase A - Plan:
[展示计划]

User: "OK, go ahead"

Codex:
Phase B - Implement:
1) What I shipped:
   - mynotes command
   - Commands: create, list, show, edit

2) How to run:
npm install -g .
mynotes create "Buy milk"

3) Notes:
[...]

4) Next step: [下一步]
```

---

## 📋 工作订单模板

使用 `examples/kickoff.md` 提供完整的工作订单：

```markdown
# Project Kickoff

## 1. Product Overview
- Name: [Product name]
- Description: [一句话描述]
- Target Users: [用户群体]

## 2. Problem Statement
[问题是什么？为什么需要？]

## 3. V1 Scope (Must Have)
- Feature 1
- Feature 2
- Feature 3

## 4. Technical Constraints
- Platform: Web/Mobile/CLI
- Stack: [前端/后端/数据库]
- Budget: [预算]
- Timeline: [时间线]

## 5. Deployment
- Required: Yes/No
- Platform: Vercel/AWS/Local

## 6. Autonomy
- Low/Medium/High (推荐: Medium)
```

---

## 🎯 工作流程

### Phase A: Plan-to-Build Brief (计划阶段)

**Agent 输出**：
```
1. Scope restatement (5-10 bullets)
2. Assumptions/defaults
3. Blocking decisions
4. Build plan with stages
```

**你的行动**：
- 审阅计划
- 提出问题（如果需要）
- 批准继续

### Phase B: Implement (构建阶段)

**Agent 输出**：
```
1. Concrete artifacts (files/code)
2. How to run + how to test
3. Status update + next step
4. Basic validation
```

**你的行动**：
- 测试交付物
- 提供反馈
- 批准继续到下一阶段

### Phase C: Polish (打磨阶段)

**Agent 输出**：
```
1. Error handling
2. Code structure (lint/format)
3. Performance checks
```

**你的行动**：
- 审查质量
- 确认无遗漏

### Phase D: Handoff (交付阶段)

**Agent 输出**：
```
1. README (setup/run/test/deploy)
2. Maintenance notes
3. V2 suggestions
```

**你的行动**：
- 验证交付物
- 开始使用/部署

---

## ✨ 关键特性

### ✅ 分阶段交付
- 每个阶段都有明确的产出
- 你可以看到进度
- 可以在任意阶段叫停或调整

### ✅ 决策审批
- 重大决策需要你的批准
- Agent 提供选项 + 推荐
- 避免错误的技术选择

### ✅ 完整交付物
- 代码
- README
- 测试
- 部署指南
- 维护说明

### ✅ 可维护性
- 清晰的代码结构
- 详细的注释
- 完整的文档

---

## 🎨 工作示例

### 示例 1: Web App

**你**：
```
Build a customer support chatbot platform.
```

**Tech Co-Founder**:
```
Phase A - Plan:

Scope:
- User-facing chat widget (react)
- Admin dashboard (next.js)
- Backend API (fastapi)
- Real-time messaging (socket.io)
- Knowledge base integration
- User management

Assumptions:
- Stack: Next.js + Supabase
- Auth: Supabase Auth
- Database: Supabase
- Hosting: Vercel

Blocking decisions:
- None (default stack works)

Build Plan:
1. Setup Next.js + Supabase
2. Create authentication
3. Build chat widget
4. Create admin dashboard
5. Implement real-time messaging
6. Add KB integration

[等待批准...]
```

### 示例 2: CLI Tool

**你**：
```
Create a note-taking CLI tool.
```

**Tech Co-Founder**:
```
1) What I shipped:
   - mynotes command
   - Commands: create, list, show, edit, delete
   - Storage: JSON file in ~/.mynotes/
   - Config: ~/.mynotes/config.yml

2) How to run:
npm install -g .
mynotes create "Buy milk"
mynotes list
mynotes show 1

3) Notes:
   - Data file: ~/.mynotes/data.json
   - No API needed (local storage)
   - Edit with your preferred editor

4) Next step:
   - Add tests
   - Make it colorized
   - Add search functionality
```

---

## 📚 文件结构

```
tech-cofounder/
├── AGENT.md                    # Agent 定义
├── README.md                   # 简要说明
├── .agent-team-config.md       # Agent Teams 配置总结
├── .codex-skill.md             # Codex 技能文件
├── .openclaw-skill.md          # OpenClaw 技能文件
├── CONFIGURATION.md            # 本文件
├── examples/
│   ├── kickoff.md             # 工作订单模板
│   └── work-order.md          # 简短工作订单
├── assets/
└── references/
```

---

## 🎓 使用建议

### 1. 从简单项目开始

**建议**：
```
✅ Good:
- Build a note-taking CLI
- Create a todo list web app
- Implement a password generator

❌ Too complex:
- Build a full e-commerce platform
- Create a social media app
- Build a complex SaaS with multiple features
```

### 2. 提供清晰的要求

**好的要求**：
```
✅ "Build a CLI tool for managing todos.
   - Create, list, complete todos
   - Store in local JSON file
   - Simple and clean"
```

**不够清晰**：
```
❌ "Build something"
❌ "Make it good"
❌ "Create a website"
```

### 3. 参与决策

**建议**：
- Phase A 必须审查并批准
- 重大技术选择要参与
- 测试每个阶段的输出

---

## 🔄 后续扩展

### 可以添加的 Agent

1. **Code Reviewer** (代码审查员)
   - 审查代码质量
   - 提供改进建议
   - 自动化测试

2. **Tester** (测试员)
   - 编写测试用例
   - 自动化测试
   - 质量报告

3. **Docs Writer** (文档撰写者)
   - 编写 API 文档
   - 生成 README
   - 创建教程

4. **DevOps Engineer** (运维工程师)
   - Docker 配置
   - CI/CD 流程
   - 部署脚本

### Agent Teams 示例

```
Product Owner (你)
    ↓
Tech Co-Founder Builder (当前)
    ↓
   (测试完成)
    ↓
Code Reviewer (审查代码)
    ↓
   (文档完成)
    ↓
Docs Writer (编写文档)
    ↓
   (部署完成)
    ↓
DevOps Engineer (部署上线)
```

---

## 💡 提示

- 使用 `kickoff.md` 模板确保信息完整
- Phase A 一定要等待批准再继续
- 重大技术决策需要你的参与
- 每个阶段都要测试后再继续

---

## 📞 问题？

如果遇到问题：

1. **Agent 不知道做什么** → 使用 kickoff.md 模板
2. **技术选择错误** → 在 Phase A 提出选项，等待批准
3. **交付物不符合** → 给出明确反馈，要求修改
4. **进度太慢** → 询问是否需要调整优先级或范围

---

**配置完成时间**: 2026-02-18
**配置者**: OpenClaw Assistant
