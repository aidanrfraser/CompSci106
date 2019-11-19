from cisc106 import assertEqual
#working with Rohan and Jack

def sumSpecials(num1, num2, num3, num4):
    """
    Adds four numbers if they don't fall under the parameters defined in Special
    """
    num = [num1, num2, num3, num4]
    final = 0
    for element in num:
        if element >= 10 and element <=14:
            element = 0
        elif element >= 25 and element <= 29:
            element = 0
        else:
            final = (final + element)
    return final
    
assertEqual(sumSpecials(1, 9, 12, 25), 10)
assertEqual(sumSpecials(3, 5, 7, 9), 24)
assertEqual(sumSpecials(14, 10, 25, 29), 0)