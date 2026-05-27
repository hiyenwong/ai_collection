
## 2026-05-28 - Neuroscience Research (Cron Job)

### Random neural networks match observed dimensionality of neural population recordings
- [[random-neural-network-dimensionality]] - 随机神经网络维数匹配神经种群记录的DMFT方法论 (arXiv:2605.26551)
  - Dynamical Mean-Field Theory扩展纳入有限测量时间和跨语境变异
  - 流形方向相似性比维数更敏感于网络结构
  - 提供推断连接结构的定量实验设计指导
  - **Activation**: neural dimensionality, DMFT, neural manifold, experimental design

### Revealing the core dimensions underlying representations in brains, behavior and AI
- [[srf-similarity-representation-factorization]] - SRF方法从相似性矩阵恢复可解释维度 (arXiv:2605.26921)
  - 非负低维嵌入提高可解释性
  - 支持稀疏采样和不完整数据
  - 假设检验效力高于直接比较相似性矩阵
  - **Activation**: SRF, representation factorization, similarity matrix, interpretability

     1|## 2026-05-28 - Systems Engineering (Cron Job)
     2|
     3|### Statistical and Algorithmic Foundations of Probing Quantum Systems with Compressive Measurements: A Review
     4|- [[structured-quantum-tomography]] - 结构化量子态层析成像方法论，结合压缩感知、低秩表示、张量网络和神经量子态实现可扩展量子态重建 (arXiv: 2605.27191)
     5|  - 三大主题：紧凑态表示、测量设计（IC-POVM/随机测量）、计算算法
     6|  - 随机测量（Pauli/Clifford）提供近最优采样复杂度
     7|  - 凸优化保证恢复、非凸优化提升可扩展性
     8|  - **Activation**: quantum state tomography, compressive quantum measurement, IC-POVM, randomized measurement
     9|
    10|
    11|## 2026-05-27 - Neuroscience Research (Cron Job)
    12|
    13|### MindAlign: Bridging EEG, Vision, and Language for Zero-Shot Visual Decoding
    14|- [[mindalign-eeg-visual-decoding]] - 三模态对比学习框架，实现EEG零样本视觉解码，54.1% Top-1准确率大幅超越基线 (arXiv: 2605.24523)
    15|  - 两阶段训练：Masked autoencoder预训练 + 三模态对比对齐
    16|  - CN-CLIP紧凑嵌入优于大型CLIP模型
    17|  - 文本描述作为语义正则化器，权重α=0.3最优
    18|  - **Activation**: EEG visual decoding, zero-shot image retrieval, tri-modal alignment
    19|
    20|### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
    21|- [[stm-sequence-timing-replay]] - 脉冲神经网络中的序列时序学习，振荡背景输入控制重放速度 (arXiv: 2605.22523)
    22|  - 持续编码：元素特定神经元群的顺序激活表示时长
    23|  - 振荡时钟：背景振荡作为时钟信号控制重放速度
    24|  - EEG/LFP相关性：清醒/睡眠重放速度与脑电振荡特征相关
    25|  - **Activation**: spiking sequence timing, replay speed control, oscillatory clock
    26|
    27|
    28|## 2026-05-27 - Neuroscience Research (Cron Job)
    29|
    30|### Random neural networks match observed dimensionality of neural population recordings and motivate stronger experimental tests
    31|- [[random-network-neural-dimensionality]] - First quantitative validation that minimally structured random neural networks can account for observed low dimensionality using DMFT with finite measurement time corrections (arXiv: 2605.26551)
    32|  - Core methodology: Dynamical Mean-Field Theory extended with measurement time and behavioral context variability
    33|  - Key finding: manifold orientation similarity more sensitive to network structure than dimensionality alone
    34|  - **Activation**: neural dimensionality, random neural network, population recording, DMFT, neural manifold, connectivity inference
    35|
    36|### Revealing the core dimensions underlying representations in brains, behavior and AI
    37|- [[srf-similarity-representation-factorization]] - Similarity-Based Representation Factorization (SRF) for recovering interpretable non-negative embeddings from similarity matrices across neural/behavioral/AI data (arXiv: 2605.26921)
    38|  - Core methodology: Non-negative factorization of similarity matrices with robustness to sparse/incomplete data
    39|  - Key advantage: higher statistical power for hypothesis testing than traditional RSA
    40|  - **Activation**: representation factorization, SRF, similarity matrix, interpretable embedding, brain-AI alignment
    41|
    42|## 2026-05-27 - Medicine + Quantum (Cron Job)
    43|
    44|### What Molecular Structure Cannot Tell Us: A Taxonomy of Explainability Gaps in GNN-Based Drug Toxicity Prediction
    45|- [[gnn-drug-toxicity-explainability]] - Gap Taxonomy (GAP-1 to GAP-4) for systematic analysis of explainability limitations in GNN drug toxicity prediction using GNNExplainer on MPNN models (arXiv: 2605.26183)
    46|  - Core methodology: Train MPNN on Tox21, apply GNNExplainer for atom-level attribution, categorize missing predictions into 4 gap types
    47|  - Key finding: molecular structure explains ~45% of known adverse effects; MNAR gap reveals systematic data absence in ChEMBL
    48|  - **Activation**: GNN drug toxicity, GNNExplainer, MPNN, Gap Taxonomy, MNAR drug data, Tox21, pharmacovigilance, drug safety signals
    49|
    50|### Autonomous oscillations in quantum electromechanics: tensor network treatment
    51|- [[tensor-network-quantum-electromechanics]] - Tensor network framework for quantum electromechanical self-oscillations using binary vibrational mode representation with mesoscopic reservoir embeddings (arXiv: 2605.27326)
    52|  - Core methodology: Map bosonic Hilbert space to binary representation, embed fermionic leads, compute steady states without real-time propagation
    53|  - Key finding: self-oscillation window preceded by peak in occupation fluctuations, observed for both slow and fast mechanical modes
    54|  - **Activation**: tensor network quantum, quantum electromechanics, self-oscillation, mesoscopic leads, binary mode mapping, quantum thermodynamics
    55|
    56|     1|## 2026-05-28 - Neuroscience Research (Cron Job)
    57|     2|
    58|     3|### Arbor-TVB: Multi-Scale Co-Simulation Framework for Neural-Level Seizure Generation and Whole-Brain Propagation
    59|     4|- [[arbor-tvb-multiscale-simulation]] - MPI-based integration of microscopic Arbor neurons with macroscopic TVB brain models, enabling bidirectional spike ↔ mean activity translation (arXiv: 2505.16861)
    60|     5|  - First framework linking detailed spiking neurons (Arbor) with whole-brain network models (TVB) via MPI intercommunicator
    61|     6|  - Real-time translation: discrete spikes → continuous mean activity, continuous input → synaptic currents
    62|     7|  - Seizure case study: 38-region mouse brain model, seizure onset propagation from Arbor-embedded hippocampus to whole-brain
    63|     8|  - Modular design: replace any TVB node with biologically realistic Arbor populations
    64|     9|  - **Activation**: multiscale simulation, arbor tvb, seizure propagation, brain network model, mpi neuroscience, neural mass model
    65|    10|
    66|    11|## 2026-05-28 - Medicine + Quantum (Cron Job)
    67|    12|
    68|    13|### Parallel Multi-Circuit Quantum Feature Fusion in Hybrid Quantum-Classical Convolutional Neural Networks for Breast Tumor Classification
    69|    14|- [[qcnn-parallel-feature-fusion-medical]] - Hybrid QCNN with parallel amplitude+angle encoding VQCs for medical image classification, statistically validated via Wilcoxon test and Cohen's d (arXiv: 2512.02066)
    70|    15|  - Core methodology: Two distinct quantum circuits (amplitude-encoding VQC + angle-encoding VQC with circular entanglement) run in parallel on 4 qubits; quantum embeddings fused with classical conv features
    71|    16|  - Statistical validation: Parameter-matched comparison, 5 independent runs, Wilcoxon signed-rank test (p=0.03125), Cohen's d=2.14 (large effect)
    72|    17|  - **Activation**: qcnn parallel feature fusion, quantum feature fusion medical, statistical validation quantum ml, wilcoxon quantum advantage, cohen d quantum classification, breastmnist quantum
    73|    18|
    74|    19|### Discovering Data Encoding Strategies for Quantum-Classical Neural Networks Using Monte Carlo Tree Search
    75|    20|- [[mcts-encoding-discovery-qml]] - MCTS discovers optimal data encoding circuits for QCCNN, effective rank as encoding performance predictor (arXiv: 2605.18540)
    76|    21|  - Core methodology: MCTS searches encoding circuit space for quantum-classical CNN with non-variational quantum block + classical classifier
    77|    22|  - Key insight: Effective rank of feature maps correlates with encoding performance (not entanglement capability or Fourier decomposition)
    78|    23|  - **Activation**: mcts encoding discovery, effective rank encoding, quantum data encoding, QCCNN encoding, monte carlo tree search quantum
    79|    24|
    80|    25|## 2026-05-27 - Medicine + Quantum (Cron Job)
    81|    26|
    82|    27|### A novel perspective on denoising using quantum localization with application to medical imaging
    83|    28|- [[a-novel-perspective-on-denoising-using-quantum-loc]] - Quantum-enhanced medical image classification framework (arXiv: 2405.12226)
    84|    29|  - Core methodology: Background noise in many fields such as medical imaging poses significant challenges for accurate diagnosis, prompting the development of denoising algorithms. Traditional methodologies, however, ofte
    85|    30|  - **Activation**: diagnosis, measurement, image, medical, noise, quantum
    86|    31|
    87|    32|## 2026-05-27 - Medicine + Quantum Metrology (Cron Job)
    88|    33|
    89|    34|### Journey in quantum metrology and sensing from foundations to applications: a review
    90|    35|- [[quantum-metrology-sensing-review]] - 93页量子计量与传感综述，涵盖参数估计、量子Fisher信息、量子成像与照明、原子钟 (arXiv: 2605.21702)
    91|    36|  - 经典/贝叶斯参数估计框架与量子Cramér-Rao界
    92|    37|  - 量子Fisher信息矩阵用于多参数估计与资源检测
    93|    38|  - 量子照明在噪声环境中的目标检测优势
    94|    39|  - 量子传感在生物医学中的应用(NV中心磁力计、量子增强MRI)
    95|    40|  - **Activation**: quantum metrology, quantum sensing, quantum Fisher information, quantum thermometry, quantum imaging, quantum illumination
    96|    41|
    97|    42|## 2026-05-27 - Medicine + Quantum ML (Cron Job)
    98|    43|
    99|    44|### High-fidelity molecular quantum logic gates resilient to interaction fluctuation
   100|    45|- [[quantum-ml-medical-diagnosis]] - Quantum ML methodologies for medical diagnosis and healthcare
   101|