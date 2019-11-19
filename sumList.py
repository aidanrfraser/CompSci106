from cisc106 import assertEqual

def sum_list(alist):
    """
    Sums all elements in a list
    """
    if not alist:
        return 0
    else:
        return alist[0] + sum_list(alist[1:])