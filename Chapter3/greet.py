# reading input
def greet():
	name = input("What's your name?")
	myname = "Peter"

	if name==myname:
		print("That's my name too!")
	else:
		print("Hello, ", name)

greet()