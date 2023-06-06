#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20th 2021

@author: Rachel Système
"""

import pyfirmata as f
import time

# "COM3" #Windows
# "/dev/ttyACM3" # Linux
# "/dev/tty.usbmodem11401"# Mac

try:
    arduino = f.Arduino("COM5")
    i=True
    print("arduino connecté")
except:
    i=False
    print("Arduino non connecté")

#void loop()
while i:
        try:    
            arduino.digital[2].write(1)
            arduino.digital[3].write(1)
            time.sleep(0.5)
            arduino.digital[2].write(0)
            arduino.digital[3].write(0)
            time.sleep(0.5)
        except:
            print("Arduino non connecté")
            break
        
        
        
        
        
        
        