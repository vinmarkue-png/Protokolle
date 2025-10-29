import pandas as pd
import matplotlib.pyplot as plt

# Pfad zur CSV-Datei
file_path = "converted_file.csv"  # Passe diesen Pfad an, falls nötig

# CSV einlesen
df = pd.read_csv(file_path)

# Plot erstellen
plt.figure(figsize=(10, 5))
plt.plot(df["Wert1"], df["Wert2"], label="Messdaten", linewidth=1)

# Achsenbeschriftungen und Titel
plt.xlabel("Wert1")
plt.ylabel("Wert2")
plt.title("Plot der CSV-Daten")
plt.legend()
plt.grid(True)

# Plot anzeigen
plt.show()