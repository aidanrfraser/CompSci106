from cisc106 import assertEqual
#working with Ben
def nested_sum(alist):
    """
    Finds the sum of a list even when lists are inside the list
    """
    if not alist:
        return 0
    elif not isinstance(alist, list):
        return alist
    else:
        return nested_sum(alist[0]) + nested_sum(alist[1:])
        
assertEqual(nested_sum([1, 2, 3, [4, 5, 6]]), 21)
assertEqual(nested_sum([1, 2, 3, [0]]), 6)
assertEqual(nested_sum([0, [0, 1, 2]]), 3)