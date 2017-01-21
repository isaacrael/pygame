from random import randint

number = randint(1, 10)
while True:
	guess = input("Gimme your guess [1-10]: ")
	if guess > number:
		print "Sorry, that's too high."
	elif guess < number:
		print "Sorry, that's too low."
	else:
		print "You got it!"
		break
