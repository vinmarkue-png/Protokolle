import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

filename1 = r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\EPR\DPPH\A)\01_DPPH_start_0p01mod_20db_5gain_471701.txt"
filename2 = r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\EPR\DPPH\A)\02_DPPH_start_0p01mod_20db_3_10-1gain_471701.txt"

df1 = pd.read_csv(filename1, delimiter='\t', decimal='.', header=None)
df2 = pd.read_csv(filename2, delimiter='\t', decimal='.', header=None)

x1, y1 = df1.iloc[:, 0], df1.iloc[:, 1]
x2, y2 = df2.iloc[:, 0], df2.iloc[:, 1]

# Normierung
# y1 = y1 / np.max(np.abs(y1))
# y2 = y2 / np.max(np.abs(y2))

plt.plot(x1, y1, label=r"DPPH start: Gain $5\cdot10^{0}$", lw=1.5)
plt.plot(x2, y2, label=r"DPPH opt: Gain $3\cdot10^{1}$", lw=1.5, color="black")

plt.tick_params(direction='in', top=True, right=True)
plt.xlim(337, 339)

plt.xlabel(r"$B$ / mT")
plt.ylabel(r"Absorption / a.u.")
plt.legend(fontsize=8)

plt.tight_layout()

plot_filename = os.path.splitext(filename1)[0] + '.pdf'
plt.savefig(plot_filename)
# plt.show()
