#!/usr/bin/env python3
"""
自动化目录监控和提醒工具
检查每个目录的文件数量,如果接近GitHub显示限制(1000)则发出警告
"""

import sys
from pathlib import Path

# GitHub显示限制
GITHUB_DISPLAY_LIMIT = 1000
WARNING_THRESHOLD = 800  # 超过800个文件就发出警告
CRITICAL_THRESHOLD = 900  # 超过900个文件就发出严重警告


def count_files_in_directory(dir_path):
    """递归计算目录中的文件总数"""
    total = 0
    try:
        for item in Path(dir_path).rglob("*"):
            if item.is_file() and not item.name.startswith("."):
                total += 1
    except Exception as e:
        print(f"Error counting {dir_path}: {e}")
    return total


def scan_repository(root_path):
    """扫描repository的目录结构"""
    results = {}

    # 检查collection/skills/的每个域目录
    skills_path = Path(root_path) / "collection" / "skills"
    if skills_path.exists():
        for domain_dir in skills_path.iterdir():
            if domain_dir.is_dir() and not domain_dir.name.startswith("."):
                file_count = count_files_in_directory(domain_dir)
                results[domain_dir.name] = {
                    "path": str(domain_dir),
                    "count": file_count,
                    "status": "OK"
                    if file_count < WARNING_THRESHOLD
                    else "WARNING"
                    if file_count < CRITICAL_THRESHOLD
                    else "CRITICAL",
                }

    # 检查collection/agents/
    agents_path = Path(root_path) / "collection" / "agents"
    if agents_path.exists():
        for agent_dir in agents_path.iterdir():
            if agent_dir.is_dir() and not agent_dir.name.startswith("."):
                file_count = count_files_in_directory(agent_dir)
                results[f"agents/{agent_dir.name}"] = {
                    "path": str(agent_dir),
                    "count": file_count,
                    "status": "OK"
                    if file_count < WARNING_THRESHOLD
                    else "WARNING"
                    if file_count < CRITICAL_THRESHOLD
                    else "CRITICAL",
                }

    return results


def generate_report(results):
    """生成报告"""
    print("=" * 80)
    print("DIRECTORY SIZE MONITORING REPORT")
    print("=" * 80)
    print()

    # 按文件数量排序
    sorted_results = sorted(results.items(), key=lambda x: x[1]["count"], reverse=True)

    critical_count = 0
    warning_count = 0

    for domain, data in sorted_results:
        status = data["status"]
        count = data["count"]
        path = data["path"]

        if status == "CRITICAL":
            print(f"🔴 CRITICAL: {domain} ({count} files) - EXCEEDS LIMIT!")
            print(f"   Path: {path}")
            print("   Action needed: Split into subdirectories immediately!")
            critical_count += 1
        elif status == "WARNING":
            print(f"⚠️  WARNING: {domain} ({count} files) - Approaching limit!")
            print(f"   Path: {path}")
            print("   Consider splitting soon")
            warning_count += 1
        else:
            print(f"✅ OK: {domain} ({count} files)")

    print()
    print("=" * 80)
    print("SUMMARY:")
    print(f"  Total directories scanned: {len(results)}")
    print(f"  Critical (needs immediate action): {critical_count}")
    print(f"  Warning (monitor closely): {warning_count}")
    print(f"  GitHub display limit: {GITHUB_DISPLAY_LIMIT}")
    print("=" * 80)

    if critical_count > 0 or warning_count > 0:
        print(
            "\n⚠️  ATTENTION: Some directories are approaching GitHub's display limit!"
        )
        print("   Run subdivision scripts to prevent truncation issues.")
        return False
    else:
        print("\n✅ All directories are within safe limits.")
        return True


def main():
    # 确定repository根目录
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
    else:
        # 默认使用当前目录或检测.git目录
        current_dir = Path.cwd()
        if (current_dir / ".git").exists():
            root_path = current_dir
        else:
            # 尝试向上查找.git目录
            for parent in current_dir.parents:
                if (parent / ".git").exists():
                    root_path = parent
                    break
            else:
                print("Error: Cannot find Git repository root")
                sys.exit(1)

    print(f"Scanning repository: {root_path}")
    print()

    results = scan_repository(root_path)
    all_ok = generate_report(results)

    # 返回状态码供CI/CD使用
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
