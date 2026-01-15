import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Ordner mit den Bildern
base_path = r"C:\Users\49157\OneDrive\Dokumente\1. Uni Stuttgart\1.4. PC\1.4.6. PC II Lab\Protokolle\PC2\Diff\DIFF\ZnSO4"

# Alle PNG-Dateien finden
image_files = sorted(glob.glob(os.path.join(base_path, "*.png")))

print(f"{len(image_files)} Bilder gefunden")

for input_filename in image_files:

    print(f"Verarbeite: {input_filename}")

    output_filename = input_filename.replace(".png", ".dat")

    image = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(" → Fehler beim Einlesen")
        continue

    # Binarisierung
    _, binary_image = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

    # Weiße Pixel finden
    coordinates = np.column_stack(np.where(binary_image == 255))
    if coordinates.size == 0:
        print(" → Keine Linie gefunden")
        continue

    x = coordinates[:, 1]
    y = -coordinates[:, 0]   # y invertieren

    # Nach x sortieren
    idx = np.argsort(x)
    x_sorted = x[idx]
    y_sorted = y[idx]

    # Speichern
    df = pd.DataFrame({'x': x_sorted, 'y': y_sorted})
    df.to_csv(output_filename, sep=';', index=False)

    print(f" → gespeichert: {output_filename}")

print("FERTIG.")
