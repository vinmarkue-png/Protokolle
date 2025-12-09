import numpy as np
import matplotlib.pyplot as plt


# Funktion zur Berechnung der gedämpften harmonischen Schwingung
def damped_oscillation(t, A, gamma, omega):
    """
    Berechnet die Auslenkung einer gedämpften harmonischen Schwingung zur Zeit t.
    
    x(t) = A * e^(-gamma * t) * cos(omega * t)
    """
    return A * np.exp(-gamma * t) * np.cos(omega * t)


