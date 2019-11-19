#Working with Rohan and Jack
from cisc106 import assertEqual
def close_enough(x,y,z):
    if abs(x-y) <= z:
        return True #returns True if the absolute value of x-y is less than or equal to z
    else:
        return False #returns False if the absolute value of x-y is greater than or equal to z
    
#The absolute value of the difference between 5 and 0 is equal to 5, therefore True    
assertEqual(close_enough(0,5,5),True)
#The absolute value of the difference between 3.5 and 4 is less than 1, therefore True
assertEqual(close_enough(3.5,4,1),True)
#the absolute value of the difference between 10 and 5 is greater than 3, therefore False
assertEqual(close_enough(10,5,3),False)