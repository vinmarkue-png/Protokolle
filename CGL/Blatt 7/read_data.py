import matplotlib.pyplot as plt

dateiname = "messdaten.txt"
x_werte = []
y_werte = []

# 1. Datei öffnen und Schleife über Zeilen
with open(dateiname, 'r') as datei:
    print(f"Verarbeite Daten aus '{dateiname}'...")
    
    for zeilennummer, zeile in enumerate(datei, 1):
        
        # 2. .strip() verwenden
        bereinigte_zeile = zeile.strip()
        
        # 3. Filtern von leeren Zeilen und Kommentaren
        if not bereinigte_zeile or bereinigte_zeile.startswith('#'):
            # Ignoriere auch Zeilen, die mit '#' (Kommentar) beginnen
            continue
        
        # 4. Sonst Zeile ausgeben und Werte extrahieren
        print(f"Verarbeite: '{bereinigte_zeile}'")
        
        #Teile die bereinigte_zeile in Einzelteile auf
        teile = # DEIN CODE HIER
        
        if len(teile) == 2:
            # Wandel die Teile in Gleitkommazahlen um
            x = # DEIN CODE HIER
            y = # DEIN CODE HIER
            
            # Speicher die Werte in den Listen x_werte und y_werte
            # DEIN CODE HIER
            # DEIN CODE HIER


# 5. Am Ende alle Tupel x-y plotten
if x_werte:
    print(f"Erfolgreich {len(x_werte)} Datenpunkte gesammelt. Erstelle Plot.")
    
    plt.figure()
    # Verwende Sie plt.scatter() um x_werte gegen y_werte zu plotten
    # DEIN CODE HIER
    
    plt.title('Messdaten aus Datei')
    plt.xlabel('X-Koordinate')
    plt.ylabel('Y-Koordinate')
    plt.grid(True)
    plt.savefig('messdaten_plot.pdf')
    plt.show()
else:
    print("Keine gültigen Daten zum Plotten gefunden.")