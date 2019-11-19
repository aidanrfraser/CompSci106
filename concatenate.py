from cisc106 import assertEqual
#Working with Ben
def concatenate(alist,blist):
    """
    Combines 2 lists into one
    """
    if not alist:
        return blist
    elif not blist:
        return alist
    else:
        return concatenate(alist+blist[0:1], blist[1:])
        
assertEqual(concatenate([0,0,0],[1,2,3]), [0,0,0,1,2,3])
assertEqual(concatenate([1,2],[3,4,5]), [1,2,3,4,5])
assertEqual(concatenate([5,6,7],[8,11,13]), [5,6,7,8,11,13])