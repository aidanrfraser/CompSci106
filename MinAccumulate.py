from cisc106 import assertEqual
#working with Neel
def min(a, b):
    """
    Finds the lesser of two numbers
    """
    if a < b:
        return a
    else:
        return b
        
def accumulate(fcn, alist, init):
    """
    Uses functions to accummulate a list
    """
    if not alist:
        return init
    else:
        return fcn(alist[0], accumulate(fcn, alist[1:], init))