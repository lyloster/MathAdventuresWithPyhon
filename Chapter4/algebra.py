# first-degree equstions having the general formula ax + b = cx + d

def equation(a, b, c, d):
	# solve algebraically for x
	return (d - b)/(a - c)


x = equation(2, 5, 0, 13)
print("x = ", x)