import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ---------- Konstanten ----------
k_B = 1.380649e-23        # J/K
epsilon_0 = 1.643e-21    # J
sigma_0 = 3.41e-10       # m
TORR_TO_PA = 133.322     # Pa

# ---------- Funktion zum Einlesen ----------
def load_data(filepath):
    data = pd.read_csv(
        filepath,
        skiprows=4,
        sep=r"\s+",
        engine="python",
        names=["T_red", "p_red", "time"]
    )

    data["T_red"] = pd.to_numeric(data["T_red"], errors="coerce")
    data["p_red"] = pd.to_numeric(data["p_red"], errors="coerce")
    data = data.dropna()

    return data["T_red"], data["p_red"]

# ---------- Simulation laden ----------
Tred1, pred1 = load_data(
    r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\MDGE\Simulationen\A05\default\nvt-out.dat"
)

Tred2, pred2 = load_data(
    r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\MDGE\Simulationen\A05\default\nvt-out_task_2.dat"
)

# ---------- Umrechnung Simulation ----------
T1 = (Tred1 * epsilon_0) / k_B
p1 = (pred1 * epsilon_0) / sigma_0**3

T2 = (Tred2 * epsilon_0) / k_B
p2 = (pred2 * epsilon_0) / sigma_0**3

# ---------- Glätten ----------
p1_smooth = p1.rolling(window=5, center=True).mean()
p2_smooth = p2.rolling(window=5, center=True).mean()

# ---------- Experimentelle Daten ----------
p_Ar_torr = np.array([
    11.5509548,
    13.2010912,
    13.2010912,
    13.5761222,
    16.6513764,
    18.4515252,
    20.1016616,
    21.5267794,
    22.9518972,
    24.9770646,
    25.9521452,
    28.877387,
    31.2775854,
    33.6027776,
    36.0779822,
    38.9282178,
    42.378503,
    45.3037448,
    48.6040176,
    51.9042904,
    55.7296066,
    59.8549476,
    63.6052576,
    67.0555428,
    71.7809334,
    76.0562868,
    80.7816774,
    85.9571052,
    90.9825206,
    96.2329546,
    101.633401,
    105.9837606,
    112.2842814,
    117.759734,
    123.9852486,
    129.5357074,
    135.9862406,
    142.2867614,
    143.0368234,
    154.512772,
    161.0383114,
    168.0888942,
    175.514508,
    182.4150784,
    189.1656364,
    196.141213
])


T_exp = np.array([
63.89062847,64.10482618,64.08974303,64.22433386,64.80692335,
65.26290943,65.59169318,65.89177789,66.22824378,66.57730357,
66.91888403,67.26085624,67.60980641,67.95541053,68.29116432,
68.66140261,68.99795305,69.35779649,69.70121289,70.03147128,
70.37851284,70.71407153,71.02805856,71.34521301,71.66350826,
71.99535851,72.30215343,72.65635316,72.92107702,73.20878693,
73.51254007,73.78489222,74.07409912,74.36416769,74.63647841,
74.90495329,75.16874062,75.43109442,75.68809945,75.9323749,
76.17218705,76.40775272,76.68142119,76.91261558,77.14943448,
77.39063173
])

# Torr → Pa
p_exp = p_Ar_torr * TORR_TO_PA

# ---------- Plot ----------
plt.figure(figsize=(8,5))

plt.plot(T1, p1_smooth, label="T2p1", linewidth=2)
plt.plot(T2, p2_smooth, label="T2p2", linewidth=2, color="tab:red")

plt.scatter(T_exp, p_exp, label="experimental data", s=20, marker="x", color="tab:green")

plt.xlabel("Temperature $T$ [K]")
plt.ylabel("Pressure $p$ [Pa]")
plt.ylim(bottom=0)
plt.grid(False)
plt.legend()
plt.tight_layout()
plt.show()
