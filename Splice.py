from cisc106 import assertEqual
#working with Neel
def lt(a, b):
    """
    Determines if a is less than b, if so it returns true. otherwise it returns false
    """
    if a < b:
        return True
    else:
        return False
        
def splice(asorted, bsorted):
    """
    Combines 2 lists while also sorting them
    """
    if not asorted:
        return bsorted
    elif not bsorted:
        return asorted
    else:
        if lt(asorted, bsorted) == True:
            return [asorted[0]] + splice(asorted[1:], bsorted)
        else:
            return [bsorted[0]] + splice(asorted, bsorted[1:])