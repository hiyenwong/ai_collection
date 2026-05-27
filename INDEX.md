## 2026-05-27 - Neuroscience Research (Cron Job)

### MindAlign: Bridging EEG, Vision, and Language for Zero-Shot Visual Decoding
- [[mindalign-eeg-visual-decoding]] - 三模态对比学习框架，实现EEG零样本视觉解码，54.1% Top-1准确率大幅超越基线 (arXiv: 2605.24523)
  - 两阶段训练：Masked autoencoder预训练 + 三模态对比对齐
  - CN-CLIP紧凑嵌入优于大型CLIP模型
  - 文本描述作为语义正则化器，权重α=0.3最优
  - **Activation**: EEG visual decoding, zero-shot image retrieval, tri-modal alignment

### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[stm-sequence-timing-replay]] - 脉冲神经网络中的序列时序学习，振荡背景输入控制重放速度 (arXiv: 2605.22523)
  - 持续编码：元素特定神经元群的顺序激活表示时长
  - 振荡时钟：背景振荡作为时钟信号控制重放速度
  - EEG/LFP相关性：清醒/睡眠重放速度与脑电振荡特征相关
  - **Activation**: spiking sequence timing, replay speed control, oscillatory clock


## 2026-05-27 - Neuroscience Research (Cron Job)

### Random neural networks match observed dimensionality of neural population recordings and motivate stronger experimental tests
- [[random-network-neural-dimensionality]] - First quantitative validation that minimally structured random neural networks can account for observed low dimensionality using DMFT with finite measurement time corrections (arXiv: 2605.26551)
  - Core methodology: Dynamical Mean-Field Theory extended with measurement time and behavioral context variability
  - Key finding: manifold orientation similarity more sensitive to network structure than dimensionality alone
  - **Activation**: neural dimensionality, random neural network, population recording, DMFT, neural manifold, connectivity inference

### Revealing the core dimensions underlying representations in brains, behavior and AI
- [[srf-similarity-representation-factorization]] - Similarity-Based Representation Factorization (SRF) for recovering interpretable non-negative embeddings from similarity matrices across neural/behavioral/AI data (arXiv: 2605.26921)
  - Core methodology: Non-negative factorization of similarity matrices with robustness to sparse/incomplete data
  - Key advantage: higher statistical power for hypothesis testing than traditional RSA
  - **Activation**: representation factorization, SRF, similarity matrix, interpretable embedding, brain-AI alignment

## 2026-05-27 - Medicine + Quantum (Cron Job)

### What Molecular Structure Cannot Tell Us: A Taxonomy of Explainability Gaps in GNN-Based Drug Toxicity Prediction
- [[gnn-drug-toxicity-explainability]] - Gap Taxonomy (GAP-1 to GAP-4) for systematic analysis of explainability limitations in GNN drug toxicity prediction using GNNExplainer on MPNN models (arXiv: 2605.26183)
  - Core methodology: Train MPNN on Tox21, apply GNNExplainer for atom-level attribution, categorize missing predictions into 4 gap types
  - Key finding: molecular structure explains ~45% of known adverse effects; MNAR gap reveals systematic data absence in ChEMBL
  - **Activation**: GNN drug toxicity, GNNExplainer, MPNN, Gap Taxonomy, MNAR drug data, Tox21, pharmacovigilance, drug safety signals

### Autonomous oscillations in quantum electromechanics: tensor network treatment
- [[tensor-network-quantum-electromechanics]] - Tensor network framework for quantum electromechanical self-oscillations using binary vibrational mode representation with mesoscopic reservoir embeddings (arXiv: 2605.27326)
  - Core methodology: Map bosonic Hilbert space to binary representation, embed fermionic leads, compute steady states without real-time propagation
  - Key finding: self-oscillation window preceded by peak in occupation fluctuations, observed for both slow and fast mechanical modes
  - **Activation**: tensor network quantum, quantum electromechanics, self-oscillation, mesoscopic leads, binary mode mapping, quantum thermodynamics

     1|## 2026-05-28 - Neuroscience Research (Cron Job)
     2|
     3|### Arbor-TVB: Multi-Scale Co-Simulation Framework for Neural-Level Seizure Generation and Whole-Brain Propagation
     4|- [[arbor-tvb-multiscale-simulation]] - MPI-based integration of microscopic Arbor neurons with macroscopic TVB brain models, enabling bidirectional spike ↔ mean activity translation (arXiv: 2505.16861)
     5|  - First framework linking detailed spiking neurons (Arbor) with whole-brain network models (TVB) via MPI intercommunicator
     6|  - Real-time translation: discrete spikes → continuous mean activity, continuous input → synaptic currents
     7|  - Seizure case study: 38-region mouse brain model, seizure onset propagation from Arbor-embedded hippocampus to whole-brain
     8|  - Modular design: replace any TVB node with biologically realistic Arbor populations
     9|  - **Activation**: multiscale simulation, arbor tvb, seizure propagation, brain network model, mpi neuroscience, neural mass model
    10|
    11|## 2026-05-28 - Medicine + Quantum (Cron Job)
    12|
    13|### Parallel Multi-Circuit Quantum Feature Fusion in Hybrid Quantum-Classical Convolutional Neural Networks for Breast Tumor Classification
    14|- [[qcnn-parallel-feature-fusion-medical]] - Hybrid QCNN with parallel amplitude+angle encoding VQCs for medical image classification, statistically validated via Wilcoxon test and Cohen's d (arXiv: 2512.02066)
    15|  - Core methodology: Two distinct quantum circuits (amplitude-encoding VQC + angle-encoding VQC with circular entanglement) run in parallel on 4 qubits; quantum embeddings fused with classical conv features
    16|  - Statistical validation: Parameter-matched comparison, 5 independent runs, Wilcoxon signed-rank test (p=0.03125), Cohen's d=2.14 (large effect)
    17|  - **Activation**: qcnn parallel feature fusion, quantum feature fusion medical, statistical validation quantum ml, wilcoxon quantum advantage, cohen d quantum classification, breastmnist quantum
    18|
    19|### Discovering Data Encoding Strategies for Quantum-Classical Neural Networks Using Monte Carlo Tree Search
    20|- [[mcts-encoding-discovery-qml]] - MCTS discovers optimal data encoding circuits for QCCNN, effective rank as encoding performance predictor (arXiv: 2605.18540)
    21|  - Core methodology: MCTS searches encoding circuit space for quantum-classical CNN with non-variational quantum block + classical classifier
    22|  - Key insight: Effective rank of feature maps correlates with encoding performance (not entanglement capability or Fourier decomposition)
    23|  - **Activation**: mcts encoding discovery, effective rank encoding, quantum data encoding, QCCNN encoding, monte carlo tree search quantum
    24|
    25|## 2026-05-27 - Medicine + Quantum (Cron Job)
    26|
    27|### A novel perspective on denoising using quantum localization with application to medical imaging
    28|- [[a-novel-perspective-on-denoising-using-quantum-loc]] - Quantum-enhanced medical image classification framework (arXiv: 2405.12226)
    29|  - Core methodology: Background noise in many fields such as medical imaging poses significant challenges for accurate diagnosis, prompting the development of denoising algorithms. Traditional methodologies, however, ofte
    30|  - **Activation**: diagnosis, measurement, image, medical, noise, quantum
    31|
    32|## 2026-05-27 - Medicine + Quantum Metrology (Cron Job)
    33|
    34|### Journey in quantum metrology and sensing from foundations to applications: a review
    35|- [[quantum-metrology-sensing-review]] - 93页量子计量与传感综述，涵盖参数估计、量子Fisher信息、量子成像与照明、原子钟 (arXiv: 2605.21702)
    36|  - 经典/贝叶斯参数估计框架与量子Cramér-Rao界
    37|  - 量子Fisher信息矩阵用于多参数估计与资源检测
    38|  - 量子照明在噪声环境中的目标检测优势
    39|  - 量子传感在生物医学中的应用(NV中心磁力计、量子增强MRI)
    40|  - **Activation**: quantum metrology, quantum sensing, quantum Fisher information, quantum thermometry, quantum imaging, quantum illumination
    41|
    42|## 2026-05-27 - Medicine + Quantum ML (Cron Job)
    43|
    44|### High-fidelity molecular quantum logic gates resilient to interaction fluctuation
    45|- [[quantum-ml-medical-diagnosis]] - Quantum ML methodologies for medical diagnosis and healthcare
    46|  - Core pattern 1: Hybrid quantum-classical feature fusion with temperature-scaled balancing
    47|  - Core pattern 2: Tensor-network compression enabling small-qubit quantum processing
    48|  - **Activation**: quantum medical diagnosis, quantum healthcare, federated quantum, quantum transfer learning, quantum neural network, medical imaging quantum
    49|
    50|## 2026-05-27 - Neuroscience Research (Cron Job)
    51|
    52|## 2026-05-27 - Neuroscience Research (Cron Job)
    53|
    54|### BrainDyn: Sheaf Neural ODE for Generative Brain Dynamics
    55|- [[braindyn-sheaf-neural-ode]] - Sheaf Neural ODE + LSTM + Neural ODE framework for continuous-time generative brain dynamics on anatomically structured graphs (arXiv: 2605.19324)
    56|  - Combines sheaf theory (restriction maps + Laplacian) with neural ODEs for expressive brain graph dynamics
    57|  - Multi-modal: validated on resting-state fMRI (PNC), scalp EEG epilepsy (TUSZ), NEST spiking simulator
    58|  - Supports in-silico perturbation prediction and downstream classification tasks
    59|  - **Activation**: brain dynamics, sheaf neural ODE, generative brain model, fMRI forecasting, EEG dynamics, digital brain twin
    60|
    61|### Learning Sequence Timing and Control of Replay Speed in Spiking Neural Networks
    62|- [[learning-sequence-timing-snn]] - spiking Temporal Memory (sTM) model with element-specific timing encoding and oscillatory clock for flexible replay speed control (arXiv: 2605.22523)
    63|  - Novel mechanism: duration encoded by sequential sub-population activation (spatial encoding of time)
    64|  - Oscillatory background inputs serve as clock signals -- frequency controls replay speed
    65|  - Biological connection: EEG/LFP oscillation characteristics predict replay speed (theta=real-time, ripple=fast)
    66|  - **Activation**: sequence timing, spiking temporal memory, replay speed, oscillatory clock, hippocampal sequences
    67|
    68|### Large-scale Brain Dynamics Organized by Directional Coordination Hierarchy
    69|- [[directional-coordination-hierarchy-brain]] - Three-regime resting-state coordination framework (feedback/feedforward/integrative) revealing hierarchical information flow and schizophrenia disruption (biorxiv: 10.64898/2026.05.25.727703)
    70|  - 核心要点 1: Three stable coordination regimes form a low-dimensional directional landscape replicating across four cohorts
    71|  - 核心要点 2: In schizophrenia: feedback coordination decreases, integrative coordination increases, dynamics faster — tracks symptom severity and cognition
    72|  - **Activation**: directional brain coordination, resting-state dynamics, cortical hierarchy, schizophrenia biomarker
    73|
    74|### Low-Frequency Alpha Activity Shapes Visual Cortex Information Routing
    75|- [[low-frequency-alpha-visual-cortex-routing]] - Alpha oscillations in V1 encode spatially-specific figure-ground info and gate V1-V4 inter-areal communication via phase-dependent coupling (biorxiv: 10.64898/2026.05.25.727722)
    76|  - 核心要点 1: Alpha carries spatial figure position and orientation with fine specificity — active routing not idle inhibition
    77|  - 核心要点 2: Both local V1 spiking and V1-V4 coupling depend on alpha amplitude and instantaneous phase difference — alpha implements feedback gating
    78|  - **Activation**: alpha oscillation routing, visual cortex V1 V4 coupling, figure-ground, oscillatory gating
    79|
    80|## 2026-05-27 - Medicine + Quantum Computing (Cron Job)
    81|
    82|### Enhancing Blood Cells Classification using Hybrid Quantum Neural Networks
    83|- [[hqnn-medical-image-classification]] - HQNN combining ResNet-50 with variational quantum circuits for blood cell classification, improves macro F1-score by 3.7% (arXiv: 2605.23324)
    84|  - 核心要点 1: Three-model comparison methodology (HQNN vs Classical Matched vs Baseline) isolates quantum contribution from parameter count effects
    85|  - 核心要点 2: Bottleneck layer compresses 2048-dim CNN features to qubit count (4-8 qubits) for VQC input
    86|  - 核心要点 3: Tested on real IBM quantum hardware, proving noise robustness with only 1-3% degradation
    87|  - **Activation**: hybrid quantum neural network, HQNN, medical image classification, blood cell, variational quantum circuit, ResNet, noise robustness
    88|
    89|### Discovering Data Encoding Strategies for Quantum-Classical Neural Networks Using MCTS
    90|- [[mcts-encoding-discovery-qml]] - MCTS discovers optimal data encoding circuits for QCCNN, effective rank predicts encoding performance (arXiv: 2605.18540)
    91|  - 核心要点 1: MCTS outperforms hand-designed encoding circuits for quantum-classical CNN on medical imaging
    92|  - 核心要点 2: Effective rank of feature maps is better predictor than entanglement capability or Fourier decomposition
    93|  - **Activation**: monte carlo tree search, data encoding, quantum neural network, medical imaging, effective rank
    94|
    95|### FQPDR: Federated Quantum Neural Network for Privacy-preserving Diabetic Retinopathy Detection
    96|- [[federated-quantum-medical-diagnosis]] - Federated QNN for early diabetic retinopathy detection with privacy preservation (arXiv: 2605.08324)
    97|  - 核心要点 1: Shares model parameters only, not patient data, enabling cross-institutional collaboration
    98|  - 核心要点 2: Lightweight model works with limited samples and few learnable parameters
    99|  - **Activation**: federated learning, quantum neural network, diabetic retinopathy, privacy, medical imaging
   100|
   101|### Multi-Class Neurological Disorder Prediction with Tensor Network Feature Engineering
   102|- [[tensor-network-neurological-predictor]] - PARAFAC CP tensor decomposition ensemble for 8-class neurological disorder diagnosis on 55k+ images (arXiv: 2605.17771)
   103|  - 核心要点 1: Quantum-inspired classical tensor network approach achieves competitive performance
   104|  - 核心要点 2: Robust to tensor network expressivity variations (high/low rank configurations)
   105|  - **Activation**: tensor network, PARAFAC, neurological disorder, medical diagnosis, ensemble classifier
   106|
   107|     1|     1|## 2026-05-27 - Neuroscience Research (Cron Job)
   108|     2|     2|
   109|     3|     3|### Maximum Entropy Networks for Context-Dependent Neural Computations
   110|     4|     4|- [[maximum-entropy-neural-connectivity]] - Normative maximum entropy principle for deriving neural connectivity from task constraints, independent of gradient descent — bridges theory with trained network structure (arXiv: 2605.25607)
   111|     5|     5|  - 核心要点 1: Connectivity = probability distribution over weights maximizing Shannon entropy under task constraints; yields unique "least-biased" solution consistent with function
   112|     6|     6|  - 核心要点 2: Maximum entropy connectivity matches gradient-descent-trained networks quantitatively across different learning regimes; context count drives phase transition from specialized to random populations
   113|     7|     7|  - **Activation**: maximum entropy, neural connectivity, context-dependent computation, normative neuroscience, information theory, brain network structure
   114|     8|     8|
   115|     9|     9|### Multi-Objective SNN Oscillation Optimization with NSGA-III
   116|    10|    10|- [[multi-objective-snn-oscillation]] - NSGA-III genetic algorithm for simultaneously optimizing recurrent SNN connectivity to match neural firing rates and oscillation frequencies — validated on brain organoids (arXiv: 2605.25224)
   117|    11|    11|  - 核心要点 1: Oscillation frequencies are more parameter-sensitive than firing rates; NSGA-III Pareto frontier reveals trade-offs between matching multiple neural targets simultaneously
   118|    12|    12|  - 核心要点 2: Framework generalizes to brain organoids and decision-making models with transient epoch dynamics; identified low-activity regime for decision states
   119|    13|    13|  - **Activation**: spiking neural network, NSGA-III, neural oscillation, Izhikevich neuron, brain organoid, multi-objective optimization, recurrent SNN
   120|    14|    14|
   121|    15|    15|## 2026-05-27 - Neuroscience Research (Cron Job)
   122|    16|    16|
   123|    17|    17|### Random Neural Networks & Neural Population Dimensionality
   124|    18|    18|- [[random-neural-network-dimensionality]] - DMFT framework quantitatively predicts low dimensionality in large-scale neural population recordings by incorporating finite measurement time and behavioral context variability (arXiv: 2605.26551)
   125|    19|    19|  - 核心要点 1: Dynamical Mean-Field Theory predicts covariance structure of randomly-connected networks; finite-T corrections align predictions with experiment
   126|    20|    20|  - 核心要点 2: Manifold orientation similarity across behavioral contexts is more sensitive to connectivity structure than dimensionality alone
   127|    21|    21|  - **Activation**: random neural network, neural population dimensionality, DMFT, neural manifold, connectivity inference
   128|    22|    22|
   129|    23|    23|### SRF: Similarity-Based Representation Factorization
   130|    24|    24|- [[srf-similarity-representation-factorization]] - General method for recovering low-dimensional, non-negative, interpretable dimensions from similarity matrices in brains, behavior, and AI (arXiv: 2605.26921)
   131|    25|    25|  - 核心要点 1: SRF factorizes pairwise similarity matrices S approx W*W^T with non-negativity constraints, yielding semantically interpretable additive dimensions
   132|    26|    26|  - 核心要点 2: 6-8 shared core dimensions found between human visual cortex and CNN layers; behavioral judgments emphasize unique semantic/functional axes
   133|    27|    27|  - **Activation**: representation factorization, brain-AI alignment, RSA interpretable, similarity embedding, core dimensions
   134|    28|    28|
   135|    29|    29|## 2026-05-27 - 医学 + 量子力学 (Cron Job - Wednesday)
   136|    30|    30|
   137|    31|    31|### Quantum Medical Patterns
   138|    32|    32|- [[quantum-medical-patterns]] - Reusable research patterns from quantum computing in medical/healthcare: hybrid architectures, quantum kernel methods, federated diagnosis, reservoir computing, QLIF forecasting (arXiv: multiple)
   139|    33|    33|- Core pattern 1: Hybrid quantum-classical clinical forecasting (GRU → VQC → classical decoder)
   140|    34|    34|- Core pattern 2: Quantum kernel medical imaging (foundation model → PCA → QSVM, 18/18 F1 wins)
   141|    35|    35|- Core pattern 3: Federated quantum medical diagnosis (privacy-preserving multi-hospital DR detection)
   142|    36|    36|- Core pattern 4: Cold-atom reservoir computing for medical imaging (auto-encoder + neutral-atom RC)
   143|    37|    37|- Core pattern 5: QLIF-CAST quantum spiking forecasting (15.4% lower MSE than classical LIF)
   144|    38|    38|- Design space exploration: encoding schemes, entanglement topologies, measurement strategies
   145|    39|    39|- **Activation**: quantum medical diagnosis, quantum healthcare AI, quantum clinical forecasting, hybrid quantum medical, quantum kernel medical imaging, federated quantum medical, quantum reservoir medical, 量子医疗诊断
   146|    40|    40|
   147|    41|    41|1|## 2026-05-27 - Neuroscience Research (Cron Job)
   148|    42|    42|2|
   149|    43|    43|3|### SpikeReg: Energy-Efficient 3D Deformable Medical Image Registration with Spiking Neural Networks
   150|    44|    44|4|- [[spikereg-snn-medical-registration]] - First SNN-based 3D deformable brain MRI registration matching ANN accuracy at 12.8% spike rate and 55.5× energy reduction (arXiv: 2605.25144)
   151|    45|    45|5|  - ANN-to-SNN conversion via layer-wise weight transfer + activation-percentile threshold calibration
   152|    46|    46|6|  - Surrogate gradient fine-tuning with local cross-correlation + diffusion regularization + spike-rate sparsity
   153|    47|    47|7|  - Negative findings: displacement distillation hurts, Dice-loss ANN teachers fail to transfer
   154|    48|    48|8|  - **Activation**: SNN medical imaging, neuromorphic registration, energy-efficient 3D perception, ANN-to-SNN conversion
   155|    49|    49|9|
   156|    50|    50|10|### Neuromorphic LiDAR-based Bird's Eye View Object Detection using Energy-efficient Spiking Neural Networks
   157|    51|    51|11|
   158|    52|    52|  - Learned spike encoding outperforms hand-crafted Poisson/latency/z-axis encoding strategies
   159|    53|    53|  - Two variants: membrane potential (max accuracy) and fully binary (neuromorphic hardware deployment)
   160|    54|    54|  - Block-wise energy analysis via SynOps/MAC proxy model
   161|    55|    55|  - **Activation**: neuromorphic autonomous driving, SNN object detection, LiDAR perception, spike encoding
   162|    56|    56|
   163|    57|    57|## 2026-05-27 - Medicine + Quantum (Cron Job - Wednesday 13:00)
   164|    58|    58|
   165|    59|    59|### HQNN Expressibility-Trainability Trade-off
   166|    60|    60|- [[hqnn-expressibility-trainability]] - Multi-objective NAS framework for HQNNs revealing classical components decouple trainability from PQC expressibility under full end-to-end training (arXiv: 2605.25768)
   167|    61|    61|  - Full end-to-end hybrid training can completely eliminate the expressibility-trainability trade-off
   168|    62|    62|  - Multi-objective NAS jointly optimizes expressibility, trainability, and task performance over combined classical-quantum design space
   169|    63|    63|  - Pure PQCs show only weak trade-off; hybrid architectures increasingly disrupt it
   170|    64|    64|  - **Activation**: HQNN expressibility trainability, hybrid quantum neural network optimization, quantum circuit barren plateau, neural architecture search quantum, PQC expressibility, quantum classical hybrid training
   171|    65|    65|
   172|    66|    66|## 2026-05-27 - Neuroscience Research (Cron Job)
   173|    67|    67|
   174|    68|    68|### Random Neural Networks Match Neural Population Dimensionality
   175|    69|    69|- [[random-neural-network-dimensionality]] - DMFT framework shows random connectivity explains low-dimensionality of large-scale neural recordings when finite measurement time and behavioral context variability are included (arXiv: 2605.26551)
   176|    70|    70|  - Non-monotonic dependence: dimensionality varies non-monotonically with external input strength
   177|    71|    71|  - Manifold orientation similarity across behavioral contexts is more sensitive to connectivity structure than dimensionality alone
   178|    72|    72|  - **Activation**: random neural network, neural population dimensionality, dynamical mean field theory, neural manifold, brain recording, connectivity inference, collective dynamics
   179|    73|    73|
   180|    74|    74|### Multi-Objective NSGA-III Optimisation of SNN Oscillatory Dynamics
   181|    75|    75|- [[multi-objective-snn-oscillation]] - NSGA-III co-optimises Izhikevich RSNN connectivity for both firing rates AND oscillation frequencies in spontaneous activity, brain organoids, and decision-making dynamics (arXiv: 2605.25224)
   182|    76|    76|  - Oscillation frequencies are more parameter-sensitive than firing rates — harder to pin precisely
   183|    77|    77|  - Successfully validated on brain organoid recordings and simulated decision-making RSNNs
   184|    78|    78|  - **Activation**: spiking neural network oscillation, NSGA-III, RSNN optimisation, Izhikevich neuron, brain organoid, neural oscillation fitting, multi-objective SNN
   185|    79|    79|
   186|    80|    80|## 2026-05-27 - Medicine + Quantum ML (Cron Job)
   187|    81|    81|
   188|    82|    82|### Quantum ML Medical Diagnosis Consolidated Skill
   189|    83|    83|- [[quantum-ml-medical-diagnosis]] - Comprehensive quantum ML methodologies for medical diagnosis and healthcare
   190|    84|    84|  - Core pattern 1: Hybrid quantum-classical feature fusion with temperature-scaled balancing (TSHF)
   191|    85|    85|  - Core pattern 2: Tensor-network compression enabling small-qubit quantum processing
   192|    86|    86|  - Core pattern 3: Privacy-aware federated quantum learning with MPC-secured aggregation
   193|    87|    87|  - Core pattern 4: Quantum transfer learning with fair benchmarking under NISQ constraints
   194|    88|    88|  - Core pattern 5: Quanvolutional neural networks for disease detection
   195|    89|    89|  - **Activation**: quantum medical diagnosis, quantum healthcare, federated quantum, quantum transfer learning, quantum neural network, medical imaging quantum, quanvolutional, HQNN
   196|    90|    90|
   197|    91|    91|## 2026-05-27 - Medicine + Quantum (Cron Job)
   198|    92|    92|
   199|    93|    93|### Design Space Exploration of Hybrid Quantum Neural Networks for Chronic Kidney Disease
   200|    94|    94|- [[hqnn-design-space-exploration]] - Systematic benchmarking of 625 HQNN configurations for CKD diagnosis, IQP+Ring entanglement achieves best accuracy-efficiency trade-off (arXiv: 2604.13608)
   201|    95|    95|  - Core finding: high performance does NOT require large parameter counts or complex circuits
   202|    96|    96|  - IQP encoding + Ring entanglement is optimal combo — captures pairwise correlations efficiently with minimal depth
   203|    97|    97|  - **Activation**: HQNN design space, quantum neural network architecture, hybrid quantum medical diagnosis, quantum encoding schemes, CKD classification, quantum circuit benchmarking
   204|    98|    98|
   205|    99|    99|### Analyzing Blood Cells with QML: Equilibrium Propagation and VQCs for Acute Myeloid Leukemia Detection
   206|   100|   100|- [[qml-equilibrium-propagation-medical]] - Energy-based backprop-free quantum training for blood cell classification, competitive under NISQ constraints (arXiv: 1808)
   207|   101|   101|
   208|   102|## 2026-05-27 - Medicine + Quantum Computing (Cron Job)
   209|   103|
   210|   104|### Enhancing Blood Cells Classification using Hybrid Quantum Neural Networks
   211|   105|- [[hqnn-medical-classification]] - HQNN combines ResNet-50 backbone with variational quantum circuit for blood cell classification, improving macro F1 by 3.7% (arXiv: 2605.23324)
   212|   106|  - ResNet-50 → latent bottleneck → VQC architecture
   213|   107|  - 3-architecture comparison isolates quantum contribution
   214|   108|  - **Activation**: hybrid quantum neural network, HQNN, medical image classification, blood cell
   215|   109|
   216|   110|### QT-PUF: Quantum Tunneling Leakage Based PUF for Implantable IoMT Devices
   217|   111|- [[quantum-medical-device-security]] - Gate-tunneling-leakage PUF leverages quantum effects for implantable healthcare device authentication (arXiv: 2605.22113)
   218|   112|  - Physical unclonable function using quantum tunneling
   219|   113|  - Device-level security for Internet of Medical Things
   220|   114|  - **Activation**: quantum PUF, IoMT security, implantable device authentication
   221|   115|
   222|   116|### Multi-Class Neurological Disorder Prediction with Tensor Network Feature Engineering
   223|   117|- [[tensor-network-medical-imaging]] - PARAFAC CP tensor decomposition for neurological disorder diagnosis, inspired by quantum many-body physics (arXiv: 2605.17771)
   224|   118|  - Quantum-inspired tensor feature engineering for MRI
   225|   119|  - Ensemble classifier with tensor features
   226|   120|  - **Activation**: tensor network, PARAFAC CP, neurological disorder, MRI diagnosis
   227|   121|
   228|   122|### Quantum Circuit Simulation of Compartmental Drug Dynamics
   229|   123|- [[quantum-pkpd-simulation]] - Reformulates PK/PD models as open quantum systems with 12-qubit variational circuits for drug dynamics simulation (arXiv: 2605.09691)
   230|   124|  - 12 qubits encoding 4 pharmacological compartments
   231|   125|  - Inter-compartmental transitions as controlled quantum gates
   232|   126|  - **Activation**: quantum PK/PD, drug dynamics, compartmental model, variational quantum circuit, pennylane
   233|   127|
   234|   128|### FQPDR: Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy
   235|   129|- [[federated-quantum-medical-diagnosis]] - Federated QNN for microaneurysm detection combining FL with quantum neural networks for privacy-preserving medical imaging (arXiv: 2605.08324)
   236|   130|  - Federated quantum learning for medical image privacy
   237|   131|  - Early detection of low-contrast microaneurysm features
   238|   132|  - **Activation**: federated quantum neural network, diabetic retinopathy, privacy-preserving ML
   239|   133|
   240|   134|### Medical Imaging Classification with Cold-Atom Reservoir Computing
   241|   135|- [[cold-atom-reservoir-computing-medical]] - Neutral-atom reservoir computing with guided auto-encoder and surrogate-driven training for medical image classification (arXiv: 2605.06727)
   242|   136|  - Guided auto-encoder for high-dimensional medical image compression
   243|   137|  - Surrogate-driven training for non-differentiable quantum measurements
   244|   138|  - **Activation**: cold atom reservoir computing, medical imaging, surrogate training, neutral atom
   245|   139|
   246|   140|### Quantum Kernel Advantage over Classical Collapse in Medical Foundation Model Embeddings
   247|   141|- [[quantum-kernel-advantage-medical]] - QSVM with frozen medical foundation model embeddings (MedSigLIP-448, RAD-DINO) shows quantum kernel advantage on MIMIC-CXR (arXiv: 2604.24597)
   248|   142|  - Two-tier fair comparison framework for QSVM vs classical SVM
   249|   143|  - Medical foundation model embeddings with quantum kernels
   250|   144|  - **Activation**: quantum kernel advantage, QSVM, medical foundation model, MIMIC-CXR
   251|   145|
   252|   146|## 2026-05-27 - Medicine + Quantum ML (Cron Job - Wednesday)
   253|   147|
   254|   148|### Deterministic Mapping of Topological Phases via NARX Neural Networks
   255|   149|- [[narx-topological-phase-mapping]] - NARX neural network discovers deterministic functional identities between topological invariants and critical parameters in quantum systems, achieving MSE of 10^{-27} (arXiv: 2605.27300)
   256|   150|  - NARX achieves numerical-precision MSE at delay d=1, revealing exact functional identity between winding number and critical measurement strength
   257|   151|  - Complexity paradox: NARX accuracy collapses at higher delays (d=4), confirming non-trivial high-precision dynamic mapping rather than trivial pattern learning
   258|   152|  - **Activation**: NARX neural network, topological phase transition, winding number, quantum phase mapping, autoregressive exogenous, deterministic identity discovery
   259|   153|
   260|   154|### Leveraging Quantum-Based Architectures for Robust Diagnostics (QCNN)
   261|   155|- [[quantum-medical-diagnostics]] - Hybrid classical-quantum QCNN framework for multi-class medical image classification using pretrained encoders + angle/amplitude encoding + QCNN (arXiv: 2511.12386)
   262|   156|  - Achieves 99% accuracy on kidney CT, 97% on cervical cell, 99% on brain tumor classification
   263|   157|  - Fewer trainable parameters than classical CNNs with superior precision, recall, and F1
   264|   158|  - **Activation**: QCNN medical, quantum convolutional neural network, medical image classification, hybrid quantum classical diagnostics, pretrained encoder quantum
   265|   159|
   266|   160|### HQNN with Multi-Head Attention for Breast Cancer Thermographic Classification
   267|   161|- [[hqnn-breast-cancer-thermographic]] - HQNN combining 4-qubit variational circuit with strongly entangling layers and classical CNN with multi-head attention for breast cancer thermography (arXiv: 2604.16953)
   268|   162|  - Quantum-aware feature encoding via parameterized quantum circuits with multi-head attention
   269|   163|  - Classical attention mechanisms for feature fusion, superior convergence dynamics
   270|   164|  - **Activation**: HQNN thermography, breast cancer classification, quantum-classical attention, variational quantum circuit, multi-head quantum encoding
   271|   165|
   272|   166|
   273|## 2026-05-27 - Medicine + Quantum ML (Cron Job)
   274|
   275|### Enhancing Blood Cells Classification using Hybrid Quantum Neural Networks
   276|- [[hqnn-medical-image-classification]] - HQNN combining ResNet-50 + VQC for blood cell classification, +3.7% macro F1 over classical baselines, IBM hardware validated (arXiv: 2605.23324)
   277|  - ResNet-50 backbone with low-dimensional latent bottleneck + variational quantum circuit
   278|  - Three-way comparison: HQNN vs Classical Matched vs Baseline
   279|  - IBM quantum hardware evaluation shows modest noise degradation
   280|  - **Activation**: HQNN, blood cell classification, quantum medical imaging, ResNet quantum, variational quantum circuit, medical image classification quantum
   281|
   282|### Adaptive Hybrid Quantum-Classical Feature Fusion for Breast Cancer
   283|- [[adaptive-hybrid-quantum-classical-feature-fusion-medical]] - Temperature-Scaled Hybrid Fusion (TSHF) for breast cancer diagnosis on BreastMNIST, 87.82% accuracy (arXiv: 2604.22903)
   284|  - Three fusion strategies: SHF (static), DHF (dynamic), TSHF (temperature-scaled)
   285|  - TSHF resolves optimization bottlenecks via learnable scalar for gradient balancing
   286|  - Dual-branch pipeline: classical + quantum feature extraction with complementary fusion
   287|  - **Activation**: TSHF, temperature-scaled fusion, breast cancer quantum, hybrid quantum-classical, feature fusion, BreastMNIST, gradient balancing
   288|
   289|### SDA-QEC: Diffusion Augmentation with Quantum-Enhanced Classification
   290|- [[quantum-generative-diffusion-medical]] - Simplified Diffusion Augmentation + Quantum-Enhanced Classification for coronary angiography, 98.33% accuracy (arXiv: 2601.18556)
   291|  - Lightweight diffusion augmentor for minority class oversampling
   292|  - Quantum feature layer in MobileNetV2 for Hilbert space mapping
   293|  - Addresses class imbalance in medical imaging (98.33% sensitivity + specificity)
   294|  - **Activation**: SDA-QEC, diffusion augmentation, quantum-enhanced classification, coronary angiography, class imbalance medical, MobileNetV2 quantum
   295|
   296|## 2026-05-27 - Medicine + Quantum (Cron Job)
   297|
   298|### MediQ-GAN: Quantum-Inspired GAN for High Resolution Medical Image Generation
   299|- [[mediq-gan-medical-image-generation]] - Quantum-inspired GAN with dual-stream generator and prototype-guided skip connections for medical image augmentation (arXiv: 2506.21015)
   300|  - Dual-stream architecture fusing classical and quantum-inspired branches via prototype-guided skip connections
   301|  - VQCs inherently preserve full-rank mappings, avoid rank collapse, and balance expressivity with trainability
   302|  - Outperforms state-of-the-art GANs and diffusion models on three medical imaging datasets
   303|  - First latent-geometry and rank-based analysis of quantum-inspired GANs
   304|  - **Activation**: quantum gan medical, mediq-gan, medical image augmentation, dual-stream quantum generator, prototype-guided skip, variational quantum circuit gan, rank collapse prevention
   305|
   306|