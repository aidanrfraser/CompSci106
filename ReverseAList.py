#HOW TO REVERSE A LIST
alist = [1, 2, 3, 4]
print(alist)
print(alist[::-1])

def reverse(alist):
    """
    Reverses a list in a non mutated way
    """
    print(alist)
    return alist[::-1]
    
def rev(alist):
    """
    Reverses a list in a mutated way
    """
    print(alist)
    blist = alist[::-1]
    for element in range(len(blist)):
        alist[element] = blist[element]
    print(alist)