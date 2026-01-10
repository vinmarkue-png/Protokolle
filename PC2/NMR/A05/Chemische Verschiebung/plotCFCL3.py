import matplotlib.pyplot as plt
import os

# Ermittelt das Verzeichnis, in dem dieses Script liegt
script_dir = os.path.dirname(__file__) 
# Verbindet das Verzeichnis mit dem Dateinamen
file_path = os.path.join(script_dir, 'fluor_ft_pcii_CFCl3.txt')

x, y = [], []

# Jetzt nutzt du 'file_path' statt nur den Dateinamen
with open(file_path, 'r') as datei:
    for _ in range(8):
        next(datei)
    for zeile in datei:
        werte = zeile.split()
        if len(werte) == 2:
            x.append(float(werte[0]))
            y.append(float(werte[1]))


#Achsenbeschriftungen
plt.ylabel("Intensität / %")
plt.xlabel("Freqenz / kHz")

plt.plot(x, y, color = "black")
plt.xlim(-3, 3)
plt.show()