#!/usr/bin/env python3
"""
Skill Migration Execution Script
使用git mv迁移技能到领域子目录（保留git历史）
"""

import subprocess
import json
from pathlib import Path

BASE_DIR = Path("/Users/hiyenwong/ai_github/ai_collection")
SKILLS_DIR = BASE_DIR / "collection/skills"


def load_migration_plan():
    """加载迁移计划"""
    plan_path = BASE_DIR / "skill_migration_plan.json"
    with open(plan_path) as f:
        return json.load(f)


def create_domain_directories(plan: dict):
    """创建领域子目录"""
    for domain, info in plan["target_structure"].items():
        target_path = SKILLS_DIR / domain
        target_path.mkdir(exist_ok=True)
        print(f"Created directory: {target_path}")


def execute_migration(plan: dict):
    """执行迁移（使用git mv保留历史）"""
    total = len(plan["migrations"])

    print(f"\nMigrating {total} skills...")
    print("This will preserve git history using 'git mv'")

    for i, migration in enumerate(plan["migrations"], 1):
        source = BASE_DIR / migration["from"]
        target = BASE_DIR / migration["to"]

        if not source.exists():
            print(f"  [{i}/{total}] SKIP: {source} not found")
            continue

        # 使用git mv保留历史
        cmd = ["git", "mv", str(source), str(target)]
        try:
            subprocess.run(cmd, cwd=BASE_DIR, check=True, capture_output=True)
            print(f"  [{i}/{total}] Migrated: {migration['from']} → {migration['to']}")
        except subprocess.CalledProcessError as e:
            print(f"  [{i}/{total}] ERROR: {e.stderr.decode()}")
            # 如果git mv失败，使用普通mv
            subprocess.run(["mv", str(source), str(target)], check=True)
            print(f"  [{i}/{total}] Fallback to mv (no git history)")


def verify_migration(plan: dict):
    """验证迁移结果"""
    print("\nVerifying migration...")

    success_count = 0
    for migration in plan["migrations"]:
        target = BASE_DIR / migration["to"]
        if target.exists():
            success_count += 1

    print(
        f"Verification: {success_count}/{len(plan['migrations'])} skills migrated successfully"
    )

    # 检查领域目录文件数
    for domain, info in plan["target_structure"].items():
        domain_path = SKILLS_DIR / domain
        if domain_path.exists():
            count = len([d for d in domain_path.iterdir() if d.is_dir()])
            print(f"  {domain}: {count} skills (target: {info['count']})")


def main():
    print("=" * 60)
    print("Skill Migration Execution")
    print("=" * 60)

    # Step 1: 加载迁移计划
    plan = load_migration_plan()
    print(f"Loaded plan: {len(plan['migrations'])} migrations")

    # Step 2: 创建领域目录
    create_domain_directories(plan)

    # Step 3: 执行迁移
    execute_migration(plan)

    # Step 4: 验证
    verify_migration(plan)

    print("\n" + "=" * 60)
    print("Migration Complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review git status")
    print("2. Update INDEX.md and documentation")
    print("3. git commit -m 'Organize skills by domain (fix GitHub truncation)'")
    print("4. git push")


if __name__ == "__main__":
    # 检查是否在git仓库中
    result = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"], cwd=BASE_DIR, capture_output=True
    )

    if result.returncode == 0:
        main()
    else:
        print("ERROR: Not in a git repository")
        print("Run this script from /Users/hiyenwong/ai_github/ai_collection")
