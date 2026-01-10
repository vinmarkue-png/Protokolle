def quick_sort(arr):
    # Basisfall: Die Liste ist leer ist oder hat nur ein Element
    if len(arr) <= 1:
        return arr

    # 1. Wahl des Pivot-Elements (mittleres Element)
    pivot = arr[len(arr) // 2]

    # 2. Aufteilen der Liste in drei Teile
    # Elemente < Pivot
    left = [x for x in arr if x < pivot]
    
    # Elemente = Pivot (Duplikate)
    middle = [x for x in arr if x == pivot]
    
    # Elemente > Pivot
    right = [x for x in arr if x > pivot]

    # 3. Rekursiver Aufruf und Zusammenfügen der Ergebnisse
    return quick_sort(left) + middle + quick_sort(right)

#Beispiel
b_liste = [3, 6, 8, 10, 1, 2, 1, 90, 4, 9, 0, -1]
s_liste = quick_sort(b_liste)

print(f"Original: {b_liste}")
print(f"Sortiert: {s_liste}")