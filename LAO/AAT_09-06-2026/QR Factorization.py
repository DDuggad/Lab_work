import numpy as np

def qr_solve():
    A = np.array([
        [1, 2],
        [3, 4]
    ], dtype=float)
    
    B = np.array([
        [5],
        [6]
    ], dtype=float)

    # 1. QR Factorization
    Q, R = np.linalg.qr(A)
    
    # 2. Solve RX = Q^T * B
    QT_B = Q.T @ B
    X = np.linalg.solve(R, QT_B)

    print("--- QR Factorization ---")
    print("Matrix Q (Orthogonal):\n", np.round(Q, 4))
    print("\nMatrix R (Upper Triangular):\n", np.round(R, 4))
    
    print("\n--- Solution ---")
    print("Solution X:\n", np.round(X, 4))
    
    print("\n--- Verification (A @ X) ---")
    print(np.round(A @ X, 4), " == \n", B)

if __name__ == "__main__":
    qr_solve()
