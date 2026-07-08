#!/usr/bin/env python3
"""
Complete KG research workflow script
Usage: python3 scripts/kg_workflow.py
"""

import sys
import os

sys.path.append("/Users/hiyenwong/.openclaw/workspace/scripts")

from import_papers import import_papers
from regenerate_embeddings import regenerate_all_embeddings


def run_workflow():
    """Execute full KG research workflow"""

    print("=" * 60)
    print("KG Research Workflow")
    print("=" * 60)

    # Step 1: Import papers
    print("\n[Step 1] Importing papers...")
    _ = import_papers()

    # Step 2: Generate embeddings
    print("\n[Step 2] Generating embeddings...")
    regenerate_all_embeddings()

    # Step 3: Run KG stats
    print("\n[Step 3] KG Statistics:")
    os.system(
        "/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool stats /Users/hiyenwong/.openclaw/workspace/kg.db"
    )

    # Step 4: PageRank
    print("\n[Step 4] PageRank Analysis:")
    os.system(
        "/Users/hiyenwong/.openclaw/workspace/scripts/kg_tool/target/release/kg_tool pagerank /Users/hiyenwong/.openclaw/workspace/kg.db"
    )

    # Step 5: Vector search
    print("\n[Step 5] Vector Similarity Search:")
    os.system("python3 /Users/hiyenwong/.openclaw/workspace/scripts/vector_search.py")

    print("\n" + "=" * 60)
    print("Workflow Complete")
    print("=" * 60)


if __name__ == "__main__":
    run_workflow()
