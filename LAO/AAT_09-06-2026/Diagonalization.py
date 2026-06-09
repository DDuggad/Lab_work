import numpy as np

def diagonalize():
    # Using a symmetric matrix for Orthogonal Diagonalization
    A = np.array([
        [4, 1],
        [1, 3]
    ], dtype=float)

    # Get Eigenvalues and Eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Matrix P (Eigenvectors) and Matrix D (Diagonal of Eigenvalues)
    P = eigenvectors
    D = np.diag(eigenvalues)
    P_inv = np.linalg.inv(P)

    print("--- Standard Diagonalization (A = P D P^-1) ---")
    print("Matrix P:\n", np.round(P, 4))
    print("\nMatrix D:\n", np.round(D, 4))
    print("\nVerification (P @ D @ P^-1):\n", np.round(P @ D @ P_inv, 4))

    # Because A is symmetric, P is orthogonal (P^-1 == P^T)
    # Therefore, we can Orthogonally Diagonalize: A = Q D Q^T
    Q = P
    Q_T = Q.T
    
    print("\n--- Orthogonal Diagonalization (A = Q D Q^T) ---")
    print("Orthogonal Matrix Q:\n", np.round(Q, 4))
    print("\nVerification (Q @ D @ Q^T):\n", np.round(Q @ D @ Q_T, 4))

if __name__ == "__main__":
    diagonalize()
