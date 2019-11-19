from math import pi

def mult(x,y):
    return x*y
    
def square(x):
    return mult(x,x)
    
def calcCircleArea(r):
    return mult(pi,square(r))
    
def cylinderVolume(r,h):
    return mult(h,calcCircleArea(r))
