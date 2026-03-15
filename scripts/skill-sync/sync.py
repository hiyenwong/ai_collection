#!/usr/bin/env python3
"""
Skill Sync Tool - AI Coding Tools Skill Synchronization

整合多个 AI 编码工具的 skill，支持：
1. 收集各平台的 skills
2. 指定主导平台或合并所有平台
3. 分发到各目标工具

Usage:
    python sync.py collect                    # 收集所有平台的 skills
    python sync.py status                     # 查看状态
    python sync.py sync --all                 # 同步所有
    python sync.py sync --target openclaw     # 同步到特定工具
    python sync.py sync --master openclaw     # 以 openclaw 为主导
    python sync.py sync --merge               # 合并所有平台
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

# 配置
SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent.parent
CONFIG_FILE = SCRIPT_DIR / "config.json"
CONVERTERS_DIR = SCRIPT_DIR / "converters"
LOG_FILE = SCRIPT_DIR / "sync.log"


def log(message: str, level: str = "INFO"):
    """记录日志"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level}] {message}"
    print(log_line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line + "\n")


def load_config() -> dict:
    """加载配置文件"""
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)
    # 展开波浪号
    config["source"] = os.path.expanduser(config["source"])
    for target in config["targets"]:
        target["path"] = os.path.expanduser(target["path"])
    if "lastSyncFile" in config["sync"]:
        config["sync"]["lastSyncFile"] = os.path.expanduser(
            config["sync"]["lastSyncFile"]
        )
    return config


def save_config(config: dict):
    """保存配置文件"""
    # 备份原始路径用于保存
    save_cfg = json.loads(json.dumps(config))
    save_cfg["source"] = save_cfg["source"].replace(os.path.expanduser("~"), "~")
    for target in save_cfg["targets"]:
        target["path"] = target["path"].replace(os.path.expanduser("~"), "~")
    if "lastSyncFile" in save_cfg["sync"]:
        save_cfg["sync"]["lastSyncFile"] = save_cfg["sync"]["lastSyncFile"].replace(
            os.path.expanduser("~"), "~"
        )
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(save_cfg, f, indent=2, ensure_ascii=False)


def load_sync_state(config: dict) -> dict:
    """加载同步状态"""
    state_file = Path(config["sync"]["lastSyncFile"])
    if state_file.exists():
        with open(state_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"lastSync": None, "skills": {}, "sources": {}}


def save_sync_state(config: dict, state: dict):
    """保存同步状态"""
    state_file = Path(config["sync"]["lastSyncFile"])
    state_file.parent.mkdir(parents=True, exist_ok=True)
    with open(state_file, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def discover_skills(path: Path) -> Dict[str, dict]:
    """
    发现目录中的所有 skills
    返回 {skill_name: {path, mtime, metadata}}
    """
    skills = {}
    if not path.exists():
        return skills

    for skill_dir in path.iterdir():
        if skill_dir.is_dir():
            skill_file = skill_dir / "SKILL.md"
            if skill_file.exists():
                # 解析 frontmatter
                metadata = parse_frontmatter(skill_file)
                skills[skill_dir.name] = {
                    "path": str(skill_dir),
                    "mtime": skill_file.stat().st_mtime,
                    "metadata": metadata,
                }
    return skills


def parse_frontmatter(skill_file: Path) -> dict:
    """解析 SKILL.md 的 frontmatter"""
    metadata = {}
    try:
        content = skill_file.read_text(encoding="utf-8")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm_text = parts[1].strip()
                for line in fm_text.split("\n"):
                    if ":" in line:
                        key, value = line.split(":", 1)
                        metadata[key.strip()] = value.strip().strip('"')
    except Exception as e:
        log(f"解析 frontmatter 失败 {skill_file}: {e}", "WARN")
    return metadata


def collect_all_skills(config: dict) -> Dict[str, Dict[str, dict]]:
    """
    收集所有平台的 skills
    返回 {platform: {skill_name: skill_info}}
    """
    all_skills = {}

    # 收集中央仓库
    source_path = Path(config["source"])
    if source_path.exists():
        all_skills["central"] = discover_skills(source_path)
        log(f"中央仓库: 发现 {len(all_skills['central'])} 个 skills")

    # 收集各目标平台的 skills
    for target in config["targets"]:
        target_path = Path(target["path"])
        if target_path.exists():
            skills = discover_skills(target_path)
            all_skills[target["name"]] = skills
            log(f"{target['name']}: 发现 {len(skills)} 个 skills")

    return all_skills


def merge_skills(
    all_skills: Dict[str, Dict[str, dict]], master: Optional[str] = None
) -> Dict[str, dict]:
    """
    合并所有平台的 skills

    Args:
        all_skills: 所有平台的 skills
        master: 主导平台名称，如果指定则以此平台为准

    Returns:
        合并后的 skills {skill_name: skill_info}
    """
    merged = {}

    if master and master in all_skills:
        # 以主导平台为准
        log(f"以 {master} 为主导平台")
        merged = dict(all_skills[master])
        # 添加其他平台的独有 skills
        for platform, skills in all_skills.items():
            if platform == master:
                continue
            for skill_name, skill_info in skills.items():
                if skill_name not in merged:
                    merged[skill_name] = skill_info
                    log(f"  从 {platform} 添加: {skill_name}")
    else:
        # 合并所有平台，以最新 mtime 为准
        for platform, skills in all_skills.items():
            for skill_name, skill_info in skills.items():
                if skill_name not in merged:
                    merged[skill_name] = skill_info
                else:
                    # 比较修改时间，保留较新的
                    if skill_info["mtime"] > merged[skill_name]["mtime"]:
                        merged[skill_name] = skill_info
                        log(f"  更新 {skill_name} (来自 {platform})")

    log(f"合并后总计: {len(merged)} 个 skills")
    return merged


def copy_skill(source: Path, dest: Path, mode: str = "copy") -> bool:
    """
    复制或链接 skill 到目标位置

    Args:
        source: 源 skill 目录
        dest: 目标 skill 目录
        mode: "copy" 或 "symlink"

    Returns:
        是否成功
    """
    try:
        # 删除旧的目标
        if dest.exists() or dest.is_symlink():
            if dest.is_symlink():
                dest.unlink()
            else:
                shutil.rmtree(dest)

        if mode == "symlink":
            # 创建符号链接
            dest.symlink_to(source)
            log(f"  创建链接: {dest} -> {source}")
        else:
            # 复制目录
            shutil.copytree(source, dest)
            log(f"  复制: {source} -> {dest}")
        return True
    except Exception as e:
        log(f"  失败: {e}", "ERROR")
        return False


def convert_skill(
    skill_path: Path, target_format: str, converter: Optional[str]
) -> Optional[str]:
    """
    转换 skill 格式

    Args:
        skill_path: skill 目录路径
        target_format: 目标格式
        converter: 转换器脚本名

    Returns:
        转换后的内容（如果需要）
    """
    if not converter:
        return None

    converter_path = CONVERTERS_DIR / converter
    if not converter_path.exists():
        log(f"转换器不存在: {converter}", "WARN")
        return None

    # 调用转换器
    try:
        result = subprocess.run(
            [sys.executable, str(converter_path), str(skill_path)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return result.stdout
        else:
            log(f"转换失败: {result.stderr}", "ERROR")
            return None
    except Exception as e:
        log(f"转换器执行失败: {e}", "ERROR")
        return None


def sync_to_target(
    merged_skills: Dict[str, dict],
    target: dict,
    source_path: Path,
    config: dict,
) -> int:
    """
    同步 skills 到目标平台

    Returns:
        同步成功数量
    """
    target_path = Path(target["path"])
    target_path.mkdir(parents=True, exist_ok=True)

    success_count = 0

    for skill_name, skill_info in merged_skills.items():
        # 获取源路径
        skill_source = Path(skill_info["path"])

        # 如果源不在中央仓库，先复制到中央仓库
        central_skill = source_path / skill_name
        if not central_skill.exists() and skill_source.exists():
            copy_skill(skill_source, central_skill, "copy")
            log(f"  添加到中央仓库: {skill_name}")

        # 同步到目标
        skill_dest = target_path / skill_name

        if target.get("converter"):
            # 需要格式转换
            converted = convert_skill(
                skill_source, target["format"], target["converter"]
            )
            if converted:
                # 写入转换后的内容
                skill_dest.mkdir(parents=True, exist_ok=True)
                (skill_dest / "SKILL.md").write_text(converted, encoding="utf-8")
                success_count += 1
        else:
            # 直接复制或链接
            if copy_skill(central_skill, skill_dest, target.get("mode", "copy")):
                success_count += 1

    return success_count


def cmd_collect(args):
    """收集所有平台的 skills"""
    config = load_config()
    all_skills = collect_all_skills(config)

    print("\n=== Skills 收集结果 ===\n")

    for platform, skills in all_skills.items():
        print(f"📁 {platform} ({len(skills)} 个):")
        for skill_name in sorted(skills.keys()):
            metadata = skills[skill_name].get("metadata", {})
            desc = metadata.get("description", "")[:50]
            print(f"   - {skill_name}: {desc}...")

    # 保存状态
    state = load_sync_state(config)
    state["sources"] = {
        platform: list(skills.keys()) for platform, skills in all_skills.items()
    }
    save_sync_state(config, state)


def cmd_status(args):
    """查看同步状态"""
    config = load_config()
    state = load_sync_state(config)
    all_skills = collect_all_skills(config)

    print("\n=== 同步状态 ===\n")

    # 各平台统计
    print("📊 各平台 Skills 数量:")
    for platform, skills in all_skills.items():
        marker = "📍" if platform == "central" else "  "
        print(f"{marker} {platform}: {len(skills)}")

    # 差异分析
    print("\n🔍 差异分析:")
    central_skills = set(all_skills.get("central", {}).keys())
    for platform, skills in all_skills.items():
        if platform == "central":
            continue
        platform_skills = set(skills.keys())
        only_central = central_skills - platform_skills
        only_platform = platform_skills - central_skills
        if only_central:
            print(f"   {platform} 缺少: {', '.join(only_central)}")
        if only_platform:
            print(f"   {platform} 独有: {', '.join(only_platform)}")

    # 最后同步时间
    if state.get("lastSync"):
        print(f"\n⏰ 最后同步: {state['lastSync']}")


def cmd_sync(args):
    """执行同步"""
    config = load_config()
    all_skills = collect_all_skills(config)

    # 确定合并模式
    master = args.master
    if master:
        log(f"主导模式: {master}")
    else:
        log("合并模式: 所有平台")

    # 合并 skills
    merged_skills = merge_skills(all_skills, master=master)

    # 确定同步目标
    if args.target:
        targets = [t for t in config["targets"] if t["name"] == args.target]
        if not targets:
            log(f"目标不存在: {args.target}", "ERROR")
            return
    elif args.all:
        targets = [t for t in config["targets"] if t.get("enabled", True)]
    else:
        log("请指定 --all 或 --target", "ERROR")
        return

    # 执行同步
    source_path = Path(config["source"])
    source_path.mkdir(parents=True, exist_ok=True)

    print("\n=== 开始同步 ===\n")

    for target in targets:
        log(f"同步到 {target['name']}...")
        count = sync_to_target(merged_skills, target, source_path, config)
        log(f"  完成: {count} 个 skills")

    # 更新状态
    state = load_sync_state(config)
    state["lastSync"] = datetime.now().isoformat()
    state["skills"] = list(merged_skills.keys())
    save_sync_state(config, state)

    log("同步完成!")


def main():
    parser = argparse.ArgumentParser(description="AI Skills 同步工具")
    subparsers = parser.add_subparsers(dest="command", help="命令")

    # collect 命令
    subparsers.add_parser("collect", help="收集所有平台的 skills")

    # status 命令
    subparsers.add_parser("status", help="查看同步状态")

    # sync 命令
    sync_parser = subparsers.add_parser("sync", help="执行同步")
    sync_parser.add_argument("--all", action="store_true", help="同步到所有目标")
    sync_parser.add_argument("--target", type=str, help="同步到指定目标")
    sync_parser.add_argument("--master", type=str, help="指定主导平台")
    sync_parser.add_argument("--merge", action="store_true", help="合并所有平台")

    args = parser.parse_args()

    if args.command == "collect":
        cmd_collect(args)
    elif args.command == "status":
        cmd_status(args)
    elif args.command == "sync":
        cmd_sync(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
