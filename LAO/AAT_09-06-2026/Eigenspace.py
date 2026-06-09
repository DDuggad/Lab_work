import sympy as sp

def find_eigenspace():
    # Define a 3x3 matrix
    A = sp.Matrix([
        [2, 1, 0],
        [1, 2, 0],
        [0, 0, 3]
    ])
    
    print("--- Matrix A ---")
    sp.pprint(A)

    # eigenvects() returns a list of tuples: (eigenvalue, algebraic_multiplicity, [eigenvectors])
    eigen_data = A.eigenvects()

    for data in eigen_data:
        eigenval = data[0]
        multiplicity = data[1]
        eigenvecs = data[2]
        
        print(f"\n=======================================")
        print(f"Eigenvalue (\u03BB) = {eigenval} (Multiplicity: {multiplicity})")
        print(f"=======================================")
        
        print("Basis for Eigenspace (Eigenvectors):")
        for vec in eigenvecs:
            sp.pprint(vec)
            
        print("\nEigenspan:")
        span_str = ", ".join([str(v.T) for v in eigenvecs])
        print(f"Span {{ {span_str} }}")

if __name__ == "__main__":
    find_eigenspace()
