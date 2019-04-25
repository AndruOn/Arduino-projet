
    
#!/usr/bin/python3
 # -*-coding:Utf-8 -*

from serial import Serial
import time
import numpy 
from matplotlib import pyplot as plt

nbofvalues=1000
port = Serial('COM6', 9600)


#### test que le port est ouvert
if (port.isOpen()):
    # demande de la chaîne à envoyer
    chaine = input("Que voulez vous transformer ? ")
    # on écrit la chaîne en question
    port.write(bytes(chaine, 'UTF-8'))
    # attend que des données soit revenues
    while(port.inWaiting() == 0):
        # on attend 0.5 seconde pour que les données arrive
        time.sleep(0.5)

    # si on arrive là, des données sont arrivées
    number=""
    l= numpy.zeros(nbofvalues)
    i=0
    while(port.inWaiting() != 0):
        # il y a des données !
        byte = port.read() #on lit un caractère
        car=str(byte)[2:-1]
        if car!= " ":
            number+=car
            print(byte,end="") #on l'affiche
            print("    ",end="")
            print(car,end="")
        else:
            print("\n")
            print(number)
            
        time.sleep(0.01)
            
else:
    print ("Le port n'a pas pu être ouvert !")

