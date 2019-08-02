from turtle import *
from random import randint

shape('turtle')
speed(0)

#turtle wanders on screen, press X to exit
def wander():
	while True:
		#forward
		fd(3)
		#x and y coordintes are from -300 to 300 by default
		if xcor() >= 200 or xcor() <= -200 or ycor() <= -200 or ycor() >= 200:
			#left turn
			#randint generates a random int between 90 and 180 degrees for the turn 
			lt(randint(90,180))


wander()
done()