from cisc106 import assertEqual
def memory(n, m, alist):
    """
    Returns a list with m if either of the two previous elements were n
    """
    if(len(alist) < 2):
        return alist
    value1 = 0
    value2 = 1
    blist = [0] * len(alist)
    for element in range(len(alist)):
        blist[element] = alist[element]
    if alist[0] == n:
        blist[1] = m
    for element in range(2, len(alist)):
        if(alist[value1] == n or alist[value2] == n):
            blist[element] = m
        value1 += 1
        value2 += 1
    return blist
assertEqual(memory(5, 7, [5, 5, 6, 3, 5, 2, 3, 4, 5]), [5, 7, 7, 7, 5, 7, 7, 4, 5])
assertEqual(memory(3, 4, []), [])
assertEqual(memory(3, 4, [3, 5, 6]), [3, 4, 4])