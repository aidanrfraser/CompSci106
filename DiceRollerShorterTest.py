import random
def No():
    """
    Runs if any answer is no
    """
    run = input("Disappointing. I thought you were better than this. Are you sure about your decision? ")
    if run == 'no':
        print("Let's play then.")
        DiceRoll()
    else:
        print("You're the worst.")
def add(x, y):
    """
    Adds x and y
    """
    return x + y
def Roller():
    """
    The brains of the program, creates random integers and does number processing
    """
    d1 = random.randint(1, 6)
    print(d1)
    d2 = random.randint(1, 6)
    print(d2)
    print("The sum of the dice is ", add(d1,d2))
    if d1 == d2:
        print("You got doubles!")
    yess = input("Type y to roll again! ")
    Roller() if yess == 'y' else No()
def DiceRoll():
    """
    Asks if you would like to roll the dice
    """
    yess = input("Roll the dice? (y/n) ")
    Roller() if yess == 'y' else No()
run = input("Would you like to play a game? ")
# Runs on startup, will take many forms of yes to initiate the dice roller
if run == 'yes':
    DiceRoll()
elif run == 'y':
    DiceRoll()
elif run == 'ye':
    DiceRoll()
elif run == 'yeah':
    DiceRoll()
elif run == "sure":
    DiceRoll()
else:
    No()