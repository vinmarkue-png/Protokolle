import numpy as np
np.random.seed(42)
data = np.random.rand(100, 2)

# Gibt die gesamte Anzahl aller Elemente aus
anzahl_elemente = data.size
print(f"1. Gesamtanzahl der Elemente: {anzahl_elemente}")

# Gibt das Element aus Zeile 0 und Spalte 1 aus
element_0_1 = data[0, 1]
print(f"2. Element (Zeile 0, Spalte 1): {element_0_1}")

# Gibt die Elemente aus der gesamten letzten Zeile aus
letzte_zeile = data[-1, :]
print(f"3. Die gesamte letzte Zeile: {letzte_zeile}")

# Gibt die Elemente aus der 10. Spalte aus. Fehler: es gibt nur 2 Spalten.
# zehnte_spalte = data[:,9]
# print(f"4. Die Zehnte Spalte: {zehnte_spalte}")

# Definiert einen sub_array von Zeile 50 bis 59 und Spalte 0. Dabei ist zu beachten, dass der Start inklusiv ist, weswegen der Index 50 angegeben ist und das Ende exklusiv ist, weswegen der Index 60 angegeben werden muss, damit der Wert 59 mitinbegriffen ist.
sub_array = data[50:60, 0]
print(f"5. Sub-Array (Zeile 50-59, Spalte 0):\n{sub_array}")

# Berechnet den Mittelwert der Zeilen 50 bis 99 in der Spalte 0.
mean_val = np.mean(data[50:100, 0])
print(f"6. Mittelwert (Zeile 50-99, Spalte 0): {mean_val}")
