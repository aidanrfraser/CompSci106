num = 3
#don't do this pls
#don't use global variables unless ya gotta
def add(x, y):
    return x + y + num
    
    
def addd(x, y):
    num = 5 #this is much better
    return x + y + num
    
def adddd(x, y):
    global num #changes things outside your function
    num = 5
    return x + y + num
    
def returnTwoValues():
    return 3, 4 #implies parentheses
    
#(a, b) = returnTwoValues()
#a returns as 3
#b returns as 4
#(4, 5, 5, 6, 7, 8) is a tuple
#immutable
