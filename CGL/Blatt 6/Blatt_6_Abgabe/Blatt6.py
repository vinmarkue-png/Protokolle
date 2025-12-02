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
def get_summation_sq(number):
    """Summiere Quadratzahlen bis N."""
    assert isinstance(number, int) and number >= 1, \
        "Die gegebene Zahl ist keine positive, natürliche Zahl."

    result = 0
    for k in range(1, number + 1):
        result += k**2

    return result

try:
    eingabe_text = input("Gib eine natürliche Zahl N ein: ")
    N = int(eingabe_text)

    # Test: Vergleich zur bekannten Formel S(N) = N(N+1)(2N+1)/6
    assert get_summation_sq(N) == N*(N+1)*(2*N+1)//6

    # Ausgabe
    result = get_summation_sq(N)
    print("Die Summe der Quadratzahlen bis", N, "ist:", result)

except ValueError:
    print("Das war keine gültige ganze Zahl!")
except AssertionError as e:
    print(f"Fehler: {e}")

# Fakultät
def fak(n):
    """Berechne das Produkt aller natürlichen Zahlen von 1 bis n."""
    assert isinstance(n, int) and n >= 0, \
        "Die gegebene Zahl ist keine positive, natürliche Zahl."

    result = 1
    for k in range(1, n + 1):
        result *= k
    return result


try:
    eingabe = input("Gib eine natürliche Zahl n ein: ")
    n = int(eingabe)

    # Fakultät berechnen
    result = fak(n)

    print(f"Die Fakultät von {n} ist: {result}")

except ValueError:
    print("Das war keine gültige ganze Zahl!")
except AssertionError as e:
    print(f"Fehler: {e}")

# e Funktion

def berechne_euler(genauigkeit):
    """Berechnet die Eulersche Zahl e mittels der Potenzreihe.
    Eingabe: Anzahl der Summanden (Iterationen), die berechnet werden."""
    e_approx = 0
    x = 1  # Mit x=1 wird e^1
    
    for k in range(genauigkeit):
        # Die Formel zur Berechnung lautet:(x^k)/k!
        # Da x=1 gilt, ist der Zähler immer 1.
        term = 1 / fak(k) 
        e_approx += term
        
    return e_approx

try:
    eingabe = input("Gib die Anzahl der Iterationen für die Näherung ein: ")
    n_iter = int(eingabe)

    # e berechnen
    e_wert = berechne_euler(n_iter)

    print(f"Näherungswert für e nach {n_iter} Schritten: {e_wert}")

except ValueError:
    print("Bitte gib eine gültige ganze Zahl ein!")
except AssertionError as e:
    print(f"Fehler: {e}")