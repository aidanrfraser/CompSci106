#Working with Denise and Dylan
from cisc106 import assertEqual
def gridMatch(alist, blist):
    """
    Finds if the string 'x' is located in the same place in nested lists
    """
    for i in range(len(alist)):
        for j in range(len(alist[i])):
            if alist[i][j] == 'x':
                if blist[i][j] != 'x':
                    return False
            if blist[i][j] == 'x':
                if alist[i][j] != 'x':
                    return False
            if 'x' not in blist[i]:
                return False
            if 'x' not in alist[i]:
                return False
    return True
    
assertEqual(gridMatch([[1, 'x'], ['x', 'z']], [[9, 'x'], ['x', 'spam']]), True)
assertEqual(gridMatch([[1, 'x'], ['x', 'z']], [[9, 'x'], ['x', 'x']]), False)
assertEqual(gridMatch([[0], [0]], [[0], [0]]), False)