from cisc106 import assertEqual
#working with Ben
def pullFromList(number, alist):
    """
    Pulls the nth number from a list
    """
    if not alist or number <= 0:
        return alist[0]
    else:
        return pullFromList(number - 1, alist[1:])
        
assertEqual(pullFromList(0, [1, 2, 3]), 1)
assertEqual(pullFromList(1, [13, 0, 15]), 0)
assertEqual(pullFromList(4, [1, 2, 3, 4, 5]), 5)