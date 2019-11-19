from cisc106 import assertEqual
def multTable(x):
    """
    Prints a multiplication table for x-1
    """
    for I in range(x):
        for J in range(x):
            print(I * J, end = '')
        print()
        
assertEqual(multTable(0), print(0))