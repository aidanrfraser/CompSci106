from cisc106 import assertEqual
#Working with Ben
def sum_list(alist):
    """
    Adds numbers in a list
    """
    if not alist:
        return 0
    else:
        return alist[0] + sum_list(alist[1:])

assertEqual(sum_list([1, 2, 3]), 6)
assertEqual(sum_list([0, 3, 14]), 17)
assertEqual(sum_list([0, 1, 0]), 1)