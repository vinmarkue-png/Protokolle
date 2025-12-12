import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# --- Datei korrekt einlesen ---
data = pd.read_csv(
    r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\MDGE\Simulationen\A05\default\nvt-out.dat",
    skiprows=4,
    sep=r"\s+",
    engine="python",
    names=["temp", "pressure", "time"]
)

# --- erzwinge echte Zahlen ---
data["temp"] = pd.to_numeric(data["temp"], errors="coerce")
data["pressure"] = pd.to_numeric(data["pressure"], errors="coerce")

# --- entferne nicht-numerische Zeilen ---
data = data.dropna()

# Daten extrahieren
temp = data["temp"]
pressure = data["pressure"]

# --- glätten ---
pressure_smooth = pressure.rolling(window=5, center=True).mean()

# --- plot ---
plt.figure(figsize=(8,5))

plt.plot(temp, pressure_smooth, label="Simulation", linewidth=2)

plt.xlabel("Reduced temperature")
plt.ylabel("Reduced pressure")
plt.ylim(bottom=0)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
