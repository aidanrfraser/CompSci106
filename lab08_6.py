def myReadFunction(file):
    """
    Opens a file, reads it, and creatse a dictionary
    """
    numbers = {}
    with open(filename) as infile:
        data = infile.readline()
        while data:
            pair = data.split()
            numbers[pair[0]] = pair[1]
            data = infile.readline()
    return numbers