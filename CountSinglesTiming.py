from cisc106 import assertEqual
def is_next_to(index, alist):
    """
    Finds if a number is next to itself
    """
    if not index == 0 and alist[index - 1] == alist[index]:
        return True
    elif not index >= len(alist) - 1 and alist[index + 1] == alist[index]:
        return True
    else:
        return False
        
assertEqual(is_next_to(1, [1, 2, 3]), False)
assertEqual(is_next_to(1, [1, 1, 5]), True)
assertEqual(is_next_to(1, [2, 2, 1]), True)

def count_singlesA(key, alist):
    """
    Counts numbers if they're not next to themselves with a range
    """
    result = 0
    for x in range(len(alist)):
        if alist[x] == key:
            if not is_next_to(x, alist):
                result += 1
    return result
    
assertEqual(count_singlesA(1, [1]), 1)
assertEqual(count_singlesA(2, []), 0)
assertEqual(count_singlesA(1, [1, 1]), 0)

def count_singlesB(key, alist):
    """
    Counts the appearances of key in alist if key is not next to itself using a state variable
    """
    num = 0
    result = 0
    for element in alist:
        if num == 0 and element == key:
            result += 1
            num = 1
        elif num == 1 and element == key:
            result -= 1
            num += 1
        elif num > 1 and element == key:
            num += 1
        elif element == key:
            num = 1
        else:
            num = 0
    return result
    
assertEqual(count_singlesB(1, [1]), 1)
assertEqual(count_singlesB(2, []), 0)
assertEqual(count_singlesB(1, [1, 1]), 0)

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
    elapsed = timeit.timeit('count_singlesA(key, the_list)', number = 100, globals = globals())
    dependent = dependent + [elapsed]
pyplot.plot(range1, dependent, 'r', label = 'For Loop (A)')

dependent = []
for num in range1:
    the_list = plotlist[:num]
    elapsed = timeit.timeit('count_singlesB(key, the_list)', number = 100, globals = globals())
    dependent = dependent + [elapsed]
pyplot.plot(range1, dependent, 'b', label = 'State Variable (B)')

pyplot.title("Count Singles Timings")
pyplot.ylabel("Time in Seconds")
pyplot.xlabel("List Size")
pyplot.legend()
pyplot.savefig("lab07_10.png")
pyplot.show()