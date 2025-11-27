# Gerade/Ungerade
# 1. Zuerst die Funktion definieren
def is_even(number):
    """Check, if a given number is even."""
    # Assertion prüft, ob es ein Integer und >= 1 ist
    assert isinstance(number, int) and number >= 1, "Die gegebene Zahl ist keine positive, natürliche Zahl."
    
    # Rückgabe: True wenn gerade, sonst False
    return number % 2 == 0

# ---------------------------------------------------------

# 2. Danach erst der Hauptteil mit der Eingabe
eingabe_text = input("Bitte gib eine Zahl ein: ")

try:
    zahl = int(eingabe_text)
    
    # Jetzt kennt Python die Funktion 'is_even' von oben
    if is_even(zahl):
        print(f"Die Zahl {zahl} ist gerade.")
    else:
        print(f"Die Zahl {zahl} ist ungerade.")

except ValueError:
    print("Das war keine gültige ganze Zahl!")
except AssertionError as e:
    print(f"Fehler: {e}")

# Summation


# Fakultät
