from cisc106 import assertEqual
def lt(a, b):
    """
    Determines if a is less than b, if so it returns true. otherwise it returns false
    """
    if a < b:
        return True
    else:
        return False
        
assertEqual(lt(2, 4), True)
assertEqual(lt(1, 1), False)
assertEqual(lt(2, 1), False)

def merge(asorted, bsorted):
    """
    Combines 2 lists into 1 sorted list
    """
    if not asorted:
        return bsorted
    elif not bsorted:
        return asorted
    else:
        if lt(asorted, bsorted) == True:
            return [asorted[0]] + merge(asorted[1:], bsorted)
        else:
            return [bsorted[0]] + merge(asorted, bsorted[1:])
            
assertEqual(merge([1, 2], [2, 3]), [1, 2, 2, 3])
assertEqual(merge([1, 2], []), [1, 2])
assertEqual(merge([], [1, 2]), [1, 2])

def mergeSort(alist):
    """
    Merge sorts a list
    """
    if len(alist) <= 1:
        return alist
    else:
        mid = len(alist) // 2
        return merge(mergeSort(alist[:mid]), mergeSort(alist[mid:]))

assertEqual(mergeSort([3, 2, 1]), [1, 2, 3])
assertEqual(mergeSort([]), [])
assertEqual(mergeSort([1, 2, 3]), [1, 2, 3])

import timeit
from matplotlib import pyplot
import random

key = random.randint(1, 1000)
plotlist = list(range(1, 1001))
random.shuffle(plotlist)
plotlist = plotlist[:(len(plotlist) // 2)]
plotlist += [(500 * key)]
random.shuffle(plotlist)

range1 = range(100, 1001, 100)

dependent = []
for num in range1:
    the_list = plotlist[:num]
    elapsed = timeit.timeit('mergeSort(the_list)', number=100, globals=globals())
    dependent = dependent + [elapsed]
pyplot.plot(range1, dependent, 'r', label = 'For Loop (A)')

pyplot.title("Merge Sort Timing")
pyplot.ylabel("Time in Seconds")
pyplot.xlabel("List Size")
pyplot.legend()
pyplot.savefig("lab07_9.png")
pyplot.show()