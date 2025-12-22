import EPRsim.EPRsim as sim
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# --- Simulation Setup ---
P = sim.Parameters()
P.Range = [334, 337]
P.mwFreq = 9.4067
P.g = 2.003
P.Nucs = 'H,H'
P.n = [1, 4]
P.A = [15, 3] 
P.lw = [0.05]
P.motion = 'fast'
B0, spc, flag = sim.simulate(P)

# --- Daten laden ---
filename4 = "C:/Studium/5. Semester/AC II lab/Protokolle/PC2/EPR/Galvinoxyl/24_Galvin_bisschen_O2_337B_5sweep_0p03mod_10db_5_10-1_4727720.txt"
df4 = pd.read_csv(filename4, delimiter='\t', decimal='.', header=None)

x4, y4 = df4.iloc[:, 0], df4.iloc[:, 1]
x4c = x4 - 1.258

# --- SKALIERUNG (NEU) ---
# Berechne die Amplitude (Max - Min) für Simulation und Experiment
sim_amplitude = np.max(spc) - np.min(spc)
exp_amplitude = np.max(y4) - np.min(y4)

# Berechne den Skalierungsfaktor, um Exp an Sim anzupassen
scale_factor = sim_amplitude / exp_amplitude

# Skalierte y-Werte
y4_scaled = y4 * scale_factor

# Optional: Offset-Korrektur (Zentrierung auf 0), falls die Basislinie verschoben ist
# y4_scaled = y4_scaled - np.mean(y4_scaled) 
# ------------------------

# --- Plotting ---
plt.figure(figsize=(10, 6))

# Simulation plotten
plt.plot(B0, spc, color='red', label='Simulation', linewidth=1.5)

# Skalierte experimentelle Daten plotten (y4_scaled statt y4)
plt.plot(x4c, y4_scaled, label=r"Galvinoxyl + DPPH: entgast", lw=0.8, color="black", alpha=0.8)

plt.xlabel(r'$B$ / mT') 
plt.ylabel(r'Absorption / a.u.')

# Optische Verbesserungen
# plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')
plt.legend()
plt.tight_layout() # Verhindert abgeschnittene Labels

plt.savefig('Gal_Sim_Vgl.pdf')
plt.show()