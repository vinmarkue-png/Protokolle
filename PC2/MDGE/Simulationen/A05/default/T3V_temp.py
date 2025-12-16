import matplotlib.pyplot as plt
import pandas as pd
import os

# ----------------------------------------------------------------------
# PASSE DIESE VARIABLEN AN:
# ----------------------------------------------------------------------
# 1. Der vollständige Pfad zu dem Ordner, in dem alle drei Dateien liegen.
data_directory = r"C:\Users\49157\OneDrive\Dokumente\1. Uni Stuttgart\1.4. PC\1.4.6. PC II Lab\Protokolle\PC2\MDGE\Simulationen\A05\default" # Beispiel

# 2. Liste der Dateinamen Ihrer drei .dat-Dateien
file_names = ['T3V1.dat', 'T3V2.dat', 'T3V3.dat'] # BITTE ANPASSEN!

# 3. Liste der Beschriftungen für die Legende
labels = ['T3 V1', 'T3 V2', 'T3 V3']

# 4. Linien-Stile/Farben/Marker
line_styles = ['-r', '-b', '-g']

# ----------------------------------------------------------------------
# NEU EINGEFÜGT: VARIABLEN FÜR TEMPERATURUMRECHNUNG UND INTERVALL
# ----------------------------------------------------------------------
# 5. UMWANDLUNGSFAKTOR T* -> T (T = T* * C)
conversion_factor_T = 119 # Setzen Sie hier Ihren Faktor ein (z.B. 120.0 für Kelvin)
temp_unit = r'$[\epsilon / k_B]$' # Einheit für die X-Achse, z.B. '[K]' oder '$[\epsilon / k_B]$'

# 6. DEFINITION DES PLOT-INTERVALLS (in der "actual" Einheit, also T)
temp_min = 0 # Untere Grenze des Temperaturbereichs
temp_max = 300  # Obere Grenze des Temperaturbereichs
# ----------------------------------------------------------------------

# Die bekannten Spaltennamen
column_names = ['temp', 'vol', 'pressure', 'time']

# Erstellen einer neuen Plot-Figur
plt.figure(figsize=(10, 6))

# Schleife über alle drei Datensätze
for file_name, label, style in zip(file_names, labels, line_styles):
    # Vollständigen Pfad zusammensetzen
    full_path = os.path.join(data_directory, file_name)

    if not os.path.exists(full_path):
        print(f"FEHLER: Datei nicht gefunden unter: '{full_path}'. Dieser Datensatz wird übersprungen.")
        continue

    try:
        # Daten laden (skiprows=6)
        df = pd.read_csv(
            full_path,
            skiprows=6,
            sep=r'\s+',
            header=None,
            names=column_names,
            engine='python'
        )
        
        # ----------------------------------------------------------------------
        # NEU EINGEFÜGT: BERECHNUNG UND FILTERUNG
        # ----------------------------------------------------------------------
        # 1. Berechnung der tatsächlichen Temperatur
        # Erstellt die neue Spalte 'temp_actual'
        df['temp_actual'] = df['temp'] * conversion_factor_T
        
        # 2. Filtern des DataFrames auf das gewünschte Temperaturintervall
        df_filtered = df[
            (df['temp_actual'] >= temp_min) & (df['temp_actual'] <= temp_max)
        ].copy() 

        if df_filtered.empty:
            print(f"WARNUNG: Keine Daten für {file_name} im Intervall {temp_min} bis {temp_max} gefunden. Datensatz wird übersprungen.")
            continue
            
        # ----------------------------------------------------------------------
        
        # NEU EINGEFÜGT: PLOT MIT GEFILTERTEN DATEN
        # Datenreihe plotten (Temp_actual gegen Vol)
        # Es muss df_filtered und 'temp_actual' verwendet werden
        plt.plot(df_filtered['temp_actual'], df_filtered['vol'], style, label=label, linewidth=2)

    except Exception as e:
        print(f"WARNUNG: Fehler beim Laden oder Plotten der Datei '{file_name}': {e}. Dieser Datensatz wird übersprungen.")
        continue

# ----------------------------------------------------------------------
# NEU EINGEFÜGT: ACHSENBESCHRIFTUNG MIT NEUER EINHEIT
# ----------------------------------------------------------------------
# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel(r'temperature $T$ [K] ') # Verwendet die oben definierte Einheit
plt.ylabel(r'volume $V$ [mL] ')

# Legende anzeigen
plt.legend()

# Plot speichern
plt.show()