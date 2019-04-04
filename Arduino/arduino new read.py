
    
#!/usr/bin/python3
 # -*-coding:Utf-8 -*

from serial import Serial
import time
import numpy 
from matplotlib import pyplot as plt

nbofvalues=100
port = Serial('COM5', 9600,timeout=1)
count=0






"""
start1=time.time()
#port = Serial("COM5", 9600)
while count < nbofvalues:
     cc=str(port.readline())
     print(cc[2:-5])
     count+=1
end1=time.time()
"""

while count < nbofvalues:
    # using ser.readline() assumes each line contains a single reading
    # sent using Serial.println() on the Arduino
    reading = port.readline().decode('utf-8')
    # reading is a string...do whatever you want from here
    print(reading)
    count+=1




start2=time.time()
#### test que le port est ouvert
if (port.isOpen()):
    print("begin reading")
    while(port.inWaiting() == 0):
        # on attend 0.01 seconde pour que les données arrive
        time.sleep(0.01)

    # si on arrive là, des données sont arrivées
    l= numpy.zeros(nbofvalues)
    print("port full")
    count=0
    while(port.inWaiting() != 0) and count < nbofvalues:
        # il y a des données !
        byte = port.readline()
        print(byte)
        car=str(byte).strip("b\n")
        print(car)
        #l[i]=abs(int(byte))
        count+=1

            
else:
    print ("Le port n'a pas pu être ouvert !")

end2=time.time()
print("Time taken1: %ss" % (end1-start1))
print("Time taken2: %ss" % (end2-start2))
#print(l)

t= numpy.arange(0,nbofvalues,1)
plt.plot(t,l,'-b')
plt.show()
