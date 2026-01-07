import itertools
import math
import random
import matplotlib.pyplot as plt
import time

def distanz(p1, p2): # Euklidische Distanz berechnen
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def pfad_laenge(pfad): # Gesamtlänge eines Pfades berechnen (Liste von Punkten)
    laenge = 0
    # Iteration von 0 bis zum vorletzten Punkt und Addition der Distanz zum Nachfolger
    for i in range(len(pfad) - 1):
        laenge += distanz(pfad[i], pfad[i+1])
    return laenge

def main():
    n = 10  # Anzahl der Punkte
    random.seed() # Setzt den Seed für reproduzierbare Ergebnisse, ohne Wert ist das Ergebnis für jede Ausführung des Programms unterschiedlich  
    
    # Zufällige Punkte für x und y zwischen 0 und 100 generieren  
    punkte = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]
    
    print(f"Berechne kürzesten Pfad für {n} Punkte...")
    print(f"Zu prüfende Permutationen: {math.factorial(n):,}")
    
    start_time = time.time()

    # Alle Permutationen berechnen und die mit der kürzesten Strecke finden
    kuerzeste_strecke = float('inf')
    bester_pfad = None

    # itertools.permutations erstellt alle möglichen Reihenfolgen
    for perm in itertools.permutations(punkte):
        aktuelle_laenge = pfad_laenge(perm)
        
        if aktuelle_laenge < kuerzeste_strecke:
            kuerzeste_strecke = aktuelle_laenge
            bester_pfad = perm

    end_time = time.time()
    print(f"Fertig in {end_time - start_time:.2f} Sekunden.")
    print(f"Kürzeste Strecke: {kuerzeste_strecke:.2f}")
    
    if bester_pfad:
        # Koordinaten für den Plot entpacken
        x_coords = [p[0] for p in bester_pfad]
        y_coords = [p[1] for p in bester_pfad]

        plt.figure(figsize=(8, 6))
        
        # Weg zeichnen und Punkte anzeigen
        plt.plot(x_coords, y_coords, color='black', linestyle='-', linewidth=2, zorder=1, label='Kürzester Pfad')
        plt.scatter(x_coords, y_coords, color='green', s=100, zorder=2, label='Orte')
        
        # Start- und Endpunkt beschriften
        plt.text(x_coords[0], y_coords[0], ' Start', verticalalignment='bottom', fontweight='bold')
        plt.text(x_coords[-1], y_coords[-1], ' Ende', verticalalignment='bottom', fontweight='bold')

        plt.title(f'Kürzester Pfad durch {n} zufällige Punkte\nLänge: {kuerzeste_strecke:.2f}')
        plt.xlabel('X-Koordinate')
        plt.ylabel('Y-Koordinate')
        plt.grid(True)
        plt.legend()
        plt.savefig("Reisender2.pdf")
        plt.show()

if __name__ == "__main__":
    main()