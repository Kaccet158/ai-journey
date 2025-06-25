import random

secrect_number = random.randint(1, 100)
while True:
    guess = input("Guess? ")
    guess = int(guess)
    if guess < secrect_number:
        print("Too low!")
    elif guess > secrect_number:
        print("Too high!")
    else:
        print("You got it!")
        break