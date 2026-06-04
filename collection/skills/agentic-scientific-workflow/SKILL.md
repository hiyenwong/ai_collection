---
name: agentic-scientific-workflow
description: Multi-agent AI framework for automating scientific workflow generation from natural language research questions. Bridges intent understanding, data discovery, tool selection, and workflow composition for autonomous scientific pipelines. Use for scientific automation, workflow generation, research pipeline automation, multi-agent scientific AI.
---

# Agentic AI Framework for Scientific Workflow Automation

This skill provides a multi-agent AI framework that automates the translation of natural language research questions into executable scientific workflow specifications, based on the paper "From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation" (arXiv:2604.21910).

## Problem Statement

**Gap in Scientific Computing**: Existing workflow systems automate execution (scheduling, fault tolerance, resource management) but NOT the semantic translation from research questions to workflow specifications.

**Current State**: Scientists manually convert research questions → workflow specifications, requiring both domain expertise and infrastructure knowledge.

**Solution**: Multi-agent AI system that automates this translation with 87% accuracy.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Scientific Workflow System                     │
├─────────────────────────────────────────────────────────────────┤
│  Input: Natural Language Research Question                        │
│                           ↓                                       │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │   Intent    │  │    Data      │  │    Tool      │            │
│  │Understanding│→ │  Discovery   │→ │  Selection   │            │
│  │   Agent     │  │    Agent     │  │    Agent     │            │
│  └─────────────┘  └──────────────┘  └──────────────┘            │
│         ↓                  ↓                  ↓                   │
│         └──────────────────┴──────────────────┘                    │
│                           ↓                                       │
│  ┌──────────────────────────────────────────┐                   │
│  │        Workflow Composition Agent        │                   │
│  │  - Integrate components                  │                   │
│  │  - Generate executable workflow          │                   │
│  │  - Validate syntax and semantics       │                   │
│  └──────────────────────────────────────────┘                   │
│                           ↓                                       │
│  Output: Executable Workflow Specification (e.g., CWL, Nextflow) │
└─────────────────────────────────────────────────────────────────┘
```

## Multi-Agent Architecture

### Agent 1: Intent Understanding Agent

**Purpose**: Parse natural language research questions into structured research intent.

**Input**: "Analyze differential gene expression between tumor and normal samples using RNA-seq data"

**Output**:
```json
{
  "research_goal": "differential_expression_analysis",
  "data_type": "rna_seq",
  "comparison_groups": ["tumor", "normal"],
  "analysis_type": "differential_expression",
  "expected_outputs": ["differential_genes", "volcano_plot", "heatmap"],
  "computational_requirements": {
    "memory": "32GB",
    "runtime": "hours",
    "parallelism": "sample_level"
  }
}
```

**Components**:
- LLM for semantic parsing (GPT-4/Claude/DeepSeek)
- Domain-specific prompt engineering
- Ontology mapping (EDAM, BioPortal)

### Agent 2: Data Discovery Agent

**Purpose**: Identify, locate, and describe required datasets.

**Capabilities**:
- Search public repositories (GEO, SRA, Zenodo)
- Query institutional data catalogs
- Infer data formats and metadata
- Assess data quality and availability

**Output**:
```json
{
  "discovered_data": [
    {
      "source": "GEO",
      "accession": "GSE12345",
      "description": "RNA-seq from tumor/normal samples",
      "format": "fastq",
      "samples": 50,
      "size_gb": 120,
      "quality_score": 0.95
    }
  ],
  "data_mapping": {
    "tumor_samples": "GSE12345_tumor_*.fastq",
    "normal_samples": "GSE12345_normal_*.fastq"
  }
}
```

### Agent 3: Tool Selection Agent

**Purpose**: Select appropriate tools and algorithms for the workflow.

**Knowledge Base**:
- Bioinformatics tools: STAR, HISAT2, Salmon, DESeq2, edgeR
- ML frameworks: scikit-learn, TensorFlow, PyTorch
- Workflow tools: CWL, Nextflow, Snakemake, WDL

**Selection Criteria**:
- Domain appropriateness
- Computational requirements
- Input/output compatibility
- Community adoption (citations, maintenance)

**Output**:
```json
{
  "selected_tools": [
    {
      "name": "fastp",
      "version": "0.23.2",
      "purpose": "quality_control",
      "inputs": ["raw_fastq"],
      "outputs": ["clean_fastq", "qc_report"]
    },
    {
      "name": "star",
      "version": "2.7.10a",
      "purpose": "alignment",
      "inputs": ["clean_fastq", "reference_genome"],
      "outputs": ["bam", "alignment_stats"]
    },
    {
      "name": "featureCounts",
      "version": "2.0.3",
      "purpose": "quantification",
      "inputs": ["bam", "annotation_gtf"],
      "outputs": ["counts_matrix"]
    },
    {
      "name": "deseq2",
      "version": "1.38.0",
      "purpose": "differential_expression",
      "inputs": ["counts_matrix", "sample_metadata"],
      "outputs": ["de_results", "plots"]
    }
  ]
}
```

### Agent 4: Workflow Composition Agent

**Purpose**: Assemble selected components into executable workflow.

**Tasks**:
1. Define step dependencies (DAG construction)
2. Map data flows between steps
3. Generate workflow code (CWL/Nextflow/Snakemake)
4. Add resource specifications
5. Validate syntax and semantics

**Output Example (CWL)**:
```yaml
# workflow.cwl
class: Workflow
cwlVersion: v1.2

inputs:
  tumor_samples: File[]
  normal_samples: File[]
  reference_genome: File
  annotation_gtf: File

steps:
  quality_control:
    run: fastp.cwl
    in:
      reads: [tumor_samples, normal_samples]
    out: [clean_reads, qc_reports]
  
  alignment:
    run: star.cwl
    in:
      reads: quality_control/clean_reads
      genome: reference_genome
    out: [aligned_bam, alignment_stats]
    scatter: reads
  
  quantification:
    run: featurecounts.cwl
    in:
      bam: alignment/aligned_bam
      annotation: annotation_gtf
    out: [counts_matrix]
  
  differential_expression:
    run: deseq2.cwl
    in:
      counts: quantification/counts_matrix
      metadata: sample_metadata
    out: [de_results, volcano_plot, heatmap]

outputs:
  de_results: differential_expression/de_results
  plots: [differential_expression/volcano_plot, differential_expression/heatmap]
```

## Implementation

### Agent Orchestration Framework

```python
from typing import List, Dict, Any
import asyncio

class ScientificWorkflowOrchestrator:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.agents = {
            "intent": IntentUnderstandingAgent(llm_client),
            "data": DataDiscoveryAgent(llm_client),
            "tools": ToolSelectionAgent(llm_client),
            "composition": WorkflowCompositionAgent(llm_client)
        }
    
    async def generate_workflow(
        self, 
        research_question: str,
        domain: str = "auto-detect"
    ) -> Dict[str, Any]:
        """
        Generate executable workflow from natural language.
        """
        # Step 1: Intent Understanding
        intent = await self.agents["intent"].parse(research_question)
        
        # Step 2: Parallel Data Discovery & Tool Selection
        data_task = self.agents["data"].discover(intent)
        tools_task = self.agents["tools"].select(intent)
        
        data_spec, tool_spec = await asyncio.gather(data_task, tools_task)
        
        # Step 3: Workflow Composition
        workflow = await self.agents["composition"].compose(
            intent=intent,
            data_spec=data_spec,
            tool_spec=tool_spec
        )
        
        # Validation
        validation = await self.validate_workflow(workflow)
        
        return {
            "workflow": workflow,
            "validation": validation,
            "intent": intent,
            "data_spec": data_spec,
            "tool_spec": tool_spec
        }
    
    async def validate_workflow(self, workflow: Dict) -> Dict:
        """
        Validate workflow syntax and semantics.
        """
        # Syntax validation (CWL/Nextflow parser)
        # Dependency graph validation
        # Resource requirement validation
        # Data type compatibility
        pass
```

### Intent Understanding Implementation

```python
class IntentUnderstandingAgent:
    def __init__(self, llm):
        self.llm = llm
        self.domain_ontologies = {
            "bioinformatics": load_bio_ontology(),
            "climate": load_climate_ontology(),
            "materials": load_materials_ontology()
        }
    
    async def parse(self, question: str) -> Dict:
        """
        Parse research question into structured intent.
        """
        prompt = f"""
        Parse this research question into structured components.
        
        Question: {question}
        
        Extract:
        1. Research goal (what scientific question)
        2. Data types involved
        3. Analysis methods implied
        4. Expected outputs
        5. Computational requirements
        
        Return as JSON.
        """
        
        response = await self.llm.complete(prompt)
        parsed = json.loads(response)
        
        # Enrich with ontology mappings
        parsed["edam_terms"] = self.map_to_edam(parsed)
        parsed["domain"] = self.detect_domain(parsed)
        
        return parsed
    
    def map_to_edam(self, parsed: Dict) -> List[str]:
        """Map to EDAM ontology terms."""
        # Implementation using ontology matching
        pass
```

### Data Discovery Implementation

```python
class DataDiscoveryAgent:
    def __init__(self, llm):
        self.llm = llm
        self.repositories = [
            GEORepository(),
            ZenodoRepository(),
            FigshareRepository(),
            InstitutionalCatalog()
        ]
    
    async def discover(self, intent: Dict) -> Dict:
        """
        Discover relevant datasets based on research intent.
        """
        # Generate search queries from intent
        queries = self.generate_queries(intent)
        
        # Search all repositories in parallel
        results = []
        for repo in self.repositories:
            repo_results = await repo.search(queries)
            results.extend(repo_results)
        
        # Rank by relevance
        ranked = self.rank_by_relevance(results, intent)
        
        # Select best datasets
        selected = await self.select_datasets(ranked, intent)
        
        return {
            "datasets": selected,
            "metadata": self.extract_metadata(selected),
            "quality_assessment": self.assess_quality(selected)
        }
```

### Tool Selection Implementation

```python
class ToolSelectionAgent:
    def __init__(self, llm):
        self.llm = llm
        self.tool_registry = load_tool_registry()
        self.benchmark_db = load_benchmarks()
    
    async def select(self, intent: Dict, data_spec: Dict) -> Dict:
        """
        Select appropriate tools for the workflow.
        """
        # Identify required operations
        operations = self.identify_operations(intent)
        
        # For each operation, select best tool
        selected_tools = []
        for op in operations:
            candidates = self.tool_registry.get_tools_for_operation(op)
            
            # Score candidates
            scores = []
            for tool in candidates:
                score = self.score_tool(tool, intent, data_spec)
                scores.append((tool, score))
            
            # Select highest scoring
            best_tool = max(scores, key=lambda x: x[1])[0]
            selected_tools.append(best_tool)
        
        return {"tools": selected_tools}
    
    def score_tool(self, tool: Dict, intent: Dict, data_spec: Dict) -> float:
        """
        Score tool based on multiple criteria.
        """
        scores = {
            "domain_match": self.domain_score(tool, intent),
            "performance": self.performance_score(tool, data_spec),
            "compatibility": self.compatibility_score(tool, data_spec),
            "community": self.community_score(tool),
            "maintenance": self.maintenance_score(tool)
        }
        
        # Weighted sum
        weights = {
            "domain_match": 0.3,
            "performance": 0.25,
            "compatibility": 0.25,
            "community": 0.1,
            "maintenance": 0.1
        }
        
        return sum(scores[k] * weights[k] for k in scores)
```

## Evaluation Results

### Accuracy Metrics

| Domain | Intent Parsing | Data Discovery | Tool Selection | Workflow Generation | Overall |
|--------|---------------|----------------|----------------|-------------------|---------|
| Bioinformatics | 92% | 85% | 89% | 91% | **89%** |
| Climate Science | 88% | 82% | 84% | 87% | **85%** |
| Materials Science | 85% | 80% | 86% | 85% | **84%** |
| **Average** | **88%** | **82%** | **86%** | **88%** | **87%** |

### Comparison with Baselines

| Approach | Accuracy | Time (min) | Domain Expertise Required |
|----------|----------|------------|---------------------------|
| Manual | 95% | 120 | High |
| Template-based | 65% | 30 | Medium |
| Single-agent LLM | 72% | 15 | Low |
| **Multi-agent (This)** | **87%** | **20** | **Low** |

## Validation Domains

1. **Bioinformatics**
   - RNA-seq differential expression
   - Variant calling pipelines
   - Metagenomic analysis

2. **Climate Modeling**
   - CMIP6 data processing
   - Downscaling workflows
   - Climate attribution studies

3. **Materials Science**
   - DFT calculation workflows
   - Molecular dynamics simulations
   - Property prediction pipelines

## Advantages

1. **87% accuracy** in workflow generation
2. **Natural language interface** - no coding required
3. **Multi-domain support** - bioinformatics, climate, materials
4. **Integration with existing engines** - CWL, Nextflow, Snakemake
5. **Reproducible** - standardized workflow outputs

## Limitations

1. **Complex workflows** (>50 steps) may require manual refinement
2. **Novel methods** may not be in tool registry
3. **Data access** requires authentication for restricted datasets
4. **Computational resources** need to be pre-configured

## Deployment Architecture

```
┌───────────────────────────────────────────────┐
│              User Interface                     │
│  (Web UI / CLI / Jupyter Extension)             │
└───────────────────────────────────────────────┘
                    ↓
┌───────────────────────────────────────────────┐
│         Workflow Orchestrator API               │
│  (FastAPI / Flask)                            │
└───────────────────────────────────────────────┘
                    ↓
┌───────────────────────────────────────────────┐
│           Multi-Agent System                    │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐        │
│  │  Intent │ │  Data   │ │  Tools  │        │
│  │  Agent  │ │  Agent  │ │  Agent  │        │
│  └─────────┘ └─────────┘ └─────────┘        │
│  ┌─────────────────────────────────┐          │
│  │      Workflow Composition       │          │
│  │           Agent                 │          │
│  └─────────────────────────────────┘          │
└───────────────────────────────────────────────┘
                    ↓
┌───────────────────────────────────────────────┐
│         External Services                       │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐        │
│  │   LLM   │ │  Data   │ │ Workflow│        │
│  │ Service │ │Catalogs │ │ Engines │        │
│  └─────────┘ └─────────┘ └─────────┘        │
└───────────────────────────────────────────────┘
```

## References

- Balis, B., Orzechowski, M., Kica, P., et al. (2026). "From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation." arXiv:2604.21910.
- Amstutz, P., et al. (2016). "Common Workflow Language, v1.0."
- Tommaso, P.D., et al. (2017). "Nextflow enables reproducible computational workflows." Nature Biotechnology.

## Tools and Integrations

- **Workflow Engines**: CWL, Nextflow, Snakemake, WDL
- **LLM APIs**: OpenAI, Anthropic, DeepSeek
- **Data Catalogs**: GEO, SRA, Zenodo, Dataverse
- **Container Registries**: Docker Hub, Biocontainers

## Example Use Case

```
User: "I want to identify differentially expressed genes between 
        wild-type and knockout mouse liver samples using RNA-seq data."

Agentic Workflow System:
1. Intent Parsing: 
   - Goal: differential expression analysis
   - Organism: Mus musculus
   - Tissue: liver
   - Comparison: wild-type vs knockout

2. Data Discovery:
   - Search GEO for relevant RNA-seq datasets
   - Identify: GSE67890 (WT vs KO, liver, n=6 per group)

3. Tool Selection:
   - QC: fastp
   - Alignment: HISAT2 (mouse reference)
   - Quantification: featureCounts
   - DE: DESeq2

4. Workflow Generation:
   - Generate Nextflow pipeline
   - Include quality control, alignment, quantification, DE analysis
   - Add visualization steps (volcano plot, heatmap)

5. Validation:
   - Syntax check: ✓
   - Dependency check: ✓
   - Resource estimation: 16GB RAM, 4 CPU cores, ~2 hours

Output: Executable Nextflow workflow with sample sheet and config
```
