#!/usr/bin/env python
# coding: utf-8

# load packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

# ===========================
# USER-EDITABLE VARIABLES
# ===========================

# Filenames for input data
# Change the names of the files here to use the files you want for calibration
# Make sure the files are located in the same directory as this script
# Ändere diese Zeilen so ab (relativ zum Skript-Standort):
lamp_file = r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\lampe\Lamp2.txt"
bandfilter_file = r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\data\filter.txt"
bandfilter_transmission_file = r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\data\bandfilter-transmission.txt"
# Calibration parameters
# scale: Adjusts the intensity of the transmission spectrum to normalize it
# Recommended range: 1–2 (or as needed)
scale =1.0
# f: Calibration factor, typically between 0.9 and 1.0, used to stretch the spectrum
# Recommended range: 0.85–1.05
f = 0.925

# delta_alpha: Offset for calibration, represents the starting angle, affects resulting wavelength values
# Recommended range: -0.2 to 0.2
deltaAlpha = 0.59


# Filenames for output files
# vergleich_plot_file = 'calibration.pdf'

###################################
# Do not modify code below this line!
###################################

# Read data
Data1 = pd.read_csv(lamp_file, skiprows=0, delimiter=' ', header=None)
Data2 = pd.read_csv(bandfilter_file, skiprows=0, delimiter=' ', header=None)
Data3 = pd.read_csv(
    bandfilter_transmission_file, skiprows=30, delimiter='\t', decimal=',', header=None
)


# Extract arrays
xData1 = Data1[0].values
yData1 = Data1[1].values
xData2 = Data2[0].values
yData2 = Data2[1].values
xData3 = Data3[0].values
yData3 = Data3[1].values


plt.clf()
# (optional) Plot settings for later use
plt.xlabel('Wavelength in nm')
plt.ylabel('Transmission')

# Normalize theoretical bandpass filter spectrum
yRel3 = yData3 / np.max(yData3)

# Extrapolation
f2 = interp1d(xData2, yData2, kind='linear', bounds_error=False, fill_value='extrapolate')
yData2_interploiert = f2(xData1)   # calculates new y-values fitting to xData1
xData2 = xData1                # equals xData2 and xData1
yData2 = yData2_interploiert   # sets yData2 to the interpolated values

# plt.plot(xData1,yData1)
# plt.plot(xData2,yData2)



# Normalize experimental bandpass filter spectrum (correction using lamp data)
yT = yData2 / yData1
yRelT = yT / np.max(yT) * scale

# plt.plot(xData1,yT)
# plt.plot(xData2,yRelT)
# plt.plot(xData3,yData3)

# Conversion: step count -> wavelength (only for experimental spectrum)
faktor = (1.8 / (20*16) * np.pi / 180) * f             #Übersetzung 1/20; 16 Microsteps pro Step
Alpha = -faktor * xData1 + deltaAlpha
theta = 0.222 
Lambda = (np.sin(Alpha + theta) + np.sin(Alpha)) / 1200 * 1e6



# Plots (falls gewünscht)
# plt.plot(xData1, yData1, label='Intensity Lamp')
# plt.plot(xData2, yData2, label='Intensity Sample')
plt.plot(Lambda, yRelT, label='transmission')
plt.plot(xData3, yRel3, label='theo')
plt.legend()
#plt.xlim(400, 900)
#plt.ylim(0, 1)
# plt.savefig(vergleich_plot_file)
plt.show()

