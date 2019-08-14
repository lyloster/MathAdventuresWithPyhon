from math import sqrt

# Solves quadratic equations of the form ax^2 + bx + c = 0
def quad(a, b , c):
	x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
	x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
	print("x1 = ", x1)
	print("x2 = ", x2)
	return x1, x2


quad(2, 7, -15)