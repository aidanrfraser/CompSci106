num = 3
#don't do this pls
#don't use global variables unless ya gotta
def add(x, y):
    """
    adds 2 numbers
    """
    return x + y + num
    
def addd(x, y):
    """
    adds 2 numbers
    """
    num = 5 #this is much better
    return x + y + num
    
def adddd(x, y):
    """
    adds 2 numbers
    """
    global num #changes things outside your function
    num = 5
    return x + y + num
    
def returnTwoValues():
    """
    returns 2 values
    """
    return 3, 4 #implies parentheses
    
#(a, b) = returnTwoValues()
#a returns as 3
#b returns as 4
#(4, 5, 5, 6, 7, 8) is a tuple
#immutable