def minimum(alist):
    """
    Finds minimum of alist
    """
    if len(alist) == 1:
        return alist[0]
    else:
        minofrest = minimum(alist[1:])
        if alist[0] < minofrest:
            return alist[0]
        else:
            return minofrest
            
def minim(alist):
    """
    Finds minimum of alist
    """
    minsofar = alist[0]
    for element in alist:
        if element < minsofar:
            minsofar = element
    return minsofar