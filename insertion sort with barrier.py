from cisc106 import assertEqual
def insertionSort(alist):
    """
    Insertion sorts
    """
    for barrier in range(1, len(alist)):
        num = alist[barrier]
        n = barrier - 1
        while n >= 0 and num < alist[n]:
            alist[n + 1] = alist[n]
            n -= 1
        alist[n + 1] = num
    return alist
    
assertEqual(insertionSort([3, 2, 1]), [1, 2, 3])
assertEqual(insertionSort([]), [])
assertEqual(insertionSort([1]), [1])