# -*- coding: utf-8 -*-
"""
Batch-Auswertung: Differenz zwischen Spline-Minimum und linearem Fit für mehrere Dateien
Ergebnisse werden mit -1 multipliziert und in einer CSV mit Semikolon gespeichert.

@author: Clarissa
"""
import csv
import os
import numpy as np
import pandas as pd
from scipy.interpolate import UnivariateSpline
from scipy.optimize import curve_fit, minimize_scalar

# Pfad zum Ordner mit allen .dat-Dateien
folder_path = r"C:\Users\49157\OneDrive\Dokumente\1. Uni Stuttgart\1.4. PC\1.4.6. PC II Lab\Protokolle\PC2\Diff\DIFF\ZnSO4"
# Intervall für Minimum der Spline
xmin_interval = 950
xmax_interval = 1050

# Liste für Ergebnisse
results = []

# Alle .dat-Dateien im Ordner durchgehen
for filename in os.listdir(folder_path):
    if filename.endswith(".dat"):
        file_path = os.path.join(folder_path, filename)
        
        # Daten einlesen
        x = []
        y = []
        with open(file_path, "r") as datafile:
            reader = csv.reader(datafile, delimiter=";")
            next(reader)  # Kopfzeile überspringen
            for row in reader:
                x.append(int(row[0]))
                y.append(int(row[1]))
        
        # DataFrame vorbereiten
        df = pd.DataFrame({"x": x, "y": y})
        df = df.groupby("x").mean().reset_index()
        df = df.sort_values("x")
        
        # Bereiche ausschneiden
        mask1 = (df["x"] >= 732) & (df["x"] <= 991)
        mask2 = (df["x"] >= 1150) & (df["x"] <= 1220)
        combined_mask = ~(mask1 | mask2)
        df_filtered = df[combined_mask].reset_index(drop=True)
        
        # Linearer Fit
        def linear_fit(x, m, b):
            return m * x + b
        
        popt, _ = curve_fit(linear_fit, df_filtered["x"], df_filtered["y"], p0=[-30, -50])
        
        # Spline-Glättung
        spl = UnivariateSpline(df["x"], df["y"], k=3, s=500)
        
        # Minimum der Spline im Intervall bestimmen
        res = minimize_scalar(spl, bounds=(xmin_interval, xmax_interval), method='bounded')
        x_min = res.x
        y_min = res.fun
        
        # Wert der linearen Fit-Funktion am Minimum
        y_linear_at_min = linear_fit(x_min, *popt)
        
        # Differenz und mit -1 multiplizieren
        delta_y = -1 * (y_min - y_linear_at_min)
        
        # Ergebnis speichern
        results.append({"Datei": filename, "Delta_y": delta_y})

# Ergebnisse als DataFrame
results_df = pd.DataFrame(results)

# Ergebnisse als CSV mit Semikolon speichern
results_df.to_csv(os.path.join(folder_path, "Differenz_Spline_Linear.csv"),
                  index=False, sep=';')

print("Auswertung abgeschlossen. Ergebnisse in 'Differenz_Spline_Linear.csv'")
print(results_df)
