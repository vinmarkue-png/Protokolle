import numpy as np                   #Mathe und Arrays
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt      #Plotten



# ### read data from file
 # "./data/WATER.txt",
 # "./data/KMnO4-DILUTED.txt"
#
p1=r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\Opt\Holm\HNO3_6-turns.txt"
p2=r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\Opt\Holm\HNO3_Holm_6-turns.txt"
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
# xmin, xmax = 350, 670
xmin, xmax = 400, 800
# mask = (Lambda >= xmin) & (Lambda <= xmax)
#
# restricted values
# xData1 = xData1[mask]
# yData1 = yData1[mask]
# xData2 = xData2[mask]
# yData2 = yData2[mask]
# Lambda=Lambda[mask]
# End of the restriction
 

plt.close('all')   # plt.clf(), plt.vla(), plt.close(), plt(close('all'))  

# --- Plot 1 ---

fig, axs = plt.subplots(1, 3, figsize=(15, 4), sharex=False)
# axs ist ein Array aus 3 Achsen: axs[0], axs[1], axs[2]

# --- Plot 1: Original Data ---
axs[0].plot(Lambda, yData1, label='Background')
axs[0].plot(Lambda, yData2, label='Sample')
axs[0].set_title('Original Data')
axs[0].set_xlabel('Lambda / nm')
axs[0].set_ylabel('Intensity')
axs[0].legend()
axs[0].set_xlim(xmin,xmax)

# --- Plot 2: Transmission ---
yData2_trans = yData2 / yData1
axs[1].plot(Lambda, yData2_trans, label='Sample')
axs[1].set_title('Transmission')
axs[1].set_xlabel('Lambda / nm')
axs[1].set_ylabel('Transmission')
axs[1].legend()
axs[1].set_xlim(xmin,xmax)

# --- Plot 3: Absorption ---
yData2_abs = -np.log10(yData2_trans)
axs[2].plot(Lambda, yData2_abs, label='Sample')
axs[2].set_title('Absorption')
axs[2].set_xlabel('Lambda / nm')
axs[2].set_ylabel('Absorption')
axs[2].legend()
axs[2].set_xlim(xmin,xmax)
axs[2].grid()
plt.tight_layout()
plt.show()

# Write transition
new_filename = p2.replace(".txt", "_trans.csv")
df = pd.DataFrame({"x": Lambda, "y": yData2_trans})
df.to_csv(new_filename, index=False)
#
# Write absorption
new_filename = p2.replace(".txt", "_abs.csv")
df = pd.DataFrame({"x": Lambda, "y": yData2_abs})
df.to_csv(new_filename, index=False)
#