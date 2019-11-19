from cisc106 import assertEqual
#working with Neel
def replace_n(number, replace, alist, n):
    """
    Replaces N amounts of the first parameter in a list with the second parameter
    """
    if not alist or n == 0:
        return alist
    elif number == alist[0]:
        return [replace] + replace_n(number, replace, alist[1:], n - 1)
    else:
        return [alist[0]] + replace_n(number, replace, alist[1:], n)
#tests
assertEqual(replace_n(3, 4, [1, 2, 3, 3, 3, 3, 5], 2), [1, 2, 4, 4, 3, 3, 5])
assertEqual(replace_n(1, 2, [1, 2, 2], 1), [2, 2, 2])
assertEqual(replace_n(-1, 7, [-1, 2, -1, 3], 0), [-1, 2, -1, 3])