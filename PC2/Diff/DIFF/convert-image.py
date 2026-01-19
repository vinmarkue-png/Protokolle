import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Bild einlesen (Pfad zu deinem Bild angeben)
input_filename = r"C:\Users\49157\OneDrive\Dokumente\1. Uni Stuttgart\1.4. PC\1.4.6. PC II Lab\Protokolle\PC2\Diff\DIFF\NaCl\NaCl00002.png"
output_filename = input_filename.replace('.png', '.dat')


image = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)

# Bild binarisieren (Schwarz-Weiß, damit nur die Linie bleibt)
# Annahme: Die weiße Linie hat hohe Intensität, der Hintergrund ist dunkel
_, binary_image = cv2.threshold(image,200, 255, cv2.THRESH_BINARY)

# Finde die Koordinaten der weißen Pixel (also der Linie)
coordinates = np.column_stack(np.where(binary_image == 255))

x=coordinates[:, 1]
y=coordinates[:, 0]



# Sortiere die Werte nach den x-Werten
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]


# Zeige das Bild und die extrahierten Koordinaten
# plt.imshow(binary_image, cmap='gray')
# plt.plot(coordinates[:, 1], coordinates[:, 0])  # Koordinaten plotten
plt.clf()
# plt.plot(x_sorted,-y_sorted)
plt.plot(x_sorted,-y_sorted,ls='',marker='.', markersize=0.5)

plt.show()

# Zeige die extrahierten Koordinaten der Linie

print(coordinates)

# Optional: Koordinaten in einer Datei speichern
df = pd.DataFrame({'x': x_sorted, 'y': -y_sorted})

df.to_csv(output_filename, sep=';', index=False)

