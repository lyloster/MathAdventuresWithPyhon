from turtle import *

shape('turtle')

def square(sidelength=5):
    for i in range(4):
        forward(100)
        right(90)


speed(0)
sidelength = 5

#doesn't look like a spiral

for i in range(60):
    square(sidelength)
    right(5)
    sidelength += 5


    
