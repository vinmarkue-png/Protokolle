import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# =========================
# DATEIPFADE
# =========================
excel_pfad = r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\NMR\A05\Paramagnetisch\T1 Inversion\NMR_data.xlsx"

# =========================
# EXCEL EINLESEN (Sheet 1)
# =========================
df = pd.read_excel(excel_pfad, sheet_name=0)

tau = df.iloc[:, 0].values      # τ / ms
signal = df.iloc[:, 1].values  # Intensität / %

# =========================
# PLOT 1: T1-MESSUNG
# =========================
plt.figure(figsize=(8, 5))
plt.scatter(tau, signal, marker='o', color='black')

plt.xlabel("τ / ms")
plt.ylabel("Intensität / %")

plt.tight_layout()

plot1_name = os.path.splitext(excel_pfad)[0] + "_T1.pdf"
plt.savefig(plot1_name)
plt.close()

# ======================================================
# AB HIER: KORRIGIERTE ln-BERECHNUNG + FIT (Gl. 6.26)
# ======================================================

# Gleichgewichtsmagnetisierung
M0 = abs(signal[0])

# GEMESSENE Magnetisierung verwenden!
Mz = signal

# Argument des Logarithmus
argument = (M0 - Mz) / (2 * M0)

# Nur physikalisch sinnvolle Werte (Argument > 0)
maske = argument > 0

tau_ln = tau[maske]
ln_wert = np.log(argument[maske])

# =========================
# LINEARER FIT (nur linearer Bereich)
# =========================
fit_grenze = 140.5  # ms, wie im Plot
fit_maske = tau_ln <= fit_grenze

# LINEARER FIT + FEHLER
(m, c), cov = np.polyfit(
    tau_ln[fit_maske],
    ln_wert[fit_maske],
    1,
    cov=True
)

m_err = np.sqrt(cov[0, 0])

# T1 + FEHLER
T1 = -1 / m
T1_err = m_err / (m**2)

print(f"Steigung m = ({m:.4e} ± {m_err:.1e}) ms^-1")
print(f"T1 = ({T1:.2f} ± {T1_err:.2f}) ms")

# Fit-Gerade
tau_fit = np.linspace(min(tau_ln[fit_maske]),
                      max(tau_ln[fit_maske]), 200)
ln_fit = m * tau_fit + c

# =========================
# PLOT 2: ln-PLOT + FIT
# =========================
plt.figure(figsize=(8, 5))

plt.scatter(tau_ln, ln_wert, label="Berechnete ln-Werte der Magnetisierung")

plt.plot(
    tau_fit,
    ln_fit,
    'r',
    label=f"Fit (bis {fit_grenze} ms): $y$ = {m:.4e}$~\\mathrm{{ms}}^{{-1}}\\cdot \\tau$ + {c:.4f}"
)

plt.xlabel("τ / ms")
plt.ylabel(r"$\ln\left(\frac{M_0 - M_z(\tau)}{2M_0}\right)$")

plt.legend()
plt.tight_layout()

plot2_name = os.path.splitext(excel_pfad)[0] + "_ln_Fit.pdf"
plt.savefig(plot2_name)
plt.close()
