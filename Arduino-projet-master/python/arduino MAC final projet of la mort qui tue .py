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
import matplotlib


############## Setting the variables ############################################################################################################################################

maxcount= 30
nb_of_captors= 9
port = Serial('/dev/tty.usbmodem14501', 9600)
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
        print("None")
    elif 0<=nb<=5000:
        t.color(colors[nb * len(colors)//5000])
    else:
        print("Incorrect value for voltage: %s" % nb/1000)

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
print("-"*30,"Program begins","-"*30)
print()
start=time.time()
l= [ np.zeros(maxcount) for i in range(nb_of_captors)]
count=0
while count < maxcount:
    print("count= ",count)
    for i in range(nb_of_captors):
        try:
            voltage= int(port.readline().decode('utf-8'))*5000//1023
            print("A%s= %sV" % (i,voltage),end="    ")
            color_turtle(voltage,t[i])
            l[i][count]=voltage
        except:
            continue
        
    count+=1
print("-"*30,"End of program","-"*30)
print()
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

"""
x=np.arange(0,maxcount,1)
for i in range(nb_of_captors):
    liste= l[i]
    matplotlib.pyplot.plot(x,liste,'red',label="A%s voltage"%(i))
    matplotlib.pyplot.ylabel("milliVolt (mV)")
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()



wn.mainloop()
"""
