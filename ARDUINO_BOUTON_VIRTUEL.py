#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jan 2022

@author: RACHEL SYSTEME
"""
import tkinter as tk
import pyfirmata as f

#CONNEXION A L'ARDUINO
try:
    arduino = f.Arduino("COM5")
    run     = True
    etat_1  = False
    etat_2  = False
    led_1   = None
    led_2   = None
    already = False
    print("Arduino connecté")
except:
    print("Echec connexion")
    run = False

#GESTION ALLUMAGE DES LEDS
#CONNECTER VOS LEDS AUX PIN 2 ET 3
def gestion_led(index_led):
    global run
    
    if run:
        try:
            global etat_1, etat_2, already, led_1, led_2, bouton_1, bouton_2
                    
            assert index_led == 0 or index_led == 1
            
            #DEFINITION DES PINS COMME SORTIR
            if not already :
                led_1 = arduino.get_pin("d:{}:o".format(2))
                led_2 = arduino.get_pin("d:{}:o".format(3))
                already = True
            
            #ALLUMAGE OU EXTINCTION DE LA LED 1
            if index_led == 0:  
                etat_1 = not etat_1
                led_1.write(etat_1)
                
                #MISE A JOUR DU BOUTON 1
                if etat_1 == True:
                    bouton_1.config(text="LED 1 = ON", bg="yellow")
                else:
                    bouton_1.config(text="LED 1 = OFF", bg="red")
            
            #ALLUMAGE OU EXTINCTION DE LA LED 2
            if index_led == 1:  
                etat_2 = not etat_2
                led_2.write(etat_2)
                
                #MISE A JOUR DU BOUTON 2
                if etat_2 == True:
                    bouton_2.config(text="LED 2 = ON", bg="yellow")
                else:
                    bouton_2.config(text="LED 2 = OFF", bg="red")
                    
        except AssertionError:
            print("gestion_led() prend pour indice 0 ou 1")
        except:
            print("Erreur fonction gestion pin")
   
#FONCTION D'ALLUMAGE OU S'EXTINCTION DE CHAQUE LAMPE         
def led_1():
    gestion_led(0)  
def led_2():
    gestion_led(1)

#CREATION DE L'INTERFACE
if run:           
    #CREATION DE LA FENETRE
    fenetre = tk.Tk()
    fenetre.title("RACHEL SYSTEME")
    fenetre["bg"] = "green"
    fenetre.geometry("400x300")
    fenetre.resizable(width=False, height=False)
    
    #CREATION DES BOUTONS
    bouton_1 = tk.Button(fenetre,text="LED 1 = OFF",width=20,height=4,bg="red",command = led_1)
    bouton_1.pack(pady=50)
    bouton_2 = tk.Button(fenetre,text="LED 2 = OFF",width=20,height=4,bg="red",command = led_2)
    bouton_2.pack()

    fenetre.mainloop()

            
