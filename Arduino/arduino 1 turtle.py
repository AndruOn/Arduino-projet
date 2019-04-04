import turtle as turtle
import time
import numpy as np
from serial import Serial
from color import palette_de_couleurs
import matplotlib.pyplot as plt


############## Setting the variables ##############

maxcount= 1000
#nb_of_captors= 1
total_squares= 9

nb_dif_colors= 20
colors= palette_de_couleurs(nb_dif_colors)

############## Set up the screen ##############

wn = turtle.Screen()
wn.bgcolor("white")
wn.colormode(255)
wn.screensize()
wn.setup(width = 1.0, height = 1.0)

############## Grading scale visual ##################

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

############## Functions ##############

## Defining the color changing function
def color_turtle(nb,t):
    """ Input: Takes in a number that corresponds to a color and a turtle
        Function: Changes the color of that turtle
        """
    
    if nb == None:
        print("None")
        return 0.1
    elif 0<=nb<=5000:
        t.color(colors[nb * len(colors)//5000])
    else:
        print("Incorrect value for voltage: %s" % nb/1000)
    
## Function that reads values from port
def get_reading(port):
    """Reads value on port. Each space(" ") means a new value begins.
        """
    while(port.inWaiting() == 0):
        time.sleep(0.01)
    number=""
    while(port.inWaiting() != 0):
        # il y a des données !
        byte=port.read() #on lit un caractère
        car=str(byte)[2:-1]
        if car!= " ":
            number+= car
            #print(byte,end="") #on l'affiche
            #print("    ",end="")
            #print(car,end="")
        else:
            #print(number)
            return int(number)
    print("BEUG")
    #time.sleep(0.0002)

############## Setting up the changing color squares ##############
        
## Creating the turtles that will change colors
t=turtle.Turtle()
t.penup()
t.speed(0)
t.shape("square")
t.shapesize(20,20)
t.color("red")

############## MAIN LOOP ##############

## Loop that changes the colors of the turtle
start=time.time()
port = Serial('COM5', 9600)     # jai l'ai bouger des variables
l0=np.zeros(maxcount)
count=0
while count < maxcount:
    #time.sleep(delay_turtle)     #delay between each refresh
    try:
        voltage= int(port.readline().decode('utf-8'))*5000//1023
        l0[count]=voltage
        print(voltage)
        color_turtle(voltage,t)
        count+=1
        if count%10==0:
            print("count= ",count)
    except:
        continue
#print(l0)
end=time.time()

############## Print messages ##############

## Print perfomance
print()
print("-"*35,"Program performance","-"*35)
total_time= end-start
print("Time for program: %ss" % (total_time)," for %s refreshes" % maxcount)
time_per_refresh= (total_time)/maxcount
print("Time per refresh: %ss" % (time_per_refresh) )
print("-"*91)

############## Plotting ##########################################################################################################################################################

x=np.arange(0,maxcount,1)
plt.plot(x,l0,'red',label="A0 voltage")
plt.ylabel("milliVolt (mV)")
plt.legend()
plt.show()



