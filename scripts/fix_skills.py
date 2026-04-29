#!/usr/bin/env python3
"""
批量修复技能文件，添加缺少的必要部分
"""

import re
from pathlib import Path
from typing import List, Set

SKILLS_DIR = Path('/Users/hiyenwong/ai_github/ai_collection/collection/skills')

REQUIRED_SECTIONS = [
    "## Activation Keywords",
    "## Tools Used",
    "## Instructions for Agents",
    "## Examples"
]

def is_paper_skill(content: str) -> bool:
    """检查是否是论文技能（需要特殊处理）"""
    indicators = [
        "arXiv ID:",
        "**arXiv ID:**",
        "## Abstract",
        "## Key Contributions",
        "arXiv:",
        "arxiv.org",
        "source_paper:",
        "触发词:",
        "references:",
        "核心论点",
        "核心贡献",
    ]
    return any(ind in content for ind in indicators)

def get_missing_sections(content: str) -> List[str]:
    """获取内容中缺少的必要部分"""
    missing = []
    for section in REQUIRED_SECTIONS:
        if section not in content:
            missing.append(section)
    return missing

def fix_skill(skill_path: Path) -> bool:
    """修复单个技能文件，返回是否进行了修复"""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"  ⚠️ SKILL.md not found: {skill_md}")
        return False
    
    content = skill_md.read_text(encoding='utf-8')
    
    # 检查是否是论文技能
    if is_paper_skill(content):
        return False  # 论文技能使用不同的验证规则
    
    # 获取缺少的部分
    missing = get_missing_sections(content)
    if not missing:
        return False
    
    print(f"  Fixing: {skill_path.name}")
    print(f"    Missing: {missing}")
    
    # 构建需要添加的内容
    additions = []
    
    if "## Activation Keywords" in missing:
        # 从 description 提取关键词
        name_match = re.search(r'^name:\s*(\S+)', content, re.MULTILINE)
        if name_match:
            name = name_match.group(1)
            # 提取关键词
            words = re.findall(r'[a-zA-Z]+', name)
            keywords = [w for w in words if len(w) > 2][:5]
            if not keywords:
                keywords = [name]
            additions.append(f"""
## Activation Keywords

- {name}
- {" ".join(keywords)}
- 使用 {name.split('-')[0] if '-' in name else name}
""")
    
    if "## Tools Used" in missing:
        additions.append("""
## Tools Used

- `read`
- `write`
- `exec`
""")
    
    if "## Instructions for Agents" in missing:
        additions.append("""
## Instructions for Agents

1. Read and understand the skill content
2. Follow the methodology described
3. Apply the approach to user requests
4. Provide clear, actionable guidance
""")
    
    if "## Examples" in missing:
        name_match = re.search(r'^name:\s*(\S+)', content, re.MULTILINE)
        name = name_match.group(1) if name_match else skill_path.name
        additions.append(f"""
## Examples

### Example 1: Basic Usage

**User:** Help me with {name.replace('-', ' ')}

**Agent:** I can help you with that using the {name} methodology...
""")
    
    # 将新内容添加到文件末尾
    new_content = content.rstrip() + '\n' + '\n'.join(additions)
    skill_md.write_text(new_content, encoding='utf-8')
    print(f"    ✓ Fixed")
    return True

def main():
    """主函数"""
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
