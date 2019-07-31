from turtle import *

shape('turtle')

#for the turn use the external angle which the turtle turns,not the internal
side = 8

def polygon(sidelength=100):
    for i in range(side):
        forward(sidelength)
        right(360/side)

polygon()

