
    
#!/usr/bin/python3
 # -*-coding:Utf-8 -*

from serial import Serial
import time
import numpy 
from matplotlib import pyplot as plt

nbofvalues=1000
port = Serial('COM5', 9600,timeout=None)
count=0

start=time.time()
#### test que le port est ouvert
if (port.isOpen()):
    print("begin reading")
    while(port.inWaiting() == 0):
        # on attend 0.01 seconde pour que les données arrive
        time.sleep(0.01)

    # si on arrive là, des données sont arrivées
    number=""
    l= numpy.zeros(nbofvalues)
    i=0
    print("port full")
    while(port.inWaiting() != 0) and count<nbofvalues:
        # il y a des données !
        byte = port.read() #on lit un caractère
        car=str(byte).strip("b'")
        if car!= '\n' or car !="\r":
            number+=car
            print(byte) #on l'affiche
            #print("---",end="")
            print(car)
        else:
            print(number)
            print("\n")
            l[i]=abs(int(number))
            number=""
            i+=1
            count+=1
        time.sleep(0.001)
            
else:
    print ("Le port n'a pas pu être ouvert !")

end=time.time()
print(l)

t= numpy.arange(0,nbofvalues,1)
plt.plot(t,l,'-b')
plt.show()
