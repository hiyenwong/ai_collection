# Skill Extractor

## Description
A meta-skill that automatically identifies and extracts reusable skill patterns from conversations, then saves them as standard SKILL.md files following the project specification. This skill can detect recurring patterns in user requests and suggest converting them into reusable skills.

## Activation Keywords
- 提炼技能
- 提取 skill
- 生成技能
- skill extractor
- create skill from conversation
- 从对话生成技能
- extract skill pattern
- 识别技能模式
- skill mining
- 技能挖掘

## Tools Used
- write: Create new SKILL.md files
- read: Read conversation history, existing skill templates, and reference materials
- glob: Search for existing skills to avoid duplicates
- memory: Store extracted skill patterns for cross-session reference

## Usage Patterns

### Manual Extraction
```
提炼一个技能：从这段对话中提取一个处理股票数据的技能模式
```

### Auto-Detection
```
[AI detects a recurring pattern in conversation]

🔴🔴🔴 **[技能提炼建议]** 🔴🔴🔴
检测到对话中有可复用的技能模式...
```

### From Existing Code
```
从这个 Python 脚本中提取技能模式
```

## Instructions for Agents

### Phase 1: Pattern Detection

The skill can be triggered in two ways:

#### Automatic Detection
Monitor conversations for these patterns:

1. **Recurring Task Patterns**: User requests similar types of tasks multiple times
2. **Specific Tool Sequences**: Particular tool combinations being used repeatedly
3. **Domain Knowledge**: Specialized domain workflows appearing in conversation
4. **Complex Multi-step Processes**: Fixed-step operations that could be standardized

**Detection Signals:**
- User says "我经常需要..." (I often need to...)
- Similar requests appear 3+ times in a session
- User asks "这个可以做成一个技能吗?" (Can this be made into a skill?)
- Agent performs same complex workflow repeatedly

#### Manual Trigger
User explicitly uses activation keywords.

### Phase 2: Extraction Process

#### Step 1: Identify Skill Candidate
Analyze the conversation pattern to identify:
- **Core Purpose**: What problem does this pattern solve?
- **Target Audience**: Who would use this skill?
- **Reusability**: Can this be applied in different contexts?
- **Completeness**: Does it have all necessary components?

#### Step 2: Extract Key Elements

**From the conversation pattern, extract:**

| Element | Description | Example |
|---------|-------------|---------|
| **Skill Name** | Concise English name with hyphens | `stock-analyzer`, `git-workflow` |
| **Description** | 1-2 sentences of functionality | "Analyzes stock data using AkShare API" |
| **Activation Keywords** | Trigger phrases (Chinese + English) | "股票分析", "stock analysis" |
| **Tools Used** | Required tools and their usage | `exec: Run Python scripts` |
| **Usage Patterns** | Typical use cases | "Analyze single stock", "Compare stocks" |
| **Instructions** | Step-by-step workflow | 1. Fetch data, 2. Calculate indicators... |
| **Error Handling** | Common issues and solutions | "If API fails: retry after 3 seconds" |

#### Step 3: Generate SKILL.md Content

Use the project template format. The generated SKILL.md must include:

```markdown
# [Skill Name]

## Description
[1-2 sentence description]

## Activation Keywords
- [keyword1]
- [keyword2]
- [keyword3]

## Tools Used
- [tool1]: [usage description]
- [tool2]: [usage description]

## Usage Patterns
### [Pattern Name]
[Description and example]

## Instructions for Agents
### Step 1: [Action]
[Detailed instructions]

### Step 2: [Action]
[Detailed instructions]

## Error Handling
### [Error Type]
[Recovery steps]

## Examples
### Example 1: [Scenario]
[Example dialog]

## Resources
- [Relevant links]
```

#### Step 4: User Confirmation

**Display the extracted skill suggestion:**

```markdown
🔴🔴🔴 **[技能提炼建议]** 🔴🔴🔴

检测到对话中有可复用的技能模式：

**技能名称**: `your-skill-name`
**简要描述**: [技能功能描述]
**激活关键词**: [检测到的关键词]

---

**提取的关键要素:**

## Description
[description]

## Activation Keywords
- [keyword1]
- [keyword2]

## Tools Used
- [tool1]: [usage]

---

**预计生成目录结构:**
```
collection/skills/your-skill-name/
├── SKILL.md
├── examples/
└── references/
```

**是否将此模式提炼为新技能？**
- 回复 "确认" 或 "yes" 创建技能
- 回复 "修改 [内容]" 修改特定部分
- 回复 "跳过" 或 "skip" 跳过此次建议
```

#### Step 5: Create Skill Files

After user confirmation:

1. **Create directory structure:**
   ```bash
   mkdir -p collection/skills/{skill-name}/{examples,references,assets,scripts}
   ```

2. **Write SKILL.md:** Using extracted content

3. **Create supporting files:**
   - `examples/usage-examples.md`: Usage examples
   - `references/` if applicable
   - `scripts/` if Python/scripts are needed

4. **Update project indices:**
   - Add entry to `SKILLS.md`
   - Update `CLAUDE.md` if needed

5. **Save to memory:**
   - Record skill in `memory/skills.md`
   - Include: name, path, extraction date, source pattern

### Phase 3: Validation

After creating the skill, validate:

1. **Format Compliance**: Check SKILL.md follows template
2. **No Duplicates**: Verify no existing skill with same purpose
3. **Testable**: Instructions are clear and actionable
4. **Complete**: All required sections are present

## Context Files

### templates/skill-template.md
Project's standard SKILL.md template

### collection/skills/*/SKILL.md
Existing skills for reference and pattern matching

### memory/skills.md
Cross-session memory of extracted skills

## Error Handling

### Duplicate Skill Detected
```
If skill already exists:
  1. Inform user of existing skill
  2. Show differences between patterns
  3. Ask if they want to:
     - Update existing skill
     - Create as variant/alternative
     - Skip creation
```

### Incomplete Pattern
```
If extracted pattern is incomplete:
  1. Identify missing elements
  2. Ask user for missing information
  3. Provide suggestions based on similar skills
  4. Allow user to fill gaps manually
```

### Ambiguous Pattern
```
If pattern is not clear:
  1. Ask clarifying questions
  2. Provide multiple interpretations
  3. Let user choose the best approach
  4. Extract what's clear, ask for rest
```

## Best Practices

### 1. Specific Activation Keywords
- Avoid generic terms ("help", "do", "make")
- Use domain-specific phrases ("kdj indicator", "golden cross")
- Include both Chinese and English variants
- Test keywords are unique enough

### 2. Clear Instructions
- Write step-by-step instructions
- Include conditional logic (if X, then Y)
- Provide fallback options
- Reference specific tools and parameters

### 3. Comprehensive Examples
- Show typical usage scenarios
- Include edge cases
- Demonstrate error handling
- Use realistic user requests

### 4. Proper Documentation
- Add relevant references
- Include external resources
- Link to related skills
- Document limitations

### 5. Memory Integration
- Save extracted skills to memory
- Cross-reference similar patterns
- Track skill usage over time
- Update based on user feedback

## Examples

### Example 1: Manual Extraction Request

```
User: "提炼一个技能：从这段对话中，我一直在请求分析股票数据，
     你在用 AkShare 获取数据，计算技术指标，生成图表。"

Agent Process:
1. Analyzes conversation history
2. Identifies the stock analysis pattern:
   - Uses AkShare API
   - Calculates technical indicators (MA, MACD, KDJ)
   - Generates visualizations
   - Produces Markdown reports

3. Extracts key elements:
   - Skill Name: stock-analysis
   - Description: "Comprehensive stock technical analysis using AkShare"
   - Keywords: stock analysis, 股票分析, technical indicators
   - Tools: exec, read, write

4. Generates SKILL.md content

5. Displays suggestion with 🔴 markers

6. User confirms "yes"

7. Creates files and updates indices
```

### Example 2: Auto-Detection

```
[Conversation context: User has asked 3 times to format SQL queries]

Agent: (detects pattern)

🔴🔴🔴 **[技能提炼建议]** 🔴🔴🔴

检测到对话中有可复用的技能模式：

**技能名称**: `sql-formatter`
**简要描述**: Format and beautify SQL queries with consistent style
**激活关键词**: 格式化sql, format sql, sql beautify

---

**提取的关键要素:**

## Description
Formats SQL queries with consistent indentation, capitalization,
and line breaks for improved readability.

## Activation Keywords
- 格式化sql
- format sql
- sql beautify
- sql formatter
- 美化sql

## Tools Used
- exec: Run SQL formatter (e.g., sqlparse)
- write: Save formatted output

---

**是否将此模式提炼为新技能？**

User: "确认"

Agent: Creates skill files at collection/skills/sql-formatter/
```

### Example 3: Pattern from Code

```
User: "从这个脚本中提取技能：scripts/fetch_weather.py"

Agent Process:
1. Reads the Python script
2. Analyzes functionality:
   - Fetches weather data from API
   - Parses JSON response
   - Formats output for display
3. Extracts skill pattern:
   - Skill Name: weather-fetcher
   - Description: "Fetch and display weather data from API"
   - Keywords: weather, 天气, forecast
4. Generates SKILL.md with Python-specific instructions
5. Creates skill with scripts/ subdirectory
```

## Advanced Features

### Pattern Recognition Hints
Look for these indicators when auto-detecting:

| Indicator | Example Pattern |
|-----------|-----------------|
| Repetition | Same task requested 3+ times |
| Complexity | 5+ steps in a workflow |
| Domain Specific | Uses specialized terminology |
| Tool Combination | Specific tools used together |
| User Explicit | "Can this be saved/remembered?" |

### Cross-Session Learning
- Store extracted patterns in memory
- Build skill library over time
- Suggest related skills based on context
- Learn from user confirmations/rejections

### Skill Relationships
When extracting, check for:
- Parent/child skill relationships
- Complementary skills
- Conflicting skills
- Dependencies on other skills

## Limitations

- Cannot extract skills from very short conversations (< 3 exchanges)
- Requires clear, repeatable patterns
- Manual confirmation always required
- May need user input for domain-specific details
- Cannot validate extracted skills work without testing

## Resources

- **Project Template:** `templates/skill-template.md`
- **Skill Creation Guide:** `docs/skills/creation-guide.md`
- **Existing Skills:** `collection/skills/`

## Related Skills

- **skill-creator:** Official skill creation guide
- **opencode:** For skills involving code generation
- **claude-code:** For general coding assistance

## Notes

- This is a "meta-skill" - it creates other skills
- Always requires user confirmation before creating files
- Extracted skills should be tested after creation
- Consider creating variants for different use cases
- Update memory system for cross-session learning
- Skills are most valuable when they capture domain expertise
