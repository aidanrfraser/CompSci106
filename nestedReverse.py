from cisc106 import assertEqual
#working with Ben
def nested_reverse(alist):
    """
    Reverses a list, including its nested lists
    """
    if not alist:
        return alist
    elif isinstance(alist[0], list):
        return nested_reverse(alist[1:]) + [nested_reverse(alist[0])]
    else:
        return nested_reverse(alist[1:]) + [alist[0]]
        
assertEqual(nested_reverse([1, 2, 3, [4, 5, 6]]), [[6, 5, 4], 3, 2, 1])
assertEqual(nested_reverse([1, [2, [3, [4]]]]), [[[[4], 3], 2], 1])
assertEqual(nested_reverse([1, 2, 3]), [3, 2, 1])