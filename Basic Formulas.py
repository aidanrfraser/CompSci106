def add(x, y):
    """
    Adds 2 numbers
    """
    return x + y
    
def sub(x, y):
    """
    Subtracts 2 numbers
    """
    return x - y
    
def mult(x, y):
    """
    Multiplies 2 numbers
    """
    return x * y
    
def div(x, y):
    """
    Divides two numbers
    """
    return x / y
    
def square(x):
    """
    Squares a number
    """
    return mult(x, x)
    
def negative(x):
    """
    Turns a number negative
    """
    if x > 0:
        return 0 - x
    else:
        return x
    
def quadraticPos(a, b, c):
    """
    Gives positive quadratic answer given a, b, and c
    """
    return div(add(negative(b), root(sub(square(b), mult3(4, a, c)))), mult(2, a))
    
def mult3(a, b, c):
    """
    Multiplies 3 numbers
    """
    return a * b * c
    
def add3(a, b, c):
    """
    Adds 3 numbers
    """
    return a + b + c
    
def quadraticNeg(a, b, c):
    """
    Gives negative answer to the quadratic formula given a, b, and c
    """
    return div(sub(negative(b), root(sub(square(b), mult3(4, a, c)))), mult(2, a))
    
def pythagGiveC(a, b):
    """
    Finds c in the pythagorean theorem given a and b
    """
    return root(add(square(a), square(b)))
    
def pythagGiveAorB(x, c):
    """
    Finds a or b in the pythagorean theorem if you give the other and c
    """
    return root(sub(square(c), square(x)))
    
def hypotTri4590(s):
    """
    Finds hypotenuse of a 45/45/90 triangle given one side
    """
    return mult(s, root(2))
    
def triangleArea(b, h):
    """
    Finds area of a triangle given base and height
    """
    return mult3(.5, b, h)
    
def root(a):
    """
    Finds the square root of a number
    """
    return a ** div(1, 2)
    
def exp(n, power):
    """
    Raises N to the power you give it
    """
    print (n, power)
    if power == 0:
        return 1
    else:
        return n * exp(n, power-1)