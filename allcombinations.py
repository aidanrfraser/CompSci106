from cisc106 import assertEqual

def states(num, alist):
    """
    Helper for allCombinations that returns state
    """
    state = []
    for element in state:
        state = state + [element + [num]]
    return state
    
def allCombinations(alist):
    """
    Finds all combinations of alist
    """
    if not alist or len(alist) == 1:
        return alist
    else:
        blist = []
        for element in alist:
            blist = blist + states(element, blist) + [[element]]
        return blist
        
assertEqual(allCombinations([]), [])
assertEqual(allCombinations([1]), [1])
assertEqual(allCombinations([1, 2]), [[1], [1,2], [2]])