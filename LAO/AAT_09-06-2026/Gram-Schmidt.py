import numpy as np

def gram_schmidt():
    # Given Vectors (Rows)
    vectors = np.array([
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1]
    ], dtype=float)

    orthogonal_basis = []
    
    # 1. Construct Orthogonal Basis
    for v in vectors:
        w = v.copy()
        for u in orthogonal_basis:
            # Projection of v onto u: (v.u / u.u) * u
            proj = (np.dot(v, u) / np.dot(u, u)) * u
            w = w - proj
        orthogonal_basis.append(w)
        
    orthogonal_basis = np.array(orthogonal_basis)

    # 2. Construct Orthonormal Basis (Divide by magnitude)
    orthonormal_basis = np.array([u / np.linalg.norm(u) for u in orthogonal_basis])

    print("--- Given Vectors ---")
    print(vectors)
    
    print("\n--- Orthogonal Basis ---")
    for i, vec in enumerate(orthogonal_basis, 1):
        print(f"u{i} = {np.round(vec, 4)}")
        
    print("\n--- Orthonormal Basis ---")
    for i, vec in enumerate(orthonormal_basis, 1):
        print(f"e{i} = {np.round(vec, 4)}")

if __name__ == "__main__":
    gram_schmidt()
