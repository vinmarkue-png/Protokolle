import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import cm

# Ordner mit den Dateien
folder = r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\EPR\DPPH\C)"

# Dateinummern
file_numbers = [21, 22, 23, 24, 25, 26, 27]
modul = [1, 2, 4, 8 , 16 , 32 , 64]
spectra_centers = []
# Colormap: lila → blau → grün → orange
colors = cm.viridis(np.linspace(0.95, 0.0, len(file_numbers)))

plt.figure(figsize=(6, 4))

for i, num in enumerate(file_numbers):
    filename = f"{num}_DPPH_start_0p{modul[i]:02d}mod_30db_5gain_471701.txt"
    filepath = os.path.join(folder, filename)

    df = pd.read_csv(filepath, delimiter='\t', decimal='.', header=None)

    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    xc = x - 1.258
    # Normierung
    # y = y / np.max(np.abs(y))

    # Extrempunkte finden (Maximum und Minimum)
    x_max = xc[y.idxmax()]
    x_min = xc[y.idxmin()]

    # Spektrenzentrum = Mittelpunkt zwischen Max und Min
    center = (x_max + x_min) / 2
    spectra_centers.append(center)


    plt.plot(
        xc, y,
        color=colors[i],
        lw=1.5,
        label=f"modulation {modul[i]} mT"
    )

for i, c in enumerate(spectra_centers):
    print(f"Spektrum {file_numbers[i]}: Zentrum bei {c:.3f} mT")

plt.tick_params(direction='in', top=True, right=True)
plt.xlim(335.75, 337.75)

plt.xlabel(r"$B$ / mT")
plt.ylabel("Absorption / a.u.")
plt.legend(fontsize=8)
plt.tight_layout()

plt.savefig(os.path.join(folder, "DPPH_Modulation.pdf"))
# plt.show()