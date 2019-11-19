def closenough(a,b):
    if abs(a-b) < 0.001:
        return abs(a-b)<0.001
def avg(a,b):
    return (a+b)/2
def sqrt(x,y):
    num = y/x
    if closenough(num,x):
        return num
    else:
        sqrt(avg(x,y),y)