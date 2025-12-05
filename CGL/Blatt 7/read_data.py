import matplotlib.pyplot as plt


dateiname = r"C:\Studium\5. Semester\AC II lab\Protokolle\CGL\Blatt 7\messdaten.txt"
x_werte = []
y_werte = []

# 1. Datei öffnen und Schleife über Zeilen
try:
    with open(dateiname, 'r') as datei:
        print(f"Verarbeite Daten aus '{dateiname}'...")
        
        for zeilennummer, zeile in enumerate(datei, 1):
            
            # 2. .strip() verwenden
            bereinigte_zeile = zeile.strip()
            
            # 3. Filtern von leeren Zeilen und Kommentaren
            if not bereinigte_zeile or bereinigte_zeile.startswith('#'):
                # Ignoriert Kommentare
                continue
            
            # 4. Sonst Zeile ausgeben und Werte extrahieren
            # Teile die bereinigte_zeile in Einzelteile auf
            teile = bereinigte_zeile.split() 
            
            if len(teile) == 2:
                try:
                    # Wandelt die Teile in Gleitkommazahlen um
                    x = float(teile[0])
                    y = float(teile[1])
                    
                    # Speicher die Werte in den Listen x_werte und y_werte
                    x_werte.append(x)
                    y_werte.append(y)
                except ValueError:
                    print(f"Warnung in Zeile {zeilennummer}: Konnte Werte nicht in Zahlen umwandeln: '{bereinigte_zeile}'")
            else:
                print(f"Warnung in Zeile {zeilennummer}: Unerwartetes Format (erwarte 2 Werte): '{bereinigte_zeile}'")

except FileNotFoundError:
    print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden.")

# 5. Am Ende alle x-y Werte plotten
if x_werte:
    print(f"Erfolgreich {len(x_werte)} Datenpunkte gesammelt. Erstelle Plot.")
    
    plt.figure(figsize=(10, 6)) 
    
    # plt.scatter() um x_werte gegen y_werte zu plotten
    plt.scatter(x_werte, y_werte, color='red', marker='x', label='Messpunkte')
    

    plt.xlabel('X-Koordinate')
    plt.ylabel('Y-Koordinate')
    #plt.legend() # Zeigt das Label 'Messpunkte' an
    #plt.grid(True)
    
    # Speichern und Anzeigen
    plt.savefig('messdaten_plot.png')
    print("Plot gespeichert als 'messdaten_plot.png'.")
    plt.show()
else:
    print("Keine gültigen Daten zum Plotten gefunden.")