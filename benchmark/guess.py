#ask the user to guess an integer between 1 and 5

#generate a random integer between 1 and 5

#if the user's guess is wrong, print "your guess is incorrect" and prompt them again but do not generate another random number

#if it is correct, print "your guess is correct"


import random
ans = random.randint(1, 5)
error = True
while error:
    guess = int(input("Guess an integer between 1 and 5, inclusive:\n"))
    if guess == ans: error = False
    else: print(f'Your guess of {guess} is incorrect.')
print(f'Your guess of {guess} is correct.')