from cisc106 import assertEqual
def dec_to_bin(target):
    """
    Converts an integer target to binary
    """
    power = 0
    while 2 ** power <= target:
        power = power + 1
    power = power - 1
    result = ""
    while power >= 0:
        if 2 ** power <= target:
            result = result + "1"
            target = target - 2**power
        else:
            result = result + "0"
        power = power - 1
    return result
    
assertEqual(dec_to_bin(7), bin(7))
assertEqual(dec_to_bin(0), bin(0))
assertEqual(dec_to_bin(567465), bin(567465))