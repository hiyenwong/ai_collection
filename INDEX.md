     1|## 2026-05-27 - Neuroscience Research (Cron Job)
     2|
     3|### Maximum Entropy Networks for Context-Dependent Neural Computations
     4|- [[maximum-entropy-neural-connectivity]] - Normative maximum entropy principle for deriving neural connectivity from task constraints, independent of gradient descent — bridges theory with trained network structure (arXiv: 2605.25607)
     5|  - 核心要点 1: Connectivity = probability distribution over weights maximizing Shannon entropy under task constraints; yields unique "least-biased" solution consistent with function
     6|  - 核心要点 2: Maximum entropy connectivity matches gradient-descent-trained networks quantitatively across different learning regimes; context count drives phase transition from specialized to random populations
     7|  - **Activation**: maximum entropy, neural connectivity, context-dependent computation, normative neuroscience, information theory, brain network structure
     8|
     9|### Multi-Objective SNN Oscillation Optimization with NSGA-III
    10|- [[multi-objective-snn-oscillation]] - NSGA-III genetic algorithm for simultaneously optimizing recurrent SNN connectivity to match neural firing rates and oscillation frequencies — validated on brain organoids (arXiv: 2605.25224)
    11|  - 核心要点 1: Oscillation frequencies are more parameter-sensitive than firing rates; NSGA-III Pareto frontier reveals trade-offs between matching multiple neural targets simultaneously
    12|  - 核心要点 2: Framework generalizes to brain organoids and decision-making models with transient epoch dynamics; identified low-activity regime for decision states
    13|  - **Activation**: spiking neural network, NSGA-III, neural oscillation, Izhikevich neuron, brain organoid, multi-objective optimization, recurrent SNN
    14|
    15|## 2026-05-27 - Neuroscience Research (Cron Job)
    16|
    17|### Random Neural Networks & Neural Population Dimensionality
    18|- [[random-neural-network-dimensionality]] - DMFT framework quantitatively predicts low dimensionality in large-scale neural population recordings by incorporating finite measurement time and behavioral context variability (arXiv: 2605.26551)
    19|  - 核心要点 1: Dynamical Mean-Field Theory predicts covariance structure of randomly-connected networks; finite-T corrections align predictions with experiment
    20|  - 核心要点 2: Manifold orientation similarity across behavioral contexts is more sensitive to connectivity structure than dimensionality alone
    21|  - **Activation**: random neural network, neural population dimensionality, DMFT, neural manifold, connectivity inference
    22|
    23|### SRF: Similarity-Based Representation Factorization
    24|- [[srf-similarity-representation-factorization]] - General method for recovering low-dimensional, non-negative, interpretable dimensions from similarity matrices in brains, behavior, and AI (arXiv: 2605.26921)
    25|  - 核心要点 1: SRF factorizes pairwise similarity matrices S approx W*W^T with non-negativity constraints, yielding semantically interpretable additive dimensions
    26|  - 核心要点 2: 6-8 shared core dimensions found between human visual cortex and CNN layers; behavioral judgments emphasize unique semantic/functional axes
    27|  - **Activation**: representation factorization, brain-AI alignment, RSA interpretable, similarity embedding, core dimensions
    28|
    29|## 2026-05-27 - 医学 + 量子力学 (Cron Job - Wednesday)
    30|
    31|### Quantum Medical Patterns
    32|- [[quantum-medical-patterns]] - Reusable research patterns from quantum computing in medical/healthcare: hybrid architectures, quantum kernel methods, federated diagnosis, reservoir computing, QLIF forecasting (arXiv: multiple)
    33|- Core pattern 1: Hybrid quantum-classical clinical forecasting (GRU → VQC → classical decoder)
    34|- Core pattern 2: Quantum kernel medical imaging (foundation model → PCA → QSVM, 18/18 F1 wins)
    35|- Core pattern 3: Federated quantum medical diagnosis (privacy-preserving multi-hospital DR detection)
    36|- Core pattern 4: Cold-atom reservoir computing for medical imaging (auto-encoder + neutral-atom RC)
    37|- Core pattern 5: QLIF-CAST quantum spiking forecasting (15.4% lower MSE than classical LIF)
    38|- Design space exploration: encoding schemes, entanglement topologies, measurement strategies
    39|- **Activation**: quantum medical diagnosis, quantum healthcare AI, quantum clinical forecasting, hybrid quantum medical, quantum kernel medical imaging, federated quantum medical, quantum reservoir medical, 量子医疗诊断
    40|
    41|1|## 2026-05-27 - Neuroscience Research (Cron Job)
    42|2|
    43|3|### SpikeReg: Energy-Efficient 3D Deformable Medical Image Registration with Spiking Neural Networks
    44|4|- [[spikereg-snn-medical-registration]] - First SNN-based 3D deformable brain MRI registration matching ANN accuracy at 12.8% spike rate and 55.5× energy reduction (arXiv: 2605.25144)
    45|5|  - ANN-to-SNN conversion via layer-wise weight transfer + activation-percentile threshold calibration
    46|6|  - Surrogate gradient fine-tuning with local cross-correlation + diffusion regularization + spike-rate sparsity
    47|7|  - Negative findings: displacement distillation hurts, Dice-loss ANN teachers fail to transfer
    48|8|  - **Activation**: SNN medical imaging, neuromorphic registration, energy-efficient 3D perception, ANN-to-SNN conversion
    49|9|
    50|10|### Neuromorphic LiDAR-based Bird's Eye View Object Detection using Energy-efficient Spiking Neural Networks
    51|11|
    52|  - Learned spike encoding outperforms hand-crafted Poisson/latency/z-axis encoding strategies
    53|  - Two variants: membrane potential (max accuracy) and fully binary (neuromorphic hardware deployment)
    54|  - Block-wise energy analysis via SynOps/MAC proxy model
    55|  - **Activation**: neuromorphic autonomous driving, SNN object detection, LiDAR perception, spike encoding
    56|
    57|## 2026-05-27 - Medicine + Quantum (Cron Job - Wednesday 13:00)
    58|
    59|### HQNN Expressibility-Trainability Trade-off
    60|- [[hqnn-expressibility-trainability]] - Multi-objective NAS framework for HQNNs revealing classical components decouple trainability from PQC expressibility under full end-to-end training (arXiv: 2605.25768)
    61|  - Full end-to-end hybrid training can completely eliminate the expressibility-trainability trade-off
    62|  - Multi-objective NAS jointly optimizes expressibility, trainability, and task performance over combined classical-quantum design space
    63|  - Pure PQCs show only weak trade-off; hybrid architectures increasingly disrupt it
    64|  - **Activation**: HQNN expressibility trainability, hybrid quantum neural network optimization, quantum circuit barren plateau, neural architecture search quantum, PQC expressibility, quantum classical hybrid training
    65|
    66|## 2026-05-27 - Neuroscience Research (Cron Job)
    67|
    68|### Random Neural Networks Match Neural Population Dimensionality
    69|- [[random-neural-network-dimensionality]] - DMFT framework shows random connectivity explains low-dimensionality of large-scale neural recordings when finite measurement time and behavioral context variability are included (arXiv: 2605.26551)
    70|  - Non-monotonic dependence: dimensionality varies non-monotonically with external input strength
    71|  - Manifold orientation similarity across behavioral contexts is more sensitive to connectivity structure than dimensionality alone
    72|  - **Activation**: random neural network, neural population dimensionality, dynamical mean field theory, neural manifold, brain recording, connectivity inference, collective dynamics
    73|
    74|### Multi-Objective NSGA-III Optimisation of SNN Oscillatory Dynamics
    75|- [[multi-objective-snn-oscillation]] - NSGA-III co-optimises Izhikevich RSNN connectivity for both firing rates AND oscillation frequencies in spontaneous activity, brain organoids, and decision-making dynamics (arXiv: 2605.25224)
    76|  - Oscillation frequencies are more parameter-sensitive than firing rates — harder to pin precisely
    77|  - Successfully validated on brain organoid recordings and simulated decision-making RSNNs
    78|  - **Activation**: spiking neural network oscillation, NSGA-III, RSNN optimisation, Izhikevich neuron, brain organoid, neural oscillation fitting, multi-objective SNN
    79|
    80|## 2026-05-27 - Medicine + Quantum ML (Cron Job)
    81|
    82|### Quantum ML Medical Diagnosis Consolidated Skill
    83|- [[quantum-ml-medical-diagnosis]] - Comprehensive quantum ML methodologies for medical diagnosis and healthcare
    84|  - Core pattern 1: Hybrid quantum-classical feature fusion with temperature-scaled balancing (TSHF)
    85|  - Core pattern 2: Tensor-network compression enabling small-qubit quantum processing
    86|  - Core pattern 3: Privacy-aware federated quantum learning with MPC-secured aggregation
    87|  - Core pattern 4: Quantum transfer learning with fair benchmarking under NISQ constraints
    88|  - Core pattern 5: Quanvolutional neural networks for disease detection
    89|  - **Activation**: quantum medical diagnosis, quantum healthcare, federated quantum, quantum transfer learning, quantum neural network, medical imaging quantum, quanvolutional, HQNN
    90|
    91|## 2026-05-27 - Medicine + Quantum (Cron Job)
    92|
    93|### Design Space Exploration of Hybrid Quantum Neural Networks for Chronic Kidney Disease
    94|- [[hqnn-design-space-exploration]] - Systematic benchmarking of 625 HQNN configurations for CKD diagnosis, IQP+Ring entanglement achieves best accuracy-efficiency trade-off (arXiv: 2604.13608)
    95|  - Core finding: high performance does NOT require large parameter counts or complex circuits
    96|  - IQP encoding + Ring entanglement is optimal combo — captures pairwise correlations efficiently with minimal depth
    97|  - **Activation**: HQNN design space, quantum neural network architecture, hybrid quantum medical diagnosis, quantum encoding schemes, CKD classification, quantum circuit benchmarking
    98|
    99|### Analyzing Blood Cells with QML: Equilibrium Propagation and VQCs for Acute Myeloid Leukemia Detection
   100|- [[qml-equilibrium-propagation-medical]] - Energy-based backprop-free quantum training for blood cell classification, competitive under NISQ constraints (arXiv: 1808)
   101|
## 2026-05-27 - Medicine + Quantum Computing (Cron Job)

### Enhancing Blood Cells Classification using Hybrid Quantum Neural Networks
- [[hqnn-medical-classification]] - HQNN combines ResNet-50 backbone with variational quantum circuit for blood cell classification, improving macro F1 by 3.7% (arXiv: 2605.23324)
  - ResNet-50 → latent bottleneck → VQC architecture
  - 3-architecture comparison isolates quantum contribution
  - **Activation**: hybrid quantum neural network, HQNN, medical image classification, blood cell

### QT-PUF: Quantum Tunneling Leakage Based PUF for Implantable IoMT Devices
- [[quantum-medical-device-security]] - Gate-tunneling-leakage PUF leverages quantum effects for implantable healthcare device authentication (arXiv: 2605.22113)
  - Physical unclonable function using quantum tunneling
  - Device-level security for Internet of Medical Things
  - **Activation**: quantum PUF, IoMT security, implantable device authentication

### Multi-Class Neurological Disorder Prediction with Tensor Network Feature Engineering
- [[tensor-network-medical-imaging]] - PARAFAC CP tensor decomposition for neurological disorder diagnosis, inspired by quantum many-body physics (arXiv: 2605.17771)
  - Quantum-inspired tensor feature engineering for MRI
  - Ensemble classifier with tensor features
  - **Activation**: tensor network, PARAFAC CP, neurological disorder, MRI diagnosis

### Quantum Circuit Simulation of Compartmental Drug Dynamics
- [[quantum-pkpd-simulation]] - Reformulates PK/PD models as open quantum systems with 12-qubit variational circuits for drug dynamics simulation (arXiv: 2605.09691)
  - 12 qubits encoding 4 pharmacological compartments
  - Inter-compartmental transitions as controlled quantum gates
  - **Activation**: quantum PK/PD, drug dynamics, compartmental model, variational quantum circuit, pennylane

### FQPDR: Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy
- [[federated-quantum-medical-diagnosis]] - Federated QNN for microaneurysm detection combining FL with quantum neural networks for privacy-preserving medical imaging (arXiv: 2605.08324)
  - Federated quantum learning for medical image privacy
  - Early detection of low-contrast microaneurysm features
  - **Activation**: federated quantum neural network, diabetic retinopathy, privacy-preserving ML

### Medical Imaging Classification with Cold-Atom Reservoir Computing
- [[cold-atom-reservoir-computing-medical]] - Neutral-atom reservoir computing with guided auto-encoder and surrogate-driven training for medical image classification (arXiv: 2605.06727)
  - Guided auto-encoder for high-dimensional medical image compression
  - Surrogate-driven training for non-differentiable quantum measurements
  - **Activation**: cold atom reservoir computing, medical imaging, surrogate training, neutral atom

### Quantum Kernel Advantage over Classical Collapse in Medical Foundation Model Embeddings
- [[quantum-kernel-advantage-medical]] - QSVM with frozen medical foundation model embeddings (MedSigLIP-448, RAD-DINO) shows quantum kernel advantage on MIMIC-CXR (arXiv: 2604.24597)
  - Two-tier fair comparison framework for QSVM vs classical SVM
  - Medical foundation model embeddings with quantum kernels
  - **Activation**: quantum kernel advantage, QSVM, medical foundation model, MIMIC-CXR

