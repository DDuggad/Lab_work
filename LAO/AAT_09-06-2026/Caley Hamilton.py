import sympy as sp

def compute_a7_cayley_hamilton():
    # 1. Define the given Matrix A
    A = sp.Matrix([
        [5, 1, 3],
        [1, 3, 2],
        [3, 2, 1]
    ])
    
    print("--- Original Matrix A ---")
    sp.pprint(A)

    # 2. Find the Characteristic Polynomial P(lambda)
    lamda = sp.Symbol('lambda')
    char_poly = A.charpoly(lamda).as_expr()
    
    print("\n--- Characteristic Polynomial P(\u03BB) ---")
    sp.pprint(char_poly)
    
    # 3. Perform Polynomial Division (lambda^7 / P(lambda))
    # By Cayley-Hamilton, P(A) = 0. Therefore, A^7 will just be the remainder R(A)
    target_power = lamda**7
    remainder_poly = sp.rem(target_power, char_poly)
    
    print("\n--- Remainder R(\u03BB) after dividing \u03BB^7 by P(\u03BB) ---")
    sp.pprint(remainder_poly)

    # 4. Extract coefficients from the remainder: a*\lambda^2 + b*\lambda + c
    c2 = remainder_poly.coeff(lamda, 2)  # Coefficient for \lambda^2
    c1 = remainder_poly.coeff(lamda, 1)  # Coefficient for \lambda^1
    c0 = remainder_poly.subs(lamda, 0)   # Constant term

    # 5. Substitute Matrix A into the remainder equation: aA^2 + bA + cI
    I = sp.eye(3) # 3x3 Identity Matrix
    A_7_ch = (c2 * A**2) + (c1 * A) + (c0 * I)

    print("\n--- A^7 Computed using Cayley-Hamilton Theorem ---")
    sp.pprint(A_7_ch)

    # 6. Verification (Direct Matrix Exponentiation)
    A_7_direct = A**7
    print("\n--- Verification (Direct A^7 Computation) ---")
    sp.pprint(A_7_direct)

    if A_7_ch == A_7_direct:
        print("\n\u2705 Verification Successful: The Cayley-Hamilton result matches direct computation!")

if __name__ == "__main__":
    compute_a7_cayley_hamilton()
