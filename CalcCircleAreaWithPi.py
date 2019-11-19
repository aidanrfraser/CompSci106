from math import pi

def mult(x, y):
    """
    multiplies two numbers
    """
    return x * y
    
def square(x):
    """
    squares a number
    """
    return mult(x, x)
    
def calcCircleArea(r):
    """
    finds the area of a circle with radius r
    """
    return mult(pi, square(r))