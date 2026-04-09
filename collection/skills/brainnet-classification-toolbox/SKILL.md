---
name: brainnet-classification-toolbox
description: MATLAB toolbox for brain network construction and classification. Includes static/dynamic connectivity methods, connectome feature extraction, dimensionality reduction, parameter optimization, and interpretable machine learning for diagnosis.
---

# BrainNetClass: Brain Network Classification Toolbox

## Description

A MATLAB-based, open-source, cross-platform toolbox for brain network construction and individualized classification. Provides various network construction methods (including state-of-the-art dynamic connectivity), connectome feature extraction, dimensionality reduction, parameter optimization, and interpretable results for cognitive and clinical neuroscientists without requiring neuroimage computing or machine learning expertise.

**Source:** arXiv:1906.09908v1
**Utility:** 0.90
**GitHub:** https://github.com/zzstefan/BrainNetClass

## Activation Keywords

- brain network toolbox
- functional connectivity classification
- brain network construction
- connectome feature extraction
- fMRI classification toolbox
- brain network diagnosis
- dynamic functional connectivity
- BrainNetClass

## Core Concepts

### 1. Brain Network Construction Methods

**Static Connectivity:**
- Pearson's correlation (most common)
- Partial correlation
- Mutual information
- Coherence

**Dynamic Connectivity:**
- Sliding window correlation
- Time-frequency analysis
- Change point detection
- State-based connectivity

**Advanced Methods:**
- High-order functional connectivity
- Sparse inverse covariance
- Hypergraph connectivity
- Multiplex networks

### 2. Connectome Feature Extraction

**Network Measures:**
| Category | Features |
|----------|----------|
| Nodal | Degree, betweenness, efficiency, clustering coefficient |
| Global | Small-worldness, modularity, network efficiency |
| Edge | Connection strength, path length |
| Motif | Triangles, feedforward loops |

**Feature Selection:**
- Filter methods (correlation, mutual information)
- Wrapper methods (recursive feature elimination)
- Embedded methods (LASSO, random forest)

### 3. Classification Pipeline

```
fMRI data → Network construction → Feature extraction → Dimensionality reduction → Classification → Interpretation
```

**Classifiers:**
- SVM (Support Vector Machine)
- Random Forest
- LASSO
- Neural Networks

**Validation:**
- Cross-validation (k-fold, LOO)
- Nested cross-validation
- Independent test set

### 4. Parameter Optimization

**Grid Search:**
- Network construction parameters
- Classification hyperparameters
- Feature selection thresholds

**Optimization Goals:**
- Maximize accuracy
- Balance sensitivity/specificity
- Minimize overfitting

### 5. Interpretable Results

**Output Formats:**
- Feature importance rankings
- Brain region contributions
- Network visualization
- Classification performance metrics

**Visualization:**
- Brain network graphs
- Confusion matrices
- ROC curves
- Feature distributions

## Step-by-Step Instructions

### 1. Installation and Setup

```matlab
% Download BrainNetClass from GitHub
% https://github.com/zzstefan/BrainNetClass

% Add to MATLAB path
addpath('/path/to/BrainNetClass');

% Initialize toolbox
BrainNetClass_init;
```

### 2. Data Preparation

```matlab
% Input format: 4D fMRI data (x, y, z, time)
% ROI parcellation required

% Load fMRI data
fmri_data = load('subject1_fmri.mat');

% Load ROI mask
roi_mask = load('aal_mask.nii');

% Extract ROI time series
[roi_signals, roi_labels] = extract_roi_timeseries(fmri_data, roi_mask);
```

### 3. Network Construction

```matlab
% Static Pearson correlation
fc_static = corr(roi_signals');

% Dynamic sliding window correlation
window_size = 30; % TRs
step_size = 1;
fc_dynamic = sliding_window_fc(roi_signals, window_size, step_size);

% High-order functional connectivity
fc_highorder = high_order_fc(roi_signals);

% Sparse inverse covariance (graphical LASSO)
fc_sparse = glasso_fc(roi_signals, 0.1);
```

### 4. Feature Extraction

```matlab
% Extract nodal features
nodal_features = extract_nodal_measures(fc_static);

% Features:
% - Degree
% - Betweenness centrality
% - Clustering coefficient
% - Local efficiency
% - Participation coefficient

% Extract global features
global_features = extract_global_measures(fc_static);

% Features:
% - Global efficiency
% - Modularity
% - Small-worldness
% - Transitivity

% Combine features
all_features = [nodal_features, global_features];
```

### 5. Feature Selection and Dimensionality Reduction

```matlab
% Filter-based selection (correlation with labels)
[selected_features, selected_indices] = correlation_filter(...
    all_features, labels, 0.3);

% LASSO-based selection
[lasso_features, lasso_indices] = lasso_selection(...
    all_features, labels, 'CV', 5);

% PCA dimensionality reduction
[pca_features, pca_coeff] = pca(all_features);
pca_features = pca_features(:, 1:10); % Keep top 10 components
```

### 6. Classification

```matlab
% SVM classification
svm_model = fitcsvm(pca_features, labels, ...
    'KernelFunction', 'rbf', ...
    'Standardize', true, ...
    'CrossVal', 'on', ...
    'KFold', 10);

% Performance metrics
accuracy = 1 - kfoldLoss(svm_model);
disp(['SVM Accuracy: ', num2str(accuracy)]);

% Random Forest
rf_model = TreeBagger(100, pca_features, labels, ...
    'Method', 'classification', ...
    'OOBPrediction', 'on');

% OOB accuracy
rf_accuracy = 1 - mean(strcmp(rf_model.OOBPredictedClass, labels));
disp(['RF Accuracy: ', num2str(rf_accuracy)]);
```

### 7. Parameter Optimization

```matlab
% Grid search for optimal parameters
param_grid = struct(...
    'window_size', [20, 30, 40], ...
    'sparsity', [0.1, 0.2, 0.3], ...
    'n_components', [5, 10, 15]);

best_accuracy = 0;
best_params = struct();

for ws = param_grid.window_size
    for sp = param_grid.sparsity
        for nc = param_grid.n_components
            % Build network
            fc = sliding_window_fc(roi_signals, ws, 1);
            
            % Extract features
            feats = extract_all_measures(fc);
            
            % Reduce dimensions
            [pca_feats, ~] = pca(feats);
            pca_feats = pca_feats(:, 1:nc);
            
            % Cross-validate
            model = fitcsvm(pca_feats, labels, 'CrossVal', 'on', 'KFold', 5);
            acc = 1 - kfoldLoss(model);
            
            if acc > best_accuracy
                best_accuracy = acc;
                best_params = struct('window_size', ws, 'sparsity', sp, 'n_components', nc);
            end
        end
    end
end

disp(['Best accuracy: ', num2str(best_accuracy)]);
disp(best_params);
```

### 8. Result Interpretation

```matlab
% Feature importance from Random Forest
importance = rf_model.OOBPermutedVarDeltaError;
[sorted_importance, sorted_idx] = sort(importance, 'descend');

% Top contributing features
top_n = 10;
disp('Top contributing features:');
for i = 1:top_n
    disp([roi_labels{sorted_idx(i)}, ': ', num2str(sorted_importance(i))]);
end

% Visualize feature importance
figure;
bar(sorted_importance(1:top_n));
set(gca, 'XTickLabel', roi_labels(sorted_idx(1:top_n)));
xtickangle(45);
xlabel('Brain Region');
ylabel('Importance');
title('Top Contributing Brain Regions');
```

### 9. Complete Pipeline

```matlab
function results = BrainNetClass_pipeline(fmri_data, labels, params)
    % Complete brain network classification pipeline
    %
    % Inputs:
    %   fmri_data: cell array of fMRI data (subjects x 1)
    %   labels: classification labels (subjects x 1)
    %   params: parameters struct
    %
    % Outputs:
    %   results: classification results
    
    n_subjects = length(fmri_data);
    n_rois = size(fmri_data{1}, 2);
    
    % Step 1: Network construction
    networks = cell(n_subjects, 1);
    for i = 1:n_subjects
        if params.method == 'static'
            networks{i} = corr(fmri_data{i}');
        elseif params.method == 'dynamic'
            networks{i} = sliding_window_fc(fmri_data{i}, params.window_size, 1);
        end
    end
    
    % Step 2: Feature extraction
    features = zeros(n_subjects, n_rois * 4 + 5); % nodal + global
    for i = 1:n_subjects
        nodal = extract_nodal_measures(networks{i});
        global = extract_global_measures(networks{i});
        features(i, :) = [nodal(:)', global(:)'];
    end
    
    % Step 3: Feature selection
    [selected, ~] = lasso_selection(features, labels, 'CV', 5);
    
    % Step 4: Dimensionality reduction
    [pca_feats, ~] = pca(selected);
    pca_feats = pca_feats(:, 1:params.n_components);
    
    % Step 5: Classification
    model = fitcsvm(pca_feats, labels, ...
        'KernelFunction', params.kernel, ...
        'CrossVal', 'on', ...
        'KFold', params.cv_folds);
    
    % Step 6: Results
    results.accuracy = 1 - kfoldLoss(model);
    results.sensitivity = compute_sensitivity(model, labels);
    results.specificity = compute_specificity(model, labels);
    results.auc = compute_auc(model, labels);
    results.model = model;
end
```

## Tools Used

- `MATLAB` - Primary platform
- `BrainNetClass` - Open-source toolbox
- `exec` - Run MATLAB scripts
- `read` - Load data files

## Example Use Cases

### 1. Alzheimer's Disease Classification

```matlab
% Load AD vs CN fMRI data
ad_data = load('ad_fmri_data.mat');
cn_data = load('cn_fmri_data.mat');

% Combine and label
all_data = [ad_data.subjects, cn_data.subjects];
labels = [ones(length(ad_data.subjects), 1); ...
          zeros(length(cn_data.subjects), 1)];

% Run pipeline
params.method = 'dynamic';
params.window_size = 30;
params.n_components = 10;
params.kernel = 'rbf';
params.cv_folds = 10;

results = BrainNetClass_pipeline(all_data, labels, params);

fprintf('Accuracy: %.2f%%\n', results.accuracy * 100);
fprintf('AUC: %.3f\n', results.auc);
```

### 2. ADHD vs Control

```matlab
% ADHD classification
adhd_data = load('adhd_fmri.mat');

% Static correlation network
fc = corr(adhd_data.roi_signals');

% Extract features
features = extract_all_measures(fc);

% Classify
model = fitcsvm(features, adhd_data.labels, 'CrossVal', 'on');
accuracy = 1 - kfoldLoss(model);
```

### 3. Multi-Class Classification

```matlab
% CN vs MCI vs AD
data = load('multiclass_fmri.mat');
labels = data.labels; % 1=CN, 2=MCI, 3=AD

% Use multi-class SVM
model = fitcecoc(features, labels, 'CrossVal', 'on');
accuracy = 1 - kfoldLoss(model);

% Confusion matrix
[predicted, scores] = kfoldPredict(model);
confusionchart(labels, predicted);
```

## Network Construction Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| Pearson correlation | Static linear dependence | Default, baseline |
| Partial correlation | Direct connections | Remove confounding |
| Sliding window | Dynamic connectivity | Time-varying analysis |
| Graphical LASSO | Sparse inverse covariance | Remove indirect connections |
| High-order FC | Complex interactions | Capture higher-order dependencies |
| Hypergraph | Multi-way relationships | Complex brain interactions |

## Classification Metrics

```matlab
% Compute all metrics
function metrics = compute_all_metrics(predicted, actual)
    TP = sum(predicted == 1 & actual == 1);
    TN = sum(predicted == 0 & actual == 0);
    FP = sum(predicted == 1 & actual == 0);
    FN = sum(predicted == 0 & actual == 1);
    
    metrics.accuracy = (TP + TN) / (TP + TN + FP + FN);
    metrics.sensitivity = TP / (TP + FN);
    metrics.specificity = TN / (TN + FP);
    metrics.precision = TP / (TP + FP);
    metrics.f1 = 2 * metrics.precision * metrics.sensitivity / ...
                 (metrics.precision + metrics.sensitivity);
end
```

## Related Skills

- `functional-connectome-fingerprint` - Individual identification
- `drl-gnn-brain-network` - Deep learning on brain networks
- `hermes-brain-connectivity` - HERMES toolbox

## References

- Zhou, Z. et al. (2019). "Brain Network Construction and Classification Toolbox (BrainNetClass)" arXiv:1906.09908v1 [q-bio.NC]
- GitHub: https://github.com/zzstefan/BrainNetClass

---

**Created:** 2026-03-30 01:05
**Author:** Aerial (from arXiv:1906.09908v1)