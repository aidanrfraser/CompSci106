from cisc106 import assertEqual
#working with Neel
def replace_all(num, replace, alist):
    """
    Replaces all instances of the first parameter in a list with the second parameter
    """
    if not alist:
        return alist
    elif num == alist[0]:
        return [replace] + replace_all(num, replace, alist[1:])
    else:
        return [alist[0]] + replace_all(num, replace, alist[1:])

assertEqual(replace_all(2, 4, [1, 2, 3, 2]), [1, 4, 3, 4])
assertEqual(replace_all(0, 1, [2, 2, 3]), [2, 2, 3])
assertEqual(replace_all(17, 1, [17, 17, 17]), [1, 1, 1])