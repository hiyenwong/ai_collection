# OpenClaw Skills

## What is a Skill?

An OpenClaw **skill** is a reusable capability package that defines specialized behavior, tools, and instructions for handling specific types of tasks. Skills act as "plugins" that extend an agent's capabilities.

## How Skills Work

Skills are automatically activated when:
1. **Trigger keywords** match in the user's message
2. The agent reads the skill's `SKILL.md` file
3. The agent follows the skill's instructions for the task
4. The agent uses skill-defined tools and workflows

### Skill Activation

When a user message contains trigger keywords:
```
User: "Create a note about my meeting"
```

The system:
1. Detects "note" as a trigger keyword
2. Activates the `apple-notes` skill
3. Loads `/path/to/skill/apple-notes/SKILL.md`
4. Agent follows skill instructions to create the note

## Skill Structure

```
skill-name/
├── SKILL.md              # Main skill documentation and instructions
├── references/           # Reference documentation (optional)
│   ├── api-docs.md
│   └── examples.md
├── examples/            # Usage examples (optional)
│   └── example-1.md
├── scripts/             # Helper scripts (optional)
│   └── setup.sh
└── assets/              # Images, diagrams, etc. (optional)
    └── screenshot.png
```

### SKILL.md Format

The `SKILL.md` file must contain:

```markdown
# Skill Name

## Description
Brief description of what this skill does.

## Activation Keywords
- keyword1
- keyword2
- keyword3

## Instructions
How the agent should use this skill.
```

### Example SKILL.md

```markdown
# Apple Notes

## Description
Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes).

## Activation Keywords
- create a note
- list notes
- add note
- search notes
- apple notes
- memo

## Instructions
When a user asks to work with notes, use the `memo` CLI:

### Creating Notes
```bash
memo create "Note title" "Note content"
```

### Listing Notes
```bash
memo list
memo list --folder "Work"
```

### Searching Notes
```bash
memo search "keyword"
```

### Editing Notes
```bash
memo edit <note-id> "New content"
```

## Tools Used
- exec: Run memo CLI commands

## Notes
- Ensure `memo` is installed and configured
- Notes are stored in user's Apple Notes app
```

## Skill Capabilities

### 1. Specialized Instructions
Skills provide detailed, domain-specific instructions that override general behavior.

### 2. Tool Preferences
Skills define which tools to use and how:
```markdown
## Tools Used
- exec: Run commands
- web_fetch: Get data
- read: Read files
```

### 3. Workflow Automation
Skills can define multi-step workflows:
```markdown
## Workflow
1. Search for existing notes
2. If found, offer to edit
3. If not found, create new note
4. Verify note was created successfully
```

### 4. Context Management
Skills can specify what context to load:
```markdown
## Context Files
- Read NOTES_SETTINGS.md for user preferences
- Check notes-template.md for formatting
```

### 5. Error Handling
Skills define how to handle errors:
```markdown
## Error Handling
If memo command fails:
1. Check if memo is installed
2. Verify macOS accessibility permissions
3. Try alternative method or report error
```

## Skill Types

### 1. Tool Wrappers
Wrappers around external tools/CLIs:
- `apple-notes`: Memo CLI for notes
- `apple-reminders`: remindctl CLI for reminders
- `sonoscli`: Sonos speaker control

### 2. Service Integrations
Integrations with external services:
- `feishu-doc`: Feishu document operations
- `feishu-drive`: Feishu cloud storage
- `feishu-wiki`: Feishu knowledge base

### 3. Task-Specific
Specialized task capabilities:
- `coding-agent`: Run Codex CLI, Claude Code
- `video-frames`: Extract frames from videos
- `gifgrep`: Search and download GIFs

### 4. Information Retrieval
Get specific types of information:
- `weather`: Weather and forecasts
- `summarize`: Summarize content
- `model-usage`: Model usage statistics
- `consulting-report-search`: Search and answer over consulting and market research reports, prioritizing iResearch free reports

## When to Create a Skill

Create a skill when:
- ✅ Task type is repeated frequently
- ✅ Task requires specialized knowledge or workflow
- ✅ Task uses specific tools or APIs consistently
- ✅ You want to document best practices
- ✅ Task requires multiple steps that should be standardized

Don't create a skill when:
- ❌ Task is one-time or very rare
- ❌ Instructions are simple enough to be general knowledge
- ❌ Task varies significantly each time
- ❌ Existing tools handle it well without guidance

## Creating a Skill

### Step 1: Define Purpose
What does this skill do? What problems does it solve?

### Step 2: Identify Triggers
What keywords or phrases should activate this skill?

### Step 3: Document Instructions
Write clear, step-by-step instructions for the agent.

### Step 4: Add References
Include API docs, guides, and examples.

### Step 5: Test Thoroughly
Test with various prompts and edge cases.

### Step 6: Iterate
Refine based on usage and feedback.

## Skill Best Practices

### 1. Clear Activation Keywords
- Use specific, uncommon phrases
- Avoid words used in general conversation
- Include variations (synonyms, abbreviations)

**Good:** `"create a note"`, `"list my reminders"`
**Bad:** `"create"`, `"list"`

### 2. Comprehensive Instructions
- Cover common use cases
- Address edge cases
- Provide examples
- Include error handling

### 3. Tool Specifications
List tools explicitly:
```markdown
## Tools Used
- exec: Run commands with pty for CLIs
- read: Read skill-specific config files
```

### 4. Context Awareness
Specify what context to load:
```markdown
## Context
- Read TOOLS.md for device settings
- Check USER.md for user preferences
```

### 5. Maintainability
- Keep SKILL.md focused
- Put detailed docs in references/
- Use examples/ for illustration

## Skill Discovery

### Finding Available Skills
```python
agents_list()  # List available agents (also checks skills)
```

### Checking Active Skill
```
User: What skill are you using?
Agent: I'm using the apple-notes skill to manage your notes.
```

## Advanced Skills

### Multi-Tool Skills
Skills can combine multiple tools:
```markdown
## Tools Used
- exec: Run CLIs
- web_search: Find information
- write: Save results
```

### Chained Skills
Skills can reference other skills:
```markdown
## Related Skills
- feishu-doc: For document operations
- obsidian: For vault management
```

### Conditional Behavior
Skills can have conditional logic:
```markdown
## Conditional Behavior
IF user has multiple folders:
  - Ask which folder to use
ELSE:
  - Use default folder
```

## Skill Examples

### Weather Skill
```markdown
# Weather

## Description
Get current weather and forecasts (no API key required).

## Activation Keywords
- weather
- forecast
- temperature
- raining
- sunny

## Instructions
Use the weather CLI:
```bash
weather
weather forecast
weather --location "Beijing"
```

## Tools Used
- exec: Run weather CLI
```

### Feishu Doc Skill
```markdown
# Feishu Document

## Description
Feishu document read/write operations.

## Activation Keywords
- feishu doc
- feishu document
- cloud doc
- docx link

## Instructions
Use the feishu_doc tool:

### Reading Documents
```python
feishu_doc(
    action="read",
    doc_token="..."
)
```

### Writing Documents
```python
feishu_doc(
    action="write",
    doc_token="...",
    content="..."
)
```

## Tools Used
- feishu_doc: Document operations
- read: Read local templates
```

## Troubleshooting

### Skill Not Activating
- Check activation keywords in user message
- Verify SKILL.md path is correct
- Check skill is in skill directories

### Agent Not Following Instructions
- Ensure instructions are clear and explicit
- Check for conflicting skills
- Verify tool permissions

### Skill Tools Failing
- Check if external tools are installed
- Verify API keys or credentials
- Test tool usage manually

## Resources

- [OpenClaw Docs - Skills](https://docs.openclaw.ai/skills)
- [OpenClaw Skill Hub](https://clawhub.com)
- [Skill Creator Guide](./docs/skills/creation-guide.md)

---

See the [skills-collection](https://github.com/your-org/skills-collection) repository for example skills.

## Available Skills

### Quantum Finance Skills

#### Quantum Finance
- **Location:** `collection/skills/quantum-finance/`
- **Purpose:** Quantum computing applications in finance: portfolio optimization, option pricing, risk management
- **Triggers:** quantum finance, quantum portfolio, quantum Monte Carlo, QAOA portfolio, 量子金融

#### Quantum Portfolio Optimization
- **Location:** `collection/skills/quantum-portfolio-optimization/`
- **Purpose:** QAOA and quantum annealing for portfolio optimization with higher-order moments
- **Triggers:** quantum portfolio, QAOA optimization, quantum annealing portfolio

#### Quantum Finance Analysis
- **Location:** `collection/skills/quantum-finance-analysis/`
- **Purpose:** Comprehensive quantum finance analysis with QUBO formulation, Monte Carlo methods
- **Triggers:** quantum finance analysis, QUBO, quantum risk metrics

#### Quantum Knowledge Graph
- **Location:** `collection/skills/quantum-knowledge-graph/`
- **Purpose:** Quantum-enhanced knowledge graph using QNLP and quantum semantic modeling
- **Triggers:** quantum knowledge graph, QKG, QNLP, 量子知识图谱

#### Quantum Game Theory Economics
- **Location:** `collection/skills/quantum-game-theory-economics/`
- **Purpose:** Quantum game theory applications in economics, non-Nashian equilibria
- **Triggers:** quantum game theory, quantum Nash, quantum auction

### Neuroscience + Quantum Skills

#### Brain Connectivity Analysis
- **Location:** `collection/skills/brain-connectivity-analysis/`
- **Purpose:** Brain network connectivity analysis using knowledge graph tools
- **Triggers:** brain connectivity, 脑连接, brain network, 脑网络, neural connectivity

#### Brain-Inspired NCA
- **Location:** `collection/skills/brain-inspired-nca/`
- **Purpose:** Brain-inspired Neural Cellular Automata for morphological computation
- **Triggers:** brain NCA, neural cellular automata, bio-inspired computation

#### Quantized SNN Hardware Optimization
- **Location:** `collection/skills/quantized-snn-hardware-optimization/`
- **Purpose:** Integer-state SNN quantization and hardware acceleration techniques
- **Triggers:** quantized SNN, hardware SNN, neuromorphic optimization

#### Quantum Neural Hybrid
- **Location:** `collection/skills/quantum-neural-hybrid/`
- **Purpose:** Hybrid classical-quantum neural network development
- **Triggers:** quantum neural network, QNN, hybrid quantum-classical, VQC

### Research Skills

#### Research Skill Extractor
- **Location:** `collection/skills/research-skill-extractor/`
- **Purpose:** Meta-skill that extracts reusable patterns from research papers
- **Triggers:** extract skill from paper, research skill mining, 论文技能提炼

#### Agentic Portfolio Management
- **Location:** `collection/skills/agentic-portfolio-management/`
- **Purpose:** Multi-agent architecture for institutional asset management
- **Triggers:** agentic portfolio, multi-agent investment, autonomous portfolio

### OpenCode + Oh My OpenCode
- **Location:** `collection/skills/opencode/`
- **Purpose:** Open source AI coding agent with multi-agent orchestration and ultrawork mode
- **Triggers:** opencode, ultrawork, ulw, oh-my-opencode, coding agent
- **Tools:** exec, read, write, edit, process
- **Key Features:**
  - Multi-agent orchestration (Sisyphus, Oracle, Librarian, etc.)
  - Ultrawork mode for parallel execution
  - LSP/AST tools for surgical refactoring
  - MCP integration (Exa, Context7, Grep.app)

### Claude Code
- **Location:** `collection/skills/claude-code/`
- **Purpose:** Anthropic's official AI-powered coding companion
- **Triggers:** claude-code, claude code, @anthropic, anthropic coding
- **Tools:** exec, read, write, edit, process
- **Key Features:**
  - Native Claude integration
  - Privacy-first design
  - Context-aware project understanding
  - MCP, Hooks, Skills, and Agents support

### OpenSpec
- **Location:** `collection/skills/openspec/`
- **Purpose:** Specification-driven framework with Gherkin syntax for requirements
- **Triggers:** openspec, open spec, specification, gherkin, scenario, bdd
- **Tools:** read, write, edit, memory
- **Key Features:**
  - Spec deltas for change tracking
  - GIVEN-WHEN-THEN scenario format
  - Version control friendly
  - Perfect for TDD/BDD workflows
  - AI-friendly structured format

### AkShare
- **Location:** `collection/skills/akshare/`
- **Purpose:** Chinese financial data interface library
- **Triggers:** stock data, futures data, fund data, macro economics, akshare
- **Tools:** exec (Python), read, write
- **Key Features:**
  - Stock market data (A-shares, HK stocks, US stocks)
  - Futures market (all major Chinese exchanges)
  - Fund data (ETFs, open-end funds)
  - Macro economics indicators
  - Bond market, forex, cryptocurrency data
  - Options, movies, news, ESG ratings

### Stock Analysis
- **Location:** `collection/skills/stock-analysis/`
- **Purpose:** Comprehensive stock technical analysis with indicators, scoring, and visualization
- **Triggers:** stock analysis, 股票分析, technical analysis, 技术分析, stock indicators, kdj, macd, rsi, boll
- **Tools:** exec (Python), read, write
- **Key Features:**
  - Calculate technical indicators (MA, MACD, KDJ, RSI, BOLL, etc.)
  - Model-based scoring with weighted components
  - Chart generation (K-line, indicators)
  - Single stock and multi-stock comparison
  - Markdown analysis reports

### Skill Extractor
- **Location:** `collection/skills/skill-extractor/`
- **Purpose:** Meta-skill that identifies and extracts reusable skill patterns from conversations
- **Triggers:** 提炼技能, 提取 skill, 生成技能, skill extractor, create skill from conversation

### Taiyi Jinhua Meditation
- **Location:** `collection/skills/taiyi-jinhua-meditation/`
- **Purpose:** 指导用户学习和实践基于《太乙金华宗旨》的道家冥想与回光守中法法门
- **Triggers:** 冥想, meditation, 太乙金华宗旨, 回光守中, 打坐, 吕洞宾冥想
- **Tools:** read, write
- **Key Features:**
  - 核心概念讲解 (天心、元神识神)
  - 回光守中冥想实践引导
  - 差谬纠正与体会交流
  - 冥想日记记录
- **Tools:** write, read, glob, memory
- **Key Features:**
  - Auto-detection of recurring patterns
  - Manual extraction trigger
  - Generates standard SKILL.md files
  - Red-highlighted suggestions with user confirmation
  - Cross-session memory integration

### Skill RAG Indexer
- **Location:** `collection/skills/skill-rag-indexer/`
- **Purpose:** RAG indexer for semantic search and intelligent recommendation of local skill documentation
- **Triggers:** skill rag search, search skills, find skill, recommend skill, 搜索技能, 推荐技能, 技能索引
- **Tools:** exec (TypeScript CLI), read, write, glob
- **Key Features:**
  - Semantic search using natural language
  - Task-based skill recommendations
  - Knowledge base management
  - Local-first with zero external dependencies
  - Multi-language support (Chinese/English)

### Security Guardrails
- **Location:** `collection/skills/security-guardrails/`
- **Purpose:** 强制性基础安全层，防止所有代理在响应中暴露密码、API Key、数据库凭据、私钥、Token 等敏感信息
- **Triggers:** 所有代理默认激活 (default on for all agents)
- **Tools:** read, write
- **Key Features:**
  - 敏感信息分类检测（密码/API Key/连接串/私钥）
  - 自动脱敏与占位符替换
  - 文件读取安全过滤
  - 拒绝输出明文凭据的防护
  - 面向用户的安全实践引导

### ICE Review
- **Location:** `collection/skills/ice-review/`
- **Purpose:** 跨任务自我进化技能，基于 ICE (Investigate-Consolidate-Exploit) 策略进行任务回顾和知识提取
- **Triggers:** ICE review, ICE 回顾, 任务回顾, task review, 知识巩固
- **Tools:** read, write, edit, memory_search, memory_get
- **Key Features:**
  - 三阶段回顾流程（调查→巩固→利用）
  - 从任务中提取可复用模式
  - 更新 MEMORY.md 和知识库
  - 创建新 skills 或工作流程
  - 来源：arXiv:2401.13996

### Memory Retrieval
- **Location:** `collection/skills/memory-retrieval/`
- **Purpose:** 两阶段记忆检索，基于 MemRL 论文实现语义匹配 + 效用过滤的高质量记忆检索
- **Triggers:** 记忆检索, memory retrieval, 查找知识, find knowledge, 两阶段检索
- **Tools:** memory_search, memory_get, read, write
- **Key Features:**
  - 第一阶段：语义匹配获取候选记忆
  - 第二阶段：效用评分过滤和排序
  - 解决稳定性-可塑性困境
  - 效用追踪（成功率、最近使用、相关性）
  - 来源：arXiv:2601.03192

### Self-Challenge
- **Location:** `collection/skills/self-challenge/`
- **Purpose:** 自我挑战机制，基于 Agent0 论文实现双代理竞争模型驱动能力扩展
- **Triggers:** 自我挑战, self challenge, 能力测试, capability test, 挑战任务
- **Tools:** exec, read, write, memory_search, sessions_spawn
- **Key Features:**
  - Curriculum Agent 设计挑战
  - Executor Agent 执行挑战
  - 能力评估和知识提取
  - 渐进式难度提升
  - 来源：arXiv:2511.16043

### iamb Matrix CLI Operations
- **Location:** `collection/skills/iamb-matrix-cli/`
- **Purpose:** Matrix/iamb 实操技能，覆盖注册、token 获取、Space ID 查询和空间子房间维护
- **Triggers:** iamb, matrix cli, 用户注册, 获取 token, access token, space id, spaces id
- **Tools:** exec (Python CLI), read, write
- **Key Features:**
  - Matrix API 用户注册（m.login.dummy 流程）
  - 登录并获取 access token
  - 从 iamb `session.json` 提取 token
  - 查询 joined Space IDs（过滤 `m.room.create` 中 `type=m.space`）
  - 对接 iamb `:spaces` / `:room id show` / `:space child set/remove`

---

See: [skills-collection](https://github.com/your-org/skills-collection) repository for more example skills.

### arXiv Paper Tracker
- **Location:** `collection/skills/arxiv-paper-tracker/`
- **Purpose:** 追踪和引用 AI Agent 系统相关的高价值 arXiv 论文，包含多代理协调、记忆管理、代理架构和评估方法等
- **Triggers:** arxiv paper, agent paper, multi-agent coordination, memory management, agent architecture, evaluation methods
- **Tools:** web_search, web_fetch, read
- **Key Features:**
  - 高价值论文快速参考（utility >= 0.85）
  - 多代理协调、记忆管理、架构设计等分类
  - 相关基准和资源索引
  - 最新趋势分析

### Agent Memory Forgetting
- **Location:** `collection/skills/agent-memory-forgetting/`
- **Purpose:** 自适应记忆遗忘框架，解决长时程对话代理的记忆累积和假记忆传播问题
- **Triggers:** agent memory, memory forgetting, long-horizon agent, 记忆遗忘
- **Tools:** read, write
- **Key Features:**
  - 相关性导向评分（recency/frequency/semantic）
  - 有界优化防止记忆膨胀
  - 结构化遗忘机制
  - 来源：arXiv:2604.02280

### Agentic Control Memory (SCRAT)
- **Location:** `collection/skills/agentic-control-memory/`
- **Purpose:** SCRAT框架：耦合控制、结构化记忆和可验证行动的代理AI设计
- **Triggers:** SCRAT, agentic control, structured memory, verifiable action
- **Tools:** read, write
- **Key Features:**
  - 层级部分观测控制模型
  - 结构化情景记忆
  - 观察者-信念状态
  - 来源：arXiv:2604.03201

### Agentic Portfolio
- **Location:** `collection/skills/agentic-portfolio/`
- **Purpose:** 多代理架构设计，包含专业化角色、批评投票机制和元代理自改进
- **Triggers:** agentic portfolio, multi-agent architecture, meta-agent, 投资组合代理
- **Tools:** read, write, exec
- **Key Features:**
  - 50+专业化代理角色
  - 批评投票周期
  - 元代理自改进循环
  - 政策文档治理
  - 来源：arXiv:2604.02279

### Chart Visual Reasoning (Chart-RL)
- **Location:** `collection/skills/chart-visual-reasoning/`
- **Purpose:** RL增强VLM图表理解，4B模型超越8B基座模型
- **Triggers:** chart reasoning, chart-RL, VLM chart, 图表理解
- **Tools:** read, write
- **Key Features:**
  - 策略优化强化学习
  - LoRA参数高效微调
  - 单GPU配置可行
  - 推理延迟降低3.4倍
  - 来源：arXiv:2604.03157 (KDD 2026)

### Efficient Reasoning BCR
- **Location:** `collection/skills/efficient-reasoning-bcr/`
- **Purpose:** Batched Contextual Reinforcement实现高效推理，减少Token消耗
- **Triggers:** efficient reasoning, BCR, token reduction, reasoning optimization
- **Tools:** read, write
- **Key Features:**
  - 任务缩放定律发现
  - 免费午餐现象（N=1时减少15.8%-62.6%Token）
  - 隐式Token预算约束
  - 避免显式长度惩罚的优化崩溃
  - 来源：arXiv:2604.02322

### Emotion Steering Vectors
- **Location:** `collection/skills/emotion-steering-vectors/`
- **Purpose:** LLM情绪控制：Valence-Arousal子空间发现和行为调控
- **Triggers:** emotion steering, VA subspace, emotion control, 情绪控制
- **Tools:** read, write
- **Key Features:**
  - VA子空间圆几何结构
  - 双向控制拒绝/迎合行为
  - 跨架构通用性
  - 来源：arXiv:2604.03147

### Hierarchical Agent Search
- **Location:** `collection/skills/hierarchical-agent-search/`
- **Purpose:** 层级并行代理框架用于Web信息检索，3-5倍加速
- **Triggers:** hierarchical search, parallel agent, web information seeking
- **Tools:** web_search, web_fetch, read, write
- **Key Features:**
  - Host-Manager-Worker三层架构
  - 上下文隔离防止饱和
  - 错误遏制停止级联传播
  - 开源实现：github.com/agent-on-the-fly/InfoSeeker
  - 来源：arXiv:2604.02971

### LLM Confidence BAS
- **Location:** `collection/skills/llm-confidence-bas/`
- **Purpose:** Behavioral Alignment Score：决策理论置信度评估指标
- **Triggers:** BAS, confidence evaluation, behavioral alignment, 置信度评估
- **Tools:** read, write
- **Key Features:**
  - 弃权感知决策度量
  - 不对称惩罚（优先避免过度自信错误）
  - 关联校准与决策最优行为
  - 来源：arXiv:2604.03216

### LLM Interaction Awareness
- **Location:** `collection/skills/llm-interaction-awareness/`
- **Purpose:** 用户轮生成探针：测量LLM交互意识超越任务准确率
- **Triggers:** interaction awareness, user-turn generation, conversation quality
- **Tools:** read, write
- **Key Features:**
  - 交互意识与任务准确率解耦
  - 潜在意识通过温度采样揭示
  - 后训练可针对交互意识优化
  - 来源：arXiv:2604.02315

### Membership Inference Transfer
- **Location:** `collection/skills/membership-inference-transfer/`
- **Purpose:** LT-MIA：跨架构可迁移成员推断攻击
- **Triggers:** membership inference, MIA, privacy attack, 隐私攻击
- **Tools:** read, write
- **Key Features:**
  - 记忆化不变签名检测
  - 跨Transformer/Mamba/RWKV架构迁移
  - 自然语言训练迁移到代码域
  - 开源：github.com/JetBrains-Research/learned-mia
  - 来源：arXiv:2604.03199

### Multi-Agent Formalization
- **Location:** `collection/skills/multi-agent-formalization/`
- **Purpose:** 多代理系统自动教科书形式化，500+页代数组合学→Lean
- **Triggers:** textbook formalization, Lean, multi-agent collaboration
- **Tools:** read, write, exec
- **Key Features:**
  - 30K Claude代理并行协作
  - 一周完成130K行Lean代码
  - 推理成本媲美专家薪资
  - 来源：arXiv:2604.03071

### Multi-Agent Recommenders
- **Location:** `collection/skills/multi-agent-recommenders/`
- **Purpose:** MAVRS多代理视频推荐系统架构和演进
- **Triggers:** MAVRS, video recommender, multi-agent recommendation
- **Tools:** read, write
- **Key Features:**
  - Video Understanding/Reasoning/Memory/Feedback/Explainability代理
  - 协作模式分类（短视频/长视频/通用）
  - 开放挑战：可扩展性/多模态/激励对齐
  - 来源：arXiv:2604.02211 (WSDM 2026)

### RAG Contextual Enrichment
- **Location:** `collection/skills/rag-contextual-enrichment/`
- **Purpose:** LLM上下文增强技术谱系：ICL→RAG→GraphRAG→CausalRAG
- **Triggers:** RAG, GraphRAG, CausalRAG, contextual enrichment
- **Tools:** read, write, web_fetch
- **Key Features:**
  - 增强谱系分类（结构化程度递增）
  - 部署决策框架
  - 因果结构检索
  - 来源：arXiv:2604.03174

### Reflective Context Learning
- **Location:** `collection/skills/reflective-context-learning/`
- **Purpose:** RCL统一框架：上下文空间的优化原语
- **Triggers:** RCL, reflective learning, context optimization, 上下文优化
- **Tools:** read, write
- **Key Features:**
  - Reflection + Mutation两阶段
  - 批处理/信用分配/辅助损失优化原语
  - 失败回放/分组rollout方差减少
  - 开源：github.com/nvassilyev/RCL
  - 来源：arXiv:2604.03189 (COLM under review)

### Role-Based LLM Framework
- **Location:** `collection/skills/role-based-llm-framework/`
- **Purpose:** 角色基LLM框架：专业化角色减少幻觉提升域任务准确性
- **Triggers:** role-based LLM, structured extraction, domain specialization
- **Tools:** read, write
- **Key Features:**
  - Analyst/Specialist/Expert角色分工
  - 结构化域知识嵌入提示
  - 工作流模仿专家分析模式
  - 透明可解释输出
  - 来源：arXiv:2604.01529
