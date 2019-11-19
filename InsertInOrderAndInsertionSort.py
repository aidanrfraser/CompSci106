from cisc106 import assertEqual
def insert_in_order(n, alist):
    """
    Inserts n into its respective place in alist
    """
    if not alist:
        return [n]
    else:
        if n < alist[0]:
            return [n] + alist
        else:
            return alist[0:1] + insert_in_order(n, alist[1:])
            
assertEqual(insert_in_order(1, [2, 3]), [1, 2, 3])
assertEqual(insert_in_order(1, [1, 2, 3]), [1, 1, 2, 3])
assertEqual(insert_in_order(1, []), [1])
            
def insertionSort(alist):
    """
    Sorts alist via instertion
    """
    if not alist:
        return alist
    else:
        return insert_in_order(alist[0], insertionSort(alist[1:]))

assertEqual(insertionSort([3, 2, 1]), [1, 2, 3])
assertEqual(insertionSort([]), [])
assertEqual(insertionSort([1]), [1])