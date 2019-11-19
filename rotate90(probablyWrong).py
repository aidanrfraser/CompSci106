#working with denise and dylan
from cisc106 import assertEqual
def rotate(m):
    """
    Rotates a matrix 90 degress
    """
    result = [len(m) * [False] for r in range(len(m[0]))]
    for element1 in range(len(m)):
        result[element1] = m[element1][::-1]
    return result

assertEqual(rotate([[1, 2], [3, 4]]), [[2, 1], [4, 3]])
assertEqual(rotate([[1, 2], []]), [[2, 1], []])
assertEqual(rotate([[1], [1]]), [[1], [1]])