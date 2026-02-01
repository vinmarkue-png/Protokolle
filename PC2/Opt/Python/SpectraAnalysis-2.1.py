#!/usr/bin/env python
# coding: utf-8

# Pakete importieren
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

# ===========================
# BENUTZER-EDITIERBARE VARIABLEN
# ===========================

# Liste aller Dateien, die eingelesen werden sollen
filenames = [
r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\Chloro\chloro_1.txt",
r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\Chloro\chloro_2.txt",
r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\Chloro\chloro_3.txt",
r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\Chloro\chloro_4.txt",
r"C:\Users\49157\OneDrive\Desktop\Protokolle\PC2\Opt\Chloro\chloro_5.txt"
]

# Kalibrierungsparameter
# Bitte passen Sie die Werte entsprechend Ihrer Ergebnisse bei der Kalibrierung an!
f = 0.925
deltaAlpha = 0.593

#########################################
# AB HIER NICHT MEHR BEARBEITEN!
#########################################

# =====================================
# 2) DATEN EINLESEN
# =====================================
# Wir lesen alle Dateien in ein Dictionary:
# Key = Dateiname, Value = (xData, yData)
data_dict = {}
for fname in filenames:
    df = pd.read_csv(fname, skiprows=0, delimiter=' ', header=None)
    xData = df[0].values
    yData = df[1].values
    data_dict[fname] = (xData, yData)

theta = 0.222
# =====================================
# 3) ROHDATEN SPEICHERN & PLOTTEN (SCHRITTZAHL)
# =====================================
# Wir gehen davon aus, dass alle Dateien die gleiche Schritt-Skala haben.
# Dann nehmen wir für die CSV die Schrittachse der ersten Datei als "Hauptachse".
first_file = filenames[0]
xData_first, yData_first = data_dict[first_file]

# Dictionary für Rohdaten-CSV
# Erste Spalte: "Step" (also Schrittzahl)
rohdaten_dict = {"Step": xData_first}

# Jetzt fügen wir pro Datei eine Spalte hinzu
# mit der Überschrift = Dateiname (z. B. "Beispiel1.txt").

# for fname, (xData, yData) in data_dict.items():
#     rohdaten_dict[fname] = yData

# Änderung für den Fall, dass die Datensätze nicht alle gleich lang sind
for fname, (xData, yData) in data_dict.items():
    # Falls Länge unterschiedlich ist: Interpolieren
    if len(xData) != len(xData_first) or not np.allclose(xData, xData_first):
        interp_func = interp1d(xData, yData, kind='linear', fill_value='extrapolate')
        yData_interp = interp_func(xData_first)
    else:
        yData_interp = yData
    rohdaten_dict[fname] = yData_interp

### Ende der Änderung



# DataFrame daraus bauen und speichern
df_roh = pd.DataFrame(rohdaten_dict)
df_roh.to_csv("Rohdaten.csv", index=False, sep=';', decimal=',')

# Plot der Rohdaten (Schrittzahl vs. Intensität)
plt.clf()

plt.figure()
plt.title("Rohdaten in Schrittzahl")
plt.xlabel("Schrittzahl")
plt.ylabel("Intensität (arb.u.)")

for fname, (xData, yData) in data_dict.items():
    plt.plot(xData, yData, label=fname)
plt.legend()


# =====================================
# 4) WELLENLÄNGE BERECHNEN & SPEICHERN
# =====================================
# Zur Umrechnung Schrittzahl -> Wellenlänge
# verwenden wir die Achse der ERSTEN Datei (xData_first) und
# rechnen einmal "Lambda" aus. Anschließend wird diese Lambda-Achse
# für alle Dateien genommen (Annahme: identischer Schritt-Aufbau).

faktor = (1.8 / (20*16) * np.pi/180) * f
Alpha = -faktor * xData_first + deltaAlpha
Lambda = (np.sin(Alpha + theta) + np.sin(Alpha)) / 1200 * 1e6  # in nm

# Dictionary für Auswertung-CSV
auswertung_dict = {"Wavelength": Lambda}

# Wir haben keine Referenz -> kein Transmission/Absorption.
# Wir speichern deshalb lediglich die Intensitäten als Funktion der Wellenlänge.
# for fname, (xData, yData) in data_dict.items():
#     auswertung_dict[fname] = yData
    
# Änderung für den Fall, dass die Datensätze nicht alle gleich lang sind
for fname, (xData, yData) in data_dict.items():
    # Falls Länge unterschiedlich ist: Interpolieren
    if len(xData) != len(xData_first) or not np.allclose(xData, xData_first):
        interp_func = interp1d(xData, yData, kind='linear', fill_value='extrapolate')
        yData_interp = interp_func(xData_first)
    else:
        yData_interp = yData
    auswertung_dict[fname] = yData_interp

### Ende der Änderung


# DataFrame und CSV
df_ausw = pd.DataFrame(auswertung_dict)
df_ausw.to_csv("Auswertung Daten.csv", index=False, sep=';', decimal=',')

# Plot der verarbeiteten Daten (Wellenlänge vs. Intensität)
plt.figure()
plt.title("Rohdaten in Wellenlänge")
plt.xlabel("Wellenlänge (nm)")
plt.ylabel("Intensität (arb.u.)")



for fname, (xData, yData) in data_dict.items():
    Alpha = -faktor * xData + deltaAlpha
    Lambda = (np.sin(Alpha + theta) + np.sin(Alpha)) / 1200 * 1e6  # in nm
    plt.plot(Lambda, yData, label=fname)
    
plt.legend()
plt.show()


# =====================================
# 5) OPTIONAL: PLOTS ANZEIGEN/SPEICHERN
# =====================================
# plt.show()
# plt.savefig("alle_plots.png")

