from turtle import *

shape('turtle')

def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)


speed(0)
sidelength = 5

for i in range(60):
    square(sidelength)
    right(5)
    sidelength += 5


    
