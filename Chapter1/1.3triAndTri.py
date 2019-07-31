from turtle import *

shape('turtle')

#for the turn use the external angle which the turtle turns,not the internal

def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(120)

speed(0)
triangle(50)

