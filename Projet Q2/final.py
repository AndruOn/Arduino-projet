#--------------------------------------------------------------------------------
# Interface visuelle Turtle avec nombre de capteurs variables
# Plotting des valeurs de chaque capteur
#
# Andru Onciul
#--------------------------------------------------------------------------------


############## IMPORTS ############################################################################################################################################

import turtle as turtle
import time
import numpy as np
from serial import Serial
from color import palette_de_couleurs
from matplotlib import pyplot as plt
from position_point import pospoint

############## Setting the variables ############################################################################################################################################

maxcount= 200
nb_of_captors= 6
port = Serial('COM6', 115200)
nb_dif_colors= 10
colors= palette_de_couleurs(nb_dif_colors)

############## Set up the screen ############################################################################################################################################

wn = turtle.Screen()
wn.bgcolor("white")
wn.colormode(255)
wn.screensize()
wn.setup(width = 1.0, height = 1.0)

############## Grading scale visual ################################################################################################################################################

## Grading scale size
legend_start=(-550,310)
legend_length=1100

## Creating the turtles for grading
for i in range(nb_dif_colors):
    t=turtle.Turtle()
    t.penup()
    t.speed(0)
    t.shape("square")
    t.shapesize(3,3)
    t.color(colors[i])
    t.setposition(legend_start[0]+30 + (legend_length/len(colors))*(i) ,legend_start[1]+57)
    
## Write the values of grading
volt_values=["0 V","1 V","2 V","3 V","4 V","5 V"]
mypen=turtle.Turtle()
mypen.speed(0)
mypen.penup()
mypen.setposition(legend_start)
for i in range(6):
    mypen.write(volt_values[i],False,align="center",font=("Arial black",12,"normal"))
    mypen.forward((legend_length+40)/5)
mypen.hideturtle()

############## Functions ##########################################################################################################################################################

## Defining the color changing function
def color_turtle(nb,t):
    """ Input: Takes in a number that corresponds to a color and a turtle
        Function: Changes the color of that turtle
        """
    if nb == None:
        print("Incorrect value for voltage" )
    elif 0<=nb<=1024:
        t.color(colors[nb * len(colors)//1024])   
    
## Function that reads values from port
def get_reading(port):
    """Reads value on port. Each space(" ") means a new value begins.
        """
    number=""
    while(port.inWaiting() != 0):
        byte=port.read() #on lit un caractère
        car=str(byte)[2:-1]
        if car!= " ":
            number+= car
        else:
            return int(number)
        
############## Setting up the changing color squares ##############################################################################################################################
        
## Creating the turtles that will change colors
t= [0 for i in range(nb_of_captors)]
for i in range(nb_of_captors):
    ## Creating and positioning the turtles
    t[i]=turtle.Turtle()
    t[i].penup()
    t[i].shape("square")
    t[i].shapesize(9,9)
    t[i].color("red")
    x= -200+ (i%3)*200
    y= -280+(i//3)*200 
    t[i].setposition(x,y)
    ## Writing theirs names
    mypen.setposition(x,y+90)
    mypen.write("A%s"%(i),False,align="center",font=("Arial black",14,"bold"))
    #print("turtle n%s position: x: %s  y: %s" % (i,x,y))

############## MAIN LOOP ##########################################################################################################################################################

## Loop that changes the colors of the turtle
start=time.time()

print("-"*30,"Program begins","-"*30)
l= [ np.zeros(maxcount) for i in range(nb_of_captors) ]
count=0
while count < maxcount:
    port.write(b'K')
    dist= np.zeros(nb_of_captors)
    for i in range(nb_of_captors):
        port.write(b'K')
        voltage= get_reading(port)
        color_turtle(voltage,t[i])
        l[i][count]=voltage
        dist[i]=voltage
    print(pospoint(dist))
    #print("A1= ",voltage2,"  A0= ",voltage1,"  count= ",count)
    count+=1

end=time.time()

############## Print messages ##########################################################################################################################################################

## Print perfomance
print("-"*35,"Program performance","-"*35)
total_time= end-start
print("Time for program: %ss" % (total_time)," for %s refreshes" % maxcount)
time_per_refresh= (total_time)/maxcount
print("Time per refresh: %ss" % (time_per_refresh) )
print("-"*91)

############## Plotting ##########################################################################################################################################################

x=np.arange(0,maxcount,1)
for i in range(nb_of_captors):
    liste= l[i]
    plt.subplot( int('33'+str(i+1)) )
    plt.plot(x,liste,'red',label="A%s voltage"%(i))
    plt.ylabel("milliVolt (mV)")
    plt.legend()

mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
plt.show()
wn.mainloop()
