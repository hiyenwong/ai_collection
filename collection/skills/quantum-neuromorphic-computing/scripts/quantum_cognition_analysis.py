#!/usr/bin/env python3
"""Quantum Cognition Analysis Script

Analyzes quantum cognition papers from knowledge graph,
extracting key patterns and insights for skill development.
"""

import sqlite3
import json
import argparse
from typing import Dict, List, Optional

KG_DB_PATH = "/Users/hiyenwong/.openclaw/workspace/kg.db"

def get_paper(conn: sqlite3.Connection, paper_id: int) -> Optional[Dict]:
    """Get paper details from knowledge graph."""
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, properties FROM kg_entities WHERE id = ?",
        (paper_id,)
    )
    row = cursor.fetchone()
    if not row:
        return None
    
    return {
        "id": row[0],
        "name": row[1],
        "properties": json.loads(row[2]) if row[2] else {}
    }

def find_quantum_cognition_papers(conn: sqlite3.Connection) -> List[Dict]:
    """Find quantum cognition related papers."""
    cursor = conn.cursor()
    
    # Search for quantum cognition keywords
    keywords = [
        "quantum cognition",
        "quantum brain",
        "quantum neural",
        "quantum decision",
        "quantum reservoir",
        "quantum extreme learning"
    ]
    
    papers = []
    for kw in keywords:
        cursor.execute(
            "SELECT id, name, properties FROM kg_entities WHERE entity_type = 'paper' AND name LIKE ?",
            (f"%{kw}%",)
        )
        for row in cursor.fetchall():
            papers.append({
                "id": row[0],
                "name": row[1],
                "properties": json.loads(row[2]) if row[2] else {}
            })
    
    # Deduplicate by id
    seen = set()
    unique = []
    for p in papers:
        if p["id"] not in seen:
            seen.add(p["id"])
            unique.append(p)
    
    return unique

def analyze_paper(paper: Dict) -> Dict:
    """Analyze a quantum cognition paper for key patterns."""
    props = paper.get("properties", {})
    
    analysis = {
        "paper_id": paper["id"],
        "title": paper["name"],
        "arxiv_id": props.get("arxiv_id", ""),
        "key_concepts": [],
        "applications": [],
        "methods": []
    }
    
    abstract = props.get("abstract", "").lower()
    
    # Extract key concepts
    concept_keywords = {
        "quantum cognition": "Quantum probability for cognitive modeling",
        "deliberative": "Deliberative decision making",
        "attention": "Dynamical attention mechanism",
        "reservoir": "Quantum reservoir computing",
        "extreme learning": "Quantum extreme learning",
        "superposition": "Quantum superposition states",
        "entanglement": "Quantum entanglement",
        "contextuality": "Quantum contextuality",
        "phase transition": "Quantum phase transitions",
        "synaptic feedback": "Synaptic feedback modulation"
    }
    
    for kw, concept in concept_keywords.items():
        if kw in abstract:
            analysis["key_concepts"].append(concept)
    
    # Extract applications
    app_keywords = {
        "classification": "Classification tasks",
        "decision": "Decision making",
        "sequence": "Sequence analysis",
        "anomaly": "Anomaly detection",
        "diagnosis": "Automatic diagnosis",
        "inference": "Symbolic inference"
    }
    
    for kw, app in app_keywords.items():
        if kw in abstract:
            analysis["applications"].append(app)
    
    # Extract methods
    method_keywords = {
        "hamiltonian": "Hamiltonian-based evolution",
        "mean-field": "Mean-field equations",
        "husimi": "Husimi distribution analysis",
        "entropy": "Wehrl entropy measurement",
        "quantum monte carlo": "Quantum Monte Carlo simulation",
        "neural network": "Neural network architecture"
    }
    
    for kw, method in method_keywords.items():
        if kw in abstract:
            analysis["methods"].append(method)
    
    return analysis

def main():
    parser = argparse.ArgumentParser(description="Quantum Cognition Analysis")
    parser.add_argument("--input", type=int, help="Paper entity ID to analyze")
    parser.add_argument("--kg", type=str, default=KG_DB_PATH, help="Knowledge graph database path")
    parser.add_argument("--output", type=str, help="Output JSON file path")
    args = parser.parse_args()
    
    conn = sqlite3.connect(args.kg)
    
    if args.input:
        paper = get_paper(conn, args.input)
        if paper:
            analysis = analyze_paper(paper)
            print(f"\n# Analysis of Paper ID {args.input}")
            print(f"Title: {analysis['title']}")
            print(f"\nKey Concepts: {', '.join(analysis['key_concepts'])}")
            print(f"Applications: {', '.join(analysis['applications'])}")
            print(f"Methods: {', '.join(analysis['methods'])}")
            
            if args.output:
                with open(args.output, 'w') as f:
                    json.dump(analysis, f, indent=2)
        else:
            print(f"Paper ID {args.input} not found")
    else:
        # Analyze all quantum cognition papers
        papers = find_quantum_cognition_papers(conn)
        print(f"\n# Quantum Cognition Papers Analysis")
        print(f"Found {len(papers)} papers")
        
        all_analysis = []
        for paper in papers:
            analysis = analyze_paper(paper)
            all_analysis.append(analysis)
            print(f"\n- {analysis['arxiv_id']}: {analysis['title'][:60]}...")
            print(f"  Concepts: {len(analysis['key_concepts'])}")
            print(f"  Applications: {len(analysis['applications'])}")
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(all_analysis, f, indent=2)
    
    conn.close()

if __name__ == "__main__":
    main()