while True:
	name = raw_input("Please give me your name: ")

	# We can't have special characters. Spaces are okay, though.
	if not name.replace(' ', '').isalpha():
		print "There's some invalid characters in your name. Sorry. Please try again."
	else:
		break

print "Welcome, {}".format(name)

