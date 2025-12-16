import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Daten mit delimiter , laden
try:
    data = np.loadtxt('C:/Studium/5. Semester/AC II lab/Protokolle/CGL/Blatt 9/data.txt', delimiter=',')
    x_data = data[:, 0]
    y_data = data[:, 1]
except Exception as e:
    print(f"Fehler: {e}")
    # Fallback simulation, damit der Code hier läuft
    x_data = np.linspace(0, 3, 300)
    y_data = 1.0 * np.exp(-0.8 * x_data) * np.sin(10 * x_data) + np.random.normal(0, 0.1, 300)


# Fitfunktion definieren
def damped_sine(x, amplitude, decay, omega, phase, offset):
    """
    amplitude: Start-Höhe der Welle
    decay:     Wie schnell die Welle abklingt (Dämpfung)
    omega:     Kreisfrequenz (bestimmt den Abstand der Wellenberge)
    phase:     Verschiebung nach links/rechts
    offset:    Verschiebung nach oben/unten
    """
    return amplitude * np.exp(-decay * x) * np.sin(omega * x + phase) + offset


p0_guess = [1.0, 0.8, 10.0, 0.0, 0.0]

try:
    params, covariance = curve_fit(damped_sine, x_data, y_data, p0=p0_guess)
    
    # Parameter ausgeben
    labels = ["Amplitude", "Decay (Dämpfung)", "Omega (Frequenz)", "Phase", "Offset"]
    print("Gefundene Parameter:")
    for label, val in zip(labels, params):
        print(f"  {label}: {val:.4f}")

    # Plotten
    plt.figure(figsize=(10, 6))
    
    # Messdaten
    plt.scatter(x_data, y_data, label='Messdaten', color='black', alpha=0.5, s=15)
    
    # Fit-Kurve
    x_fit = np.linspace(min(x_data), max(x_data), 1000)
    y_fit = damped_sine(x_fit, *params)
    
    plt.plot(x_fit, y_fit, 'r-', linewidth=2, label='Fit: Gedämpfte Schwingung')
    # Plot anzeigen und speichern
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('fit_plot.pdf')
    plt.show()

except RuntimeError:
    print("Der Fit hat nicht konvergiert. Versuche, die p0_guess Werte anzupassen.")