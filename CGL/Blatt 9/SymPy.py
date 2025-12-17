import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
#--------Definition-----------
# Definition der Symbole
t = sp.Symbol('t', real=True)
A = sp.Symbol('A', real=True)
lam = sp.Symbol('lambda', positive=True, real=True)
omega = sp.Symbol('omega', positive=True, real=True)

# Definition der Funktion
f = A * sp.exp(-lam * t) * sp.cos(omega * t)

print("--- Symbolische Analyse ---")
print(f"Funktion f(t): {f}")

#------Analysis------
# Erste Ableitung
f_prime = sp.diff(f, t)
print(f"Ableitung f'(t): {f_prime}")

# Unbestimmtes Integral
f_int = sp.integrate(f, t)
print(f"Stammfunktion F(t): {f_int}")

# Grenzwert für t -> unendlich
limit_inf = sp.limit(f, t, sp.oo)
print(f"Grenzwert für t->oo: {limit_inf}")

# ---Numerische Konvertierung---
# Erstellen von Python-Funktionen die mit NumPy-Arrays arbeiten können und definieren der Variablen
func_f = sp.lambdify((t, A, lam, omega), f, modules='numpy')
func_f_prime = sp.lambdify((t, A, lam, omega), f_prime, modules='numpy')

# ---Visualisierung---
# Festlegung der Parameterwerte
A_val = 2
lam_val = 0.5
omega_val = 3

# Festlegung des Zeitbereichs
t_vals = np.linspace(0, 10, 500)

# Berechnung der y-Werte durch Aufruf der erstellten Funktionen
y_vals = func_f(t_vals, A_val, lam_val, omega_val)
y_prime_vals = func_f_prime(t_vals, A_val, lam_val, omega_val)

plt.figure(figsize=(10, 6))

plt.plot(t_vals, y_vals, label=r'$f(t) = A \cdot e^{-\lambda t} \cdot \cos(\omega t)$', color='blue')
plt.plot(t_vals, y_prime_vals, label=r"$f'(t)$ (Ableitung)", color='orange', linestyle='--')


plt.xlabel('Zeit t')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.savefig('Sympy.pdf')
plt.show()