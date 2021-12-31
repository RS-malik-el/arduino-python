#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 2021
@author: Admin
"""
import pyfirmata as f

#CONNEXION A L'ARDUINO
try:
    arduino = f.Arduino("COM5")
    print("Arduino connecté")
    run = True
except:
    print("Echec connexion")
    run = False

if run:
    #Bouton = arduino.get_pin("d:2:i")
    Bouton = arduino.digital[2]
    Bouton.mode = f.INPUT
    
    # Start iterator POUR RECEVOIR LES DONNEES
    it = f.util.Iterator(arduino)
    it.start()

#PROGRAMME PRINCIPAL
while run:
    try:
        # LECTURE DE L'ETAT DU BOUTON
        etat_b1 = Bouton.read()
        print(etat_b1)  
    except:
        print("arduino déconnecté")
        arduino.exit()
        break