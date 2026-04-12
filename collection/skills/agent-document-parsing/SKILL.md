---
name: agent-document-parsing
description: "Agent-centric document parsing framework for semantic correctness in AI systems. Focuses on structure preservation, table extraction, chart data recovery, visual grounding, and formatting semantics for autonomous decision-making. Use for: document parsing for agents, semantic document extraction, enterprise automation parsing, chart/table extraction, PDF parsing for AI. Activation: agent document parsing, semantic document parsing, ParseBench, enterprise document extraction."
---

# Agent Document Parsing

Framework for semantic document parsing optimized for AI agents and autonomous systems, implementing the ParseBench benchmark methodology for enterprise automation.

## Problem Statement

Traditional document parsing focuses on text extraction and formatting recovery. However, AI agents require **semantic correctness**:

- **Structure preservation**: Tables, lists, hierarchies must be semantically meaningful
- **Chart data recovery**: Precise extraction of numerical values from visualizations
- **Visual grounding**: Elements must be traceable to source locations
- **Formatting semantics**: Formatting carries meaning (bold = important, strike = deleted)

Existing benchmarks fail to capture agent-critical failures:
- Narrow document distributions (academic papers only)
- Text-similarity metrics miss structural errors
- No evaluation of agent decision-making downstream

## ParseBench Framework

### Semantic Correctness Evaluation

**Four critical dimensions:**

1. **Table Structure**: Correct row/column relationships, not just cell text
2. **Chart Data**: Accurate numerical values, not just visual description
3. **Visual Grounding**: Source coordinates for each extracted element
4. **Formatting Semantics**: Semantic interpretation of visual styles

### Benchmark Categories

| Category | Agent Task | Semantic Requirement |
|----------|------------|---------------------|
| Financial Reports | Extract earnings data | Table structure + numerical precision |
| Legal Documents | Identify obligations | Formatting semantics + hierarchy |
| Technical Manuals | Execute procedures | List ordering + step identification |
| Marketing Materials | Extract claims | Visual grounding + attribution |

## Implementation

### Semantic Parser Architecture

```python
import pdfplumber
from PIL import Image
import numpy as np
from typing import List, Dict, Tuple, Optional

class SemanticDocumentParser:
    """
    Agent-centric document parser with semantic correctness focus.
    
    Implements ParseBench methodology for enterprise automation.
    """
    
    def __init__(self, document_path: str):
        self.doc = pdfplumber.open(document_path)
        self.pages = self.doc.pages
        self.grounding_map = {}  # element_id -> (page, bbox)
        
    def parse_for_agent(self) -> Dict:
        """
        Parse document with agent-semantic focus.
        
        Returns:
            semantic_doc: Structured document with grounding
        """
        return {
            "tables": self.extract_tables_semantic(),
            "charts": self.extract_chart_data(),
            "sections": self.extract_sections_with_hierarchy(),
            "formatting": self.extract_formatting_semantics(),
            "grounding": self.grounding_map
        }
    
    def extract_tables_semantic(self) -> List[Dict]:
        """
        Extract tables with semantic structure.
        
        Key: Preserve row/column relationships, not just cell text.
        """
        tables = []
        for page in self.pages:
            for table in page.extract_tables():
                # Semantic structure
                semantic_table = {
                    "headers": self.identify_headers(table),
                    "rows": self.parse_rows_semantic(table),
                    "relationships": self.identify_row_column_relations(table),
                    "type": self.classify_table_type(table),  # data, comparison, schedule
                    "grounding": self.get_table_grounding(page, table)
                }
                tables.append(semantic_table)
        return tables
    
    def extract_chart_data(self) -> List[Dict]:
        """
        Extract chart data with numerical precision.
        
        Key: Recover actual values, not just visual descriptions.
        """
        charts = []
        for page in self.pages:
            # Convert to image for chart detection
            im = page.to_image()
            
            # Detect charts
            chart_regions = self.detect_chart_regions(im)
            
            for region in chart_regions:
                chart_data = {
                    "type": self.classify_chart_type(region),  # bar, line, pie, scatter
                    "values": self.extract_numerical_values(region),
                    "axes": self.extract_axis_labels(region),
                    "legend": self.extract_legend(region),
                    "grounding": self.get_chart_grounding(page, region)
                }
                charts.append(chart_data)
        return charts
    
    def extract_formatting_semantics(self) -> Dict:
        """
        Extract formatting with semantic interpretation.
        
        Key: Formatting carries meaning for agents.
        """
        formatting = {}
        for page in self.pages:
            for char in page.chars:
                style = self.get_char_style(char)
                semantic = self.interpret_formatting_semantic(style)
                
                # Group by semantic meaning
                if semantic not in formatting:
                    formatting[semantic] = []
                formatting[semantic].append({
                    "text": char["text"],
                    "grounding": (page.page_number, char["x0"], char["top"])
                })
        
        return {
            "important": formatting.get("important", []),  # bold, larger
            "deleted": formatting.get("deleted", []),  # strikethrough
            "emphasis": formatting.get("emphasis", []),  # italic, underline
            "heading": formatting.get("heading", [])  # distinct size/style
        }
    
    def interpret_formatting_semantic(self, style: Dict) -> str:
        """Map visual formatting to semantic meaning."""
        if style.get("bold"):
            return "important"
        if style.get("strikethrough"):
            return "deleted"
        if style.get("italic") or style.get("underline"):
            return "emphasis"
        if style.get("size", 12) > 14:
            return "heading"
        return "normal"
    
    def get_grounding(self, element: Dict, page) -> Dict:
        """Get source location for extracted element."""
        return {
            "page": page.page_number,
            "bbox": (element["x0"], element["top"], element["x1"], element["bottom"])
        }
```

### Agent Decision Integration

```python
class AgentDocumentInterface:
    """
    Interface for agents to query parsed documents.
    
    Focuses on agent-critical extraction patterns.
    """
    
    def __init__(self, semantic_doc: Dict):
        self.doc = semantic_doc
        
    def find_obligations(self) -> List[Dict]:
        """Find legally binding obligations in documents."""
        # Use formatting semantics + visual grounding
        obligations = []
        
        for item in self.doc["formatting"]["important"]:
            if self.is_obligation_text(item["text"]):
                obligations.append({
                    "text": item["text"],
                    "location": item["grounding"],
                    "confidence": self.compute_confidence(item)
                })
        
        return obligations
    
    def extract_financial_values(self) -> Dict:
        """Extract financial data with numerical precision."""
        # Use table structure + chart data
        values = {}
        
        for table in self.doc["tables"]:
            if table["type"] == "financial":
                values.update(self.parse_financial_table(table))
        
        for chart in self.doc["charts"]:
            if chart["type"] in ["bar", "line"]:
                values.update(chart["values"])
        
        return values
    
    def trace_source(self, element_id: str) -> Tuple:
        """Trace extracted element back to source location."""
        return self.doc["grounding"].get(element_id)
```

## Use Cases

### 1. Financial Report Analysis

```python
parser = SemanticDocumentParser("quarterly_report.pdf")
semantic_doc = parser.parse_for_agent()

interface = AgentDocumentInterface(semantic_doc)

# Extract earnings with grounding
earnings = interface.extract_financial_values()
# {"revenue": {"value": 123.4, "unit": "M", "source": (page=5, bbox=...)}}

# Trace to original location
source = interface.trace_source("revenue")
# Navigate to exact position in PDF
```

### 2. Legal Document Processing

```python
parser = SemanticDocumentParser("contract.pdf")
semantic_doc = parser.parse_for_agent()

interface = AgentDocumentInterface(semantic_doc)

# Find obligations
obligations = interface.find_obligations()
# [{"text": "Party A shall deliver...", "location": (page=3, bbox=...)}]

# Check deleted clauses (strikethrough)
deleted = semantic_doc["formatting"]["deleted"]
# Review changes/amendments
```

### 3. Technical Manual Execution

```python
parser = SemanticDocumentParser("manual.pdf")
semantic_doc = parser.parse_for_agent()

# Extract procedure steps with ordering
steps = []
for section in semantic_doc["sections"]:
    if section["type"] == "procedure":
        steps.extend(section["ordered_items"])

# Execute with grounding for verification
for step in steps:
    result = execute_step(step["text"])
    source = interface.trace_source(step["id"])
    log_result(result, source)
```

## Evaluation Metrics

### Semantic Correctness Score

| Metric | Description | Weight |
|--------|-------------|--------|
| Table Structure | Row/column accuracy | 0.25 |
| Chart Data | Numerical precision | 0.25 |
| Visual Grounding | Location accuracy | 0.20 |
| Formatting Semantics | Semantic interpretation | 0.20 |
| Agent Task Success | Downstream decision accuracy | 0.10 |

### ParseBench Benchmarks

```python
def evaluate_parser(parser, documents, agent_tasks):
    """Evaluate parser on ParseBench methodology."""
    scores = []
    
    for doc, task in zip(documents, agent_tasks):
        semantic_doc = parser.parse_for_agent(doc)
        
        # Semantic correctness
        sc_score = compute_semantic_correctness(semantic_doc)
        
        # Agent task success
        task_result = execute_agent_task(semantic_doc, task)
        task_score = compute_task_success(task_result)
        
        scores.append(0.9 * sc_score + 0.1 * task_score)
    
    return np.mean(scores)
```

## Tools Used

- `pdfplumber`: PDF parsing with structure
- `PIL`: Image processing for chart detection
- `numpy`: Numerical operations
- `exec`: Run parsing scripts
- `write`: Save parsed documents
- `read`: Load document configurations

## References

- Zhang, B., et al. (2026). ParseBench: A Document Parsing Benchmark for AI Agents. arXiv:2604.08538.

## Activation Keywords

- agent document parsing
- semantic document parsing
- ParseBench
- enterprise document extraction
- chart data extraction
- table structure extraction
- visual grounding
- formatting semantics

## Related Skills

- **meta-cognitive-tool-optimization**: For deciding when to use document parsing
- **claude-code**: For implementing parsing scripts
- **skill-extractor**: For extracting patterns from documents

## Description

This skill provides specialized capabilities for its domain.

## Instructions for Agents

When this skill is activated:

1. Identify the user's specific need
2. Apply the specialized knowledge
3. Provide clear guidance

## Examples

```
User: How do I use this skill?
Agent: I'll help you with this skill...
```