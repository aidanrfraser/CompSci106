from cisc106 import assertEqual
#working with Rohan and Jack
def distance(Time, IVelocity, Accel):
    """
    Finds distance when you give Time, inital velocity, and acceleration
    """
    return ((IVelocity*Time)+((1/2)*(Accel*(Time*Time))))
    
assertEqual(distance(5,2,4),60)
assertEqual(distance(0,17,30),0)
assertEqual(distance(7,8,0),56)
