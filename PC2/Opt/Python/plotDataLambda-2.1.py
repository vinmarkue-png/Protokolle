import numpy as np                   #Mathe und Arrays
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt      #Plotten



# ### read data from file
 # "./data/WATER.txt",
 # "./data/KMnO4-DILUTED.txt"
#
p1=r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\data\WATER.txt"
p2=r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\data\KMnO4-DILUTED.txt"
# p2=r"./data/KMnO4-HIGH-CONC.txt"


Data1=pd.read_csv(p1,skiprows=0,delimiter=' ',decimal='.',header=None)
Data2=pd.read_csv(p2,skiprows=0,delimiter=' ',decimal='.',header=None)
#
xData1 = Data1[0]
yData1 = Data1[1]
xData2 = Data2[0]
yData2 = Data2[1]
#
# Extrapolation
f2 = interp1d(xData2, yData2, kind='linear', bounds_error=False, fill_value='extrapolate')
yData2_interploiert = f2(xData1)   # calculates new y-values fitting to xData1
xData2 = xData1                # equals xData2 and xData1
yData2 = yData2_interploiert   # sets yData2 to the interpolated values


# Calculaton of the wavelength
f = 0.925
deltaAlpha = 0.59
# faktor = (1.8 / (20*16) * np.pi / 180) * f             # gear ratio 1/20; 16 microsteps per step
# Alpha = faktor * xData1 + deltaAlpha
# #Alpha=Alpha[::-1]
# theta = 0.222 
# Lambda = (np.sin(Alpha + theta) + np.sin(Alpha)) / 2400 * 1e6

faktor = (1.8 / (20*16) * np.pi / 180) * f             #Übersetzung 1/20; 16 Microsteps pro Step
Alpha = -faktor * xData1 + deltaAlpha
theta = 0.222 
Lambda = (np.sin(Alpha + theta) + np.sin(Alpha)) / 1200 * 1e6

  
# If the plot area needs to be restricted, please enable this area.
xmin, xmax = 200, 900
ymin, ymax = 0,0.6
# mask = (Lambda >= xmin) & (Lambda <= xmax)
#
# restricted values
# xData1 = xData1[mask]
# yData1 = yData1[mask]
# xData2 = xData2[mask]
# yData2 = yData2[mask]
# Lambda=Lambda[mask]
# End of the restriction
 

plt.close('all')

# --- Vorbereitung der Daten (bleibt gleich) ---
yData2_trans = yData2 / yData1
yData2_abs = -np.log10(yData2_trans)

# --- Plot 1: Original Data ---
plt.figure(figsize=(8, 5))
plt.plot(Lambda, yData1, label='Background')
plt.plot(Lambda, yData2, label='Sample')
plt.xlabel('$\lambda$ / nm')
plt.ylabel('Intensity')
plt.xlim(xmin, xmax)
plt.legend()
plt.tight_layout()

plt.show() # Öffnet das erste Fenster

# --- Plot 2: Transmission ---
plt.figure(figsize=(8, 5))
plt.plot(Lambda, yData2_trans, color='black')
plt.xlabel('$\lambda$ / nm')
plt.ylabel('Transmission')
plt.tight_layout()
plt.xlim(xmin, xmax)

plt.show() # Öffnet das zweite Fenster

# --- Plot 3: Absorption ---
plt.figure(figsize=(8, 5))
plt.plot(Lambda, yData2_abs, label='Sample', color='black')
plt.xlabel('$\lambda$ / nm')
plt.ylabel('Absorption (A)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.xlim(xmin, xmax)

plt.show() # Öffnet das dritte Fenster

# --- Export-Teil (CSV-Dateien schreiben) ---
# ... (bleibt wie in deinem ursprünglichen Code)