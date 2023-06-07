#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    email : openprogramming23@gmail.com
    @author: Exaucé KIMBEMBE / @OpenProgramming
    Created on Mon Dec 20th 2021
    Modifier : 07/06/2023
"""

import pyfirmata as f
import serial
import time

# "COM3" #Windows
# "/dev/ttyACM3" # Linux
# "/dev/tty.usbmodem11401"# Mac

try:
    arduino = f.Arduino("COM5")# Remplacer par le port actif
    i=True
    print("arduino connecté")
except Exception as e:
    raise(e)
    

#void loop()
while i:
    try:    
        arduino.digital[2].write(1)
        arduino.digital[3].write(1)
        time.sleep(0.5)
        arduino.digital[2].write(0)
        arduino.digital[3].write(0)
        time.sleep(0.5)
    except serial.serialutil.SerialException:
        print("Arduino non connecté")
        break