from turtle import *

shape('turtle')
speed(0)

def star(sidelength = 50):
    for i in range(5):
        forward(sidelength)
        #144 stackOverflow
        right(144)

def starSpiral():
    sidelength = 50
    for i in range(60):
        star(sidelength)
        right(5)
        sidelength += 5


starSpiral()

    
