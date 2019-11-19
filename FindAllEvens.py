from cisc106 import assertEqual
def evens_n(n):
    """
    Finds all the evens between 0 and n
    """
    alist = []
    for element in range(0, n + 1):
        if element % 2 == 0:
            alist += [element]
    return alist

assertEqual(evens_n(14), [0, 2, 4, 6, 8, 10, 12, 14])
assertEqual(evens_n(0), [0])
assertEqual(evens_n(3), [0, 2])