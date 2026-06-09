import numpy as np
import matplotlib.pyplot as plt

def curve_fitting():
    # Given Data
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    y = np.array([2, 5, 7, 10, 15], dtype=float)

    # 1. Straight Line Fit (Degree 1)
    # polyfit returns coefficients in descending order (a, b)
    line_coeffs = np.polyfit(x, y, 1)
    a_line, b_line = line_coeffs
    y_line_pred = (a_line * x) + b_line

    print("--- Straight Line Fit ---")
    print(f"Equation: y = {a_line:.4f}x + {b_line:.4f}")

    # 2. Parabola Fit (Degree 2)
    # Returns (a, b, c)
    para_coeffs = np.polyfit(x, y, 2)
    a_para, b_para, c_para = para_coeffs
    y_para_pred = (a_para * x**2) + (b_para * x) + c_para

    print("\n--- Parabola Fit ---")
    print(f"Equation: y = {a_para:.4f}x\u00b2 + {b_para:.4f}x + {c_para:.4f}")

    # Plotting (Optional but helpful for visualization)
    plt.scatter(x, y, color='red', label="Original Data")
    plt.plot(x, y_line_pred, label="Line Fit", linestyle='--')
    plt.plot(x, y_para_pred, label="Parabola Fit")
    plt.legend()
    plt.title("Least Squares Curve Fitting")
    plt.show()

if __name__ == "__main__":
    curve_fitting()
