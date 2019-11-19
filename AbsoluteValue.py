from cisc106 import assertEqual
#working with Rohan and Jack
def positive(number):
    """
    Finds the absolute value of a number
    """
    if number >= 0:
        return number
    else:
        return (0 - number)
        
assertEqual(positive(-8), 8)
assertEqual(positive(0), 0)
assertEqual(positive(7), 7)