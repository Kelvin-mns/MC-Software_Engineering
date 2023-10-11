import random

secret_number = random.randint(1, 100)
guess = None

while guess != secret_number:
    guess = int(input("GUESS the secret number (between 1 and 100): "))
    if guess < secret_number:
        print("Higher")
    elif guess > secret_number:
        print("Lower")
    else:
        print("correct! the secret number was", secret_number)