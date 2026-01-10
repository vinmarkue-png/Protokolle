import numpy as np
import matplotlib.pyplot as plt

# Part 1
v = np.array([1.0, 1.0])
M = np.array([[1, 1], 
              [1, 0]])

ratios = []
n_values = range(50)

for i in range(50):
   current_ratio = v[0] / v[1]
   ratios.append(current_ratio)
   v = M @ v

plt.figure(figsize=(10, 6))
plt.plot(n_values, ratios, linestyle="none", marker="o", label="Numerisches Verhältnis $a_n/a_{n-1}$", markersize=4)


# Part 2
# Berechnung der Eigenwerte und Eigenvektoren
eigenvalues, eigenvectors = np.linalg.eig(M)

# Sortierung nach dem größten Eigenwert
idx = np.argsort(np.abs(eigenvalues))[::-1]
lambdas = eigenvalues[idx]

print(f"Die Eigenwerte von M sind: {lambdas}")
print(f"Dominanter Eigenwert (lambda_1): {lambdas[0]}")

# Approximation:
approx_ratios = [lambdas[0]] * len(n_values)

# Plotten der Approximation
plt.plot(n_values, approx_ratios, color='red', linestyle='--', label=f"Approximation ($\\lambda_1 \\approx {lambdas[0]:.4f}$)")


plt.title("Konvergenz des Verhältnisses von Fibonacci-Zahlen")
plt.xlabel("Iteration n")
plt.ylabel("Verhältnis $a_n / a_{n-1}$")
plt.legend()
plt.grid(True, which="both", linestyle='--', alpha=0.7)
plt.savefig('fibonacci.pdf')
plt.show()