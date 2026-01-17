import numpy as np
import matplotlib.pyplot as plt
import os

# =========================
# DATEIPFAD
# =========================
dateipfad = r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\NMR\A05\Paramagnetisch\Carr-Purcell\cpmg_pci_20Loops_20msi.txt"

# =========================
# TXT EINLESEN
# =========================
daten = np.loadtxt(dateipfad, skiprows=6)

zeit = daten[:, 0]        # Zeit / ms
signal = daten[:, 1]      # Intensität / %

# =====================================================
# 1. PLOT: ROHDATEN (ohne Fit, Linienverbindung)
# =====================================================
plt.figure(figsize=(8, 5))
plt.plot(zeit, signal, '-k')

plt.xlabel("τ / ms")
plt.ylabel("Intensität / %")

plt.tight_layout()
plot_raw = os.path.splitext(dateipfad)[0] + "_T2.pdf"
plt.savefig(plot_raw)
plt.close()

# =====================================================
# 2. BESTIMMUNG DER SPINECHOAMPLITUDEN (20 Echos)
# =====================================================
anzahl_echos = 20
punkte_pro_echo = len(signal) // anzahl_echos

echo_amplituden = []
echo_zeiten = []

for i in range(anzahl_echos):
    start = i * punkte_pro_echo
    ende = (i + 1) * punkte_pro_echo

    segment_signal = signal[start:ende]
    segment_zeit = zeit[start:ende]

    idx_max = np.argmax(np.abs(segment_signal))
    echo_amplituden.append(abs(segment_signal[idx_max]))
    echo_zeiten.append(segment_zeit[idx_max])

echo_amplituden = np.array(echo_amplituden)
echo_zeiten = np.array(echo_zeiten)

# =========================
# LaTeX-TABELLE AUSGEBEN
# =========================
print("\nLaTeX-Tabelle der Spinechoamplituden:\n")
print(r"\begin{tabular}{c c}")
print(r"\hline")
print(r"$2n\tau$ / ms & $M(2n\tau)$ \\")
print(r"\hline")

for t, a in zip(echo_zeiten, echo_amplituden):
    print(f"{t:.1f} & {a:.3f} \\\\")

print(r"\hline")
print(r"\end{tabular}")

# =====================================================
# 3. ln-DARSTELLUNG + LINEARER FIT (Gl. 6.29)
# =====================================================
# Gl. 6.29: ln M(t) = ln M0 - t / T2

maske = echo_amplituden > 0
t_ln = echo_zeiten[maske]
ln_M = np.log(echo_amplituden[maske])

# LINEARER FIT + FEHLER
(m, c), cov = np.polyfit(t_ln, ln_M, 1, cov=True)
m_err = np.sqrt(cov[0, 0])

# T2 + FEHLER
T2 = -1 / m
T2_err = m_err / (m**2)

print(f"Steigung m = ({m:.4e} ± {m_err:.1e}) ms^-1")
print(f"T2 = ({T2:.2f} ± {T2_err:.2f}) ms")


# Fit-Gerade
t_fit = np.linspace(min(t_ln), max(t_ln), 200)
ln_fit = m * t_fit + c

# =========================
# PLOT: ln M(2nτ) + FIT
# =========================
plt.figure(figsize=(8, 5))

plt.scatter(
    t_ln,
    ln_M,
    label="Berechnete ln-Werte der Spinechoamplituden"
)

plt.plot(
    t_fit,
    ln_fit,
    'r',
    label=f"Fit: $y$ = {m:.4e}$~\\mathrm{{ms}}^{{-1}}\\cdot t$ + {c:.4f}"
)

plt.xlabel(r"$2n\tau$ / ms")
plt.ylabel(r"$\ln M(2n\tau)$")

plt.legend()
plt.tight_layout()

plot_ln = os.path.splitext(dateipfad)[0] + "_T2_ln_Fit.pdf"
plt.savefig(plot_ln)
plt.close()
