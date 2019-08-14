def average (a,b):
	return (a+b)/2

def squareRoot(number, low, high):
	for i in range(20):
		guess = average(low, high)
		if guess**2 == number:
			print(guess)
			break
		elif guess**2 > number:
			#Guess lower
			high = guess
		else:
			# Guess higher
			low = guess
	print(guess)

squareRoot(60, 7, 8)