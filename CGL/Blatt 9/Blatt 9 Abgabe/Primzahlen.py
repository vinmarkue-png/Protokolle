N = int(input("N eingeben: "))
gestrichen = [False] * (N + 1) # False = noch Primzahl

# Jede zusammengesetzte Zahl j=a⋅b hat mindestens einen Faktor ≤ √j
for i in range(2, int(N**0.5) + 1): # Hat eine Zahl keinen Teiler ≤ √N, dann ist sie prim
    if not gestrichen[i]: # i ist Primzahl
        print(i, end=", ")
        for j in range(i*i, N + 1, i): # Vielfache streichen
            gestrichen[j] = True

# Restliche Primzahlen ausgeben:
for i in range(int(N**0.5) + 1, N + 1):
    if not gestrichen[i]:
        print(i, end=", ")