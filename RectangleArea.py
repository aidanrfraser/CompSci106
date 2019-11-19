#Working with Rohan & Jack
from cisc106 import assertEqual
def rectangleArea(l, w):
    """
    Finds area of a rectangle with length l and width w
    """
    return l * w
    
assertEqual(rectangleArea(4,0),0)
assertEqual(rectangleArea(5,5),25)
assertEqual(rectangleArea(10,5),50)