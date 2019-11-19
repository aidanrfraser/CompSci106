#Working with Rohan and Jack
from cisc106 import assertEqual
def average(x, y):
    """
    finds the average of 2 numbers
    """
    return (x + y) / 2

assertEqual(average(2,0),1)
assertEqual(average(5,3),4)
assertEqual(average(10,5),7.5)