import re
import numpy as np                   # Mathe und Arrays
import pandas as pd
from scipy.optimize import curve_fit   # Fit (hier nicht zwingend)
import matplotlib.pyplot as plt      # Plotten
import matplotlib as mpl
from lmfit import Model, Parameters
import os
base_path = r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\Opt\Holm"

def lorentz(x, pos, amp, gam):
    gam = gam/2.  # for full width at half maximum (FWHM)
    return amp/np.pi * gam / ( gam**2 + (x - pos)**2 )

def multi_lorentz(x, off, slope, **pars):
    total = slope * x + off    
    # nPeaks = 2
    nPeaks = len(pars)//3    
    for i in range(1,nPeaks+1):
        pos_key = f'pos{i}'
        amp_key = f'amp{i}'
        gam_key = f'gam{i}'
        # nur summieren, wenn das Triplet komplett vorhanden ist
        if pos_key in pars and amp_key in pars and gam_key in pars:
            total += lorentz(x, pars[pos_key], pars[amp_key], pars[gam_key])
        # total += lorentz(x, pars[pos_key], pars[amp_key], pars[gam_key])
    return total


# Daten werden eingelesen
# Data = pd.read_csv('./data/Ho2O2-acid-halfturns_trans.csv', skiprows=0, delimiter='\t', header=None)
Data = pd.read_csv(r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\Opt\Holm\HNO3_Holm_1.5-turns_abs.csv", skiprows=0, delimiter=',', header=0)



# x- und y-Spalten werden extrahiert
# Check actual column names: print(Data.columns)
xData, yData = Data.iloc[:, 0], Data.iloc[:, 1]  # Use first two columns
start=400; stop=700
mask = (xData >= start) & (xData <= stop)
xData , yData = xData[mask] , yData[mask]

# Startparameter festlegen
model = Model(multi_lorentz)
params = Parameters()
params.add('off', value=-0.01, vary=True)
params.add('slope', value=0.0, vary=True)
#
# -> Füge hier so viele pos-Werte hinzu, wie du Peaks erwartest.
pos = [461,544,650]   # Anfangspositionen festlegen
amp = 1               # Anfangsamplituden
gamma = 10               # Anfangsbreiten
for i in range(1,len(pos)+1):
    params.add(f'pos{i}', value=pos[i-1])   
    params.add(f'amp{i}', value=amp)
    params.add(f'gam{i}', value=gamma)
 
# -> alle Paremeter fixieren, hilfreich für Tests
# for par in params.values():
#     par.vary = False
# #
# -> oder einzelen Parameter ändern, wenn nötig
# params['pos1', value=350, vary=False]

# ------------ eigentlicher Fit --------------
result = model.fit(yData, params, x=xData, nan_policy='omit')
#

params=result.params
# params['pos1', value=350, vary=True]
# 

# Plot & Report
# result.plot()
# plt.show()
print(result.fit_report())

#--------------------------------------------------------

basis = params['off'].value + params['slope'].value * xData

# Visualisierung
plt.clf()
plt.plot(xData,yData-basis, 'x',label='Exp')
plt.plot(xData,result.best_fit-basis,label='Fit', lw = 2)
#
# zeichne einzelne Peaks
for i in range(1,len(pos)+1):
    yPeak = lorentz(xData, params[f'pos{i}'].value, params[f'amp{i}'].value, params[f'gam{i}'].value)
    plt.plot(xData, yPeak, label=f'Peak{i}')                  # Peaks
#
# plt.title('Holmiumoxide')
plt.xlabel('Lambda / nm')
plt.ylabel('Absorption / a.u.')
plt.legend()
plt.savefig(os.path.join(base_path, "lorentz_1.5.pdf"))
