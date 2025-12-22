import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks  # Wichtig für die Peak-Suche

# Dateipfade
filename4 = "C:/Studium/5. Semester/AC II lab/Protokolle/PC2/EPR/Galvinoxyl/24_Galvin_bisschen_O2_337B_5sweep_0p03mod_10db_5_10-1_4727720.txt"

# Daten laden
df4 = pd.read_csv(filename4, delimiter='\t', decimal='.', header=None)

# x und y zuweisen
x4, y4 = df4.iloc[:, 0], df4.iloc[:, 1]

# x-Achsen Korrektur
x4c = x4 - 1.258

# --- TEIL ZUR BERECHNUNG DER KOPPLUNGSKONSTANTEN ---

# 1. Peaks finden
# 'prominence': Filtert Rauschen raus. Hier: mind. 10% der maximalen Signalhöhe.
# 'distance': Mindestabstand zwischen Peaks (in Datenpunkten), verhindert, dass Rauschen als Doppelpeak erkannt wird.
peaks_indices, properties = find_peaks(y4, prominence=np.max(y4)*0.4, distance=5)

# Die B-Feld Werte an den Peak-Positionen
peak_fields = x4c.iloc[peaks_indices].values

# 2. Abstände berechnen (Differenz zwischen benachbarten Peaks)
coupling_constants = np.diff(peak_fields)

# 3. Ausgabe in der Konsole
print("-" * 40)
print("ERGEBNISSE DER KOPPLUNGSKONSTANTEN")
print("-" * 40)
print(f"Gefundene Peaks bei B (mT): \n{peak_fields}")
print("-" * 40)
print(f"Abstände zwischen den Peaks (Kopplungskonstanten in mT): \n{coupling_constants}")
print("-" * 40)
if len(coupling_constants) > 0:
    print(f"Mittelwert der Kopplungskonstante a_iso (mT): {np.mean(coupling_constants):.4f}")
    print(f"Standardabweichung (mT): {np.std(coupling_constants):.4f}")
else:
    print("Keine Peaks für Abstandsberechnung gefunden. Passe 'prominence' an.")
print("-" * 40)

# --- PLOTTING ---

plt.figure(figsize=(8, 5)) # Größe explizit setzen für bessere Lesbarkeit

plt.plot(x4c, y4, label=r"Galvinoxyl + DPPH: entgast", lw=0.8, color="black")

# Markiere die gefundenen Peaks im Plot (rote Kreuze)
plt.plot(peak_fields, y4.iloc[peaks_indices], "x", color="red", label="Peaks zur Berechnung", markersize=8, markeredgewidth=2)

plt.tick_params(direction='in', top=True, right=True)
plt.xlim(334.5, 338)
# plt.ylim(5000, -5000) # Optional: Auskommentiert lassen oder anpassen, wenn Peaks abgeschnitten werden

plt.xlabel(r"$B$ / mT")
plt.ylabel(r"Absorption / a.u.")
plt.legend(fontsize=10)
plt.title(f"a_iso ≈ {np.mean(coupling_constants):.3f} mT (Mittelwert)", fontsize=10)

plt.tight_layout()

plt.savefig('Galvinoxyl_dg_mit_Kopplung.pdf')
plt.show()