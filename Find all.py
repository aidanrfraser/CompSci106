from cisc106 import assertEqual

def findAll(key, alist):
    """
    Finds all instances of key in alist
    """
    result = []
    keyIndex = 0
    for element in alist:
        if element == key:
            result += [keyIndex]
        keyIndex += 1
    return result
    
assertEqual(findAll(1, [1, 1, 1]), [0, 1, 2])
assertEqual(findAll(1, []), [])
assertEqual(findAll(1, [2, 3]), [])