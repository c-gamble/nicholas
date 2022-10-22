#ask user to enter a digit between 1 and 3 (inclusive)
num = int(input("Enter a digit between 1 and 3 (inclusive):\n"))
#if they enter 1, print "first"
if num == 1: print("first")
#if they enter 2, print "second"
elif num == 2: print("second")
#if they enter 3, print "third"
elif num == 3: print("third")
#if they enter an invalid input, print "you must enter a number between 1 and 3"
else: print("you must enter a number between 1 and 3")