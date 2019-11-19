from math import pi

def mult(x, y):
    """
    Multiplies 2 numbers
    """
    return x * y
    
def square(x):
    """
    Squares a number
    """
    return mult(x, x)
    
def calcCircleArea(r):
    """
    Calculates area of a circle with radius r
    """
    return mult(pi, square(r))
    
def cylinderVolume(r, h):
    """
    Calculates volume of a cylinder with radius r and height h
    """
    return mult(h, calcCircleArea(r))