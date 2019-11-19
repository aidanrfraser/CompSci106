from cisc106 import assertEqual
#working with Neel
def scale_by_five(alist):
    """
    scales all of a list by 5
    """
    if not alist:
        return alist
    else:
        return [(alist[0] * 5)] + scale_by_five(alist[1:])
        
def square(alist):
    """
    square each element of a list
    """
    if not alist:
        return alist
    else:
        return [(alist[0] * alist[0])] + square(alist[1:])
        
def map(fcn, alist):
    """
    uses a function on a list
    """
    if not alist:
        return alist
    else:
        return fcn([alist[0]]) + map(fcn, alist[1:])