def binsearch(alist, key, start, end):
    """
    Finds a key in alist
    """
    mid = len(alist) // 2
    if start > end:
        return None
    elif start < end:
        return binsearch(alist, key, start, mid-1)
    else:
        return mid