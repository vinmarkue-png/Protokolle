import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import os

# --- Konfiguration & Parameter ---
base_path = r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\Opt\Holm"
turns_list = ["1.5-turns", "3-turns", "6-turns"]

# Konstanten für die Wellenlängenberechnung
f = 0.925
deltaAlpha = 0.59
theta = 0.222
faktor = (1.8 / (20 * 16) * np.pi / 180) * f
xmin, xmax = 400, 800

# Plot vorbereiten
plt.figure(figsize=(10, 6))

# --- Loop über die verschiedenen Messungen ---
for turns in turns_list:
    # Dateipfade generieren
    # Annahme: Background heißt "HNO3_X-turns.txt", Probe "HNO3_Holm_X-turns.txt"
    p_bg = os.path.join(base_path, f"HNO3_{turns}.txt")
    p_sample = os.path.join(base_path, f"HNO3_Holm_{turns}.txt")
    
    try:
        # Daten einlesen
        data_bg = pd.read_csv(p_bg, delimiter=' ', decimal='.', header=None)
        data_sample = pd.read_csv(p_sample, delimiter=' ', decimal='.', header=None)
        
        x_bg, y_bg = data_bg[0], data_bg[1]
        x_sample, y_sample = data_sample[0], data_sample[1]

        # Interpolation (falls die x-Werte nicht exakt übereinstimmen)
        f_interp = interp1d(x_sample, y_sample, kind='linear', bounds_error=False, fill_value='extrapolate')
        y_sample_aligned = f_interp(x_bg)

        # Wellenlänge berechnen (basierend auf x_bg)
        alpha = -faktor * x_bg + deltaAlpha
        lambdas = (np.sin(alpha + theta) + np.sin(alpha)) / 1200 * 1e6

        # Absorption berechnen: A = -log10(I_sample / I_background)
        # Wir nutzen np.where um Division durch Null oder Log-Fehler zu vermeiden
        transmission = y_sample_aligned / y_bg
        absorption = -np.log10(transmission)

        # In den gemeinsamen Plot einfügen
        plt.plot(lambdas, absorption, label=f'Holm {turns}')

        # Optional: Als CSV speichern (wie im Originalcode)
        output_df = pd.DataFrame({"Lambda": lambdas, "Absorption": absorption})
        output_filename = os.path.join(base_path, f"HNO3_Holm_{turns}_abs.csv")
        output_df.to_csv(output_filename, index=False)
        
    except FileNotFoundError:
        print(f"Datei für {turns} wurde nicht gefunden. Pfad geprüft? {p_sample}")

# --- Plot-Styling ---
plt.xlabel('Lambda / nm')
plt.ylabel('Absorption / a.u')
plt.xlim(xmin, xmax)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.tight_layout()
plt.savefig(os.path.join(base_path, "Holm_spektrum.pdf"), dpi=300)