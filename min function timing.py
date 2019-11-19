from cisc106 import assertEqual

def min1(alist):
    """ precondition: alist is not empty """
    if len(alist) == 1:
        return alist[0]
    else:
        min_rest = min1(alist[1:])
        if alist[0] < min_rest:
            return alist[0]
        else:
            return min_rest
            
assertEqual(min1([1,2,3]), 1)
assertEqual(min1([2,1,3]), 1)
assertEqual(min1([2,3,1]), 1)

def min2(alist):
    """ precondition: alist is not empty """
    min_so_far = alist[0]
    for elt in alist:
        if elt < min_so_far:
            min_so_far = elt
    return min_so_far
    
assertEqual(min2([1,2,3]), 1)
assertEqual(min2([2,1,3]), 1)
assertEqual(min2([2,3,1]), 1)

def min3(alist):
    """ precondition: alist is not empty """
    def helper(elt, min_of_rest):
            if elt < min_of_rest:
                return elt
            else:
                return min_of_rest
    import functools
    return functools.reduce(helper, alist, alist[0])
            
assertEqual(min3([1,2,3]), 1)
assertEqual(min3([2,1,3]), 1)
assertEqual(min3([2,3,1]), 1)

import timeit
import random

alist = list(range(500))
random.shuffle(alist)

from matplotlib import pyplot
range1 = range(50, 501, 50)

dependent = []
for size in range1:
    short_list = alist[:size]
    elapsed = timeit.timeit('min1(short_list)', number=1000, globals=globals())
    dependent = dependent + [elapsed]
pyplot.plot(range1, dependent, 'b', label = 'min1')

dependent = []
for size in range1:
    short_list = alist[:size]
    elapsed = timeit.timeit('min2(short_list)', number=1000, globals=globals())
    dependent = dependent + [elapsed]
pyplot.plot(range1, dependent, 'y', label = 'min2')

dependent = []
for size in range1:
    short_list = alist[:size]
    elapsed = timeit.timeit('min3(short_list)', number=1000, globals=globals())
    dependent = dependent + [elapsed]
pyplot.plot(range1, dependent, 'g', label = 'min3')

dependent = []
for size in range1:
    short_list = alist[:size]
    elapsed = timeit.timeit('min(short_list)', number=1000, globals=globals())
    dependent = dependent + [elapsed]
pyplot.plot(range1, dependent, 'r', label = 'min')

pyplot.title("Minimum Function Timings")
pyplot.ylabel("Time in Seconds")
pyplot.xlabel("List Size")
pyplot.legend()
pyplot.savefig("lab06_10.png")
pyplot.show()