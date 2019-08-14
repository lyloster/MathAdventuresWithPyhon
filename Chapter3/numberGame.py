from random import randint

def guessNumber():

	number = randint(1,100)
	print("I am thinking of a number between 1 and 100.")
	guess = int(input("What's your guess?"))

#while the variable guess contains a value, there was no break
	while guess:
		if number == guess:
			print("That's correct! The number was", number)
			break
		elif number> guess:
			print("Nope. Higher.")
		else:
			print("Nope. Lower.")
		guess = int(input("What's your guess?"))


guessNumber()