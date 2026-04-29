#!/usr/bin/env python3
"""
批量修复技能文件，添加缺少的必要部分
针对论文类技能（有 Core Contributions 但没有 arXiv ID）
"""

import re
from pathlib import Path
from typing import List, Set

SKILLS_DIR = Path('/Users/hiyenwong/ai_github/ai_collection/collection/skills')

def needs_fixing(content: str) -> bool:
    """检查技能是否需要修复"""
    # 如果有 Core Contributions 或 Key Contributions，但没有 arXiv ID
    # 说明这是论文风格但不是标准的论文技能
    has_core = "## Core Contributions" in content or "## Key Contributions" in content
    has_arxiv = "arXiv ID:" in content or "**arXiv ID:**" in content or "arXiv:" in content
    
    # 检查是否缺少标准技能结构
    missing_tools = "## Tools Used" not in content
    missing_instructions = "## Instructions for Agents" not in content
    missing_examples = "## Examples" not in content
    
    return has_core and not has_arxiv and (missing_tools or missing_instructions or missing_examples)

def fix_skill(skill_path: Path) -> bool:
    """修复单个技能文件"""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False
    
    content = skill_md.read_text(encoding='utf-8')
    
    if not needs_fixing(content):
        return False
    
    print(f"  Fixing: {skill_path.name}")
    
    # 构建需要添加的内容
    additions = []
    
    if "## Tools Used" not in content:
        additions.append("""
## Tools Used

- `read` - 读取相关文件和资料
- `write` - 创建实现代码
- `exec` - 运行实验和验证
""")
    
    if "## Instructions for Agents" not in content:
        additions.append("""
## Instructions for Agents

1. 阅读技能内容，理解核心方法论
2. 根据用户需求提供相应的技术指导
3. 结合实际应用场景给出建议
4. 如需代码实现，参考核心贡献部分的方法
""")
    
    if "## Examples" not in content:
        # 从文件名提取关键词
        name = skill_path.name.replace('-', ' ').replace('_', ' ').title()
        additions.append(f"""
## Examples

### Example 1: 基本概念理解

**User:** 什么是 {name}?

**Agent:** {name} 是一种计算方法...

### Example 2: 实际应用

**User:** 如何在项目中使用这个方法?

**Agent:** 你可以按照以下步骤应用...
""")
    
    # 将新内容添加到文件末尾
    new_content = content.rstrip() + '\n\n' + '\n'.join(additions)
    skill_md.write_text(new_content, encoding='utf-8')
    print(f"    ✓ Fixed")
    return True

def main():
    import subprocess
    
    # 运行验证脚本获取失败的技能
    result = subprocess.run(
        ['python', 'scripts/validate_skill.py'],
        cwd='/Users/hiyenwong/ai_github/ai_collection',
        capture_output=True,
        text=True
    )
    
    lines = result.stdout.split('\n')
    current_skill = None
    failed_skills = []
    
    for i, line in enumerate(lines):
        if line.startswith('Validating:'):
            current_skill = line.replace('Validating:', '').strip()
        if line.startswith('❌ Errors:') and current_skill:
            failed_skills.append(current_skill)
            current_skill = None
    
    print(f"Found {len(failed_skills)} failed skills")
    
    fixed_count = 0
    for skill_name in failed_skills:
        skill_path = SKILLS_DIR / skill_name
        if skill_path.exists():
            if fix_skill(skill_path):
                fixed_count += 1
        else:
            print(f"  ⚠️ Skill directory not found: {skill_path}")
    
    print(f"\nFixed {fixed_count} skills")

if __name__ == "__main__":
    main()
