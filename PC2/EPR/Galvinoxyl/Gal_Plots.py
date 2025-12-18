import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

filename1 = "C:/Studium/5. Semester/AC II lab/Protokolle/PC2/EPR/Galvinoxyl/21_Galvin_O2_337B_5sweep_0p1mod_10db_5_10-1_4727720.txt"
filename2 = "C:/Studium/5. Semester/AC II lab/Protokolle/PC2/EPR/Galvinoxyl/22_Galvin_bisschen_O2_337B_5sweep_0p03mod_10db_5_10-1_4727720.txt"
filename3 = "C:/Studium/5. Semester/AC II lab/Protokolle/PC2/EPR/Galvinoxyl/23_Galvin_bisschen_O2_337B_5sweep_0p03mod_10db_5_10-1_4727720.txt"
filename4 = "C:/Studium/5. Semester/AC II lab/Protokolle/PC2/EPR/Galvinoxyl/24_Galvin_bisschen_O2_337B_5sweep_0p03mod_10db_5_10-1_4727720.txt"
filename5 = "C:/Studium/5. Semester/AC II lab/Protokolle/PC2/EPR/Galvinoxyl/25_Galvin_bisschen_O2_337B_5sweep_0p03mod_10db_5_10-1_4727720.txt"

df1 = pd.read_csv(filename1, delimiter='\t', decimal='.', header=None)
df2 = pd.read_csv(filename2, delimiter='\t', decimal='.', header=None)
df3 = pd.read_csv(filename3, delimiter='\t', decimal='.', header=None)
df4 = pd.read_csv(filename4, delimiter='\t', decimal='.', header=None)
df5 = pd.read_csv(filename5, delimiter='\t', decimal='.', header=None)


x1, y1 = df1.iloc[:, 0], df1.iloc[:, 1]
x2, y2 = df2.iloc[:, 0], df2.iloc[:, 1]
x3, y3 = df3.iloc[:, 0], df3.iloc[:, 1]
x4, y4 = df4.iloc[:, 0], df4.iloc[:, 1]
x5, y5 = df5.iloc[:, 0], df5.iloc[:, 1]

x1c = x1 - 1.258
x2c = x2 - 1.258
x3c = x3 - 1.258
x4c = x4 - 1.258
x5c = x5 - 1.258
# Normierung
# y1 = y1 / np.max(np.abs(y1))
# y2 = y2 / np.max(np.abs(y2))

plt.plot(x1c, y1, label=r"Galvinoxyl + DPPH: mit O$_2$", lw=0.5, color = "red")
plt.plot(x2c, y2, label=r"Galvinoxyl + DPPH: leicht entgast", lw=0.5, color="yellow")
plt.plot(x3c, y3, label=r"Galvinoxyl + DPPH: stärker entgast", lw=0.5, color = "green")
plt.plot(x4c, y4, label=r"Galvinoxyl + DPPH: entgast", lw=0.5, color="blue")
plt.plot(x5c, y5, label=r"Galvinoxyl + DPPH: entgast", lw=0.5, color = "magenta")

plt.tick_params(direction='in', top=True, right=True)
plt.xlim(334.0, 338)
plt.ylim(8000, -8000)

plt.xlabel(r"$B$ / mT")
plt.ylabel(r"Absorption / a.u.")
plt.legend(fontsize=8)

plt.tight_layout()


plt.savefig('Galvinoxyl.pdf')
plt.show()
