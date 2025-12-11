import numpy as np
import matplotlib.pyplot as plt

# Erstellt ein Array mit dem Namen data mit 10x10 Nullen
data = np.zeros((10, 10))

# Der Mund:
# x-Bereich geht von 1 bis 6 
# y-Position ist fest auf 3
data[1:7, 3] = 1

# Das linke Auge:
# x-Position ist fest auf 2
# y-Bereich geht von 5 bis 6 
data[2, 5:7] = 1

# Das rechte Auge:
# x-Position ist fest auf 6
# y-Bereich geht von 5 bis 6 
data[6, 5:7] = 1


plt.imshow(data.T, origin='lower')
plt.colorbar()
plt.show()