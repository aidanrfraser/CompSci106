def closeenough(a, b):
    """
    Finds if 2 numbers are within a close enough range
    """
    if abs(a - b) < 0.001:
        return abs(a - b) < 0.001

def avg(a, b):
    """
    Finds the average of 2 numbers
    """
    return (a + b) / 2

def sqrt(x, y):
    """
    Finds the square root of x with respect to y
    """
    num = y / x
    if closeenough(num, x):
        return num
    else:
        sqrt(avg(x, y), y)