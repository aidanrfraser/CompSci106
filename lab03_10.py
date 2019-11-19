from cisc106 import assertEqual
#working with Neel
def reverser(alist, y):
    """
    Reverses a list
    """
    return [y] + alist
def accumulate(fcn, alist, init):
    """
    Uses functions to accummulate a list
    """
    if not alist:
        return init
    else:
        return fcn(alist[0], accumulate(fcn, alist[1:], init))
#tests