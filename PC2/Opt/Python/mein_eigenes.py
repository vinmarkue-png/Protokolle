import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import os

# ===========================
# BENUTZER-EINSTELLUNGEN
# ===========================
# Die ERSTE Datei sollte deine Referenz (Blank/Lampe) sein!
filenames = [
    r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\lampe\Lamp2.txt",
    r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\Chloro\chloro_1.txt", 
    r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\Chloro\chloro_2.txt",
    r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\Chloro\chloro_3.txt",
    r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\Chloro\chloro_4.txt",
    r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\Chloro\chloro_5.txt",
]

f = 0.925
deltaAlpha = 0.593
theta = 0.222

# ===========================
# AUSWERTUNG
# ===========================
plt.figure(figsize=(10, 6))

# 1. Referenz laden
ref_df = pd.read_csv(filenames[0], delimiter=' ', header=None)
x_ref = ref_df[0].values
y_ref = ref_df[1].values

def get_lambda(steps):
    faktor = (1.8 / (20*16) * np.pi/180) * f
    Alpha = -faktor * steps + deltaAlpha
    return (np.sin(Alpha + theta) + np.sin(Alpha)) / 1200 * 1e6

lambda_ref = get_lambda(x_ref)

# 2. Schleife über die Proben (ab Index 1)
for i in range(1, len(filenames)):
    df = pd.read_csv(filenames[i], delimiter=' ', header=None)
    x_sample = df[0].values
    y_sample = df[1].values
    
    # Interpolation auf Referenz-Achse (falls nötig)
    interp_func = interp1d(x_sample, y_sample, kind='linear', fill_value='extrapolate')
    y_sample_adj = interp_func(x_ref)
    
    # BERECHNUNG
    transmission = y_sample_adj / y_ref
    # Absorption A = -log10(T)
    # clip verhindert Fehler bei negativen Werten oder 0
    absorption = -np.log10(np.clip(transmission, 1e-5, 1)) 
    
    label = os.path.basename(filenames[i]).replace(".txt", "")
    plt.plot(lambda_ref, absorption, label=label, linewidth=0.8)

# Styling
plt.xlabel(r"Wavelength $\lambda$ / nm")
plt.ylabel("Absorption $A$")
plt.legend(frameon=False)
plt.show()