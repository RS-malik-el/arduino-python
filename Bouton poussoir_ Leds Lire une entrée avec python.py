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
    
if run:   
    # DEFINITION DES PINS COMME SORTIE
    Bouton = [arduino.get_pin("d:2:i")]
    Bouton.append(arduino.get_pin("d:3:i"))
    Bouton.append(arduino.get_pin("d:4:i"))
    
    # DEFINITION DES PINS COMME ENTREE
    led = [arduino.get_pin("d:5:o")]
    led.append(arduino.get_pin("d:6:o"))
    led.append(arduino.get_pin("d:7:o"))
    
    #ETAT INITIAL DES LEDS
    etat_led1 = False
    etat_led2 = False
    etat_led3 = False
    
    # Start iterator POUR RECEVOIR LES DONNEES
    it = f.util.Iterator(arduino)
    it.start()
    
    
#PROGRAMME PRINCIPAL
while run:  
    try:  
        # LECTURE DES ETATS DES BOUTONS
        etat_b1 = Bouton[0].read()
        etat_b2 = Bouton[1].read()
        etat_b3 = Bouton[2].read()
            
        # CHANGEMENT DES ETATS DES LEDS
        if etat_b1 :
            etat_led1 = not etat_led1
            print("Etat led 1 = ",etat_led1)
                
        if etat_b2 :
            etat_led2 = not etat_led2
            print("Etat led 2 = ",etat_led2)
                
        if etat_b3 :
            etat_led3 = not etat_led3
            print("Etat led 3 = ",etat_led3)
         
        #ALLUMAGE OU EXTINCTION DES LEDS
        led[0].write(etat_led1)
        led[1].write(etat_led2)
        led[2].write(etat_led3)
        
        #temps de pause
        t.sleep(0.100)
            
    except:
        print("arduino déconnecté")
        arduino.exit()
        break

    
