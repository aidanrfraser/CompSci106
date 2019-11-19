#Working with Rohan and Jack
from cisc106 import assertEqual
def average(x,y):
    return (x+y)/2 #adds both numbers then divides by two

#tests
#The average of 2 and 0 is 1
assertEqual(average(2,0),1)
#The average of 5 and 3 is 4
assertEqual(average(5,3),4)
#The average of 10 and 5 is 7.5
assertEqual(average(10,5),7.5)