from cisc106 import assertEqual
#working with Neel
def isEven(a):
    """
    Returns a number if it is even
    """
    if (a % 2) == 0:
        return [a]
    else:
        return []
        
def filter(fcn, alist):
    """
    Applies a filter function to a list
    """
    if not alist:
        return alist
    else:
        return fcn(alist[0]) + filter(fcn, alist[1:])
#tests