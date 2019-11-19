#Working with Rohan and Jack
from cisc106 import assertEqual
def close_enough(x, y, z):
    """
    Finds if the difference between x and y is less than or equal to z
    """
    if abs(x - y) <= z:
        return True
    else:
        return False
   
assertEqual(close_enough(0, 5, 5), True)
assertEqual(close_enough(3.5, 4, 1), True)
assertEqual(close_enough(10, 5, 3), False)