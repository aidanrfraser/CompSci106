from cisc106 import assertEqual
#working with Neel
def negative(x, y):
    """
    Only returns a number if it is negative
    """
    if x < 0:
        return [x] + y
    else:
        return y
def accumulate(fcn, alist, init):
    """
    Uses functions to accummulate a list
    """
    if not alist:
        return init
    else:
        return fcn(alist[0], accumulate(fcn, alist[1:], init))
#tests