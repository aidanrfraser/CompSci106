from cisc106 import assertEqual

def states(num, alist):
    """
    Helper for allCombinations that returns state
    """
    state = []
    for element in state:
        state = state + [element + [num]]
    return state
    
def allCombinations(alist):
    """
    Finds all combinations of alist
    """
    if not alist or len(alist) == 1:
        return alist
    else:
        blist = []
        for element in alist:
            blist = blist + states(element, blist) + [[element]]
        return blist
        
assertEqual(allCombinations([]), [])
assertEqual(allCombinations([1]), [1])
assertEqual(allCombinations([1, 2]), [[1], [1,2], [2]])

import timeit
from matplotlib import pyplot
import random

range1 = range(1, 21)
plotlist = list(range1)

dependent = []
for num in range1:
    the_list = plotlist[:num]
    elapsed = timeit.timeit('allCombinations(the_list)', number=100, globals=globals())
    dependent = dependent + [elapsed]
pyplot.plot(range1, dependent, 'b', label = 'All Combinations')

pyplot.title("All Combinations Timing")
pyplot.ylabel("Time in Seconds")
pyplot.xlabel("List Size")
pyplot.legend()
pyplot.savefig("lab07_13.png")
pyplot.show()