#working with denise and dylan
from cisc106 import assertEqual
def transpose(m):
    """
    Transposes a matrix m
    """
    result = [len(m) * [False] for r in range(len(m[0]))]
    for element1 in range(len(m)):
        for element2 in range(len(m[0])):
            result[element2][element1] = m[element1][element2]
    return result
    
assertEqual(transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])
assertEqual(transpose([[]]), [])
assertEqual(transpose([[4, 5, 6], [7, 8, 9]]), [[4, 7], [5, 8], [6, 9]])