import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Data1 = pd.read_csv('nvt-out.dat',skiprows=6,delimiter='\t',header=None)
# Data2 = pd.read_csv('nvt-out_1.dat',skiprows=6,delimiter='\t',header=None)
# Data3 = pd.read_csv('nvt_out_2023-09-26-11:29.dat',skiprows=5,delimiter='\t',header=None)
# Data4 = pd.read_csv('nvt_out_2023-10-04-17:35.dat',skiprows=5,delimiter='\t',header=None)
# Data5 = pd.read_csv('nvt_out_2023-10-02-18:53.dat',skiprows=5,delimiter='\t',header=None)


xData1 = Data1[0].values
yData1 = Data1[1].values
# xData2 = Data2[0].values
# yData2 = Data2[1].values
# # xData3 = Data3[0].values
# # yData3 = Data3[1].values
# # xData4 = Data4[0].values
# # yData4 = Data4[1].values
# # xData5 = Data5[0].values
# # yData5 = Data5[1].values


# plt.clf()

plt.plot(xData1,yData1)
# plt.plot(xData2,yData2)
# plt.plot(xData3,yData3)
# plt.plot(xData4,yData4)
# plt.plot(xData5,yData5)



plt.xlabel("Temperatur")
plt.ylabel("Volumen")
#plt.xlim(0.0,2)
# plt.ylim(400,800)
plt.grid(True)
#plt.legend(['20,20','40,40','40,500','40,2000','500,40'])
plt.legend(['40,500','500,40'])
plt.show()