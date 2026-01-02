import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Symbole und Funktion
t, A, gamma, omega = sp.symbols('t A gamma omega')
dA, dgamma, domega = sp.symbols('dA dgamma domega')

x = A * sp.exp(-gamma * t) * sp.cos(omega * t)
dx = (dA * sp.Abs(sp.diff(x, A)) +
    dgamma * sp.Abs(sp.diff(x, gamma)) +
    domega * sp.Abs(sp.diff(x, omega)))

x_func = sp.lambdify((t, A, gamma, omega), x, "numpy")
dx_func = sp.lambdify((t, A, gamma, omega, dA, dgamma, domega), dx, "numpy")

# Zeitvektor
t_num = np.linspace(0, 20, 400)

# Fall 1: dA = 1.0
x_num = x_func(t_num, 10, 0.1, 2.0) # numerische x-Werte
dx_num = dx_func(t_num, 10, 0.1, 2.0, 1.0, 0.0, 0.0)

plt.plot(t_num, x_num)
plt.fill_between(t_num, x_num - dx_num, x_num + dx_num, alpha=0.4)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend(["x(t)", "Unsicherheitsbereich"])
plt.show()

# Fall 2: domega = 0.2
dx_num = dx_func(t_num, 10, 0.1, 2.0, 0.0, 0.0, 0.2)

plt.plot(t_num, x_num)
plt.fill_between(t_num, x_num - dx_num, x_num + dx_num, alpha=0.4)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend(["x(t)", "Unsicherheitsbereich"])
plt.show()
