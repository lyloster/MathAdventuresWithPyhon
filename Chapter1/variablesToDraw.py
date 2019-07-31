from turtle import *

shape('turtle')
#speed(0) moves fast, speed(1) moves slower

#making program more robust
#giving default value for sidelength, no errors if sidelength is ommitted
#if sidelength is specified, 100 will be overwritten

def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

speed(0)
square(50)
speed(1)
square(80)
square()
