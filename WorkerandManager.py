from cisc106 import assertEqual
#working with Neel
def worker(num):
    """
    Multiplies a single parameter by 2
    """
    return num * 2
    
def manager(fcn, number):
    """
    Runs a function on a parameter
    """
    return fcn(number)
    
#tests
assertEqual(worker(4), 8)
assertEqual(worker(0), 0)
assertEqual(worker(17), 34)
assertEqual(manager(worker, 2), 4)
assertEqual(manager(worker, 0), 0)
assertEqual(manager(worker, -1), -2)