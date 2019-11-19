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

def count_singles(key, alist):
    """
    Counts numbers if they're not next to themselves
    """
    result = 0
    for x in range(len(alist)):
        if alist[x] == key:
            if not is_next_to(x, alist):
                result += 1
    return result
    
assertEqual(count_singles(1, [1]), 1)
assertEqual(count_singles(2, []), 0)
assertEqual(count_singles(1, [1, 1]), 0)