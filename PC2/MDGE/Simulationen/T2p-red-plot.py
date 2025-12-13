import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ---------- Funktion zum Einlesen ----------
def load_data(filepath):
    data = pd.read_csv(
        filepath,
        skiprows=4,
        sep=r"\s+",
        engine="python",
        names=["temp", "pressure", "time"]
    )
    data["temp"] = pd.to_numeric(data["temp"], errors="coerce")
    data["pressure"] = pd.to_numeric(data["pressure"], errors="coerce")
    data = data.dropna()
    return data["temp"], data["pressure"]

# ---------- Datensätze laden ----------
temp1, pressure1 = load_data(
    r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\MDGE\Simulationen\A05\default\nvt-out.dat"
)

temp2, pressure2 = load_data(
    r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\MDGE\Simulationen\A05\default\nvt-out_task_2.dat"
)

# ---------- Glätten ----------
pressure1_smooth = pressure1.rolling(window=5, center=True).mean()
pressure2_smooth = pressure2.rolling(window=5, center=True).mean()

# ---------- Plot ----------
plt.figure(figsize=(8,5))

plt.plot(temp1, pressure1_smooth, label="T2p1", linewidth=2)
plt.plot(temp2, pressure2_smooth, label="T2p2", linewidth=2, color="tab:red")

plt.xlabel("Reduced temperature")
plt.ylabel("Reduced pressure")
plt.ylim(bottom=0)
plt.grid(False)
plt.legend()
plt.tight_layout()
plt.show()
