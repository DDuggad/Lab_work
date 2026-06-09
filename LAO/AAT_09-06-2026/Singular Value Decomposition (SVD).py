import numpy as np

def compute_svd():
    A = np.array([
        [4, 1],
        [1, 3]
    ], dtype=float)

    # Compute SVD directly via NumPy
    U, Singular_Values, VT = np.linalg.svd(A)

    # Construct the Sigma matrix from the 1D array of singular values
    Sigma = np.zeros(A.shape)
    np.fill_diagonal(Sigma, Singular_Values)

    print("--- Singular Value Decomposition (A = U \u03A3 V^T) ---")
    print("Matrix A:\n", A)
    print("\nMatrix U (Left Singular):\n", np.round(U, 4))
    print("\nMatrix \u03A3 (Singular Values):\n", np.round(Sigma, 4))
    print("\nMatrix V^T (Right Singular Transposed):\n", np.round(VT, 4))

    # Verification
    A_reconstructed = U @ Sigma @ VT
    print("\nVerification (U @ \u03A3 @ V^T):\n", np.round(A_reconstructed, 4))

if __name__ == "__main__":
    compute_svd()
