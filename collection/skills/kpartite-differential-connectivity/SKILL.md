# SKILL.md - K-Partite Differential Brain Connectivity

## Activation Keywords

- k-partite graph, differential connectivity, brain network biomarker
- differentially expressed networks, connectivity analysis, disease detection
- Parkinson's disease, brain connectivity, network topology
- latent topology detection, connectivity biomarker

## What It Does

Provides an algorithm to automatically detect latent topology of differentially expressed functional connectivity networks using k-partite graph structure. Identifies network-level biomarkers that distinguish patient groups (e.g., Parkinson's disease) from healthy controls.

## When To Use

**Use this skill when:**
- Identifying disease-related connectivity differences
- Finding network biomarkers for patient classification
- Analyzing group differences in brain connectivity
- Detecting differential functional connectivity
- Applying k-partite graph topology to brain networks

**Do NOT use for:**
- Single-subject connectivity analysis
- Structural connectivity only (no functional)
- Classification without network topology analysis

## How To Use

### Step-by-Step Workflow

1. **Collect fMRI Data**
   - Patient group (e.g., Parkinson's disease)
   - Healthy control group
   - Preprocess and extract time series

2. **Compute Functional Connectivity**
   - Correlation between brain regions
   - Create connectivity matrices for each subject
   - Fisher z-transform for statistical analysis

3. **Identify Differential Connections**
   - Statistical test (t-test, permutation) between groups
   - Select significant connections (p < threshold)
   - Build differential connectivity set

4. **Construct K-Partite Graph**
   - Define k partitions (e.g., functional modules)
   - Map differential connections to k-partite structure
   - Each partition = set of nodes

5. **Detect Latent Topology**
   - Apply topology detection algorithm
   - Identify connected components across partitions
   - Extract differentially expressed network biomarker

### K-Partite Graph Definition

A k-partite graph:
- Nodes divided into k disjoint sets (partitions)
- Edges only between different partitions
- No edges within same partition

**For brain networks:**
- Partitions = functional modules (DMN, FPN, etc.)
- Edges = differential connections
- Reveals cross-module connectivity changes

### Key Parameters

| Parameter | Purpose | Typical Value |
|-----------|---------|---------------|
| Statistical threshold | Significance level | p < 0.05 (FDR corrected) |
| K (partitions) | Number of modules | 5-10 brain networks |
| Min component size | Biomarker threshold | 3-5 nodes |

## Example Usage

### Detecting Parkinson's Disease Biomarkers

**Problem:** Find connectivity biomarker distinguishing PD patients

**Pipeline:**
```python
import numpy as np
from scipy import stats
import networkx as nx

class KPartiteDifferentialConnectivity:
    def __init__(self, n_partitions, p_threshold=0.05):
        self.n_partitions = n_partitions
        self.p_threshold = p_threshold
    
    def compute_differential_connectivity(self, patient_fcs, control_fcs):
        """
        Identify differentially expressed connections
        
        Parameters:
        -----------
        patient_fcs : array (n_patients, n_regions, n_regions)
            Functional connectivity matrices for patients
        control_fcs : array (n_controls, n_regions, n_regions)
            Functional connectivity matrices for controls
            
        Returns:
        --------
        diff_edges : list of tuples
            Significant differential connections
        p_values : array
            Statistical p-values
        """
        n_regions = patient_fcs.shape[1]
        
        # T-test for each connection
        p_values = np.ones((n_regions, n_regions))
        t_stats = np.zeros((n_regions, n_regions))
        
        for i in range(n_regions):
            for j in range(i+1, n_regions):
                patient_conn = patient_fcs[:, i, j]
                control_conn = control_fcs[:, i, j]
                
                t, p = stats.ttest_ind(patient_conn, control_conn)
                t_stats[i, j] = t
                p_values[i, j] = p
                p_values[j, i] = p
        
        # FDR correction
        from statsmodels.stats.multitest import fdrcorrection
        _, p_corrected = fdrcorrection(p_values.flatten())
        p_corrected = p_corrected.reshape(n_regions, n_regions)
        
        # Extract significant connections
        diff_edges = []
        for i in range(n_regions):
            for j in range(i+1, n_regions):
                if p_corrected[i, j] < self.p_threshold:
                    diff_edges.append((i, j, t_stats[i, j]))
        
        return diff_edges, p_corrected
    
    def build_k_partite_graph(self, diff_edges, partition_assignments):
        """
        Build k-partite graph from differential edges
        
        Parameters:
        -----------
        diff_edges : list
            Differential connections
        partition_assignments : array (n_regions,)
            Partition index for each region
        """
        G = nx.Graph()
        
        # Add nodes with partition attribute
        for node, partition in enumerate(partition_assignments):
            G.add_node(node, partition=partition)
        
        # Add edges (only between different partitions)
        for i, j, weight in diff_edges:
            if partition_assignments[i] != partition_assignments[j]:
                G.add_edge(i, j, weight=weight)
        
        return G
    
    def detect_biomarker(self, G, min_size=3):
        """
        Detect connected components as biomarkers
        """
        # Find connected components
        components = list(nx.connected_components(G))
        
        # Filter by size
        biomarkers = [c for c in components if len(c) >= min_size]
        
        # Extract biomarker network
        biomarker_networks = []
        for biomarker in biomarkers:
            subgraph = G.subgraph(biomarker)
            biomarker_networks.append({
                'nodes': list(biomarker),
                'edges': list(subgraph.edges()),
                'size': len(biomarker)
            })
        
        return biomarker_networks
```

### Application to Parkinson's Disease

**Analysis:**
```python
# Load data
patient_fcs = load_patient_fcs()  # (24, 200, 200)
control_fcs = load_control_fcs()  # (18, 200, 200)

# Define partitions (brain networks)
partitions = define_brain_networks()  # Yeo 7 networks

# Initialize detector
detector = KPartiteDifferentialConnectivity(n_partitions=7)

# Find differential connections
diff_edges, p_values = detector.compute_differential_connectivity(
    patient_fcs, control_fcs
)

# Build k-partite graph
G_kpartite = detector.build_k_partite_graph(diff_edges, partitions)

# Detect biomarkers
biomarkers = detector.detect_biomarker(G_kpartite)

print(f"Found {len(biomarkers)} connectivity biomarkers")
for i, bm in enumerate(biomarkers):
    print(f"Biomarker {i+1}: {bm['size']} nodes, {len(bm['edges'])} edges")
```

**Output:** Connectivity biomarker distinguishing PD from healthy controls

## Key Advantages

| Advantage | Benefit |
|-----------|---------|
| Latent topology | Reveals hidden network structure |
| K-partite constraint | Focuses on cross-module changes |
| Biomarker detection | Disease-specific signatures |
| Statistical rigor | Multiple comparison correction |

## Description

SKILL.md - K-Partite Differential Brain Connectivity

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Collect fMRI Data

### Step 2: Compute Functional Connectivity

### Step 3: Identify Differential Connections

### Step 4: Construct K-Partite Graph

### Step 5: Detect Latent Topology

## Examples

### Example 1: Basic Application

**User:** I need to apply SKILL.md - K-Partite Differential Brain Connectivity to my analysis.

**Agent:** I'll help you apply kpartite-differential-connectivity. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for kpartite-differential-connectivity?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **brain-network-joint-embedding** - Network comparison
- **task-aware-brain-connectivity** - Task-based connectivity
- **weighted-brain-community-detection** - Community detection

## Source

- arXiv:1603.07211v1
- Title: Differentially Expressed Functional Connectivity Networks with K-partite Graph Topology
- Utility: 0.87
- Authors: (from arxiv)
- Published: Statistical Methods in Medical Research

## Notes

- Key innovation: K-partite topology for differential connectivity
- Applied to Parkinson's disease biomarker detection
- Reveals cross-module connectivity changes
- Published in Statistical Methods in Medical Research
- Applications: disease diagnosis, patient classification
- Combines statistical testing with graph topology

---

_Created: 2026-04-01_