from turtle import *

#works for starts with odd # of angles
shape('turtle')
speed(0)

def star(n, sidelength = 300):
    for i in range(n):
        forward(sidelength)
        #144 stackOverflow --> perfect angle for a 5-pointed star
        right(180-(180/n))

star(35)
exitonclick()
    
