#!/usr/bin/env python3
"""
Extract structured insights from quantum medical imaging papers.
"""

import argparse
import json
import re
from pathlib import Path

ALGORITHMS = [
    "Quantum Fourier Transform", "QFT",
    "Variational Quantum Eigensolver", "VQE",
    "Quantum Approximate Optimization Algorithm", "QAOA",
    "Quantum Annealing",
    "Grover's Algorithm",
    "Shor's Algorithm"
]

APPLICATIONS = [
    "MRI reconstruction", "MRI",
    "CT imaging", "CT",
    "PET imaging", "PET",
    "radiology",
    "medical imaging",
    "diagnostics",
    "biosensing"
]

HARDWARE = [
    "NV centers", "nitrogen-vacancy",
    "superconducting qubits",
    "trapped ions",
    "photonic",
    "quantum dots"
]

METRICS_PATTERN = re.compile(r'(\d+)%\s*(speedup|improvement|reduction|enhancement)')

def extract_paper_insights(text: str) -> dict:
    """Extract structured insights from paper text."""
    
    insights = {
        "algorithm": None,
        "application": None,
        "hardware": None,
        "metrics": [],
        "status": "simulation",  # default
        "key_insight": None
    }
    
    # Extract algorithm
    for algo in ALGORITHMS:
        if algo.lower() in text.lower():
            insights["algorithm"] = algo
            break
    
    # Extract application
    for app in APPLICATIONS:
        if app.lower() in text.lower():
            insights["application"] = app
            break
    
    # Extract hardware
    for hw in HARDWARE:
        if hw.lower() in text.lower():
            insights["hardware"] = hw
            break
    
    # Extract metrics
    metrics_found = METRICS_PATTERN.findall(text)
    for match in metrics_found:
        insights["metrics"].append({
            "value": int(match[0]),
            "type": match[1]
        })
    
    # Determine status
    if "clinical" in text.lower() and "validation" in text.lower():
        insights["status"] = "clinical validation"
    elif "preclinical" in text.lower():
        insights["status"] = "preclinical"
    elif "experiment" in text.lower() and "real" in text.lower():
        insights["status"] = "experimental"
    
    # Extract key insight (first significant finding)
    sentences = text.split('.')
    for sentence in sentences:
        if any(kw in sentence.lower() for kw in ["demonstrate", "show", "achieve", "improve"]):
            insights["key_insight"] = sentence.strip()[:200]
            break
    
    return insights

def main():
    parser = argparse.ArgumentParser(description="Extract insights from quantum medical imaging paper")
    parser.add_argument("--paper", required=True, help="Path to paper file (txt/pdf)")
    parser.add_argument("--output", help="Output JSON file path")
    args = parser.parse_args()
    
    # Read paper (assuming text format for simplicity)
    paper_path = Path(args.paper)
    if paper_path.suffix == ".txt":
        text = paper_path.read_text()
    else:
        # For PDF, would need pdfplumber - just note this
        print("Note: PDF extraction requires pdfplumber. Reading as text...")
        try:
            text = paper_path.read_text()
        except Exception:
            text = ""
    
    insights = extract_paper_insights(text)
    
    if args.output:
        Path(args.output).write_text(json.dumps(insights, indent=2))
        print(f"Insights saved to {args.output}")
    else:
        print(json.dumps(insights, indent=2))

if __name__ == "__main__":
    main()