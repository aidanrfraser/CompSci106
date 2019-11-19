from cisc106 import assertEqual
#working with Rohan and Jack
def sumNoDups(num1, num2, num3):
    """
    Finds the sum of 3 numbers, if two are the same they will be ignored. If all 3 are the same it will ignnore all of the numbers and return 0.
    """
    if num1 == num2 == num3:
        return 0
    elif num1 == num2:
        return num3
    elif num1 == num3:
        return num2
    elif num2 == num3:
        return num1
    else:
        return num1 + num2 + num3
        
assertEqual(sumNoDups(3, 3, 3), 0)
assertEqual(sumNoDups(3, 4, 3), 4)
assertEqual(sumNoDups(0, 0, 1), 1)