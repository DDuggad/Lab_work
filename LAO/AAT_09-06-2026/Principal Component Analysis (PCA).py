import numpy as np
from sklearn.decomposition import PCA

def compute_pca():
    # Sample Data (Rows = Samples, Cols = Features)
    X = np.array([
        [2, 3],
        [3, 4],
        [4, 5],
        [5, 6]
    ], dtype=float)

    # Initialize PCA to keep 2 components
    pca = PCA(n_components=2)
    
    # Fit the model and transform the data
    principal_components = pca.fit_transform(X)

    print("--- Principal Component Analysis (PCA) ---")
    print("Original Data (X):\n", X)
    print("\nTransformed Data (Principal Components):\n", np.round(principal_components, 4))
    
    # How much variance (information) is retained by each component
    print("\nExplained Variance (Eigenvalues of Covariance Matrix):")
    print(np.round(pca.explained_variance_, 4))
    
    print("\nExplained Variance Ratio (% of total variance):")
    print(np.round(pca.explained_variance_ratio_ * 100, 2), "%")

if __name__ == "__main__":
    compute_pca()
