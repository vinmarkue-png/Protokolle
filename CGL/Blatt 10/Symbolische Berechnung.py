import sympy as sp
# Variablen und Fehler definieren
t, A, gamma, omega = sp.symbols('t A gamma omega')
dA, dgamma, domega = sp.symbols('dA dgamma domega')

# Funktion
x = A * sp.exp(-gamma * t) * sp.cos(omega * t)

# Partielle Ableitungen
dx_dA = sp.diff(x, A)
dx_dgamma = sp.diff(x, gamma)
dx_domega = sp.diff(x, omega)

# Fehlerfortpflanzung
dx = dA * sp.Abs(dx_dA) + dgamma * sp.Abs(dx_dgamma) + domega * sp.Abs(dx_domega)

# Lambdify für numerische Funktion
x_func = sp.lambdify((t, A, gamma, omega), x, "numpy")
dx_func = sp.lambdify((t, A, gamma, omega, dA, dgamma, domega), dx, "numpy")
