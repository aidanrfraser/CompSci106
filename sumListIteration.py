from cisc106 import assertEqual
#working with Ben
def sum_list_iter(alist, num):
    """
    Finds the sum of alist (parameter 1) and adds it to the state variable (parameter 2)
    """
    if not alist:
        return num
    else:
        return sum_list_iter(alist[1:], num + alist[0])
        
assertEqual(sum_list_iter([5, 6, 7], 0), 18)
assertEqual(sum_list_iter([0, 1, 0], 0), 1)
assertEqual(sum_list_iter([13, 27, 0], 1), 41)