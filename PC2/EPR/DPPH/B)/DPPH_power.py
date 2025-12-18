import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import cm

# Ordner mit den Dateien
folder = r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\EPR\DPPH\B)"

# Dateinummern
file_numbers = [11, 12, 13, 14, 15, 16]
mw_atten = [20, 17, 14, 11, 8, 5]
# Colormap: lila → blau → grün → orange
colors = cm.viridis(np.linspace(0.85, 0.0, len(file_numbers)))

plt.figure(figsize=(6, 4))

for i, num in enumerate(file_numbers):
    filename = f"{num}_DPPH_start_0p01mod_{mw_atten[i]}db_5gain_471701.txt"
    filepath = os.path.join(folder, filename)

    df = pd.read_csv(filepath, delimiter='\t', decimal='.', header=None)

    x = df.iloc[:, 0]
    y = df.iloc[:, 1]

    # Normierung
    # y = y / np.max(np.abs(y))

    plt.plot(
        x, y,
        color=colors[i],
        lw=1.5,
        label=f"attenuation {mw_atten[i]} dB"
    )

plt.tick_params(direction='in', top=True, right=True)
plt.xlim(337, 339)

plt.xlabel(r"$B$ / mT")
plt.ylabel("Absorption / a.u.")
plt.legend(fontsize=8)
plt.tight_layout()

plt.savefig(os.path.join(folder, "DPPH_MW_Attenuation.pdf"))
# plt.show()