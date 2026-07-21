"""
Utility functions for CSFS implementation.
"""

import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering


def find_optimal_clusters(X, max_clusters=10, method='silhouette'):
    """
    Find optimal number of clusters using various validation methods.
    
    Parameters:
    X: Feature matrix (n_samples, n_features)
    max_clusters: Maximum number of clusters to consider
    method: Validation method ('silhouette', 'elbow', 'gap')
    
    Returns:
    optimal_n_clusters: Suggested number of clusters
    scores: List of scores for each number of clusters tried
    """
    n_features = X.shape[1]
    if n_features < 2:
        return 1, [1.0]
    
    # Transpose to cluster features (not samples)
    X_features = X.T
    
    # Standardize features for clustering
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_features)
    
    if method == 'silhouette':
        scores = []
        # Need at least 2 clusters for silhouette score
        for n_clusters in range(2, min(max_clusters + 1, n_features)):
            clusterer = AgglomerativeClustering(n_clusters=n_clusters)
            cluster_labels = clusterer.fit_predict(X_scaled)
            if len(set(cluster_labels)) > 1:  # Need at least 2 different labels
                silhouette_avg = silhouette_score(X_scaled, cluster_labels)
                scores.append(silhouette_avg)
            else:
                scores.append(-1)  # Invalid score
        
        if scores:
            best_idx = np.argmax(np.array(scores))
            return best_idx + 2, scores  # +2 because we started from 2
        else:
            return 2, scores
    
    elif method == 'elbow':
        # Simplified elbow method using inertia
        from sklearn.cluster import KMeans
        inertias = []
        for n_clusters in range(1, min(max_clusters + 1, n_features)):
            kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
            kmeans.fit(X_scaled)
            inertias.append(kmeans.inertia_)
        
        # Find elbow point (simplified: point of maximum curvature)
        if len(inertias) >= 3:
            diffs = np.diff(inertias)
            ratios = diffs[:-1] / diffs[1:]
            # Find point where ratio change is maximal
            if len(ratios) >= 2:
                ratio_changes = np.diff(ratios)
                if len(ratio_changes) > 0:
                    elbow_idx = np.argmax(np.abs(ratio_changes)) + 2  # +2 for offset
                    return min(elbow_idx, max_clusters), inertias
        return min(3, max_clusters), inertias  # Default fallback
    
    else:
        # Default to square root of features
        return int(np.sqrt(n_features)), []


def evaluate_feature_subset(X, y, estimator, feature_indices, cv=5, 
                           scoring='neg_mean_squared_error'):
    """
    Evaluate performance of a feature subset using cross-validation.
    
    Parameters:
    X: Feature matrix
    y: Target vector
    estimator: Sklearn-compatible estimator
    feature_indices: List of feature indices to evaluate
    cv: Number of cross-validation folds
    scoring: Scoring metric
    
    Returns:
    mean_score: Average cross-validation score
    """
    if len(feature_indices) == 0:
        return -np.inf
    
    X_subset = X[:, feature_indices]
    
    try:
        scores = cross_val_score(estimator, X_subset, y, cv=cv, scoring=scoring)
        return np.mean(scores)
    except:
        # Fallback to train/test split
        from sklearn.model_selection import train_test_split
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                X_subset, y, test_size=0.2, random_state=42
            )
            estimator.fit(X_train, y_train)
            score = estimator.score(X_test, y_test)
            
            # Convert to negative MSE if needed
            if scoring == 'neg_mean_squared_error':
                y_pred = estimator.predict(X_test)
                mse = np.mean((y_test - y_pred) ** 2)
                return -mse
            return score
        except:
            return -np.inf


def get_feature_names_from_indices(feature_names, indices):
    """
    Get feature names corresponding to indices.
    
    Parameters:
    feature_names: List of feature names
    indices: List of feature indices
    
    Returns:
    names: List of feature names for the given indices
    """
    if feature_names is None:
        return [f"feature_{i}" for i in indices]
    return [feature_names[i] for i in indices]


def print_csfs_summary(selected_features, feature_names=None, 
                      selected_X=None, y=None, estimator=None):
    """
    Print a summary of the CSFS results.
    
    Parameters:
    selected_features: List of selected feature indices
    feature_names: Optional list of feature names
    selected_X: Optional selected feature matrix
    y: Optional target vector (for performance evaluation)
    estimator: Optional estimator (for performance evaluation)
    """
    print("=== Cluster-based Sequential Feature Selection (CSFS) Summary ===")
    print(f"Number of selected features: {len(selected_features)}")
    
    names = get_feature_names_from_indices(feature_names, selected_features)
    print(f"Selected features: {names}")
    
    if selected_X is not None:
        print(f"Selected feature matrix shape: {selected_X.shape}")
    
    if y is not None and estimator is not None and selected_X.size > 0:
        score = evaluate_feature_subset(selected_X, y, estimator, 
                                      list(range(selected_X.shape[1])))
        print(f"Cross-validation score: {score:.4f}")
    
    print("=" * 60)


if __name__ == "__main__":
    print("CSFS Utilities module loaded")
    print("Use evaluate_feature_subset(), find_optimal_clusters(), etc.")