import matplotlib.pyplot as plt
import numpy as np

# unpack=True trennt die Spalten direkt in x und y auf
x, y = np.loadtxt(r"C:\Users\49157\OneDrive\Dokumente\1. Uni Stuttgart\1.4. PC\1.4.6. PC II Lab\Protokolle\PC2\EPR\Cu_VO\VO_340B_100sweep_mT_0p2mod_30db_5_10-1_4711839.txt", unpack=True)

xkorr = x - 1.258

# 2. Plot erstellen
plt.plot(xkorr, y, color="black")

# 3. Beschriftungen (optional, aber sinnvoll)
plt.xlabel('$B$ / mT')
plt.ylabel('Absorption')

plt.tight_layout()

# 4. Anzeigen
plt.show()