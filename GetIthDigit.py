from cisc106 import assertEqual
#working with Rohan and Jack
def getIthDigit(n,i):
    """
    Finds the digit of the first number that's the second number of digits from the end
    """
    integer = (0 - i)
    n = str(n)
    return int(n[integer])
    
assertEqual(getIthDigit(3410,2),1)
assertEqual(getIthDigit(5678658426786,7),8)
assertEqual(getIthDigit(2,1),2)
assertEqual(getIthDigit(465,3),4)
assertEqual(getIthDigit(40000004,4),0)
assertEqual(getIthDigit(1111111111111,7),1)