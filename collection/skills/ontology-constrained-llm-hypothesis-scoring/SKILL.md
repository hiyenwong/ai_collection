---
name: ontology-constrained-llm-hypothesis-scoring
description: "Multi-LLM pipeline for ontology-constrained literature synthesis in predictive processing neuroscience. Local LLM council scores studies against expert glossary, producing quantitative hypothesis-space maps and auditable disagreement measurements. Use when analyzing heterogeneous literatures, predictive coding, or cross-study hypothesis mapping where conventional meta-analysis lacks common comparison space."
metadata:
  arxiv_id: "2606.05206"
  authors: ["Hamed Nejat", "Alexander Maier", "Jesse Spencer-Smith", "Andre M. Bastos"]
  published: "2026-05-23"
  subjects: ["q-bio.NC", "cs.AI", "stat.AP"]
  tags: [predictive-processing, LLM, ontology, hypothesis-scoring, literature-synthesis, meta-analysis, multi-LLM, evidence-space]
license: Complete terms in LICENSE.txt
---

# Ontology-Constrained Multi-LLM Hypothesis Scoring

## Context

Predictive coding neuroscience spans computational theory, electrophysiology, imaging, behavior, and modeling, creating a synthesis problem that conventional meta-analysis cannot resolve. This framework uses a local multi-LLM council to score studies against an expert-defined ontology, producing quantitative evidence spaces.

## Core Methodology

### 1. Ontology Construction (Expert Glossary)

Define structured concepts grouped into hypotheses:

```python
# Example: Predictive Processing Glossary
glossary = {
    "hypothesis_1": {
        "name": "Predictive Suppression",
        "concepts": [
            "prediction error suppression",
            "feedback inhibition",
            "predictive coding hierarchy",
            "recurrent suppression"
        ]
    },
    "hypothesis_2": {
        "name": "Feedforward Error Propagation",
        "concepts": [
            "error signal propagation",
            "forward pathway",
            "precision-weighted error",
            "prediction error encoding"
        ]
    },
    "hypothesis_3": {
        "name": "Ubiquity",
        "concepts": [
            "widespread prediction error",
            "ubiquitous predictive coding",
            "multi-modal predictive processing",
            "global prediction signals"
        ]
    }
}

# Total: 36 concepts across 3 hypotheses
```

### 2. Paper Extraction Pipeline

```python
def extract_paper_evidence(pdf_path, llm_model):
    """Extract evidence from paper using local LLM"""
    prompt = f"""
    Read this paper and extract:
    1. Main findings related to predictive processing
    2. Experimental paradigm (local oddball, global oddball)
    3. Evidence for/against each concept in the glossary
    4. Figure descriptions if relevant
    
    Paper: {pdf_path}
    Glossary: {glossary}
    """
    
    response = llm_model.generate(prompt)
    return {
        "findings": parse_findings(response),
        "paradigm": parse_paradigm(response),
        "scores": parse_scores(response),
        "figures": parse_figures(response)
    }
```

### 3. Ontology-Constrained Prompt Assembly

```python
def assemble_constrained_prompt(paper_evidence, glossary):
    """Create ontology-constrained scoring prompt"""
    prompt = f"""
    Score this study against the predictive coding glossary.
    
    Study evidence: {paper_evidence['findings']}
    Paradigm: {paper_evidence['paradigm']}
    
    For each of the 36 concepts:
    - Score: +1 (agreement), 0 (neutral), -1 (disagreement)
    - Justify each score with specific evidence from the study
    
    Output format:
    {{
        "concept_name": {{
            "score": [1/0/-1],
            "evidence": [specific quote or finding],
            "confidence": [high/medium/low]
        }}
    }}
    
    Validate all outputs against glossary definitions.
    """
    return prompt
```

### 4. Multi-LLM Council Scoring

```python
def council_scoring(papers, models, glossary):
    """Run multi-LLM council for hypothesis scoring"""
    scores = {}
    for paper_id, evidence in papers.items():
        paper_scores = []
        for model in models:
            prompt = assemble_constrained_prompt(evidence, glossary)
            response = model.generate(prompt)
            validated = validate_against_glossary(response, glossary)
            paper_scores.append(validated)
        
        # Aggregate across council
        scores[paper_id] = aggregate_scores(paper_scores)
    return scores

def aggregate_scores(council_scores):
    """Aggregate scores across LLM models"""
    aggregated = {}
    for concept in all_concepts:
        scores = [s[concept]['score'] for s in council_scores]
        aggregated[concept] = {
            'mean_score': np.mean(scores),
            'std_score': np.std(scores),
            'consensus': check_consensus(scores)
        }
    return aggregated
```

### 5. Hypothesis-Space Mapping

```python
def map_hypothesis_space(scores, hypotheses):
    """Map studies into 3D hypothesis space"""
    coordinates = {}
    for paper_id, paper_scores in scores.items():
        # Compute hypothesis-level scores
        coords = []
        for hypothesis in hypotheses:
            concept_scores = [paper_scores[c]['mean_score'] 
                            for c in hypothesis['concepts']]
            coords.append(np.mean(concept_scores))
        coordinates[paper_id] = coords  # [H1, H2, H3]
    return coordinates
```

### 6. Hypothesis-Space Temperature

```python
def compute_temperature(coordinates):
    """Geometric dispersion metric for hypothesis space"""
    # Convert to numpy array
    points = np.array(list(coordinates.values()))
    
    # Compute centroid
    centroid = np.mean(points, axis=0)
    
    # Compute distances from centroid
    distances = np.linalg.norm(points - centroid, axis=1)
    
    # Temperature = variance of distances
    temperature = np.var(distances)
    return temperature

# Interpretation:
# - Low temperature: studies cluster tightly (high agreement)
# - High temperature: studies dispersed (structured disagreement)
```

### 7. Agreement Analysis

```python
def pairwise_agreement(scores):
    """Compute pairwise study agreement"""
    papers = list(scores.keys())
    agreement_matrix = np.zeros((len(papers), len(papers)))
    
    for i, p1 in enumerate(papers):
        for j, p2 in enumerate(papers):
            # Correlation across all concepts
            s1 = [scores[p1][c]['mean_score'] for c in all_concepts]
            s2 = [scores[p2][c]['mean_score'] for c in all_concepts]
            agreement_matrix[i, j] = np.corrcoef(s1, s2)[0, 1]
    
    return agreement_matrix
```

### 8. Context Transition Vectors

```python
def compute_transition_vectors(local_coords, global_coords):
    """Estimate vectors of change between experimental contexts"""
    transitions = {}
    for paper_id in local_coords.keys():
        if paper_id in global_coords:
            local = np.array(local_coords[paper_id])
            global_ = np.array(global_coords[paper_id])
            transitions[paper_id] = global_ - local
    return transitions
```

## Implementation Workflow

1. **Ontology Definition**: Create expert glossary with 36 concepts grouped into 3 hypotheses
   
2. **Paper Extraction**: Use local LLM to extract evidence from each study
   
3. **Constrained Prompt Assembly**: Format prompts with glossary constraints
   
4. **Council Scoring**: Run 10 local LLM models independently
   
5. **Validation**: Check outputs against glossary definitions
   
6. **Aggregation**: Compute mean scores and consensus measures
   
7. **Hypothesis-Space Mapping**: Map studies into 3D space
   
8. **Temperature Computation**: Calculate dispersion metrics
   
9. **Visualization**:
   - Hypothesis-space scatter plots (3D)
   - Agreement heatmap
   - Temperature comparison (local vs global oddball)

## Key Results

- **High agreement for some hypotheses**: Predictive suppression shows consensus
- **Structured disagreement**: Local vs global oddball paradigms differ systematically
- **Temperature difference**: Local oddball (lower temperature) vs global oddball (higher temperature)
- **Transition vectors**: Quantify paradigm-dependent shifts in hypothesis support
- **Auditable**: Each score traceable to specific evidence and model

## Pitfalls

- **Ontology bias**: Glossary must represent domain consensus, not single perspective
- **Model variance**: Different LLM models may score differently; use council approach
- **Validation gaps**: Check outputs against glossary to prevent hallucination
- **Figure interpretation**: LLMs may miss figure details; include explicit descriptions
- **Paradigm matching**: Ensure correct context (local vs global oddball) assignment
- **Evidence extraction**: Double-check quotes against original paper text

## Verification

```bash
# Check temperature ranges
echo "Local oddball temperature: ~0.05-0.15 (compact cluster)"
echo "Global oddball temperature: ~0.20-0.30 (dispersed)"

# Verify hypothesis scores
echo "Predictive Suppression: scores > 0 for most studies"
echo "Feedforward Error: moderate agreement"
echo "Ubiquity: lowest consensus"

# Check glossary completeness
grep -r "predictive coding" ~/.hermes/skills/ai_collection/*/SKILL.md
```

## Activation Keywords

predictive processing, predictive coding, ontology-constrained, multi-LLM, hypothesis scoring, literature synthesis, meta-analysis, evidence space, hypothesis-space mapping, local oddball, global oddball, LLM council, glossary validation, temperature metric, geometric dispersion, auditable disagreement, cross-study comparison, evidence aggregation, predictive suppression, feedforward error, ubiquitous coding