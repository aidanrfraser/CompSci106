from cisc106 import assertEqual
def contains(key, alist):
    """
    Returns True if key is in alist
    """
    for x in alist:
        if x == key:
            return True
    return False
    
assertEqual(contains(1, [1, 1, 2, 3, 4, 5, 1]), True)
assertEqual(contains('d', ['a', 'b', 'c']), False)
assertEqual(contains(4, []), False)