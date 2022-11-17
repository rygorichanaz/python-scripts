import random

print("-----Guess the Number-----")
print("You have 5 attempts to guess the secret number!")
attempts = 5
upperLimit = int(input("What is the upper limit? "))
secretNumber = random.randrange(1, upperLimit)

def checkAttempts(remainingAttempts):
    if (remainingAttempts == 0):
        print("You've run out of attempts.")
        print("The secret number was {}".format(secretNumber))
    return (remainingAttempts == 0)

for i in range(5):
    userGuess = int(input("Guess the secret number: "))
    if (userGuess > secretNumber):
        print("Lower")
        attempts -= 1
        if checkAttempts(attempts):
            break
    elif (userGuess < secretNumber):
        print("Higher")
        attempts -= 1
        if checkAttempts(attempts):
            break
    else:
        print("Correct")
        break
    print("Guesses remaining: {}".format(attempts))