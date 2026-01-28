# -*- coding: utf-8 -*-
"""
Created on Fri May 23 09:45:12 2025

@author: Spektroskop
"""

###########################
##### Here to change
###########################

number_of_steps = 6000   #Number of Stepper Motor Steps
stepper_motor_speed = 1000  #speed of the stepper motor in steps per s
ADC_speed = 3               # 0: 20 SPS, 1: 45 SPS, 2: 90SPS, 3: 175 SPS 

Saving = 'YES'              # YES or NO
filename = r'HNO3_Holm_6-turns.txt'

# filename = r'Ho2O2-acid-6-bturns.txt'

###########################
###########################





import matplotlib.pyplot as plt
import serial
import numpy as np
from time import sleep

ser = serial.Serial('COM3', 115200, timeout=1)

ser.write(b'from machine import soft_reset\r\n')
print(ser.readline().decode('utf-8'))
ser.write(b'soft_reset()\r\n')
message = ''
while message != '>>> ':
    message = ser.readline().decode('utf-8')
    print(message)

ser.write(b'import Firmware\r\n')
print(ser.readline().decode('utf-8'))
sleep(2)
message = '%s, %s, %s\r\n' % (number_of_steps, stepper_motor_speed, ADC_speed)
ser.write(message.encode())     #Target, Target_Speed, ADC_Speed
print(ser.readline().decode('utf-8'))
print('=======================')

pos = 0
Daten = np.array([])
Positionen = []
while pos != number_of_steps:
    message = ser.readline().decode('utf-8')
    print(message)
    data = message.split(' ')
    pos = int(data[1][:-1])
    volt = float(data[3].split('\r\n')[0])
    Daten = np.append(Daten, volt)
    Positionen = np.append(Positionen, pos)

plt.clf()
plt.plot(Positionen, Daten, 'b')
plt.pause(0.05)
ser.close()

if Saving == 'YES':
    np.savetxt(filename, np.transpose(np.append([Positionen], [Daten], axis=0)))

