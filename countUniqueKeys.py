def CountUniqueKeys(alist):
    """
    Creates a dictionary out of the amount of times each unique element appears in alist
    """
    if not alist:
        return {}
    else:
        dictionary = {alist[0]:1}
        unique = True
        unique_elements = [alist[0]]
        for element in alist[1:]:
            unique = True
            for elementA in unique_elements:
                if element == elementA:
                    unique = False
                elif unique:
                    unique_elements += [element]
                    dictionary[element] = 1
                else:
                    dictionary[element] = dictionary[element] + 1
            return dictionary