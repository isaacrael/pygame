while True:
    age = input("Give me your age: ")
    if age <= 0:
        print "NO. That is not possible."
    elif age > 145:
        print "No way. You can't be that old."
    else:
        print "Okay, that works."
        break
    print "Okay. Let's try this again, because {} doesn't work.".format(age)
print "Your age is {}".format(age)
