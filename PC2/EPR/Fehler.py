import numpy as np

# Konstanten (SI-Einheiten)
mu_B = 9.2741e-24      # J/T
h = 6.6261e-34         # J*s

# Fehler der Messgrößen (anpassen!)
delta_nu_GHz = 0.021   # GHz
delta_B0_mT = 0.005      # mT

# Umrechnung in SI
delta_nu = delta_nu_GHz * 1e9      # Hz
delta_B0 = delta_B0_mT * 1e-3      # T

# Proben: Name, Frequenz [GHz], Magnetfeld [mT]
samples = [
    # ("DPPH", 9.43402, 336.656),
    # # ("Probe 2", 9.50, 338.2),
    # ("Galvinoxyl", 9.4554, 336.25),
    ("Cu", 9.44, 317.2),
]

print(f"{'Probe':<10} {'g':>10} {'Δg':>12}")

for name, nu_GHz, B0_mT in samples:
    # Umrechnung in SI
    nu = nu_GHz * 1e9     # Hz
    B0 = B0_mT * 1e-3     # T

    # g-Faktor
    g = h * nu / (mu_B * B0)

    # Fehlerfortpflanzung
    delta_g = (
        abs(h / (mu_B * B0)) * delta_nu
        + abs(h * nu / (mu_B * B0**2)) * delta_B0
    )

    # Ausgabe mit Komma als Dezimaltrennzeichen
    g_str = f"{g:0.5f}".replace(".", ",")
    delta_g_str = f"{delta_g:0.5f}".replace(".", ",")

    print(f"{name:<10} {g_str:>10} {delta_g_str:>10}")
