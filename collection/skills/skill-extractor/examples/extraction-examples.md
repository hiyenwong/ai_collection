# Skill Extraction Examples

This document contains real-world examples of skill extraction patterns.

## Example 1: Stock Analysis Skill

**Context:**
User repeatedly requested stock analysis with technical indicators.

**Conversation Pattern:**
```
User: "分析 600519 贵州茅台最近 60 天的走势"
Agent: [Fetches data, calculates MA, MACD, KDJ, generates chart]

User: "查看 000858 五粮液的技术指标"
Agent: [Fetches data, calculates indicators, shows results]

User: "对比分析 贵州茅台、五粮液、泸州老窖"
Agent: [Fetches all data, compares, generates table]
```

**Extracted Skill:** `stock-analysis`

**Key Elements Identified:**
- Pattern: Fetch stock data → Calculate indicators → Generate output
- Tools: `exec` (Python), `read`, `write`
- Domain: Financial analysis, technical indicators
- API: AkShare

---

## Example 2: Git Workflow Automation

**Context:**
Developer needed consistent git commit patterns.

**Conversation Pattern:**
```
User: "帮我创建一个规范的 git commit"
Agent: [Runs git status, git diff, drafts commit message]

User: "提交这些更改"
Agent: [Stages files, creates commit with conventional format]

User: "推送到远程"
Agent: [Pushes with proper flags]
```

**Extracted Skill:** `git-workflow`

**Key Elements Identified:**
- Pattern: Check status → Review changes → Draft message → Commit → Push
- Tools: `exec` (git commands)
- Convention: Conventional Commits
- Safety checks: Pre-flight validation

---

## Example 3: Markdown Document Formatter

**Context:**
Writer needed consistent markdown formatting.

**Conversation Pattern:**
```
User: "格式化这个 markdown 文档"
Agent: [Fixes headings, lists, spacing]

User: "检查文档的格式问题"
Agent: [Validates links, table syntax, code blocks]

User: "生成目录"
Agent: [Creates TOC from headings]
```

**Extracted Skill:** `markdown-formatter`

**Key Elements Identified:**
- Pattern: Parse → Validate → Fix → Generate TOC
- Tools: `read`, `write`, `exec` (linting tools)
- Standards: CommonMark, GitHub Flavored Markdown

---

## Example 4: API Test Generator

**Context:**
QA engineer repeatedly requested API test generation.

**Conversation Pattern:**
```
User: "根据这个 OpenAPI spec 生成测试"
Agent: [Reads spec, generates test cases]

User: "为 POST /users 端点创建测试"
Agent: [Creates request with validation]

User: "添加边界情况测试"
Agent: [Adds edge cases: empty, null, overflow]
```

**Extracted Skill:** `api-test-generator`

**Key Elements Identified:**
- Pattern: Parse spec → Identify endpoints → Generate tests
- Tools: `read`, `write`
- Framework: pytest, requests
- Test types: happy path, edge cases, error handling

---

## Example 5: Database Migration Assistant

**Context:**
Backend developer needed migration script generation.

**Conversation Pattern:**
```
User: "创建一个迁移脚本添加用户表"
Agent: [Generates migration with up/down]

User: "在这个表上添加索引"
Agent: [Creates incremental migration]

User: "回滚最后一个迁移"
Agent: [Provides rollback command]
```

**Extracted Skill:** `migration-assistant`

**Key Elements Identified:**
- Pattern: Define schema → Generate migration → Handle rollback
- Tools: `write` (migration files), `exec` (migration runner)
- Framework: Alembic, Django migrations, etc.

---

## Extraction Checklist

When extracting a skill, verify:

- [ ] Pattern appears at least 3 times
- [ ] Clear trigger words identified
- [ ] Tool usage is consistent
- [ ] Steps are reproducible
- [ ] Error cases are understood
- [ ] Value is clear to user

---

## Anti-Patterns (Don't Extract)

These patterns should NOT be extracted as skills:

### Too Generic
```
❌ "帮助我" (Help me)
❌ "修复这个" (Fix this)
❌ "写代码" (Write code)
```

### Too Simple
```
❌ Single command execution
❌ One-line responses
❌ Basic file operations
```

### Too Specific
```
❌ Single-use scripts
❌ One-off debugging sessions
❌ Project-specific hacks
```

---

## Naming Convention Examples

| Domain | Skill Name |
|--------|------------|
| Stock Analysis | `stock-analysis` |
| Git Operations | `git-workflow` |
| API Testing | `api-test-generator` |
| Database | `migration-assistant` |
| Documentation | `markdown-formatter` |
| Cloud Deploy | `aws-deploy` |
| Data Processing | `csv-processor` |
| Web Scraping | `web-scraper` |
