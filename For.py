def map(fcn, alist):
    result = []
    for x in alist:
        result = result + [fcn(x)]
    return result
        
def square(x):
    return x*x
    