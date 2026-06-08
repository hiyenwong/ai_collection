#!/usr/bin/env python3
"""
Migration execution script using git mv to preserve history.

Pattern: Batch git mv operations with progress tracking and error handling.

Usage:
    python migrate_by_domain.py <base_dir> --plan migration_plan.json
"""

import os
import json
import argparse
import subprocess
from pathlib import Path
from collections import defaultdict


def git_mv(source: str, dest: str) -> bool:
    """
    Execute git mv operation.
    
    Returns True if successful, False if failed.
    """
    try:
        subprocess.run(
            ["git", "mv", source, dest],
            check=True,
            capture_output=True,
            text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Failed: {source} -> {dest}")
        print(f"    Error: {e.stderr}")
        return False


def main(base_dir: str, plan_file: str = "migration_plan.json"):
    """Execute migration plan using git mv."""
    
    # Load migration plan
    with open(plan_file) as f:
        migration_plan = json.load(f)
    
    base_path = Path(base_dir)
    
    # Create domain directories
    domains = set(entry['domain'] for entry in migration_plan)
    for domain in domains:
        domain_dir = base_path / domain
        domain_dir.mkdir(exist_ok=True)
        print(f"Created directory: {domain_dir}/")
    
    # Execute migrations
    print(f"\nMigrating {len(migration_plan)} entries...")
    
    success_count = 0
    fail_count = 0
    domain_counts = defaultdict(int)
    
    for entry in migration_plan:
        name = entry['name']
        domain = entry['domain']
        
        source = str(base_path / name)
        dest = str(base_path / domain / name)
        
        # Check source exists
        if not Path(source).exists():
            print(f"  ⚠ Source not found: {source}")
            fail_count += 1
            continue
        
        # Execute git mv
        if git_mv(source, dest):
            success_count += 1
            domain_counts[domain] += 1
            print(f"  ✓ {name} -> {domain}/")
        else:
            fail_count += 1
    
    # Summary report
    print(f"\n{'='*60}")
    print(f"Migration complete:")
    print(f"  Success: {success_count}")
    print(f"  Failed: {fail_count}")
    
    print(f"\nPer-domain counts:")
    for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
        print(f"  {domain}: {count}")
    
    # Safety check
    max_domain, max_count = max(domain_counts.items(), key=lambda x: x[1])
    if max_count > 1000:
        print(f"\n⚠ WARNING: {max_domain} still exceeds 1000 entries")
        print("   Requires further splitting before push to GitHub")
    
    if fail_count > 0:
        print(f"\n⚠ {fail_count} migrations failed — check errors above")
        print("   Review git status before committing")
    
    # Git status hint
    print(f"\n{'='*60}")
    print("Next steps:")
    print("  1. Verify: git status")
    print("  2. Commit: git add -A && git commit -m 'Reorganize by domain'")
    print("  3. Push:   git push origin main")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute repository migration with git mv")
    parser.add_argument("base_dir", help="Base directory containing entries to migrate")
    parser.add_argument("--plan", default="migration_plan.json", help="Migration plan JSON file")
    
    args = parser.parse_args()
    main(args.base_dir, args.plan)