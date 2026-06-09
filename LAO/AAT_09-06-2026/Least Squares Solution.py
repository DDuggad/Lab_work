import numpy as np

def least_squares():
    A = np.array([
        [1, 1],
        [1, 2],
        [1, 3]
    ], dtype=float)
    
    B = np.array([
        [1],
        [2],
        [2]
    ], dtype=float)

    # Compute A^T * A and A^T * B
    A_T = A.T
    ATA = A_T @ A
    ATB = A_T @ B

    # Solve X = (A^T A)^-1 * (A^T B)
    X = np.linalg.inv(ATA) @ ATB

    # Calculate Error = B - AX
    residual = B - (A @ X)
    error_norm = np.linalg.norm(residual)

    print("--- Least Squares Solution ---")
    print("Matrix A:\n", A)
    print("\nVector B:\n", B)
    print("\nSolution X:\n", X)
    print("\nResidual Vector (B - AX):\n", residual)
    print("\nLeast Square Error (Norm):\n", round(error_norm, 4))

if __name__ == "__main__":
    least_squares()
