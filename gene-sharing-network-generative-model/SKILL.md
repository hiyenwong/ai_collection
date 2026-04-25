---
name: gene-sharing-network-generative-model
description: "Generative model for bipartite gene-sharing networks explaining evolutionary patterns in viruses and mobile genetic elements. Captures scale-free gene degree and exponential genome degree distributions via horizontal gene transfer, gene capture, and loss processes. Activation: gene-sharing network, bipartite network evolution, viral genome evolution, pangenome modeling, horizontal gene transfer."
---

# Gene-Sharing Network Generative Model

Mechanistic generative model for bipartite gene-sharing networks linking genes to genomes, explaining characteristic degree distributions in viral and prokaryotic pangenomes.

## Paper Information

- **Title:** A generative model for bipartite gene-sharing networks
- **Authors:** Jaime Iranzo, Pedro Jódar, Francisco Rodrigues, Mario A. Fuentes, Susanna Manrubia
- **arXiv ID:** 2604.13963v1
- **Date:** April 15, 2026
- **Category:** q-bio.PE, physics.bio-ph
- **PDF:** https://arxiv.org/pdf/2604.13963v1

## Problem Statement

**Gene-sharing networks** link genes to the genomes containing them, exhibiting characteristic patterns:
- **Scale-free gene degree**: Few genes appear in many genomes (hubs)
- **Exponential genome degree**: Genomes contain gene counts with exponential-like decay
- **Evolutionary drivers**: Horizontal gene transfer, gene capture, genome emergence, gene loss

Traditional models fail to capture both distributions simultaneously.

## Core Model

### Evolutionary Processes

```
┌────────────────────────────────────────────────────────────────┐
│                    Gene-Sharing Network Model                   │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   GENES ────────┐          ┌────────── GENOMES                │
│                 │          │                                  │
│   ┌───┐         │          │         ┌───┐                   │
│   │g_1│─────────┼──────────┼─────────│G_1│                   │
│   └───┘         │          │         └───┘                   │
│                 │          │                                  │
│   ┌───┐         │          │         ┌───┐                   │
│   │g_2│─────────┼──────────┼─────────│G_2│                   │
│   └───┘         │          │         └───┘                   │
│                 │          │                                  │
│   ┌───┐         │          │         ┌───┐                   │
│   │g_3│─────────┼──────────┼─────────│G_3│                   │
│   └───┘         │          │         └───┘                   │
│                 │          │                                  │
│   ...           │          │          ...                     │
│                 │          │                                  │
└─────────────────┴──────────┴──────────────────────────────────┘

Evolutionary Dynamics:
━━━━━━━━━━━━━━━━━━━━
1. New genome emerges (empty)
2. Horizontal gene transfer (existing genes to new genome)
3. Capture of new genes (genome acquires novel genes)
4. Gene loss (genes removed from genomes)
```

### Model Parameters

Only **two parameters** govern the entire dynamics:

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Gene gain rate | λ | Rate of horizontal transfer + new gene capture |
| Gene loss rate | μ | Rate of gene removal from genomes |

**Ratio**: γ = λ/μ (relative gain-to-loss rate)

## Mathematical Framework

### Mean-Field Approximation

The model uses mean-field theory to derive analytical expressions:

**Gene Degree Distribution** (number of genomes containing a gene):
```
P(k_gene) ~ k_gene^(-α)  (power-law, scale-free)
where α depends on γ
```

**Genome Degree Distribution** (number of genes in a genome):
```
P(k_genome) ~ exp(-k_genome / k_0)  (exponential decay)
where k_0 depends on γ
```

### Analytical Solutions

```python
def gene_degree_distribution(k, gamma):
    """
    Asymptotic gene degree distribution (scale-free).
    
    Args:
        k: Gene degree (number of genomes containing the gene)
        gamma: λ/μ ratio (gain-to-loss rate)
    
    Returns:
        Probability density for degree k
    """
    alpha = 1 + 1/gamma  # Power-law exponent
    normalization = zeta(alpha)  # Riemann zeta function
    
    return k**(-alpha) / normalization

def genome_degree_distribution(k, gamma, N_genes):
    """
    Asymptotic genome degree distribution (exponential).
    
    Args:
        k: Genome degree (number of genes in genome)
        gamma: λ/μ ratio
        N_genes: Total number of genes in network
    
    Returns:
        Probability density for degree k
    """
    k_0 = gamma * N_genes / (1 + gamma)
    
    return (1/k_0) * np.exp(-k / k_0)
```

## Implementation

### Simulation Algorithm

```python
import numpy as np
import networkx as nx

class GeneSharingNetwork:
    """
    Bipartite gene-sharing network with evolutionary dynamics.
    """
    def __init__(self, lambda_gain=0.1, mu_loss=0.01):
        """
        Initialize gene-sharing network.
        
        Args:
            lambda_gain: Rate of gene gain (horizontal transfer + new capture)
            mu_loss: Rate of gene loss
        """
        self.lambda_gain = lambda_gain
        self.mu_loss = mu_loss
        self.gamma = lambda_gain / mu_loss
        
        # Bipartite graph: genes (0) and genomes (1)
        self.network = nx.Graph()
        self.genes = set()
        self.genomes = set()
        
        # Gene and genome counters
        self.next_gene_id = 0
        self.next_genome_id = 0
    
    def add_genome(self):
        """
        Add new genome to network (genome emergence event).
        """
        genome_id = f"G_{self.next_genome_id}"
        self.next_genome_id += 1
        self.genomes.add(genome_id)
        self.network.add_node(genome_id, bipartite=1)
        return genome_id
    
    def capture_gene(self, genome_id, existing=False):
        """
        Capture gene: either existing gene (horizontal transfer) 
        or new gene (gene innovation).
        
        Args:
            genome_id: Target genome
            existing: If True, transfer existing gene; else create new gene
        """
        if existing and len(self.genes) > 0:
            # Horizontal gene transfer: choose existing gene
            # Prefer hub genes (scale-free property)
            gene_probs = [self.network.degree(g) + 1 for g in self.genes]
            gene_probs = np.array(gene_probs) / sum(gene_probs)
            gene_id = np.random.choice(list(self.genes), p=gene_probs)
        else:
            # Capture new gene
            gene_id = f"g_{self.next_gene_id}"
            self.next_gene_id += 1
            self.genes.add(gene_id)
            self.network.add_node(gene_id, bipartite=0)
        
        # Add edge between gene and genome
        self.network.add_edge(gene_id, genome_id)
        return gene_id
    
    def lose_gene(self, genome_id):
        """
        Gene loss event: remove random gene from genome.
        
        Args:
            genome_id: Genome losing a gene
        """
        neighbors = list(self.network.neighbors(genome_id))
        if len(neighbors) > 0:
            gene_to_remove = np.random.choice(neighbors)
            self.network.remove_edge(gene_to_remove, genome_id)
    
    def evolve(self, n_steps=10000, n_initial_genomes=10):
        """
        Simulate network evolution.
        
        Args:
            n_steps: Number of evolutionary steps
            n_initial_genomes: Initial number of genomes
        """
        # Initialize with empty genomes
        for _ in range(n_initial_genomes):
            self.add_genome()
        
        # Evolution loop
        for step in range(n_steps):
            # Random event selection
            r = np.random.random()
            
            # New genome emergence
            if r < 0.1:
                new_genome = self.add_genome()
                # New genome captures some genes immediately
                n_initial_genes = np.random.poisson(self.lambda_gain * 10)
                for _ in range(n_initial_genes):
                    self.capture_gene(new_genome, existing=True)
            
            # Gene gain (horizontal transfer or new capture)
            elif r < 0.1 + self.lambda_gain:
                genome = np.random.choice(list(self.genomes))
                existing = np.random.random() < 0.7  # 70% HGT, 30% new gene
                self.capture_gene(genome, existing=existing)
            
            # Gene loss
            elif r < 0.1 + self.lambda_gain + self.mu_loss:
                genome = np.random.choice(list(self.genomes))
                self.lose_gene(genome)
            
            # Otherwise: nothing happens (drift)
    
    def get_degree_distributions(self):
        """
        Compute gene and genome degree distributions.
        
        Returns:
            gene_degrees: List of gene degrees
            genome_degrees: List of genome degrees
        """
        gene_degrees = [self.network.degree(g) for g in self.genes]
        genome_degrees = [self.network.degree(g) for g in self.genomes]
        
        return gene_degrees, genome_degrees
```

### Fitting to Empirical Data

```python
def fit_model_to_data(observed_gene_degrees, observed_genome_degrees):
    """
    Fit model parameters to empirical degree distributions.
    
    Args:
        observed_gene_degrees: List of observed gene degrees
        observed_genome_degrees: List of observed genome degrees
    
    Returns:
        lambda_gain, mu_loss: Estimated parameters
    """
    from scipy.optimize import minimize
    
    def loss(params):
        lambda_gain, mu_loss = params
        
        # Simulate with these parameters
        model = GeneSharingNetwork(lambda_gain, mu_loss)
        model.evolve(n_steps=50000)
        
        sim_gene, sim_genome = model.get_degree_distributions()
        
        # Compute KL divergence or similar metric
        gene_kl = compute_kl_divergence(observed_gene_degrees, sim_gene)
        genome_kl = compute_kl_divergence(observed_genome_degrees, sim_genome)
        
        return gene_kl + genome_kl
    
    # Optimize parameters
    result = minimize(loss, x0=[0.1, 0.01], 
                     bounds=[(0.001, 1.0), (0.0001, 0.1)])
    
    return result.x
```

## Validation Results

### Empirical Data Fit

The model closely fits data from:

| Dataset | Type | Gene Loss Rate | Key Finding |
|---------|------|----------------|-------------|
| dsDNA viruses | Viral | μ ≈ 0 | Gene gain dominates |
| RNA viruses | Viral | μ ≈ 0 | Gene gain dominates |
| Prokaryotic pangenomes | Bacterial | μ > 0 | Balance of gain/loss |

### Key Findings

1. **Viral evolution is dominated by gene gain** (μ ≈ 0)
   - Viruses continuously acquire new genes
   - Minimal gene loss relative to gain
   - Creates highly connected gene hubs

2. **Genome plasticity emerges naturally**
   - Scale-free gene distribution: few genes in many genomes
   - Exponential genome distribution: genomes have characteristic size

3. **Only two parameters needed**
   - Model complexity is minimal yet predictive
   - Parameters interpretable as evolutionary rates

## Applications

### Viral Evolution Studies
- **Pandemic tracking**: Model gene flow between viral strains
- **Drug resistance**: Track resistance gene spread
- **Vaccine design**: Identify conserved vs variable genes

### Pangenome Analysis
- **Core vs accessory genome**: Distinguish essential vs flexible genes
- **Open vs closed pangenomes**: Classify pangenome types
- **Evolutionary dynamics**: Predict future gene content changes

### Horizontal Gene Transfer
- **HGT quantification**: Estimate transfer rates from network structure
- **Transfer hot spots**: Identify highly mobile genes
- **Ecological networks**: Model gene sharing in microbial communities

## Extensions

### Time-Dependent Rates
```python
class DynamicGeneSharingNetwork(GeneSharingNetwork):
    """
    Extension with time-varying evolutionary rates.
    """
    def __init__(self):
        super().__init__()
        self.lambda_history = []
        self.mu_history = []
    
    def update_rates(self, t):
        """
        Update rates based on evolutionary time.
        """
        # Example: rates increase during adaptation events
        self.lambda_gain = base_lambda * (1 + 0.5 * np.sin(t / 1000))
        self.mu_loss = base_mu * (1 + 0.3 * np.cos(t / 1000))
```

### Fitness-Dependent Dynamics
```python
class FitnessAwareGeneSharingNetwork(GeneSharingNetwork):
    """
    Extension where gene fitness affects retention.
    """
    def __init__(self):
        super().__init__()
        self.gene_fitness = {}
    
    def capture_gene(self, genome_id, existing=False):
        gene_id = super().capture_gene(genome_id, existing)
        
        if not existing:
            # New genes have random fitness
            self.gene_fitness[gene_id] = np.random.exponential(1.0)
        
        return gene_id
    
    def lose_gene(self, genome_id):
        """
        Preferentially lose low-fitness genes.
        """
        neighbors = list(self.network.neighbors(genome_id))
        if len(neighbors) == 0:
            return
        
        # Weight by inverse fitness
        weights = [1.0 / (self.gene_fitness.get(g, 1.0) + 0.1) 
                  for g in neighbors]
        weights = np.array(weights) / sum(weights)
        
        gene_to_remove = np.random.choice(neighbors, p=weights)
        self.network.remove_edge(gene_to_remove, genome_id)
```

## Activation Keywords

- gene-sharing network
- bipartite network evolution
- viral genome evolution
- pangenome modeling
- horizontal gene transfer
- gene degree distribution
- genome degree distribution
- evolutionary network model
- mean-field approximation
- scale-free gene network
- gene gain loss model
- 基因共享网络
- 病毒基因组进化
- 泛基因组建模
- 水平基因转移
- network evolution biology

## Related Work

- **Pangenome graphs**: Sequence-based pangenome representations
- **Gene family evolution**: Tree-based models of gene duplication/loss
- **Horizontal transfer networks**: Network analysis of HGT patterns
- **Viral phylogenomics**: Evolutionary reconstructions of viral genomes

## References

- Iranzo, J., et al. (2026). A generative model for bipartite gene-sharing networks. *arXiv preprint* arXiv:2604.13963v1.
- Tettelin, H., et al. (2005). Genome analysis of multiple pathogenic isolates of Streptococcus agalactiae. *PNAS*.
- Baillie, C., et al. (2022). Pangenome evolution. *Nature Reviews Genetics*.

## Limitations

- Mean-field approximation may miss finite-size effects
- Assumes constant rates (extensions needed for dynamic rates)
- Does not capture spatial/ecological structure
- Gene functionality not explicitly modeled

## Future Directions

1. **Multi-species networks**: Gene sharing across species boundaries
2. **Functional annotations**: Incorporate gene function into model
3. **Ecological networks**: Spatial structure and community dynamics
4. **Temporal evolution**: Time-series fitting to track rate changes
