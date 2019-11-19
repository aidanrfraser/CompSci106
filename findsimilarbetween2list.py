def concatenate(alist, blist):
    """
    Finds similar elements between 2 lists
    """
    for element in alist:
        if element == element in blist:
            return element