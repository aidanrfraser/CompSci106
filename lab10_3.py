#Working with Denise and Dylan
from cisc106 import assertEqual
def fits(nlist1, nlist2):
    """
    Tests if a nested list fits into another nested list
    """
    for element1 in range(len(nlist1)):
        for element2 in range(len(nlist1[element1])):
            if nlist1[element1][element2] != nlist2[element1][element2]:
                return True
            else:
                return False
assertEqual(fits([[True, True], [True, True]], [[False, False], [False, False]]), True)
assertEqual(fits([[True, False], [True, False]], [[False, False], [False, False]]), True)
assertEqual(fits([[[], 0], [1, 'hello']], [[True, True], [False, False]]), True)