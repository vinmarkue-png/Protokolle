import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

filename1 = r"C:\Studium\5. Semester\AC II lab\Protokolle\PC2\NMR\A05\Bildgebung\Probe 1\imaging1_pcii_0Grad.txt"
filename2 = r"C:\Studium\5. Semester\AC II lab\Protokolle\PC2\NMR\A05\Bildgebung\Probe 1\imaging1_pcii_90Grad.txt"

p1 = pd.read_csv(filename1, delimiter='\s+', decimal='.', skiprows=7, header=None)
p2 = pd.read_csv(filename2, delimiter='\s+', decimal='.', skiprows=7, header=None)

x1, y1 = p1.iloc[:,0], p1.iloc[:,1]
x2, y2 = p2.iloc[:,0], p2.iloc[:,1]

plt.plot(x1, y1, label=r"Wasser 0 Grad", lw=1.5)
plt.xlabel(r"Ort / m")
plt.ylabel(r"Intensität / a.u.")
# plt.legend(fontsize=8)

plt.tight_layout()


plt.savefig('Wasser0.pdf')
plt.show()

plt.plot(x2, y2, label=r"Wasser 90 Grad", lw=1.5)

plt.xlabel(r"Ort / m")
plt.ylabel(r"Intensität / a.u.")
# plt.legend(fontsize=8)

plt.tight_layout()


plt.savefig('Wasser90.pdf')
plt.show()