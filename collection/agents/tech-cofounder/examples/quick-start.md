# Quick Start Guide - Tech Co-Founder Agent

## 🚀 30秒快速开始

### 使用 OpenClaw

```python
sessions_spawn(
    task="Build a note-taking CLI tool that creates, lists, and completes todos in a local JSON file",
    agentId="tech-cofounder",
    model="claude-sonnet-4.5",
    thinking="high",
    runTimeoutSeconds=600,
    cleanup="keep"
)
```

### 使用 Claude Code

1. 打开 Claude Code
2. 创建新的 Agent Team
3. 添加 tech-cofounder-builder agent
4. 在对话中发送：
```
Build a note-taking CLI tool that creates, lists, and completes todos.
```

### 使用 Codex

1. 打开 Codex 应用
2. 启用 tech-cofounder skill
3. 输入：
```
Build a note-taking CLI tool that creates, lists, and completes todos.
```

---

## 📝 5分钟完整示例

### 场景：创建一个个人知识库 CLI

**你（Product Owner）**：
```
我想创建一个个人知识库 CLI 工具。

功能需求：
1. 添加笔记（支持标题和内容）
2. 列出所有笔记
3. 显示单个笔记详情
4. 编辑现有笔记
5. 删除笔记
6. 标签功能（可以给笔记打标签）
7. 搜索功能（通过标题或内容搜索）

技术要求：
- 使用 Python
- 数据存储在本地 JSON 文件
- 代码要清晰易读
- 包含简单的错误处理
```

**Tech Co-Founder（Builder）**：

#### Phase A - Plan-to-Build Brief

```
Scope:
- CLI tool for personal knowledge base
- CRUD operations for notes
- Tagging system for notes
- Search functionality
- Local JSON file storage
- Simple and maintainable code

Assumptions:
- Language: Python 3.10+
- Storage: ~/.knowledge-base/notes.json
- Structure: Single JSON with array of note objects
- Format: JSON with id, title, content, tags, created_at, updated_at

Blocking decisions:
- None (simple local storage is fine)

Build plan:
1. Set up project structure
   - Create main.py
   - Create models.py (data structure)
   - Create commands.py (CLI commands)

2. Implement CRUD operations
   - create_note(title, content, tags)
   - list_notes(filter_by_tag=None)
   - show_note(note_id)
   - edit_note(note_id, new_title, new_content, new_tags)
   - delete_note(note_id)

3. Add search functionality
   - search_notes(query)

4. Add CLI interface
   - Click or argparse
   - Clear commands and options

5. Add error handling
   - File not found
   - Invalid input
   - Note not found

6. Create README
   - Setup instructions
   - Command reference
   - Examples
```

**你（Product Owner）**：
```
计划看起来不错。不过我有一个问题：

关于标签功能，你建议如何实现？
A. 每个笔记可以有多个标签，用逗号分隔
B. 每个笔记只能有一个标签
C. 每个标签只能关联一个笔记（更简单，但灵活性低）

我倾向于 A，但想听听你的建议。
```

**Tech Co-Founder**：
```
我建议选择 A（每个笔记可以有多个标签）。

理由：
1. 灵活性高 - 你可以按不同维度组织笔记
2. 现代应用常用 - 大多数知识库工具都支持多标签
3. 搜索方便 - 搜索一个标签可以找到所有相关笔记

实现方式：
- 标签存储为列表
- 搜索时支持模糊匹配
- 列出笔记时显示标签

所以最终的技术决策：
- 每个笔记可以有多个标签
- 标签用逗号分隔字符串，存储时解析成列表
- 搜索支持标签匹配

确认是否继续？
```

**你**：
```
好的，确认继续。开始 Phase B - Implement。
```

#### Phase B - Implement (Stage 1/3)

```
1) What I shipped:
   - Project structure:
     - knowledge_base/
       ├── __init__.py
       ├── models.py (data structures)
       ├── storage.py (file operations)
       ├── commands.py (CLI commands)
       └── main.py (entry point)
   - Models defined:
     - Note (id, title, content, tags, created_at, updated_at)
   - Storage module:
     - load_notes() - read from JSON
     - save_notes() - write to JSON
     - create_note() - add new note
     - get_note() - retrieve by id
     - update_note() - modify existing note
     - delete_note() - remove note
     - list_notes() - get all notes with optional filter
     - search_notes() - search by title/content/tags

2) How to run:
git clone <repo>
cd knowledge_base
pip install -r requirements.txt
python main.py --help
python main.py create "Hello" "This is my first note" "intro"
python main.py list
python main.py show 1
python main.py edit 1 "New title" "Updated content" "tag1,tag2"
python main.py delete 1
python main.py search "intro"
python main.py list --tag tag1

3) Notes:
   - Data file location: ~/.knowledge_base/notes.json
   - Auto-created if doesn't exist
   - File format: JSON array of note objects
   - Tag parsing: "tag1, tag2, tag3" → ["tag1", "tag2", "tag3"]
   - Search: case-insensitive, matches in title/content/tags

4) Next step:
   Implement CLI commands using Click framework.
```

**你测试后**：
```
很好！命令可以工作。现在开始 Stage 2/3。
```

#### Phase B - Implement (Stage 2/3)

```
1) What I shipped:
   - CLI commands implemented:
     - create <title> <content> [tags] - Create a new note
     - list [--tag <tag>] - List all notes (filter by tag)
     - show <id> - Show note details
     - edit <id> <title> <content> [tags] - Edit existing note
     - delete <id> - Delete note
     - search <query> - Search notes
   - Features added:
     - Help system (--help)
     - Color output for better UX
     - Progress indicators
     - Error messages with suggestions

2) How to run:
python main.py create "Learn Python" "Study basics of Python programming" "learning,python"
python main.py list --tag learning
python main.py show 1
python main.py edit 1 "Master Python" "Learn advanced Python concepts" "learning,python,mastery"
python main.py search "Python"
python main.py delete 1

3) Notes:
   - All commands have --help
   - Error messages are clear and actionable
   - Color coding: success (green), warning (yellow), error (red)
   - Search is case-insensitive
   - Tags are flexible (comma-separated)

4) Next step:
   Polish the code, add error handling, and create README.
```

#### Phase B - Implement (Stage 3/3)

```
1) What I shipped:
   - Code improvements:
     - Added type hints throughout
     - Added docstrings for all functions
     - Added input validation
     - Improved error handling with specific exceptions
     - Added logging for debugging
   - Documentation:
     - README.md with:
       - Installation instructions
       - Command reference
       - Usage examples
       - File structure
       - Configuration options
   - Testing:
     - Created tests/ directory
     - Added basic tests for all commands

2) How to run:
python main.py create "Buy groceries" "Milk, eggs, bread" "shopping"
python main.py list
python main.py search "milk"
python main.py delete 1
cat ~/.knowledge_base/notes.json | jq

3) Notes:
   - Type hints improve code readability and IDE support
   - Logging helps debug issues
   - Comprehensive README makes it easy to use
   - Basic tests ensure core functionality works

4) Next step:
   Move to Phase C - Polish code structure and test thoroughly.
```

**你测试后**：
```
看起来不错！开始 Phase C。
```

#### Phase C - Polish

```
1) What I shipped:
   - Code quality improvements:
     - Added pylint checks (passed all checks)
     - Added black formatting (code is formatted)
     - Added isort imports sorted
     - Improved code organization
   - Error handling:
     - Added proper exception handling for all edge cases
     - Added user-friendly error messages
     - Added recovery options for common errors
   - Performance:
     - Optimized search function
     - Added caching for file reads (noted in documentation)
   - Documentation:
     - Added inline comments for complex logic
     - Created examples/ directory with sample usage

2) How to run:
pip install -r requirements.txt
pip install pylint black isort
pylint knowledge_base/
black --check knowledge_base/
isort --check-only knowledge_base/

# Run the tool
python main.py create "Project Idea" "Build a CLI for knowledge management" "project"
python main.py list
python main.py show 1

3) Notes:
   - Code is now production-ready
   - All linting checks passed
   - Error handling covers common failure scenarios
   - Documentation is comprehensive

4) Next step:
   Move to Phase D - Final handoff with complete documentation.
```

**你满意后**：
```
完美！开始 Phase D。
```

#### Phase D - Handoff

```
1) What I shipped:
   - README.md (comprehensive documentation):
     - Project overview
     - Installation (Python 3.10+)
     - Quick start guide
     - All commands with examples
     - Configuration
     - File structure
     - Contributing guidelines
     - License
   - Complete codebase:
     - All modules documented
     - Type hints added
     - Error handling comprehensive
     - Code formatted
   - Testing:
     - tests/ directory with test cases
     - All tests passing
   - Deployment:
     - Ready for local use
     - No external dependencies needed

2) How to run:
pip install -r requirements.txt
python main.py --help

# Create your first note
python main.py create "Welcome to Knowledge Base CLI" "Your personal knowledge management tool. Start creating notes and organizing your thoughts." "getting-started,welcome"

# List all notes
python main.py list

# Search for a tag
python main.py list --tag getting-started

# Show note details
python main.py show 1

# Search by content
python main.py search "welcome"

3) Notes:
   - Data stored at: ~/.knowledge_base/notes.json
   - No database needed - simple JSON file
   - Easy to backup and migrate
   - Plain text editor can edit the JSON file directly
   - Fully functional and tested

4) V2 suggestions:
   - Add cloud sync (GitHub Gist, Dropbox, etc.)
   - Add rich text editing
   - Add note categories/folders
   - Add export/import to Markdown
   - Add attachments (images, files)
   - Add search in real-time
   - Add keyboard shortcuts
   - Add CLI themes
   - Add reminder notifications
   - Add collaboration features
```

## ✅ 完成！

**你的知识库 CLI 工具已经构建完成！**

主要交付物：
- ✅ 完整的 Python CLI 工具
- ✅ CRUD 操作（创建、读取、更新、删除）
- ✅ 标签系统
- ✅ 搜索功能
- ✅ 完整的 README 文档
- ✅ 代码质量改进（格式化、类型提示）
- ✅ 错误处理
- ✅ 基础测试

**下一步**：
1. 使用工具：`python main.py <command>`
2. 备份数据：`cp ~/.knowledge_base/notes.json ~/backup/`
3. 分享项目：`git clone <repo>`
4. 继续使用 V2 功能（根据需要）

---

## 🎯 下个项目建议

### 从简单开始
1. 个人待办列表 CLI
2. 项目时间追踪工具
3. 简单的文件管理器
4. 快速笔记应用

### 逐步扩展
1. 添加更多功能
2. 优化用户体验
3. 集成更多工具
4. 分享给他人使用

---

**这个示例展示了完整的从需求到交付的过程。**

现在你可以：
- 直接使用 Kickoff 模板
- 在任何工具中使用 tech-cofounder agent
- 快速构建你的第一个项目！

祝构建愉快！🚀
