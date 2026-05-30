#!/usr/bin/env python3
"""
Verification script for ai-collection-research-sync pipeline.

Checks:
1. Skills exist in expected locations
2. INDEX.md contains skill entries
3. Obsidian notes were created
4. Knowledge graph has paper entries
5. Git repository state (optional)

Run: python scripts/verify_pipeline.py --skills skill1 skill2 --arxiv-ids 2605.12345 2605.67890
"""

import os
import sys
import json
import sqlite3
from pathlib import Path
import argparse

def check_skill_exists(skill_name: str) -> dict:
    """Check if skill exists in Hermes skill library."""
    skill_path = Path.home() / ".hermes" / "skills" / "ai_collection" / skill_name
    
    result = {
        "skill": skill_name,
        "exists": skill_path.exists(),
        "skill_md_exists": (skill_path / "SKILL.md").exists(),
        "path": str(skill_path)
    }
    
    if result["skill_md_exists"]:
        # Quick check for arXiv metadata in frontmatter
        skill_md = (skill_path / "SKILL.md").read_text()
        result["has_arxiv_metadata"] = "arxiv_id:" in skill_md
        
    return result

def check_ai_collection_sync(skill_name: str) -> dict:
    """Check if skill synced to ai_collection GitHub repo."""
    ai_collection_path = Path("/Users/hiyenwong/ai_github/ai_collection/collection/skills") / skill_name
    
    result = {
        "skill": skill_name,
        "ai_collection_exists": ai_collection_path.exists(),
        "path": str(ai_collection_path)
    }
    
    return result

def check_index_md(skill_names: list) -> dict:
    """Check if INDEX.md contains skill entries."""
    index_path = Path("/Users/hiyenwong/ai_github/ai_collection/INDEX.md")
    
    result = {
        "index_exists": index_path.exists(),
        "skills_found": []
    }
    
    if result["index_exists"]:
        index_content = index_path.read_text()
        for skill in skill_names:
            if f"[[{skill}]]" in index_content:
                result["skills_found"].append(skill)
    
    result["all_skills_present"] = len(result["skills_found"]) == len(skill_names)
    
    return result

def check_obsidian_notes(arxiv_ids: list) -> dict:
    """Check if Obsidian notes were created."""
    obsidian_path = Path("~/Library/Mobile Documents/iCloud~md~obsidian/Documents").expanduser()
    
    result = {
        "obsidian_path_exists": obsidian_path.exists(),
        "notes_found": []
    }
    
    if result["obsidian_path_exists"]:
        # Look for notes containing arXiv IDs
        for md_file in obsidian_path.glob("*.md"):
            content = md_file.read_text()
            for arxiv_id in arxiv_ids:
                if arxiv_id in content:
                    result["notes_found"].append({
                        "arxiv_id": arxiv_id,
                        "file": md_file.name
                    })
    
    return result

def check_knowledge_graph(arxiv_ids: list) -> dict:
    """Check if kg.db has entries for arXiv papers."""
    kg_path = Path.home() / ".hermes" / "knowledge-graph" / "kg.db"
    
    result = {
        "kg_exists": kg_path.exists(),
        "papers_found": []
    }
    
    if result["kg_exists"]:
        try:
            conn = sqlite3.connect(str(kg_path))
            cursor = conn.cursor()
            
            # Check if arxiv_papers table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='arxiv_papers'")
            result["table_exists"] = cursor.fetchone() is not None
            
            if result["table_exists"]:
                for arxiv_id in arxiv_ids:
                    cursor.execute("SELECT id, title, skill_name FROM arxiv_papers WHERE id = ?", (arxiv_id,))
                    row = cursor.fetchone()
                    if row:
                        result["papers_found"].append({
                            "arxiv_id": row[0],
                            "title": row[1][:50] + "..." if len(row[1]) > 50 else row[1],
                            "skill_name": row[2]
                        })
            
            conn.close()
        except Exception as e:
            result["error"] = str(e)
    
    return result

def check_git_status(skill_names: list) -> dict:
    """Check git repository status (optional, requires terminal access)."""
    # This is a placeholder - actual git check would require terminal tool
    # In background review, terminal is not available
    
    result = {
        "repo_path": "/Users/hiyenwong/ai_github/ai_collection",
        "skills_expected": skill_names,
        "note": "Git check requires terminal tool - run manually if needed"
    }
    
    return result

def main():
    parser = argparse.ArgumentParser(description="Verify ai-collection-research-sync pipeline")
    parser.add_argument("--skills", nargs="+", required=True, help="Skill names to verify")
    parser.add_argument("--arxiv-ids", nargs="+", required=True, help="arXiv IDs to verify")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("AI Collection Research Sync Pipeline Verification")
    print("=" * 60)
    
    # Check skills in Hermes library
    print("\n1. Hermes Skill Library:")
    for skill in args.skills:
        result = check_skill_exists(skill)
        status = "✓" if result["exists"] and result["skill_md_exists"] else "✗"
        print(f"   {status} {skill}")
        if result["exists"]:
            print(f"      Path: {result['path']}")
            print(f"      SKILL.md: {result['skill_md_exists']}")
            print(f"      arXiv metadata: {result.get('has_arxiv_metadata', False)}")
    
    # Check ai_collection sync
    print("\n2. ai_collection GitHub Sync:")
    for skill in args.skills:
        result = check_ai_collection_sync(skill)
        status = "✓" if result["ai_collection_exists"] else "✗"
        print(f"   {status} {skill} synced to ai_collection")
    
    # Check INDEX.md
    print("\n3. INDEX.md Entries:")
    index_result = check_index_md(args.skills)
    status = "✓" if index_result["all_skills_present"] else "✗"
    print(f"   {status} All skills present in INDEX.md")
    print(f"      Found: {index_result['skills_found']}")
    
    # Check Obsidian notes
    print("\n4. Obsidian Notes:")
    obsidian_result = check_obsidian_notes(args.arxiv_ids)
    status = "✓" if len(obsidian_result["notes_found"]) > 0 else "✗"
    print(f"   {status} Obsidian vault accessible")
    print(f"      Notes found: {len(obsidian_result['notes_found'])}")
    for note in obsidian_result["notes_found"]:
        print(f"      - {note['arxiv_id']}: {note['file']}")
    
    # Check knowledge graph
    print("\n5. Knowledge Graph (kg.db):")
    kg_result = check_knowledge_graph(args.arxiv_ids)
    status = "✓" if kg_result["kg_exists"] and len(kg_result["papers_found"]) > 0 else "✗"
    print(f"   {status} kg.db accessible")
    if kg_result["kg_exists"]:
        print(f"      arxiv_papers table: {kg_result.get('table_exists', False)}")
        print(f"      Papers found: {len(kg_result['papers_found'])}")
        for paper in kg_result["papers_found"]:
            print(f"      - {paper['arxiv_id']}: {paper['skill_name']}")
    
    # Git status (note only)
    print("\n6. Git Repository:")
    git_result = check_git_status(args.skills)
    print(f"   Repo: {git_result['repo_path']}")
    print(f"   {git_result['note']}")
    
    # Summary
    print("\n" + "=" * 60)
    all_checks = [
        all([check_skill_exists(s)["exists"] for s in args.skills]),
        all([check_ai_collection_sync(s)["ai_collection_exists"] for s in args.skills]),
        check_index_md(args.skills)["all_skills_present"],
        len(check_obsidian_notes(args.arxiv_ids)["notes_found"]) > 0,
        len(check_knowledge_graph(args.arxiv_ids)["papers_found"]) > 0
    ]
    
    if all(all_checks):
        print("✓ ALL VERIFICATIONS PASSED")
    else:
        print("✗ SOME VERIFICATIONS FAILED")
        print("   Check details above for specific failures")
    
    print("=" * 60)

if __name__ == "__main__":
    main()