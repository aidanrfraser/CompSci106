def map(fcn, alist):
    """
    Maps another function along alist
    """
    result = []
    for x in alist:
        result = result + [fcn(x)]
    return result
        
def square(x):
    """
    Squares a number
    """
    return x * x