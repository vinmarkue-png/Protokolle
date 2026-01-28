import numpy as np                   #Mathe und Arrays
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt      #Plotten



# ### read data from file
#
# p1=r"./data/pure-acid-halfturns.txt"
# p2=r"./data/Ho2O2-acid-halfturns.txt"

# p1=r"./data/lamp.txt"
# p2=r"./data/filter.txt"

p1=r"water2.txt"
# p2=r"./data/KMnO4-DILUTED.txt"
p2=r"kmno4_dünn.txt"
#
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

plt.close('all')   # plt.clf(), plt.vla(), plt.close(), plt(close('all'))  

# --- Plot 1 ---
fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# --- Plot 1: Original Data ---
axs[0].plot(xData1, yData1, label='Background')
axs[0].plot(xData2, yData2, label='Sample')
axs[0].set_title('Original Data')
axs[0].set_xlabel('Steps')
axs[0].set_ylabel('Intensity')
axs[0].legend()

# --- Plot 2: Transmission ---
yData2_trans = yData2 / yData1
axs[1].plot(xData2, yData2_trans, label='Probe')
axs[1].set_title('Transmission')
axs[1].set_xlabel('Steps')
axs[1].set_ylabel('Transmission')
axs[1].legend()

# --- Plot 3: Absorption ---
yData2_abs = -np.log10(yData2_trans)
axs[2].plot(xData2, yData2_abs, label='Probe')
axs[2].set_title('Absorption')
axs[2].set_xlabel('Steps')
axs[2].set_ylabel('Absorption')
axs[2].legend()

plt.tight_layout()
plt.show()

# Write transition
new_filename = p2.replace(".txt", "_trans.csv")
df = pd.DataFrame({"x": xData1, "y": yData2_trans})
df.to_csv(new_filename, index=False)
#
# Write absorption
new_filename = p2.replace(".txt", "_abs.csv")
df = pd.DataFrame({"x": xData1, "y": yData2_abs})
df.to_csv(new_filename, index=False)
#