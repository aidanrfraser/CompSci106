from cisc106 import assertEqual
def boolTable():
    """
    Prints a boolean table for p1, p2, and p3
    """
    alist = [True, False]
    print('p1' + '\t' + 'p2' + '\t' + 'p3' + '\t' + 'p1 or (p2 and p3)')
    for p1 in alist:
        for p2 in alist:
            for p3 in alist:
                print(str(p1) + '\t' + str(p2) + '\t' + str(p3) + '\t' + str(p1 or (p2 and p3)))