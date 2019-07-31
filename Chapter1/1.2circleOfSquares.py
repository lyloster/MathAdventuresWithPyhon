from turtle import *

shape('turtle')
#speed(0) moves fast, speed(1) moves slower
speed(0)
def square():
    for i in range(4):
        forward(100)
        right(90)
        
for i in range(60):
    square()
    right(5)


