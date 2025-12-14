import matplotlib.pyplot as plt
import pandas as pd
import os

# ----------------------------------------------------------------------
# PASSE DIESE VARIABLEN AN:
# ----------------------------------------------------------------------
# 1. Der vollständige Pfad zu dem Ordner, in dem alle drei Dateien liegen.
#    ACHTUNG: Muss der Pfad sein, der bei der Einzeldatei funktioniert hat!
data_directory = r"C:\Users\49157\OneDrive\Dokumente\1. Uni Stuttgart\1.4. PC\1.4.6. PC II Lab\Protokolle\PC2\MDGE\Simulationen\A05\default" # Beispiel

# 2. Liste der Dateinamen Ihrer drei .dat-Dateien
file_names = ['T3V1.dat', 'T3V2.dat', 'T3V3.dat'] # BITTE ANPASSEN!

# 3. Liste der Beschriftungen für die Legende (muss mit der Reihenfolge oben übereinstimmen)
labels = ['T3V1', 'T3V2', 'T3V3']

# 4. Linien-Stile/Farben/Marker für die Plots
line_styles = ['-r', '-b', '-g']

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
        # Daten aus der Datei laden.
        # skiprows=6: Überspringt die 5 Metadatenzeilen UND die Kopfzeile.
        # header=None: Keine automatische Kopfzeilenerkennung.
        # names: Manuelle Zuweisung der bekannten Spaltennamen.
        df = pd.read_csv(
            full_path,
            skiprows=6,
            sep=r'\s+',
            header=None,
            names=column_names,
            engine='python'
        )
        
        # Datenreihe plotten (Temp gegen Vol)
        plt.plot(df['temp'], df['vol'], style, label=label, linewidth=2)

    except Exception as e:
        print(f"WARNUNG: Fehler beim Laden oder Plotten der Datei '{file_name}': {e}. Dieser Datensatz wird übersprungen.")
        continue

# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel(r'reduced temperature')
plt.ylabel(r'$V$ [mL] ')


# Legende anzeigen
plt.legend()

plt.show()
