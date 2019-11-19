from cisc106 import assertEqual
import timeit
import random
from matplotlib import pyplot

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
            
def insertionSort6(alist):
    """
    Sorts alist via insertion
    """
    if not alist:
        return alist
    else:
        return insert_in_order(alist[0], insertionSort6(alist[1:]))
        
assertEqual(insertionSort6([3, 2, 1]), [1, 2, 3])
assertEqual(insertionSort6([]), [])
assertEqual(insertionSort6([1]), [1])

def insertionSort7(alist):
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
    
assertEqual(insertionSort7([3, 2, 1]), [1, 2, 3])
assertEqual(insertionSort7([]), [])
assertEqual(insertionSort7([1]), [1])
    
plotlist = list(range(500))
random.shuffle(plotlist)

range1 = range(100, 501, 50)

dependent = []
for num in range1:
    the_list = plotlist[:num]
    elapsed = timeit.timeit('insertionSort7(the_list)', number = 100, globals = globals())
    dependent = dependent + [elapsed]
pyplot.plot(range1, dependent, 'r', label = 'Constant Space (7)')

dependent = []
for num in range1:
    the_list = plotlist[:num]
    elapsed = timeit.timeit('insertionSort6(the_list)', number = 100, globals = globals())
    dependent = dependent + [elapsed]
pyplot.plot(range1, dependent, 'g', label = 'Number by Number (6)')

pyplot.title("Insertion Sort Timings")
pyplot.ylabel("Time in Seconds")
pyplot.xlabel("List Size")
pyplot.legend()
pyplot.savefig("lab07_8.png")
pyplot.show()