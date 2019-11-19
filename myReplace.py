from cisc106 import assertEqual
#working with Ben
def my_replace(num, replace, alist):
    """
    Replaces the first instance of the first parameter with the second parameter, in the list (third parameter)
    """
    if num == alist[0]:
        return [replace] + alist[1:]
    else:
        return [alist[0]] + my_replace(num, replace, alist[1:])

assertEqual(my_replace(1, 2, [2,1,3]), [2,2,3])
assertEqual(my_replace(0, 4, [0, 0, 5]), [4, 0, 5])
assertEqual(my_replace(14, 57, [3, 18, 14]), [3, 18, 57])