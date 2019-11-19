def binsearch(alist, key, start, end):
    mid = len(alist)//2
    if start > end:
        return none
    elif start < end:
        return binsearch(alist, key, start, mid-1)
    else:
        return mid