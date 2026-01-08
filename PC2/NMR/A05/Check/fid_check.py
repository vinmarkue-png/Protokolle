import numpy as np
import matplotlib.pyplot as plt
import os

dateipfad = r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\NMR\A05\Check\fid_pcii.Daylicheck.txt"

# TXT-Datei einlesen
# Kommentarzeilen und Text werden automatisch übersprungen
daten = np.loadtxt(dateipfad, delimiter='\t', skiprows=7)

# Spalten trennen
zeit_ms = daten[:, 0]
intensitaet = daten[:, 1]

# Plot
plt.figure(figsize=(8, 5))
plt.plot(zeit_ms, intensitaet, linewidth=1)

# Achsenbeschriftung
plt.xlabel("Zeit / ms")
plt.ylabel("Intensität / %")

# plt.title("FID-Messung – Kernspinrelaxation von CuSO₄")

# Anzeigen
plt.tight_layout()
plot_filename = os.path.splitext(dateipfad)[0] + '.pdf'
plt.savefig(plot_filename)
