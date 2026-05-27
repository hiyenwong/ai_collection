## 2026-05-27 - Medicine + Quantum Computing (Cron Job)

### Enhancing Blood Cells Classification using Hybrid Quantum Neural Networks
- [[hqnn-medical-image-classification]] - HQNN combining ResNet-50 with variational quantum circuits for blood cell classification, improves macro F1-score by 3.7% (arXiv: 2605.23324)
  - 核心要点 1: Three-model comparison methodology (HQNN vs Classical Matched vs Baseline) isolates quantum contribution from parameter count effects
  - 核心要点 2: Bottleneck layer compresses 2048-dim CNN features to qubit count (4-8 qubits) for VQC input
  - 核心要点 3: Tested on real IBM quantum hardware, proving noise robustness with only 1-3% degradation
  - **Activation**: hybrid quantum neural network, HQNN, medical image classification, blood cell, variational quantum circuit, ResNet, noise robustness

### Discovering Data Encoding Strategies for Quantum-Classical Neural Networks Using MCTS
- [[mcts-encoding-discovery-qml]] - MCTS discovers optimal data encoding circuits for QCCNN, effective rank predicts encoding performance (arXiv: 2605.18540)
  - 核心要点 1: MCTS outperforms hand-designed encoding circuits for quantum-classical CNN on medical imaging
  - 核心要点 2: Effective rank of feature maps is better predictor than entanglement capability or Fourier decomposition
  - **Activation**: monte carlo tree search, data encoding, quantum neural network, medical imaging, effective rank

### FQPDR: Federated Quantum Neural Network for Privacy-preserving Diabetic Retinopathy Detection
- [[federated-quantum-medical-diagnosis]] - Federated QNN for early diabetic retinopathy detection with privacy preservation (arXiv: 2605.08324)
  - 核心要点 1: Shares model parameters only, not patient data, enabling cross-institutional collaboration
  - 核心要点 2: Lightweight model works with limited samples and few learnable parameters
  - **Activation**: federated learning, quantum neural network, diabetic retinopathy, privacy, medical imaging

### Multi-Class Neurological Disorder Prediction with Tensor Network Feature Engineering
- [[tensor-network-neurological-predictor]] - PARAFAC CP tensor decomposition ensemble for 8-class neurological disorder diagnosis on 55k+ images (arXiv: 2605.17771)
  - 核心要点 1: Quantum-inspired classical tensor network approach achieves competitive performance
  - 核心要点 2: Robust to tensor network expressivity variations (high/low rank configurations)
  - **Activation**: tensor network, PARAFAC, neurological disorder, medical diagnosis, ensemble classifier

     1|     1|## 2026-05-27 - Neuroscience Research (Cron Job)
     2|     2|
     3|     3|### Maximum Entropy Networks for Context-Dependent Neural Computations
     4|     4|- [[maximum-entropy-neural-connectivity]] - Normative maximum entropy principle for deriving neural connectivity from task constraints, independent of gradient descent — bridges theory with trained network structure (arXiv: 2605.25607)
     5|     5|  - 核心要点 1: Connectivity = probability distribution over weights maximizing Shannon entropy under task constraints; yields unique "least-biased" solution consistent with function
     6|     6|  - 核心要点 2: Maximum entropy connectivity matches gradient-descent-trained networks quantitatively across different learning regimes; context count drives phase transition from specialized to random populations
     7|     7|  - **Activation**: maximum entropy, neural connectivity, context-dependent computation, normative neuroscience, information theory, brain network structure
     8|     8|
     9|     9|### Multi-Objective SNN Oscillation Optimization with NSGA-III
    10|    10|- [[multi-objective-snn-oscillation]] - NSGA-III genetic algorithm for simultaneously optimizing recurrent SNN connectivity to match neural firing rates and oscillation frequencies — validated on brain organoids (arXiv: 2605.25224)
    11|    11|  - 核心要点 1: Oscillation frequencies are more parameter-sensitive than firing rates; NSGA-III Pareto frontier reveals trade-offs between matching multiple neural targets simultaneously
    12|    12|  - 核心要点 2: Framework generalizes to brain organoids and decision-making models with transient epoch dynamics; identified low-activity regime for decision states
    13|    13|  - **Activation**: spiking neural network, NSGA-III, neural oscillation, Izhikevich neuron, brain organoid, multi-objective optimization, recurrent SNN
    14|    14|
    15|    15|## 2026-05-27 - Neuroscience Research (Cron Job)
    16|    16|
    17|    17|### Random Neural Networks & Neural Population Dimensionality
    18|    18|- [[random-neural-network-dimensionality]] - DMFT framework quantitatively predicts low dimensionality in large-scale neural population recordings by incorporating finite measurement time and behavioral context variability (arXiv: 2605.26551)
    19|    19|  - 核心要点 1: Dynamical Mean-Field Theory predicts covariance structure of randomly-connected networks; finite-T corrections align predictions with experiment
    20|    20|  - 核心要点 2: Manifold orientation similarity across behavioral contexts is more sensitive to connectivity structure than dimensionality alone
    21|    21|  - **Activation**: random neural network, neural population dimensionality, DMFT, neural manifold, connectivity inference
    22|    22|
    23|    23|### SRF: Similarity-Based Representation Factorization
    24|    24|- [[srf-similarity-representation-factorization]] - General method for recovering low-dimensional, non-negative, interpretable dimensions from similarity matrices in brains, behavior, and AI (arXiv: 2605.26921)
    25|    25|  - 核心要点 1: SRF factorizes pairwise similarity matrices S approx W*W^T with non-negativity constraints, yielding semantically interpretable additive dimensions
    26|    26|  - 核心要点 2: 6-8 shared core dimensions found between human visual cortex and CNN layers; behavioral judgments emphasize unique semantic/functional axes
    27|    27|  - **Activation**: representation factorization, brain-AI alignment, RSA interpretable, similarity embedding, core dimensions
    28|    28|
    29|    29|## 2026-05-27 - 医学 + 量子力学 (Cron Job - Wednesday)
    30|    30|
    31|    31|### Quantum Medical Patterns
    32|    32|- [[quantum-medical-patterns]] - Reusable research patterns from quantum computing in medical/healthcare: hybrid architectures, quantum kernel methods, federated diagnosis, reservoir computing, QLIF forecasting (arXiv: multiple)
    33|    33|- Core pattern 1: Hybrid quantum-classical clinical forecasting (GRU → VQC → classical decoder)
    34|    34|- Core pattern 2: Quantum kernel medical imaging (foundation model → PCA → QSVM, 18/18 F1 wins)
    35|    35|- Core pattern 3: Federated quantum medical diagnosis (privacy-preserving multi-hospital DR detection)
    36|    36|- Core pattern 4: Cold-atom reservoir computing for medical imaging (auto-encoder + neutral-atom RC)
    37|    37|- Core pattern 5: QLIF-CAST quantum spiking forecasting (15.4% lower MSE than classical LIF)
    38|    38|- Design space exploration: encoding schemes, entanglement topologies, measurement strategies
    39|    39|- **Activation**: quantum medical diagnosis, quantum healthcare AI, quantum clinical forecasting, hybrid quantum medical, quantum kernel medical imaging, federated quantum medical, quantum reservoir medical, 量子医疗诊断
    40|    40|
    41|    41|1|## 2026-05-27 - Neuroscience Research (Cron Job)
    42|    42|2|
    43|    43|3|### SpikeReg: Energy-Efficient 3D Deformable Medical Image Registration with Spiking Neural Networks
    44|    44|4|- [[spikereg-snn-medical-registration]] - First SNN-based 3D deformable brain MRI registration matching ANN accuracy at 12.8% spike rate and 55.5× energy reduction (arXiv: 2605.25144)
    45|    45|5|  - ANN-to-SNN conversion via layer-wise weight transfer + activation-percentile threshold calibration
    46|    46|6|  - Surrogate gradient fine-tuning with local cross-correlation + diffusion regularization + spike-rate sparsity
    47|    47|7|  - Negative findings: displacement distillation hurts, Dice-loss ANN teachers fail to transfer
    48|    48|8|  - **Activation**: SNN medical imaging, neuromorphic registration, energy-efficient 3D perception, ANN-to-SNN conversion
    49|    49|9|
    50|    50|10|### Neuromorphic LiDAR-based Bird's Eye View Object Detection using Energy-efficient Spiking Neural Networks
    51|    51|11|
    52|    52|  - Learned spike encoding outperforms hand-crafted Poisson/latency/z-axis encoding strategies
    53|    53|  - Two variants: membrane potential (max accuracy) and fully binary (neuromorphic hardware deployment)
    54|    54|  - Block-wise energy analysis via SynOps/MAC proxy model
    55|    55|  - **Activation**: neuromorphic autonomous driving, SNN object detection, LiDAR perception, spike encoding
    56|    56|
    57|    57|## 2026-05-27 - Medicine + Quantum (Cron Job - Wednesday 13:00)
    58|    58|
    59|    59|### HQNN Expressibility-Trainability Trade-off
    60|    60|- [[hqnn-expressibility-trainability]] - Multi-objective NAS framework for HQNNs revealing classical components decouple trainability from PQC expressibility under full end-to-end training (arXiv: 2605.25768)
    61|    61|  - Full end-to-end hybrid training can completely eliminate the expressibility-trainability trade-off
    62|    62|  - Multi-objective NAS jointly optimizes expressibility, trainability, and task performance over combined classical-quantum design space
    63|    63|  - Pure PQCs show only weak trade-off; hybrid architectures increasingly disrupt it
    64|    64|  - **Activation**: HQNN expressibility trainability, hybrid quantum neural network optimization, quantum circuit barren plateau, neural architecture search quantum, PQC expressibility, quantum classical hybrid training
    65|    65|
    66|    66|## 2026-05-27 - Neuroscience Research (Cron Job)
    67|    67|
    68|    68|### Random Neural Networks Match Neural Population Dimensionality
    69|    69|- [[random-neural-network-dimensionality]] - DMFT framework shows random connectivity explains low-dimensionality of large-scale neural recordings when finite measurement time and behavioral context variability are included (arXiv: 2605.26551)
    70|    70|  - Non-monotonic dependence: dimensionality varies non-monotonically with external input strength
    71|    71|  - Manifold orientation similarity across behavioral contexts is more sensitive to connectivity structure than dimensionality alone
    72|    72|  - **Activation**: random neural network, neural population dimensionality, dynamical mean field theory, neural manifold, brain recording, connectivity inference, collective dynamics
    73|    73|
    74|    74|### Multi-Objective NSGA-III Optimisation of SNN Oscillatory Dynamics
    75|    75|- [[multi-objective-snn-oscillation]] - NSGA-III co-optimises Izhikevich RSNN connectivity for both firing rates AND oscillation frequencies in spontaneous activity, brain organoids, and decision-making dynamics (arXiv: 2605.25224)
    76|    76|  - Oscillation frequencies are more parameter-sensitive than firing rates — harder to pin precisely
    77|    77|  - Successfully validated on brain organoid recordings and simulated decision-making RSNNs
    78|    78|  - **Activation**: spiking neural network oscillation, NSGA-III, RSNN optimisation, Izhikevich neuron, brain organoid, neural oscillation fitting, multi-objective SNN
    79|    79|
    80|    80|## 2026-05-27 - Medicine + Quantum ML (Cron Job)
    81|    81|
    82|    82|### Quantum ML Medical Diagnosis Consolidated Skill
    83|    83|- [[quantum-ml-medical-diagnosis]] - Comprehensive quantum ML methodologies for medical diagnosis and healthcare
    84|    84|  - Core pattern 1: Hybrid quantum-classical feature fusion with temperature-scaled balancing (TSHF)
    85|    85|  - Core pattern 2: Tensor-network compression enabling small-qubit quantum processing
    86|    86|  - Core pattern 3: Privacy-aware federated quantum learning with MPC-secured aggregation
    87|    87|  - Core pattern 4: Quantum transfer learning with fair benchmarking under NISQ constraints
    88|    88|  - Core pattern 5: Quanvolutional neural networks for disease detection
    89|    89|  - **Activation**: quantum medical diagnosis, quantum healthcare, federated quantum, quantum transfer learning, quantum neural network, medical imaging quantum, quanvolutional, HQNN
    90|    90|
    91|    91|## 2026-05-27 - Medicine + Quantum (Cron Job)
    92|    92|
    93|    93|### Design Space Exploration of Hybrid Quantum Neural Networks for Chronic Kidney Disease
    94|    94|- [[hqnn-design-space-exploration]] - Systematic benchmarking of 625 HQNN configurations for CKD diagnosis, IQP+Ring entanglement achieves best accuracy-efficiency trade-off (arXiv: 2604.13608)
    95|    95|  - Core finding: high performance does NOT require large parameter counts or complex circuits
    96|    96|  - IQP encoding + Ring entanglement is optimal combo — captures pairwise correlations efficiently with minimal depth
    97|    97|  - **Activation**: HQNN design space, quantum neural network architecture, hybrid quantum medical diagnosis, quantum encoding schemes, CKD classification, quantum circuit benchmarking
    98|    98|
    99|    99|### Analyzing Blood Cells with QML: Equilibrium Propagation and VQCs for Acute Myeloid Leukemia Detection
   100|   100|- [[qml-equilibrium-propagation-medical]] - Energy-based backprop-free quantum training for blood cell classification, competitive under NISQ constraints (arXiv: 1808)
   101|   101|
   102|## 2026-05-27 - Medicine + Quantum Computing (Cron Job)
   103|
   104|### Enhancing Blood Cells Classification using Hybrid Quantum Neural Networks
   105|- [[hqnn-medical-classification]] - HQNN combines ResNet-50 backbone with variational quantum circuit for blood cell classification, improving macro F1 by 3.7% (arXiv: 2605.23324)
   106|  - ResNet-50 → latent bottleneck → VQC architecture
   107|  - 3-architecture comparison isolates quantum contribution
   108|  - **Activation**: hybrid quantum neural network, HQNN, medical image classification, blood cell
   109|
   110|### QT-PUF: Quantum Tunneling Leakage Based PUF for Implantable IoMT Devices
   111|- [[quantum-medical-device-security]] - Gate-tunneling-leakage PUF leverages quantum effects for implantable healthcare device authentication (arXiv: 2605.22113)
   112|  - Physical unclonable function using quantum tunneling
   113|  - Device-level security for Internet of Medical Things
   114|  - **Activation**: quantum PUF, IoMT security, implantable device authentication
   115|
   116|### Multi-Class Neurological Disorder Prediction with Tensor Network Feature Engineering
   117|- [[tensor-network-medical-imaging]] - PARAFAC CP tensor decomposition for neurological disorder diagnosis, inspired by quantum many-body physics (arXiv: 2605.17771)
   118|  - Quantum-inspired tensor feature engineering for MRI
   119|  - Ensemble classifier with tensor features
   120|  - **Activation**: tensor network, PARAFAC CP, neurological disorder, MRI diagnosis
   121|
   122|### Quantum Circuit Simulation of Compartmental Drug Dynamics
   123|- [[quantum-pkpd-simulation]] - Reformulates PK/PD models as open quantum systems with 12-qubit variational circuits for drug dynamics simulation (arXiv: 2605.09691)
   124|  - 12 qubits encoding 4 pharmacological compartments
   125|  - Inter-compartmental transitions as controlled quantum gates
   126|  - **Activation**: quantum PK/PD, drug dynamics, compartmental model, variational quantum circuit, pennylane
   127|
   128|### FQPDR: Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy
   129|- [[federated-quantum-medical-diagnosis]] - Federated QNN for microaneurysm detection combining FL with quantum neural networks for privacy-preserving medical imaging (arXiv: 2605.08324)
   130|  - Federated quantum learning for medical image privacy
   131|  - Early detection of low-contrast microaneurysm features
   132|  - **Activation**: federated quantum neural network, diabetic retinopathy, privacy-preserving ML
   133|
   134|### Medical Imaging Classification with Cold-Atom Reservoir Computing
   135|- [[cold-atom-reservoir-computing-medical]] - Neutral-atom reservoir computing with guided auto-encoder and surrogate-driven training for medical image classification (arXiv: 2605.06727)
   136|  - Guided auto-encoder for high-dimensional medical image compression
   137|  - Surrogate-driven training for non-differentiable quantum measurements
   138|  - **Activation**: cold atom reservoir computing, medical imaging, surrogate training, neutral atom
   139|
   140|### Quantum Kernel Advantage over Classical Collapse in Medical Foundation Model Embeddings
   141|- [[quantum-kernel-advantage-medical]] - QSVM with frozen medical foundation model embeddings (MedSigLIP-448, RAD-DINO) shows quantum kernel advantage on MIMIC-CXR (arXiv: 2604.24597)
   142|  - Two-tier fair comparison framework for QSVM vs classical SVM
   143|  - Medical foundation model embeddings with quantum kernels
   144|  - **Activation**: quantum kernel advantage, QSVM, medical foundation model, MIMIC-CXR
   145|
   146|## 2026-05-27 - Medicine + Quantum ML (Cron Job - Wednesday)
   147|
   148|### Deterministic Mapping of Topological Phases via NARX Neural Networks
   149|- [[narx-topological-phase-mapping]] - NARX neural network discovers deterministic functional identities between topological invariants and critical parameters in quantum systems, achieving MSE of 10^{-27} (arXiv: 2605.27300)
   150|  - NARX achieves numerical-precision MSE at delay d=1, revealing exact functional identity between winding number and critical measurement strength
   151|  - Complexity paradox: NARX accuracy collapses at higher delays (d=4), confirming non-trivial high-precision dynamic mapping rather than trivial pattern learning
   152|  - **Activation**: NARX neural network, topological phase transition, winding number, quantum phase mapping, autoregressive exogenous, deterministic identity discovery
   153|
   154|### Leveraging Quantum-Based Architectures for Robust Diagnostics (QCNN)
   155|- [[quantum-medical-diagnostics]] - Hybrid classical-quantum QCNN framework for multi-class medical image classification using pretrained encoders + angle/amplitude encoding + QCNN (arXiv: 2511.12386)
   156|  - Achieves 99% accuracy on kidney CT, 97% on cervical cell, 99% on brain tumor classification
   157|  - Fewer trainable parameters than classical CNNs with superior precision, recall, and F1
   158|  - **Activation**: QCNN medical, quantum convolutional neural network, medical image classification, hybrid quantum classical diagnostics, pretrained encoder quantum
   159|
   160|### HQNN with Multi-Head Attention for Breast Cancer Thermographic Classification
   161|- [[hqnn-breast-cancer-thermographic]] - HQNN combining 4-qubit variational circuit with strongly entangling layers and classical CNN with multi-head attention for breast cancer thermography (arXiv: 2604.16953)
   162|  - Quantum-aware feature encoding via parameterized quantum circuits with multi-head attention
   163|  - Classical attention mechanisms for feature fusion, superior convergence dynamics
   164|  - **Activation**: HQNN thermography, breast cancer classification, quantum-classical attention, variational quantum circuit, multi-head quantum encoding
   165|
   166|