from cisc106 import assertEqual
#working with Neel
def greater_than_five(a, b):
    """
    Returns a number only if it is greater than 5
    """
    if (a > 5):
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