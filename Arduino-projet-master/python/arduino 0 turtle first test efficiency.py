import turtle as turtle
import math
#import random
import time
import numpy


## Setting the variables
delay_turtle= 0.01
maxcount= 7
nb_of_captors= 1
total_squares= 9

## Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
#wn.bgpic("IMAGEEE")
wn.tracer(3)

## Creating the turtles
turtles=[[0,0,0],[0,0,0],[0,0,0]]
for x in range(3):
    for y in range(3):
        t=turtle.Turtle()
        t.penup()
        t.shape("square")
        t.shapesize(9,9)
        t.setposition(-200+x*200,-200+y*200)
        turtles[x][y]= t

## Defining the color changing function
def color_turtle(nb,t):
    """ Input: Takes in a number that corresponds to a color and a turtle
        Function: Changes the color of that turtle
        """
    if nb == 0:
        t.color("white")
    else:
        t.color("red")
    
## Creating the list with clor changing data
ll=[[[1,1,0],[0,0,1],[1,1,1]],[[0,0,0],[0,0,1],[1,1,1]],[[1,1,0],[1,1,1],[1,1,1]],[[1,1,0],[0,1,1],[1,1,1]],[[1,0,1],[0,0,1],[1,1,1]],[[1,0,0],[0,0,1],[1,0,1]],[[0,1,0],[1,1,1],[1,0,1]]]
l=numpy.zeros((maxcount,3,3))
print(l)
    
    
    
    
## Loop that changes the colors of the turtles
start=time.time()

count=0
while count < maxcount:
    time.sleep(delay_turtle)     #delay between each full refresh (every square changed once)
    for x in range(3): 
        for y in range(3):
            color_turtle(ll[count][x][y],turtles[x][y])
            """
            print("x= ",x,"y= ",y,"count= ",count)
            print("ll[count][x][y](data value for color change)= ",ll[count][x][y])          #les prints
            
        print("\n")"""
    count+=1
    
end= time.time()


## Print perfomance
total_time= end-start
print()
print("Time for program: %ss" % (total_time),"for a %ss delay between refreshes" % (delay_turtle),"and for %s refreshes" % maxcount)
time_per_refresh= (total_time)/len(ll)
print("Time per refresh: %ss" % (time_per_refresh) )
print("Time taken by python per refresh: %ss" % (time_per_refresh - delay_turtle) )

            

wn.mainloop()


