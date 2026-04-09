# AI Usage Monitor - 非百炼 AI 使用检测

**创建时间：** 2026-03-24 15:45
**用途：** 通过 CodexBar 检测除了百炼(bailian/zai)以外的 AI 使用情况

---

## 激活关键词

- ai usage monitor
- codexbar usage
- check ai usage
- non-bailian usage
- AI 使用监控
- 检测 AI 使用

## 工具说明

**CodexBar** 是一个 AI 使用量监控工具，支持多个 AI 提供商：
- copilot (GitHub Copilot)
- gemini (Google Gemini)
- claude (Anthropic Claude)
- cursor (Cursor)
- codex (OpenAI Codex)
- zai (百炼/智谱) ← 排除这个
- minimax
- kimi
- 等等

## 快速使用

### 检查所有非百炼 AI 使用情况

```bash
# 检查 Copilot 使用量
codexbar usage --provider copilot

# 检查 Gemini 使用量
codexbar usage --provider gemini

# 检查 Claude 使用量
codexbar usage --provider claude
```

### JSON 格式输出

```bash
codexbar usage --provider copilot --format json
```

## 检测脚本

```python
#!/usr/bin/env python3
"""
AI 使用量监控脚本
检测除百炼以外的 AI 使用情况
"""

import subprocess
import json
import sys
from datetime import datetime

# 排除的提供商（百炼）
EXCLUDED_PROVIDERS = ['zai', 'minimax']  # zai = 百炼/智谱

# 启用的提供商（从 config.json）
ENABLED_PROVIDERS = [
    'copilot',
    'gemini',
    'cursor',
    'antigravity'
]


def run_codexbar(provider, format='json'):
    """
    运行 codexbar 获取使用量
    """
    try:
        result = subprocess.run(
            ['codexbar', 'usage', '--provider', provider, '--format', format],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            return json.loads(result.stdout)
        else:
            return {'error': result.stderr, 'provider': provider}
    except subprocess.TimeoutExpired:
        return {'error': 'Timeout', 'provider': provider}
    except json.JSONDecodeError:
        return {'error': 'Invalid JSON', 'raw': result.stdout, 'provider': provider}
    except Exception as e:
        return {'error': str(e), 'provider': provider}


def get_all_usage(exclude=EXCLUDED_PROVIDERS):
    """
    获取所有启用的 AI 使用量（排除指定提供商）
    """
    results = {}

    for provider in ENABLED_PROVIDERS:
        if provider in exclude:
            continue

        print(f"检查 {provider}...")
        usage = run_codexbar(provider)

        if 'error' not in usage:
            results[provider] = usage
        else:
            results[provider] = {'status': 'error', 'message': usage.get('error')}

    return results


def format_usage_report(results):
    """
    格式化使用报告
    """
    report = []
    report.append("=" * 50)
    report.append(f"AI 使用量报告 - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("=" * 50)

    for provider, data in results.items():
        report.append(f"\n### {provider.upper()}")

        if 'error' in data:
            report.append(f"  状态: 错误 - {data['error']}")
            continue

        if isinstance(data, list) and len(data) > 0:
            for item in data:
                if 'usage' in item:
                    usage = item['usage']
                    if 'primary' in usage:
                        used = usage['primary'].get('usedPercent', 'N/A')
                        report.append(f"  使用量: {used}%")
                    if 'identity' in usage:
                        login = usage['identity'].get('loginMethod', 'N/A')
                        report.append(f"  登录方式: {login}")
        elif isinstance(data, dict):
            if 'usage' in data:
                usage = data['usage']
                if 'primary' in usage:
                    used = usage['primary'].get('usedPercent', 'N/A')
                    report.append(f"  使用量: {used}%")

    report.append("\n" + "=" * 50)
    return "\n".join(report)


def check_usage_alert(results, threshold=80):
    """
    检查使用量是否超过阈值
    """
    alerts = []

    for provider, data in results.items():
        if isinstance(data, list):
            for item in data:
                if 'usage' in item and 'primary' in item['usage']:
                    used = item['usage']['primary'].get('usedPercent', 0)
                    if isinstance(used, (int, float)) and used >= threshold:
                        alerts.append({
                            'provider': provider,
                            'used': used,
                            'alert': f"⚠️ {provider} 使用量已达 {used}%"
                        })

    return alerts


def main():
    """
    主函数
    """
    import argparse

    parser = argparse.ArgumentParser(description='AI 使用量监控')
    parser.add_argument('--provider', '-p', help='指定提供商')
    parser.add_argument('--all', '-a', action='store_true', help='检查所有提供商')
    parser.add_argument('--alert', '-l', type=int, default=80, help='使用量警告阈值')
    parser.add_argument('--json', '-j', action='store_true', help='JSON 输出')
    args = parser.parse_args()

    if args.provider:
        # 单个提供商
        result = run_codexbar(args.provider)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_usage_report({args.provider: result}))
    else:
        # 所有提供商
        results = get_all_usage()
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(format_usage_report(results))

            # 检查警告
            alerts = check_usage_alert(results, args.alert)
            if alerts:
                print("\n⚠️ 使用量警告:")
                for alert in alerts:
                    print(f"  {alert['alert']}")


if __name__ == '__main__':
    main()
```

## 使用示例

### 1. 检查所有非百炼 AI

```bash
python ai_usage_monitor.py --all
```

输出示例：
```
==================================================
AI 使用量报告 - 2026-03-24 15:45
==================================================

### COPILOT
  使用量: 100%
  登录方式: Individual

### GEMINI
  使用量: 45%
  登录方式: OAuth

### CURSOR
  使用量: 30%

==================================================
⚠️ 使用量警告:
  ⚠️ copilot 使用量已达 100%
```

### 2. 检查单个提供商

```bash
python ai_usage_monitor.py --provider copilot
```

### 3. JSON 输出

```bash
python ai_usage_monitor.py --all --json
```

### 4. 设置警告阈值

```bash
python ai_usage_monitor.py --all --alert 90
```

## 配置文件

位置：`~/.codexbar/config.json`

```json
{
  "providers": [
    {"enabled": true, "id": "copilot"},
    {"enabled": true, "id": "gemini"},
    {"enabled": true, "id": "cursor"},
    {"enabled": false, "id": "zai"}  // 百炼已禁用
  ]
}
```

## 定时检查

使用 cron 每小时检查一次：

```bash
# 添加到 crontab
0 * * * * python /path/to/ai_usage_monitor.py --all >> /tmp/ai_usage.log
```

## 相关命令

```bash
# 查看帮助
codexbar --help

# 查看所有启用状态
codexbar usage --status

# 仅查看状态不获取使用量
codexbar usage --provider copilot --status
```

---

_此技能用于监控非百炼 AI 的使用情况，帮助管理 AI 资源_