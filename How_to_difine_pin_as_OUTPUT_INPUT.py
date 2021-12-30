#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 2021

@author: RACHEL SYSTEME
"""

import pyfirmata as f
import time as t

#CONNEXION A L'ARDUINO
try:
    arduino = f.Arduino("COM5")
    print("Arduino connecté")
    run = True
except:
    print("Echec connexion")
    run = False
 
# DEFINITION DES PINS COMME SORTIE
#arduino.get_pin("d:2:o") # DIGITAL OUTPUT
#arduino.get_pin("d:2:i") # DIGITAL INPUT
#arduino.get_pin("P:2:o") # PWM OUTPUT
#arduino.get_pin("a:2:i") # ANALOG  INPUT
if run:   
    led = [arduino.get_pin("d:2:o")]
    led.append(arduino.get_pin("d:3:o"))
    led.append(arduino.get_pin("d:4:o"))
    led.append(arduino.get_pin("d:5:o"))
    led.append(arduino.get_pin("d:6:o"))
 
#PROGRAMME PRINCIPAL
while run:  
    try:  
        for x in range(len(led)):
            led[x].write(1)
            t.sleep(0.5)
            led[x].write(0)
            t.sleep(0.5)
    except:
        print("arduino déconnecté")
        arduino.exit()
        break
