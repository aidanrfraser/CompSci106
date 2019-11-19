from cisc106 import assertEqual
#working with Ben
def reverse(alist):
    """
    Reverses a list
    """
    if not alist:
        return alist
    else:
        return reverse(alist[1:]) + [alist[0]]
        
assertEqual(reverse([1, 2, 3]), [3, 2, 1])
assertEqual(reverse([0, 1, 0]), [0, 1, 0])
assertEqual(reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])