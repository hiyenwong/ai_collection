#!/usr/bin/env python3
"""
AI Research Daily Fetch Script
Fetches latest research from AI labs and creates Obsidian notes
"""

import os
import sys
import re
import subprocess
from datetime import datetime

# Configuration
OBSIDIAN_PATH = os.environ.get('OBSIDIAN_VAULT', '/Users/hiyenwong/obsdian/Documents/OpenAI Research')
JINA_AI_BASE = 'https://r.jina.ai/http://'

# Auto-detect proxy or use environment variable
PROXY = os.environ.get('HTTP_PROXY') or os.environ.get('HTTPS_PROXY')
if not PROXY:
    # Try common proxy ports
    for test_port in ['7890', '7891', '7897', '1080', '1087', '9090']:
        try:
            result = subprocess.run(
                ['curl', '-s', '--max-time', '2', '--proxy', f'http://127.0.0.1:{test_port}',
                 'https://httpbin.org/ip'],
                capture_output=True, text=True, timeout=3
            )
            if result.returncode == 0 and 'origin' in result.stdout:
                PROXY = f'http://127.0.0.1:{test_port}'
                print(f'Detected working proxy: {PROXY}')
                break
        except Exception:
            pass

if not PROXY:
    print('Warning: No working proxy detected, trying direct connection...')

def run_command(cmd, timeout=60):
    """Run shell command"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return '', 'Timeout', 1

def fetch_url(url):
    """Fetch URL content via jina.ai with proxy fallback"""
    services = [
        f'{JINA_AI_BASE}{url}',
        f'https://r.jina.ai/http://r.jina.ai/http://{url}',
    ]

    for jina_url in services:
        # Try with proxy first if available
        if PROXY:
            cmd = f'curl -sL --max-time 30 --proxy "{PROXY}" "{jina_url}" 2>&1'
            stdout, stderr, code = run_command(cmd, timeout=35)
            if code == 0 and stdout and len(stdout) > 100:
                return stdout

        # Try without proxy
        cmd = f'curl -sL --max-time 30 "{jina_url}" 2>&1'
        stdout, stderr, code = run_command(cmd, timeout=35)
        if code == 0 and stdout and len(stdout) > 100:
            return stdout

    return None

def parse_research_page(content):
    """Parse research page and extract articles"""
    articles = []
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, content)
    
    for title, url in matches:
        if 'openai.com' in url and ('index' in url or 'research' in url):
            articles.append({
                'title': title,
                'url': url if url.startswith('http') else f'https://openai.com{url}',
                'date': datetime.now().strftime('%Y-%m-%d')
            })
    
    return articles

def create_paper_note(article):
    """Create paper note from article"""
    title = article['title']
    url = article['url']
    date = article['date']
    
    clean_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '-').lower()[:50]
    filename = f'{clean_title}.md'
    filepath = os.path.join(OBSIDIAN_PATH, 'Papers', filename)
    
    if os.path.exists(filepath):
        print(f'Note exists: {filename}')
        return None
    
    content = fetch_url(url)
    if not content:
        print(f'Failed to fetch: {url}')
        return None
    
    summary = content[:500] if len(content) > 500 else content
    
    note_content = f'''---
title: {title}
date: {date}
url: {url}
tags: [new, todo]
status: draft
---

# {title}

## 基本信息
- **发布日期**: {date}
- **原文链接**: [{url}]({url})
- **研究类型**: 待分类
- **重要性**: 待评估

---

## 原文摘要
{summary}

---

## 中文翻译
[待翻译]

---

## 深度解读
### 核心创新
[待补充]

### 技术细节
[待补充]

### 性能提升
[待补充]

---

## 关键要点
1. [待补充]
2. [待补充]
3. [待补充]

---

## 实际应用
[待补充]

---

## 局限性与风险
[待补充]

---

## 相关链接
- [官方博客]({url})

---

## 个人笔记
[待补充]

---

*创建于: {datetime.now().strftime("%Y-%m-%d")}*
*状态: 草稿 - 需要完善*
'''
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(note_content)
    
    print(f'Created: {filename}')
    return filename

def create_daily_update(articles):
    """Create daily update note"""
    today = datetime.now().strftime('%Y-%m-%d')
    filename = f'{today}.md'
    filepath = os.path.join(OBSIDIAN_PATH, 'Daily Updates', filename)
    
    if os.path.exists(filepath):
        print(f'Daily update exists: {filename}')
        return
    
    articles_section = ''
    for i, article in enumerate(articles[:5], 1):
        clean_title = re.sub(r'[^\w\s-]', '', article['title']).strip().replace(' ', '-').lower()[:50]
        articles_section += f'''### {i}. {article['title']}
- **类型**: 待分类
- **重要性**: 待评估
- **一句话总结**: [待总结]
- **详细笔记**: [[{clean_title}]]

'''
    
    if not articles_section:
        articles_section = '今日无新研究。\n'
    
    content = f'''---
date: {today}
type: daily-update
---

# AI Research Daily Update - {today}

## 今日概览
- **新发布研究**: {len(articles)} 篇
- **重要更新**: 待评估
- **重点关注**: [待确定]

---

## 新发布内容
{articles_section}
---

## 趋势观察
### 本周热点
[待分析]

### 技术演进方向
[待分析]

---

## 行动计划
- [ ] 深入阅读重要论文
- [ ] 更新相关技术笔记
- [ ] 实践新功能/工具
- [ ] 分享关键发现

---

*自动生成于: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
'''
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Created daily update: {filename}')

def main():
    print('Fetching AI Research updates...')
    print(f'Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    
    research_url = 'openai.com/research'
    print(f'\nFetching: {research_url}')
    
    content = fetch_url(research_url)
    if not content:
        print('Failed to fetch research page')
        print('\nPossible causes:')
        print('1. Proxy service not running (Clash/V2Ray/etc.)')
        print('2. Network connectivity issues')
        print('3. jina.ai service unavailable')
        print('\nTo fix:')
        print('1. Start your proxy service (Clash Verge, V2Ray, etc.)')
        print('2. Verify proxy: curl --proxy http://127.0.0.1:7890 https://httpbin.org/ip')
        print('3. Test jina.ai: curl -sL "https://r.jina.ai/http://openai.com/research"')
        sys.exit(1)
    
    print('\nParsing articles...')
    articles = parse_research_page(content)
    print(f'Found {len(articles)} articles')
    
    print('\nCreating notes...')
    created = []
    for article in articles[:3]:
        note = create_paper_note(article)
        if note:
            created.append(note)
    
    print('\nCreating daily update...')
    create_daily_update(articles)
    
    print(f'\nDone! Created {len(created)} notes.')

if __name__ == '__main__':
    main()
