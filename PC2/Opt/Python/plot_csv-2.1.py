import numpy as np                   #Mathe und Arrays
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt      #Plotten



# ### read data

p1=r"./data/KMnO4-DILUTED_abs.csv"
p2=r"./data/KMnO4-HIGH-CONC_abs.csv"
# p3=r"./data/Ho2O2-acid-halfturns_abs.csv"


Data1=pd.read_csv(p1)
Data2=pd.read_csv(p2)
# Data3=pd.read_csv(p3)

xData1 = Data1["x"]; yData1 = Data1["y"]
xData2 = Data2["x"]; yData2 = Data2["y"]
# xData3 = Data3["x"]; yData3 = Data3["y"]

xmin=400; xmax=700

plt.clf()
plt.plot(xData1, yData1, label='dilutet')
plt.plot(xData2, yData2, label='high concentrated')
# plt.plot(xData3, yData3)
plt.legend()
plt.xlim(xmin,xmax)
plt.show()