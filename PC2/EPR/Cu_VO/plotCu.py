import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.signal import find_peaks

# 1. Pfad-Eingabe (Lass die Klammer leer, du tippst den Pfad unten im Terminal ein!)
raw_pfad = input("Cu_VO/Cu_320B_60sweep_mT_0p4mod_20db_5_10-1_4711839.txt").strip()

# Bereinigung für Windows
pfad = raw_pfad.replace('"', '').replace("'", "").replace('\\', '/')

if not os.path.exists(pfad):
    print(f"FEHLER: Datei nicht gefunden unter: {pfad}")
else:
    try:
        # 2. Daten laden
        x, y = np.loadtxt(pfad, unpack=True)

        # 3. Maxima UND Minima finden (Wichtig für ESR!)
        # Hochpunkte
        peaks_pos, _ = find_peaks(y, prominence=5000) 
        # Tiefpunkte (indem wir y invertieren)
        peaks_neg, _ = find_peaks(-y, prominence=5000) 

        # 4. Plot erstellen
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, color='black', label='ESR-Spektrum', linewidth=1)
        
        # Markierungen zeichnen
        plt.plot(x[peaks_pos], y[peaks_pos], "ro", label='Maxima')
        plt.plot(x[peaks_neg], y[peaks_neg], "bx", label='Minima')

        # 5. Achsenbeschriftung (wie in deinem PDF)
        plt.xlabel('B / mT')
        plt.ylabel('Absorption')
        plt.title(f"Analyse: {os.path.basename(pfad)}")
        plt.grid(True, linestyle=':')
        plt.legend()
        
        # Verhindert abgeschnittene Ränder
        plt.tight_layout()

        plt.show()

    except Exception as e:
        print(f"Fehler beim Lesen: {e}")