     1|---
     2|name: irene-eeg-seizure-detection
     3|version: v1.0.0
     4|last_updated: 2026-04-18
     5|description: "Information Bottleneck-guided EEG Seizure Detection (IRENE). Jointly learns denoised dynamic graph structures and informative spatial-temporal representations for EEG seizure detection. Addresses noisy EEG graphs, redundant connections, and inter-patient variability using IB principle and self-supervised Graph Masked AutoEncoder. Accepted at IEEE ICHI 2026."
     6|category: neuroscience
     7|tags:
     8|  - eeg
     9|  - seizure-detection
    10|  - information-bottleneck
    11|  - dynamic-graph
    12|  - self-supervised-learning
    13|  - graph-masked-autoencoder
    14|  - spatiotemporal-representation
    15|paper:
    16|  title: "Optimizing EEG Graph Structure for Seizure Detection: An Information Bottleneck and Self-Supervised Learning Approach"
    17|  authors: "Lincan Li, Rikuto Kotoge, Xihao Piao, Zheng Chen, Yushun Dong"
    18|  arxiv: "2604.01595v1"
    19|  published: "2026-04-02"
    20|  url: "https://arxiv.org/abs/2604.01595"
    21|  accepted: "IEEE ICHI 2026"
    22|activation: "eeg seizure detection, information bottleneck EEG, dynamic graph EEG, IRENE, graph masked autoencoder EEG, seizure propagation, inter-patient variability EEG"
    23|---
    24|
    25|# IRENE: Information Bottleneck-guided EEG Seizure Detection
    26|
    27|## 概述
    28|
    29|IRENE (Information Bottleneck-guided EEG SeizuRE DetectioN via SElf-Supervised Learning) 是一种新的 EEG 癫痫检测框架，通过信息瓶颈 (IB) 原则联合学习去噪的动态图结构和信息丰富的时空表示。解决了 EEG 图结构中的噪声、冗余连接和患者间变异性问题。已被 IEEE ICHI 2026 接受。
    30|
    31|## 来源论文
    32|
    33|- **标题**: Optimizing EEG Graph Structure for Seizure Detection: An Information Bottleneck and Self-Supervised Learning Approach
    34|- **作者**: Lincan Li, Rikuto Kotoge, Xihao Piao, Zheng Chen, Yushun Dong
    35|- **arXiv**: 2604.01595v1
    36|- **发表**: 2026-04-02
    37|- **录用**: IEEE 14th International Conference on Healthcare Informatics (ICHI)
    38|- **代码**: https://github.com/LabRAI/IRENE
    39|- **PDF**: https://arxiv.org/pdf/2604.01595v1
    40|
    41|## 核心问题
    42|
    43|EEG 癫痫检测的三大挑战：
    44|1. **噪声图结构**: 基于统计相关性或隐式学习的动态图包含冗余和任务无关连接
    45|2. **癫痫传播解释**: 难以解释癫痫在大脑网络中的传播路径
    46|3. **标签稀缺与患者间变异**: 标注数据有限且不同患者的 EEG 模式差异巨大
    47|
    48|## 核心方法
    49|
    50|### Information Bottleneck (IB) 原理
    51|
    52|IB 原则：在压缩输入信息的同时，最大化对目标任务的预测能力。
    53|
    54|```
    55|min I(X; Z) - β·I(Z; Y)
    56|
    57|其中:
    58|- X: 原始 EEG 输入
    59|- Z: 学到的表示
    60|- Y: 癫痫标签
    61|- β: 权衡参数
    62|```
    63|
    64|IRENE 将此应用于 EEG 图结构学习：学习紧凑、可靠的连接模式，同时保留癫痫检测所需的关键信息。
    65|
    66|### 架构组件
    67|
    68|```
    69|EEG Signals
    70|    ↓
    71|┌─────────────────────────────────────┐
    72|│  Dynamic Graph Constructor (IB)     │
    73|│  - Accounts for EEG noise           │
    74|│  - Produces compact connectivity    │
    75|└─────────────────────────────────────┘
    76|    ↓
    77|┌─────────────────────────────────────┐
    78|│  Graph Masked AutoEncoder (GMAE)    │
    79|│  - Self-supervised pretraining       │
    80|│  - Reconstructs masked EEG signals  │
    81|│  - Structure-aware representations   │
    82|└─────────────────────────────────────┘
    83|    ↓
    84|┌─────────────────────────────────────┐
    85|│  Spatiotemporal Encoder              │
    86|│  - Captures temporal dynamics        │
    87|│  - Spatial propagation patterns      │
    88|└─────────────────────────────────────┘
    89|    ↓
    90|Seizure Detection + Explanation
    91|```
    92|
    93|### 关键实现
    94|
    95|```python
    96|import torch
    97|import torch.nn as nn
    98|import torch.nn.functional as F
    99|
   100|class IRENE(nn.Module):
   101|    """Information Bottleneck-guided EEG Seizure Detection."""
   102|    
   103|    def __init__(self, n_channels, n_samples, hidden_dim=128, beta=0.1):
   104|        super().__init__()
   105|        self.n_channels = n_channels
   106|        self.n_samples = n_samples
   107|        self.beta = beta
   108|        
   109|        # IB-guided graph constructor
   110|        self.graph_constructor = IBGraphConstructor(
   111|            n_channels, hidden_dim, beta=beta
   112|        )
   113|        
   114|        # Graph Masked AutoEncoder
   115|        self.gmae = GraphMaskedAutoEncoder(
   116|            n_channels, hidden_dim
   117|        )
   118|        
   119|        # Spatiotemporal encoder
   120|        self.st_encoder = SpatiotemporalEncoder(
   121|            hidden_dim, n_classes=2
   122|        )
   123|    
   124|    def forward(self, x, mask_ratio=0.3):
   125|        """
   126|        Forward pass with IB-guided graph learning and GMAE.
   127|        
   128|        Args:
   129|            x: EEG signals (batch, n_channels, n_samples)
   130|            mask_ratio: Fraction of channels to mask for GMAE
   131|        """
   132|        # Step 1: Learn IB-optimized dynamic graph
   133|        adj, ib_loss = self.graph_constructor(x)
   134|        
   135|        # Step 2: Self-supervised GMAE pretraining
   136|        x_masked, mask = self._mask_channels(x, mask_ratio)
   137|        reconstructed = self.gmae(x_masked, adj)
   138|        recon_loss = self._reconstruction_loss(reconstructed, x, mask)
   139|        
   140|        # Step 3: Spatiotemporal encoding for seizure detection
   141|        features = self.gmae.encode(x, adj)
   142|        seizure_pred = self.st_encoder(features, adj)
   143|        
   144|        return seizure_pred, ib_loss, recon_loss
   145|    
   146|    def _mask_channels(self, x, mask_ratio):
   147|        """Randomly mask EEG channels for self-supervised learning."""
   148|        batch_size, n_channels, n_samples = x.shape
   149|        n_mask = int(n_channels * mask_ratio)
   150|        
   151|        # Random channel selection
   152|        mask = torch.rand(batch_size, n_channels) < mask_ratio
   153|        x_masked = x.clone()
   154|        x_masked[mask] = 0  # Zero-masked channels
   155|        
   156|        return x_masked, mask
   157|
   158|
   159|class IBGraphConstructor(nn.Module):
   160|    """Information Bottleneck-guided dynamic graph constructor."""
   161|    
   162|    def __init__(self, n_channels, hidden_dim, beta=0.1):
   163|        super().__init__()
   164|        self.beta = beta
   165|        
   166|        # Learn node embeddings
   167|        self.node_embed = nn.Sequential(
   168|            nn.Linear(n_channels, hidden_dim),
   169|            nn.ReLU(),
   170|            nn.Linear(hidden_dim, hidden_dim)
   171|        )
   172|        
   173|        # Graph attention for adjacency
   174|        self.attn = nn.Sequential(
   175|            nn.Linear(hidden_dim * 2, hidden_dim),
   176|            nn.Tanh(),
   177|            nn.Linear(hidden_dim, 1)
   178|        )
   179|    
   180|    def forward(self, x):
   181|        """
   182|        Construct IB-optimized adjacency matrix.
   183|        
   184|        Args:
   185|            x: EEG signals (batch, n_channels, n_samples)
   186|        """
   187|        batch_size, n_channels, n_samples = x.shape
   188|        
   189|        # Extract node features (channel-wise statistics)
   190|        node_features = self.node_embed(x.mean(dim=-1))  # (batch, n_channels, hidden)
   191|        
   192|        # Compute pairwise attention
   193|        adj = torch.zeros(batch_size, n_channels, n_channels, device=x.device)
   194|        for i in range(n_channels):
   195|            for j in range(n_channels):
   196|                pair = torch.cat([node_features[:, i], node_features[:, j]], dim=-1)
   197|                adj[:, i, j] = self.attn(pair).squeeze(-1)
   198|        
   199|        # IB regularization: penalize overly dense graphs
   200|        ib_loss = self.beta * torch.mean(adj ** 2)
   201|        
   202|        # Normalize adjacency
   203|        adj = F.softmax(adj, dim=-1)
   204|        
   205|        return adj, ib_loss
   206|
   207|
   208|class GraphMaskedAutoEncoder(nn.Module):
   209|    """Self-supervised Graph Masked AutoEncoder for EEG."""
   210|    
   211|    def __init__(self, n_channels, hidden_dim):
   212|        super().__init__()
   213|        self.encoder = nn.Sequential(
   214|            nn.Linear(n_channels, hidden_dim),
   215|            nn.ReLU(),
   216|            nn.Linear(hidden_dim, hidden_dim)
   217|        )
   218|        
   219|        self.decoder = nn.Sequential(
   220|            nn.Linear(hidden_dim, hidden_dim),
   221|            nn.ReLU(),
   222|            nn.Linear(hidden_dim, n_channels)
   223|        )
   224|    
   225|    def encode(self, x, adj):
   226|        """Encode EEG signals with graph context."""
   227|        # x: (batch, n_channels, n_samples)
   228|        features = self.encoder(x.mean(dim=-1))  # (batch, n_channels, hidden)
   229|        
   230|        # Graph message passing
   231|        features = torch.bmm(adj, features)  # (batch, n_channels, hidden)
   232|        
   233|        return features
   234|    
   235|    def decode(self, features, adj):
   236|        """Reconstruct masked channels."""
   237|        features = torch.bmm(adj, features)
   238|        reconstructed = self.decoder(features)
   239|        return reconstructed
   240|    
   241|    def forward(self, x_masked, adj):
   242|        features = self.encode(x_masked, adj)
   243|        reconstructed = self.decode(features, adj)
   244|        return reconstructed
   245|```
   246|
   247|### 训练流程
   248|
   249|```python
   250|def train_irene(model, dataloader, n_epochs=100):
   251|    """
   252|    Train IRENE with joint supervised and self-supervised objectives.
   253|    """
   254|    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
   255|    
   256|    for epoch in range(n_epochs):
   257|        for eeg_signals, seizure_labels in dataloader:
   258|            # Forward pass
   259|            preds, ib_loss, recon_loss = model(eeg_signals)
   260|            
   261|            # Supervised loss (seizure classification)
   262|            cls_loss = F.cross_entropy(preds, seizure_labels)
   263|            
   264|            # Combined objective
   265|            loss = cls_loss + ib_loss + 0.5 * recon_loss
   266|            
   267|            loss.backward()
   268|            optimizer.step()
   269|            optimizer.zero_grad()
   270|```
   271|
   272|## 应用场景
   273|
   274|### 1. 癫痫检测
   275|```python
   276|# Detect seizures in real-time EEG
   277|model = IRENE(n_channels=21, n_samples=256)
   278|model.load_state_dict(torch.load('irene_checkpoint.pt'))
   279|model.eval()
   280|
   281|eeg_segment = load_eeg_segment()  # (1, 21, 256)
   282|with torch.no_grad():
   283|    pred, _, _ = model(eeg_segment)
   284|    seizure_prob = F.softmax(pred, dim=1)[0, 1]
   285|    is_seizure = seizure_prob > 0.5
   286|```
   287|
   288|### 2. 癫痫传播解释
   289|```python
   290|# Analyze seizure propagation patterns
   291|adj, _ = model.graph_constructor(eeg_segment)
   292|
   293|# Visualize learned connectivity
   294|import networkx as nx
   295|G = nx.from_numpy_array(adj[0].detach().cpu().numpy())
   296|nx.draw(G, node_size=50)
   297|```
   298|
   299|### 3. 跨患者泛化
   300|```python
   301|# Self-supervised pretraining on unlabeled data from new patient
   302|unlabeled_eeg = load_unlabeled_eeg()
   303|for eeg_segment in unlabeled_eeg:
   304|    _, ib_loss, recon_loss = model(eeg_segment, mask_ratio=0.3)
   305|    loss = ib_loss + 0.5 * recon_loss
   306|    loss.backward()
   307|    optimizer.step()
   308|```
   309|
   310|## 关键创新
   311|
   312|1. **IB 指导的图学习**: 显式考虑 EEG 噪声特性，产生紧凑可靠的连接模式
   313|2. **GMAE 自监督**: 通过掩码重建学习结构感知表示，缓解标签稀缺
   314|3. **可解释性**: 学到的图结构提供癫痫传播的临床洞见
   315|4. **患者间鲁棒性**: IB 原则和自监督学习提升跨患者泛化
   316|
   317|## 实现要点
   318|
   319|- **IB β 参数**: 需要调优以平衡信息压缩和预测能力
   320|- **掩码比例**: 通常 0.2-0.4 之间，过高会导致重建困难
   321|- **通道数**: 根据 EEG 导联配置调整（常见 19-64 通道）
   322|- **时间窗口**: 通常 1-4 秒的 EEG 片段（256-1024 样本 @ 256Hz）
   323|
   324|## 局限性
   325|
   326|- 图构造的计算复杂度为 O(n_channels²)
   327|- IB 原则的 β 参数需要针对不同数据集调优
   328|- 对极低质量 EEG（如大量伪迹）可能需要预处理
   329|
   330|## 激活关键词
   331|
   332|- eeg seizure detection, information bottleneck EEG, dynamic graph EEG, IRENE, graph masked autoencoder EEG, seizure propagation, inter-patient variability EEG
   333|

## Activation Keywords

- "irene-eeg-seizure-detection"
- "irene eeg seizure detection"
- "use irene eeg seizure detection"
- "irene eeg seizure detection help"
- "irene eeg seizure detection tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Irene Eeg Seizure Detection usage
```
User: "Help me with irene eeg seizure detection"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed irene eeg seizure detection assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
