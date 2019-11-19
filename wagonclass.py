class Wagon:
    def __init__(self, wheels, direction):
        """
        location must be greater than or equal to 0
        """
        self.wheels = wheels
        self.location = 0

    def move(self):
        self.location += 1