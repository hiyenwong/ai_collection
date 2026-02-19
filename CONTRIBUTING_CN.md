# 贡献指南

感谢你对 AI Collection 项目的关注！本仓库是一个社区驱动的 OpenClaw 代理和技能集合。

## 贡献类型

我们欢迎以下方面的贡献：

### 1. 添加新代理
- 创建具有特定用途的新代理
- 记录其能力和使用方法
- 提供示例和配置

### 2. 添加新技能
- 创建扩展 OpenClaw 能力的技能
- 编写完整的 SKILL.md 文档
- 包含示例和参考资料

### 3. 改进文档
- 修正拼写错误或澄清现有文档
- 添加教程或指南
- 将文档翻译成其他语言

### 4. 问题报告
- 报告现有代理或技能的问题
- 提出改进建议或新功能

### 5. 示例和模板
- 添加真实使用场景的示例
- 为常见用例创建新模板

## 快速开始

### 1. Fork 并克隆

```bash
# 在 GitHub 上 Fork 本仓库
git clone https://github.com/你的用户名/ai_collection.git
cd ai_collection
```

### 2. 创建分支

```bash
git checkout -b feat/your-feature-name
# 或
git checkout -b fix/your-fix-name
```

### 3. 进行修改

请遵循[代理创建指南](./docs/agents/creation-guide.md)或[技能创建指南](./docs/skills/creation-guide.md)。

### 4. 提交修改

```bash
git add .
git commit -m "feat: add new data-analysis agent"

# 或修复
git commit -m "fix: correct skill activation keywords"
```

### 5. 推送并创建 PR

```bash
git push origin feat/your-feature-name
```

然后在 GitHub 上创建 Pull Request。

## 贡献规范

### 代理

**什么样的代理贡献是有价值的：**

- ✅ 目的明确且具体
- ✅ 文档完善的系统提示
- ✅ 经过多种任务测试
- ✅ 包含使用示例
- ✅ 选择合适的模型
- ✅ 有错误处理策略

**代理检查清单：**

- [ ] 在 `collection/agents/agent-name/` 创建目录
- [ ] 创建包含所有必需章节的 `AGENT.md`
- [ ] 在 `examples/` 添加使用示例
- [ ] 使用 `sessions_spawn` 测试代理
- [ ] 在主 `AGENTS.md` 中更新条目
- [ ] 如需要，添加参考资料

### 技能

**什么样的技能贡献是有价值的：**

- ✅ 具体、不常见的激活关键词
- ✅ 全面的、分步的指令
- ✅ 常见问题的错误处理
- ✅ 多个使用示例
- ✅ 参考文档
- ✅ 经过各种提示词测试

**技能检查清单：**

- [ ] 在 `collection/skills/skill-name/` 创建目录
- [ ] 创建包含所有必需章节的 `SKILL.md`
- [ ] 在 `examples/` 添加使用示例
- [ ] 如需要，在 `references/` 添加参考文档
- [ ] 如适用，在 `scripts/` 添加辅助脚本
- [ ] 在主 `SKILLS.md` 中更新条目
- [ ] 使用触发关键词测试技能激活

## 代码风格

### Markdown

- 使用一致的标题层级
- 为代码块包含代码围栏
- 为图片添加 alt 文本
- 每行保持在 100 字符以内

### Python/脚本文件

- 遵循 PEP 8 风格指南
- 使用描述性变量名
- 为函数添加文档字符串
- 包含错误处理

### 注释

- 解释"为什么"，而不是"是什么"
- 保持注释简洁
- 单行注释使用 `#`
- 多行文档字符串使用 `"""`

## 文档标准

### AGENT.md 必须包含

```markdown
# 代理名称

## 目的
[清晰的描述]

## 模型
- 主要: [模型]
- 备选: [模型]

## 工具
- [工具]: [用途]

## 技能
- [技能]: [描述]

## 系统提示
```
[详细提示]
```

## 激活方式
[代理如何被激活]

## 使用示例
[示例]

## 配置
[JSON 配置]

## 最佳实践
[列表]
```

### SKILL.md 必须包含

```markdown
# 技能名称

## 描述
[简短描述]

## 激活关键词
- [关键词1]
- [关键词2]

## 使用的工具
- [工具]: [用途]

## 安装
[如适用]

## 使用模式
[示例]

## 代理指令
[分步说明]

## 错误处理
[常见错误]

## 示例
[真实示例]

## 资源
[链接]
```

## 测试

### 测试代理

1. **手动测试:**
```python
# 简单任务测试
sessions_spawn(task="测试任务", agentId="your-agent")

# 复杂任务测试
sessions_spawn(task="复杂任务带参数", agentId="your-agent", thinking="high")
```

2. **检查:**
- 代理遵循系统提示
- 使用适当的工具
- 结果正确传递
- 错误被优雅处理

### 测试技能

1. **触发测试:**
```
User: "[使用触发关键词]"
```

2. **验证:**
- 代理读取 SKILL.md
- 指令被遵循
- 工具使用正确
- 常见错误被处理

## Pull Request 流程

### PR 标题格式

- **新代理:** `feat(agent): add new data-analysis agent`
- **新技能:** `feat(skill): add new slack-integration skill`
- **Bug 修复:** `fix(agent): resolve timeout issue in research-agent`
- **文档:** `docs: update agent creation guide`
- **重构:** `refactor(skills): improve error handling`

### PR 描述

```markdown
## 描述
[变更简要描述]

## 变更
- [ ] 添加新代理/技能
- [ ] 更新文档
- [ ] 添加示例
- [ ] 修复 Bug

## 测试
[描述如何测试你的变更]

## 截图（如适用）
[附上截图]

## 相关 Issue
Closes #123
```

## 审查流程

### 1. 自动检查
   - CI/CD 测试通过
   - 无 linting 错误

### 2. 人工审查
   - 代码质量
   - 文档完整性
   - 示例准确性
   - 整体实用性

### 3. 批准
   - 至少一名维护者批准
   - 解决所有审查意见

## 社区准则

### 互相尊重

- 欢迎新贡献者
- 提供建设性反馈
- 认可优秀工作
- 帮助他人学习

### 协作精神

- 公开讨论想法
- 在重大变更上寻求共识
- 认可贡献者
- 分享知识

### 保持耐心

- 审查可能需要时间
- 维护者是志愿者
- 不清楚时提问

## 获取帮助

如果需要贡献方面的帮助：

1. **查看文档：**
   - [代理创建指南](./docs/agents/creation-guide.md)
   - [技能创建指南](./docs/skills/creation-guide.md)
   - `collection/` 中的现有示例

2. **提交 Issue：**
   - 清楚地描述你的问题
   - 包含你尝试过的内容
   - 引用现有的代理/技能

3. **加入社区：**
   - [OpenClaw Discord](https://discord.gg/clawd)
   - 提交标记为"question"的 issue

## 认可

所有贡献者将在以下地方获得认可：

- 本 CONTRIBUTING.md 文件
- 项目 README.md
- 单个代理/技能文档

## 许可证

通过贡献，你同意你的贡献将在与仓库相同的许可证（MIT）下授权。

---

感谢你的贡献！🚀
