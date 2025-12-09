import numpy as np
import matplotlib.pyplot as plt

# Funktion zur Berechnung der gedämpften harmonischen Schwingung
def damped_oscillation(t, A, gamma, omega):
    """
    Berechnet die Auslenkung einer gedämpften harmonischen Schwingung zur Zeit t.
    
    x(t) = A * e^(-gamma * t) * cos(omega * t)
    """
    return A * np.exp(-gamma * t) * np.cos(omega * t)

def main():
    A = 1.0
    gamma = 0.2
    omega = 2 * np.pi
    t = np.linspace(0, 10, 500)
    x = damped_oscillation(t, A, gamma, omega)

    plt.figure(figsize=(8,4))
    plt.plot(t, x, label="x(t)")
    plt.title("Gedämpfte harmonische Schwingung")
    plt.xlabel("Zeit t [s]")
    plt.ylabel("Auslenkung x(t)")
    plt.legend()
    # folder = r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\CGL\Blatt 8"
    plt.savefig("damped_oscillator.pdf")
    plt.show()
