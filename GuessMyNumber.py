import random
def logic(guess):
    """
    Manages the logic for guess_my_number
    """
    attempt = 0
    number = random.randint(1, 101)
    while guess != number:
        if guess > number:
            attempt = attempt + 1
            guess = int(input("Too high! Try again: "))
        elif guess < number:
            attempt = attempt + 1
            guess = int(input("Too low! Try again: "))
    print("You guessed it! It took")
    print(attempt)
    print("guesses!")

def guess_my_number():
    """
    Prompts user to guess a number between 1 and 100
    """
    guess = int(input("Guess a number between 1 and 100: "))
    if isinstance(guess, int):
        logic(guess)
    else:
        print("That's not an integer.")
        guess_my_number()