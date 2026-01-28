#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 21:13:32 2025

@author: dominik
"""


###########################
##### Here to change
###########################

number_of_steps = -4000
stepper_motor_speed = 500

###########################
###########################



















import serial
import time

def send_raw_repl(ser, code):
    ser.write(b'\x03')  # CTRL-C Stop
    #time.sleep(0.1)
    ser.write(b'\x01')  # CTRL-A Raw REPL
    #time.sleep(0.1)
    ser.write(code.encode('utf-8') + b'\x04')  # Sende Code + CTRL-D (EOF)
    #time.sleep(0.3)
    ser.write(b'\x02')  # CTRL-B zurück zur normalen REPL


ser = serial.Serial('COM3', 115200, timeout=1)


code = """
from stepper import Stepper
from machine import Pin

EN = Pin(18, Pin.OUT)
MS1 = Pin(19, Pin.OUT)
MS2 = Pin(20, Pin.OUT)
MS3 = Pin(21, Pin.OUT)
RST = Pin(13, Pin.OUT)
SLP = Pin(12, Pin.OUT, Pin.PULL_UP)
STEP = Pin(11, Pin.OUT)
DIR = Pin(10, Pin.OUT)

#Max Auflösung
MS1.on()
MS2.on()
MS3.on()

# Alles an
RST.on()
SLP.on()

TARGET = %i
STEPPER_SPEED = %i

s1 = Stepper(11,10,EN,steps_per_rev=1,speed_sps=4000)
TARGET = int(TARGET)
STEPPER_SPEED = int(STEPPER_SPEED)

EN.off()	#off ist an

s1.speed(STEPPER_SPEED)
s1.target(TARGET)

""" % (number_of_steps, stepper_motor_speed)


response = send_raw_repl(ser, code)


ser.close()