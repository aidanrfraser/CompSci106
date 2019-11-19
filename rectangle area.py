#Working with Rohan & Jack
from cisc106 import assertEqual
def rectangleArea(l,w):
    return l*w #length times width
    
#When multiplying 4 length by 0 width, 0 is recieved due to there being no width.
assertEqual(rectangleArea(4,0),0)
#When multiplying 5 and 5, 25 is recieved due to 5 being both length and width.
assertEqual(rectangleArea(5,5),25)
#When multiplying 10 and 5, 50 is recieved due to 10 being length and 5 being width
assertEqual(rectangleArea(10,5),50)